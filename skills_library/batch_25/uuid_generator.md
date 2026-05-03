---
title: uuid-generator
url: https://skills.sh/aidotnet/moyucode/uuid-generator
---

# uuid-generator

skills/aidotnet/moyucode/uuid-generator
uuid-generator
Installation
$ npx skills add https://github.com/aidotnet/moyucode --skill uuid-generator
SKILL.md
UUID Generator Tool
Description

Generate various types of unique identifiers including UUID v1, v4, v5, ULID, and nanoid.

Trigger
/uuid command
User needs unique identifiers
User wants to generate IDs
Usage
# Generate UUID v4
python scripts/uuid_generator.py

# Generate multiple UUIDs
python scripts/uuid_generator.py --count 10

# Generate UUID v5 with namespace
python scripts/uuid_generator.py --v5 --namespace dns --name example.com

# Generate short ID
python scripts/uuid_generator.py --short --length 12

Tags

uuid, id, generator, unique, identifier

Compatibility
Codex: ✅
Claude Code: ✅
Weekly Installs
16
Repository
aidotnet/moyucode
GitHub Stars
79
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass