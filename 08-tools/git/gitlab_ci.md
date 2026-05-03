---
title: gitlab-ci
url: https://skills.sh/grandcamel/gitlab-assistant-skills/gitlab-ci
---

# gitlab-ci

skills/grandcamel/gitlab-assistant-skills/gitlab-ci
gitlab-ci
Installation
$ npx skills add https://github.com/grandcamel/gitlab-assistant-skills --skill gitlab-ci
SKILL.md
CI/CD Pipeline Skill

CI/CD pipeline operations for GitLab using the glab CLI.

Quick Reference
Operation	Command	Risk
View status	glab ci status	-
View pipeline	glab ci view	-
List pipelines	glab ci list	-
Run pipeline	glab ci run	⚠️
Get pipeline JSON	glab ci get	-
Retry job	glab ci retry <job-id>	⚠️
Trace job	glab ci trace <job-id>	-
Download artifacts	glab ci artifact	-
Lint CI config	glab ci lint	-
Delete pipeline	glab ci delete <id>	⚠️⚠️

Risk Legend: - Safe | ⚠️ Caution | ⚠️⚠️ Warning | ⚠️⚠️⚠️ Danger

When to Use This Skill

ALWAYS use when:

User wants to check pipeline/build status
User mentions "CI", "CD", "pipeline", "build", "job", "deploy"
User wants to trigger or retry builds
User wants to view job logs

NEVER use when:

User wants to manage CI/CD variables (use gitlab-variable instead)
User wants to manage schedules (use gitlab-schedule skill)
Available Commands
View Pipeline Status
glab ci status [options]


Options:

Flag	Description
-b, --branch=<branch>	Check status for specific branch
-l, --live	Show status in real-time (updates automatically)
-c, --compact	Show compact view

Examples:

# View current branch pipeline status
glab ci status

# View status for specific branch
glab ci status --branch=main

# Watch status live (updates in real-time)
glab ci status --live

# Compact view
glab ci status --compact

Interactive Pipeline View
glab ci view [options]


Options:

Flag	Description
-b, --branch=<branch>	View pipeline for specific branch/tag
-p, --pipeline-id=<id>	View specific pipeline by ID
-w, --web	Open pipeline in browser

Keyboard shortcuts in view mode:

Key	Action
Esc or q	Close logs or return to pipeline
Ctrl+R or Ctrl+P	Run, retry, or play a job
Tab / Arrow keys	Navigate
Enter	Confirm selection
Ctrl+D	Cancel job / Quit view

Examples:

# Interactive view for current branch
glab ci view

# View specific branch pipeline
glab ci view --branch=feature/new

# View specific pipeline ID
glab ci view --pipeline-id=12345

# Open in browser
glab ci view --web

List Pipelines
glab ci list [options]


Options:

Flag	Description
-b, --branch=<branch>	Filter by branch
--status=<status>	Filter by status: running, pending, success, failed, canceled, skipped
--all	List all pipelines (not just default page)
-P, --per-page=<n>	Items per page

Examples:

# List recent pipelines
glab ci list

# List pipelines for branch
glab ci list --branch=main

# List failed pipelines
glab ci list --status=failed

# List all running pipelines
glab ci list --status=running --all

Run/Trigger Pipeline
glab ci run [options]


Options:

Flag	Description
-b, --branch=<ref>	Branch or tag to run pipeline on
--variables=<vars>	CI variables as key=value pairs (comma-separated)

Examples:

# Run pipeline for current branch
glab ci run

# Run pipeline for specific branch
glab ci run --branch=main

# Run with CI variables
glab ci run --variables="DEPLOY_ENV=staging,DEBUG=true"

# Run for a tag
glab ci run --branch=v1.2.3

Get Pipeline JSON
glab ci get [options]


Get JSON representation of a pipeline.

Options:

Flag	Description
-b, --branch=<branch>	Get pipeline for specific branch
-p, --pipeline-id=<id>	Get specific pipeline by ID

Examples:

# Get current branch pipeline
glab ci get

# Get specific pipeline
glab ci get --pipeline-id=12345

# Pipe to jq for processing
glab ci get | jq '.status'

Retry Job
glab ci retry <job-id>


Retry a failed CI job.

Examples:

# Retry specific job
glab ci retry 456789

Trace Job Logs
glab ci trace <job-id> [options]


View job logs in real-time.

Examples:

# Trace job output
glab ci trace 456789

Download Artifacts
glab ci artifact [options]


Download artifacts from the last pipeline.

Options:

Flag	Description
-b, --branch=<branch>	Download from specific branch
-j, --job=<job-name>	Download from specific job
-p, --path=<path>	Download to specific path

Examples:

# Download all artifacts from last pipeline
glab ci artifact

# Download from specific job
glab ci artifact --job=build

# Download to specific directory
glab ci artifact --path=./artifacts/

Lint CI Configuration
glab ci lint [file]


Validate .gitlab-ci.yml file.

Examples:

# Lint default .gitlab-ci.yml
glab ci lint

# Lint specific file
glab ci lint path/to/.gitlab-ci.yml

Delete Pipeline
glab ci delete <pipeline-id>


Warning: This permanently deletes the pipeline and its jobs.

Common Workflows
Workflow 1: Check and Fix Failed Pipeline
# 1. Check current status
glab ci status

# 2. View failed pipeline interactively
glab ci view

# 3. Find failed job and view logs (in interactive view)
# Press arrow keys to select job, Enter to view logs

# 4. Retry the failed job
glab ci retry <job-id>

# 5. Watch the retry
glab ci status --live

Workflow 2: Trigger Deployment
# 1. Ensure tests pass
glab ci status --branch=main

# 2. Trigger deployment pipeline with variables
glab ci run --branch=main --variables="DEPLOY_ENV=production"

# 3. Monitor deployment
glab ci status --live

Workflow 3: Debug CI Configuration
# 1. Lint your CI config
glab ci lint

# 2. If valid, run a test pipeline
glab ci run

# 3. Watch the results
glab ci view

Workflow 4: Download Build Artifacts
# 1. Check pipeline succeeded
glab ci status --branch=release

# 2. Download artifacts from build job
glab ci artifact --branch=release --job=build --path=./dist/

Pipeline Status Reference
Status	Meaning
running	Pipeline is currently executing
pending	Pipeline is waiting to run
success	All jobs passed
failed	One or more jobs failed
canceled	Pipeline was manually canceled
skipped	Pipeline was skipped
manual	Waiting for manual trigger
scheduled	Scheduled to run later
Troubleshooting
Issue	Cause	Solution
Authentication failed	Invalid/expired token	Run glab auth login
Pipeline not found	No pipeline for branch	Check branch name or run glab ci run
Job stuck pending	No runners available	Check runner configuration
Lint fails	Invalid YAML syntax	Fix syntax errors in .gitlab-ci.yml
Cannot retry	Job not in retryable state	Wait for current run or cancel first
Related Documentation
Safeguards
Quick Reference
Weekly Installs
92
Repository
grandcamel/gitl…t-skills
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass