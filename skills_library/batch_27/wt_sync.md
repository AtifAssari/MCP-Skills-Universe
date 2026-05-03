---
title: wt-sync
url: https://skills.sh/michael-menard/monorepo/wt-sync
---

# wt-sync

skills/michael-menard/monorepo/wt-sync
wt-sync
Installation
$ npx skills add https://github.com/michael-menard/monorepo --skill wt-sync
SKILL.md
/wt:sync - Sync Worktree with Upstream
Description

Quick command to sync the current worktree with upstream changes from the remote repository.

Usage
/wt:sync

What It Does

This slash command:

Activates the Git Worktree Manager skill (@git-worktree)
Automatically runs the *sync command
Syncs your worktree with the remote branch
Workflow

The command will:

Check working directory - Verify it's clean (or offer to stash)
Fetch from origin - Get latest remote changes
Ask merge preference - Rebase or merge?
Sync the branch - Apply the chosen strategy
Show results - Display what changed
Benefits

✅ Stay Updated - Keep worktree in sync with remote ✅ Safe Process - Handles uncommitted changes ✅ Flexible - Choose rebase or merge ✅ Automatic Stash - Stashes and restores changes

Notes
If you have uncommitted changes, they'll be stashed and restored
You can choose between rebase (cleaner) or merge (safer)
The command will show you what changed after syncing
Weekly Installs
21
Repository
michael-menard/monorepo
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass