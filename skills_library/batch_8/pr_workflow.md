---
title: pr-workflow
url: https://skills.sh/tursodatabase/turso/pr-workflow
---

# pr-workflow

skills/tursodatabase/turso/pr-workflow
pr-workflow
Installation
$ npx skills add https://github.com/tursodatabase/turso --skill pr-workflow
Summary

Guidelines for commits, pull requests, CI workflows, and secure dependency management.

Emphasizes atomic, focused commits with clear messages; recommends git rebase -i for clean history and avoiding mixed logic/formatting changes
PR best practices include keeping changes small and focused, running tests before submission, and using WIP states in GitHub Actions when needed
Security checklist: never commit .env files, credentials, or secrets
Dependency additions require a license file in licenses/ and an entry in NOTICE.md
External API/tool usage should rely on official documentation rather than guessing parameters
SKILL.md
PR Workflow Guide
Commit Practices
Atomic commits. Small, focused, single purpose
Don't mix: logic + formatting, logic + refactoring
Good message = easy to write short description of intent

Learn git rebase -i for clean history.

PR Guidelines
Keep PRs focused and small
Run relevant tests before submitting
Each commit tells part of the story
CI Environment Notes

If running as GitHub Action:

Max-turns limit in .github/workflows/claude.yml
OK to commit WIP state and push
OK to open WIP PR and continue in another action
Don't spiral into rabbit holes. Stay focused on key task
Security

Never commit:

.env files
Credentials
Secrets
Third-Party Dependencies

When adding:

Add license file under licenses/
Update NOTICE.md with dependency info
External APIs/Tools
Never guess API params or CLI args
Search official docs first
Ask for clarification if ambiguous
Weekly Installs
542
Repository
tursodatabase/turso
GitHub Stars
18.4K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass