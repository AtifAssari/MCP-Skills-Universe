---
title: sync
url: https://skills.sh/october-academy/agent-plugins/sync
---

# sync

skills/october-academy/agent-plugins/sync
sync
Installation
$ npx skills add https://github.com/october-academy/agent-plugins --skill sync
Summary

Quick git synchronization with remote repository, defaulting to origin main.

Supports multiple sync targets: origin main, origin develop, upstream main (for forks), and custom branches
Automatically checks for uncommitted changes and offers stash, commit, or discard options before syncing
Handles merge conflicts by listing conflicting files and guiding resolution; supports both merge and rebase workflows
Responds to English commands (/sync, /sync develop) and Korean triggers (동기화, 원격에서 가져와, 풀 받아)
SKILL.md
Sync Skill

Quick git synchronization with remote repository.

Usage
Commands
/sync              # Pull from origin main
/sync develop      # Pull from origin develop
/sync upstream     # Pull from upstream main (forks)

Korean Triggers
"동기화"
"원격에서 가져와"
"풀 받아"
Workflow
1. Pre-sync Check
git status


If working directory has uncommitted changes:

Options:

Stash: git stash → sync → git stash pop
Commit first: Suggest using /cp
Discard: Only if user confirms with git checkout .
2. Fetch and Pull

Default (origin main):

git pull origin main


With rebase (cleaner history):

git pull --rebase origin main

3. Report Results

After successful sync:

Synced with origin/main
- 3 commits pulled
- Files changed: 5
- No conflicts

Handling Conflicts

If merge conflicts occur:

List conflicting files
Offer to help resolve
After resolution: git add <files> → git commit
Common Scenarios
Fork Workflow
# Add upstream if not exists
git remote add upstream <original-repo-url>

# Sync with upstream
git fetch upstream
git merge upstream/main

Diverged Branches

If local and remote have diverged:

# Option 1: Merge (default)
git pull origin main

# Option 2: Rebase (cleaner)
git pull --rebase origin main

# Option 3: Reset (destructive, ask user)
git fetch origin
git reset --hard origin/main

Error Handling
Error	Solution
"Uncommitted changes"	Stash or commit first
"Merge conflict"	Help resolve conflicts
"Remote not found"	Check git remote -v
Weekly Installs
1.2K
Repository
october-academy…-plugins
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn