---
rating: ⭐⭐
title: git-worktree-tidy
url: https://skills.sh/0xbigboss/claude-code/git-worktree-tidy
---

# git-worktree-tidy

skills/0xbigboss/claude-code/git-worktree-tidy
git-worktree-tidy
Installation
$ npx skills add https://github.com/0xbigboss/claude-code --skill git-worktree-tidy
SKILL.md
git-worktree-tidy

Routine hygiene for bare-repo + worktree layouts. Fetches origin, prunes gone branches and orphaned worktrees, and fast-forwards important local branches.

When to use

User asks to "fetch prune", "clean up stale branches/worktrees", or "update main/dev to latest" in a worktree-based repo.

Hard Rules
All destructive actions (worktree remove, branch delete) require user confirmation. Present the full list and wait.
Never force-delete a worktree with uncommitted changes without explicit approval. Flag dirty worktrees separately.
Use --ff-only when updating branches. If ff-only fails, stop and ask.
Operate from the .bare directory (or repo root) for branch/worktree management commands.
Workflow
1) Locate the bare root

Determine the bare repo directory:

If cwd contains .bare/, use it
Otherwise: git rev-parse --git-common-dir

All branch and worktree management commands run from this directory.

2) Fetch + prune
git fetch --prune origin


Report what was pruned (deleted remote-tracking branches, updated refs).

3) Discover stale branches
git branch -vv | grep ': gone]'


Collect branch names whose upstream is gone.

4) Discover stale worktrees
git worktree list
git worktree prune --dry-run


Cross-reference worktrees against the gone-branch list. Check each stale worktree for dirty state:

cd <worktree-path> && git status --short


Categorize:

Clean + gone: safe to remove
Dirty + gone: flag for user review
Prunable metadata: orphaned worktree entries (directory already gone)
5) Confirm deletions

Present a summary table:

Stale worktrees to remove:
  <path> (<branch>) [clean]
  <path> (<branch>) [dirty — N uncommitted changes]

Stale branches to delete:
  <branch>

Prunable worktree metadata:
  <entry>


Wait for user confirmation before proceeding.

6) Remove stale worktrees

For each confirmed worktree:

git worktree remove <name>


If removal fails (dirty), report and skip unless user approved force.

7) Delete stale branches
git branch -D <branch1> <branch2> ...

8) Prune worktree metadata
git worktree prune -v

9) Update important branches

Identify which branches have dedicated worktrees for main, dev, or other important branches (user may specify). For each:

cd <worktree-path> && git pull --ff-only origin <branch>


If ff-only fails, report the divergence and ask for guidance.

10) Final status

Show a summary: what was removed, what was updated, any items skipped.

Weekly Installs
38
Repository
0xbigboss/claude-code
GitHub Stars
43
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn