---
title: worker-dispatch
url: https://skills.sh/jsonlee12138/agent-team/worker-dispatch
---

# worker-dispatch

skills/jsonlee12138/agent-team/worker-dispatch
worker-dispatch
Installation
$ npx skills add https://github.com/jsonlee12138/agent-team --skill worker-dispatch
SKILL.md
worker-dispatch
Audience
controller
human
Triggers
open worker
dispatch worker
reply to worker
inspect current worker before replying
CLI Binding
agent-team worker open
agent-team worker status
agent-team reply
Required Entry
MUST read .agent-team/rules/index.md first.
Expansion
Load the relevant worker config and referenced task artifact only when required by the dispatch action.
Boundary
This is the controller -> worker dispatch surface.
Do not use this skill to recover a worker's own context; that belongs to worker-recovery.
For read-only fleet inspection with no dispatch or reply intent, prefer worker-inspector.
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