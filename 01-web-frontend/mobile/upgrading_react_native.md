---
rating: ⭐⭐⭐
title: upgrading-react-native
url: https://skills.sh/callstackincubator/agent-skills/upgrading-react-native
---

# upgrading-react-native

skills/callstackincubator/agent-skills/upgrading-react-native
upgrading-react-native
Installation
$ npx skills add https://github.com/callstackincubator/agent-skills --skill upgrading-react-native
Summary

Orchestrates React Native version upgrades with template diffs, dependency resolution, and native platform migration.

Applies canonical rn-diff-purge template diffs to align native iOS and Android configuration with target React Native versions
Handles package.json dependency updates, CocoaPods and Gradle changes, and breaking API migrations across major and minor version bumps
Includes Expo SDK upgrade layer for managed Expo projects and post-upgrade verification checklist
Provides structured workflow routing: choose upgrade path, fetch diff, assess dependencies, align React version, validate builds on both platforms
SKILL.md
Upgrading React Native
Overview

Covers the full React Native upgrade workflow: template diffs via Upgrade Helper, dependency updates, Expo SDK steps, and common pitfalls.

Typical Upgrade Sequence
Route: Choose the right upgrade path via upgrading-react-native.md
Diff: Fetch the canonical template diff using Upgrade Helper via upgrade-helper-core.md
Dependencies: Assess and update third-party packages via upgrading-dependencies.md
React: Align React version if upgraded via react.md
Expo (if applicable): Apply Expo SDK layer via expo-sdk-upgrade.md
Verify: Run post-upgrade checks via upgrade-verification.md
# Quick start: detect current version and fetch diff
npm pkg get dependencies.react-native --prefix "$APP_DIR"
npm view react-native dist-tags.latest

# Example: upgrading from 0.76.9 to 0.78.2
# 1. Fetch the template diff
curl -L -f -o /tmp/rn-diff.diff \
  "https://raw.githubusercontent.com/react-native-community/rn-diff-purge/diffs/diffs/0.76.9..0.78.2.diff" \
  && echo "Diff downloaded OK" || echo "ERROR: diff not found, check versions"
# 2. Review changed files
grep -n "^diff --git" /tmp/rn-diff.diff
# 3. Update package.json, apply native changes, then install + rebuild
npm install --prefix "$APP_DIR"
cd "$APP_DIR/ios" && pod install
# 4. Validate: both platforms must build successfully
npx react-native build-android --mode debug --no-packager
xcodebuild -workspace "$APP_DIR/ios/App.xcworkspace" -scheme App -sdk iphonesimulator build

When to Apply

Reference these guidelines when:

Moving a React Native app to a newer version
Reconciling native config changes from Upgrade Helper
Validating release notes for breaking changes
Quick Reference
File	Description
upgrading-react-native.md	Router: choose the right upgrade path
upgrade-helper-core.md	Core Upgrade Helper workflow and reliability gates
upgrading-dependencies.md	Dependency compatibility checks and migration planning
react.md	React and React 19 upgrade alignment rules
expo-sdk-upgrade.md	Expo SDK-specific upgrade layer (conditional)
upgrade-verification.md	Manual post-upgrade verification checklist
monorepo-singlerepo-targeting.md	Monorepo and single-repo app targeting and command scoping
Problem → Skill Mapping
Problem	Start With
Need to upgrade React Native	upgrade-helper-core.md
Need dependency risk triage and migration options	upgrading-dependencies.md
Need React/React 19 package alignment	react.md
Need workflow routing first	upgrading-react-native.md
Need Expo SDK-specific steps	expo-sdk-upgrade.md
Need manual regression validation	upgrade-verification.md
Need repo/app command scoping	monorepo-singlerepo-targeting.md
Weekly Installs
2.4K
Repository
callstackincuba…t-skills
GitHub Stars
1.3K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn