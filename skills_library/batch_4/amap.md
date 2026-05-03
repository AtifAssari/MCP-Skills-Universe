---
title: amap
url: https://skills.sh/kaichen/amap-skill/amap
---

# amap

skills/kaichen/amap-skill/amap
amap
Installation
$ npx skills add https://github.com/kaichen/amap-skill --skill amap
SKILL.md
AMap Skill
Quick Start
Ensure AMAP_MAPS_API_KEY is set.
Run bun scripts/amap.ts --help in this skill directory.
Pick the matching command from references/command-map.md.
Workflow
Validate user intent and select one command.
Prefer address commands for route planning when users provide plain addresses.
Keep output as raw AMap JSON without wrapping fields.
Treat any non-zero API business state as failure.
Commands
Full command mapping: references/command-map.md
Ready-to-run examples: references/examples.md
Notes
This skill is script-first and does not run an MCP server.
Only AMAP_MAPS_API_KEY is supported.
Weekly Installs
344
Repository
kaichen/amap-skill
GitHub Stars
108
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn