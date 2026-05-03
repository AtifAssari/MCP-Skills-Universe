---
title: auramaxx
url: https://skills.sh/aura-industry/auramaxx/auramaxx
---

# auramaxx

skills/aura-industry/auramaxx/auramaxx
auramaxx
Installation
$ npx skills add https://github.com/aura-industry/auramaxx --skill auramaxx
SKILL.md
AuraMaxx Skill

Use this skill when working inside an AuraMaxx or AuraJS game project.

Working Set

Read these files in order:

project-requirements.md
starter-recipes.md
validation-checklist.md
the current project files named by those docs

Use https://www.aurajs.gg/llm.txt only when you need broader public docs context than the local project and installed package sources provide.

Rules
Treat the current project files as the primary source of truth.
Keep src/main.js thin; prefer the registry-backed runtime flow already in the scaffold.
Put durable authored data in config/ or content/, not scene-local constants.
Put mutable runtime state in scenes or src/runtime/app-state.js.
Extend src/starter-utils/ before inventing one-off helpers.
Use auramaxx make instead of hand-wiring new scaffold nouns when a generator exists.
Default Loop
Infer the current game requirements with project-requirements.md.
Choose the starter-specific edit path in starter-recipes.md.
Implement the smallest playable slice that changes one mechanic at a time.
Run the relevant checks from validation-checklist.md.
Retrieval Boundary

Open local project files first. If you still need package-level behavior or template intent, inspect:

node_modules/@auraindustry/aurajs/src/
node_modules/@auraindustry/aurajs/templates/

Use aurajs.gg/llm.txt after that, not before.

Weekly Installs
13
Repository
aura-industry/auramaxx
GitHub Stars
174
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail