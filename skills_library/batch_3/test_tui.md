---
title: test-tui
url: https://skills.sh/openai/codex/test-tui
---

# test-tui

skills/openai/codex/test-tui
test-tui
Installation
$ npx skills add https://github.com/openai/codex --skill test-tui
SKILL.md

You can start and use Codex TUI to verify changes.

Important notes:

Start interactively. Always set RUST_LOG="trace" when starting the process. Pass -c log_dir=<some_temp_dir> argument to have logs written to a specific directory to help with debugging. When sending a test message programmatically, send text first, then send Enter in a separate write (do not send text + Enter in one burst). Use just codex target to run - just codex -c ...

Weekly Installs
601
Repository
openai/codex
GitHub Stars
79.4K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass