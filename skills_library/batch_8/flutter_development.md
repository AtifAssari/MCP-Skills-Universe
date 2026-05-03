---
title: flutter-development
url: https://skills.sh/aj-geddes/useful-ai-prompts/flutter-development
---

# flutter-development

skills/aj-geddes/useful-ai-prompts/flutter-development
flutter-development
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill flutter-development
SKILL.md
Flutter Development
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Create high-performance, visually stunning mobile applications using Flutter with Dart language. Master widget composition, state management patterns, navigation, and API integration.

When to Use
Building iOS and Android apps with native performance
Designing custom UIs with Flutter's widget system
Implementing complex animations and visual effects
Rapid app development with hot reload
Creating consistent UX across platforms
Quick Start

Minimal working example:

// pubspec.yaml
name: my_flutter_app
version: 1.0.0

dependencies:
  flutter:
    sdk: flutter
  provider: ^6.0.0
  http: ^1.1.0
  go_router: ^12.0.0

// main.dart with GoRouter navigation
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Project Structure & Navigation	Project Structure & Navigation
State Management with Provider	State Management with Provider
Screens with Provider Integration	Screens with Provider Integration
Best Practices
✅ DO
Use widgets for every UI element
Implement proper state management
Use const constructors where possible
Dispose resources in state lifecycle
Test on multiple device sizes
Use meaningful widget names
Implement error handling
Use responsive design patterns
Test on both iOS and Android
Document custom widgets
❌ DON'T
Build entire screens in build() method
Use setState for complex state logic
Make network calls in build()
Ignore platform differences
Create overly nested widget trees
Hardcode strings
Ignore performance warnings
Skip testing
Forget to handle edge cases
Deploy without thorough testing
Weekly Installs
444
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass