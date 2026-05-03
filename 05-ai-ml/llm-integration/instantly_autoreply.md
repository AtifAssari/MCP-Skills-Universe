---
title: instantly-autoreply
url: https://skills.sh/aiagentwithdhruv/skills/instantly-autoreply
---

# instantly-autoreply

skills/aiagentwithdhruv/skills/instantly-autoreply
instantly-autoreply
Installation
$ npx skills add https://github.com/aiagentwithdhruv/skills --skill instantly-autoreply
SKILL.md
Instantly Auto-Reply
Goal

Auto-generate intelligent replies to incoming emails from Instantly campaigns using campaign-specific knowledge bases.

Scripts
./scripts/instantly_autoreply.py - Main auto-reply script
How It Works
Receives incoming email thread from Instantly webhook
Looks up campaign ID in knowledge base sheet
Retrieves campaign context (offers, credentials, tone)
Generates contextual reply using Claude
Sends reply through Instantly API
Knowledge Base

Spreadsheet: 1QS7MYDm6RUTzzTWoMfX-0G9NzT5EoE2KiCE7iR1DBLM

Each row contains:

Campaign ID
Campaign Name
Knowledge Base (service details, offers, credentials)
Reply Examples (tone/style guidance)
Usage
# Process incoming thread
python3 ./scripts/instantly_autoreply.py --thread_id <id>

Environment
INSTANTLY_API_KEY=your_key
ANTHROPIC_API_KEY=your_key

Schema
Inputs
Name	Type	Required	Description
thread_id	string	Yes	Instantly thread ID to reply to
Outputs
Name	Type	Description
reply_sent	boolean	Whether reply was sent successfully
Credentials
Name	Source
INSTANTLY_API_KEY	.env
ANTHROPIC_API_KEY	.env
Composable With

Skills that chain well with this one: instantly-campaigns

Cost

Claude API per reply

Weekly Installs
19
Repository
aiagentwithdhruv/skills
GitHub Stars
9
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykWarn