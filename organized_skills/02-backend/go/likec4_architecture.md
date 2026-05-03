---
rating: ⭐⭐
title: likec4-architecture
url: https://skills.sh/timseriakov/likec4-architecture-skill/likec4-architecture
---

# likec4-architecture

skills/timseriakov/likec4-architecture-skill/likec4-architecture
likec4-architecture
Installation
$ npx skills add https://github.com/timseriakov/likec4-architecture-skill --skill likec4-architecture
SKILL.md
LikeC4 Architecture

Model software architecture in LikeC4, keep it executable, and return validation-backed outputs.

Workflow
Scope the model:
Identify system boundary and audience.
Start with context and container views unless user asks otherwise.
Locate model files:
Reuse existing .c4/.likec4 files when present.
If missing, bootstrap from assets/likec4-starter/docs/architecture/model.c4.
Model structure before visuals:
Define stable element IDs and meaningful names.
Add explicit directional relationships with short labels.
Add technology/description fields where helpful.
Keep views focused:
Build small, purposeful views.
Split crowded diagrams by domain, team, or bounded context.
Validate and package:
Run npx likec4 validate and fix all errors.
Provide npx likec4 start preview command.
If requested, provide build/export commands.
Required Quality Gates
Do not leave unlabeled ambiguous relationships.
Do not leave orphan elements that never appear in views.
Prefer domain names over implementation noise in element titles.
Finish only after successful CLI validation.
Command Set

Use the minimal commands needed for the task:

npx likec4 validate
npx likec4 start
npx likec4 build -o ./dist
npx likec4 export png -o ./assets/architecture

Output Contract

When architecture files change, return:

Changed files.
Validation result.
One-line purpose for each view.
Preview/build/export command(s) relevant to the request.
Resources
CLI and modeling checklist: references/likec4-checklist.md
Starter model template: assets/likec4-starter/docs/architecture/model.c4
Bootstrap helper: scripts/bootstrap_likec4_starter.sh
Weekly Installs
37
Repository
timseriakov/lik…re-skill
GitHub Stars
1
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass