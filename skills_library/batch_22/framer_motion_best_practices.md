---
title: framer-motion-best-practices
url: https://skills.sh/pproenca/dot-skills/framer-motion-best-practices
---

# framer-motion-best-practices

skills/pproenca/dot-skills/framer-motion-best-practices
framer-motion-best-practices
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill framer-motion-best-practices
SKILL.md
Community Framer Motion Best Practices

Comprehensive performance optimization guide for Framer Motion animations in React applications. Contains 42 rules across 9 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Adding animations to React components with Framer Motion
Optimizing bundle size for animation-heavy applications
Preventing unnecessary re-renders during animations
Implementing layout transitions or shared element animations
Building scroll-linked or gesture-based interactions
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Bundle Optimization	CRITICAL	bundle-
2	Re-render Prevention	CRITICAL	rerender-
3	Animation Properties	HIGH	anim-
4	Layout Animations	HIGH	layout-
5	Scroll Animations	MEDIUM-HIGH	scroll-
6	Gesture Optimization	MEDIUM	gesture-
7	Spring & Physics	MEDIUM	spring-
8	SVG & Path Animations	LOW-MEDIUM	svg-
9	Exit Animations	LOW	exit-
Quick Reference
1. Bundle Optimization (CRITICAL)
bundle-lazy-motion - Use LazyMotion and m component instead of motion
bundle-dynamic-features - Dynamically import motion features
bundle-dom-animation - Use domAnimation for basic animations
bundle-use-animate-mini - Use mini useAnimate for simple cases
bundle-strict-mode - Enable strict mode to catch accidental imports
2. Re-render Prevention (CRITICAL)
rerender-motion-value - Use useMotionValue instead of useState
rerender-use-transform - Derive values with useTransform
rerender-stable-callbacks - Keep animation callbacks stable
rerender-variants-object - Define variants outside component
rerender-animate-prop - Use stable animate values
rerender-motion-value-event - Use motion value events
3. Animation Properties (HIGH)
anim-transform-properties - Animate transform properties
anim-opacity-filter - Prefer opacity and filter for visual effects
anim-hardware-acceleration - Leverage hardware acceleration
anim-will-change - Use willChange prop judiciously
anim-independent-transforms - Animate transforms independently
anim-keyframes-array - Use keyframe arrays for sequences
4. Layout Animations (HIGH)
layout-dependency - Use layoutDependency to limit measurements
layout-position-size - Use layout="position" or "size" appropriately
layout-group - Group related layout animations
layout-id-shared - Use layoutId for shared element transitions
layout-scroll - Add layoutScroll to scrollable ancestors
5. Scroll Animations (MEDIUM-HIGH)
scroll-use-scroll - Use useScroll hook for scroll-linked animations
scroll-use-spring-smooth - Smooth scroll animations with useSpring
scroll-element-tracking - Track specific elements entering viewport
scroll-offset-configuration - Configure scroll offsets
scroll-container-ref - Track scroll within specific containers
6. Gesture Optimization (MEDIUM)
gesture-while-props - Use whileHover/whileTap instead of handlers
gesture-variants-flow - Let gesture variants flow to children
gesture-drag-constraints - Use dragConstraints ref for boundaries
gesture-drag-elastic - Configure dragElastic for natural feel
gesture-tap-cancel - Use onTapCancel for interrupted gestures
7. Spring & Physics (MEDIUM)
spring-physics-based - Use physics-based springs for interruptibility
spring-damping-ratio - Configure damping to control oscillation
spring-mass-inertia - Adjust mass for heavier/lighter feel
spring-use-spring-hook - Use useSpring for reactive values
8. SVG & Path Animations (LOW-MEDIUM)
svg-path-length - Use pathLength for line drawing animations
svg-motion-components - Use motion.path and motion.circle
svg-viewbox-animation - Animate viewBox for zoom effects
svg-morph-matching-points - Match point counts for morphing
9. Exit Animations (LOW)
exit-animate-presence - Wrap conditional renders with AnimatePresence
exit-unique-keys - Provide unique keys for AnimatePresence children
exit-mode-wait - Use mode="wait" for sequential transitions
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
191
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