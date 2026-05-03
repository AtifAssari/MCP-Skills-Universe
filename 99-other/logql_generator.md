---
title: logql-generator
url: https://skills.sh/akin-ozer/cc-devops-skills/logql-generator
---

# logql-generator

skills/akin-ozer/cc-devops-skills/logql-generator
logql-generator
Installation
$ npx skills add https://github.com/akin-ozer/cc-devops-skills --skill logql-generator
SKILL.md
LogQL Query Generator
Overview

Interactive workflow for generating production-ready LogQL queries. LogQL is Grafana Loki's query language with indexed label selection, line filtering, parsing, and metric aggregation.

Trigger Hints
"Write a LogQL query for error rate by service."
"Help me build a Loki alert query."
"Convert this troubleshooting requirement into LogQL."
"I need step-by-step LogQL query construction."

Use this skill for query generation, dashboard queries, alerting expressions, and troubleshooting with Loki logs.

Execution Flow (Deterministic)

Always run stages in order. Do not skip required stages.

Stage 1 (Required): Capture Intent

Use AskUserQuestion to collect goal and use case.

Template:

"What is your primary goal: debugging, alerting, dashboard metric, or investigation?"
"Do you need a log query (raw lines) or a metric query (numeric output)?"
"What time window should this cover (example: last 15m, 1h, 24h)?"

Fallback if AskUserQuestion is unavailable:

Ask the same questions in plain text and continue.
Stage 2 (Required): Capture Log Source Details

Collect:

Labels for stream selectors (job, namespace, app, service_name, cluster)
Log format (JSON, logfmt, plain text, mixed)
Known fields to filter/aggregate (status, level, duration, path, trace_id)

Ambiguity and partial-answer handling:

If a required field is missing, ask one focused follow-up question.
If still missing, proceed with explicit assumptions.
Prefix assumptions with Assumptions: in the output so the user can correct them quickly.
Stage 3 (Required): Discover Loki and Grafana Versions

Collect or infer:

Loki version (example: 2.9.x, 3.0+, unknown)
Grafana version (example: 10.x, 11.x, unknown)
Deployment context (self-hosted Loki, Grafana Cloud, unknown)

Version compatibility policy:

If versions are known, use the newest compatible syntax only.
If versions are unknown, use compatibility-first syntax and avoid 3.x-only features by default.
For unknown versions, provide an optional "3.x optimized variant" separately.

Avoid by default when version is unknown:

Pattern match operators |> and !>
approx_topk
Structured metadata specific behavior (detected_level, accelerated metadata filtering assumptions)
Stage 4 (Required): Plan Confirmation and Output Mode

Present a plain-English plan, then ask the user to choose output mode.

Plan template:

LogQL Query Plan
Goal: <goal>
Query type: <log or metric>
Streams: <selector>
Filters/parsing: <filters + parser>
Aggregation window: <function and [range]>
Compatibility mode: <version-aware or compatibility-first>


Mode selection template:

"Do you want final query only (default) or incremental build (step-by-step)?"

If user does not choose, default to final query only.

Stage 5 (Conditional, Blocking): Reference Checkpoint for Complex Queries

Complex query triggers:

Nested aggregations (topk(sum by(...)), multiple sum by, percentiles)
Performance-sensitive queries (high volume streams, long ranges)
Alerting expressions
Template functions (line_format, label_format)
Regex-heavy extraction, IP matching, pattern parsing
Loki 3.x feature usage

Blocking checkpoint rule:

Read relevant files before generation using explicit file-open/read actions.
Minimum file set:
examples/common_queries.logql for syntax and query patterns
references/best_practices.md for performance and alerting guidance
Do not generate the final query until this checkpoint is complete.

Fallback when file-read tools are unavailable:

State that reference files could not be read in this environment.
Generate a conservative query (compatibility-first, simpler operators).
Mark result as Unverified against local references.
Stage 6 (Conditional): External Docs Lookup Policy (Context7 Before WebSearch)

Use external lookup only for version-specific behavior, unclear syntax, or advanced features not covered in local references.

Decision order:

Context7 first:
mcp__context7__resolve-library-id with libraryName="grafana loki"
mcp__context7__query-docs for the exact topic
WebSearch second (fallback only) when:
Context7 is unavailable
Context7 does not provide required version-specific detail
You need latest release/deprecation confirmation

WebSearch fallback constraints:

Prefer official Grafana/Loki docs and release notes.
Note which statement came from fallback search.
Stage 7 (Required): Generate Query
Stage 7A (Default): Final Query Only

Return one production-ready query plus short explanation.

Stage 7B (Optional): Incremental Build Mode

Use this when requested or when debugging complex pipelines.

Step-by-step template:

Stream selector
Line filter
Parser
Parsed-field filter
Aggregation/window
Stage 8 (Required): Deliver Usage and Checks

Always include:

Final query or incremental sequence
How to run it (Grafana Explore/panel or logcli)
Tunables (labels, thresholds, range)
Any assumptions and compatibility notes
AskUserQuestion Templates
Intake Template
"What system/service should this query target?"
"Which labels are reliable for stream selection?"
"What defines a match (error text, status code, latency threshold, user path)?"
"Should output be raw logs or a metric for alert/dashboard?"
Version Template
"What Loki version are you running?"
"What Grafana version are you using?"
"If unknown, should I generate a compatibility-first query and add an optional 3.x variant?"
Ambiguity Follow-up Template
"I am missing <field>. Should I assume <default> so I can continue?"
Core Patterns
Stream Selection and Filtering
{job="app"} |= "error" |= "timeout"
{job="app"} |~ "error|fatal|critical"
{job="app"} != "debug"

Parsing
{app="api"} | json | level="error" | status_code >= 500
{app="api"} | logfmt | caller="database.go"
{job="nginx"} | pattern "<ip> - - [<_>] \"<method> <path>\" <status> <size>"

Metric Aggregation
rate({job="app"} | json | level="error" [5m])
sum by (app) (count_over_time({namespace="prod"} | json [5m]))
sum(rate({app="api"} | json | level="error" [5m])) / sum(rate({app="api"}[5m])) * 100
quantile_over_time(0.95, {app="api"} | json | unwrap duration [5m])
topk(10, sum by (error_type) (count_over_time({job="app"} | json | level="error" [1h])))

Formatting and IP Matching
{job="app"} | json | line_format "{{.level}}: {{.message}}"
{job="app"} | json | label_format env=`{{.environment}}`
{job="nginx"} | logfmt | remote_addr = ip("192.168.4.0/24")

Query Construction Rules
Use specific stream selectors (indexed labels first).
Prefer filter order: line filter -> parse -> parsed-field filter.
Prefer parser cost order: pattern > logfmt > json > regexp.
For unknown Loki version, stay on compatibility-first syntax.
For complex/critical queries, complete Stage 5 checkpoint before final output.
Advanced Techniques
Multiple Parsers
{app="api"} | json | regexp "user_(?P<user_id>\\d+)"

Unwrap for Numeric Metrics
sum(sum_over_time({app="api"} | json | unwrap duration [5m]))

Pattern Match Operators (Loki 3.0+, 10x faster than regex)
{service_name=`app`} |> "<_> level=debug <_>"

Logical Operators
{app="api"} | json | (status_code >= 400 and status_code < 500) or level="error"

Offset Modifier
sum(rate({app="api"} | json | level="error" [5m])) - sum(rate({app="api"} | json | level="error" [5m] offset 1d))

Label Operations
{app="api"} | json | keep namespace, pod, level
{app="api"} | json | drop pod, instance


Note: LogQL has no dedup or distinct operators. Use metric aggregations like sum by (field) for programmatic deduplication.

Loki 3.x Key Features
Structured Metadata

High-cardinality data without indexing (trace_id, user_id, request_id):

# Filter AFTER stream selector, NOT in it
{app="api"} | trace_id="abc123" | json | level="error"

Query Acceleration (Bloom Filters)

Place structured metadata filters BEFORE parsers:

# ACCELERATED
{cluster="prod"} | detected_level="error" | logfmt | json
# NOT ACCELERATED
{cluster="prod"} | logfmt | json | detected_level="error"

approx_topk (Probabilistic)
approx_topk(10, sum by (endpoint) (rate({app="api"}[5m])))

vector() for Alerting
sum(count_over_time({app="api"} | json | level="error" [5m])) or vector(0)

Automatic Labels
service_name: Auto-populated from container name
detected_level: Auto-detected when discover_log_levels: true (stored as structured metadata)
Function Reference
Log Range Aggregations
Function	Description
rate(log-range)	Entries per second
count_over_time(log-range)	Count entries
bytes_rate(log-range)	Bytes per second
bytes_over_time(log-range)	Total bytes in time range
absent_over_time(log-range)	Returns 1 if no logs

Rule:

Use bytes_over_time(<log-range>) for raw log-byte volume.
Use | unwrap bytes(field) with unwrapped range aggregations for numeric byte fields extracted from log content.
Unwrapped Range Aggregations
Function	Description
sum_over_time, avg_over_time, max_over_time, min_over_time	Aggregate numeric values
quantile_over_time(φ, range)	φ-quantile (0 ≤ φ ≤ 1)
first_over_time, last_over_time	First/last value in interval
stddev_over_time	Population standard deviation of unwrapped values
stdvar_over_time	Population variance of unwrapped values
rate_counter	Per-second rate treating values as a monotonically increasing counter
Aggregation Operators

sum, avg, min, max, count, stddev, topk, bottomk, approx_topk, sort, sort_desc

With grouping: sum by (label1, label2) or sum without (label1)

Conversion Functions
Function	Description
duration_seconds(label)	Convert duration string
bytes(label)	Convert byte string (KB, MB)
label_replace()
label_replace(rate({job="api"} |= "err" [1m]), "foo", "$1", "service", "(.*):.*")

Parser Reference
logfmt
| logfmt [--strict] [--keep-empty]

--strict: Error on malformed entries
--keep-empty: Keep standalone keys
JSON
| json                                           # All fields
| json method="request.method", status="response.status"  # Specific fields
| json servers[0], headers="request.headers[\"User-Agent\"]"  # Nested/array

pattern
| pattern "<ip> - - [<timestamp>] \"<method> <path> <_>\" <status> <size>"


Named placeholders become extracted labels; <_> discards a field.

regexp
| regexp "(?P<level>\\w+): (?P<message>.+)"


Uses named capture groups (?P<name>). Slower than pattern/logfmt/json.

decolorize
| decolorize


Strips ANSI color escape codes. Apply before parsing when logs come from terminal output.

unpack
| unpack


Unpacks log entries that were packed by Promtail's pack pipeline stage. Restores the original log line and any embedded labels.

Template Functions

Common functions for line_format and label_format:

String: trim, upper, lower, replace, trunc, substr, printf, contains, hasPrefix Math: add, sub, mul, div, addf, subf, floor, ceil, round Date: date, now, unixEpoch, toDate, duration_seconds Regex: regexReplaceAll, count Other: fromJson, default, int, float64, __line__, __timestamp__

See examples/common_queries.logql for detailed usage.

Alerting Rules
# Alert when error rate exceeds 5%
(sum(rate({app="api"} | json | level="error" [5m])) / sum(rate({app="api"}[5m]))) > 0.05

# With vector() to avoid "no data"
sum(rate({app="api"} | json | level="error" [5m])) or vector(0) > 10

Error Handling
Issue	Solution
No results	Check labels exist, verify time range, test stream selector alone
Query slow	Use specific selectors, filter before parsing, reduce time range
Parse errors	Verify log format matches parser, test JSON validity
High cardinality	Use line filters not label filters for unique values, aggregate
Documentation Lookup

Use Stage 6 policy. Trigger external docs for:

Trigger	Topic to Search	Tool to Use
User mentions Loki 3.x features	structured metadata, bloom filters, detected_level	Context7 first
approx_topk function needed	approx_topk probabilistic	Context7 first
Pattern match operators (|>, !>)	pattern match operator	Context7 first
vector() function for alerting	vector function alerting	Context7 first
Recording rules configuration	recording rules loki	Context7 first
Unclear syntax or edge cases	Specific function/operator	Context7 first
Version-specific behavior questions	Version + feature	WebSearch fallback
Grafana Alloy integration	grafana alloy loki	WebSearch fallback
Resources
examples/common_queries.logql: Query patterns, template function examples
references/best_practices.md: Optimization, anti-patterns, alerting guidance
Example Flows
Example A: Final Query Only (Default)
User asks for 5xx rate by service over 15m.
Capture labels and format (json).
Confirm version and mode (final query only).
Generate one query:
sum by (service) (rate({namespace="prod", app="api"} | json | status_code >= 500 [15m]))

Example B: Incremental Build (Optional)
User asks to debug login failures and requests step-by-step mode.
Provide staged build:
{app="auth"}
{app="auth"} |= "login failed"
{app="auth"} |= "login failed" | json
sum(count_over_time({app="auth"} |= "login failed" | json [5m]))

Explain where to stop if any step returns zero results.
Done Criteria

Mark task done only when all checks pass:

Required stages (1, 2, 3, 4, 7, 8) were completed.
Stage 5 checkpoint was completed for any complex query.
Stage 6 lookup order followed Context7 before WebSearch when external docs were needed.
Output mode was explicitly selected or defaulted (final query only).
Loki/Grafana compatibility assumptions were stated when versions were unknown.
Final output includes query text, usage note, tunables, and assumptions.
Version Notes
Loki 3.0+: Bloom filters, structured metadata, pattern match operators (|>, !>)
Loki 3.3+: approx_topk function
Loki 3.5+: Promtail deprecated (use Grafana Alloy)
Loki 3.6+: Horizontally scalable compactor, Loki UI as Grafana plugin

Deprecations: Promtail (use Alloy), BoltDB store (use TSDB with v13 schema)

Weekly Installs
141
Repository
akin-ozer/cc-de…s-skills
GitHub Stars
200
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn