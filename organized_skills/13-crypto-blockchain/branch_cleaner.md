---
rating: ⭐⭐
title: branch-cleaner
url: https://skills.sh/jmerta/codex-skills/branch-cleaner
---

# branch-cleaner

skills/jmerta/codex-skills/branch-cleaner
branch-cleaner
Installation
$ npx skills add https://github.com/jmerta/codex-skills --skill branch-cleaner
SKILL.md
Branch cleaner
Goal

Safely identify stale branches and provide explicit delete/prune commands.

Inputs to confirm (ask if missing)
Default branch (main/master/develop).
Remote name (origin) and whether remote deletion is desired.
Safety rules: keep patterns (release/, hotfix/), minimum age, merged-only.
Workflow
Sync and inspect
Run git fetch --prune.
Check git status and note uncommitted changes.
Build candidate lists
Local merged into default: git branch --merged <base>
Local not merged (list only): git branch --no-merged <base>
Remote merged: git branch -r --merged <base>
Stale by date: git for-each-ref --sort=committerdate refs/heads --format="%(committerdate:short) %(refname:short)"
Exclude protected branches
Always keep <base>, current branch, and user-provided patterns.
Confirm with user
Present candidates grouped by local vs remote.
Provide delete commands
Delete branches approved for deletion by the user
Optional GitHub CLI checks
gh pr list --state merged --base <base> to correlate merged branches.
gh pr view <branch> to verify status if needed.
Deliverables
Candidate lists and rationale.
Warnings for unmerged or recently updated branches.
Don't remove remote branches unless explicitly approved.
Weekly Installs
21
Repository
jmerta/codex-skills
GitHub Stars
126
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn