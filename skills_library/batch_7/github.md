---
title: github
url: https://skills.sh/steipete/clawdis/github
---

# github

skills/steipete/clawdis/github
github
Installation
$ npx skills add https://github.com/steipete/clawdis --skill github
Summary

GitHub repository operations via gh CLI for issues, PRs, CI runs, and API queries.

Covers PR and issue workflows: list, create, view, comment, merge, and close operations
Includes CI/workflow run inspection with log filtering, status checks, and failed job re-runs
Supports structured JSON output with --jq filtering for programmatic data extraction and querying
Requires gh CLI authentication (one-time setup via gh auth login) and works best within git directories or with explicit --repo owner/repo flags
SKILL.md
GitHub Skill

Use the gh CLI to interact with GitHub repositories, issues, PRs, and CI.

When to Use

✅ USE this skill when:

Checking PR status, reviews, or merge readiness
Viewing CI/workflow run status and logs
Creating, closing, or commenting on issues
Creating or merging pull requests
Querying GitHub API for repository data
Listing repos, releases, or collaborators
When NOT to Use

❌ DON'T use this skill when:

Local git operations (commit, push, pull, branch) → use git directly
Non-GitHub repos (GitLab, Bitbucket, self-hosted) → different CLIs
Cloning repositories → use git clone
Reviewing actual code changes → use coding-agent skill
Complex multi-file diffs → use coding-agent or read files directly
Setup
# Authenticate (one-time)
gh auth login

# Verify
gh auth status

Common Commands
Pull Requests
# List PRs
gh pr list --repo owner/repo

# Check CI status
gh pr checks 55 --repo owner/repo

# View PR details
gh pr view 55 --repo owner/repo

# Create PR
gh pr create --title "feat: add feature" --body "Description"

# Merge PR
gh pr merge 55 --squash --repo owner/repo

Issues
# List issues
gh issue list --repo owner/repo --state open

# Create issue
gh issue create --title "Bug: something broken" --body "Details..."

# Close issue
gh issue close 42 --repo owner/repo

CI/Workflow Runs
# List recent runs
gh run list --repo owner/repo --limit 10

# View specific run
gh run view <run-id> --repo owner/repo

# View failed step logs only
gh run view <run-id> --repo owner/repo --log-failed

# Re-run failed jobs
gh run rerun <run-id> --failed --repo owner/repo

API Queries
# Get PR with specific fields
gh api repos/owner/repo/pulls/55 --jq '.title, .state, .user.login'

# List all labels
gh api repos/owner/repo/labels --jq '.[].name'

# Get repo stats
gh api repos/owner/repo --jq '{stars: .stargazers_count, forks: .forks_count}'

JSON Output

Most commands support --json for structured output with --jq filtering:

gh issue list --repo owner/repo --json number,title --jq '.[] | "\(.number): \(.title)"'
gh pr list --json number,title,state,mergeable --jq '.[] | select(.mergeable == "MERGEABLE")'

Templates
PR Review Summary
# Get PR overview for review
PR=55 REPO=owner/repo
echo "## PR #$PR Summary"
gh pr view $PR --repo $REPO --json title,body,author,additions,deletions,changedFiles \
  --jq '"**\(.title)** by @\(.author.login)\n\n\(.body)\n\n📊 +\(.additions) -\(.deletions) across \(.changedFiles) files"'
gh pr checks $PR --repo $REPO

Issue Triage
# Quick issue triage view
gh issue list --repo owner/repo --state open --json number,title,labels,createdAt \
  --jq '.[] | "[\(.number)] \(.title) - \([.labels[].name] | join(", ")) (\(.createdAt[:10]))"'

Notes
Always specify --repo owner/repo when not in a git directory
Use URLs directly: gh pr view https://github.com/owner/repo/pull/55
Rate limits apply; use gh api --cache 1h for repeated queries
Weekly Installs
1.2K
Repository
steipete/clawdis
GitHub Stars
367.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn