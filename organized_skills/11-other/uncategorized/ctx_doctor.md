---
rating: ⭐⭐
title: ctx-doctor
url: https://skills.sh/mksglu/context-mode/ctx-doctor
---

# ctx-doctor

skills/mksglu/context-mode/ctx-doctor
ctx-doctor
Installation
$ npx skills add https://github.com/mksglu/context-mode --skill ctx-doctor
SKILL.md
Context Mode Doctor

Run diagnostics and display results directly in the conversation.

Instructions
Call the ctx_doctor MCP tool directly. It runs all checks server-side and returns a markdown checklist.
Display the results verbatim — they are already formatted as a checklist with [x] PASS, [ ] FAIL, [-] WARN.
Fallback (only if MCP tool call fails): Derive the plugin root from this skill's base directory (go up 2 levels — remove /skills/ctx-doctor), then run with Bash:
CLI="<PLUGIN_ROOT>/cli.bundle.mjs"; [ ! -f "$CLI" ] && CLI="<PLUGIN_ROOT>/build/cli.js"; node "$CLI" doctor

Re-display results as a markdown checklist.
Weekly Installs
171
Repository
mksglu/context-mode
GitHub Stars
11.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass