---
title: react-native
url: https://skills.sh/hairyf/skills/react-native
---

# react-native

skills/hairyf/skills/react-native
react-native
Installation
$ npx skills add https://github.com/hairyf/skills --skill react-native
SKILL.md
React Native

The skill is based on React Native, generated at 2026-01-31.

React Native lets you build mobile apps using only JavaScript. It uses the same design as React, letting you compose a rich mobile UI from declarative components. With React Native, you don't build a "mobile web app", an "HTML5 app", or a "hybrid app". You build a real mobile app that's indistinguishable from an app built using Objective-C or Java.

Core References
Topic	Description	Reference
Core Components	View, Text, Image, TextInput, ScrollView - fundamental UI building blocks	core-components
Layout with Flexbox	Flexbox layout system for positioning and aligning components	core-layout
Styling	StyleSheet API for creating and organizing component styles	core-styling
Features
Animations
Topic	Description	Reference
Animated API	Create fluid animations with Animated.Value, timing, spring, and gesture integration	features-animations
Easing Functions	Easing functions for custom animation curves and natural motion	features-easing
User Interactions
Topic	Description	Reference
Touch Handling	Pressable, Touchable components, and gesture responders for handling user input	features-touch-handling
Keyboard	Keyboard API for handling keyboard events, dismissing keyboard, and KeyboardAvoidingView	features-keyboard
UI Components
Topic	Description	Reference
Additional Components	Modal, Switch, ActivityIndicator, RefreshControl for dialogs, toggles, loading states	components-ui
Data Display
Topic	Description	Reference
Lists	FlatList and SectionList for efficiently rendering large, scrollable lists	features-lists
Styling and Theming
Topic	Description	Reference
Colors and Theming	Colors, PlatformColor, Appearance API for theming and dark mode support	features-colors-theming
Platform Integration
Topic	Description	Reference
Platform APIs	Linking, Dimensions, Platform detection, AppState, and native integrations	features-platform-apis
Network	Fetch API for making HTTP requests and handling network responses	features-network
StatusBar	Control status bar appearance, style, and visibility	features-statusbar
Share & Vibration	Native share dialog and device vibration for haptic feedback	features-share-vibration
Timers	setTimeout, setInterval, requestAnimationFrame for scheduling and delays	features-timers
Platform-Specific APIs	Android (PermissionsAndroid, ToastAndroid, DrawerLayoutAndroid) and iOS (ActionSheetIOS)	features-platform-specific
Accessibility
Topic	Description	Reference
Accessibility	Screen reader support, accessibility labels, roles, and states	features-accessibility
Advanced Styling
Topic	Description	Reference
Transforms	2D and 3D transforms for rotation, scale, translation, and skew	features-transforms
Best Practices
Topic	Description	Reference
Performance	Performance optimization techniques, profiling, and common bottlenecks	best-practices-performance
Debugging	Debugging tools, Dev Menu, LogBox, React Native DevTools, and debugging techniques	best-practices-debugging
Key Recommendations
Use StyleSheet.create() for all styles instead of inline objects
Use FlatList instead of ScrollView for long lists
Enable useNativeDriver for animations when possible (transform, opacity)
Use Pressable for new touch interactions (preferred over Touchable components)
Handle platform differences with Platform.select() and Platform.OS
Test on real devices - simulator behavior may differ from actual devices
Optimize list performance with getItemLayout for fixed-height items
Use TypeScript for better type safety and developer experience
Weekly Installs
76
Repository
hairyf/skills
GitHub Stars
15
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass