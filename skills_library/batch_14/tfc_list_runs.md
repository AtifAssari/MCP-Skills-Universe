---
title: tfc-list-runs
url: https://skills.sh/laurigates/claude-plugins/tfc-list-runs
---

# tfc-list-runs

skills/laurigates/claude-plugins/tfc-list-runs
tfc-list-runs
Installation
$ npx skills add https://github.com/laurigates/claude-plugins --skill tfc-list-runs
SKILL.md
Terraform Cloud List Runs

List and filter runs from Terraform Cloud workspaces with formatted output.

When to Use
Scenario	Use this skill	Alternative
List recent runs for any TFC workspace	tfc-list-runs	-
Filter runs by status, operation, or source	tfc-list-runs	-
List runs across an entire org	tfc-list-runs	-
Search runs by commit SHA or user	tfc-list-runs	-
Quick status of a single known run ID	tfc-run-status	Use run-status for one run's details
View plan/apply log output for a run	tfc-run-logs	Use run-logs for log content
Analyze structured plan JSON	tfc-plan-json	Use plan-json for resource change details
List runs for known Forum Virium workspaces	tfc-workspace-runs	Use workspace-runs for shorthand access
Prerequisites
export TFE_TOKEN="your-api-token"        # User or team token
export TFE_ADDRESS="app.terraform.io"    # Optional

Core Commands
List Recent Runs for a Workspace
#!/bin/bash
set -euo pipefail

TOKEN="${TFE_TOKEN:?TFE_TOKEN not set}"
BASE_URL="https://${TFE_ADDRESS:-app.terraform.io}/api/v2"
WORKSPACE_ID="${1:?Usage: $0 <workspace-id> [limit]}"
LIMIT="${2:-10}"

curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/workspaces/$WORKSPACE_ID/runs?page[size]=$LIMIT" | \
  jq -r '.data[] | [
    .id,
    .attributes.status,
    .attributes."created-at"[0:19],
    (.attributes.message // "No message")[0:50]
  ] | @tsv' | \
  column -t -s $'\t'

List Runs by Workspace Name (requires org)
TOKEN="${TFE_TOKEN:?TFE_TOKEN not set}"
BASE_URL="https://${TFE_ADDRESS:-app.terraform.io}/api/v2"
ORG="ForumViriumHelsinki"
WORKSPACE="infrastructure-gcp"

# Get workspace ID first
WS_ID=$(curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/organizations/$ORG/workspaces/$WORKSPACE" | \
  jq -r '.data.id')

# List runs
curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/workspaces/$WS_ID/runs?page[size]=10" | \
  jq -r '.data[] | "\(.id) | \(.attributes.status) | \(.attributes."created-at"[0:19]) | \(.attributes.message // "No message")"'

Filter by Status
TOKEN="${TFE_TOKEN:?TFE_TOKEN not set}"
BASE_URL="https://${TFE_ADDRESS:-app.terraform.io}/api/v2"
WORKSPACE_ID="ws-abc123"

# Filter by single status
curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/workspaces/$WORKSPACE_ID/runs?filter[status]=errored" | \
  jq -r '.data[] | "\(.id) | \(.attributes.status) | \(.attributes."created-at")"'

# Filter by multiple statuses
curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/workspaces/$WORKSPACE_ID/runs?filter[status]=errored,canceled" | \
  jq -r '.data[] | "\(.id) | \(.attributes.status)"'

Filter by Status Group
# Non-final runs (in progress)
curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/workspaces/$WORKSPACE_ID/runs?filter[status_group]=non_final"

# Final runs (completed)
curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/workspaces/$WORKSPACE_ID/runs?filter[status_group]=final"

# Discardable runs
curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/workspaces/$WORKSPACE_ID/runs?filter[status_group]=discardable"

Include Plan-Only Runs

By default, plan-only runs are excluded. To include them:

curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/workspaces/$WORKSPACE_ID/runs?filter[operation]=plan_and_apply,plan_only,save_plan,refresh_only,destroy"

List Runs Across Organization
TOKEN="${TFE_TOKEN:?TFE_TOKEN not set}"
BASE_URL="https://${TFE_ADDRESS:-app.terraform.io}/api/v2"
ORG="ForumViriumHelsinki"

# All runs in org (limited info, no total count)
curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/organizations/$ORG/runs?page[size]=20" | \
  jq -r '.data[] | "\(.id) | \(.attributes.status)"'

# Filter by workspace names
curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/organizations/$ORG/runs?filter[workspace_names]=infrastructure-gcp,infrastructure-github"

Formatted Output Examples
Table Format with Resource Changes
curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/workspaces/$WORKSPACE_ID/runs?page[size]=10&include=plan" | \
  jq -r '
    ["RUN_ID", "STATUS", "ADD", "CHG", "DEL", "CREATED"],
    (.data[] | [
      .id,
      .attributes.status,
      (.relationships.plan.data.id as $pid |
        (.included[] | select(.id == $pid) | .attributes."resource-additions" // 0)),
      (.relationships.plan.data.id as $pid |
        (.included[] | select(.id == $pid) | .attributes."resource-changes" // 0)),
      (.relationships.plan.data.id as $pid |
        (.included[] | select(.id == $pid) | .attributes."resource-destructions" // 0)),
      .attributes."created-at"[0:19]
    ]) | @tsv' | column -t

JSON Output for Further Processing
curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/workspaces/$WORKSPACE_ID/runs?page[size]=5" | \
  jq '[.data[] | {
    id: .id,
    status: .attributes.status,
    created: .attributes."created-at",
    message: .attributes.message,
    has_changes: .attributes."has-changes",
    auto_apply: .attributes."auto-apply"
  }]'

Available Filter Parameters
Parameter	Description	Example Values
filter[status]	Run status	applied, errored, planned, canceled
filter[status_group]	Status group	non_final, final, discardable
filter[operation]	Operation type	plan_and_apply, plan_only, destroy
filter[source]	Run source	tfe-api, tfe-ui, tfe-configuration-version
filter[timeframe]	Time period	2024, year, month
search[user]	VCS username	Username string
search[commit]	Commit SHA	SHA string
search[basic]	Combined search	Search term
Run Statuses

Final States: applied, planned_and_finished, discarded, errored, canceled, force_canceled, policy_soft_failed

Non-Final States: pending, planning, planned, cost_estimating, policy_checking, confirmed, applying, and others

Pagination
# Page 2 with 20 items per page
curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/workspaces/$WORKSPACE_ID/runs?page[number]=2&page[size]=20"

# Check pagination info
curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/workspaces/$WORKSPACE_ID/runs" | \
  jq '.meta.pagination'

Rate Limiting

The /runs endpoint has a special rate limit of 30 requests/minute (not 30/second like most endpoints). Plan accordingly when scripting.

See Also
tfc-run-logs: Get plan/apply logs for a run
tfc-run-status: Quick status check for a run
tfc-workspace-runs: Convenience wrapper for known workspaces
Weekly Installs
56
Repository
laurigates/clau…-plugins
GitHub Stars
30
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass