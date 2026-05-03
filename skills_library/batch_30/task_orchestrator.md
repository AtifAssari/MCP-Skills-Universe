---
title: task-orchestrator
url: https://skills.sh/jsonlee12138/agent-team/task-orchestrator
---

# task-orchestrator

skills/jsonlee12138/agent-team/task-orchestrator
task-orchestrator
Installation
$ npx skills add https://github.com/jsonlee12138/agent-team --skill task-orchestrator
SKILL.md
task-orchestrator
Audience
controller
human
Triggers
create task
assign task
complete task
archive task
task flow
CLI Binding
agent-team task create
agent-team task list
agent-team task show
agent-team task assign
agent-team task done
agent-team task archive
Required Entry
MUST read .agent-team/rules/index.md first.
Expansion
Load only the task artifacts and rule files required by the current lifecycle action.
Boundary
This is the write-capable task lifecycle entry.
Do not use this skill for worker-only recovery or worker -> main reporting.
If the user only wants read-only task status with no lifecycle mutation intent, prefer task-inspector.
Weekly Installs
23
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