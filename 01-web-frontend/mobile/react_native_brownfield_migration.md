---
rating: ⭐⭐
title: react-native-brownfield-migration
url: https://skills.sh/callstackincubator/agent-skills/react-native-brownfield-migration
---

# react-native-brownfield-migration

skills/callstackincubator/agent-skills/react-native-brownfield-migration
react-native-brownfield-migration
Installation
$ npx skills add https://github.com/callstackincubator/agent-skills --skill react-native-brownfield-migration
SKILL.md
Migrating to React Native
Overview

Prescriptive workflow for incremental adoption of React Native in existing native apps using @callstack/react-native-brownfield, from initial setup through phased host integration.

Expo track
Bare React Native track

Use one track per task unless the user explicitly asks for migration or comparison.

Migration Strategy

Use this strategy for brownfield migration planning and execution:

Assess app state and select Expo or bare path.
Perform initial setup with @callstack/react-native-brownfield.
Package RN artifacts (XCFramework/AAR) from the RN source app.
Integrate one RN surface into the host app and validate startup/runtime.
Repeat integration by feature/screen for incremental rollout.
Agent Guardrails (Global)

Apply these rules across all reference files:

Select one path first (Expo or bare) and do not mix steps.
Use placeholders from the docs (<framework_target_name>, <android_module_name>, <registered_module_name>) and resolve from project files.
Validate each packaging command before moving to host integration.
Prefer official docs for long platform snippets and CLI option details.
Keep host apps isolated from direct React Native APIs when possible (facade approach).
Canonical Docs
Quick Start
Expo Integration
iOS Integration
Android Integration
Brownfield CLI
Guidelines
Troubleshooting
Path Selection Gate (Must Run First)

Before selecting any reference file, classify the project:

If no React Native app exists yet, use Expo creation path:
expo-create-app.md -> expo-quick-start.md
If React Native app exists, inspect package.json and app.json:
Expo if expo is present or Expo plugin workflow is requested.
Bare RN if native folders and direct RN CLI workflow are used without Expo path requirements.
If still unclear, ask one disambiguation question.
Continue with exactly one path.
When to Apply

Reference this package when:

Planning incremental migration from native-only apps to React Native or Expo
Creating brownfield integration flows for Expo or bare React Native projects
Performing initial setup with @callstack/react-native-brownfield
Generating iOS XCFramework artifacts from a React Native app
Generating and publishing Android AAR artifacts from a React Native app
Integrating generated artifacts into host iOS/Android apps
Quick Reference
File	Description
quick-start.md	Shared preflight and mandatory path-selection gate
expo-create-app.md	Scaffold a new Expo app before Expo brownfield setup
expo-quick-start.md	Expo plugin setup and packaging readiness
expo-ios-integration.md	Expo iOS packaging and host startup integration
expo-android-integration.md	Expo Android packaging, publish, and host integration
bare-quick-start.md	Bare React Native baseline setup
bare-ios-xcframework-generation.md	Bare iOS XCFramework generation
bare-android-aar-generation.md	Bare Android AAR generation and publish
bare-ios-native-integration.md	Bare iOS host integration
bare-android-native-integration.md	Bare Android host integration
Problem -> Skill Mapping
Problem	Start With
Need path decision first	quick-start.md
Need to create a new Expo app for brownfield	expo-create-app.md
Need Expo brownfield setup and plugin wiring	expo-quick-start.md
Need Expo iOS brownfield integration	expo-ios-integration.md
Need Expo Android brownfield integration	expo-android-integration.md
Need bare RN baseline setup	bare-quick-start.md
Need bare RN iOS XCFramework generation	bare-ios-xcframework-generation.md
Need bare RN Android AAR generation/publish	bare-android-aar-generation.md
Need bare RN iOS host integration	bare-ios-native-integration.md
Need bare RN Android host integration	bare-android-native-integration.md
Weekly Installs
972
Repository
callstackincuba…t-skills
GitHub Stars
1.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass