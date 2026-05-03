---
title: git-clean-gone-branches
url: https://skills.sh/everyinc/compound-engineering-plugin/git-clean-gone-branches
---

# git-clean-gone-branches

skills/everyinc/compound-engineering-plugin/git-clean-gone-branches
git-clean-gone-branches
Installation
$ npx skills add https://github.com/everyinc/compound-engineering-plugin --skill git-clean-gone-branches
SKILL.md
Clean Gone Branches

Delete local branches whose remote tracking branch has been deleted, including any associated worktrees.

Workflow
Step 1: Discover gone branches

Run the discovery script to fetch the latest remote state and identify gone branches:

bash scripts/clean-gone


scripts/clean-gone

The script runs git fetch --prune first, then parses git branch -vv for branches marked : gone].

If the script outputs __NONE__, report that no stale branches were found and stop.

Step 2: Present branches and ask for confirmation

Show the user the list of branches that will be deleted. Format as a simple list:

These local branches have been deleted from the remote:

  - feature/old-thing
  - bugfix/resolved-issue
  - experiment/abandoned

Delete all of them? (y/n)


Wait for the user's answer using the platform's question tool (e.g., AskUserQuestion in Claude Code, request_user_input in Codex, ask_user in Gemini). If no question tool is available, present the list and wait for the user's reply before proceeding.

This is a yes-or-no decision on the entire list -- do not offer multi-selection or per-branch choices.

Step 3: Delete confirmed branches

If the user confirms, delete each branch. For each branch:

Check if it has an associated worktree (git worktree list | grep "\\[$branch\\]")
If a worktree exists and is not the main repo root, remove it first: git worktree remove --force "$worktree_path"
Delete the branch: git branch -D "$branch"

Report results as you go:

Removed worktree: .worktrees/feature/old-thing
Deleted branch: feature/old-thing
Deleted branch: bugfix/resolved-issue
Deleted branch: experiment/abandoned

Cleaned up 3 branches.


If the user declines, acknowledge and stop without deleting anything.

Weekly Installs
229
Repository
everyinc/compou…g-plugin
GitHub Stars
16.0K
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass