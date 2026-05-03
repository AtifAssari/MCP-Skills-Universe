---
title: daily-standup
url: https://skills.sh/seangjr/product-skills/daily-standup
---

# daily-standup

skills/seangjr/product-skills/daily-standup
daily-standup
Installation
$ npx skills add https://github.com/seangjr/product-skills --skill daily-standup
SKILL.md

Error handling convention for ALL bash commands in this skill:

IF command exits non-zero → capture stderr, print diagnostic, then fallback:
✗ {command} failed: {stderr summary}
  → Try: {suggested fix}
  → Fallback: {what the skill does instead}

IF command returns empty stdout when a result is expected → treat as ⚠ warn, note it, proceed
Never stop the entire skill for a single command failure — degrade gracefully and skip the affected section
0. Validate Environment

Check Linear CLI:

Run linear auth whoami 2>&1

IF command not found → set LINEAR_AVAILABLE=false, warn:

✗ linear CLI not found
  → Try: Install from https://github.com/schpet/linear-cli
  → Fallback: Running git-only standup (Linear sections will be skipped)


ELIF output contains auth error or exit code non-zero → set LINEAR_AVAILABLE=false, warn:

✗ linear CLI not authenticated
  → Try: Run `linear auth` to log in
  → Fallback: Running git-only standup


ELSE → LINEAR_AVAILABLE=true

Check if inside a git repo: git rev-parse --is-inside-work-tree 2>&1 (still useful without one, just skip git sections)

Read project scope:

IF .linear-project exists:
Read and trim: PROJECT=$(cat .linear-project | tr -d '\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
IF empty after trim → continue unscoped
ELSE → note: "Scoped to Linear project: {name}"
IF missing → continue unscoped (no warning — standup should be frictionless)
Store PROJECT_FLAG as ${PROJECT:+--project "$PROJECT"} for use in all linear calls
1. Gather Data

From Linear (skip entirely if LINEAR_AVAILABLE=false):

linear issue list -s completed --limit 10 $PROJECT_FLAG 2>&1 — recently completed
IF fails → warn and set COMPLETED_ISSUES=empty
linear issue list -s started --limit 10 $PROJECT_FLAG 2>&1 — in-progress
IF fails → warn and set STARTED_ISSUES=empty
linear issue list -s unstarted --limit 10 $PROJECT_FLAG 2>&1 — backlog
IF fails → warn and set BACKLOG_ISSUES=empty

From Git (if in a repo):

git log --oneline --since="24 hours ago" — yesterday's commits
git log --oneline --since="48 hours ago" — extended window for stale detection
git branch --list — active branches
Current branch

From GSD (if .planning/ exists):

Read STATE.md for phase context
Check for incomplete phases
2. Build Standup Report

Print a formatted report:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 PRODUCT ► DAILY STANDUP [{project-name or "All Projects"}]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Done (last 24h):
  ✓ ENG-123 — Added auth flow (3 commits)
  ✓ ENG-124 — Fixed mobile nav regression

In Progress:
  → ENG-125 — Payment integration (branch: eng-125-payments, 2 commits)
  ⚠ ENG-126 — Dashboard redesign (no commits in 3 days)

Up Next:
  ○ ENG-127 — Urgent — API rate limiting
  ○ ENG-128 — High — Email notifications

Blockers:
  ❌ ENG-126 — Stale: in-progress since Mon, no commits since then
  ❌ ENG-129 — Blocked by ENG-125 (payment integration)

3. Detect Issues

Automatically flag problems:

Stale issues:

Any issue In Progress with no matching commits in 48h+
For each: note how long it's been stale

Orphan work:

Commits in the last 24h that don't reference any Linear issue
IF scoped: "Found 3 commits not tied to any issue in {project-name}. Track them?"
IF unscoped: "Found 3 commits not tied to any Linear issue. Track them?"

Overloaded WIP:

If more than 3 issues are In Progress simultaneously
"You have N issues in progress. Consider finishing some before starting new ones."

Due date warnings:

Any issue due today or overdue
"ENG-130 is due today and still In Progress"

GSD misalignment (if .planning/ exists):

Active GSD phase that doesn't match any In Progress Linear issue
Linear issue In Progress with no corresponding GSD phase
4. Focus Plan

Based on the data, propose a focus plan for today:

Suggested focus for today:
──────────────────────────
1. [Priority] ENG-126 — Unblock: dashboard redesign has been stalled 3 days
2. [Continue] ENG-125 — Payment integration (in progress, momentum)
3. [Start] ENG-127 — API rate limiting (urgent, unstarted)


Explain the reasoning briefly:

Why this order (urgency, staleness, momentum, dependencies)
What to skip or defer if time is short
5. Confirm or Adjust

Ask: "Does this plan work for today, or do you want to adjust priorities?"

Looks good → "Alright. Run /product:start-task when you're ready to pick up the first item."
Adjust → gather changes, update the plan
IF a stale issue was flagged: Ask: "What's the status on ENG-126? Should I update Linear?"
Still working → keep as-is
Blocked → add blocker comment
Deprioritized → move back to backlog
Done → move to Done

<success_criteria>

 Complete picture of yesterday's work, current state, and upcoming work
 Every stale or blocked issue surfaced with explicit user resolution
 Concrete focus plan for today presented
 User confirmed or adjusted the plan
 Any Linear status corrections applied </success_criteria>
Weekly Installs
8
Repository
seangjr/product-skills
First Seen
Apr 2, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass