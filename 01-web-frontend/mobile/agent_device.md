---
rating: ⭐⭐
title: agent-device
url: https://skills.sh/callstackincubator/agent-device/agent-device
---

# agent-device

skills/callstackincubator/agent-device/agent-device
agent-device
Installation
$ npx skills add https://github.com/callstackincubator/agent-device --skill agent-device
Summary

Automate iOS and Android app interactions with snapshot-based discovery and selector-driven replay.

Supports iOS simulators/devices and Android emulators/devices with session-bound automation, multi-tenant remote daemon mode, and device-scope isolation for QA workflows
Core commands: snapshot for UI discovery with refs, press/fill/scroll for interactions, open/close for app lifecycle, install/reinstall for binary deployment
Includes utilities for logging, network inspection, performance metrics, clipboard access, permission management, biometric simulation, and notification delivery
Handles React Native + Metro workflows, tvOS/AndroidTV targeting, batch step execution, and replay maintenance with selector drift detection
SKILL.md
agent-device

Router only. Private setup before using this skill:

agent-device --version


Require agent-device >= 0.14.0; older CLIs lack these help topics. If older, run npm install -g agent-device@latest, recheck, then continue. If you cannot upgrade, stop and tell the user. Do not include version/upgrade commands in final plans.

Before your first agent-device command or plan, read the version-matched CLI guide:

agent-device help workflow


Escalate only when relevant:

agent-device help debugging
agent-device help react-devtools
agent-device help remote
agent-device help macos
agent-device help dogfood


Default loop: open -> snapshot/-i -> get/is/find or press/fill/scroll/wait -> verify -> close.

Use this skill only to route into version-matched CLI help. Let help workflow provide exact command shapes, platform limits, and current workflow guidance.

Weekly Installs
3.3K
Repository
callstackincuba…t-device
GitHub Stars
1.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn