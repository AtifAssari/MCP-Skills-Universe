---
rating: ⭐⭐⭐
title: async-repl-protocol
url: https://skills.sh/parcadei/continuous-claude-v3/async-repl-protocol
---

# async-repl-protocol

skills/parcadei/continuous-claude-v3/async-repl-protocol
async-repl-protocol
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill async-repl-protocol
SKILL.md
Async REPL Protocol

When working with Agentica's async REPL harness for testing.

Rules
1. Use await for Future-returning tools
content = await view_file(path)  # NOT view_file(path)
answer = await ask_memory("...")

2. Single code block per response

Compute AND return in ONE block. Multiple blocks means only first executes.

# GOOD: Single block
content = await view_file(path)
return any(c.isdigit() for c in content)

# BAD: Split blocks (second block never runs)
content = await view_file(path)

Weekly Installs
297
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass