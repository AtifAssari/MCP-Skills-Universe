---
title: wt-commit-and-pr
url: https://skills.sh/michael-menard/monorepo/wt-commit-and-pr
---

# wt-commit-and-pr

skills/michael-menard/monorepo/wt-commit-and-pr
wt-commit-and-pr
Installation
$ npx skills add https://github.com/michael-menard/monorepo --skill wt-commit-and-pr
SKILL.md
/wt:commit-and-pr - Commit, Push, and Create/Update PR
Description

Commits all staged changes in the current worktree, pushes to the remote, and creates a GitHub PR (or detects an existing one). Designed for automated use from workflow orchestrators.

Note: With the draft-PR-first workflow (/wt:new creates a draft PR upfront), this skill is primarily used for incremental commit+push operations to existing draft PRs. It gracefully handles both cases: existing PRs (reports "updated") and new PRs (creates one).

Usage
/wt:commit-and-pr {STORY_ID} "{STORY_TITLE}"
/wt:commit-and-pr {STORY_ID} "{STORY_TITLE}" {EVIDENCE_PATH}

Examples
/wt:commit-and-pr WINT-1012 "Add worktree management"
/wt:commit-and-pr WINT-1012 "Add worktree management" _implementation/EVIDENCE.yaml

Parameters
Parameter	Required	Default	Description
STORY_ID	Yes	—	Story identifier (e.g., WINT-1012)
STORY_TITLE	Yes	—	Human-readable story title for commit message and PR
EVIDENCE_PATH	No	—	Path to EVIDENCE.yaml for AC checklist in PR body
What It Does

This slash command:

Verifies the current directory is inside the story worktree
Stages all changes in the worktree
Creates a conventional commit
Pushes the branch to the remote
Creates a new GitHub PR or detects an existing one
Reports the result with PR number and URL
Workflow

Verify worktree context - Confirm current directory is inside tree/story/{STORY_ID} worktree. If not, attempt to locate and cd into it.

Stage all changes - Run git add -A. This is safe because worktrees are isolated per-story; there is no risk of staging unrelated work.

Check for changes to commit - Run git status --porcelain. If no staged changes exist, skip commit and push steps, proceed directly to PR check (step 5).

Commit changes - Create a conventional commit:

git commit -m "feat({STORY_ID}): {STORY_TITLE}"


Push to remote - Push the branch and set upstream:

git push -u origin story/{STORY_ID}


Check for existing PR - Query GitHub for an open PR on this branch:

gh pr list --head story/{STORY_ID} --state open --json number,url


Create or report PR:

If no PR exists: Create one:

gh pr create --title "{STORY_ID}: {STORY_TITLE}" --body "..." --base main


The PR body is built from:

AC checklist extracted from EVIDENCE.yaml (if EVIDENCE_PATH provided)
Default body if artifact is not available

If PR already exists: Report "updated with new commits" and capture the existing PR number/URL.

Output

After completion, always report:

COMMIT AND PR COMPLETE
  story_id: {STORY_ID}
  branch: story/{STORY_ID}
  commit: {short_sha}
  pr_number: {number}
  pr_url: {url}
  pr_action: created | updated


If no changes were committed (step 3 skip):

COMMIT AND PR COMPLETE
  story_id: {STORY_ID}
  branch: story/{STORY_ID}
  commit: skipped (no changes)
  pr_number: {number}
  pr_url: {url}
  pr_action: created | updated | unchanged


This structured output allows the calling orchestrator to parse pr_number and pr_url for CHECKPOINT.yaml.

Error Handling
Error	Action
Not in a worktree	ERROR: "Not inside story worktree. Run from tree/story/{STORY_ID}."
gh CLI not found	ERROR: "GitHub CLI (gh) is required. Install: https://cli.github.com"
No changes to commit	WARNING: Skip commit/push, still check/create PR
Push fails (no remote)	ERROR: "Push failed. Check remote configuration."
Push fails (rejected)	WARNING: "Push rejected. Try pulling first: git pull --rebase origin story/{STORY_ID}"
PR creation fails	ERROR: Report gh error message verbatim
Not authenticated	ERROR: "gh auth required. Run: gh auth login"
Notes
Worktrees are isolated per-story, so git add -A is safe
The commit message follows conventional commit format: feat({STORY_ID}): {STORY_TITLE}
PR base branch is always main
If called multiple times (e.g., after fixes), new commits are pushed and the existing PR updates automatically
The gh CLI must be installed and authenticated
Weekly Installs
21
Repository
michael-menard/monorepo
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass