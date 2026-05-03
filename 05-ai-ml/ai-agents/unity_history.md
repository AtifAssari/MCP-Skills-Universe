---
rating: ⭐⭐
title: unity-history
url: https://skills.sh/besty0728/unity-skills/unity-history
---

# unity-history

skills/besty0728/unity-skills/unity-history
unity-history
Installation
$ npx skills add https://github.com/besty0728/unity-skills --skill unity-history
SKILL.md
History Skills

Manage Unity Editor undo/redo history.

Guardrails

Mode: Full-Auto required

DO NOT (common hallucinations):

history_list / history_get do not exist → use history_get_current for current undo group
history_clear does not exist → Unity undo history cannot be cleared via API
history_save does not exist → undo history is managed by Unity automatically

Routing:

For simple undo/redo → history_undo / history_redo (this module) or editor_undo / editor_redo
For persistent task-level undo → use workflow module
For conversation-level undo → use workflow module's workflow_session_undo
Skills
history_undo

Undo the last operation. Parameters: None.

history_redo

Redo the last undone operation. Parameters: None.

history_get_current

Get current undo history state. Parameters: None.

Exact Signatures

Exact names, parameters, defaults, and returns are defined by GET /skills/schema or unity_skills.get_skill_schema(), not by this file.

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