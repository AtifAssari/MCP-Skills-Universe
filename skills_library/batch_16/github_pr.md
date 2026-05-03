---
title: github-pr
url: https://skills.sh/hjewkes/agent-skills/github-pr
---

# github-pr

skills/hjewkes/agent-skills/github-pr
github-pr
Installation
$ npx skills add https://github.com/hjewkes/agent-skills --skill github-pr
SKILL.md
GitHub PR Workflow

Handles the GitHub-specific stage: creating PRs, posting automated review comments, managing feedback.

When to Use
Code review is complete (see code-review skill) and ready for GitHub
Need automated review comments posted to a PR
Managing PR feedback cycles
Automated PR Review

Post automated review comments on a GitHub PR using the orchestration prompt at references/pr-review-orchestrator.md.

How it works:

Eligibility check (skip closed, draft, trivial, already-reviewed PRs)
Gather CLAUDE.md files from repository
Summarize PR changes
Launch 5 parallel Sonnet agents:
CLAUDE.md compliance audit
Shallow bug scan (changes only)
Git blame/history context analysis
Previous PR comment relevance check
Code comment compliance check
Score each issue 0-100 with independent Haiku agents
Filter issues below 80 confidence
Post formatted comment to GitHub via gh

Allowed tools: gh issue view/search/list, gh pr comment/diff/view/list

Creating PRs

See git-workflow stack for deciding between merge, PR, or cleanup.

Typical Flow
Complete implementation
Self-review with code-review skill (Quick or Deep mode)
Fix issues found
Open PR (via git-workflow stack)
Run PR review orchestrator for automated GitHub review
Address feedback, push fixes, re-request review
Reference Files
Reference	Purpose
references/pr-review-orchestrator.md	Full orchestration prompt for automated PR review
Weekly Installs
14
Repository
hjewkes/agent-skills
GitHub Stars
3
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn