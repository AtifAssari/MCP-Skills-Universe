---
title: agent-dd
url: https://skills.sh/shhac/agent-dd/agent-dd
---

# agent-dd

skills/shhac/agent-dd/agent-dd
agent-dd
Installation
$ npx skills add https://github.com/shhac/agent-dd --skill agent-dd
SKILL.md
agent-dd — Datadog Triage CLI

Investigate Datadog monitors, logs, metrics, traces, incidents, and SLOs. Triage and debugging workflows only — not full Datadog administration.

When to Use
Checking monitor/alert status, muting/unmuting monitors
Searching logs for errors, spikes, or anomalies
Querying metrics or investigating metric spikes
Searching traces for latency or errors
Managing incidents (list, create, update)
Checking SLO burn rate or error budget
Process
Investigation workflow
Identify the signal: monitors list --status alert or incidents list --status active
Scope the time window: --from now-1h (or broader)
Find the hotspot: logs facets to see which services/hosts/statuses dominate
Gather context: Pull logs, metrics, and traces for the affected service
Correlate: Do log errors align with metric spikes? Do traces show latency?
Always read before acting
Check monitor state before muting: monitors get <id>
Check incident status before updating: incidents get <id>
Preview logs before drawing conclusions: logs search --query "..." --limit 10
Error handling

Errors are JSON to stderr with a classification:

fixable_by: agent — bad query syntax or wrong ID. Read the hint and retry.
fixable_by: human — credentials or permissions. Tell the user.
fixable_by: retry — transient error. Wait and retry once.
Quick Reference
# Explore (read-only)
agent-dd monitors list --status alert
agent-dd monitors get <id>
agent-dd logs search --query "service:web status:error" --from now-1h
agent-dd logs facets --query "status:error" --from now-1h
agent-dd metrics query --query "avg:system.cpu.user{host:web-1}" --from now-1h --to now
agent-dd traces search --service my-api --from now-30m
agent-dd incidents list --status active
agent-dd slo list
agent-dd hosts list --tag "env:production"

# Triage actions
agent-dd monitors mute <id> --reason "investigating" --end now+1h
agent-dd monitors unmute <id>
agent-dd incidents create --title "Elevated error rate" --severity SEV-3
agent-dd incidents update <id> --status stable

# Discovery
agent-dd metrics list --search "system.cpu"
agent-dd traces services [--env production] [--search checkout]
agent-dd slo history <id> --from now-7d --to now

Query Syntax

Log queries: service:web status:error @http.status_code:>500 "timeout" Metric queries: avg:system.cpu.user{host:web-1} by {service} Trace queries: same as log syntax, with @duration:>1000000000 (nanoseconds)

For full operator reference (wildcards, booleans, numeric comparisons, facets): see references/query-syntax.md

Key Concepts
Time formats: relative (now-15m, now-1h, now-7d), RFC3339, or unix epoch. Defaults: --from now-1h, --to now
Output: NDJSON for list/search commands, JSON for single items. --full for complete API response. --format json|yaml|jsonl to override
Monitor statuses: ok, alert, warn, no_data, unknown
Incident severities: SEV-1 (critical) through SEV-5 (informational)
Incident statuses: active, stable, resolved
Deeper Reference

Per-domain details with examples and field descriptions (only load when you need specifics not covered above):

agent-dd usage                    # top-level command overview
agent-dd logs usage               # log query examples, sort options, compact vs full
agent-dd monitors usage           # monitor statuses, muting best practices
agent-dd metrics usage            # metric query syntax, aggregation details
agent-dd traces usage             # trace search, duration units
agent-dd incidents usage          # severity guide, lifecycle
agent-dd slo usage                # error budgets, history interpretation

Organization Setup

If credentials aren't configured yet:

agent-dd org add <alias> --api-key <key> --app-key <key> [--site datadoghq.com]
agent-dd org test


Keys are in Datadog → Organization Settings → API Keys / Application Keys.

Environment variables also work: DD_API_KEY, DD_APP_KEY, DD_SITE.

Weekly Installs
13
Repository
shhac/agent-dd
GitHub Stars
1
First Seen
4 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail