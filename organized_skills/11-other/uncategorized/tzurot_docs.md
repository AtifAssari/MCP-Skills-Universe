---
rating: ⭐⭐⭐
title: tzurot-docs
url: https://skills.sh/lbds137/tzurot/tzurot-docs
---

# tzurot-docs

skills/lbds137/tzurot/tzurot-docs
tzurot-docs
Installation
$ npx skills add https://github.com/lbds137/tzurot --skill tzurot-docs
SKILL.md
Documentation & Session Workflow

Invoke with /tzurot-docs for session management and documentation procedures.

Session Start Procedure
Read CURRENT.md - What's the active task?
Read BACKLOG.md High Priority - What's next?
Continue active task or pull next
Session End Procedure
Update CURRENT.md with progress
If task incomplete, note blockers in Scratchpad
Commit with wip: prefix if needed
Work Tracking Files
File	Purpose	Update When
CURRENT.md	Active session - what's happening NOW	Start/end session, task done
BACKLOG.md	Everything else - all queued work	New ideas, triage, completion

Tags: 🏗️ [LIFT] refactor/debt | ✨ [FEAT] feature | 🐛 [FIX] bug | 🧹 [CHORE] maintenance

CURRENT.md Structure
# Current

> **Session**: YYYY-MM-DD
> **Version**: v3.0.0-beta.XX

## Session Goal

_One sentence on what we're doing today._

## Active Task

🏗️ `[LIFT]` **Task Name**

- [ ] Subtask 1
- [ ] Subtask 2

## Scratchpad

_Error logs, decisions, API snippets._

## Recent Highlights

- **beta.XX**: Brief description

BACKLOG.md Structure
## Inbox

_New items. Triage to appropriate section later._

## High Priority

_Top 3-5 items to pull into CURRENT next._

## Epic: [Theme Name]

_Group related work by project._

## Smaller Items

_Opportunistic work._

## Icebox

_Ideas for later._

Workflow Operations
Intake (New Idea)

Add to Inbox in BACKLOG.md with a tag:

- ✨ `[FEAT]` **Feature Name** - Brief description

Start Work (Pull)
Cut task from BACKLOG.md
Paste into CURRENT.md under Active Task
Add checklist if needed
Update Session Goal
Complete Work (Done)
Mark task complete in CURRENT.md
Move to Recent Highlights (keep last 3-5)
Pull next task from BACKLOG High Priority
Documentation Standards

For doc placement, naming, and lifecycle rules, see .claude/rules/07-documentation.md.

References
Current session: CURRENT.md
All work items: BACKLOG.md
Documentation standards: .claude/rules/07-documentation.md
Documentation audit: .claude/skills/tzurot-doc-audit/SKILL.md
Weekly Installs
14
Repository
lbds137/tzurot
GitHub Stars
8
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass