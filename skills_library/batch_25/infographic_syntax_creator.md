---
title: infographic-syntax-creator
url: https://skills.sh/antvis/infographic/infographic-syntax-creator
---

# infographic-syntax-creator

skills/antvis/infographic/infographic-syntax-creator
infographic-syntax-creator
Installation
$ npx skills add https://github.com/antvis/infographic --skill infographic-syntax-creator
SKILL.md
Infographic Syntax Creator
Overview

Generate AntV Infographic syntax output from user content, following the rules in references/prompt.md.

Workflow
Read references/prompt.md for syntax rules, templates, and output constraints.
Extract the user's key structure: title, desc, items, hierarchy, metrics; infer missing pieces if needed.
Select a template that matches the structure (sequence/list/compare/hierarchy/chart).
Compose the syntax using references/prompt.md as the formatting baseline.
Preserve hard constraints in every output:
Output is a single plain code block; no extra text.
First line is infographic <template-name>.
Use two-space indentation; key/value pairs are key value; arrays use -.
compare-binary-* / compare-hierarchy-left-right-* must have exactly two root nodes, and the actual comparison points belong in each root node's children.
compare-swot / compare-quadrant-* follow their own root-node counts and should not be forced into a binary structure.
Weekly Installs
65
Repository
antvis/infographic
GitHub Stars
5.0K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass