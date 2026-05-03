---
rating: ⭐⭐⭐
title: buildkite
url: https://skills.sh/hjewkes/agent-skills/buildkite
---

# buildkite

skills/hjewkes/agent-skills/buildkite
buildkite
Installation
$ npx skills add https://github.com/hjewkes/agent-skills --skill buildkite
SKILL.md
Buildkite — CI/CD
Setup

The buildkite wrapper auto-detects first run and launches scripts/setup.

Build Operations
# List recent builds for a pipeline
buildkite build list --pipeline SLUG

# View build details
buildkite build view BUILD_NUMBER --pipeline SLUG

# Trigger a new build
buildkite build create --pipeline SLUG --branch main --message "Deploy"

# Rebuild a failed build
buildkite build rebuild BUILD_NUMBER --pipeline SLUG

# Cancel a running build
buildkite build cancel BUILD_NUMBER --pipeline SLUG

Job & Log Operations
# List jobs for a build
buildkite job list --build BUILD_NUMBER --pipeline SLUG

# View job log output
buildkite job log JOB_ID

# Download build artifacts
buildkite artifacts download --build BUILD_NUMBER --pipeline SLUG

Pipeline Operations
# List all pipelines
buildkite pipeline list

# View pipeline configuration
buildkite pipeline view SLUG

Failure Debugging Workflow

When a build fails, follow this sequence:

Find the failed build: buildkite build list --pipeline SLUG --state failed

View build details to see which jobs failed: buildkite build view BUILD_NUMBER --pipeline SLUG

Get the failed job's log: buildkite job log JOB_ID

Download artifacts (test reports, etc.) if available: buildkite artifacts download --build BUILD_NUMBER --pipeline SLUG

For detailed debugging patterns, load references/build-debugging.md.

Output Conventions
buildkite outputs JSON by default — pipe through jq for display or extraction.
Use buildkite api for REST API endpoints not covered by direct commands.
Example: buildkite api /v2/organizations/ORG/pipelines | jq '.[].slug'
Reference Files
Reference	When to Load
references/bk-commands.md	Full bk CLI command reference needed
references/build-debugging.md	Debugging build failures in depth
references/troubleshooting.md	Auth failures, CLI errors, rate limits
Weekly Installs
14
Repository
hjewkes/agent-skills
GitHub Stars
3
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn