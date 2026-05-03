---
title: sentry
url: https://skills.sh/openai/skills/sentry
---

# sentry

skills/openai/skills/sentry
sentry
Installation
$ npx skills add https://github.com/openai/skills --skill sentry
Summary

Read-only Sentry API queries for production error inspection and health summaries.

Requires SENTRY_AUTH_TOKEN with read-only scopes (project:read, event:read, org:read); supports optional org, project, and base URL environment variables
Core commands: list unresolved issues, fetch issue details, retrieve events for an issue, and inspect individual event data with automatic PII redaction
Defaults to 24-hour time range, production environment, and 20-result limit (max 50); supports pagination and optional search queries
Built-in Python script handles API pagination, transient error retries, and deterministic GET-only calls to five core Sentry endpoints
SKILL.md
Sentry (Read-only Observability)
Quick start
If not already authenticated, ask the user to run sentry auth login or set SENTRY_AUTH_TOKEN as an env var.
The CLI auto-detects org/project from DSNs in .env files, source code, config defaults, and directory names. Only specify <org>/<project> if auto-detection fails or picks the wrong target.
Defaults: time range 24h, environment production, limit 20.
Always use --json when processing output programmatically. Use --json --fields to select specific fields and reduce output size.
Use sentry schema <resource> to discover API endpoints quickly.

If the CLI is not installed, give the user these steps:

Install the Sentry CLI: curl https://cli.sentry.dev/install -fsS | bash
Authenticate: sentry auth login
Confirm authentication: sentry auth status
Never ask the user to paste the full token in chat. Ask them to set it locally and confirm when ready.
Core tasks (use Sentry CLI)

Use the sentry CLI for all queries. It handles authentication, org/project detection, pagination, and retries automatically. Use --json for machine-readable output.

1) List issues (ordered by most recent)
sentry issue list \
  --query "is:unresolved environment:production" \
  --period 24h \
  --limit 20 \
  --json --fields shortId,title,priority,level,status


If auto-detection doesn't resolve org/project, pass them explicitly:

sentry issue list {your-org}/{your-project} \
  --query "is:unresolved environment:production" \
  --period 24h \
  --limit 20 \
  --json

2) Resolve an issue short ID to issue detail
sentry issue view {ABC-123} --json


Use the short ID format (e.g., ABC-123), not the numeric ID.

3) Issue detail
sentry issue view {ABC-123}

4) Issue events
sentry issue events {ABC-123} --limit 20 --json

5) Event detail
sentry event view {your-org}/{your-project}/{event_id} --json

6) AI-powered root cause analysis
sentry issue explain {ABC-123}

7) AI-powered fix plan
sentry issue plan {ABC-123}

Fallback: arbitrary API access

For endpoints not covered by dedicated CLI commands, use sentry api:

sentry api /api/0/organizations/{your-org}/ --method GET


Use sentry schema to discover available API endpoints:

sentry schema issues

Inputs and defaults
org_slug, project_slug: auto-detected by the CLI from DSNs, env vars, and directory names. Override with positional {your-org}/{your-project} if auto-detection fails.
time_range: default 24h (pass as --period 24h).
environment: default prod (pass as part of --query, e.g., environment:production).
limit: default 20 (pass as --limit).
search_query: optional --query parameter, uses Sentry search syntax (e.g., is:unresolved, assigned:me).
issue_short_id: use directly with sentry issue view.
Output formatting rules
Issue list: show title, short_id, status, first_seen, last_seen, count, environments, top_tags; order by most recent.
Event detail: include culprit, timestamp, environment, release, url.
If no results, state explicitly.
Redact PII in output (emails, IPs). Do not print raw stack traces.
Never echo auth tokens.
Golden test inputs
Org: {your-org}
Project: {your-project}
Issue short ID: {ABC-123}

Example prompt: "List the top 10 open issues for prod in the last 24h." Expected: ordered list with titles, short IDs, counts, last seen.

Weekly Installs
910
Repository
openai/skills
GitHub Stars
18.0K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn