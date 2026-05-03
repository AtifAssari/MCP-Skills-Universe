---
title: agent-manager-skill
url: https://skills.sh/davila7/claude-code-templates/agent-manager-skill
---

# agent-manager-skill

skills/davila7/claude-code-templates/agent-manager-skill
agent-manager-skill
Originally fromsickn33/antigravity-awesome-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill agent-manager-skill
Summary

Manage multiple local CLI agents in parallel tmux sessions with task assignment and monitoring.

Start, stop, and monitor agents running in isolated tmux sessions with log tailing and health checks
Assign tasks to specific agents and track their execution output in real time
Schedule recurring agent work via cron integration for automated workflows
Requires tmux and Python 3; agents are configured in a local agents/ directory
SKILL.md
Agent Manager Skill
When to use

Use this skill when you need to:

run multiple local CLI agents in parallel (separate tmux sessions)
start/stop agents and tail their logs
assign tasks to agents and monitor output
schedule recurring agent work (cron)
Prerequisites

Install agent-manager-skill in your workspace:

git clone https://github.com/fractalmind-ai/agent-manager-skill.git

Common commands
python3 agent-manager/scripts/main.py doctor
python3 agent-manager/scripts/main.py list
python3 agent-manager/scripts/main.py start EMP_0001
python3 agent-manager/scripts/main.py monitor EMP_0001 --follow
python3 agent-manager/scripts/main.py assign EMP_0002 <<'EOF'
Follow teams/fractalmind-ai-maintenance.md Workflow
EOF

Notes
Requires tmux and python3.
Agents are configured under an agents/ directory (see the repo for examples).
Weekly Installs
459
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass