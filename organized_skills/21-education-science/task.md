---
rating: ⭐⭐⭐
title: task
url: https://skills.sh/wintree86/plan-task-fix/task
---

# task

skills/wintree86/plan-task-fix/task
task
Installation
$ npx skills add https://github.com/wintree86/plan-task-fix --skill task
SKILL.md
Task Manager

Track execution against the live plan.md.

Usage
/task
/task summary
/task update
/task done
/task verify
/task wrap


If a command needs clarification, ask one short plain-text question. Do not rely on environment-specific interactive tools.

File Detection

plan.md search order:

.claude-docs/plan.md
.claude/docs/plan.md
docs/plan.md
PLAN.md
plan.md

Related files live in the same document folder:

progress.md
archive.md
knowledge.md
context.md
backlog.md
Role Split

Use the documents this way:

plan.md: committed roadmap, active feature work, and tasks you explicitly intend to execute
backlog.md: bugs, improvements, and tech debt discovered during work
wrap: combines plan.md, backlog.md, and recent changes into the next-session handoff

Escalation rule:

keep small fixes in backlog.md
promote larger or scheduled work into plan.md
during wrap, important open fixes may appear in context.md and the recommended next tasks
Assumptions About plan.md

Expected schema:

## Progress Overview
## Development Plan
### Phase N: Name
**Status:** pending|in-progress|completed|archived
checklist items - [ ] N.M Task

Archived phases stay in plan.md as summary stubs so overall progress remains readable.

Commands
/task or /task summary

Summarize:

overall progress
each phase status
active phase
next 1-3 incomplete tasks from the first non-archived unfinished phase
/task update

Refresh progress metadata from plan.md.

Rules:

Count checked and unchecked tasks for non-archived phases directly from checklist lines.
For archived phases, preserve the existing Progress Overview row unless detailed counts are still present.
Update each phase status:
pending: none complete
in-progress: some complete
completed: all checklist tasks complete
archived: explicitly marked archived
Recalculate Overall.
Refresh Last Updated.
Append a short dated entry to progress.md.
/task done

Mark completed tasks conservatively.

Rules:

Inspect the current session's code or document changes.
Match only when implemented work clearly corresponds to an unchecked task.
If unsure, do not mark it complete.
After marking tasks, run the same table refresh rules as /task update.
/task verify

Compare plan.md against the working tree.

Rules:

Focus on the first in-progress phase; if none exist, use the first pending phase.
Use available file search and read tools to verify that the task appears implemented.
Report three buckets: verified, partial, not found.
Skip archived phases unless the user explicitly asks to inspect them.
/task wrap

Compact context for the next session without losing history.

Primary goal:

make recent work cheaper for the next LLM to load
keep durable detail in dedicated files
keep plan.md readable and current

Workflow:

Review the current plan, backlog, and recent changes.
Append a dated session note to progress.md.
Extract durable insights to knowledge.md.
Refresh context.md as the primary short-form handoff document.
If a phase is fully completed and no longer active:
copy its full details to archive.md
replace its detailed checklist in plan.md with an archived summary stub
keep the phase row in Progress Overview
Pull forward important backlog items:
unresolved bugs
recently completed fixes worth remembering
improvements or debt that should affect next-session priorities
Ask for confirmation in plain text before modifying files if the wrap proposes archiving a phase or rewriting context.md substantially.
context.md format

Use a short, high-signal structure:

# Current Context

## Project State
- Overall progress and active phase

## Recently Completed
- 3-5 bullets

## Open Risks / Bugs
- important unresolved items from `backlog.md`

## Next Best Tasks
1. ...
2. ...
3. ...

## Important References
- plan.md: Phase 2
- archive.md: Phase 1
- backlog.md: open high-priority items
- key files or decisions

Output Guidance

Keep responses short:

what was updated
what was verified
what was archived or compacted
next recommended action
Weekly Installs
8
Repository
wintree86/plan-task-fix
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass