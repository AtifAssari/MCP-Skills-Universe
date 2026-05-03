---
rating: ⭐⭐
title: obsidian-link-graph
url: https://skills.sh/galaxy-dawn/claude-scholar/obsidian-link-graph
---

# obsidian-link-graph

skills/galaxy-dawn/claude-scholar/obsidian-link-graph
obsidian-link-graph
Installation
$ npx skills add https://github.com/galaxy-dawn/claude-scholar --skill obsidian-link-graph
SKILL.md
Obsidian Link Graph

This is a legacy compatibility helper.

Despite the name, the current default workflow is not graph-heavy. Use this skill to repair navigation among existing canonical notes, not to generate graph artifacts by default.

Responsibilities
strengthen wikilinks among 00-Hub.md, 01-Plan.md, Knowledge/, Papers/, Experiments/, Results/, Writing/, and Daily/
improve backlinks where a durable relationship is already clear
help route a new reference to the best existing canonical note
reduce disconnected durable notes without creating concept or dataset sprawl
Link heuristics
Prefer one canonical note per durable object.
Link through stable project objects, not ad-hoc phrases.
Avoid overlinking every paragraph; keep only meaningful edges.
Prefer repairing existing links over creating new auxiliary notes.
If the best target is unclear, narrow the search first and use find-canonical-note from obsidian-project-memory when helpful.
Do not assume by default
Concepts/
Datasets/
Maps/
Views/
.canvas
.base

Create those only if the user explicitly asks for them.

Weekly Installs
45
Repository
galaxy-dawn/cla…-scholar
GitHub Stars
3.5K
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass