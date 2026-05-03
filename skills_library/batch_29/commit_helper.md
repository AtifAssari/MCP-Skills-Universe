---
title: commit-helper
url: https://skills.sh/chmouel/lazyworktree/commit-helper
---

# commit-helper

skills/chmouel/lazyworktree/commit-helper
commit-helper
Installation
$ npx skills add https://github.com/chmouel/lazyworktree --skill commit-helper
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Commit Helper

Generate a conventional commit message from staged changes.

Changes to commit

!git diff --staged --stat

Detailed diff

!git diff --staged

Recent commit style

!git log --oneline -5

Generate a conventional commit message following these rules:

Follow Conventional Commits 1.0.0 format
50 characters maximum for title, 70 characters for body lines
Use past tense
State what and why only, not how
Use British spelling
Cohesive paragraph unless multiple distinct points require bullet points
Present the commit message for user approval before executing

Example format:

feat: added worktree deletion confirmation

Implemented confirmation dialogue before deleting worktrees to prevent
accidental data loss. The confirmation shows the worktree path and any
uncommitted changes that would be lost.

Weekly Installs
43
Repository
chmouel/lazyworktree
GitHub Stars
215
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass