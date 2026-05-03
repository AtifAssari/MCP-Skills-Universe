---
title: gh-address-comments
url: https://skills.sh/davila7/claude-code-templates/gh-address-comments
---

# gh-address-comments

skills/davila7/claude-code-templates/gh-address-comments
gh-address-comments
Originally fromopenai/skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill gh-address-comments
SKILL.md
Contains Hooks

This skill uses Claude hooks which can execute code automatically in response to events. Review carefully before installing.

PR Comment Handler

Guide to find the open PR for the current branch and address its comments with gh CLI. Run all gh commands with elevated network access.

Prereq: ensure gh is authenticated (for example, run gh auth login once), then run gh auth status with escalated permissions (include workflow/repo scopes) so gh commands succeed. If sandboxing blocks gh auth status, rerun it with sandbox_permissions=require_escalated.

1) Inspect comments needing attention
Run scripts/fetch_comments.py which will print out all the comments and review threads on the PR
2) Ask the user for clarification
Number all the review threads and comments and provide a short summary of what would be required to apply a fix for it
Ask the user which numbered comments should be addressed
3) If user chooses comments
Apply fixes for the selected comments

Notes:

If gh hits auth/rate issues mid-run, prompt the user to re-authenticate with gh auth login, then retry.
Weekly Installs
269
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn