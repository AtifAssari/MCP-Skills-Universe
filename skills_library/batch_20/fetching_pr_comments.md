---
title: fetching-pr-comments
url: https://skills.sh/bumgeunsong/daily-writing-friends/fetching-pr-comments
---

# fetching-pr-comments

skills/bumgeunsong/daily-writing-friends/fetching-pr-comments
fetching-pr-comments
Installation
$ npx skills add https://github.com/bumgeunsong/daily-writing-friends --skill fetching-pr-comments
SKILL.md
Fetching PR Comments
Overview

Retrieve and parse GitHub PR review comments for the current branch using gh CLI.

Quick Reference
Task	Command
Check if PR exists	gh pr view
View PR with issue comments	gh pr view --comments
Fetch review comments (code-level)	gh api repos/{owner}/{repo}/pulls/{n}/comments
Extract key fields	--jq '.[] | {path, line, body}'
Workflow

Get PR number for current branch:

gh pr view --json number --jq '.number'


Fetch review comments:

gh api repos/{owner}/{repo}/pulls/{n}/comments \
  --jq '.[] | {path: .path, line: .line, body: .body}'


Full command (single step):

gh api repos/OWNER/REPO/pulls/$(gh pr view --json number -q .number)/comments \
  --jq '.[] | {path: .path, line: .line, body: .body}'

Important Distinctions
Type	What it shows	How to get
Issue comments	PR-level discussion	gh pr view --comments
Review comments	Code-level feedback	gh api .../pulls/{n}/comments
Common Patterns

Check if current branch has a PR:

gh pr view 2>/dev/null && echo "PR exists" || echo "No PR"


Get PR details + comments in one view:

gh pr view --comments


Fetch specific PR by number:

gh pr view 429 --repo owner/repo --comments

When NOT to Use
Creating new PRs (use gh pr create)
Reviewing diffs (use gh pr diff)
Merging (use gh pr merge)
Weekly Installs
28
Repository
bumgeunsong/dai…-friends
GitHub Stars
9
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn