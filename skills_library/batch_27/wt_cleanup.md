---
title: wt-cleanup
url: https://skills.sh/michael-menard/monorepo/wt-cleanup
---

# wt-cleanup

skills/michael-menard/monorepo/wt-cleanup
wt-cleanup
Installation
$ npx skills add https://github.com/michael-menard/monorepo --skill wt-cleanup
SKILL.md
/wt:cleanup - Clean Up Merged Worktrees
Description

Quick command to identify and remove merged or stale worktrees.

Usage
/wt:cleanup

What It Does

This slash command:

Activates the Git Worktree Manager skill (@git-worktree)
Automatically runs the *cleanup command
Helps you clean up old worktrees
Workflow

The command will:

List all worktrees - Show all active worktrees
Identify merged branches - Find branches already merged to main/develop
Close orphaned PRs - For each worktree being removed:
gh pr list --head {branch} --state open --json number
If PR exists: gh pr close {number} --comment "Story worktree cleaned up — closing stale PR"
If gh CLI is unavailable: skip with WARNING, continue cleanup
Ask which to remove - Interactive selection
Remove selected worktrees - Safely delete worktrees
Prune worktree references - Clean up git metadata
Benefits

✅ Smart Detection - Identifies merged branches automatically ✅ Safe Cleanup - Only suggests merged branches ✅ Selective Removal - Choose which to remove ✅ Complete Cleanup - Removes worktrees and branches

Notes
Only suggests worktrees with merged branches
You can choose which ones to remove
Warns about unmerged branches
Prunes git metadata after cleanup
Closes any orphaned GitHub PRs associated with branches being removed (gh CLI optional — skipped with warning if unavailable)
Weekly Installs
21
Repository
michael-menard/monorepo
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn