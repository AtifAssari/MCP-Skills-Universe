---
title: git-helper
url: https://skills.sh/joshuadavidthomas/opencode-agent-skills/git-helper
---

# git-helper

skills/joshuadavidthomas/opencode-agent-skills/git-helper
git-helper
Installation
$ npx skills add https://github.com/joshuadavidthomas/opencode-agent-skills --skill git-helper
SKILL.md
Git Helper

A comprehensive skill for git workflow management and best practices.

Quick Start

Use this skill when you need help with:

Branch creation and management
Commit message formatting
Git workflow optimization
Repository maintenance
Common Workflows
Creating a New Feature Branch
git checkout -b feature/your-feature-name
git push -u origin feature/your-feature-name

Writing Good Commit Messages

Follow the conventional commit format:

type(scope): description

[optional body]

[optional footer]


Types: feat, fix, docs, style, refactor, test, chore

Git Cleanup Commands
Remove stale branches
git remote prune origin

Clean up local branches
git branch -d branch-name

Scripts

This skill includes helper scripts:

• create-branch.sh - Creates new feature branches with proper naming • commit-check.sh - Validates commit message format • cleanup.sh - Removes stale branches

Best Practices
Always pull latest changes before creating branches
Use descriptive branch names with prefixes (feature/, bugfix/, hotfix/)
Write atomic commits (one logical change per commit)
Keep commit messages under 72 characters for the subject line
Weekly Installs
40
Repository
joshuadavidthom…t-skills
GitHub Stars
169
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass