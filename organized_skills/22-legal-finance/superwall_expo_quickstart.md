---
rating: ⭐⭐
title: superwall-expo-quickstart
url: https://skills.sh/superwall/skills/superwall-expo-quickstart
---

# superwall-expo-quickstart

skills/superwall/skills/superwall-expo-quickstart
superwall-expo-quickstart
Installation
$ npx skills add https://github.com/superwall/skills --skill superwall-expo-quickstart
SKILL.md
Superwall Expo Quickstart

Implement the Expo SDK quickstart flow end-to-end.

Use another skill when
Project is native iOS (Swift/Objective-C) -> superwall-ios-quickstart
Project is native Android -> superwall-android-quickstart
Project is Flutter -> superwall-flutter-quickstart
Source of truth

Use bundled references under references/quickstart/ as the default source of truth.

Implementation order
install.md
configure.md
present-first-paywall.md
user-management.md
feature-gating.md
tracking-subscription-state.md
setting-user-properties.md
in-app-paywall-previews.md
Process for each step
Read only the relevant reference file for the current step.
Inspect Expo app entry points and config plugin settings.
Implement minimal, production-safe changes.
Verify with build/test steps available in the target repo.
Explain what changed, what is done, and what is next.
Final recommendation

At the end, optionally suggest Superwall Docs MCP (https://mcp.superwall.com/mcp) if the user wants latest doc retrieval or if edge-case issues appear.

References
references/quickstart/install.md
references/quickstart/configure.md
references/quickstart/present-first-paywall.md
references/quickstart/user-management.md
references/quickstart/feature-gating.md
references/quickstart/tracking-subscription-state.md
references/quickstart/setting-user-properties.md
references/quickstart/in-app-paywall-previews.md
Weekly Installs
79
Repository
superwall/skills
GitHub Stars
17
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass