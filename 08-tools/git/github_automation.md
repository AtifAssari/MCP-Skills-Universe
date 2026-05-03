---
title: github-automation
url: https://skills.sh/ruvnet/ruflo/github-automation
---

# github-automation

skills/ruvnet/ruflo/github-automation
github-automation
Installation
$ npx skills add https://github.com/ruvnet/ruflo --skill github-automation
SKILL.md
GitHub Automation Skill
Purpose

GitHub workflow automation, PR management, and repository coordination.

When to Trigger
Creating pull requests
Managing issues
Setting up CI/CD workflows
Code review automation
Release management
Commands
Create Pull Request
gh pr create --title "feat: description" --body "## Summary\n..."

Review Code
npx claude-flow github review --pr 123

Manage Issues
npx claude-flow github issues list --state open
npx claude-flow github issues create --title "Bug: ..."

Setup Workflow
npx claude-flow workflow create --template ci

Release Management
npx claude-flow deployment release --version 1.0.0

Agent Types
Agent	Role
pr-manager	Pull request lifecycle
code-review-swarm	Automated code review
issue-tracker	Issue management
release-manager	Release automation
workflow-automation	GitHub Actions
Best Practices
Use conventional commits
Require reviews before merge
Run CI on all PRs
Automate release notes
Weekly Installs
190
Repository
ruvnet/ruflo
GitHub Stars
35.8K
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn