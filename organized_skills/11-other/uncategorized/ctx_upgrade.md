---
rating: ⭐⭐⭐
title: ctx-upgrade
url: https://skills.sh/mksglu/context-mode/ctx-upgrade
---

# ctx-upgrade

skills/mksglu/context-mode/ctx-upgrade
ctx-upgrade
Installation
$ npx skills add https://github.com/mksglu/context-mode --skill ctx-upgrade
SKILL.md
Context Mode Upgrade

Pull latest from GitHub and reinstall the plugin.

Instructions
Call the ctx_upgrade MCP tool directly. It returns a shell command to execute.
Run the returned command using your shell execution tool (Bash, shell_execute, etc.).
Display results as a markdown checklist:
## context-mode upgrade
- [x] Pulled latest from GitHub
- [x] Built and installed v1.0.39
- [x] Hooks configured
- [x] Doctor: all checks PASS

Use [x] for success, [ ] for failure. Show actual version numbers.
Tell the user to restart their session to pick up the new version.
Fallback (only if MCP tool call fails): Derive the plugin root from this skill's base directory (go up 2 levels — remove /skills/ctx-upgrade), then run with Bash:
CLI="<PLUGIN_ROOT>/cli.bundle.mjs"; [ ! -f "$CLI" ] && CLI="<PLUGIN_ROOT>/build/cli.js"; node "$CLI" upgrade

Weekly Installs
165
Repository
mksglu/context-mode
GitHub Stars
11.9K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn