---
rating: ⭐⭐
title: maestro-e2e
url: https://skills.sh/raphaelbarbosaqwerty/maestro-dev-skills/maestro-e2e
---

# maestro-e2e

skills/raphaelbarbosaqwerty/maestro-dev-skills/maestro-e2e
maestro-e2e
Installation
$ npx skills add https://github.com/raphaelbarbosaqwerty/maestro-dev-skills --skill maestro-e2e
SKILL.md
When to use

Use this skill whenever you are:

Creating E2E, UI, or integration tests
Testing login, registration, or navigation flows
Handling permission dialogs (camera, location, notifications)
Debugging test failures or exploring UI hierarchy
Working with Maestro test files (.yaml)
Captions

When dealing with native permission dialogs, load the ./rules/permissions.md file for platform-specific information.

When working with Flutter apps, load the ./rules/platforms/flutter.md file for Semantics patterns.

How to use

Read individual rule files for detailed explanations and code examples:

Core
rules/installation.md - Installing Maestro on macOS, Linux, and Windows
rules/test-structure.md - YAML test structure, appId, env variables, and flow definition
rules/commands.md - Complete reference of 40+ Maestro commands
rules/selectors.md - Element targeting with id, text, index, and matchers
rules/assertions.md - assertVisible, assertNotVisible, assertTrue, and AI assertions
rules/interactions.md - tapOn, inputText, scroll, swipe, and gesture commands
rules/permissions.md - iOS vs Android permission configuration and dialog handling
Platforms
rules/platforms/android.md - Android-specific: ADB, permission dialogs, emulators
rules/platforms/ios.md - iOS-specific: auto-dismiss dialogs, simulators, limitations
rules/platforms/flutter.md - Flutter integration using Semantics and identifier
rules/platforms/react-native.md - React Native with testID and accessibilityLabel
rules/platforms/web.md - Desktop browser testing with Chromium
Advanced
rules/advanced/parameters.md - Environment variables, external params, ${} syntax
rules/advanced/conditions.md - Conditional execution with when: visible, platform
rules/advanced/nested-flows.md - Reusable subflows with runFlow command
rules/advanced/javascript.md - evalScript, runScript, and GraalJS support
rules/advanced/waiting.md - extendedWaitUntil, waitForAnimationToEnd
rules/advanced/repeat-retry.md - Repeat and retry patterns for flaky tests
Additional
rules/debugging.md - Maestro Studio, hierarchy inspection, troubleshooting
rules/screenshots.md - Screenshots, video recording, and visual evidence
rules/ci-integration.md - GitHub Actions, GitLab CI, Maestro Cloud
rules/best-practices.md - Semantic identifiers, atomic tests, project structure
Weekly Installs
291
Repository
raphaelbarbosaq…v-skills
GitHub Stars
5
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn