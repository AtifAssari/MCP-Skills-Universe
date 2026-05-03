---
title: react-native-expo
url: https://skills.sh/hairyf/skills/react-native-expo
---

# react-native-expo

skills/hairyf/skills/react-native-expo
react-native-expo
Installation
$ npx skills add https://github.com/hairyf/skills --skill react-native-expo
SKILL.md

The skill is based on Expo SDK (docs from expo/expo repo), generated at 2026-02-26.

Expo provides tooling and services for React Native: app config and Prebuild (Continuous Native Generation), Expo SDK packages, development builds, EAS Build (cloud builds and internal distribution), and EAS Update (over-the-air JS updates). Use development builds for production apps; Expo Go is a limited playground.

Core References
Topic	Description	Reference
App config	app.json, app.config.js/ts, dynamic config, reading in app	core-config
Development workflow	Dev loop, development builds vs Expo Go, when to rebuild	core-development-workflow
Development and production modes	DEV, --no-dev --minify, when to use each	core-development-mode
Metro	metro.config.js, resolver, transformer, cache, env vars	core-metro
Logging	Console in terminal, native logs, log-android / log-ios	core-logging
CNG and Prebuild	npx expo prebuild, --clean, EAS Build and native dirs	core-continuous-native-generation
Features
Expo SDK and native code
Topic	Description	Reference
Expo SDK and third-party libs	Install with npx expo install, compatibility, config plugins	features-expo-modules
expo-constants	App manifest, build info, system constants, extra/env at runtime	features-sdk-constants
expo-image	Performant image component, caching, BlurHash/ThumbHash, contentFit	features-sdk-image
expo-file-system	File and directory API, Paths.cache/document, read/write, download	features-sdk-filesystem
expo-secure-store	Encrypted key-value store, optional biometric auth	features-sdk-secure-store
Config plugins	Use and write plugins to modify AndroidManifest, Info.plist during prebuild	features-config-plugins
Native modules	Expo Modules API, local module, config plugin for native config, lifecycle	features-native-modules
EAS Build and Submit
Topic	Description	Reference
EAS Build	Cloud builds, eas.json profiles, development/preview/production	features-eas
EAS Submit	Submit to Google Play and App Store (TestFlight), eas.json, CI	features-eas-submit
Development experience
Topic	Description	Reference
iOS Simulator and Android emulator	Setup, npx expo start + i/a, limitations, troubleshooting	features-simulators-emulators
Updates and versioning
Topic	Description	Reference
expo-updates and EAS Update	OTA updates, runtime version, channels	features-updates
Upgrading Expo SDK	Incremental upgrade, npx expo install --fix, expo-doctor	features-versioning
Best practices
Topic	Description	Reference
Debugging	Dev vs production errors, native logs, reproducing crashes	best-practices-debugging
Common development errors	Metro, AppRegistry, SDK version, version mismatch, caches	best-practices-common-errors
Weekly Installs
77
Repository
hairyf/skills
GitHub Stars
15
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass