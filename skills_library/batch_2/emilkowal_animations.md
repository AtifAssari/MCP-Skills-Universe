---
title: emilkowal-animations
url: https://skills.sh/pproenca/dot-skills/emilkowal-animations
---

# emilkowal-animations

skills/pproenca/dot-skills/emilkowal-animations
emilkowal-animations
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill emilkowal-animations
Summary

Animation best practices across easing, timing, properties, transforms, interactions, and accessibility for web interfaces.

43 rules organized by priority across 7 categories, from critical easing and timing decisions to medium-priority accessibility and polish
Covers easing curves (ease-out default, custom cubic-bezier, spring animations), timing windows (300ms max for UI, 500ms for drawers), and property selection (transform and opacity only)
Includes interaction patterns for gesture-based components: momentum-based dismissal, damping at boundaries, velocity-aware snap points, and pointer capture for drag operations
Provides specific values and techniques: scale(0.97) for button press, iOS-style cubic-bezier curves, asymmetric timing for press/release, and reduced-motion accessibility fallbacks
SKILL.md
Emil Kowalski Animation Best Practices

Comprehensive animation guide for web interfaces based on Emil Kowalski's teachings, open-source libraries (Sonner, Vaul), and his animations.dev course. Contains 43 rules across 7 categories, prioritized by impact.

When to Apply

Reference these guidelines when:

Adding animations to React components
Choosing easing curves or timing values
Implementing gesture-based interactions (swipe, drag)
Building toast notifications or drawer components
Optimizing animation performance
Ensuring animation accessibility
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Easing Selection	CRITICAL	ease-
2	Timing & Duration	CRITICAL	timing-
3	Property Selection	HIGH	props-
4	Transform Techniques	HIGH	transform-
5	Interaction Patterns	MEDIUM-HIGH	interact-
6	Strategic Animation	MEDIUM	strategy-
7	Accessibility & Polish	MEDIUM	polish-
Quick Reference
1. Easing Selection (CRITICAL)
ease-out-default - Use ease-out as your default easing
ease-custom-curves - Use custom cubic-bezier over built-in CSS
ease-in-out-onscreen - Use ease-in-out for on-screen movement
ease-spring-natural - Use spring animations for natural motion
ease-ios-drawer - Use iOS-style easing for drawer components
ease-context-matters - Match easing to animation context
2. Timing & Duration (CRITICAL)
timing-300ms-max - Keep UI animations under 300ms
timing-faster-better - Faster animations improve perceived performance
timing-asymmetric - Use asymmetric timing for press and release
timing-tooltip-delay - Delay initial tooltips, instant subsequent ones
timing-drawer-500ms - Use 500ms duration for drawer animations
3. Property Selection (HIGH)
props-transform-opacity - Animate only transform and opacity
props-hardware-accelerated - Use hardware-accelerated animations when main thread is busy
props-will-change - Use will-change to prevent 1px shift
props-avoid-css-variables - Avoid CSS variables for drag animations
props-clip-path-performant - Use clip-path for layout-free reveals
4. Transform Techniques (HIGH)
transform-scale-097 - Scale buttons to 0.97 on press
transform-never-scale-zero - Never animate from scale(0)
transform-percentage-translate - Use percentage values for translateY
transform-origin-aware - Make animations origin-aware
transform-scale-children - Scale transforms affect children
transform-3d-preserve - Use preserve-3d for 3D transform effects
5. Interaction Patterns (MEDIUM-HIGH)
interact-interruptible - Make animations interruptible
interact-momentum-dismiss - Use momentum-based dismissal
interact-damping - Damp drag at boundaries
interact-scroll-drag-conflict - Resolve scroll and drag conflicts
interact-snap-points - Implement velocity-aware snap points
interact-friction-upward - Allow upward drag with friction
interact-pointer-capture - Use pointer capture for drag operations
6. Strategic Animation (MEDIUM)
strategy-keyboard-no-animate - Never animate keyboard-initiated actions
strategy-frequency-matters - Consider interaction frequency before animating
strategy-purpose-required - Every animation must have a purpose
strategy-feedback-immediate - Provide immediate feedback on all actions
strategy-marketing-exception - Marketing sites are the exception
7. Accessibility & Polish (MEDIUM)
polish-reduced-motion - Respect prefers-reduced-motion
polish-opacity-fallback - Use opacity as reduced motion fallback
polish-framer-hook - Use useReducedMotion hook in Framer Motion
polish-dont-remove-all - Don't remove all animation for reduced motion
polish-blur-bridge - Use blur to bridge animation states
polish-clip-path-tabs - Use clip-path for tab transitions
polish-toast-stacking - Implement toast stacking with scale and offset
polish-scroll-reveal - Trigger scroll animations at appropriate threshold
polish-hover-gap-fill - Fill gaps between hoverable elements
polish-stagger-children - Stagger child animations for orchestration
Key Values Reference
Value	Usage
cubic-bezier(0.32, 0.72, 0, 1)	iOS-style drawer/sheet animation
scale(0.97)	Button press feedback
scale(0.95)	Minimum enter scale (never scale(0))
200ms ease-out	Standard UI transition
300ms	Maximum duration for UI animations
500ms	Drawer animation duration
0.11 px/ms	Velocity threshold for momentum dismiss
100px	Scroll-reveal viewport threshold
14px	Toast stack offset
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
882
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass