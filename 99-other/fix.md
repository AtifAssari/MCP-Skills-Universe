---
title: fix
url: https://skills.sh/wintree86/plan-task-fix/fix
---

# fix

skills/wintree86/plan-task-fix/fix
fix
Installation
$ npx skills add https://github.com/wintree86/plan-task-fix --skill fix
SKILL.md
Fix Manager

Manage backlog.md.

Role Split

Use backlog.md for:

bugs found during implementation
improvements not yet committed into the roadmap
tech debt notes and cleanup candidates

Promote an item from backlog.md into plan.md when:

it needs planned multi-step execution
it is large enough to span a session or phase
it changes roadmap priorities

/task wrap should still read backlog.md so important fix items appear in context.md and next-task recommendations.

Usage
/fix
/fix "description"
/fix bug "description"
/fix improve "description"
/fix debt "description"
/fix done [ID]
/fix clean


If the command needs clarification, ask one short plain-text follow-up question.

File Detection

backlog.md search order:

.claude-docs/backlog.md
.claude/docs/backlog.md
docs/backlog.md
BACKLOG.md
backlog.md

If no document folder exists, create the file in the project root or .claude-docs/ if that folder is created for other docs.

Canonical backlog.md Format
# Backlog

**Last Updated:** YYYY-MM-DD

## Bugs
- [ ] B1 [high] Login keyboard overlap (YYYY-MM-DD)
- [x] B2 Card animation flicker (YYYY-MM-DD) -- YYYY-MM-DD

## Improvements
- [ ] I1 Loading speed optimization (YYYY-MM-DD)

## Tech Debt
- [ ] T1 Replace deprecated API calls (YYYY-MM-DD)


Rules:

Priority tags are optional: [critical], [high], [medium], [low]
Existing files without priority tags remain valid.
IDs are never reused.
Commands
/fix

Show open items grouped by section.

/fix bug|improve|debt "description"

Add an item to the target section.

Rules:

Accept optional leading priority tags in the description, for example:
/fix bug "[high] Keyboard overlap on iPhone SE"
/fix improve "[low] Add haptic feedback"
If no priority is provided, leave it omitted or treat it as medium in summaries.
/fix "description"

Auto-classify using keywords.

Priority rules:

preserve any explicit leading priority tag
otherwise leave priority blank

Category rules:

bug keywords: bug, error, broken, fail, issue, problem, crash, 안됨, 오류
improvement keywords: improve, better, optimize, performance, UX, 개선, 최적화
tech debt keywords: deprecated, refactor, cleanup, legacy, upgrade, 리팩토링
default category: bug
/fix done [ID]

Mark the item complete and append -- YYYY-MM-DD.

If no ID is provided:

list open items
ask the user which ID to close in plain text
/fix clean

Remove completed items after plain-text confirmation.

Output Guidance

Keep responses short:

added or completed item IDs
section affected
remaining open count
Weekly Installs
9
Repository
wintree86/plan-task-fix
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass