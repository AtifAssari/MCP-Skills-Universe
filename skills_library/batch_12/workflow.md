---
title: workflow
url: https://skills.sh/johnlindquist/claude/workflow
---

# workflow

skills/johnlindquist/claude/workflow
workflow
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill workflow
SKILL.md
GitHub Actions Workflow Manager

Monitor and manage CI/CD workflows using the GitHub CLI.

Prerequisites

Install GitHub CLI:

brew install gh
# or
curl -sS https://webi.sh/gh | sh


Authenticate:

gh auth login

CLI Reference
Quick Status Check
# Current branch CI status
gh run list --branch $(git branch --show-current) --limit 5

# All recent runs
gh run list --limit 10

# Filter by workflow
gh run list --workflow "CI" --limit 5

View Specific Run
# Get run details
gh run view <run-id>

# View with logs
gh run view <run-id> --log

# Failed jobs only
gh run view <run-id> --log-failed

# Exit codes for CI scripts
gh run view <run-id> --exit-status

List Runs with Filters
# By branch
gh run list --branch main --limit 10

# By workflow name
gh run list --workflow "Build and Test" --limit 10

# By status
gh run list --status failure --limit 10
gh run list --status success --limit 10
gh run list --status in_progress --limit 10

# Combined filters
gh run list --branch main --workflow "CI" --status failure --limit 5

Rerun Workflows
# Rerun entire workflow
gh run rerun <run-id>

# Rerun only failed jobs
gh run rerun <run-id> --failed

# Rerun specific job
gh run rerun <run-id> --job <job-id>

Watch Running Workflow
# Watch a run in progress
gh run watch <run-id>

# Watch and exit with run's exit code
gh run watch <run-id> --exit-status

Download Artifacts
# List artifacts from a run
gh run view <run-id> --json artifacts

# Download all artifacts
gh run download <run-id>

# Download specific artifact
gh run download <run-id> --name "artifact-name"

# Download to specific directory
gh run download <run-id> --dir ./artifacts

Cancel a Run
gh run cancel <run-id>

View Workflow Files
# List workflow files
gh workflow list

# View specific workflow
gh workflow view "CI"

# Enable/disable workflow
gh workflow enable "CI"
gh workflow disable "CI"

Run Workflow Manually
# Trigger workflow_dispatch
gh workflow run "CI"

# With inputs
gh workflow run "Deploy" -f environment=staging -f version=1.2.3

# On specific branch
gh workflow run "CI" --ref feature-branch

Output Formats
# JSON output for parsing
gh run list --json status,conclusion,name,headBranch,url

# Specific fields
gh run view <run-id> --json jobs,status,conclusion

Workflow Patterns
Quick CI Check
# Is my branch passing?
gh run list --branch $(git branch --show-current) --limit 1 --json status,conclusion

Debug Failing CI
# 1. Find the failing run
gh run list --branch main --status failure --limit 1

# 2. View failed logs
gh run view <run-id> --log-failed

# 3. After fixing, rerun
gh run rerun <run-id> --failed

Monitor Deployment
# Watch deployment in progress
gh run watch <run-id>

# Get notified when done (macOS)
gh run watch <run-id> && osascript -e 'display notification "Deployment complete"'

Retry Flaky Tests
# Rerun just the failed jobs
gh run rerun <run-id> --failed

Pre-Merge Check
# Ensure all checks pass before merging
gh run list --branch $(git branch --show-current) --json conclusion --jq '.[0].conclusion'

Common Statuses
Status	Meaning
queued	Waiting to start
in_progress	Currently running
completed	Finished
Conclusion	Meaning
success	All jobs passed
failure	One or more jobs failed
cancelled	Run was cancelled
skipped	Run was skipped
timed_out	Run exceeded time limit
Best Practices
Check status before merge - Ensure CI passes
Use --log-failed - Only see relevant failure logs
Rerun --failed first - Faster than full rerun
Watch long runs - Don't poll manually
Download artifacts - For test reports, coverage, etc.
Use JSON output - For scripting and parsing
Weekly Installs
24
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail