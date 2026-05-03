---
rating: ⭐⭐
title: forge-status
url: https://skills.sh/fwehrling/forge/forge-status
---

# forge-status

skills/fwehrling/forge/forge-status
forge-status
Installation
$ npx skills add https://github.com/fwehrling/forge --skill forge-status
SKILL.md
/forge-status — FORGE Sprint Status

Displays the current sprint status by reading .forge/sprint-status.yaml.

Workflow

Load context:

Read .forge/memory/MEMORY.md for project context
Read the latest session from .forge/memory/sessions/ for continuity

Read sprint data: Parse .forge/sprint-status.yaml

Display summary table:

FORGE Sprint Status — <project name>
──────────────────────────────────────
Sprint    : #<id>
Stories   : X completed / Y in_progress / Z pending / W blocked

| Story       | Status      | QA      | Review  | Assignee |
|-------------|-------------|---------|---------|----------|
| STORY-001   | completed   | PASS    | CLEAN   | dev      |
| STORY-002   | in_progress | —       | —       | dev      |
| STORY-003   | pending     | —       | —       | —        |
| STORY-004   | blocked     | —       | —       | —        |

Metrics:
  Tests    : XX pass / Y fail
  Coverage : XX%
  Velocity : X pts/sprint

Blockers:
  - STORY-004 blocked by STORY-002

Backlog (not in sprint):
  - STORY-010 — <title>
  - STORY-011 — <title>


Identify next story: First unblocked pending story

Suggest next action: /forge-build STORY-XXX

Backlog section: List all story files in docs/stories/ and compare with stories in the sprint. Display stories NOT in the current sprint as "Backlog" with their ID and title (read from the story file's front matter or first heading). This gives visibility on upcoming work outside the sprint.

Weekly Installs
14
Repository
fwehrling/forge
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass