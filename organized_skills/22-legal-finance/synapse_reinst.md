---
rating: ⭐⭐⭐
title: synapse-reinst
url: https://skills.sh/s-hiraoku/synapse-a2a/synapse-reinst
---

# synapse-reinst

skills/s-hiraoku/synapse-a2a/synapse-reinst
synapse-reinst
Installation
$ npx skills add https://github.com/s-hiraoku/synapse-a2a --skill synapse-reinst
SKILL.md
Synapse Re-Instruction

Restore Synapse A2A agent identity and instructions after /clear or context reset.

When to Use
After running /clear (or equivalent context reset)
When the agent no longer recognizes Synapse commands
When A2A communication has stopped working
After any event that clears the agent's initial instructions
Usage

Run the reinst script to output your full Synapse instructions:

# From the source tree
python plugins/synapse-a2a/skills/synapse-reinst/scripts/reinst.py

# From a synced or installed skill copy
cd .claude/skills/synapse-reinst && python scripts/reinst.py


The script reads environment variables set by Synapse at startup (SYNAPSE_AGENT_ID, SYNAPSE_AGENT_TYPE, SYNAPSE_PORT) which persist even after /clear.

Instructions
Run the script above
Read the output carefully — it contains your full Synapse A2A configuration
Follow the instructions as if they were just sent to you
Resume normal operation with A2A communication enabled
How It Works

The script:

Reads Synapse environment variables (set at agent startup, survives /clear)
Looks up your name/role from the agent registry
Loads your instruction template from .synapse/settings.json
Outputs the complete instruction with all placeholders replaced
Weekly Installs
222
Repository
s-hiraoku/synapse-a2a
GitHub Stars
4
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail