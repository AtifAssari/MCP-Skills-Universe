---
rating: ⭐⭐⭐
title: paseo-handoff
url: https://skills.sh/getpaseo/paseo/paseo-handoff
---

# paseo-handoff

skills/getpaseo/paseo/paseo-handoff
paseo-handoff
Installation
$ npx skills add https://github.com/getpaseo/paseo --skill paseo-handoff
SKILL.md
Handoff Skill

Transfer the current task — context, decisions, failed attempts, constraints — to a fresh agent. The receiving agent starts with zero context, so the handoff prompt must be a self-contained briefing.

User's arguments: $ARGUMENTS

Prerequisites

Read the paseo skill — provider for the receiving agent comes from orchestration preferences unless the user names one.

Parsing arguments
Provider — explicit user request first; otherwise resolve from impl preference (or ui if the task is styling-only).
Worktree — "in a worktree" / "worktree" → create a worktree via Paseo with a short branch name derived from the task, based on the current branch.
Task description — anything else the user said.
The handoff prompt

The receiving agent has zero context. Include:

## Task
[Imperative description.]

## Context
[Why this task exists, background needed.]

## Relevant files
- `path/to/file.ts` — [what it is and why it matters]

## Current state
[What's done, what works, what doesn't.]

## What was tried
- [Approach] — [why it failed or was abandoned]

## Decisions
- [Decision — rationale]

## Acceptance criteria
- [ ] [Criterion]

## Constraints
- [Must-not / must-preserve]


Preserve task semantics. Investigate-only → "DO NOT edit files." Fix → "implement the fix." Refactor → "refactor, not rewrite." Carry the user's exact intent.

Launch

Create the agent via Paseo with a [Handoff] <task> title, the briefing as initial prompt, and cwd set to the worktree path if --worktree.

Don't wait by default — the user decides whether to follow along or move on. Tell them the agent ID and how to follow along (the paseo skill explains).

Weekly Installs
609
Repository
getpaseo/paseo
GitHub Stars
5.2K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass