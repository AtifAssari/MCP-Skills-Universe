---
rating: ⭐⭐
title: cloudflare-traffic-investigator
url: https://skills.sh/delexw/claude-code-misc/cloudflare-traffic-investigator
---

# cloudflare-traffic-investigator

skills/delexw/claude-code-misc/cloudflare-traffic-investigator
cloudflare-traffic-investigator
Installation
$ npx skills add https://github.com/delexw/claude-code-misc --skill cloudflare-traffic-investigator
SKILL.md
Investigating Traffic on Cloudflare-Protected Domains
Inputs

Raw arguments: $ARGUMENTS

Infer from the arguments:

DOMAIN: Cloudflare-protected domain to investigate
ZONE_ID: Cloudflare zone ID for the domain
TIME_RANGE: (optional) time range to investigate, in current agent's local timezone (detect via system clock)
SINCE: (optional) UTC ISO8601 start of analysis window. When provided, takes precedence over TIME_RANGE for all GraphQL queries.
UNTIL: (optional) UTC ISO8601 end of analysis window. When provided, takes precedence over TIME_RANGE for all GraphQL queries.
TZ_DISPLAY: (optional) Timezone abbreviation for report display (e.g. the output of date +"%Z" on the calling machine). When provided, use this as the pinned timezone instead of detecting via system clock in Step 1.

If domain or zone ID cannot be inferred, ask the user via AskUserQuestion. Time range is collected in Step 1 if neither TIME_RANGE nor SINCE/UNTIL are provided.

Investigate unusual traffic patterns on Cloudflare-protected domains that cause downstream service failures (e.g., service overload, database saturation, API rate limiting). This skill walks through a structured investigation from confirming the spike through to a full incident report.

Investigation Workflow

Follow these steps in order. Each step file contains detailed instructions and example Cloudflare GraphQL queries.

Get parameters — Collect time range and zone info
Confirm spike — Query hourly traffic to verify the anomaly
Minute-level detail — Narrow to exact spike timing
Identify culprit JA4 — Find JA4 fingerprints with highest request counts
Analyze traffic — For top JA4s, identify paths, user IDs, ASNs
Verify legitimacy — Check bot scores, WAF scores, User-Agent 6b. Check WAF & page rules — Inventory active WAF rules, rate limits, and page rules; identify protection gaps
Extract top users — Find which users made the most requests
Synthesize & report — Combine findings into an incident report
Cloudflare API CLI

All Cloudflare interactions use the cloudflare-mcp-cli CLI tool (via cloudflare-mcp-cli):

cloudflare-mcp-cli search '<async fn>' — Discover API endpoints by searching the OpenAPI spec
cloudflare-mcp-cli execute '<async fn>' — Execute API calls via cloudflare.request() (GraphQL analytics via POST to /graphql, Radar via REST, zone operations via /zones)

See Cloudflare API CLI Reference for query patterns and examples.

JA4 TLS Fingerprints
Format: t13dNNNNNN_XXXXXXXXXXXX_YYYYYYYYYYYY
A single fingerprint across millions of requests indicates backend service configuration, not individual users
Useful for identifying automated/service-to-service traffic
Cross-reference with the CLOUDFLARE_JA4 environment variable before flagging as unknown
Cloudflare Sampled Data

Firewall events use adaptive sampling. Numbers are sampled counts, not actual totals. Use them for pattern identification and relative comparisons — top users in sample likely represent top users overall. Always note this in reports.

Common Failure Patterns

Quickly identify root causes using these patterns:

Pattern	Signal	Resolution
Circuit Breaker Cascade	429 → timeout → breaker opens	Scale service or add rate limiting
Retry Storm	Error count exceeds initial traffic	Add exponential backoff, client-side circuit breaker
Single User Amplification	One user dominates request count	Contact user, fix frontend logic
Undersized Service	Normal distribution, fails at <10 req/sec	Scale service capacity urgently
Cascading Failure	Multiple services failing sequentially	Isolate fault, restart root service
Cache Stampede	Spike after cache expiration	Cache lock, stale-while-revalidate

Detailed descriptions and resolution steps: Failure Patterns Reference

Escalation Criteria
Priority	Condition
P1 — Immediate	Service 429 errors / circuit breaker open, >10% error rate, cascading failures
P2 — High	Single user >500 req/hour on critical endpoint, sustained spike >50% above baseline, multiple dependencies affected
P3 — Monitor	Moderate increase <50% above baseline, isolated user anomalies
Incident Report

Document findings using the Incident Report Template covering metrics, timeline, security analysis, root cause, and recommendations.

Tips
Ask for time range first using AskUserQuestion if not provided
Identify JA4 dynamically — query Cloudflare, don't assume
Only ask the user about unknown/suspicious User-Agents — skip well-known bots and clearly internal services
Calculate actual req/sec to understand service load
Document findings immediately using the incident template
Reference Files
Steps
Get parameters
Confirm spike
Minute-level detail
Identify culprit JA4
Analyze traffic
Verify legitimacy 6b. Check WAF & page rules
Extract top users
Synthesize & report
References
Cloudflare API CLI
Security Scores
Failure Patterns
Incident Report Template
Weekly Installs
31
Repository
delexw/claude-code-misc
GitHub Stars
1
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn