---
rating: ⭐⭐
title: no-polling-agents
url: https://skills.sh/parcadei/continuous-claude-v3/no-polling-agents
---

# no-polling-agents

skills/parcadei/continuous-claude-v3/no-polling-agents
no-polling-agents
Installation
$ npx skills add https://github.com/parcadei/continuous-claude-v3 --skill no-polling-agents
SKILL.md
No Polling for Background Agents

When launching parallel background agents, do NOT poll with sleep loops.

Pattern

Background agents write to status files when complete. Wait for them naturally.

DO
Launch agents with run_in_background: true
Continue with other work while agents run
Check status file only when user asks or when you need results to proceed
Trust the agent completion system
DON'T
Run sleep 10 && cat status.txt in loops
Continuously poll for completion
Waste tokens checking status repeatedly
Block on agents unless absolutely necessary
When to Check Status
User explicitly asks "are they done?"
You need agent output to proceed with next task
Significant time has passed and user is waiting
Example
// Launch agents
Task({ ..., run_in_background: true })
Task({ ..., run_in_background: true })

// Continue with other work or conversation
// Agents will write to status file when done

// Only check when needed
cat .claude/cache/status.txt

Source

User feedback: "You can just wait until everyone pings you"

Weekly Installs
300
Repository
parcadei/contin…laude-v3
GitHub Stars
3.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass