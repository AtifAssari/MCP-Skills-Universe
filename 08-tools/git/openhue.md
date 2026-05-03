---
title: openhue
url: https://skills.sh/insight68/skills/openhue
---

# openhue

skills/insight68/skills/openhue
openhue
Installation
$ npx skills add https://github.com/insight68/skills --skill openhue
SKILL.md
OpenHue CLI

Use openhue to control Hue lights and scenes via a Hue Bridge.

Setup

Discover bridges: openhue discover
Guided setup: openhue setup

Read

openhue get light --json
openhue get room --json
openhue get scene --json

Write

Turn on: openhue set light <id-or-name> --on
Turn off: openhue set light <id-or-name> --off
Brightness: openhue set light <id> --on --brightness 50
Color: openhue set light <id> --on --rgb #3399FF
Scene: openhue set scene <scene-id>

Notes

You may need to press the Hue Bridge button during setup.
Use --room "Room Name" when light names are ambiguous.
Weekly Installs
9
Repository
insight68/skills
GitHub Stars
4
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass