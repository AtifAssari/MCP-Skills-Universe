---
title: unity-scene-contracts
url: https://skills.sh/besty0728/unity-skills/unity-scene-contracts
---

# unity-scene-contracts

skills/besty0728/unity-skills/unity-scene-contracts
unity-scene-contracts
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-scene-contracts
SKILL.md
Unity Scene Contracts

Use this skill when scene setup needs to be explicit instead of relying on hidden runtime lookups.

Define
Required root objects
Required components on each root
Which references are assigned in Inspector
Which objects act as bootstrap/installers
Which objects are runtime-spawned
Which assumptions should be validated early
Output Format
Scene object contract
Bootstrap sequence
Inspector wiring rules
Validation rules
Hidden dependency risks
Guardrails

Mode: Both (Semi-Auto + Full-Auto) — advisory only, no REST skills

Prefer explicit scene wiring over chains of runtime Find.
Keep bootstrap objects small and focused.
Weekly Installs
13
Repository
besty0728/unity-skills
GitHub Stars
894
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass