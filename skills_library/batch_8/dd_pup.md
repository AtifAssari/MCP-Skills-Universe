---
title: dd-pup
url: https://skills.sh/datadog-labs/agent-skills/dd-pup
---

# dd-pup

skills/datadog-labs/agent-skills/dd-pup
dd-pup
Installation
$ npx skills add https://github.com/datadog-labs/agent-skills --skill dd-pup
SKILL.md
pup (Datadog CLI)

Pup CLI for Datadog API operations. Supports OAuth2 and API key auth.

Quick Reference
Task	Command
Search error logs	pup logs search --query "status:error" --from 1h
List monitors	pup monitors list
Schedule monitor downtime	pup downtime create --file downtime.json
Find recent slow traces for a service (last 1h)	pup traces search --query "service:<service-name> @duration:>500ms" --from 1h
List incidents	pup incidents list --limit 50
Import incident payload	pup incidents import --file incident.json
Query metrics	pup metrics query --query "avg:system.cpu.user{*}"
List hosts	pup infrastructure hosts list --count 50
Check SLOs	pup slos list
On-call teams	pup on-call teams list
Triage open critical security signals (last 1h)	pup security signals list --query "status:open severity:critical" --from 1h --limit 100
Check auth	pup auth status
Token expiry (time left)	pup auth status
Refresh token	pup auth refresh
Prerequisites

Install pup using the setup instructions.

Required Input Resolution

For commands that need specific scope values (<env>, <service-name>, <team-id>, resource IDs), use this order:

Check context first (conversation history, prior command output, saved variables).
If missing, run a discovery command first (list/search) to get valid values.
If still missing or ambiguous, ask the user to confirm the exact value.
Then run the target command.
Never run commands with unresolved placeholders like <env> or <monitor-id>.
Auth
pup auth login          # OAuth2 browser flow (recommended)
pup auth status         # Check token validity
pup auth refresh        # Refresh expired token (no browser)
pup auth logout         # Clear credentials


⚠️ Tokens expire (~1 hour). If a command fails with 401/403 mid-conversation:

pup auth refresh        # Try refresh first
pup auth login          # If refresh fails, full re-auth


If Chrome opens the wrong profile/window, use the one-time OAuth URL printed by pup auth login (If the browser doesn't open, visit: ...) and open that link manually in the correct account session.

Headless/CI (no browser)
# Use env vars or:
export DD_API_KEY=your-api-key
export DD_APP_KEY=your-app-key
export DD_SITE=datadoghq.com    # or datadoghq.eu, etc.

Command Reference
Monitors
pup monitors list --limit 10
pup monitors list --tags "env:<env>"
pup monitors get <monitor-id>
pup monitors search --query "<monitor-name>"
pup monitors create --file monitor.json
pup monitors update <monitor-id> --file monitor.json
pup monitors delete <monitor-id>
# No pup monitors mute/unmute commands; use downtime payloads instead.
pup downtime create --file downtime.json

Logs
pup logs search --query "status:error" --from 1h
pup logs search --query "service:<service-name>" --from 1h --limit 100
pup logs search --query "@http.status_code:5*" --from 24h
pup logs search --query "env:<env> level:error" --from 1h
pup logs aggregate --query "service:<service-name>" --compute count --from 1h

Metrics
pup metrics query --query "avg:system.cpu.user{*}" --from 1h --to now
pup metrics query --query "sum:trace.express.request.hits{service:<service-name>}" --from 1h --to now
pup metrics list --filter "system.*"

APM / Traces
# Confirm env tag with the user first (do not assume production/prod/prd).
pup apm services list --env <env> --from 1h --to now
pup traces search --query "service:<service-name>" --from 1h
pup traces search --query "service:<service-name> @duration:>500ms" --from 1h
pup traces search --query "service:<service-name> status:error" --from 1h

Incidents
pup incidents list --limit 50
pup incidents get <incident-id>
pup incidents import --file incident.json

Dashboards
pup dashboards list
pup dashboards get <dashboard-id>
pup dashboards create --file dashboard.json
pup dashboards update <dashboard-id> --file dashboard.json
pup dashboards delete <dashboard-id>

SLOs
pup slos list
pup slos get <slo-id>
pup slos status <slo-id> --from 30d --to now
pup slos create --file slo.json

Synthetics
pup synthetics tests list
pup synthetics tests get <test-id>
pup synthetics tests search --text "login"
pup synthetics locations list

On-Call
pup on-call teams list
# Pick a real team id from `pup on-call teams list` output.
pup on-call teams get <team-id>
pup on-call teams memberships list <team-id>

Hosts / Infrastructure
pup infrastructure hosts list --count 50
pup infrastructure hosts list --filter "env:<env>"
pup infrastructure hosts get <host-name>

Events
pup events list --from 24h
pup events list --tags "source:deploy"
pup events search --query "deploy" --from 24h --limit 50
pup events get <event-id>

Downtimes
pup downtime list
pup downtime create --file downtime.json
pup downtime cancel <downtime-id>

Users / Teams
pup users list
pup users get <user-id>

Security
pup security signals list --query "*" --from 1h --limit 100
pup security signals list --query "status:open severity:critical" --from 1h --limit 100
# Broader lookback for historical triage
pup security signals list --query "severity:critical" --from 24h --limit 100

Service Catalog
pup service-catalog list
pup service-catalog get <service-name>

Notebooks
pup notebooks list
pup notebooks get <notebook-id>

Workflows
pup workflows get <workflow-id>
pup workflows run <workflow-id> --payload '{"key":"value"}'
pup workflows instances list <workflow-id>

Observability Pipelines
pup obs-pipelines list --limit 50
pup obs-pipelines get <pipeline-id>
pup obs-pipelines create --file pipeline.json
pup obs-pipelines update <pipeline-id> --file pipeline.json
pup obs-pipelines delete <pipeline-id>
pup obs-pipelines validate --file pipeline.json

LLM Observability
pup llm-obs projects list
pup llm-obs projects create --file project.json
pup llm-obs experiments list
pup llm-obs experiments list --filter-project-id <project-id>
pup llm-obs experiments list --filter-dataset-id <dataset-id>
pup llm-obs experiments create --file experiment.json
pup llm-obs experiments update <experiment-id> --file experiment.json
pup llm-obs experiments delete --file delete-request.json
pup llm-obs datasets list --project-id <project-id>
pup llm-obs datasets create --project-id <project-id> --file dataset.json
pup llm-obs spans search --ml-app <ml-app-name> --from 1h --limit 20

Reference Tables
pup reference-tables list --limit 50
pup reference-tables get <table-id>
pup reference-tables create --file table.json
pup reference-tables batch-query --file query.json

Cost Cloud Configs
# AWS CUR configs
pup cost aws-config list
pup cost aws-config get <account-id>
pup cost aws-config create --file config.json
pup cost aws-config delete <account-id>

# Azure UC configs
pup cost azure-config list
pup cost azure-config get <account-id>
pup cost azure-config create --file config.json
pup cost azure-config delete <account-id>

# GCP usage cost configs
pup cost gcp-config list
pup cost gcp-config get <account-id>
pup cost gcp-config create --file config.json
pup cost gcp-config delete <account-id>

Subcommand Discovery
pup --help              # List all commands
pup <command> --help    # Command-specific help

Error Handling
Error	Cause	Fix
401 Unauthorized	Token expired	pup auth refresh
403 Forbidden	Missing scope	Check app key permissions
404 Not Found	Wrong ID/resource	Verify resource exists
Rate limited	Too many requests	Add delays between calls
Install

See Setup Pup for installation instructions.

Verify Installation
which pup
pup --version

Sites
Site	DD_SITE value
US1 (default)	datadoghq.com
US3	us3.datadoghq.com
US5	us5.datadoghq.com
EU1	datadoghq.eu
AP1	ap1.datadoghq.com
AP2	ap2.datadoghq.com
US1-FED	ddog-gov.com
Weekly Installs
577
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