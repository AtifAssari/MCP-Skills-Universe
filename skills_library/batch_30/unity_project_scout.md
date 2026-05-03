---
title: unity-project-scout
url: https://skills.sh/besty0728/unity-skills/unity-project-scout
---

# unity-project-scout

skills/besty0728/unity-skills/unity-project-scout
unity-project-scout
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-project-scout
SKILL.md
Unity Project Scout

Use this before recommending architecture changes in an existing project.

Inspect First

Collect only the information needed to avoid clashing with the current project:

Unity version and render pipeline
Installed packages and notable dependencies
asmdef layout, if any
Folder structure under Assets/
Whether the project already uses:
ScriptableObject config
service/singleton patterns
event-driven flows
custom inspectors/property drawers
tests
Existing naming and code organization style
Suggested Tools / Inputs
Unity project info and project settings
Script/file search for patterns
Local inspection of Packages/manifest.json, Assets/, and *.asmdef
Output Format
Technical baseline
Existing architectural signals
Existing conventions worth preserving
Existing risks or inconsistencies
Constraints for future suggestions
Unknowns that still need confirmation
Guardrails

Mode: Both (Semi-Auto + Full-Auto) — advisory only, no REST skills

Do not propose a clean-slate architecture if the project already has a consistent pattern.
Do not recommend new dependencies until the current stack is clear.
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