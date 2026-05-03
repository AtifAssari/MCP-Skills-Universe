---
title: commit
url: https://skills.sh/aravhawk/claude-code-utils/commit
---

# commit

skills/aravhawk/claude-code-utils/commit
commit
Installation
$ npx skills add https://github.com/aravhawk/claude-code-utils --skill commit
SKILL.md
Git Commit Command

Create atomic git commits following Conventional Commits.

Flow

Check state: git status --porcelain

Empty → STOP, report "No changes to commit"
Merge conflict markers → STOP, report conflict

Verify .gitignore excludes: secrets/.env, build artifacts, OS files (.DS_Store), IDE configs

Stage: git add -A (or specific files for atomic commits)

Analyze: git diff --cached --stat and git diff --cached

If unrelated changes exist, split into separate commits via git reset HEAD <file>

Commit: Use Conventional Commits format

<type>(<scope>): <summary>

[body: what/why, wrap 72 chars]

[footer: BREAKING CHANGE: or Fixes #123]


Types: feat | fix | docs | style | refactor | perf | test | build | ci | chore

Summary rules: imperative mood (e.g., "add", "fix", "refactor"), lowercase, no period, max 72 chars

Confirm: git log -1 --oneline → report hash and summary
Output

Success: Committed: <hash> <type>(<scope>): <summary> Failure: explain why and required action

Weekly Installs
15
Repository
aravhawk/claude…de-utils
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass