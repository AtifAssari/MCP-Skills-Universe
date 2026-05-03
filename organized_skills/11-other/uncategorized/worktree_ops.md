---
rating: ⭐⭐
title: worktree-ops
url: https://skills.sh/krzysztofsurdy/code-virtuoso/worktree-ops
---

# worktree-ops

skills/krzysztofsurdy/code-virtuoso/worktree-ops
worktree-ops
Installation
$ npx skills add https://github.com/krzysztofsurdy/code-virtuoso --skill worktree-ops
SKILL.md
Worktree Management

Git worktrees let you check out multiple branches of the same repository into separate directories simultaneously. Each worktree has its own working directory and index while sharing the same .git object store and history. This is useful for running parallel development sessions, reviewing a PR while mid-feature, or isolating experimental changes without stashing or committing half-finished work.

Core Principles
Principle	Meaning
Isolation without duplication	Worktrees share git history but keep working directories separate -- no need to clone the repo again
Safety first	Always check for uncommitted changes and unpushed commits before removing a worktree
Clean up after yourself	Stale worktree entries and orphaned branches accumulate -- prune regularly
Convention over configuration	Use a consistent directory layout (.worktrees/<name>/) and branch naming (worktree-<name>)
Quick Reference
Command	What it does	When to use
git worktree add <path> -b <branch>	Create a new worktree with a new branch	Starting parallel work on a new task
git worktree list	Show all worktrees with their branches and paths	Checking what is active
git worktree list --porcelain	Machine-readable worktree listing	Scripting or enriching with status info
git worktree remove <path>	Remove a worktree directory and its admin files	Done with a parallel task
git worktree remove <path> --force	Force-remove even with uncommitted changes	After explicit user confirmation
git worktree prune	Clean up stale worktree entries	After manual directory deletion or errors
git branch -D worktree-<name>	Delete the orphaned branch after worktree removal	Keeping branches clean
Create

Create a new worktree for an isolated parallel development session.

Workflow
Confirm the current directory is a git repository.
Confirm the current session is NOT already inside a worktree:
git rev-parse --is-inside-work-tree && git worktree list

If the current working directory is already a worktree (not the main working tree), warn the user and stop.
If a name was provided as an argument, use it. Otherwise, present an interactive prompt (or the platform's equivalent): "What name should I use for this worktree? (e.g., feature-auth, bugfix-123)"
Create the worktree:
git worktree add .worktrees/<name> -b worktree-<name>

Change your working directory to the new worktree path.
Report to the user:
Worktree created:
  Directory: .worktrees/<name>/
  Branch: worktree-<name>
  Based on: <current HEAD>

Remind the user:
Run your stack's dependency installation command (e.g., composer install, npm install, pip install -r requirements.txt)
The worktree shares git history with the main repo but has its own working directory
Use the list command to see all active worktrees
Use the remove command to clean up when done
List

List all active worktrees with their branches, paths, and status.

Workflow
Confirm the current directory is inside a git repository.
Run:
git worktree list --porcelain

For each worktree, gather uncommitted change count:
git -C <worktree-path> status --short 2>/dev/null

Display a clean table:
Active worktrees:

| # | Name         | Branch               | Path                          | Status        |
|---|--------------|----------------------|-------------------------------|---------------|
| 1 | (main)       | main                 | /path/to/repo                 | clean         |
| 2 | feature-auth | worktree-feature-auth| .worktrees/feature-auth       | 3 uncommitted |
| 3 | bugfix-123   | worktree-bugfix-123  | .worktrees/bugfix-123         | clean         |

If no worktrees exist beyond the main working tree, say: "No additional worktrees found. Use the create command to create one."
Switch

Switch your working directory to a different existing worktree.

Workflow
Confirm the current directory is inside a git repository.
Run:
git worktree list

If only the main working tree exists, say: "No worktrees available to switch to. Use the create command to create one." and stop.
If a name was provided as an argument, find the matching worktree path. Otherwise, show the list and present an interactive prompt (or the platform's equivalent): "Which worktree do you want to switch to?"
If the name does not match any existing worktree, say: "Worktree <name> not found." and show the available list.
Open a terminal in the worktree path, or switch your editor to the worktree directory.
Report to the user:
Switched to worktree:
  Directory: <worktree-path>
  Branch: <branch-name>

Show a quick status:
git status --short

Remove

Remove one or all worktrees from the current repository.

Workflow
Confirm the current directory is inside a git repository.
Run:
git worktree list

If no worktrees exist beyond the main working tree, say: "No worktrees to clean up." and stop.
Determine what to remove:
If argument is all -- remove all worktrees (except the main working tree).
If a specific name was provided -- remove only that worktree.
If no argument -- show the list and present an interactive prompt (or the platform's equivalent): "Which worktree should I remove? Enter the name, or type all to remove everything."
Safety check -- for each worktree being removed:
git -C <worktree-path> status --short
git -C <worktree-path> log --oneline @{upstream}..HEAD 2>/dev/null

If there are uncommitted changes or unpushed commits, warn the user:
WARNING: Worktree "<name>" has uncommitted changes / unpushed commits:
  - 2 modified files
  - 1 unpushed commit
These will be permanently lost. Continue? (yes/no)

Wait for explicit confirmation before proceeding.
For each worktree to remove:
git worktree remove <path> --force
git branch -D worktree-<name> 2>/dev/null

Use --force only after the user has confirmed in step 4.
Prune stale entries:
git worktree prune

Report what was removed:
Removed worktrees:
  - feature-auth (branch worktree-feature-auth deleted)
  - bugfix-123 (branch worktree-bugfix-123 deleted)

Remaining worktrees: 1 (main working tree only)

Troubleshooting
Problem	Cause	Fix
fatal: '<path>' is a missing but locked worktree	Worktree directory was deleted manually but the lock file remains	Run git worktree unlock <path> then git worktree prune
Stale entries in git worktree list	Worktree directory was deleted without using git worktree remove	Run git worktree prune to clean up admin files
fatal: '<branch>' is already checked out	Branch is active in another worktree	Switch the other worktree to a different branch first, or remove it
Worktree path exists but is empty	Interrupted creation or corrupted state	Run git worktree remove <path> --force then git worktree prune
Integration with Other Skills
Situation	Recommended Skill
When managing branches and commits	git-workflow
When executing a TDD implementation in an isolated worktree	test-driven-development
When following a full ticket workflow that uses worktrees	ticket-delivery
Weekly Installs
8
Repository
krzysztofsurdy/…virtuoso
GitHub Stars
17
First Seen
10 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass