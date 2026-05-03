---
title: gitlab
url: https://skills.sh/odyssey4me/agent-skills/gitlab
---

# gitlab

skills/odyssey4me/agent-skills/gitlab
gitlab
Installation
$ npx skills add https://github.com/odyssey4me/agent-skills --skill gitlab
SKILL.md
GitLab Skill

This skill provides GitLab integration using the official glab CLI tool. A Python wrapper script produces markdown-formatted output for read/view operations. Action commands (create, merge, close, comment) should use glab directly.

Prerequisites

Install glab CLI: installation guide

Authentication
# Authenticate with GitLab
glab auth login

# Verify authentication
glab auth status


Supports GitLab.com, GitLab Dedicated, and GitLab Self-Managed instances. See GitLab CLI Authentication for details.

Script Usage

The wrapper script (scripts/gitlab.py) formats output as markdown. Use it for read/view operations to get agent-consumable output. Use glab directly for action commands (create, merge, close, comment). See permissions.md for read/write classification of each command.

# Check glab CLI is installed and authenticated
$SKILL_DIR/scripts/gitlab.py check

# Issues
$SKILL_DIR/scripts/gitlab.py issues list --repo GROUP/REPO
$SKILL_DIR/scripts/gitlab.py issues view 123 --repo GROUP/REPO

# Merge Requests
$SKILL_DIR/scripts/gitlab.py mrs list --repo GROUP/REPO
$SKILL_DIR/scripts/gitlab.py mrs view 456 --repo GROUP/REPO

# Pipelines
$SKILL_DIR/scripts/gitlab.py pipelines list --repo GROUP/REPO
$SKILL_DIR/scripts/gitlab.py pipelines view 123456 --repo GROUP/REPO

# Repositories
$SKILL_DIR/scripts/gitlab.py repos list
$SKILL_DIR/scripts/gitlab.py repos view GROUP/REPO


All commands support --limit N for list commands (default 30).

Commands (Direct glab Usage)

For action commands, use glab directly:

Issues
glab issue list                    # List issues
glab issue view 123                # View issue details
glab issue create                  # Create new issue
glab issue note 123                # Add comment
glab issue close 123               # Close issue
glab issue update 123 --label bug  # Edit issue


Full reference: glab issue

Merge Requests
glab mr list                       # List merge requests
glab mr view 456                   # View MR details
glab mr create                     # Create new MR
glab mr approve 456                # Approve MR
glab mr merge 456                  # Merge MR
glab mr checkout 456               # Checkout MR branch
glab mr diff 456                   # View MR diff
glab mr note 456                   # Add comment to MR


Full reference: glab mr

Pipelines & CI/CD
glab ci list                       # List pipelines
glab ci view 123456                # View pipeline details
glab ci run                        # Trigger pipeline
glab ci trace                      # Watch pipeline logs
glab ci retry 123456               # Retry failed pipeline
glab ci status                     # Show pipeline status


Full references:

glab ci
glab pipeline
Repositories
glab repo list                     # List repositories
glab repo view GROUP/REPO          # View repository
glab repo create                   # Create repository
glab repo clone GROUP/REPO         # Clone repository
glab repo fork GROUP/REPO          # Fork repository


Full reference: glab repo

Releases
glab release list                  # List releases
glab release view v1.0.0           # View release details
glab release create v1.0.0         # Create release
glab release delete v1.0.0         # Delete release


Full reference: glab release

Examples
Daily MR Review
# List MRs assigned to you
glab mr list --assignee=@me

# Review a specific MR
$SKILL_DIR/scripts/gitlab.py mrs view 456
glab mr diff 456
glab mr approve 456

# Verify approval was recorded
$SKILL_DIR/scripts/gitlab.py mrs view 456  # check approval status

Create Issue and Link MR
# Create issue
glab issue create --title "Bug: Login fails" --description "Description" --label bug
# Verify: note the issue number from output

# Create MR that closes it (use issue number from above)
glab mr create --title "Fix login bug" --description "Closes #123"
# Verify MR was created and linked
$SKILL_DIR/scripts/gitlab.py mrs view <number>

Monitor CI Pipeline
# Check current pipeline status
glab ci status

# Watch pipeline logs in real-time
glab ci trace

# Retry failed jobs
glab ci retry
# Verify pipeline restarted
$SKILL_DIR/scripts/gitlab.py pipelines list


See common-workflows.md for more examples.

Advanced Usage
JSON Output for Scripting
# Get JSON output
glab issue list --output json

# Process with jq
glab mr list --output json | jq '.[] | "\(.iid): \(.title)"'

GitLab API Access

For operations not covered by glab commands:

# Make authenticated API request
glab api projects/:id/issues

# POST request
glab api projects/:id/issues -X POST -f title="Issue" -f description="Text"

# Process response
glab api projects/:id | jq '.star_count'


Full reference: glab api

Aliases for Frequent Operations
# Create shortcuts
glab alias set mrs 'mr list --assignee=@me'
glab alias set issues 'issue list --assignee=@me'
glab alias set pipelines 'ci list'

# Use them
glab mrs
glab issues
glab pipelines

Configuration
# View configuration
glab config get

# Set default editor
glab config set editor vim

# Set default Git protocol
glab config set git_protocol ssh


Configuration stored in ~/.config/glab-cli/config.yml

Model Guidance

This skill wraps an official CLI. A fast, lightweight model is sufficient.

Troubleshooting
# Check authentication
glab auth status

# Re-authenticate
glab auth login

# Enable debug logging
DEBUG=1 glab issue list

# Check glab version
glab version

Official Documentation
GitLab CLI Manual: https://docs.gitlab.com/cli/
GitLab CLI Repository: https://gitlab.com/gitlab-org/cli
GitLab API Documentation: https://docs.gitlab.com/ee/api/
GitLab CI/CD: https://docs.gitlab.com/ee/ci/
Weekly Installs
167
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