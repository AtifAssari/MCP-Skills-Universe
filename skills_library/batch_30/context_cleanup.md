---
title: context-cleanup
url: https://skills.sh/jsonlee12138/agent-team/context-cleanup
---

# context-cleanup

skills/jsonlee12138/agent-team/context-cleanup
context-cleanup
Installation
$ npx skills add https://github.com/jsonlee12138/agent-team --skill context-cleanup
SKILL.md
context-cleanup
Audience
controller
worker
Triggers
clean context
session drift
re-anchor context
resume after pause
phase transition
CLI Binding
agent-team context-cleanup
This skill is a standalone context-cleanup and file re-anchoring entry.
Required Entry
controller/main: MUST read .agent-team/rules/index.md first.
worker: MUST read worker.yaml first.
Expansion
controller/main: read only the rule files matched from .agent-team/rules/index.md, then the current workflow/task artifacts.
worker: read task.yaml after worker.yaml, then context.md and referenced materials only when needed.
Hard Rules
Clean session context, not file contents.
Never skip the required entry file.
Never default to scanning all rule bodies or all task context files.
Never describe this skill as context compression.
Boundary
Use this skill to stabilize context and re-anchor from files.
Use worker-recovery for routine worker task resume when the problem is simply recovering the current assignment.
Weekly Installs
24
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