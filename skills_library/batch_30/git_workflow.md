---
title: git-workflow
url: https://skills.sh/totto2727-dotfiles/agents/git-workflow
---

# git-workflow

skills/totto2727-dotfiles/agents/git-workflow
git-workflow
Installation
$ npx skills add https://github.com/totto2727-dotfiles/agents --skill git-workflow
SKILL.md
Git Workflow

This is a unified git workflow skill that combines commit rules, operations rules, file deletion rules, and branch-split workflows into a single reference. It MUST ALWAYS be applied when performing any git operations.

Decision Flow

When performing git operations, determine which reference applies:

"I need to create a commit"

Follow references/commit-rules.md:

Analyze changes with git status, git diff, git diff --staged
Detect commit message language from git log --oneline -10
Group related changes into granular commits
Use Conventional Commits format: type(scope): description
GPG signing is required (see below)
"I need to stage, unstage, undo, or stash"

Follow references/operations-rules.md:

Use git unstage (no options) to reset staging area
Use git undo (no options) to undo the last commit
Use git stash push (not shorthand git stash) to save changes
Use git stash apply (not git stash pop) to restore
Do not use git -C <path>
"I need to delete files"

Follow references/file-deletion-rules.md:

NEVER use rm or unlink directly
ALWAYS stash files before deletion to preserve them
For tracked files: git stash push then git rm
For untracked files: git add then git stash push
Before performing destructive file operations, confirm the target files with the user if the scope is large (>5 files)
"I need to split work into multiple branches and PRs"

Follow references/branch-split-workflow.md and use assets/plan-template.md:

Create a plan analyzing file dependencies
Execute per-branch workflow: stage all, stash, switch, apply, unstage, selective add, commit
Push and create PRs for each branch
Present PR URL list when complete
Universal Rules

These rules apply to ALL git operations without exception. Details are in the reference files above.

GPG signing required — never use --no-gpg-sign; on error, halt and report (see commit-rules.md)
git reset is prohibited — use git unstage or git undo instead (see operations-rules.md)
No direct file deletion — always stash before deleting (see file-deletion-rules.md)
One command at a time — no && chaining; pipes and $(...) within a single command are allowed (see operations-rules.md)
Error handling — on conflicts, push failures, or git errors: halt, report current state, and request instructions
Reference Files
File	Description
references/commit-rules.md	Commit creation workflow, granularity rules, Conventional Commits format
references/operations-rules.md	Rules for unstage, undo, stash push/apply, and git -C prohibition
references/file-deletion-rules.md	File deletion via git stash, prohibited commands, deletion process
references/branch-split-workflow.md	Multi-branch PR splitting workflow with phases
assets/plan-template.md	Template for branch-split plans
Weekly Installs
9
Repository
totto2727-dotfi…s/agents
First Seen
Mar 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass