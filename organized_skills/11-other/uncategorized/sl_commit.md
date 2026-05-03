---
rating: ⭐⭐
title: sl-commit
url: https://skills.sh/flora131/atomic/sl-commit
---

# sl-commit

skills/flora131/atomic/sl-commit
sl-commit
Installation
$ npx skills add https://github.com/flora131/atomic --skill sl-commit
SKILL.md
Smart Sapling Commit

Create well-formatted commits following the Conventional Commits specification using Sapling SCM.

<EXTREMELY_IMPORTANT>

Windows Note: Use the full path to sl.exe to avoid conflicts with PowerShell's built-in sl alias for Set-Location. </EXTREMELY_IMPORTANT>

What This Skill Does
Checks which files have changes with sl status
If there are untracked files to include, adds them with sl add
Performs a sl diff to understand what changes are being committed
Analyzes the diff to determine if multiple distinct logical changes are present
If multiple distinct changes are detected, suggests breaking the commit into multiple smaller commits
For each commit, creates a commit message using conventional commit format
Commands to Use
sl status - Check repository state
sl diff - View pending changes
sl add <files> - Add untracked files
sl commit -m "<message>" - Create commit
Key Sapling Differences from Git
No staging area: Sapling commits all pending changes directly
Amend with auto-restack: sl amend automatically rebases descendant commits
Stacked Diffs: Each commit becomes a separate Phabricator diff
Sapling Commit Commands Reference
Command	Description
sl commit -m "message"	Create a new commit with message
sl commit -A	Add untracked files and commit
sl amend	Amend current commit (auto-rebases descendants)
sl amend --to COMMIT	Amend changes to a specific commit in stack
Important Notes
Follow pre-commit checks if configured
Keep commits small and focused - each becomes a separate Phabricator diff
Use sl amend freely - Sapling handles rebasing automatically
Attribute AI-assisted code authorship
Weekly Installs
114
Repository
flora131/atomic
GitHub Stars
164
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass