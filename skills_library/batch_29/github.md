---
title: github
url: https://skills.sh/odyssey4me/agent-skills/github
---

# github

skills/odyssey4me/agent-skills/github
github
Installation
$ npx skills add https://github.com/odyssey4me/agent-skills --skill github
SKILL.md
GitHub Skill

This skill provides GitHub integration using the official gh CLI tool. A Python wrapper script produces markdown-formatted output for read/view operations. Action commands (create, merge, close, comment) should use gh directly.

Prerequisites

Install gh CLI: installation guide

Authentication
# Authenticate with GitHub
gh auth login

# Verify authentication
gh auth status


See GitHub CLI Authentication for details.

Script Usage

The wrapper script (scripts/github.py) formats output as markdown. Use it for read/view operations to get agent-consumable output. Use gh directly for action commands (create, merge, close, comment). See permissions.md for read/write classification of each command.

# Check gh CLI is installed and authenticated
$SKILL_DIR/scripts/github.py check

# Issues
$SKILL_DIR/scripts/github.py issues list --repo OWNER/REPO
$SKILL_DIR/scripts/github.py issues view 123 --repo OWNER/REPO

# Pull Requests
$SKILL_DIR/scripts/github.py prs list --repo OWNER/REPO
$SKILL_DIR/scripts/github.py prs view 456 --repo OWNER/REPO
$SKILL_DIR/scripts/github.py prs checks 456 --repo OWNER/REPO
$SKILL_DIR/scripts/github.py prs status --repo OWNER/REPO

# Workflow Runs
$SKILL_DIR/scripts/github.py runs list --repo OWNER/REPO
$SKILL_DIR/scripts/github.py runs view 12345 --repo OWNER/REPO

# Repositories
$SKILL_DIR/scripts/github.py repos list
$SKILL_DIR/scripts/github.py repos view OWNER/REPO

# Search
$SKILL_DIR/scripts/github.py search repos "machine learning"
$SKILL_DIR/scripts/github.py search issues "label:bug is:open"
$SKILL_DIR/scripts/github.py search prs "is:open review:required"


All commands support --limit N for list commands (default 30).

Commands (Direct gh Usage)

For action commands, use gh directly:

Issues
gh issue list                    # List issues
gh issue view 123                # View issue details
gh issue create                  # Create new issue
gh issue comment 123             # Add comment
gh issue close 123               # Close issue
gh issue edit 123 --add-label bug  # Edit issue


Full reference: gh issue

Pull Requests
gh pr list                       # List PRs
gh pr view 456                   # View PR details
gh pr create                     # Create new PR
gh pr review 456 --approve       # Approve PR
gh pr merge 456 --squash         # Merge PR
gh pr checkout 456               # Checkout PR branch
gh pr diff 456                   # View PR diff
gh pr checks 456                 # View CI status


Full reference: gh pr

Workflows & Actions
gh workflow list                 # List workflows
gh workflow run "CI"             # Trigger workflow
gh run list                      # List workflow runs
gh run view 123456               # View run details
gh run watch 123456              # Watch run progress
gh run download 123456           # Download artifacts
gh run rerun 123456 --failed     # Rerun failed jobs


Full references:

gh workflow
gh run
Repositories
gh repo list                     # List repositories
gh repo view OWNER/REPO          # View repository
gh repo create                   # Create repository
gh repo clone OWNER/REPO         # Clone repository
gh repo fork OWNER/REPO          # Fork repository


Full reference: gh repo

Search
gh search repos "machine learning"   # Search repositories
gh search issues "is:open label:bug" # Search issues
gh search prs "is:open"              # Search pull requests
gh search code "function auth"       # Search code


Full reference: gh search

Examples
Daily PR Review
# Show PRs needing your attention
$SKILL_DIR/scripts/github.py prs status

# Review a specific PR
$SKILL_DIR/scripts/github.py prs view 456
$SKILL_DIR/scripts/github.py prs checks 456
gh pr diff 456
gh pr review 456 --approve

# Verify approval was recorded
$SKILL_DIR/scripts/github.py prs view 456  # check review status

Create Issue and Link PR
# Create issue
gh issue create --title "Bug: Login fails" --body "Description" --label bug
# Verify: note the issue number from output

# Create PR that fixes it (use issue number from above)
gh pr create --title "Fix login bug (#123)" --body "Fixes #123"
# Verify PR was created and linked
$SKILL_DIR/scripts/github.py prs view <number>

Monitor CI Pipeline
# Watch latest workflow run
gh run watch $(gh run list --limit 1 --json databaseId --jq '.[0].databaseId')

# Check failed runs
gh run list --status failure

# Rerun failed jobs
gh run rerun RUNID --failed
# Verify rerun started
$SKILL_DIR/scripts/github.py runs view RUNID


See common-workflows.md for more examples.

Advanced Usage
JSON Output for Scripting
# Get specific fields
gh issue list --json number,title,author

# Process with jq
gh pr list --json number,title | jq '.[] | "\(.number): \(.title)"'

# Export to CSV
gh issue list --json number,title,author | jq -r '.[] | @csv'

GitHub API Access

For operations not covered by gh commands:

# Make authenticated API request
gh api repos/OWNER/REPO/issues

# POST request
gh api repos/OWNER/REPO/issues -X POST -f title="Issue" -f body="Text"

# Process response
gh api repos/OWNER/REPO | jq '.stargazers_count'


Full reference: gh api

Aliases for Frequent Operations
# Create shortcuts
gh alias set prs 'pr list --author @me'
gh alias set issues 'issue list --assignee @me'
gh alias set review 'pr list --search "review-requested:@me"'

# Use them
gh prs
gh issues
gh review

Configuration
# View configuration
gh config list

# Set default editor
gh config set editor vim

# Set git protocol
gh config set git_protocol ssh


Configuration stored in ~/.config/gh/config.yml

Model Guidance

This skill wraps an official CLI. A fast, lightweight model is sufficient.

Troubleshooting
# Check authentication
gh auth status

# Re-authenticate
gh auth login

# Enable debug logging
GH_DEBUG=1 gh issue list

# Check gh version
gh --version

Official Documentation
GitHub CLI Manual: https://cli.github.com/manual/
GitHub CLI Repository: https://github.com/cli/cli
GitHub API Documentation: https://docs.github.com/en/rest
GitHub Actions: https://docs.github.com/en/actions
Summary

The GitHub skill uses the official gh CLI with a Python wrapper for markdown-formatted output on read/view commands.

Quick start:

Install: brew install gh (or equivalent for your OS)
Authenticate: gh auth login
Verify: $SKILL_DIR/scripts/github.py check
Read: $SKILL_DIR/scripts/github.py issues list --repo OWNER/REPO
Write: gh issue create, gh pr create, etc. (use gh directly)

For detailed command reference, use gh <command> --help or visit https://cli.github.com/manual/.

Weekly Installs
115
Repository
odyssey4me/agent-skills
GitHub Stars
3
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn