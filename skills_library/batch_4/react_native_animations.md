---
title: react-native-animations
url: https://skills.sh/pluginagentmarketplace/custom-plugin-react-native/react-native-animations
---

# react-native-animations

skills/pluginagentmarketplace/custom-plugin-react-native/react-native-animations
react-native-animations
Installation
$ npx skills add https://github.com/pluginagentmarketplace/custom-plugin-react-native --skill react-native-animations
Summary

Build smooth 60fps animations combining Reanimated 3, Gesture Handler, and layout transitions.

Master Reanimated's shared values, animated styles, and timing functions (withSpring, withTiming, withDecay) for declarative animations
Handle complex gestures like pan, pinch, and rotation using Gesture Handler, then synchronize them with animations via shared values
Implement entering/exiting animations and layout transitions using FadeIn, FadeOut, and Layout.springify() for dynamic lists and UI changes
Optimize performance by understanding worklet directives, runOnJS boundaries, and avoiding frame drops on low-end devices
SKILL.md
React Native Animations Skill

Learn high-performance animations using Reanimated 3, Gesture Handler, and layout animations.

Prerequisites
React Native basics
Understanding of JavaScript closures
Familiarity with transforms and styles
Learning Objectives

After completing this skill, you will be able to:

 Create smooth 60fps animations with Reanimated
 Handle complex gestures with Gesture Handler
 Implement layout entering/exiting animations
 Optimize animations for performance
 Combine gestures with animations
Topics Covered
1. Installation
npm install react-native-reanimated react-native-gesture-handler

# babel.config.js
module.exports = {
  plugins: ['react-native-reanimated/plugin'],
};

2. Reanimated Basics
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSpring,
} from 'react-native-reanimated';

function AnimatedBox() {
  const scale = useSharedValue(1);

  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ scale: scale.value }],
  }));

  const handlePress = () => {
    scale.value = withSpring(scale.value === 1 ? 1.5 : 1);
  };

  return (
    <Pressable onPress={handlePress}>
      <Animated.View style={[styles.box, animatedStyle]} />
    </Pressable>
  );
}

3. Gesture Handler
import { Gesture, GestureDetector } from 'react-native-gesture-handler';

function DraggableBox() {
  const translateX = useSharedValue(0);
  const translateY = useSharedValue(0);

  const pan = Gesture.Pan()
    .onUpdate((e) => {
      translateX.value = e.translationX;
      translateY.value = e.translationY;
    })
    .onEnd(() => {
      translateX.value = withSpring(0);
      translateY.value = withSpring(0);
    });

  const style = useAnimatedStyle(() => ({
    transform: [
      { translateX: translateX.value },
      { translateY: translateY.value },
    ],
  }));

  return (
    <GestureDetector gesture={pan}>
      <Animated.View style={[styles.box, style]} />
    </GestureDetector>
  );
}

4. Layout Animations
import Animated, { FadeIn, FadeOut, Layout } from 'react-native-reanimated';

function AnimatedList({ items }) {
  return (
    <Animated.View layout={Layout.springify()}>
      {items.map((item) => (
        <Animated.View
          key={item.id}
          entering={FadeIn}
          exiting={FadeOut}
          layout={Layout.springify()}
        >
          <Text>{item.title}</Text>
        </Animated.View>
      ))}
    </Animated.View>
  );
}

5. Animation Timing
Function	Use Case
withTiming	Linear, controlled duration
withSpring	Natural, physics-based
withDecay	Momentum-based (fling)
withSequence	Multiple animations in order
withRepeat	Looping animations
Quick Start Example
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSpring,
  interpolate,
} from 'react-native-reanimated';
import { Gesture, GestureDetector } from 'react-native-gesture-handler';

function SwipeCard() {
  const translateX = useSharedValue(0);

  const gesture = Gesture.Pan()
    .onUpdate((e) => { translateX.value = e.translationX; })
    .onEnd(() => { translateX.value = withSpring(0); });

  const style = useAnimatedStyle(() => ({
    transform: [
      { translateX: translateX.value },
      { rotate: `${interpolate(translateX.value, [-200, 200], [-15, 15])}deg` },
    ],
  }));

  return (
    <GestureDetector gesture={gesture}>
      <Animated.View style={[styles.card, style]} />
    </GestureDetector>
  );
}

Common Errors & Solutions
Error	Cause	Solution
"Attempted to call from worklet"	Missing runOnJS	Wrap with runOnJS()
Animation not running	Missing 'worklet'	Add 'worklet' directive
Gesture not working	Missing root view	Add GestureHandlerRootView
Validation Checklist
 Animations run at 60fps
 Gestures respond smoothly
 No frame drops on low-end devices
 Layout animations don't cause jank
Usage
Skill("react-native-animations")


Bonded Agent: 05-react-native-animation

Weekly Installs
484
Repository
pluginagentmark…t-native
GitHub Stars
7
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass