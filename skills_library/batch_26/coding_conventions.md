---
title: coding conventions
url: https://skills.sh/mineru98/skills-store/coding-conventions
---

# coding conventions

skills/mineru98/skills-store/Coding Conventions
Coding Conventions
Installation
$ npx skills add https://github.com/mineru98/skills-store --skill 'Coding Conventions'
SKILL.md
Coding Conventions
Supported Languages
Python - PEP 8
TypeScript - Google & Microsoft Style Guide
JavaScript - Airbnb Style Guide
Go - Effective Go & Google Style Guide
PHP - PSR Standards
Git Commits - Conventional Commits
Workflow

When writing or modifying code:

Identify the language of the file being edited
Read the appropriate convention file from references/ directory
Apply conventions consistently to naming, formatting, documentation, and organization
Convention Files
references/python-conventions.md - Python (PEP 8)
references/typescript-conventions.md - TypeScript
references/javascript-conventions.md - JavaScript (Airbnb)
references/golang-conventions.md - Go
references/php-conventions.md - PHP (PSR)
references/git-commit-conventions.md - Git commit format
Git Commit Quick Reference

Follow Conventional Commits format:

<type>(<scope>): <subject>


Common types: feat, fix, docs, style, refactor, test, chore

Rules:

Imperative present tense: "add" not "added"
Lowercase subject, no period
Keep subject under 50 characters
Include Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>

Example:

feat(auth): add user authentication

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>


For complete git commit guidelines, see references/git-commit-conventions.md.

Priority Rules
Project-specific conventions override language defaults
Existing code style should be matched for consistency
Automatic tools (ESLint, Prettier, gofmt) should be respected if configured
Convention files provide the default standards
Weekly Installs
–
Repository
mineru98/skills-store
GitHub Stars
4
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass