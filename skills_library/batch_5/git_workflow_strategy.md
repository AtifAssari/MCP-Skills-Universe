---
title: git-workflow-strategy
url: https://skills.sh/aj-geddes/useful-ai-prompts/git-workflow-strategy
---

# git-workflow-strategy

skills/aj-geddes/useful-ai-prompts/git-workflow-strategy
git-workflow-strategy
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill git-workflow-strategy
SKILL.md
Git Workflow Strategy
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Establish efficient Git workflows that support team collaboration, code quality, and deployment readiness through structured branching strategies and merge patterns.

When to Use
Team collaboration setup
Release management
Feature development coordination
Hotfix procedures
Code review processes
CI/CD integration planning
Quick Start

Minimal working example:

# Initialize GitFlow
git flow init -d

# Start a feature
git flow feature start new-feature
# Work on feature
git add .
git commit -m "feat: implement new feature"
git flow feature finish new-feature

# Start a release
git flow release start 1.0.0
# Update version numbers, changelog
git add .
git commit -m "chore: bump version to 1.0.0"
git flow release finish 1.0.0

# Create hotfix
git flow hotfix start 1.0.1
# Fix critical bug
git add .
git commit -m "fix: critical bug in production"
git flow hotfix finish 1.0.1

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
GitFlow Workflow Setup	GitFlow Workflow Setup, GitHub Flow Workflow, Trunk-Based Development, Git Configuration for Workflows (+1 more)
Merge Strategy Script	Merge Strategy Script
Collaborative Workflow with Code Review	Collaborative Workflow with Code Review
Best Practices
✅ DO
Choose workflow matching team size and release cycle
Keep feature branches short-lived (< 3 days)
Use descriptive branch names with type prefix
Require code review before merging to main
Enforce protection rules on main/release branches
Rebase frequently to minimize conflicts
Write atomic, logical commits
Keep commit messages clear and consistent
❌ DON'T
Commit directly to main branch
Create long-lived feature branches
Use vague branch names (dev, test, temp)
Merge without code review
Mix multiple features in one branch
Force push to shared branches
Ignore failing CI checks
Merge with merge commits in TBD
Weekly Installs
283
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass