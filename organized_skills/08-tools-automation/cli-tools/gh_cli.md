---
rating: ⭐⭐⭐
title: gh-cli
url: https://skills.sh/ericmjl/skills/gh-cli
---

# gh-cli

skills/ericmjl/skills/gh-cli
gh-cli
Installation
$ npx skills add https://github.com/ericmjl/skills --skill gh-cli
SKILL.md
GitHub CLI Operations

This skill provides quick access to common GitHub CLI operations for managing repositories, pull requests, issues, and GitHub Actions.

Requirements
gh (GitHub CLI) - must be authenticated with your GitHub account
Run gh auth login if not already authenticated
Common operations
Pull requests

Create a new PR:

gh pr create --title "Your PR title" --body "Description of changes"


Create a PR with auto-fill (from commit messages):

gh pr create --fill


Create a draft PR:

gh pr create --draft --title "WIP: Feature X"


List PRs:

# List open PRs
gh pr list

# List all PRs (including closed)
gh pr list --state all

# List your PRs
gh pr list --author @me


View a PR:

# View PR in terminal
gh pr view 123

# Open PR in browser
gh pr view 123 --web


Check out a PR locally:

gh pr checkout 123


Review a PR:

# Approve
gh pr review 123 --approve

# Request changes
gh pr review 123 --request-changes --body "Please fix the typo"

# Comment
gh pr review 123 --comment --body "Looks good overall"


Merge a PR:

# Merge with merge commit
gh pr merge 123

# Squash and merge
gh pr merge 123 --squash

# Rebase and merge
gh pr merge 123 --rebase

# Auto-merge when checks pass
gh pr merge 123 --auto --squash

GitHub Actions

List workflow runs:

# List recent runs
gh run list

# List runs for a specific workflow
gh run list --workflow "CI"

# List failed runs
gh run list --status failure


View run details:

gh run view 1234567890


View run logs:

# View all logs for a run
gh run view 1234567890 --log

# View logs for a specific job
gh run view 1234567890 --log --job "build"


Download run logs:

gh run download 1234567890


Re-run a workflow:

# Re-run failed jobs
gh run rerun 1234567890 --failed

# Re-run all jobs
gh run rerun 1234567890


Watch a running workflow:

gh run watch 1234567890


Trigger a workflow manually:

gh workflow run workflow-name.yml

Issues

Create an issue:

gh issue create --title "Bug: Something broken" --body "Description here"


List issues:

# List open issues
gh issue list

# List your issues
gh issue list --assignee @me

# List issues with a label
gh issue list --label bug


View an issue:

gh issue view 456


Comment on an issue:

gh issue comment 456 --body "Thanks for reporting this!"


Close/reopen an issue:

gh issue close 456
gh issue reopen 456

Repository operations

Clone a repository:

gh repo clone owner/repo


Create a repository:

# Create public repo
gh repo create my-repo --public

# Create private repo with README
gh repo create my-repo --private --add-readme


View repository info:

gh repo view owner/repo


Fork a repository:

gh repo fork owner/repo --clone


Set default branch:

gh repo set-default owner/repo

Status and monitoring

Check CI status:

# View checks for current branch
gh pr checks

# View checks for a specific PR
gh pr checks 123


View your notifications:

gh notify

Advanced usage

Use with specific repository:

gh pr list --repo owner/repo


Output as JSON for scripting:

gh pr list --json number,title,author,state


Use custom queries:

# Search for PRs with label
gh pr list --label "needs-review"

# Search for issues assigned to you
gh issue list --assignee @me --state open

Tips

Check command help: Add --help to any command to see all options:

gh pr create --help


Interactive mode: Many commands support interactive prompts when you don't provide required flags:

gh pr create  # Will prompt for title, body, etc.


Aliases: Create custom aliases for frequently used commands:

gh alias set prc 'pr create --fill'


Default repository: Run gh repo set-default in a repo to avoid specifying --repo flag.

Common workflows

Creating a PR from current branch:

git push -u origin feature-branch
gh pr create --fill


Checking why a PR failed:

gh pr checks 123
gh run view <run-id> --log


Quick PR review workflow:

gh pr list
gh pr view 123
gh pr checkout 123
# Make local tests/review
gh pr review 123 --approve


Monitoring a deployment:

gh run list --workflow "Deploy"
gh run watch <latest-run-id>

Weekly Installs
13
Repository
ericmjl/skills
GitHub Stars
32
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn