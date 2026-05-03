---
rating: ⭐⭐
title: unity-script-roles
url: https://skills.sh/besty0728/unity-skills/unity-script-roles
---

# unity-script-roles

skills/besty0728/unity-skills/unity-script-roles
unity-script-roles
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-script-roles
SKILL.md
Unity Script Roles

Use this skill before creating a batch of gameplay scripts.

Goal

Turn a rough script list into explicit roles so AI does not generate everything as MonoBehaviour.

Output Format
Script name
Recommended role
Main responsibility
Main dependencies
Why this role fits better than the alternatives
Common Roles
MonoBehaviour bridge
ScriptableObject config/data
pure C# domain/service
presenter / controller
state / state machine node
installer / bootstrap helper
Guardrails

Mode: Both (Semi-Auto + Full-Auto) — advisory only, no REST skills

Do not make every class a MonoBehaviour.
Do not force ScriptableObject onto runtime state that should stay in memory-only objects.
Weekly Installs
12
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