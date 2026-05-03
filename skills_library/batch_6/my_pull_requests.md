---
title: my-pull-requests
url: https://skills.sh/github/awesome-copilot/my-pull-requests
---

# my-pull-requests

skills/github/awesome-copilot/my-pull-requests
my-pull-requests
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill my-pull-requests
Summary

List and summarize your pull requests in the current GitHub repository.

Retrieves all PRs assigned to you using the current repository context and filters results to show only your own pull requests
Displays PR purpose, details, and status, with special highlighting for PRs awaiting review
Reports any CI/CD check failures and suggests remediation steps
Offers to request Copilot review for PRs that haven't been reviewed yet
SKILL.md

Search the current repo (using #githubRepo for the repo info) and list any pull requests you find (using #list_pull_requests) that are assigned to me.

Describe the purpose and details of each pull request.

If a PR is waiting for someone to review, highlight that in the response.

If there were any check failures on the PR, describe them and suggest possible fixes.

If there was no review done by Copilot, offer to request one using #request_copilot_review.

Weekly Installs
9.2K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass