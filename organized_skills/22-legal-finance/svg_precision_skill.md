---
rating: ⭐⭐
title: svg-precision-skill
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/svg-precision-skill
---

# svg-precision-skill

skills/dkyazzentwatwa/chatgpt-skills/svg-precision-skill
svg-precision-skill
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill svg-precision-skill
SKILL.md
SVG Precision Skill

Build SVGs from explicit scene specifications, then validate before handing them off.

Workflow
Translate the request into a concrete spec with fixed dimensions and coordinates.
Use references/spec.md for templates and references/recipes.md for stable layout patterns.
Build the SVG with scripts/svg_cli.py build.
Validate with scripts/svg_cli.py validate.
Render a PNG preview when the user needs a quick visual check.
Rules
Set viewBox, width, and height explicitly.
Prefer absolute coordinates and simple shapes.
Treat text as risky when exact rendering matters.
Avoid exotic filters unless they are necessary and testable.
Weekly Installs
41
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass