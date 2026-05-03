---
rating: ⭐⭐
title: twig-guide
url: https://skills.sh/708u/twig/twig-guide
---

# twig-guide

skills/708u/twig/twig-guide
twig-guide
Installation
$ npx skills add https://github.com/708u/twig --skill twig-guide
SKILL.md
twig CLI Guide

twig is a CLI tool that simplifies git worktree workflows by automating branch creation, symlinks, and change management in a single command.

Commands Overview
Command	Purpose
twig init	Initialize twig configuration
twig add <name>	Create a new worktree with symlinks
twig remove <branch>...	Remove worktrees and their branches
twig list	List all worktrees
twig clean	Remove unneeded worktrees
twig sync	Sync symlinks and submodules to worktrees
twig overlay	Temporarily overlay another branch's files
Typical Workflows
Start new feature work

Create a new worktree for a feature branch:

twig add feat/new-feature


This creates a worktree at the configured destination directory, creates a new branch if it doesn't exist, and sets up symlinks.

Move current changes to a new branch

When you realize current work should be on a different branch:

twig add feat/correct-branch --carry


The --carry flag moves uncommitted changes to the new worktree. The source worktree becomes clean.

Copy changes to a new branch

When you want changes in both the current and new worktree:

twig add feat/experiment --sync


The --sync flag copies uncommitted changes to both worktrees.

Carry only specific files

When you want to carry only certain files:

twig add feat/new --carry --file "*.go" --file "cmd/**"

Clean up after merging

Remove worktrees for branches that have been merged:

twig clean


This shows candidates and prompts for confirmation. Use --yes to skip the prompt.

Test a feature branch in another worktree

Temporarily apply another branch's file contents:

twig overlay feat/x --target main
# ... test in main worktree ...
twig overlay --restore --target main

Force remove a worktree

Remove a worktree even with uncommitted changes:

twig remove feat/abandoned -f


Use -ff to also remove locked worktrees.

Configuration

see ./references/configuration.md

Command Details

For detailed information on each command, refer to:

./references/commands/add.md - Create worktrees with sync/carry options
./references/commands/remove.md - Remove worktrees and branches
./references/commands/list.md - List worktrees
./references/commands/clean.md - Clean merged worktrees
./references/commands/sync.md - Sync symlinks and submodules
./references/commands/overlay.md - Overlay branch files temporarily
./references/commands/init.md - Initialize configuration
./references/configuration.md - Configuration file details
Weekly Installs
15
Repository
708u/twig
GitHub Stars
20
First Seen
Feb 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass