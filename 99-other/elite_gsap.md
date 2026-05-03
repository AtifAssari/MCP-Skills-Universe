---
rating: ⭐⭐
title: elite-gsap
url: https://skills.sh/rshvr/elite-web-design/elite-gsap
---

# elite-gsap

skills/rshvr/elite-web-design/elite-gsap
elite-gsap
Installation
$ npx skills add https://github.com/rshvr/elite-web-design --skill elite-gsap
SKILL.md
Elite GSAP

The most powerful animation library for the web. All plugins now 100% free.

2026 Update: GSAP is Free

As of Webflow's acquisition, all GSAP plugins (including former "Club" plugins) are completely free for commercial use:

ScrollTrigger
SplitText
Flip
MorphSVG
DrawSVG
MotionPathPlugin
Physics2D
Inertia
CustomEase

No more licensing restrictions.

Quick Reference
Topic	Reference File
ScrollTrigger	scrolltrigger.md
SplitText	splittext.md
Flip plugin	flip-plugin.md
MorphSVG & DrawSVG	morphsvg-drawsvg.md
Timelines	timelines.md
Framework integration	framework-integration.md
Utility library	utility-library.md
Smooth scroll (Lenis)	smooth-scroll.md
Core Setup
Installation
npm install gsap

Plugin Registration

Register plugins once at app entry point:

import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { SplitText } from 'gsap/SplitText';
import { Flip } from 'gsap/Flip';
import { DrawSVGPlugin } from 'gsap/DrawSVGPlugin';
import { MorphSVGPlugin } from 'gsap/MorphSVGPlugin';
import { MotionPathPlugin } from 'gsap/MotionPathPlugin';

gsap.registerPlugin(
  ScrollTrigger,
  SplitText,
  Flip,
  DrawSVGPlugin,
  MorphSVGPlugin,
  MotionPathPlugin
);

Context & Cleanup (CRITICAL)

Always use gsap.context() to scope animations. This prevents memory leaks in SPAs and component-based frameworks.

Vanilla JS
// Create context scoped to a container
const ctx = gsap.context(() => {
  // All animations and ScrollTriggers created here
  // are automatically tracked
  gsap.from('.hero-title', { opacity: 0, y: 50 });
  gsap.from('.hero-description', { opacity: 0, y: 30, delay: 0.3 });

  ScrollTrigger.create({
    trigger: '.section',
    start: 'top center',
    onEnter: () => console.log('entered')
  });
}, containerElement);  // Scope to container

// Later: Clean up everything
ctx.revert();  // Reverts all animations and kills ScrollTriggers

Why This Matters

Without context:

Animations persist after component unmount
ScrollTriggers keep listening to removed elements
Memory leaks accumulate
SPA navigation breaks animations

With context:

Single revert() call cleans everything
Safe for React/Vue/Svelte components
No stale references
Essential Animation Patterns
Basic Tween
// Animate TO a state
gsap.to('.element', {
  x: 100,
  opacity: 0.5,
  duration: 1,
  ease: 'power2.out'
});

// Animate FROM a state
gsap.from('.element', {
  opacity: 0,
  y: 50,
  duration: 0.8,
  ease: 'power3.out'
});

// FROM-TO for full control
gsap.fromTo('.element',
  { opacity: 0, y: 50 },
  { opacity: 1, y: 0, duration: 0.8 }
);

// Set immediately (no animation)
gsap.set('.element', { opacity: 1, y: 0 });

Stagger Animations
// Basic stagger
gsap.from('.card', {
  opacity: 0,
  y: 30,
  duration: 0.6,
  stagger: 0.1  // 100ms between each
});

// Advanced stagger
gsap.from('.grid-item', {
  opacity: 0,
  scale: 0.8,
  duration: 0.5,
  stagger: {
    each: 0.1,
    from: 'center',  // 'start', 'end', 'center', 'edges', 'random', or index
    grid: [4, 6],    // For grid layouts
    axis: 'x'        // 'x', 'y', or null for both
  }
});

Easing
// Power eases (most common)
gsap.to('.el', { x: 100, ease: 'power1.out' });  // Subtle
gsap.to('.el', { x: 100, ease: 'power2.out' });  // Balanced (recommended)
gsap.to('.el', { x: 100, ease: 'power3.out' });  // Snappy
gsap.to('.el', { x: 100, ease: 'power4.out' });  // Dramatic

// Ease directions
// .in - starts slow, accelerates
// .out - starts fast, decelerates (default)
// .inOut - slow at both ends

// Special eases
gsap.to('.el', { x: 100, ease: 'elastic.out(1, 0.3)' });
gsap.to('.el', { x: 100, ease: 'back.out(1.7)' });
gsap.to('.el', { x: 100, ease: 'bounce.out' });

// Custom ease
gsap.to('.el', { x: 100, ease: 'M0,0 C0.7,0 0.3,1 1,1' });  // Bezier

Callbacks
gsap.to('.element', {
  x: 100,
  duration: 1,
  onStart: () => console.log('Animation started'),
  onUpdate: () => console.log('Frame update'),
  onComplete: () => console.log('Animation complete'),
  onReverseComplete: () => console.log('Reversed to start')
});

prefers-reduced-motion (CRITICAL)

Always respect user motion preferences:

const mm = gsap.matchMedia();

mm.add('(prefers-reduced-motion: no-preference)', () => {
  // Full animations
  gsap.from('.hero', {
    opacity: 0,
    y: 50,
    duration: 1,
    ease: 'power3.out'
  });
});

mm.add('(prefers-reduced-motion: reduce)', () => {
  // Instant or simple fade
  gsap.set('.hero', { opacity: 1, y: 0 });
  // Or: gsap.from('.hero', { opacity: 0, duration: 0.3 });
});


See elite-accessibility skill for comprehensive patterns.

GPU-Accelerated Properties

For 60fps performance, only animate:

x, y (translateX, translateY)
xPercent, yPercent
scale, scaleX, scaleY
rotation, rotationX, rotationY
opacity

Never animate:

width, height
top, left, right, bottom
margin, padding
border-width
// GOOD - GPU accelerated
gsap.to('.card', { x: 100, y: 50, scale: 1.1, rotation: 5, opacity: 0.8 });

// BAD - Causes reflows
gsap.to('.card', { width: 200, height: 200, marginLeft: 50 });

ScrollTrigger Quick Start
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

// Basic scroll-triggered animation
gsap.from('.section-content', {
  opacity: 0,
  y: 50,
  duration: 1,
  scrollTrigger: {
    trigger: '.section',
    start: 'top 80%',   // When top of trigger hits 80% of viewport
    end: 'bottom 20%',
    toggleActions: 'play none none none',
    // markers: true  // Dev only
  }
});

// Pinned section
ScrollTrigger.create({
  trigger: '.sticky-section',
  start: 'top top',
  end: '+=100%',
  pin: true,
  pinSpacing: true
});

// Scrub animation (tied to scroll position)
gsap.to('.parallax-element', {
  y: -100,
  ease: 'none',
  scrollTrigger: {
    trigger: '.parallax-section',
    start: 'top bottom',
    end: 'bottom top',
    scrub: true
  }
});


See scrolltrigger.md for comprehensive patterns.

SplitText Quick Start
import { SplitText } from 'gsap/SplitText';
gsap.registerPlugin(SplitText);

// Split text into characters
const split = new SplitText('.headline', {
  type: 'chars,words,lines',
  linesClass: 'line'
});

// Animate characters
gsap.from(split.chars, {
  opacity: 0,
  y: 50,
  rotationX: -90,
  stagger: 0.02,
  duration: 0.8,
  ease: 'power4.out'
});

// IMPORTANT: Revert when done (or on cleanup)
// split.revert();


See splittext.md for text animation patterns.

Flip Plugin Quick Start
import { Flip } from 'gsap/Flip';
gsap.registerPlugin(Flip);

// Capture current state
const state = Flip.getState('.cards');

// Make DOM changes
container.appendChild(newCard);
// or
card.classList.toggle('expanded');
// or
filterCards();

// Animate the change
Flip.from(state, {
  duration: 0.6,
  ease: 'power2.inOut',
  stagger: 0.05,
  absolute: true,  // Prevents layout shift during animation
  onEnter: elements => gsap.from(elements, { opacity: 0, scale: 0.8 }),
  onLeave: elements => gsap.to(elements, { opacity: 0, scale: 0.8 })
});


See flip-plugin.md for layout animation patterns.

Timeline Quick Start
const tl = gsap.timeline({
  defaults: { duration: 0.8, ease: 'power3.out' }
});

tl.from('.hero-title', { opacity: 0, y: 50 })
  .from('.hero-description', { opacity: 0, y: 30 }, '-=0.5')  // Overlap
  .from('.hero-cta', { opacity: 0, y: 20 }, '-=0.3')
  .from('.hero-image', { opacity: 0, scale: 0.9 }, '<');  // Same time as previous

// Control
tl.play();
tl.pause();
tl.reverse();
tl.seek(0.5);  // Jump to 0.5 seconds
tl.progress(0.5);  // Jump to 50%


See timelines.md for orchestration patterns.

Common Patterns
Reveal on Scroll
const mm = gsap.matchMedia();

mm.add('(prefers-reduced-motion: no-preference)', () => {
  gsap.utils.toArray('.reveal').forEach(element => {
    gsap.from(element, {
      opacity: 0,
      y: 40,
      duration: 0.8,
      ease: 'power3.out',
      scrollTrigger: {
        trigger: element,
        start: 'top 85%',
        toggleActions: 'play none none none'
      }
    });
  });
});

Horizontal Scroll Section
const mm = gsap.matchMedia();

mm.add('(prefers-reduced-motion: no-preference)', () => {
  const panels = gsap.utils.toArray('.panel');
  const wrapper = document.querySelector('.horizontal-wrapper');

  gsap.to(panels, {
    xPercent: -100 * (panels.length - 1),
    ease: 'none',
    scrollTrigger: {
      trigger: wrapper,
      pin: true,
      scrub: 1,
      snap: 1 / (panels.length - 1),
      end: () => '+=' + wrapper.scrollWidth
    }
  });
});

Magnetic Button
const button = document.querySelector('.magnetic-btn');

button.addEventListener('mousemove', (e) => {
  const rect = button.getBoundingClientRect();
  const x = e.clientX - rect.left - rect.width / 2;
  const y = e.clientY - rect.top - rect.height / 2;

  gsap.to(button, {
    x: x * 0.3,
    y: y * 0.3,
    duration: 0.3,
    ease: 'power2.out'
  });
});

button.addEventListener('mouseleave', () => {
  gsap.to(button, {
    x: 0,
    y: 0,
    duration: 0.5,
    ease: 'elastic.out(1, 0.3)'
  });
});

Text Reveal with Mask
const split = new SplitText('.headline', { type: 'lines', linesClass: 'line' });

// Wrap each line in a mask container
split.lines.forEach(line => {
  const wrapper = document.createElement('div');
  wrapper.style.overflow = 'hidden';
  line.parentNode.insertBefore(wrapper, line);
  wrapper.appendChild(line);
});

gsap.from(split.lines, {
  yPercent: 100,
  opacity: 0,
  duration: 1,
  stagger: 0.1,
  ease: 'power4.out'
});

Debugging
// Enable dev warnings
gsap.config({
  nullTargetWarn: true
});

// ScrollTrigger markers (dev only)
ScrollTrigger.defaults({
  markers: process.env.NODE_ENV === 'development'
});

// Log animation state
gsap.to('.el', {
  x: 100,
  onUpdate: function() {
    console.log('Progress:', this.progress());
  }
});

Framework Integration

See framework-integration.md for:

React with @gsap/react
Vue composition API patterns
Svelte lifecycle patterns
Vanilla JS module patterns
Related Skills
elite-accessibility - Motion accessibility and prefers-reduced-motion patterns
elite-performance - Build optimization and Core Web Vitals
elite-css-animations - CSS-native animation alternatives
elite-layouts - Layout patterns (bento grids, horizontal scroll, sticky sections)
elite-brand-design - Brand identity and visual systems
Resources
GSAP Docs
GSAP Eases Visualizer
ScrollTrigger Demos
GreenSock Forums
Weekly Installs
30
Repository
rshvr/elite-web-design
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass