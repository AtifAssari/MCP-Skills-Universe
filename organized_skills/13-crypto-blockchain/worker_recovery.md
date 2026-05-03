---
rating: ⭐⭐
title: worker-recovery
url: https://skills.sh/jsonlee12138/agent-team/worker-recovery
---

# worker-recovery

skills/jsonlee12138/agent-team/worker-recovery
worker-recovery
Installation
$ npx skills add https://github.com/jsonlee12138/agent-team --skill worker-recovery
SKILL.md
worker-recovery
Audience
worker
Triggers
resume work
recover task
continue current assignment
CLI Binding
Read worker artifacts directly.
Use agent-team task show only when task details must be refreshed from the CLI.
Required Entry
MUST read worker.yaml first.
Expansion
Recovery order is fixed: worker.yaml -> task.yaml -> context.md -> referenced materials only if needed.
Boundary
This is the standard worker recovery path.
Do not use controller assumptions or .agent-team/rules/index.md as the first entry here.
Do not use this skill for worker -> main reporting; that belongs to worker-reply-main.
Weekly Installs
22
Repository
jsonlee12138/agent-team
GitHub Stars
24
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass