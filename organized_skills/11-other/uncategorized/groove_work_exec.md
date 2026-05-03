---
rating: ⭐⭐
title: groove-work-exec
url: https://skills.sh/andreadellacorte/groove/groove-work-exec
---

# groove-work-exec

skills/andreadellacorte/groove/groove-work-exec
groove-work-exec
Installation
$ npx skills add https://github.com/andreadellacorte/groove --skill groove-work-exec
SKILL.md
groove-work-exec
Outcome

Code, tests, and artifacts are written per the plan. The work task is created/updated in the backend with progress notes. Output is ready for review.

Acceptance Criteria
Implementation matches the plan from /groove-work-plan
Work task body tracks progress with dated notes
Output (code, tests, docs) is complete enough to hand off to /groove-work-review
Stage task created/updated in backend: YYYY-MM-DD, Work
Constraints
Read tasks.backend from .groove/index.md to determine backend
If no prior plan exists, warn the user and ask them to confirm scope before proceeding
Append progress notes to task body as work proceeds — do not overwrite
Do not mark task as completed during this stage — that happens after review
Create stage task via /groove-utilities-task-create if tasks.backend != none (title YYYY-MM-DD, Work)
Weekly Installs
207
Repository
andreadellacorte/groove
GitHub Stars
5
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass