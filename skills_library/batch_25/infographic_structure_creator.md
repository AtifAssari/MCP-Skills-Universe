---
title: infographic-structure-creator
url: https://skills.sh/antvis/infographic/infographic-structure-creator
---

# infographic-structure-creator

skills/antvis/infographic/infographic-structure-creator
infographic-structure-creator
Installation
$ npx skills add https://github.com/antvis/infographic --skill infographic-structure-creator
SKILL.md
Infographic Structure Creator
Overview

Generate complete Structure component code for the infographic framework, following the project's component rules, layout constraints, and registration requirements.

Workflow
Read references/structure-prompt.md for the full framework rules, allowed components, and output requirements.
Clarify minimal requirements if missing: structure category, layout direction, hierarchy depth, and whether add/remove buttons are needed.
Choose Item vs Items, compute layout from getElementBounds, and plan decor elements under ItemsGroup.
Produce a full TypeScript file: imports, Props extends BaseStructureProps, component implementation, and registerStructure with accurate composites.
Self-check against the constraints in the reference (no unlisted components, no SVG cx/cy/r, correct indexes, empty-state handling).
Notes
Prefer scanning src/designs/structures for similar existing structures to match local patterns when appropriate.
Keep output concise; avoid React-only features (keys, hooks).
Weekly Installs
58
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