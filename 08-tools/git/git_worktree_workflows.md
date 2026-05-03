---
title: git-worktree-workflows
url: https://skills.sh/mthines/gw-tools/git-worktree-workflows
---

# git-worktree-workflows

skills/mthines/gw-tools/git-worktree-workflows
git-worktree-workflows
Installation
$ npx skills add https://github.com/mthines/gw-tools --skill git-worktree-workflows
SKILL.md
Git Worktree Workflows

Master Git worktrees using the gw CLI tool for optimized parallel development workflows.

Rules
Rule	Description
fundamentals	HIGH - Core concepts of Git worktrees, what they share/don't share, when to use them
creation	HIGH - Creating worktrees with gw add, remote fetch behavior, auto-copy files
navigation	MEDIUM - Navigating with gw cd and gw checkout, shell integration setup
inspection	LOW - Listing worktrees with gw list, understanding worktree states
cleanup	MEDIUM - Removing worktrees, gw clean, gw prune, disk space management
troubleshooting	HIGH - Common errors and solutions, recovery procedures
Workflow Patterns
Pattern	Description
feature-branch	HIGH - Feature development workflow with worktrees
hotfix	HIGH - Urgent bug fixes without interrupting feature work
code-review	HIGH - Review PRs in isolated environments with gw pr
parallel-testing	MEDIUM - Test across Node versions or configurations
Quick Reference
Task	Command
Create worktree	gw add feature-name
Create from different branch	gw add feature-name --from develop
Create from staged files	gw checkout feature-name --from-staged
Navigate to worktree	gw cd feature-name
List all worktrees	gw list
Remove worktree	gw remove feature-name
Check out PR	gw pr 123
Update with main	gw update
Batch cleanup	gw clean
Full cleanup	gw prune
Key Principles
Use worktrees for parallel work: Keep main ready while developing features.
Always use gw add: Gets auto-copy, shell navigation, smart fetch.
One branch per worktree: Cannot check out same branch in multiple worktrees.
Clean up when done: Use gw remove, gw clean, or gw prune.
Related Skills
gw-config-management - Configure auto-copy files and hooks
autonomous-workflow - Autonomous development in isolated worktrees
Resources
Getting Started Example
Parallel Development Example
Troubleshooting Guide
gw CLI Documentation
Weekly Installs
21
Repository
mthines/gw-tools
GitHub Stars
7
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn