---
rating: ⭐⭐⭐
title: vcs-commit
url: https://skills.sh/diegocanepa/agent-skills/vcs-commit
---

# vcs-commit

skills/diegocanepa/agent-skills/vcs-commit
vcs-commit
Installation
$ npx skills add https://github.com/diegocanepa/agent-skills --skill vcs-commit
SKILL.md
VCS Commit
Conventional Commit Format
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]

Types
feat: New feature
fix: Bug fix
docs: Documentation
style: Formatting
refactor: Refactor
test: Tests
perf: Performance
chore: Maintenance
Breaking Changes
# Exclamation mark after type/scope
feat!: remove deprecated endpoint

# BREAKING CHANGE footer
feat: allow config to extend other configs

BREAKING CHANGE: `extends` key behavior changed

Workflow
Stage: git add <files> (Group changes logically).
Analyze: Use git diff --staged to understand changes.
Drafting:
Write in English only.
Follow Conventional Commits.
Use imperative mood ("add" not "added").
MITM Confirmation: ALWAYS present the drafted commit message to the USER for approval before executing git commit.
Commit: git commit -m "<type>(scope): <description>"
Best Practices
One logical change per commit
Present tense: "add" not "added"
Imperative mood: "fix bug" not "fixes bug"
Reference issues: Closes #123, Refs #456
Keep description under 72 characters
Git Safety Protocol
No Secrets: Never commit API keys or credentials.
NEVER run destructive commands (--force, hard reset) without explicit request
NEVER skip hooks (--no-verify) unless user asks
NEVER force push to main/master
If commit fails due to hooks, fix and create NEW commit (don't amend)
Weekly Installs
9
Repository
diegocanepa/agent-skills
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass