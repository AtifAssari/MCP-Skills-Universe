---
title: pr-description
url: https://skills.sh/v1-io/v1tamins/pr-description
---

# pr-description

skills/v1-io/v1tamins/pr-description
pr-description
Installation
$ npx skills add https://github.com/v1-io/v1tamins --skill pr-description
SKILL.md
Generate PR Description

Create a comprehensive pull request description based on the changes in this branch relative to main, then update the PR on GitHub.

Usage
/pr-description <PR_URL_or_NUMBER>


Examples:

/pr-description https://github.com/your-org/your-repo/pull/123
/pr-description 123

What It Does

Analyzes Changes

Runs git diff main HEAD to understand modifications
Reviews commit messages with git log main..HEAD --oneline

Generates Content

Title: Concise descriptive title (max 72 chars)
Summary: Clear summary of what the PR accomplishes
Changes Made: Key changes, highlights breaking changes
Testing: How changes were tested, new test cases
Related Issues: Links to related issues or tickets

Updates GitHub

Uses gh pr edit to update the PR title and body
Falls back to manual copy/paste if gh CLI unavailable
Notes
Requires gh CLI to be installed and authenticated
Automatically detects PR number from URL
Highlights breaking changes prominently
Formats output as proper markdown
Weekly Installs
8
Repository
v1-io/v1tamins
GitHub Stars
3
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass