---
title: commit
url: https://skills.sh/nweii/agent-stuff/commit
---

# commit

skills/nweii/agent-stuff/commit
commit
Installation
$ npx skills add https://github.com/nweii/agent-stuff --skill commit
SKILL.md
Commit

Create well-formatted git commits following conventional commit conventions.

Convention

Follow the Conventional Commits specification:

<type>[optional scope]: <description>

[optional body]

[optional footer(s)]

Types
feat: New feature
fix: Bug fix
docs: Documentation only
style: Formatting, missing semi-colons, etc. (no code change)
refactor: Code change that neither fixes a bug nor adds a feature
perf: Performance improvement
test: Adding missing tests
chore: Maintenance tasks (build process, dependencies, etc.)
Guidelines
Subject line: Max 50 characters, imperative mood ("add" not "added")
Body: Wrap at 72 characters, explain what and why (not how)
Scope: Optional, indicates section of codebase (e.g., feat(auth):)
Breaking changes: Add exclamation mark after type/scope (e.g., feat!:) and explain in footer
Process
Review staged changes (git diff --staged)
Determine appropriate type and scope
Write concise, descriptive subject line
Add body if the change needs explanation
Execute the commit
Examples
feat(auth): add OAuth2 login support

Implements Google and GitHub OAuth providers.
Closes #123

fix: resolve race condition in data fetcher

The previous implementation could return stale data
when multiple requests were in flight.

chore: update dependencies to latest versions

Weekly Installs
26
Repository
nweii/agent-stuff
GitHub Stars
2
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass