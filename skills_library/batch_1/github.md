---
title: github
url: https://skills.sh/callstackincubator/agent-skills/github
---

# github

skills/callstackincubator/agent-skills/github
github
Installation
$ npx skills add https://github.com/callstackincubator/agent-skills --skill github
Summary

GitHub workflow automation via gh CLI for pull requests, stacked PRs, and repository management.

Provides stacked PR merge workflow: squash-merge the first PR, then rebase and update base branch for each subsequent PR in the chain
Includes conflict detection and manual resolution prompts to prevent silent failures during multi-PR merges
Covers core gh CLI operations: PR creation, status checks, squash/rebase merging, and branch management
Optimized for low context usage by relying on gh CLI instead of GitHub MCP servers
SKILL.md
GitHub Patterns
Tools

Use gh CLI for all GitHub operations. Prefer CLI over GitHub MCP servers for lower context usage.

Quick Commands
# Create a PR from the current branch
gh pr create --title "feat: add feature" --body "Description"

# Squash-merge a PR
gh pr merge <PR_NUMBER> --squash --title "feat: add feature (#<PR_NUMBER>)"

# View PR status and checks
gh pr status
gh pr checks <PR_NUMBER>

Stacked PR Workflow Summary

When merging a chain of stacked PRs (each targeting the previous branch):

Merge the first PR into main via squash merge
For each subsequent PR: rebase onto main, update base to main, then squash merge
On conflicts: stop and ask the user to resolve manually
# Rebase next PR's branch onto main, excluding already-merged commits
git rebase --onto origin/main <old-base-branch> <next-branch>
git push --force-with-lease origin <next-branch>
gh pr edit <N> --base main
gh pr merge <N> --squash --title "<PR title> (#N)"


See stacked-pr-workflow.md for full step-by-step details.

Quick Reference
File	Description
stacked-pr-workflow.md	Merge stacked PRs into main as individual squash commits
Problem -> Skill Mapping
Problem	Start With
Merge stacked PRs cleanly	stacked-pr-workflow.md
Weekly Installs
2.4K
Repository
callstackincuba…t-skills
GitHub Stars
1.3K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn