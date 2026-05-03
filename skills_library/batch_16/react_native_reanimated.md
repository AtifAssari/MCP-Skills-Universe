---
title: react-native-reanimated
url: https://skills.sh/dralgorhythm/claude-agentic-framework/react-native-reanimated
---

# react-native-reanimated

skills/dralgorhythm/claude-agentic-framework/react-native-reanimated
react-native-reanimated
Installation
$ npx skills add https://github.com/dralgorhythm/claude-agentic-framework --skill react-native-reanimated
SKILL.md
React Native Reanimated
Overview

UI-thread animation library for React Native. Reanimated 4.x runs animations on the native UI thread for guaranteed 60fps performance, replacing Framer Motion for mobile applications. Provides shared values, animated styles, declarative entering/exiting transitions, and gesture integration.

Install: pnpm add react-native-reanimated (included with Expo SDK 54+)

Workflows

Adding animations to a screen:

 Import from react-native-reanimated: Animated, useSharedValue, useAnimatedStyle, withTiming
 Create shared values for animated properties
 Define animated styles using useAnimatedStyle
 Apply to Animated.View, Animated.Text, etc.
 Check useReducedMotion() and skip animations when true
 Test on device for smooth 60fps

Adding entering/exiting transitions:

 Import layout animations: FadeInDown, FadeOutUp, SlideInRight, etc.
 Apply entering and exiting props on Animated.View
 Chain modifiers: .duration(300).easing(...).delay(100)
 Verify reduced motion handling
Guidance
Core Primitives
useSharedValue(initialValue): Mutable value that lives on UI thread
useAnimatedStyle(() => ({...})): Derives style object from shared values
withTiming(toValue, config): Duration-based animation
withSpring(toValue, config): Physics-based spring animation
withDelay(ms, animation): Delay before animation starts
withSequence(...animations): Run animations in sequence
withRepeat(animation, count, reverse): Repeat animation
Standard Timing Configs

Consistent with demo-development.md durations:

Type	Duration	Use
Fast	150ms	Micro-interactions, haptic responses
Normal	300ms	Default transitions, entering
Slow	500ms	Emphasis, screen transitions
Stagger offset	50ms per item	List item reveals

Easing: Easing.out(Easing.cubic) for entrances, Easing.inOut(Easing.cubic) for transitions, Easing.in(Easing.cubic) for exits.

Declarative Entering/Exiting

Apply directly to Animated.View — no parent wrapper needed (unlike AnimatePresence):

Entering: FadeIn, FadeInDown, FadeInUp, SlideInRight, ZoomIn
Exiting: FadeOut, FadeOutUp, FadeOutDown, SlideOutLeft, ZoomOut
Chain modifiers: .duration(300), .delay(100), .easing(Easing.out(Easing.cubic))
Spring: .springify().damping(15).stiffness(150)
Stagger Pattern

Use withDelay with index multiplication:

entering={FadeInDown.delay(index * 50).duration(300)}


Or for imperative animations:

offset.value = withDelay(index * 50, withTiming(1, { duration: 300 }))

Accessibility — Reduced Motion

Always respect the user's accessibility preference:

const reducedMotion = useReducedMotion();


When reducedMotion is true:

Skip all animations (set values instantly)
Use duration(0) or don't apply entering/exiting props
Still show content — just don't animate it
Animated Components

Use Animated.View, Animated.Text, Animated.ScrollView, etc. Or create animated versions:

const AnimatedPressable = Animated.createAnimatedComponent(Pressable);

Performance
Animate only transform and opacity — these run on the UI thread
Avoid animating width, height, margin, padding (causes layout recalculation)
Shared values update on UI thread without JS bridge overhead
useAnimatedStyle worklets run on UI thread — keep them pure
For lists, use entering/exiting on items rather than animating the container
Best Practices
Use declarative entering/exiting for mount/unmount animations — simpler than manual shared values
Prefer withSpring for natural-feeling interactions (drag, gestures)
Prefer withTiming for UI transitions (screen enter, fade in)
Always check useReducedMotion() before applying animations
Keep standard durations consistent: 150ms / 300ms / 500ms
Use withDelay(index * 50, ...) for staggered list reveals
Combine with react-native-gesture-handler for gesture-driven animations
Use Easing.out(Easing.cubic) as default easing for entrances
Anti-Patterns
Using React Native's built-in Animated API instead of Reanimated
Animating layout properties (width, height, margin) — use transform and opacity
Forgetting useReducedMotion() accessibility check
Running JS-thread-heavy logic inside useAnimatedStyle worklets
Hardcoding duration values (use constants: 150/300/500ms)
Nesting many animated views unnecessarily (performance overhead)
Using setTimeout for stagger instead of withDelay
Applying entering animations without testing on real device
Weekly Installs
99
Repository
dralgorhythm/cl…ramework
GitHub Stars
76
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass