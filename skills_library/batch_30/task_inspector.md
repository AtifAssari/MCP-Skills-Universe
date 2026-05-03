---
title: task-inspector
url: https://skills.sh/jsonlee12138/agent-team/task-inspector
---

# task-inspector

skills/jsonlee12138/agent-team/task-inspector
task-inspector
Installation
$ npx skills add https://github.com/jsonlee12138/agent-team --skill task-inspector
SKILL.md
task-inspector
Audience
controller
worker
human
Triggers
inspect task
task status
list tasks
show task
CLI Binding
agent-team task list
agent-team task show
Required Entry
controller/human: MUST read .agent-team/rules/index.md first.
worker: MUST read worker.yaml first.
Expansion
Load only the task artifact or task lookup needed for the read-only question.
Boundary
This skill is read-only.
If the prompt includes create, assign, done, or archive intent, route to task-orchestrator instead.
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