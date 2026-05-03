---
rating: ⭐⭐⭐
title: dd-logs
url: https://skills.sh/datadog-labs/agent-skills/dd-logs
---

# dd-logs

skills/datadog-labs/agent-skills/dd-logs
dd-logs
Installation
$ npx skills add https://github.com/datadog-labs/agent-skills --skill dd-logs
SKILL.md
Datadog Logs

Search, process, and archive logs with cost awareness.

Prerequisites

Datadog Pup should already be installed. See Setup Pup if not.

Command Execution Order (Token-Efficient)

For scoped commands, use this order:

Check context first (prior outputs, conversation, saved values).
If a required value is missing, run a discovery command first.
If still ambiguous, ask the user to confirm.
Then run the target command.
Avoid speculative commands likely to fail.
Quick Start
pup auth login

Search Logs
# Basic search
pup logs search --query="status:error" --from="1h"

# With filters
pup logs search --query="service:api status:error" --from="1h" --limit 100

# JSON output
pup logs search --query="@http.status_code:>=500" --from="1h"

Search Syntax
Query	Meaning
error	Full-text search
status:error	Tag equals
@http.status_code:500	Attribute equals
@http.status_code:>=400	Numeric range
service:api AND env:prod	Boolean
@message:*timeout*	Wildcard
Configuration APIs

Available log configuration commands in pup 0.42.0:

# List log archives
pup logs archives list

# List log restriction queries
pup logs restriction-queries list

# List custom log destinations
pup logs custom-destinations list

Common Processors
{
  "name": "API Logs",
  "filter": {"query": "service:api"},
  "processors": [
    {
      "type": "grok-parser",
      "name": "Parse nginx",
      "source": "message",
      "grok": {"match_rules": "%{IPORHOST:client_ip} %{DATA:method} %{DATA:path} %{NUMBER:status}"}
    },
    {
      "type": "status-remapper",
      "name": "Set severity",
      "sources": ["level", "severity"]
    },
    {
      "type": "attribute-remapper",
      "name": "Remap user_id",
      "sources": ["user_id"],
      "target": "usr.id"
    }
  ]
}

⚠️ Exclusion Filters (Cost Control)

Index only what matters:

{
  "name": "Drop debug logs",
  "filter": {"query": "status:debug"},
  "is_enabled": true
}

High-Volume Exclusions
# Find noisiest log sources
pup logs search --query="*" --from="1h" | jq 'group_by(.service) | map({service: .[0].service, count: length}) | sort_by(-.count)[:10]'

Exclude	Query
Health checks	@http.url:"/health" OR @http.url:"/ready"
Debug logs	status:debug
Static assets	@http.url:*.css OR @http.url:*.js
Heartbeats	@message:*heartbeat*
Archives

Store logs cheaply for compliance:

# List archives
pup logs archives list

# Archive config (S3 example)
{
  "name": "compliance-archive",
  "query": "*",
  "destination": {
    "type": "s3",
    "bucket": "my-logs-archive",
    "path": "/datadog"
  },
  "rehydration_tags": ["team:platform"]
}

Rehydrate (Restore)
# No `pup logs rehydrate` command in pup 0.42.0.
# Use Datadog UI/API for rehydration workflows.

Log-Based Metrics

Create metrics from logs (cheaper than indexing):

# List log-based metrics
pup logs metrics list

# Get one metric by ID
pup logs metrics get api.errors.count


⚠️ Cardinality warning: Group by bounded values only.

Sensitive Data
Scrubbing Rules
{
  "type": "hash-remapper",
  "name": "Hash emails",
  "sources": ["email", "@user.email"]
}

Never Log
# In your app - sanitize before sending
import re

def sanitize_log(message: str) -> str:
    # Remove credit cards
    message = re.sub(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b', '[REDACTED]', message)
    # Remove SSNs
    message = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[REDACTED]', message)
    return message

Troubleshooting
Problem	Fix
Logs not appearing	Check agent, pipeline filters
High costs	Add exclusion filters
Search slow	Narrow time range, use indexes
Missing attributes	Check grok parser
References/Documentation
Log Search Syntax
Pipelines
Exclusion Filters
Archives
Weekly Installs
500
Repository
datadog-labs/ag…t-skills
GitHub Stars
101
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass