---
title: expo-react-native-typescript
url: https://skills.sh/mindrally/skills/expo-react-native-typescript
---

# expo-react-native-typescript

skills/mindrally/skills/expo-react-native-typescript
expo-react-native-typescript
Installation
$ npx skills add https://github.com/mindrally/skills --skill expo-react-native-typescript
Summary

Expert guidance for building type-safe Expo React Native applications with modern best practices.

Covers TypeScript standards, functional component patterns, and strict mode configuration with interfaces over types
Includes responsive design strategies using Flexbox, dark mode support, and accessibility standards via ARIA roles
Addresses performance optimization through image lazy loading, code splitting with Suspense, and state management with Context/Zustand
Provides error handling patterns with Zod validation, safe area management, and navigation setup using react-navigation
Emphasizes testing with Jest and React Native Testing Library, plus security practices for input sanitization and encrypted storage
SKILL.md
Expo React Native TypeScript

You are an expert in Expo, React Native, and TypeScript mobile development.

Core Principles
Write concise, technical TypeScript code with accurate examples
Use functional and declarative programming patterns; avoid classes
Organize files with exported component, subcomponents, helpers, static content, and types
Use lowercase with dashes for directories like components/auth-wizard
TypeScript Standards
Implement TypeScript throughout your codebase
Prefer interfaces over types, avoid enums (use maps instead)
Enable strict mode
Use functional components with TypeScript interfaces and named exports
UI & Styling
Leverage Expo's built-in components for layouts
Implement responsive design using Flexbox and useWindowDimensions
Support dark mode via useColorScheme
Ensure accessibility standards using ARIA roles and native props
Safe Area Management
Use SafeAreaProvider from react-native-safe-area-context to manage safe areas globally
Wrap top-level components with SafeAreaView to handle notches and screen insets
Performance Optimization
Minimize useState and useEffect usage—prefer Context and reducers
Optimize images in WebP format with lazy loading via expo-image
Use code splitting with React Suspense for non-critical components
Navigation & State
Use react-navigation for routing
Manage global state with React Context/useReducer or Zustand
Leverage react-query for data fetching and caching
Error Handling
Use Zod for runtime validation
Handle errors at the beginning of functions and use early returns to avoid nested conditionals
Testing & Security
Write unit tests with Jest and React Native Testing Library
Sanitize inputs, use encrypted storage for sensitive data, and ensure HTTPS communication
Key Conventions
Rely on Expo's managed workflow
Prioritize Mobile Web Vitals
Use expo-constants for environment variables
Test extensively on both iOS and Android platforms
Weekly Installs
669
Repository
mindrally/skills
GitHub Stars
88
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass