---
rating: ⭐⭐⭐
title: n8n-automation
url: https://skills.sh/site/smithery.ai/n8n-automation
---

# n8n-automation

skills/smithery.ai/n8n-automation
n8n-automation
$ npx skills add https://smithery.ai/skills/openclaw/n8n-automation
SKILL.md
n8n Automation

Control n8n workflow automation platform via REST API.

Setup

Set these environment variables (or store in .n8n-api-config):

export N8N_API_URL="https://your-instance.app.n8n.cloud/api/v1"  # or http://localhost:5678/api/v1
export N8N_API_KEY="your-api-key-here"


Generate API key: n8n Settings → n8n API → Create an API key.

Quick Reference

All calls use header X-N8N-API-KEY for auth.

List Workflows
curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_API_URL/workflows" | jq '.data[] | {id, name, active}'

Get Workflow Details
curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_API_URL/workflows/{id}"

Activate/Deactivate Workflow
# Activate
curl -s -X PATCH -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"active": true}' "$N8N_API_URL/workflows/{id}"

# Deactivate
curl -s -X PATCH -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"active": false}' "$N8N_API_URL/workflows/{id}"

Trigger Workflow (via webhook)
# Production webhook
curl -s -X POST "$N8N_API_URL/../webhook/{webhook-path}" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'

# Test webhook
curl -s -X POST "$N8N_API_URL/../webhook-test/{webhook-path}" \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'

List Executions
# All recent executions
curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_API_URL/executions?limit=10" | jq '.data[] | {id, workflowId, status, startedAt}'

# Failed executions only
curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_API_URL/executions?status=error&limit=5"

# Executions for specific workflow
curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_API_URL/executions?workflowId={id}&limit=10"

Get Execution Details
curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_API_URL/executions/{id}"

Create Workflow (from JSON)
curl -s -X POST -H "X-N8N-API-KEY: $N8N_API_KEY" \
  -H "Content-Type: application/json" \
  -d @workflow.json "$N8N_API_URL/workflows"

Delete Workflow
curl -s -X DELETE -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_API_URL/workflows/{id}"

Common Patterns
Health Check (run periodically)

List active workflows, check recent executions for errors, report status:

# Count active workflows
ACTIVE=$(curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_API_URL/workflows?active=true" | jq '.data | length')

# Count failed executions (last 24h)
FAILED=$(curl -s -H "X-N8N-API-KEY: $N8N_API_KEY" "$N8N_API_URL/executions?status=error&limit=100" | jq '[.data[] | select(.startedAt > (now - 86400 | todate))] | length')

echo "Active workflows: $ACTIVE | Failed (24h): $FAILED"

Debug Failed Execution
List failed executions → get execution ID
Fetch execution details → find the failing node
Check node parameters and input data
Suggest fix based on error message
Workflow Summary

Parse workflow JSON to summarize: trigger type, node count, apps connected, schedule.

API Endpoints Reference

See references/api-endpoints.md for complete endpoint documentation.

Tips
API key has full access on non-enterprise plans
Rate limits vary by plan (cloud) or are unlimited (self-hosted)
Webhook URLs are separate from API URLs (no auth header needed)
Use ?active=true or ?active=false to filter workflow listings
Execution data may be pruned based on n8n retention settings
Weekly Installs
10
Source
smithery.ai/ski…tomation
First Seen
Mar 8, 2026