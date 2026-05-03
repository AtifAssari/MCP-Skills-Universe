---
rating: ⭐⭐
title: git-operations-rules
url: https://skills.sh/totto2727-dotfiles/agents/git-operations-rules
---

# git-operations-rules

skills/totto2727-dotfiles/agents/git-operations-rules
git-operations-rules
Installation
$ npx skills add https://github.com/totto2727-dotfiles/agents --skill git-operations-rules
SKILL.md
Git Operations Rules
Rule (CRITICAL)

These rules MUST ALWAYS be followed when performing git operations.

git -C

Do not use git -C <path>. Always cd to the repository directory first, or use absolute paths within the current working directory.

git unstage

Use git unstage to reset the staging area. Do not pass any options.

git unstage

git undo

Use git undo to undo the last commit. Do not pass any options.

git undo

git stash

Do not use shorthand. Use explicit commands:

To save changes: git stash push (not git stash)
To restore: git stash apply (not git stash pop)

Before stashing, stage any new (untracked) files with git add so they are tracked; otherwise they will not be included in the stash.

git add <new-files>
git stash push -m "<message>" -- <paths>

Related Skills
git-commit - Use when creating git commits
file-deletion-rules - Use when deleting files
Weekly Installs
10
Repository
totto2727-dotfi…s/agents
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass