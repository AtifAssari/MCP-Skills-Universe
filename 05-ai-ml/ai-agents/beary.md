---
title: beary
url: https://skills.sh/openclaw-sk4r/beary/beary
---

# beary

skills/openclaw-sk4r/beary/beary
beary
Installation
$ npx skills add https://github.com/openclaw-sk4r/beary --skill beary
SKILL.md
BEARY skill

Before running this skill, read .agents/skills/beary/AGENTS.md and follow it.

Summon behavior:

Use .agents/skills/beary/scripts/is-beary-summon.sh "<raw user message>" to detect whether the raw message is exactly BEARY (case-insensitive, surrounding spaces ignored).
If it matches, print .agents/skills/beary/LOGO.md first.
Then continue with the normal BEARY flow (ask setup questions and run research).
If it does not match, continue normally without printing the logo.

Run the command workflow:

research

Core files:

LOGO.md
scripts/is-beary-summon.sh
commands/research.md
skills/internet-research/SKILL.md
skills/references/SKILL.md
skills/whitepaper-writing/SKILL.md
skills/user-context-template/SKILL.md
templates/*

Configure audience/source/output preferences in .beary/USER.md at the project root. This file is generated from templates/user-context-template.md on first run and lives outside the skill installation directory to survive reinstalls.

Weekly Installs
16
Repository
openclaw-sk4r/beary
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn