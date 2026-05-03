---
title: branch-split-and-pr
url: https://skills.sh/totto2727-dotfiles/agents/branch-split-and-pr
---

# branch-split-and-pr

skills/totto2727-dotfiles/agents/branch-split-and-pr
branch-split-and-pr
Installation
$ npx skills add https://github.com/totto2727-dotfiles/agents --skill branch-split-and-pr
SKILL.md
Branch Split and PR Workflow

A workflow for splitting changes into multiple branches and submitting PRs for each. The plan must strictly follow the plan-template.md included in this skill.

Referenced Skills
Commit messages & granularity: Follow git-commit
Stash / unstage: Follow git-operations-rules
Phase 1: Create and Review the Plan
Analyze changed files and their dependencies
Apply rules:
New additions (tests or target units) get separate branches
Existing modifications are included in the related new PR (but as separate commits)
Document the following in the plan:
File dependency table (group, type: new/existing modification)
List of branches to create (branch name, new/existing modification, dependencies)
"Preparation" and "Commit" steps for each branch (file paths and commit messages)
Excluded files list
Note that work should be halted and instructions requested on error

Edit the plan template from plan-template.md to match the project's changes.

Phase 2: Execute Per Branch (Strictly Follow)

Follow this order strictly for each branch. On conflicts or errors, halt immediately, report the state, and request instructions.

Common Workflow (Per Branch)
# 1. Stage all changes (required to include untracked files)
git add .

# 2. Stash (with a message identifying the work)
git stash push -m "wip: changes for <branch-name>"

# 3. Switch to base branch & create new branch
git switch -f <base-branch>
git switch -c <branch-name>

# 4. Restore stash
git stash apply stash@{0}

# 5. Unstage all
git unstage

# 6. Add only the relevant files per the plan and commit
git add <file1> <file2> ...
git commit -m "<commit-message>"

Use git switch instead of git checkout
Stash messages should clearly identify the work unit, e.g., wip: changes for <branch-name>
Restore using git stash apply stash@{0} to explicitly target the latest stash
Commits must follow Conventional Commits and granularity rules from git-commit
Notes
Deleted files must also be staged with git add <deleted-file-path>
Do not include files listed as "excluded" in the plan
Phase 3: Push and Create PRs

For each branch:

git push -u origin <branch-name>
gh pr create --base develop --title "<title>" --body "<body>" --assignee @me

PR body should follow the repository's PR template. Title should be a concise description of the changes.

Phase 4: Present PR URL List

After all PRs are created, present the following markdown format to the user (clickable links):

## Created PRs

- [PR #<number> - <branch-name>](PR-URL)
- [PR #<number> - <branch-name>](PR-URL)
  ...

On Error
If conflicts, push failures, or gh errors occur, halt work
Report the current branch, stash status, and error message
Do not attempt to resolve on your own
Plan Template

See plan-template.md for the detailed template and step examples. Structure includes:

Overview & rules (separate branches for new items, include existing modifications in related PRs, halt on error)
File dependency table (group, target files, dependent mocks, type)
Branch list table (#, branch name, new/existing modification, dependencies)
Git workflow (common workflow code block)
"Preparation" and "Commit" steps for each branch (command examples)
Excluded files & error handling
Weekly Installs
8
Repository
totto2727-dotfi…s/agents
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass