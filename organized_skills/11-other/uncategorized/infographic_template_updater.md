---
rating: ⭐⭐
title: infographic-template-updater
url: https://skills.sh/antvis/infographic/infographic-template-updater
---

# infographic-template-updater

skills/antvis/infographic/infographic-template-updater
infographic-template-updater
Installation
$ npx skills add https://github.com/antvis/infographic --skill infographic-template-updater
SKILL.md
Infographic Template Updater
Overview

Update public template lists and gallery mappings when new templates are added in src/templates.

Workflow
Collect new template names from the added src/templates/*.ts file (object keys).
If templates are composed via spreads (e.g. ...listZigzagTemplates), also confirm the final keys in src/templates/built-in.ts.
Update template lists:
skills/infographic-creator/SKILL.md in the "Available Templates" list.
site/src/components/AIPlayground/Prompt.ts in the template list.
skills/infographic-syntax-creator/references/prompt.md in the template list. Keep existing ordering/grouping; add new list-* entries near other list templates.
Sanity check with rg -n "<template-name>" across the above files to confirm presence.
Notes
Do not remove or rename existing entries.
Keep template names exact and lower-case.
If a template needs example data, update or extend site/src/components/Gallery/datasets.ts to match its structure.
Weekly Installs
54
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