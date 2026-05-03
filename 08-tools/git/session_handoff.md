---
title: session-handoff
url: https://skills.sh/rohitg00/pro-workflow/session-handoff
---

# session-handoff

skills/rohitg00/pro-workflow/session-handoff
session-handoff
Installation
$ npx skills add https://github.com/rohitg00/pro-workflow --skill session-handoff
SKILL.md
Session Handoff

Different from wrap-up. Wrap-up is a checklist for you. Handoff is a document written for the next session.

Trigger

Use when saying "handoff", "continue later", "pass to next session", "session transfer", or ending a session and wanting to resume smoothly.

Workflow
Gather current state from git.
List completed, in-progress, and pending work.
Note key decisions made and their reasoning.
Capture any learnings from this session.
Generate a resume command for the next session.
Commands
git status
git diff --stat
git log --oneline -5
git branch --show-current

Output
# Session Handoff — [date] [time]

## Status
- **Branch**: feature/xyz
- **Commits this session**: 3
- **Uncommitted changes**: 2 files modified
- **Tests**: passing / failing / not run

## What's Done
- [completed task 1]
- [completed task 2]

## What's In Progress
- [current task with context on where you stopped]
- [file:line that needs attention next]

## What's Pending
- [next task that hasn't been started]
- [blocked items with reason]

## Key Decisions Made
- [decision 1 and why]
- [decision 2 and why]

## Learnings Captured
- [Category] Rule (from this session)

## Files Touched
- `path/to/file1.ts` — [what changed]
- `path/to/file2.ts` — [what changed]

## Gotchas for Next Session
- [thing that tripped you up]
- [non-obvious behavior discovered]

## Resume Command
> Continue working on [branch]. [1-2 sentence context]. Next step: [specific action].

Guardrails
Write for the reader (next session), not the writer.
Include specific file paths and line numbers where relevant.
The resume command should be copy-pasteable into the next session.
Keep it factual — describe changes functionally, don't infer motivation.
Weekly Installs
28
Repository
rohitg00/pro-workflow
GitHub Stars
2.0K
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass