---
rating: ⭐⭐⭐
title: git-rebase-main
url: https://skills.sh/oocx/tfplan2md/git-rebase-main
---

# git-rebase-main

skills/oocx/tfplan2md/git-rebase-main
git-rebase-main
Installation
$ npx skills add https://github.com/oocx/tfplan2md --skill git-rebase-main
SKILL.md
Git Rebase Main
Purpose

Ensure the current feature branch includes all the latest changes from main before proceeding with code review, UAT, or release. This prevents merge conflicts and ensures tests run against the latest codebase.

Hard Rules
Must
Fetch from origin before rebasing.
Handle rebase conflicts by stopping and reporting to the user.
Verify the branch is not main before rebasing.
Must Not
Force-push without user confirmation.
Rebase if there are uncommitted changes.
Actions
1. Pre-flight Checks
# Ensure we're not on main
current_branch=$(git branch --show-current)
if [[ "$current_branch" == "main" ]]; then
  echo "ERROR: Cannot rebase main onto itself. Switch to a feature branch first."
  exit 1
fi

# Ensure working directory is clean
if [[ -n "$(scripts/git-status.sh --porcelain)" ]]; then
  echo "ERROR: Working directory has uncommitted changes. Commit or stash them first."
  exit 1
fi

2. Fetch and Rebase
git fetch origin
git rebase origin/main

3. Handle Conflicts

If the rebase fails due to conflicts:

Report the conflicting files to the user.
Do NOT attempt to auto-resolve.
Wait for user to resolve and run git rebase --continue.
4. Force Push (with confirmation)

After a successful rebase, the branch history has changed. Ask the user before force-pushing:

git push --force-with-lease origin HEAD

Golden Example
$ git fetch origin && git rebase origin/main
First, rewinding head to replay your work on top of it...
Applying: feat: add new formatting option
$ git push --force-with-lease origin HEAD

Weekly Installs
24
Repository
oocx/tfplan2md
GitHub Stars
163
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass