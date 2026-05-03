---
rating: ⭐⭐
title: pr-address-comments
url: https://skills.sh/google-gemini/gemini-cli/pr-address-comments
---

# pr-address-comments

skills/google-gemini/gemini-cli/pr-address-comments
pr-address-comments
Installation
$ npx skills add https://github.com/google-gemini/gemini-cli --skill pr-address-comments
SKILL.md

You are helping the user address comments on their Pull Request. These comments may have come from an automated review agent or a team member.

OBJECTIVE: Help the user review and address comments on their PR.

Comment Review Procedure
Run the scripts/fetch-pr-info.js script to get PR info and state. MAKE SURE you read the entire output of the command, even if it gets truncated.
Summarize the review status by analyzing the diff, commit log, and comments to see which still need to be addressed. Pay attention to the current user's comments. For resolved threads, summarize as a single line with a ✅. For open threads, provide a reference number e.g. [1] and the comment content.
Present your summary of the feedback and current state and allow the user to guide you as to what to fix/address/skip. DO NOT begin fixing issues automatically.
Weekly Installs
585
Repository
google-gemini/gemini-cli
GitHub Stars
103.0K
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn