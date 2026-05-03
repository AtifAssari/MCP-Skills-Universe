---
title: plasmo-extension-architect
url: https://skills.sh/shipshitdev/library/plasmo-extension-architect
---

# plasmo-extension-architect

skills/shipshitdev/library/plasmo-extension-architect
plasmo-extension-architect
Installation
$ npx skills add https://github.com/shipshitdev/library --skill plasmo-extension-architect
SKILL.md
Plasmo Extension Architect

You design Plasmo-based extensions with MV3 service workers, content scripts, and UI surfaces.

When to Use
Building a Plasmo extension
Adding content scripts or messaging
Designing popup, options, or side panel UI
Core Patterns
Keep service worker stateless; persist in storage.
Use explicit message types and typed payloads.
Gate content script injection and make it idempotent.
Keep UI small and fast; use storage sync for prefs.
Typical Surfaces
background.ts
content-script.ts
popup.tsx
options.tsx
Security
Minimize host permissions.
Validate messages.
Avoid storing secrets in the DOM.
Build and Dev
Use plasmo dev for local development.
Keep manifest permissions aligned with features.
Validate MV3 constraints for long-running tasks.
Weekly Installs
141
Repository
shipshitdev/library
GitHub Stars
21
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass