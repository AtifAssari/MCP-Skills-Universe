---
title: git-commit
url: https://skills.sh/github/awesome-copilot/git-commit
---

# git-commit

skills/github/awesome-copilot/git-commit
git-commit
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill git-commit
Summary

Standardized git commits using Conventional Commits specification with intelligent diff analysis and message generation.

Auto-detects commit type (feat, fix, docs, refactor, perf, test, build, ci, chore, revert) and scope from actual code changes
Generates semantic commit messages following conventional format with optional body and footer sections
Intelligently stages files for logical grouping when needed, with support for pattern-based and interactive staging
Detects breaking changes and formats them with exclamation mark or BREAKING CHANGE footer
Enforces git safety protocols: prevents destructive operations, config changes, and secret commits without explicit user request
SKILL.md
Git Commit with Conventional Commits
Overview

Create standardized, semantic git commits using the Conventional Commits specification. Analyze the actual diff to determine appropriate type, scope, and message.

Conventional Commit Format
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]

Commit Types
Type	Purpose
feat	New feature
fix	Bug fix
docs	Documentation only
style	Formatting/style (no logic)
refactor	Code refactor (no feature/fix)
perf	Performance improvement
test	Add/update tests
build	Build system/dependencies
ci	CI/config changes
chore	Maintenance/misc
revert	Revert commit
Breaking Changes
# Exclamation mark after type/scope
feat!: remove deprecated endpoint

# BREAKING CHANGE footer
feat: allow config to extend other configs

BREAKING CHANGE: `extends` key behavior changed

Workflow
1. Analyze Diff
# If files are staged, use staged diff
git diff --staged

# If nothing staged, use working tree diff
git diff

# Also check status
git status --porcelain

2. Stage Files (if needed)

If nothing is staged or you want to group changes differently:

# Stage specific files
git add path/to/file1 path/to/file2

# Stage by pattern
git add *.test.*
git add src/components/*

# Interactive staging
git add -p


Never commit secrets (.env, credentials.json, private keys).

3. Generate Commit Message

Analyze the diff to determine:

Type: What kind of change is this?
Scope: What area/module is affected?
Description: One-line summary of what changed (present tense, imperative mood, <72 chars)
4. Execute Commit
# Single line
git commit -m "<type>[scope]: <description>"

# Multi-line with body/footer
git commit -m "$(cat <<'EOF'
<type>[scope]: <description>

<optional body>

<optional footer>
EOF
)"

Best Practices
One logical change per commit
Present tense: "add" not "added"
Imperative mood: "fix bug" not "fixes bug"
Reference issues: Closes #123, Refs #456
Keep description under 72 characters
Git Safety Protocol
NEVER update git config
NEVER run destructive commands (--force, hard reset) without explicit request
NEVER skip hooks (--no-verify) unless user asks
NEVER force push to main/master
If commit fails due to hooks, fix and create NEW commit (don't amend)
Weekly Installs
28.1K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass