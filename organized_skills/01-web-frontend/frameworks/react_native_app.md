---
rating: ⭐⭐⭐
title: react-native-app
url: https://skills.sh/aj-geddes/useful-ai-prompts/react-native-app
---

# react-native-app

skills/aj-geddes/useful-ai-prompts/react-native-app
react-native-app
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill react-native-app
SKILL.md
React Native App Development
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create robust cross-platform mobile applications using React Native with modern development patterns including navigation, state management, API integration, and native module handling.

When to Use
Building iOS and Android apps from single codebase
Rapid prototyping for mobile platforms
Leveraging web development skills for mobile
Sharing code between React Native and React Web
Integrating with native modules and APIs
Quick Start

Minimal working example:

// Navigation with React Navigation
import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { Ionicons } from "@expo/vector-icons";

const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

function HomeStack() {
  return (
    <Stack.Navigator
      screenOptions={{
        headerStyle: { backgroundColor: "#6200ee" },
        headerTintColor: "#fff",
        headerTitleStyle: { fontWeight: "bold" },
      }}
    >
      <Stack.Screen
        name="Home"
        component={HomeScreen}
        options={{ title: "Home Feed" }}
      />
      <Stack.Screen name="Details" component={DetailsScreen} />
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Project Setup & Navigation	Project Setup & Navigation
State Management with Redux	State Management with Redux
API Integration with Axios	API Integration with Axios
Functional Component with Hooks	Functional Component with Hooks
Best Practices
✅ DO
Use functional components with React Hooks
Implement proper error handling and loading states
Use Redux or Context API for state management
Leverage React Navigation for routing
Optimize list rendering with FlatList
Handle platform-specific code elegantly
Use TypeScript for type safety
Test on both iOS and Android
Use environment variables for API endpoints
Implement proper memory management
❌ DON'T
Use inline styles excessively (use StyleSheet)
Make API calls without error handling
Store sensitive data in plain text
Ignore platform differences
Create large monolithic components
Use index as key in lists
Make synchronous operations
Ignore battery optimization
Deploy without testing on real devices
Forget to unsubscribe from listeners
Weekly Installs
302
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass