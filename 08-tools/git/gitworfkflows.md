---
title: gitworfkflows
url: https://skills.sh/lobbi-docs/claude/gitworfkflows
---

# gitworfkflows

skills/lobbi-docs/claude/gitworfkflows
gitworfkflows
Installation
$ npx skills add https://github.com/lobbi-docs/claude --skill gitworfkflows
SKILL.md
Git Workflows Skill

Provides comprehensive Git version control capabilities for the Golden Armada AI Agent Fleet Platform.

When to Use This Skill

Activate this skill when working with:

Git commands and operations
Branching strategies
Commit management
Pull requests and merges
Repository configuration
Quick Reference
Basic Commands

```bash

Status and info

git status git log --oneline -10 git diff git diff --staged

Staging

git add git add . git add -p # Interactive staging

Committing

git commit -m "message" git commit -am "message" # Add and commit git commit --amend

Branching

git branch git branch git checkout git checkout -b git switch git switch -c

Merging

git merge git merge --no-ff git rebase

Remote

git fetch git pull git push git push -u origin ```

Branching Strategy (Git Flow)

``` main ─────●─────────────●─────────────●─────── │ │ │ release ─────┼─────●───────┼─────────────┼─────── │ │ │ │ develop ─────●─────┼───────●─────────────●─────── │ │ │ │ feature ─────●─────┘ │ │ │ │ hotfix ───────────────────●─────────────┘ ```

Branch Naming

```bash

Features

feature/add-agent-api feature/GA-123-user-auth

Bugfixes

bugfix/fix-agent-timeout bugfix/GA-456-memory-leak

Hotfixes

hotfix/critical-security-patch

Releases

release/v1.0.0 ```

Commit Message Convention

```bash

Format

():

Types

feat: New feature fix: Bug fix docs: Documentation style: Formatting (no code change) refactor: Code refactoring test: Adding tests chore: Maintenance

Examples

git commit -m "feat(agent): add Claude agent support" git commit -m "fix(api): resolve timeout in task processing" git commit -m "docs: update deployment instructions" ```

Common Workflows
Start Feature

```bash git checkout develop git pull origin develop git checkout -b feature/new-feature

... work ...

git add . git commit -m "feat: implement new feature" git push -u origin feature/new-feature

Create PR to develop

```

Sync Feature Branch

```bash git checkout develop git pull origin develop git checkout feature/my-feature git rebase develop

Resolve conflicts if any

git push --force-with-lease ```

Squash Commits

```bash git rebase -i HEAD~3 # Interactive rebase last 3 commits

Change 'pick' to 'squash' for commits to combine

```

Undo Changes

```bash

Undo last commit (keep changes)

git reset --soft HEAD~1

Undo last commit (discard changes)

git reset --hard HEAD~1

Undo staged changes

git restore --staged

Discard working directory changes

git restore

Revert a commit (creates new commit)

git revert ```

GitHub CLI

```bash

PR Management

gh pr create --title "Feature: Add agent API" --body "Description" gh pr list gh pr checkout gh pr merge gh pr review --approve

Issues

gh issue create --title "Bug: Agent timeout" --label bug gh issue list gh issue close

Repository

gh repo clone / gh repo view --web ```

.gitignore Patterns

```gitignore

Dependencies

node_modules/ venv/ pycache/

Build outputs

dist/ build/ *.egg-info/

Environment

.env .env.local *.local

IDE

.idea/ .vscode/ *.swp

OS

.DS_Store Thumbs.db

Logs

*.log logs/

Secrets (never commit!)

*.pem *.key credentials.json ```

Git Hooks

```bash

.git/hooks/pre-commit

#!/bin/sh npm run lint npm run test

.git/hooks/commit-msg

#!/bin/sh if ! grep -qE "^(feat|fix|docs|style|refactor|test|chore)((.+))?: .{1,50}" "$1"; then echo "Invalid commit message format" exit 1 fi ```

Weekly Installs
32
Repository
lobbi-docs/claude
GitHub Stars
11
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass