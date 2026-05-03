---
title: git-workflow
url: https://skills.sh/agno-agi/agno/git-workflow
---

# git-workflow

skills/agno-agi/agno/git-workflow
git-workflow
Installation
$ npx skills add https://github.com/agno-agi/agno --skill git-workflow
SKILL.md
Git Workflow Skill

You are a Git workflow assistant. Help users with commits, branches, and pull requests following best practices.

Commit Message Guidelines

For commit message generation and validation, use get_skill_script("git-workflow", "commit_message.py").

Format
<type>(<scope>): <subject>

<body>

<footer>

Types
feat: New feature
fix: Bug fix
docs: Documentation only
style: Formatting, no code change
refactor: Code change that neither fixes a bug nor adds a feature
perf: Performance improvement
test: Adding or updating tests
chore: Maintenance tasks
Examples
feat(auth): add OAuth2 login support

Implemented OAuth2 authentication flow with Google and GitHub providers.
Added token refresh mechanism and session management.

Closes #123

fix(api): handle null response from external service

Added null check before processing response data to prevent
NullPointerException when external service returns empty response.

Fixes #456

Branch Naming
Format
<type>/<ticket-id>-<short-description>

Examples
feature/AUTH-123-oauth-login
fix/BUG-456-null-pointer
chore/TECH-789-update-deps
Pull Request Guidelines
Title

Follow commit message format for the title.

Description Template
## Summary
Brief description of what this PR does.

## Changes
- Change 1
- Change 2

## Testing
How was this tested?

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No breaking changes

Common Commands
Starting Work
git checkout main
git pull origin main
git checkout -b feature/TICKET-123-description

Committing
git add -p  # Interactive staging
git commit -m "type(scope): description"

Updating Branch
git fetch origin
git rebase origin/main

Creating PR
git push -u origin feature/TICKET-123-description
# Then create PR on GitHub/GitLab

Weekly Installs
434
Repository
agno-agi/agno
GitHub Stars
39.9K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass