---
rating: ⭐⭐⭐
title: no-task-output
url: https://skills.sh/parcadei/continuous-claude-v3/no-task-output
---

# no-task-output

skills/parcadei/continuous-claude-v3/no-task-output
no-task-output
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill no-task-output
SKILL.md
Never Use TaskOutput

TaskOutput floods the main context window with agent transcripts (70k+ tokens).

Rule

NEVER use TaskOutput tool. Use Task tool with synchronous mode instead.

Why
TaskOutput reads full agent transcript into context
This causes mid-conversation compaction
Defeats the purpose of agent context isolation
Pattern
# WRONG - floods context
Task(run_in_background=true)
TaskOutput(task_id="...")  // 70k tokens dumped

# RIGHT - isolated context, returns summary
Task(run_in_background=false)  // Agent runs, returns summary

Source
Session where TaskOutput caused context overflow
Weekly Installs
298
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