---
rating: ⭐⭐⭐
title: pull-request-automation
url: https://skills.sh/aj-geddes/useful-ai-prompts/pull-request-automation
---

# pull-request-automation

skills/aj-geddes/useful-ai-prompts/pull-request-automation
pull-request-automation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill pull-request-automation
SKILL.md
Pull Request Automation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement pull request automation to streamline code review processes, enforce quality standards, and reduce manual overhead through templated workflows and intelligent assignment rules.

When to Use
Code review standardization
Quality gate enforcement
Contributor guidance
Review assignment automation
Merge automation
PR labeling and organization
Quick Start

Minimal working example:

# .github/pull_request_template.md

## Description

Briefly describe the changes made in this PR.

## Type of Change

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update

## Related Issues

Closes #(issue number)

## Changes Made

- Change 1
- Change 2

## Testing

- [ ] Unit tests added/updated
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
GitHub Actions: Auto Review Assignment	GitHub Actions: Auto Review Assignment
GitHub Actions: Auto Merge on Approval	GitHub Actions: Auto Merge on Approval
GitLab Merge Request Automation	GitLab Merge Request Automation
Bors: Merge Automation Configuration	Bors: Merge Automation Configuration, Conventional Commit Validation
PR Title Validation Workflow	PR Title Validation Workflow
Code Coverage Requirement	Code Coverage Requirement
Best Practices
✅ DO
Use PR templates for consistency
Require code reviews before merge
Enforce CI/CD checks pass
Auto-assign reviewers based on code ownership
Label PRs for organization
Validate commit messages
Use squash commits for cleaner history
Set minimum coverage requirements
Provide detailed PR descriptions
❌ DON'T
Approve without reviewing code
Merge failing CI checks
Use vague PR titles
Skip automated checks
Merge to protected branches without review
Ignore code coverage drops
Force push to shared branches
Merge directly without PR
Weekly Installs
279
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn