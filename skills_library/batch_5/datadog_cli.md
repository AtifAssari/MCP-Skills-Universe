---
title: datadog-cli
url: https://skills.sh/davila7/claude-code-templates/datadog-cli
---

# datadog-cli

skills/davila7/claude-code-templates/datadog-cli
datadog-cli
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill datadog-cli
SKILL.md
Datadog CLI

A CLI tool for AI agents to debug and triage using Datadog logs and metrics.

Required Reading

You MUST read the relevant reference docs before using any command:

Log Commands
Metrics
Query Syntax
Workflows
Dashboards
Setup
Environment Variables (Required)
export DD_API_KEY="your-api-key"
export DD_APP_KEY="your-app-key"


Get keys from: https://app.datadoghq.com/organization-settings/api-keys

Running the CLI
npx @leoflores/datadog-cli <command>


For non-US Datadog sites, use --site flag:

npx @leoflores/datadog-cli logs search --query "*" --site datadoghq.eu

Commands Overview
Command	Description
logs search	Search logs with filters
logs tail	Stream logs in real-time
logs trace	Find logs for a distributed trace
logs context	Get logs before/after a timestamp
logs patterns	Group similar log messages
logs compare	Compare log counts between periods
logs multi	Run multiple queries in parallel
logs agg	Aggregate logs by facet
metrics query	Query timeseries metrics
errors	Quick error summary by service/type
services	List services with log activity
dashboards	Manage dashboards (CRUD)
dashboard-lists	Manage dashboard lists
Quick Examples
Search Errors
npx @leoflores/datadog-cli logs search --query "status:error" --from 1h --pretty

Tail Logs (Real-time)
npx @leoflores/datadog-cli logs tail --query "service:api status:error" --pretty

Error Summary
npx @leoflores/datadog-cli errors --from 1h --pretty

Trace Correlation
npx @leoflores/datadog-cli logs trace --id "abc123def456" --pretty

Query Metrics
npx @leoflores/datadog-cli metrics query --query "avg:system.cpu.user{*}" --from 1h --pretty

Compare Periods
npx @leoflores/datadog-cli logs compare --query "status:error" --period 1h --pretty

Global Flags
Flag	Description
--pretty	Human-readable output with colors
--output <file>	Export results to JSON file
--site <site>	Datadog site (e.g., datadoghq.eu)
Time Formats
Relative: 30m, 1h, 6h, 24h, 7d
ISO 8601: 2024-01-15T10:30:00Z
Incident Triage Workflow
# 1. Quick error overview
npx @leoflores/datadog-cli errors --from 1h --pretty

# 2. Is this new? Compare to previous period
npx @leoflores/datadog-cli logs compare --query "status:error" --period 1h --pretty

# 3. Find error patterns
npx @leoflores/datadog-cli logs patterns --query "status:error" --from 1h --pretty

# 4. Narrow down by service
npx @leoflores/datadog-cli logs search --query "status:error service:api" --from 1h --pretty

# 5. Get context around a timestamp
npx @leoflores/datadog-cli logs context --timestamp "2024-01-15T10:30:00Z" --service api --pretty

# 6. Follow the distributed trace
npx @leoflores/datadog-cli logs trace --id "TRACE_ID" --pretty


See workflows.md for more debugging workflows.

Weekly Installs
281
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass