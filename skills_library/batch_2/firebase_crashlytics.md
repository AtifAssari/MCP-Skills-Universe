---
title: firebase-crashlytics
url: https://skills.sh/firebase/agent-skills/firebase-crashlytics
---

# firebase-crashlytics

skills/firebase/agent-skills/firebase-crashlytics
firebase-crashlytics
Installation
$ npx skills add https://github.com/firebase/agent-skills --skill firebase-crashlytics
SKILL.md
Crashlytics

This skill provides a complete guide for getting started with Crashlytics on Android or iOS. Crash data collected from client applications can be read using the MCP server in the Firebase CLI.

Prerequisites

Provisioning Crashlytics requires both a Firebase project and a Firebase app, either Android or iOS. To read the data collected by Crashlytics, install the MCP server in the Firebase CLI. See the firebase-basics skill for references.

SDK Setup

To learn how to setup Crashlytics in your application code, choose your platform:

Android: android_setup.md
iOS: ios_setup.md
SDK Usage

The SDK provides a number of features to make crash reports more actionable.

Add custom keys
Add custom logs
Set user identifiers
Report non-fatal exceptions

To learn how to customize crash reports and add additional debugging data, consult the documentation for your platform.

Android: Customize Crash Reports for Android
iOS: Customize Crash Reports for Apple Platforms
Weekly Installs
1.7K
Repository
firebase/agent-skills
GitHub Stars
264
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass