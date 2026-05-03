---
title: figures4papers-playbook
url: https://skills.sh/l-yifan/skills/figures4papers-playbook
---

# figures4papers-playbook

skills/l-yifan/skills/figures4papers-playbook
figures4papers-playbook
Installation
$ npx skills add https://github.com/l-yifan/skills --skill figures4papers-playbook
SKILL.md
Figures4papers Playbook

Use this skill to find the closest figures4papers example and convert it into a user-specific plotting script quickly.

Workflow
Parse user intent into chart type and domain (for example: grouped bar + benchmark comparison).
Run scripts/example_locator.py to shortlist candidate scripts.
Read references/example_index.md for folder-level context and naming patterns.
Choose one base script and adapt data, labels, and file outputs.
If style consistency is required, co-use scientific-figure-pro for final polishing.
Locator Script

Use keyword and chart filters:

python skills/figures4papers-playbook/scripts/example_locator.py --keyword bar --chart-type grouped_bar


Output includes:

Folder and domain.
Matching script paths.
Recommended run commands.
Notes about the intended figure purpose.
Selection Rules
Prefer exact chart-type match first.
Then prefer domain match (biomed, LLM eval, vision survey, etc.).
If no exact match exists, choose the simplest script with nearest visual grammar.
Keep output paths under a dedicated figures/ directory in the target project.
References
references/example_index.md: curated index of available figure folders and scripts.
Handoff Pattern

After locating a base script, provide:

Selected template path.
What to replace (data arrays, labels, colors, limits).
Command to run.
Expected output files (.png and .pdf).
Weekly Installs
27
Repository
l-yifan/skills
GitHub Stars
3
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass