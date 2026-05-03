---
rating: ⭐⭐
title: gh-address-comments
url: https://skills.sh/openai/skills/gh-address-comments
---

# gh-address-comments

skills/openai/skills/gh-address-comments
gh-address-comments
Installation
$ npx skills add https://github.com/openai/skills --skill gh-address-comments
Summary

Locate and address review comments on GitHub PRs using gh CLI with user-guided workflows.

Fetches all comments and review threads from the open PR for the current branch, displaying them with summaries of required fixes
Requires gh CLI authentication with elevated permissions (workflow/repo scopes); prompts re-authentication if rate limits or auth errors occur mid-run
Presents numbered comment list to user for selection, then applies fixes to chosen comments
Handles sandboxing constraints by supporting escalated permission modes for gh auth status checks
SKILL.md
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
1.3K
Repository
openai/skills
GitHub Stars
18.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn