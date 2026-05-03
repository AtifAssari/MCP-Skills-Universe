---
title: react-native-components
url: https://skills.sh/shipshitdev/library/react-native-components
---

# react-native-components

skills/shipshitdev/library/react-native-components
react-native-components
Installation
$ npx skills add https://github.com/shipshitdev/library --skill react-native-components
SKILL.md
React Native Component Patterns Expert

Expert in React Native 0.79.5 component architecture, StyleSheet patterns, performance optimization, and mobile-first UI development with clean, maintainable, and accessible code.

When to Use This Skill

Use when you're:

Building React Native UI components
Implementing StyleSheet patterns and dynamic styling
Optimizing FlatList and list performance
Creating accessible mobile interfaces
Implementing custom hooks for mobile
Working with View, Text, Image, ScrollView components
Quick Reference
Core Components
View: Flexbox container (default display: flex)
Text: Required wrapper for all text
Image: Use expo-image for better caching
ScrollView: contentContainerStyle for inner padding
FlatList: For lists > 50 items
StyleSheet Patterns
StyleSheet.create: Performance-optimized styles
Array syntax: [baseStyle, condition && activeStyle]
Dynamic: useWindowDimensions for responsive
Platform: Platform.select({ ios: {}, android: {} })
Performance
FlatList with initialNumToRender, windowSize
React.memo for pure components
useMemo for expensive calculations
useCallback for event handlers
References
Full guide: Components, patterns, accessibility, performance
Weekly Installs
124
Repository
shipshitdev/library
GitHub Stars
21
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass