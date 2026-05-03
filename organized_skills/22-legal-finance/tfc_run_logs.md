---
rating: ⭐⭐⭐
title: tfc-run-logs
url: https://skills.sh/laurigates/claude-plugins/tfc-run-logs
---

# tfc-run-logs

skills/laurigates/claude-plugins/tfc-run-logs
tfc-run-logs
Installation
$ npx skills add https://github.com/laurigates/claude-plugins --skill tfc-run-logs
SKILL.md
Terraform Cloud Run Logs

Retrieve and display plan and/or apply logs from Terraform Cloud runs directly in the terminal.

When to Use
Scenario	Use this skill	Alternative
Read plan output for a TFC run	tfc-run-logs	-
Read apply output for a TFC run	tfc-run-logs	-
Debug a failed plan or apply	tfc-run-logs	-
Review infrastructure changes in text form	tfc-run-logs	-
Analyze resource changes as structured JSON	tfc-plan-json	Use plan-json for programmatic analysis
Quick pass/fail status without reading logs	tfc-run-status	Use run-status for status only
Find the run ID to inspect	tfc-list-runs or tfc-workspace-runs	Use list-runs to find the run first
Prerequisites
# Required environment variables
export TFE_TOKEN="your-api-token"        # User or team token (not organization token)
export TFE_ADDRESS="app.terraform.io"    # Optional, defaults to app.terraform.io

Core Workflow
Get Both Plan and Apply Logs
#!/bin/bash
set -euo pipefail

TOKEN="${TFE_TOKEN:?TFE_TOKEN not set}"
BASE_URL="https://${TFE_ADDRESS:-app.terraform.io}/api/v2"
RUN_ID="${1:?Usage: $0 <run-id>}"

# Get run with plan and apply relationships
RUN_DATA=$(curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/runs/$RUN_ID?include=plan,apply")

# Extract IDs
PLAN_ID=$(echo "$RUN_DATA" | jq -r '.data.relationships.plan.data.id')
APPLY_ID=$(echo "$RUN_DATA" | jq -r '.data.relationships.apply.data.id // empty')

# Get and display plan logs
PLAN_LOG_URL=$(curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/plans/$PLAN_ID" | jq -r '.data.attributes."log-read-url"')

echo "=== PLAN OUTPUT ==="
curl -sf "$PLAN_LOG_URL" | sed 's/\x1b\[[0-9;]*m//g'  # Strip ANSI codes

# Get apply logs if exists
if [ -n "$APPLY_ID" ]; then
  APPLY_LOG_URL=$(curl -sf --header "Authorization: Bearer $TOKEN" \
    "$BASE_URL/applies/$APPLY_ID" | jq -r '.data.attributes."log-read-url"')

  echo ""
  echo "=== APPLY OUTPUT ==="
  curl -sf "$APPLY_LOG_URL" | sed 's/\x1b\[[0-9;]*m//g'
fi

Get Plan Logs Only
TOKEN="${TFE_TOKEN:?TFE_TOKEN not set}"
BASE_URL="https://${TFE_ADDRESS:-app.terraform.io}/api/v2"
RUN_ID="run-abc123"

# Get plan ID from run
PLAN_ID=$(curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/runs/$RUN_ID" | jq -r '.data.relationships.plan.data.id')

# Get log URL and fetch logs
PLAN_LOG_URL=$(curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/plans/$PLAN_ID" | jq -r '.data.attributes."log-read-url"')

curl -sf "$PLAN_LOG_URL"

Get Apply Logs Only
TOKEN="${TFE_TOKEN:?TFE_TOKEN not set}"
BASE_URL="https://${TFE_ADDRESS:-app.terraform.io}/api/v2"
RUN_ID="run-abc123"

# Get apply ID from run
APPLY_ID=$(curl -sf --header "Authorization: Bearer $TOKEN" \
  "$BASE_URL/runs/$RUN_ID" | jq -r '.data.relationships.apply.data.id')

if [ -n "$APPLY_ID" ] && [ "$APPLY_ID" != "null" ]; then
  # Get log URL and fetch logs
  APPLY_LOG_URL=$(curl -sf --header "Authorization: Bearer $TOKEN" \
    "$BASE_URL/applies/$APPLY_ID" | jq -r '.data.attributes."log-read-url"')

  curl -sf "$APPLY_LOG_URL"
else
  echo "No apply for this run"
fi

Quick One-Liners
Plan Logs (with ANSI colors)
curl -sf -H "Authorization: Bearer $TFE_TOKEN" \
  "https://app.terraform.io/api/v2/runs/run-abc123?include=plan" | \
  jq -r '.included[0].attributes."log-read-url"' | xargs curl -sf

Plan Logs (clean text)
curl -sf -H "Authorization: Bearer $TFE_TOKEN" \
  "https://app.terraform.io/api/v2/runs/run-abc123?include=plan" | \
  jq -r '.included[0].attributes."log-read-url"' | \
  xargs curl -sf | sed 's/\x1b\[[0-9;]*m//g'

Important Notes
Log URLs are secrets: Archivist URLs contain embedded authentication - don't log them
URLs expire: Log URLs are valid for 25 hours
No auth needed for logs: Once you have the archivist URL, no bearer token is required
ANSI codes: Logs contain color codes; use sed to strip them for clean output
Rate limits: /runs endpoint is limited to 30 requests/minute
Common Errors
404 Not Found
Run ID doesn't exist OR you don't have permission
TFC returns 404 for both cases (security measure)
401 Unauthorized
Token is invalid or expired
Organization tokens cannot access run data - use user/team token
No Apply Logs
Run may be plan-only, not yet applied, or discarded
Check run status first
See Also
tfc-run-status: Quick status check for a run
tfc-list-runs: List recent runs in a workspace
tfc-plan-json: Get structured plan JSON output
Weekly Installs
59
Repository
laurigates/clau…-plugins
GitHub Stars
30
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn