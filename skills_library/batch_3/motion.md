---
title: motion
url: https://skills.sh/hairyf/skills/motion
---

# motion

skills/hairyf/skills/motion
motion
Installation
$ npx skills add https://github.com/hairyf/skills --skill motion
Summary

GPU-accelerated animation library for JavaScript, React, and Vue with gestures, springs, and layout transitions.

Supports motion components (motion.div, motion.svg), variants, transitions with spring physics, and scroll-linked effects
Includes gesture handlers for drag, pan, tap, press, hover, and focus interactions
Provides layout animations with AnimatePresence, LayoutGroup, and drag-to-reorder capabilities
Offers motion values, transforms, and imperative animation controls via useAnimate and animation sequences
Hybrid engine combines JavaScript with native browser APIs for 120fps performance; tree-shakable builds and TypeScript support included
SKILL.md

Motion is an open-source animation library for JavaScript, React, and Vue. It provides a simple API with first-class support for multiple platforms, a hybrid animation engine combining JavaScript with native browser APIs for 120fps GPU-accelerated animations, and production-ready features including TypeScript support, extensive test suite, tree-shakable builds, and a tiny footprint. Batteries included: gestures, springs, layout transitions, scroll-linked effects, and timelines.

The skill is based on Motion v12.29.2, generated at 2026-02-01.

Core References
Topic	Description	Reference
Motion Components	Basic motion components (motion.div, motion.svg, etc.)	core-components
Basic Animation	animate prop, initial, while states	core-animation
JavaScript animate()	Vanilla animate(), sequences, createScopedAnimate	core-javascript-animate
Vanilla scroll()	Imperative scroll() and scrollInfo() for non-React	core-vanilla-scroll
motionValue	Create MotionValues without React	core-vanilla-motion-value
stagger	Orchestrate child delays in variants	core-stagger
frame / cancelFrame	Motion's animation loop	core-frameloop
motion/mini	Minimal bundle entry	core-motion-mini
Variants	Declarative animation variants and orchestration	core-variants
Transitions	Animation timing, easing, spring physics	core-transitions
Motion Values
Topic	Description	Reference
useMotionValue	Create and use motion values for reactive animations	values-motion-value
useSpring	Spring-based motion values with physics	values-spring
useTransform	Transform motion values with functions	values-transform
useMotionTemplate	Combine motion values into a string (e.g. filter, boxShadow)	values-motion-template
useFollowValue	Motion value that follows a source with any transition	values-follow
useScroll	Scroll-linked motion values and animations	values-scroll
useVelocity	Access velocity of motion values	values-velocity
useTime	Time-based motion values	values-time
useWillChange	GPU layer hint for animating elements	values-will-change
Gestures
Topic	Description	Reference
Drag	Drag gestures with constraints and controls	gestures-drag
Pan	Pan gestures for touch and pointer events	gestures-pan
Tap & Press	Tap and press gesture handlers	gestures-tap-press
Hover & Focus	Hover and focus state animations	gestures-hover-focus
Layout Animations
Topic	Description	Reference
AnimatePresence	Animate components entering and exiting	layout-animate-presence
usePresence / useIsPresent	Access presence state in AnimatePresence children	layout-use-presence
usePresenceData	Read AnimatePresence custom prop in descendants	layout-presence-data
LayoutGroup	Coordinate layout animations across components	layout-group
Layout Animations	Automatic layout animations with layoutId	layout-animations
Reorder	Drag-to-reorder with layout animations	layout-reorder
useInstantLayoutTransition	Block layout update for one frame	layout-instant-transition
useResetProjection	Reset layout projection tree after structural change	layout-reset-projection
Features
Topic	Description	Reference
In View	useInView, inView(), usePageInView for viewport/visibility	features-in-view
Resize	resize() observer for window or element size	features-resize
Optimized Appear	SSR-friendly appear animations with handoff	features-optimized-appear
SVG Path	pathLength, pathOffset, pathSpacing for path animations	features-svg-path
motion/client	Next.js "use client" and tree-shakable components	features-react-client
Utils
Topic	Description	Reference
useReducedMotion	Hooks for reduced motion preference	utils-reduced-motion
useAnimationFrame	Frame-synced callback with Motion's loop	utils-animation-frame
useCycle	Cycle through a list of states	utils-cycle
useMotionValueEvent	Subscribe to motion value events	utils-motion-value-event
delay	Frame-synced delayed execution	utils-delay
interpolate	Map input range to output	utils-interpolate
useDomEvent	Attach DOM event listeners	utils-dom-event
useInstantTransition	Block layout animations during update	utils-instant-transition
calcLength / createBox / distance	Projection geometry and distance	utils-path-geometry
Advanced
Topic	Description	Reference
Animation Controls	Programmatic animation control with useAnimation	advanced-animation-controls
useAnimate	Imperative animation API	advanced-use-animate
LazyMotion	Code-split animations for better performance	advanced-lazy-motion
MotionConfig	Global configuration and reduced motion	advanced-motion-config
Scroll Animations	Scroll-linked animations and parallax effects	advanced-scroll-animations
transformTemplate	Custom transform output	advanced-transform-template
addScaleCorrector	Layout projection scale correctors	advanced-scale-corrector
Best Practices
Topic	Description	Reference
Bundle Size	Entry points and optimization strategies	best-practices-bundle
Weekly Installs
727
Repository
hairyf/skills
GitHub Stars
15
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass