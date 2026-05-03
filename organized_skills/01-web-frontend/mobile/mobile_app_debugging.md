---
rating: ⭐⭐
title: mobile-app-debugging
url: https://skills.sh/aj-geddes/useful-ai-prompts/mobile-app-debugging
---

# mobile-app-debugging

skills/aj-geddes/useful-ai-prompts/mobile-app-debugging
mobile-app-debugging
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill mobile-app-debugging
SKILL.md
Mobile App Debugging
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Mobile app debugging addresses platform-specific issues, device hardware limitations, and mobile-specific network conditions.

When to Use
App crashes on mobile
Performance issues on device
Platform-specific bugs
Network connectivity issues
Device-specific problems
Quick Start

Minimal working example:

Xcode Debugging:

Attach Debugger:
  - Xcode → Run on device
  - Set breakpoints in code
  - Step through execution
  - View variables
  - Console logs

View Logs:
  - Xcode → Window → Devices & Simulators
  - Select device → View Device Logs
  - Filter by app name
  - Check system logs for crashes

Inspect Memory:
  - Xcode → Debug → View Memory Graph
  - Identify retain cycles
  - Check object count
  - Monitor allocation growth

---
Common iOS Issues:

App Crash (SIGABRT):
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
iOS Debugging	iOS Debugging
Android Debugging	Android Debugging
Cross-Platform Issues	Cross-Platform Issues
Mobile Testing & Debugging Checklist	Mobile Testing & Debugging Checklist
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
352
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