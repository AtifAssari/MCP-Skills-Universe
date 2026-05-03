---
rating: ⭐⭐
title: pi-extension-authoring
url: https://skills.sh/romiluz13/pi-agent-skills/pi-extension-authoring
---

# pi-extension-authoring

skills/romiluz13/pi-agent-skills/pi-extension-authoring
pi-extension-authoring
Installation
$ npx skills add https://github.com/romiluz13/pi-agent-skills --skill pi-extension-authoring
SKILL.md
Pi extension authoring

Ground every answer in pi-mono/ files below.

Grounding
pi-mono/packages/coding-agent/docs/extensions.md — capabilities, lifecycle, patterns.
pi-mono/packages/coding-agent/examples/extensions/README.md — runnable examples index.
pi-mono/packages/coding-agent/src/core/resource-loader.ts — extendResources() appends paths via mergePaths after existing lastSkillPaths (late paths lose name collisions to earlier ones unless names differ).
pi-mono/packages/coding-agent/src/core/agent-session.ts — extension commands vs queued prompts; skill expansion hooks.
pi-mono/packages/coding-agent/docs/tui.md — extension TUI component integration with @mariozechner/pi-tui: Component rendering contract, overlay patterns, input handling in extension context.
pi-mono/packages/coding-agent/docs/custom-provider.md — registerProvider() for proxies, OAuth/SSO, custom APIs, and custom model definitions.
Invariants
Extensions can register tools, commands, themes, prompts, and extra skill paths; exact API surface is defined in docs and example modules — start from docs/extensions.md, not memory.
Dynamic resource discovery patterns live under pi-mono/packages/coding-agent/examples/extensions/ (e.g. dynamic-resources/ listing in examples README).
Workflows
New extension: Read docs/extensions.md, clone the closest examples/extensions/ template, then align with project AGENTS.md if working inside pi-mono.
Skills from extensions: Trace extendResources + mergePaths in resource-loader.ts to explain ordering with user/project/package skills.
Extension TUI: Read docs/tui.md for the Component rendering contract in extension context; combine with pi-tui skill for library-level APIs.
Custom providers via extension: See pi-mono/packages/coding-agent/docs/custom-provider.md for registerProvider() OAuth flows and proxy patterns (grounded in pi-cli-workspace).
Anti-patterns
Do not assert MCP support in core; optional via extension (see coding-agent README philosophy).
Weekly Installs
18
Repository
romiluz13/pi-ag…t-skills
GitHub Stars
11
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass