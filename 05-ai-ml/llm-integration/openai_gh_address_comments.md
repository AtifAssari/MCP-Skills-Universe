---
title: openai-gh-address-comments
url: https://skills.sh/trailofbits/skills-curated/openai-gh-address-comments
---

# openai-gh-address-comments

skills/trailofbits/skills-curated/openai-gh-address-comments
openai-gh-address-comments
Installation
$ npx skills add https://github.com/trailofbits/skills-curated --skill openai-gh-address-comments
SKILL.md
PR Comment Handler

Guide to find the open PR for the current branch and address its comments with gh CLI. Run all gh commands with elevated network access.

1) Inspect comments needing attention
Run scripts/fetch_comments.py which will print out all the comments and review threads on the PR
2) Ask the user for clarification
Number all the review threads and comments and provide a short summary of what would be required to apply a fix for it
Ask the user which numbered comments should be addressed
3) If user chooses comments
Apply fixes for the selected comments

Notes:

If gh hits auth/rate issues mid-run, prompt the user to re-authenticate with gh auth login, then retry.
When to Use
When NOT to Use
Weekly Installs
31
Repository
trailofbits/ski…-curated
GitHub Stars
381
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn