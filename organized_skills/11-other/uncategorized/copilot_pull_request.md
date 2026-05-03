---
rating: ⭐⭐
title: copilot-pull-request
url: https://skills.sh/squirrel289/pax/copilot-pull-request
---

# copilot-pull-request

skills/squirrel289/pax/copilot-pull-request
copilot-pull-request
Installation
$ npx skills add https://github.com/squirrel289/pax --skill copilot-pull-request
SKILL.md
Copilot Pull Request

Skill for managing GitHub pull requests and issues using Copilot's built-in APIs. Use this for agent-native, composable, and context-aware PR/issue workflows.

When to Use
In Copilot agent environments (VS Code, Copilot CLI, etc.)
When you want maximum integration and reliability
Interface, Workflows, and Best Practices

See PR_MANAGEMENT_INTERFACE.md for the unified interface, supported operations, workflows, best practices, error handling, and quick reference shared by all PR management skills.

API-Specific Usage
Fetch PR Details
operation: fetch-pr-details
pr-number: 42
repository: owner/repo


Uses: github-pull-request_activePullRequest or github-pull-request_openPullRequest

List Review Comments
operation: list-comments
pr-number: 42
repository: owner/repo


Uses: github-pull-request_activePullRequest (field: reviewThreads)

Reply to Comment
operation: reply-comment
pr-number: 42
thread-id: PRRT_abc123
body: "Thanks for the feedback!"
repository: owner/repo


Uses: pull_request_review_write (add comment)

Resolve Thread
operation: resolve-thread
pr-number: 42
thread-id: PRRT_abc123
repository: owner/repo


Uses: pull_request_review_write (resolve thread)

Merge PR
operation: merge-pr
pr-number: 42
repository: owner/repo
merge-method: squash
delete-branch: true


Uses: pull_request_review_write (merge)

Quick Reference
FETCH PR:
  operation: fetch-pr-details
  pr-number: <number>
  repository: <owner/repo>

LIST COMMENTS:
  operation: list-comments
  pr-number: <number>
  repository: <owner/repo>

LIST UNRESOLVED COMMENTS:
  operation: list-comments
  pr-number: 42
  repository: owner/repo
  filters:
    unresolved: true

REPLY TO COMMENT:
  operation: reply-comment
  pr-number: <number>
  thread-id: <id>
  body: "message"
  repository: <owner/repo>

RESOLVE THREAD:
  operation: resolve-thread
  pr-number: <number>
  thread-id: <id>
  repository: <owner/repo>

CHECK MERGEABLE:
  peration: check-status
  r-number: 42
  epository: owner/repo

MERGE PR:
  operation: merge-pr
  pr-number: <number>
  repository: <owner/repo>
  merge-method: squash|merge|rebase
  delete-branch: true|false

Weekly Installs
10
Repository
squirrel289/pax
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn