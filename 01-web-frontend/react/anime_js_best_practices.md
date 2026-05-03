---
title: anime.js best practices
url: https://skills.sh/davidosemwegie/animejs-best-practices/anime.js-best-practices
---

# anime.js best practices

skills/davidosemwegie/animejs-best-practices/anime.js Best Practices
anime.js Best Practices
Installation
$ npx skills add https://github.com/davidosemwegie/animejs-best-practices --skill 'anime.js Best Practices'
SKILL.md
anime.js v4 Best Practices

A comprehensive guide for implementing animations with anime.js v4 - the lightweight JavaScript animation engine.

Overview

anime.js v4 provides a powerful API for animating CSS properties, SVG attributes, DOM elements, and JavaScript objects. This skill covers best practices, common patterns, and performance optimization for both vanilla JavaScript and React/Next.js applications.

CRITICAL: WAAPI-First Approach

Always prefer waapi.animate() over animate() unless you need JS engine features.

Decision Matrix: WAAPI vs JS Engine
Use waapi.animate() when:	Use animate() when:
✅ Simple CSS transforms/opacity	❌ Animating 500+ targets
✅ Bundle size matters (3KB vs 10KB)	❌ Animating JS objects, Canvas, WebGL
✅ CPU/network load is high	❌ Complex timeline orchestration
✅ Need hardware acceleration	❌ Need extensive callbacks (onRender, etc.)
✅ CSS color functions	❌ SVG path morphing
WAAPI Import
// Recommended: from main module
import { waapi, stagger, splitText } from 'animejs';

// Or standalone (smallest bundle)
import { waapi } from 'animejs/waapi';

WAAPI Basic Usage
// WAAPI - hardware accelerated, lightweight
waapi.animate('.element', {
  translateX: 200,
  rotate: 180,
  opacity: [0, 1],
  duration: 800,
  ease: 'outExpo'
});

CRITICAL: CSS vs WAAPI Timing Differences
Property	CSS	WAAPI/anime.js
Duration	2s	2000 (milliseconds!)
Infinite	infinite	Infinity (JS constant)
Default easing	ease	linear
Iterations	animation-iteration-count	iterations

Common bug: Animation not visible because duration is 2 (2ms) instead of 2000 (2s).

When to Fall Back to JS Engine
import { animate } from 'animejs';

// Use animate() for: 500+ targets, JS objects, complex timelines, SVG morphing
animate(myJsObject, {
  value: 100,
  onUpdate: () => renderCanvas(myJsObject)  // Extensive callbacks
});

Native WAAPI vs anime.js waapi

anime.js waapi.animate() wraps the browser's native Element.animate(). Use native when:

Zero dependencies needed
Need commitStyles(), persist(), getAnimations()
Debugging animation issues
// Native WAAPI (no anime.js needed)
element.animate([
  { opacity: 0, transform: 'translateY(20px)' },
  { opacity: 1, transform: 'translateY(0)' }
], {
  duration: 500,      // ALWAYS milliseconds
  easing: 'ease-out', // default is 'linear', not 'ease'!
  fill: 'forwards'
});


See references/native-waapi.md for complete native WAAPI documentation.

CRITICAL: Animation Planning Workflow

Before writing any animation code, ALWAYS follow this planning workflow:

Step 1: Describe the Animation Visually

Present an ASCII/text visualization of the animation to the user:

Animation: "Bouncing Text"
Target: "hello world" (11 characters)

Timeline visualization:
t=0ms     h e l l o   w o r l d    [all at baseline]
t=100ms   H e l l o   w o r l d    [h bounces up]
t=180ms   h E l l o   w o r l d    [e bounces up]
t=260ms   h e L l o   w o r l d    [l bounces up]
...continues with 80ms stagger...

Movement pattern per character:
    ↑ (-20px)
    │
────┼──── baseline
    │
    ↓ (return)

Duration: 300ms up + 300ms down = 600ms per bounce
Loop: continuous
Total animation time: 3000ms requested

Step 2: Choose WAAPI vs JS Engine

Decide which animation engine to use:

Engine Decision:
- Target count: 11 characters (< 500) ✅ WAAPI OK
- Animation type: CSS transforms (translateY) ✅ WAAPI OK
- Callbacks needed: None ✅ WAAPI OK
- Bundle size: Want smallest ✅ WAAPI preferred

→ Decision: Use waapi.animate()

Step 3: Specify the anime.js APIs to Use

List the specific anime.js functions required:

APIs needed:
- splitText() - to split "hello world" into individual character elements
- waapi.animate() - hardware-accelerated animation (WAAPI-first!)
- stagger() - to offset each character's animation start time

Why splitText() over manual splitting:
- Handles accessibility (aria-label)
- Provides proper data attributes (data-char, data-word, data-line)
- Handles whitespace correctly
- Returns animatable element arrays directly

Step 4: Calculate Timing (ALWAYS in Milliseconds!)

Show the math for timing. Remember: WAAPI uses milliseconds, not seconds!

Timing calculation (all values in MILLISECONDS):
- User requested: 3 seconds = 3000ms
- Bounce cycle: 300ms up + 300ms down = 600ms
- Characters: 11
- Stagger delay: 80ms between each
- Last char starts at: 10 × 80ms = 800ms
- Full sequence: 800ms + 600ms = 1400ms
- For 3000ms total: loop: true (repeats ~2x)

⚠️ VERIFY: duration: 600 (not 0.6!)
⚠️ VERIFY: delay: 80 (not 0.08!)

Step 5: Accessibility Check

Verify accessibility is handled:

Accessibility:
- [ ] Will respect prefers-reduced-motion? YES - will add check
- [ ] Duration reasonable? YES - 600ms (not too fast/slow)
- [ ] Essential content visible without animation? YES

Step 6: Get User Confirmation

Always ask: "Does this animation plan look correct? Should I proceed with implementation?"

Only after confirmation, write the code using the exact APIs specified.

Installation and Setup
Package Installation
npm install animejs

Import Patterns

Use named imports from the main module (recommended for bundlers with tree-shaking):

import { animate, createTimeline, stagger, utils } from 'animejs';


For projects without bundlers or when tree-shaking is ineffective, use subpath imports:

import { animate } from 'animejs/animation';
import { createTimeline } from 'animejs/timeline';
import { stagger, random } from 'animejs/utils';
import { splitText } from 'animejs/text';
import { svg } from 'animejs/svg';

Core Animation Patterns
Basic Animation (WAAPI - Preferred)
import { waapi } from 'animejs';

// Use WAAPI for CSS transforms - hardware accelerated!
waapi.animate('.element', {
  translateX: 250,
  rotate: '1turn',
  opacity: 0.5,
  duration: 1000,
  ease: 'outExpo'
});

Animation Targets

Both waapi.animate() and animate() accept multiple target formats:

import { waapi } from 'animejs';

// CSS selector
waapi.animate('.my-class', { opacity: 0 });

// DOM element
waapi.animate(document.querySelector('#element'), { scale: 1.5 });

// Array of elements
waapi.animate([el1, el2, el3], { translateY: 100 });

JS Engine for Non-CSS Targets
import { animate } from 'animejs';

// Use animate() for JavaScript objects (WAAPI can't do this)
const obj = { value: 0 };
animate(obj, {
  value: 100,
  duration: 1000,
  onUpdate: () => console.log(obj.value)
});

Animatable Properties
CSS transforms: translateX, translateY, translateZ, rotate, rotateX, rotateY, rotateZ, scale, scaleX, scaleY, skew, skewX, skewY
CSS properties: opacity, width, height, margin, padding, borderRadius, backgroundColor, color
CSS variables: '--custom-property'
SVG attributes: cx, cy, r, fill, stroke, strokeDashoffset, points, d
HTML attributes: Any attribute via object syntax
Value Types
animate('.element', {
  // Absolute values
  translateX: 250,

  // With units
  width: '100%',

  // Relative values
  translateY: '+=50',  // Add 50 to current
  rotate: '-=45deg',   // Subtract 45deg

  // From-to array
  opacity: [0, 1],     // Animate from 0 to 1

  // Function-based (per target)
  scale: (el, i) => 1 + i * 0.1,

  // Keyframes
  translateX: [
    { value: 100, duration: 500 },
    { value: 0, duration: 500 }
  ]
});

Timeline Animations (JS Engine)

Note: Complex timelines require the JS engine (createTimeline), not WAAPI.

Orchestrate multiple animations with precise control:

import { createTimeline } from 'animejs';

const tl = createTimeline({
  defaults: { duration: 800, ease: 'outExpo' }
});

tl.add('.box-1', { translateX: 250 })
  .add('.box-2', { translateY: 100 }, '-=400')  // Start 400ms before previous ends
  .add('.box-3', { scale: 1.5 }, '+=200');      // Start 200ms after previous ends

Timeline Labels
const tl = createTimeline();

tl.add('.intro', { opacity: [0, 1] })
  .label('afterIntro')
  .add('.content', { translateY: [50, 0] }, 'afterIntro')
  .add('.sidebar', { translateX: [-100, 0] }, 'afterIntro+=200');

Timeline Controls
const tl = createTimeline({ autoplay: false });

// Add animations...

tl.play();
tl.pause();
tl.reverse();
tl.seek(500);      // Jump to 500ms
tl.restart();
tl.complete();     // Jump to end

Stagger Animations

Create sequential animations across multiple elements (works with both WAAPI and JS engine):

import { waapi, stagger } from 'animejs';

// Time staggering (WAAPI)
waapi.animate('.item', {
  translateY: [50, 0],
  opacity: [0, 1],
  delay: stagger(100)  // 100ms between each
});

// Grid staggering (WAAPI)
waapi.animate('.grid-item', {
  scale: [0, 1],
  delay: stagger(50, {
    grid: [10, 10],
    from: 'center',
    axis: 'y'
  })
});

// Stagger with easing (WAAPI)
waapi.animate('.item', {
  translateX: 200,
  delay: stagger(100, { ease: 'outQuad' })
});

Value Staggering (JS Engine only)
import { animate, stagger } from 'animejs';

// Value staggering requires JS engine
animate('.bar', {
  height: stagger([100, 200, 150, 250])  // Specific values per element
});

Text Animations with splitText

ALWAYS use splitText() for character/word/line animations - never manually split text.

Basic Text Splitting (WAAPI)
import { waapi, splitText, stagger } from 'animejs';

// Split text into characters, words, and lines
const { chars, words, lines } = splitText('.text-element', {
  chars: true,
  words: true,
  lines: true
});

// Animate characters with WAAPI (hardware accelerated)
waapi.animate(chars, {
  translateY: [-20, 0],
  opacity: [0, 1],
  delay: stagger(50),
  duration: 600,
  ease: 'outExpo'
});

splitText Options
const split = splitText('.text', {
  // What to split into
  chars: true,           // Split into characters
  words: true,           // Split into words
  lines: true,           // Split into lines

  // Wrap elements for clipping effects
  chars: { wrap: 'span', class: 'char' },
  words: { wrap: 'clip' },   // 'clip' adds overflow:hidden for reveal effects
  lines: { wrap: 'div' },

  // Accessibility
  accessible: true,      // Adds aria-label to preserve screen reader text

  // Include space characters as elements
  includeSpaces: true
});

// Access results
split.chars   // Array of character span elements
split.words   // Array of word elements
split.lines   // Array of line elements

Character Bounce Animation (Correct Pattern)
import { waapi, splitText, stagger } from 'animejs';

// Split the text
const { chars } = splitText('.bouncing-text', { chars: true });

// Bouncing animation with WAAPI
waapi.animate(chars, {
  translateY: [-20, 0],      // Simple keyframes for WAAPI
  delay: stagger(80),
  duration: 600,             // Full bounce cycle
  loop: true,
  alternate: true,           // Bounce back down
  ease: 'inOutQuad'
});

Wave Effect
import { waapi, splitText, stagger } from 'animejs';

const { chars } = splitText('.wave-text', { chars: true });

waapi.animate(chars, {
  translateY: -15,
  delay: stagger(40, { from: 'center' }),
  duration: 400,
  loop: true,
  alternate: true,
  ease: 'inOutSine'
});

Text Reveal with Clip
import { waapi, splitText, stagger } from 'animejs';

const { words } = splitText('.reveal-text', {
  words: { wrap: 'clip' }  // Clip overflow for reveal effect
});

waapi.animate(words, {
  translateY: ['100%', '0%'],
  delay: stagger(100),
  duration: 800,
  ease: 'outExpo'
});

React/Next.js Text Animation (WAAPI)
'use client';

import { useEffect, useRef } from 'react';
import { waapi, splitText, stagger } from 'animejs';

export function AnimatedText({ children, className }) {
  const textRef = useRef(null);

  useEffect(() => {
    if (!textRef.current) return;

    const { chars } = splitText(textRef.current, {
      chars: true,
      accessible: true
    });

    // Use WAAPI for hardware-accelerated text animation
    const anim = waapi.animate(chars, {
      translateY: [20, 0],
      opacity: [0, 1],
      delay: stagger(30),
      duration: 600,
      ease: 'outExpo'
    });

    return () => anim.cancel();
  }, [children]);

  return <span ref={textRef} className={className}>{children}</span>;
}

Easing Functions
Built-in Easings

Pattern: {in|out|inOut}{Quad|Cubic|Quart|Quint|Sine|Expo|Circ|Back|Elastic|Bounce}

animate('.element', {
  translateX: 200,
  ease: 'outExpo'      // Common choice for UI
});

animate('.element', {
  translateX: 200,
  ease: 'inOutQuad'    // Smooth acceleration/deceleration
});

Cubic Bezier
import { cubicBezier } from 'animejs';

animate('.element', {
  translateX: 200,
  ease: cubicBezier(0.7, 0.1, 0.5, 0.9)
});

Spring Physics
import { spring } from 'animejs';

animate('.element', {
  translateX: 200,
  ease: spring({ bounce: 0.25, duration: 800 })
});

// Stiffness/damping control
animate('.element', {
  scale: 1.2,
  ease: spring({ stiffness: 90, damping: 14 })
});

Steps Easing
animate('.element', {
  translateX: 200,
  ease: 'steps(5)'     // 5 discrete steps
});

Callbacks and Promises
Animation Callbacks
animate('.element', {
  translateX: 200,
  onBegin: (anim) => console.log('Started'),
  onUpdate: (anim) => console.log(anim.progress),
  onComplete: (anim) => console.log('Done'),
  onLoop: (anim) => console.log('Loop iteration')
});

Promise-based Chaining
await animate('.step-1', { opacity: [0, 1] }).then();
await animate('.step-2', { translateY: [50, 0] }).then();
await animate('.step-3', { scale: [0.8, 1] }).then();

Playback Controls
const anim = animate('.element', {
  translateX: 200,
  autoplay: false
});

anim.play();
anim.pause();
anim.reverse();
anim.restart();
anim.seek(500);           // Jump to 500ms
anim.stretch(2000);       // Change duration to 2000ms
anim.playbackRate = 2;    // Double speed

React/Next.js Integration
useRef with WAAPI (Recommended)
import { useRef, useEffect } from 'react';
import { waapi } from 'animejs';

function AnimatedComponent() {
  const elementRef = useRef(null);

  useEffect(() => {
    if (elementRef.current) {
      // WAAPI for hardware-accelerated animations
      waapi.animate(elementRef.current, {
        translateY: [20, 0],
        opacity: [0, 1],
        duration: 600,
        ease: 'outExpo'
      });
    }
  }, []);

  return <div ref={elementRef}>Animated content</div>;
}

Cleanup on Unmount
useEffect(() => {
  const anim = waapi.animate(elementRef.current, {
    translateX: [0, 200],
    loop: true
  });

  return () => anim.cancel();  // Cancel on unmount
}, []);

Animation Hook Pattern (WAAPI)
import { useRef, useEffect, useCallback } from 'react';
import { waapi } from 'animejs';

function useAnimation(config) {
  const elementRef = useRef(null);
  const animationRef = useRef(null);

  const play = useCallback(() => {
    if (elementRef.current) {
      animationRef.current = waapi.animate(elementRef.current, config);
    }
  }, [config]);

  useEffect(() => {
    return () => animationRef.current?.cancel();
  }, []);

  return { ref: elementRef, play };
}

Server Component Considerations (Next.js)

Animation code must run client-side. Mark components with 'use client':

'use client';

import { useEffect, useRef } from 'react';
import { waapi } from 'animejs';

export function AnimatedCard({ children }) {
  const ref = useRef(null);

  useEffect(() => {
    // WAAPI is ideal for simple entrance animations
    waapi.animate(ref.current, {
      opacity: [0, 1],
      translateY: [20, 0],
      duration: 600,
      ease: 'outExpo'
    });
  }, []);

  return <div ref={ref}>{children}</div>;
}

Accessibility: prefers-reduced-motion

ALWAYS respect user preferences for reduced motion.

const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  // No animation - instant state change
  element.style.opacity = '1';
} else {
  waapi.animate(element, { opacity: [0, 1], duration: 600 });
}


See references/accessibility-and-testing.md for React hook and full patterns.

Performance Best Practices
Prefer transforms over layout properties: Animate translateX/Y, scale, rotate instead of width, height, top, left
Use will-change sparingly: Add only when needed, remove after animation
Batch animations: Use timelines for coordinated animations
Clean up animations: Call cancel() when components unmount
Avoid animating too many elements: Stagger large sets, animate visible elements only
Use requestAnimationFrame rate: Default frameRate is optimal for most cases
Respect prefers-reduced-motion: Always check user accessibility preferences
Additional Resources
Official Documentation (references/docs/)

Comprehensive API documentation fetched from animejs.com:

Category	File	Content
Core	docs/getting-started/README.md	Installation, imports, basic usage
Core	docs/timer/README.md	createTimer API, playback, callbacks
Animation	docs/animation/targets-and-properties.md	CSS selectors, DOM elements, JS objects
Animation	docs/animation/tween-values-and-parameters.md	Value types, tween params
Animation	docs/animation/keyframes-playback-methods.md	Keyframes, playback controls
Timeline	docs/timeline/README.md	Timeline creation, time positioning
Animatable	docs/animatable/README.md	Reactive animatable objects
Draggable	docs/draggable/README.md	Draggable API, physics settings
Layout	docs/layout/README.md	FLIP animations, enter/exit states
Scope	docs/scope/README.md	Scoped animations, media queries
Events	docs/events/onscroll/README.md	ScrollObserver, thresholds, sync
SVG	docs/svg/README.md	morphTo, createDrawable, createMotionPath
Text	docs/text/splittext/README.md	Text splitting, lines/words/chars
Utilities	docs/utilities/stagger/README.md	Stagger function, grid staggering
Utilities	docs/utilities/helpers.md	$(), get(), set(), random, math
Easings	docs/easings/README.md	Built-in eases, spring physics
WAAPI	docs/web-animation-api/README.md	Hardware acceleration, API differences
Engine	docs/engine/README.md	Engine config, time units, FPS
MDN Web Animations API (references/docs/web-animations-api/)

Native browser Web Animations API documentation from MDN:

Category	File	Content
Guides	docs/web-animations-api/guides/README.md	Overview, concepts, keyframe formats, tips
Interfaces	docs/web-animations-api/interfaces/animation.md	Animation, AnimationEffect, KeyframeEffect
Interfaces	docs/web-animations-api/interfaces/timelines.md	AnimationTimeline, DocumentTimeline, ScrollTimeline, ViewTimeline
Methods	docs/web-animations-api/methods/README.md	Element.animate(), getAnimations(), events
Best Practice Guides (references/)

For patterns and techniques beyond the API docs:

references/accessibility-and-testing.md - prefers-reduced-motion, TypeScript, testing, common mistakes
references/native-waapi.md - Native Web Animations API (Element.animate) - timing, keyframes, playback controls
references/scroll-animations.md - ScrollObserver patterns and scroll-triggered animations
references/svg-animations.md - SVG morphing, path drawing, and motion paths
references/advanced-patterns.md - Text animations, draggable elements, layout animations
Example Files

Working examples in examples/:

basic-animation.js - Core animation patterns
timeline-sequence.js - Timeline orchestration
react-integration.jsx - React hooks and patterns
scroll-reveal.js - Scroll-triggered animations
Weekly Installs
–
Repository
davidosemwegie/…ractices
GitHub Stars
3
First Seen
–