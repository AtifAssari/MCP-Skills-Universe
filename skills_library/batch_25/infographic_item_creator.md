---
title: infographic-item-creator
url: https://skills.sh/antvis/infographic/infographic-item-creator
---

# infographic-item-creator

skills/antvis/infographic/infographic-item-creator
infographic-item-creator
Installation
$ npx skills add https://github.com/antvis/infographic --skill infographic-item-creator
SKILL.md
Infographic Item Generator
Overview

Generate complete Item component code for the infographic framework, following the project's item rules, layout constraints, and registration requirements.

Workflow
Read references/item-prompt.md for the full framework rules, allowed components, and output requirements.
Clarify minimal requirements if missing: desired visuals, required fields (icon/label/value/desc/illus), sizing, and alignment needs.
Use getItemProps to extract custom props and compute layout with getElementBounds.
Produce a full TypeScript file: imports, Props extends BaseItemProps, component implementation, and registerItem with accurate composites.
Self-check against the constraints in the reference (no unlisted components, indexes passed to all wrapped components, correct conditional rendering).
Notes
Prefer scanning src/designs/items for similar items to match local patterns when appropriate.
Keep output concise; avoid React-only features (keys, hooks).
Weekly Installs
57
Repository
antvis/infographic
GitHub Stars
5.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass