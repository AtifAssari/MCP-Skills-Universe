---
title: ez-ha
url: https://skills.sh/araa47/ez-ha/ez-ha
---

# ez-ha

skills/araa47/ez-ha/ez-ha
ez-ha
Installation
$ npx skills add https://github.com/araa47/ez-ha --skill ez-ha
SKILL.md
ha — Home Assistant CLI
Setup

Set HA_URL and HA_TOKEN env vars (or .env file).

Usage
Find entities first — if the user mentions a device/room, run ha search <name> or ha <domain> to discover real entity IDs before acting.
Act — ha <domain> <action> <entity_id> [args] (e.g. ha fan speed bedroom 60, ha cover open balcony_awning)
Generic power — ha on|off|toggle <entity_id> works for any entity.
Fuzzy match — ha scene|script|button [name] — omit name to list, provide name to activate (substring match).
Add -v for verbose JSON output.
Weekly Installs
11
Repository
araa47/ez-ha
GitHub Stars
3
First Seen
Mar 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass