---
title: plan
url: https://skills.sh/wintree86/plan-task-fix/plan
---

# plan

skills/wintree86/plan-task-fix/plan
plan
Installation
$ npx skills add https://github.com/wintree86/plan-task-fix --skill plan
SKILL.md
Plan Manager

Manage plan.md as the live project plan.

Usage
/plan
/plan create [description]
/plan add [description]
/plan edit Phase N


If an edit request is incomplete, ask the user a short plain-text follow-up question. Do not rely on environment-specific interactive tools.

File Detection

Project root:

Current working directory
Git root if available

Document folder search order:

.claude-docs/
.claude/docs/
docs/
Project root

plan.md search order:

.claude-docs/plan.md
.claude/docs/plan.md
docs/plan.md
PLAN.md
plan.md

If no document folder exists, create .claude-docs/.

Canonical plan.md Format

Use this schema consistently:

# {Project Name}

**Created:** YYYY-MM-DD
**Last Updated:** YYYY-MM-DD

## Project Overview

{2-4 lines}

## Progress Overview

| Phase | Name | Status | Progress |
|-------|------|--------|----------|
| 1 | MVP | pending | 0/3 (0%) |

**Overall: 0/3 (0%)**

---

## Development Plan

### Phase 1: MVP
**Status:** pending

- [ ] 1.1 Define scope
- [ ] 1.2 Build initial flow
- [ ] 1.3 Add basic validation


Rules:

Task IDs use N.M and never change after creation.
Phase headings use ### Phase N: Name.
Phase status must be one of pending, in-progress, completed, archived.
Archived phases may replace detailed checklists with a short note:
### Phase 1: MVP
**Status:** archived

Archived to `archive.md` on YYYY-MM-DD. Summary: core setup and MVP flow completed.

Commands
/plan

Summarize the plan:

file location
phase list
overall progress
current active or next phase
/plan create [description]

Create a new plan.md using the canonical schema.

Generation rules:

Default to 3-5 phases if the user does not specify a count.
Order phases from MVP to polish.
Keep tasks concrete and small enough for one focused work session.
Include the Progress Overview table from the start.
/plan add [description]

Add tasks or phases.

Rules:

If a phase is specified, append there.
If a new phase is requested, create a new section and matching table row.
If no phase is specified, place tasks in the most appropriate non-archived phase.
Continue numbering from the last task in that phase.
Refresh Last Updated.
/plan edit Phase N

Revise one phase.

Rules:

Show the current phase contents first.
If the user has not said what to change yet, ask one short follow-up question in plain text.
Preserve existing task IDs for unchanged tasks.
Use new IDs only for newly added tasks.
Output Guidance

Keep responses short and operational:

what changed
affected phase
updated counts
suggested next command such as /task update
Notes
plan.md is the live plan, not the long-term memory store.
Use plan.md for committed, scheduled work. Use backlog.md for issues and ideas that are not yet promoted into the plan.
Completed phase detail may move to archive.md, but phase rows in Progress Overview must remain.
task and wrap depend on this schema staying stable.
Weekly Installs
8
Repository
wintree86/plan-task-fix
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykPass