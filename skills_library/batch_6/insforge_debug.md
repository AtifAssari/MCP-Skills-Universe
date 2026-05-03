---
title: insforge-debug
url: https://skills.sh/insforge/agent-skills/insforge-debug
---

# insforge-debug

skills/insforge/agent-skills/insforge-debug
insforge-debug
Installation
$ npx skills add https://github.com/insforge/agent-skills --skill insforge-debug
SKILL.md
InsForge Debug

Diagnose problems in InsForge projects — from frontend SDK errors to backend infrastructure issues. This skill helps you locate problems by running the right commands and surfacing logs/status. The manual scenarios below locate problems without suggesting fixes; the AI-assisted path additionally returns suggested causes and solutions.

Always use npx @insforge/cli — never install the CLI globally.

AI-Assisted Diagnosis (Fastest Path)

When the user gives a concrete description of the problem (error message, failing URL, HTTP status), hand it to the InsForge debug agent. It inspects backend state on its own and returns a diagnosis plus possible solutions.

npx @insforge/cli diagnose --ai "<issue description>"


When to use this path first:

The user pastes an error, request URL, or status code and asks "why?"
You want a fast first pass before drilling into the manual scenarios below
The problem spans multiple subsystems (frontend + backend + database) and you're not sure where to start

Examples:

# Edge function error
npx @insforge/cli diagnose --ai "I invoked edge function https://kttprzh4.functions.insforge.app/newton, got error: 508: Loop Detected (LOOP_DETECTED)\n\nRecursive requests to the same deployment cannot be processed."

# Slow database query
npx @insforge/cli diagnose --ai "I query data with https://kttprzh4.us-west.insforge.app/api/database/records/order_customer_details?select=*&order=total_amount.desc, it costs 1.4s, why?"

# Unresponsive backend / 504
npx @insforge/cli diagnose --ai "my backend is unresponsive, request https://kttprzh4.us-west.insforge.app/api/database/records/todo?select=*&order=created_at.desc got 504 error, why?"


Unlike the other commands in this skill, diagnose --ai returns both a diagnosis and suggested solutions. Relay them to the user as a starting point, but verify against the underlying logs/metrics (the scenarios below) before committing to a fix.

Quick Triage

Match the symptom to a scenario, then follow that scenario's steps.

Symptom	Scenario
SDK returns { data: null, error: {...} }	#1 SDK Error
HTTP 400 / 401 / 403 / 404 / 429 / 500	#2 HTTP Status Code
Function throws or times out	#3 Edge Function Failure
Query slow or hangs	#4 Database Slow
Login fails / token expired / RLS denied	#5 Auth Failure
Channel won't connect / messages missing	#6 Realtime Issues
High CPU/memory, all responses slow	#7 Backend Performance
functions deploy fails	#8 Function Deploy
deployments deploy fails / Vercel error	#9 Frontend Deploy
Scenario 1: SDK Returns Error Object

Symptoms: SDK call returns { data: null, error: { code, message, details } }. PostgREST error codes like PGRST301, PGRST204, etc.

Steps:

Read the error object — extract code, message, details from the SDK response.
Check aggregated error logs to find matching backend errors:
npx @insforge/cli diagnose logs

Based on the error code prefix, drill into the relevant log source:
Error pattern	Log source	Command
PGRST* (PostgREST)	postgREST.logs	npx @insforge/cli logs postgREST.logs --limit 50
Database/SQL errors	postgres.logs	npx @insforge/cli logs postgres.logs --limit 50
Generic 500 / server error	insforge.logs	npx @insforge/cli logs insforge.logs --limit 50
If the error is DB-related, check database health for additional context:
npx @insforge/cli diagnose db --check connections,locks,slow-queries


Information gathered: Error code, backend log entries around the error timestamp, database health status.

Scenario 2: HTTP Status Code Anomaly

Symptoms: API calls return 400, 401, 403, 404, 429, or 500.

Steps:

Identify the status code from the response.
Follow the path for that status code:
Status	What to check	Command
400	Request payload/params malformed	npx @insforge/cli logs postgREST.logs --limit 50
401	Auth token missing or expired	npx @insforge/cli logs insforge.logs --limit 50
403	RLS policy or permission denied	npx @insforge/cli logs insforge.logs --limit 50
404	Endpoint or resource doesn't exist	npx @insforge/cli metadata --json
429	Rate limit hit — no backend logs recorded	See 429 note below
500	Server-side error	npx @insforge/cli diagnose logs
For 500 errors, also check aggregate error logs across all sources:
npx @insforge/cli diagnose logs

429 Rate Limit: The backend does not log 429 responses and does not return Retry-After or X-RateLimit-* headers. Checking logs will not help. Instead:
Review client code for high-frequency request patterns: loops without throttling, missing debounce, retry without exponential backoff, or parallel calls that could be batched.
Check overall backend load to see if the system is under heavy traffic:
npx @insforge/cli diagnose metrics --range 1h

A 429 status confirms the request was rate-limited. The fix is always on the client side: reduce request frequency, add backoff/debounce, or batch operations.

Information gathered: Status code context, relevant log entries, request/response details from logs. For 429: client-side request patterns and backend load metrics.

Scenario 3: Edge Function Execution Failure/Timeout

Symptoms: functions invoke returns error, function times out, or throws runtime exception.

Steps:

Check function execution logs:
npx @insforge/cli logs function.logs --limit 50

Verify the function exists and is active:
npx @insforge/cli functions list

Inspect the function source for obvious issues:
npx @insforge/cli functions code <slug>


Information gathered: Function runtime errors, function status, source code, EC2 resource metrics.

Scenario 4: Database Query Slow or Unresponsive

Symptoms: Queries take too long, hang indefinitely, or connection pool is exhausted.

Steps:

Check database health — slow queries, active connections, locks:
npx @insforge/cli diagnose db --check slow-queries,connections,locks

Check postgres logs for query errors or warnings:
npx @insforge/cli logs postgres.logs --limit 50

Check index usage and table bloat:
npx @insforge/cli diagnose db --check index-usage,bloat,cache-hit,size

If the whole system feels slow, check EC2 instance metrics:
npx @insforge/cli diagnose metrics --range 1h


Information gathered: Slow query details, connection pool state, lock contention, index efficiency, table bloat, cache hit ratio, EC2 resource usage.

Scenario 5: Authentication/Authorization Failure

Symptoms: Login fails, signup errors, token expired, OAuth callback error, RLS policy denies access.

Steps:

Check insforge.logs for auth-related errors (login failures, token issues, OAuth errors):
npx @insforge/cli logs insforge.logs --limit 50

Check postgREST.logs for RLS policy violations:
npx @insforge/cli logs postgREST.logs --limit 50

Verify the project's auth configuration:
npx @insforge/cli metadata --json

If RLS suspected, inspect current policies:
npx @insforge/cli db policies


Information gathered: Auth error details, RLS violation logs, auth configuration state, active RLS policies.

Scenario 6: Realtime Channel Issues

Symptoms: WebSocket won't connect, channel subscription fails, messages not received or lost.

Steps:

Check insforge.logs for realtime/WebSocket errors:
npx @insforge/cli logs insforge.logs --limit 50

Verify the channel pattern exists and is enabled:
npx @insforge/cli db query "SELECT pattern, description, enabled FROM realtime.channels"

If access is restricted, check RLS on realtime tables:
npx @insforge/cli db policies

If the issue is widespread (all channels affected), check overall backend health:
npx @insforge/cli diagnose


Information gathered: WebSocket error logs, channel configuration, realtime RLS policies, overall backend health.

Scenario 7: Backend Performance Degradation

Symptoms: All responses slow, high latency, intermittent failures across the board.

Steps:

Check EC2 instance metrics — CPU, memory, disk, network:
npx @insforge/cli diagnose metrics --range 1h

Check database health (often the bottleneck):
npx @insforge/cli diagnose db

Check aggregate error logs:
npx @insforge/cli diagnose logs

Check advisor for known critical issues:
npx @insforge/cli diagnose advisor --severity critical


Information gathered: CPU/memory/disk/network metrics (current and trend), database health, error log summary, advisor warnings.

Scenario 8: Edge Function Deploy Failure

Symptoms: functions deploy <slug> command fails, function not appearing in the list after deploy.

Steps:

Re-run the deploy command and capture the error output:
npx @insforge/cli functions deploy <slug>

Check deployment-related errors:
npx @insforge/cli logs function-deploy.logs --limit 50

Verify whether the function exists in the list:
npx @insforge/cli functions list


Information gathered: Deploy command error output, function deployment logs, function list status, backend error logs.

Scenario 9: Frontend (Vercel) Deploy Failure

Symptoms: deployments deploy command fails, deployment status shows error, Vercel build errors.

Steps:

Check recent deployment attempts:
npx @insforge/cli deployments list

Get the status and error details for the failed deployment:
npx @insforge/cli deployments status <id> --json


The --json output includes a metadata object with Vercel-specific context: target, fileCount, projectId, startedAt, envVarKeys, webhookEventType (e.g., deployment.succeeded or deployment.error), etc. This metadata captures the full deployment context and can be used for debugging or AI-assisted investigation.

Verify the local build succeeds before investigating further:
npm run build


Information gathered: Deployment history, deployment metadata (Vercel context, status, webhook events), local build output, backend deployment API logs.

Command Quick Reference
Logs
npx @insforge/cli logs <source> [--limit <n>]

Source	Description
insforge.logs	Main backend logs
postgREST.logs	PostgREST API layer logs
postgres.logs	PostgreSQL database logs
function.logs	Edge function execution logs
function-deploy.logs	Edge function deployment logs

Source names are case-insensitive.

Diagnostics
# Full health report (all checks)
npx @insforge/cli diagnose

# AI-powered diagnosis from a natural-language problem description
# Returns diagnosis + suggested solutions
npx @insforge/cli diagnose --ai "<issue description>"

# EC2 instance metrics (CPU, memory, disk, network)
npx @insforge/cli diagnose metrics [--range 1h|6h|24h|7d] [--metrics <list>]

# Advisor scan results
npx @insforge/cli diagnose advisor [--severity critical|warning|info] [--category security|performance|health] [--limit <n>]

# Database health checks
npx @insforge/cli diagnose db [--check <checks>]
# checks: connections, slow-queries, bloat, size, index-usage, locks, cache-hit (default: all)

# Aggregate error logs from all sources
npx @insforge/cli diagnose logs [--source <name>] [--limit <n>]

Supporting Commands
# Project metadata (auth config, tables, buckets, functions, etc.)
npx @insforge/cli metadata --json

# Edge functions
npx @insforge/cli functions list
npx @insforge/cli functions code <slug>

# Secrets
npx @insforge/cli secrets list [--all]
npx @insforge/cli secrets get <key>
npx @insforge/cli secrets add <key> <value> [--reserved] [--expires <ISO date>]

# Database
npx @insforge/cli db policies
npx @insforge/cli db query "<sql>"

# Deployments
npx @insforge/cli deployments list
npx @insforge/cli deployments status <id> --json

Weekly Installs
3.6K
Repository
insforge/agent-skills
GitHub Stars
14
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail