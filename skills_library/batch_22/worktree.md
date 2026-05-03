---
title: worktree
url: https://skills.sh/scando1993/sugar/worktree
---

# worktree

skills/scando1993/sugar/worktree
worktree
Installation
$ npx skills add https://github.com/scando1993/sugar --skill worktree
SKILL.md
Git Worktree Management
Iron Law

NEVER MODIFY FILES IN A WORKTREE YOU DID NOT CREATE

Operations
1. Create

Create a new worktree for isolated parallel development.

git worktree add <path> -b <branch-name>

Always use a descriptive branch name matching the worktree purpose
Place worktrees in a consistent location (e.g., /tmp/<repo>-worktrees/<name>)
Verify the worktree was created successfully before proceeding
Initialize any required workspace files (progress.txt, CLAUDE.md, prd.json)
2. List

Show all active worktrees and their branches.

git worktree list

Check for stale or orphaned worktrees
Verify each worktree points to a valid path
Note which branches are checked out where
3. Switch

Navigate between worktrees safely.

Always verify your current working directory before making changes
Use absolute paths to avoid confusion
Check git status in the target worktree before starting work
Never assume you are in the correct worktree — verify with pwd and git branch
4. Sync

Keep worktrees up to date with upstream changes.

# From within the worktree:
git fetch origin
git rebase origin/main  # or merge, depending on strategy

Resolve conflicts in the worktree where they occur
Do not sync during active implementation — finish the current story first
After syncing, re-run quality checks to catch integration issues
5. Cleanup

Remove worktrees that are no longer needed.

git worktree remove <path>
git worktree prune

Verify all changes are committed and pushed before removing
Never force-remove a worktree with uncommitted changes
Prune stale references after removal
Delete the associated branch only after confirming the merge
Red Flags — If You Catch Yourself Thinking:
Thought	Reality
"I'll just edit files in this other worktree quickly"	Each worktree is an isolated workspace. Switch properly or create a new one.
"I don't need to check which worktree I'm in"	Wrong worktree = wrong branch = wrong commits. ALWAYS verify with pwd and git branch.
"I'll force-remove this worktree to save time"	Force-remove destroys uncommitted work. Check git status first.
"Pruning is optional, I'll do it later"	Stale worktree references cause confusing errors. Prune after every removal.
Rules
Always verify your working directory before making any changes
Never force-remove a worktree without checking for uncommitted changes
Prune stale worktree references after every removal
Use absolute paths for all worktree operations
One branch per worktree — never checkout a branch that is active in another worktree
Weekly Installs
11
Repository
scando1993/sugar
First Seen
11 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass