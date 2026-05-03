---
rating: ⭐⭐
title: create-github-issues-feature-from-implementation-plan
url: https://skills.sh/github/awesome-copilot/create-github-issues-feature-from-implementation-plan
---

# create-github-issues-feature-from-implementation-plan

skills/github/awesome-copilot/create-github-issues-feature-from-implementation-plan
create-github-issues-feature-from-implementation-plan
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill create-github-issues-feature-from-implementation-plan
Summary

Create GitHub Issues automatically from implementation plan phases.

Analyzes implementation plan files to identify phases and generates one issue per phase
Uses feature_request.yml or chore_request.yml templates, with fallback to default issue format
Checks for existing issues before creation to avoid duplicates, and updates existing issues when needed
Includes phase details, requirements, and context in issue descriptions with appropriate labels
SKILL.md
Create GitHub Issue from Implementation Plan

Create GitHub Issues for the implementation plan at ${file}.

Process
Analyze plan file to identify phases
Check existing issues using search_issues
Create new issue per phase using create_issue or update existing with update_issue
Use feature_request.yml or chore_request.yml templates (fallback to default)
Requirements
One issue per implementation phase
Clear, structured titles and descriptions
Include only changes required by the plan
Verify against existing issues before creation
Issue Content
Title: Phase name from implementation plan
Description: Phase details, requirements, and context
Labels: Appropriate for issue type (feature/chore)
Weekly Installs
8.5K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass