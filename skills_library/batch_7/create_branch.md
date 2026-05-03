---
title: create-branch
url: https://skills.sh/getsentry/skills/create-branch
---

# create-branch

skills/getsentry/skills/create-branch
create-branch
Installation
$ npx skills add https://github.com/getsentry/skills --skill create-branch
SKILL.md
Create Branch

Create a git branch following Sentry naming conventions. Keep this workflow non-interactive unless the user explicitly asks to choose the name manually.

Workflow

Resolve the prefix:

First try gh api user --jq .login
Then git config github.user
Then the local part of git config user.email
Then whoami
Sanitize to lowercase ASCII letters, digits, and hyphens; if empty, use local

Resolve the work description:

If $ARGUMENTS is present, use it
Otherwise inspect:
git diff
git diff --cached
git status --short

If there are local changes, derive a short description from the diff
If there are no local changes, use a generic description like repo-maintenance, tooling-update, or work-in-progress

Classify the branch type:

Type	Use when
feat	New functionality
fix	Broken behavior now works
ref	Behavior stays the same, structure changes
chore	Maintenance of existing tooling/config
perf	Same behavior, faster
style	Visual or formatting only
docs	Documentation only
test	Tests only
ci	CI/CD config
build	Build system
meta	Repo metadata
license	License changes

When unsure: use feat for new things, ref for restructuring, chore for maintenance.

Generate <prefix>/<type>/<short-description>. Keep <short-description> kebab-case, ASCII-only, and ideally 3 to 6 words.

Choose the base without prompting:

git branch --show-current
git remote | grep -qx origin && echo origin || git remote | head -1
git symbolic-ref refs/remotes/<remote>/HEAD 2>/dev/null | sed 's|refs/remotes/<remote>/||' | tr -d '[:space:]'

If default branch detection fails, fall back to main, then master, then the current branch
If on a detached HEAD, branch from the current commit
If already on a non-default branch, branch from the current branch
Only switch to the default branch when the user explicitly asks

Avoid collisions by appending -2, -3, and so on until the name is unused locally and remotely.

Create the branch:

git checkout -b <branch-name>


Report the final branch name, but do not stop for confirmation.

References
Sentry Branch Naming
Weekly Installs
1.3K
Repository
getsentry/skills
GitHub Stars
657
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass