---
rating: ⭐⭐
title: openclaw-map
url: https://skills.sh/wsxqaza12/skill-openclaw-map/openclaw-map
---

# openclaw-map

skills/wsxqaza12/skill-openclaw-map/openclaw-map
openclaw-map
Installation
$ npx skills add https://github.com/wsxqaza12/skill-openclaw-map --skill openclaw-map
SKILL.md
OpenClaw Map

Full reference: references/environment.md

Read it before navigating the file system. It covers:

How to locate the OpenClaw docs on any OS (npm root -g method)
~/.openclaw/ directory layout
Agent workspace location and bootstrap files
Session transcript paths
Cron job format and CLI
Skills loading priority
Gateway daemon management
ACP bridge for IDE integrations
All log file locations
CLI quick reference
Key facts
What	Where
Config	~/.openclaw/openclaw.json
Gateway log	/tmp/openclaw/openclaw-YYYY-MM-DD.log
Cron jobs	~/.openclaw/cron/jobs.json
Sessions	~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl
Default workspace	~/.openclaw/workspace
User skills	~/.openclaw/skills/
Bundled docs	$(npm root -g)/openclaw/docs/
Online docs	https://docs.openclaw.ai
Common tasks

Modify config → edit ~/.openclaw/openclaw.json (hot-reloads automatically; only gateway.* changes need restart)

Add cron job → openclaw cron add --name "..." --cron "..." --session main --system-event "..."

Install a skill → drop skill folder (containing SKILL.md) into ~/.openclaw/skills/

Diagnose issues → openclaw doctor or openclaw logs --follow

Weekly Installs
8
Repository
wsxqaza12/skill…claw-map
GitHub Stars
80
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubFail
SocketFail
SnykPass