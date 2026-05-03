---
title: create-agents-md
url: https://skills.sh/siviter-xyz/dot-agent/create-agents-md
---

# create-agents-md

skills/siviter-xyz/dot-agent/create-agents-md
create-agents-md
Installation
$ npx skills add https://github.com/siviter-xyz/dot-agent --skill create-agents-md
SKILL.md
Create AGENTS.md

Guide for creating AGENTS.md files for project-specific inline rules.

When to Use AGENTS.md
Small, project-specific instructions that should be committed in the repo
Folder-scoped rules for specific directories
Package-specific instructions in monorepos
Test-specific guidance in test directories
When NOT to Use AGENTS.md
Reusable knowledge across projects → Use skills
Large documentation → Use skills with references
Complex workflows → Use skills with scripts
AGENTS.md Structure

AGENTS.md is a simple markdown file without metadata:

# Project Instructions

## Code Style

- Use TypeScript for all new files
- Prefer functional components in React
- Use snake_case for database columns

## Architecture

- Follow the repository pattern
- Keep business logic in service layers

Location
Project root: AGENTS.md – Primary, inline instructions and references for the whole project (commands, tech stack, testing, code style, architecture, safety boundaries).
Subdirectories: subdirectory/AGENTS.md – Folder- or package-scoped instructions when local behavior meaningfully diverges from the root (e.g., a specific package, service, or test tree).
Nested support: Agents typically combine instructions from the closest AGENTS.md with parent ones; keep root general and use nested AGENTS.md only where you truly need more specific rules.
Best Practices
Keep AGENTS.md files small and focused
Use for project-specific conventions
Prefer short, concrete references over long prose:
Link to project docs, specs, and runbooks
Point to example files or directories (e.g., see src/api/users.ts for canonical pattern)
Include the most important commands with exact CLI invocations
Reference existing code examples when possible
Update as project evolves
References

For detailed best practices, see references/best-practices.md.

Weekly Installs
199
Repository
siviter-xyz/dot-agent
GitHub Stars
11
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass