---
title: linear
url: https://skills.sh/lwlee2608/agent-skills/linear
---

# linear

skills/lwlee2608/agent-skills/linear
linear
Installation
$ npx skills add https://github.com/lwlee2608/agent-skills --skill linear
SKILL.md
Linear Issue Management

Interact with Linear.app issues using the linear CLI.

Prerequisites
linear CLI must be installed (linear --version). If missing, install with:
curl -fsSL https://raw.githubusercontent.com/lwlee2608/linear-cli/main/install.sh | bash

LINEAR_API_KEY must be set. Check with echo $LINEAR_API_KEY. If unset, tell the user to export it (export LINEAR_API_KEY="lin_api_...").
Commands
Get an issue
linear issue get ENG-123


Returns: identifier, title, state, team, priority, assignee, description.

Search issues
linear issue search "login bug"
linear issue search "login bug" --limit 50


Returns a table: ID, TITLE, STATE, ASSIGNEE. Default limit is 20.

Weekly Installs
15
Repository
lwlee2608/agent-skills
First Seen
8 days ago
Security Audits
Gen Agent Trust HubFail
SocketWarn
SnykFail