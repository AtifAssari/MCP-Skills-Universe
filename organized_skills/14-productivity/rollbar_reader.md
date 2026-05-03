---
rating: ⭐⭐⭐
title: rollbar-reader
url: https://skills.sh/delexw/claude-code-misc/rollbar-reader
---

# rollbar-reader

skills/delexw/claude-code-misc/rollbar-reader
rollbar-reader
Installation
$ npx skills add https://github.com/delexw/claude-code-misc --skill rollbar-reader
SKILL.md
Rollbar Reader

Investigate and analyse Rollbar error tracking data using the rollbar CLI (https://github.com/delexw/rollbar-cli).

Inputs

Raw arguments: $ARGUMENTS

Infer from the arguments:

QUERY: what to investigate. Defaults to last 24 hours if no time range is mentioned.
SINCE: (optional) UTC ISO8601 start of analysis window. When provided, takes precedence over time derived from QUERY. Convert to epoch seconds for time-based CLI flags: date -d "<SINCE>" +%s (Linux) or date -jf "%Y-%m-%dT%H:%M:%SZ" "<SINCE>" +%s (macOS).
UNTIL: (optional) UTC ISO8601 end of analysis window. When provided, takes precedence over time derived from QUERY. Convert to epoch seconds the same way.
TITLE_HINT: (optional) Incident title keywords to use in error item search queries (e.g. the PD incident title).
ENV: (optional) Environment to filter by (e.g. production, staging). Infer from QUERY context (e.g. "in production" → production, "staging issue" → staging). If not mentioned and cannot be inferred, omit the filter.
OUT_DIR: output directory for temp assets, or .rollbar-reader-tmp/ if not provided
TZ_DISPLAY: (optional) Timezone abbreviation for report display (e.g. the output of date +"%Z" on the calling machine). When provided, use this for all report timestamps instead of detecting via system clock.
System Requirements
rollbar CLI installed — npm install -g @delexw/rollbar-cli (see https://github.com/delexw/rollbar-cli)
A project access token configured via rollbar config set-token <project> <token> and rollbar config set-default <project>. Important: When checking configuration, verify at least 2 times before concluding it is not configured. Never expose token values — use existence checks only.
For account-level commands (teams, users, projects): account token configured via rollbar config set-account-token <token> (optional, only needed for account-level queries)
Output Directory

All intermediate JSON and the final report are saved to the output directory (default .rollbar-reader-tmp/):

.rollbar-reader-tmp/
├── items.json                  # Error items list
├── occurrences/
│   └── <ITEM_ID>.json          # Occurrences per item
├── deploys.json                # Deploy history
├── rql-results.json            # RQL query results (if used)
├── reports/
│   ├── top-active.json         # Top active items report
│   └── occurrence-counts.json  # Occurrence count data
└── report.md                   # Final analysis report

Execution
1. Verify Installation & Configuration

Check if the rollbar CLI is installed:

which rollbar


If not found, install it automatically: npm install -g @delexw/rollbar-cli. See references/setup-guide.md for full setup details.

If no projects are configured, guide the user through token setup using references/setup-guide.md. Never expose token values — use existence checks only.

Do NOT continue until both installation and configuration are verified.

2. Detect Local Timezone

If TZ_DISPLAY was not provided, run the following to get the local timezone from the current machine:

date +"%Z"


Record the output as the display timezone for all report timestamps.

3. Discover Configured Projects & Select Target

Always start by listing configured projects to know which projects are available:

rollbar config list


This returns all configured project names. Use this to:

Show the user which projects are available to query
Infer the correct --project flag from the user's request context (e.g. match keywords in the user's request to a project name from the list)
If only one project is configured, use it automatically
If multiple projects match the context, ask the user which one to query

The --project <name> global flag selects which project to query. It must match a name from rollbar config list. Examples:

# Query items for a specific project
rollbar --project my-project items list --status active

# Query occurrences for a specific project
rollbar --project my-project occurrences list


If the user does not specify a project and the default project (from rollbar config show) is appropriate, you can omit --project to use the default.

4. Prepare Output Directory

Create the output directory and subdirectories:

mkdir -p <OUT_DIR>/occurrences <OUT_DIR>/reports


Where <OUT_DIR> is OUT_DIR.

5. Investigate Using Items & Occurrences

Based on QUERY (which includes the time range), query Rollbar data. Use --format json for all commands to get structured output. Run commands sequentially.

rollbar items — Query Error Items (Readonly)

When ENV is set, pass --environment ENV to all items list calls to filter out noise from other environments.

# List all active items filtered by environment
rollbar items list --status active --environment <ENV>

# List active critical items for a specific project
rollbar --project my-app items list --status active --level critical --environment <ENV>

# List active errors (not warnings/info)
rollbar --project my-app items list --status active --level error --environment <ENV>

# List resolved items
rollbar --project my-app items list --status resolved --environment <ENV>

# Paginate through results
rollbar --project my-app items list --status active --environment <ENV> --page 2


Available --status values: active, resolved, muted, etc. Available --level values: critical, error, warning, info, debug.

Get a single item by ID, UUID, or project counter:

# Get item by numeric ID
rollbar items get --id 123456789

# Get item by UUID
rollbar items get --uuid "abcd1234-ef56-7890-abcd-ef1234567890"

# Get item by project counter (the "#123" number shown in Rollbar UI)
rollbar --project my-app items get --counter 123

rollbar occurrences — Query Occurrences (Readonly)

Use occurrences list-by-item to drill into a specific item obtained from items list --environment production. Since occurrences are already scoped to a production item, results will reflect production traffic.

# List occurrences for a specific item (item ID from items list)
rollbar --project my-app occurrences list-by-item <item_id>

# Paginate
rollbar --project my-app occurrences list-by-item <item_id> --page 2


Get a single occurrence by occurrence ID (for full stack trace, request data, etc.):

rollbar occurrences get <occurrence_id>

rollbar rql — Advanced Time-Windowed Queries

Use RQL when you need time-range filtering or aggregations. Include AND environment = 'ENV' in the WHERE clause when ENV is set. RQL jobs are async: create → poll until status: success → fetch results.

See references/rql-queries.md for the full CLI flow and query patterns.

Typical Investigation Workflow
List configured projects → rollbar config list
List active errors → rollbar --project <name> items list --status active --level error (add --environment <ENV> if ENV is set)
Pick a high-impact item → note the item ID and counter from the list
Get item detail → rollbar --project <name> items get --id <item_id>
List occurrences for that item → rollbar --project <name> occurrences list-by-item <item_id>
Get full occurrence detail → rollbar occurrences get <occurrence_id> (stack trace, request data)
Repeat for other high-priority items

Time range handling — when QUERY contains a named day ("today", "yesterday") or a calendar range, compute the window using local day boundaries, not UTC calendar days. A user saying "today" means since local midnight, so an event at 11am local is included even if it falls on a different UTC date.

For relative durations ("last 24h"), compute as now - N*3600 in epoch seconds. For named days, use the epoch helpers in references/rql-queries.md. Always include WHERE timestamp > SINCE_EPOCH AND timestamp < UNTIL_EPOCH in time-bounded queries, plus AND environment = 'ENV' when ENV is set.

Default: last 24 hours if no time range is mentioned in QUERY.

Save intermediate results as JSON to the output directory for reference.

6. Deep-Dive (if needed)

For error investigation, drill into specific items:

List active error/critical items (with --environment <ENV> if ENV is set)
For each high-priority item, fetch recent occurrences via occurrences list-by-item
Get the full occurrence detail for the most recent occurrence to understand the error context (stack trace, request data, etc.)
Check deploys around the time errors started to correlate with releases
7. Report

All timestamps in the report must use local timezone, not UTC. Format: 2026-03-20 15:30 <TZ> (with TZ abbreviation from date +"%Z"). Use TZ_DISPLAY if provided, otherwise detect via system clock (date +"%Z"). Do NOT use UTC in user-facing report sections — this includes timestamps that come directly from API responses (e.g. first_occurrence_timestamp, last_occurrence_timestamp, deploy times). Convert every timestamp to local time before writing it to the report.

Critical: When SINCE and UNTIL are provided as UTC ISO8601 (e.g. 2026-03-24T20:00:27Z), the report window header must also convert these boundaries to local time — do NOT copy the UTC hour values and relabel them as local timezone. Use date to convert:

# macOS — convert UTC ISO8601 to local display string
date -jf "%Y-%m-%dT%H:%M:%SZ" "2026-03-24T20:00:27Z" +"%Y-%m-%d %H:%M %Z"


Example: 2026-03-24T20:00:27Z converts to a different hour and possibly a different date in local time — do not copy the UTC hour value and relabel it.

Write a structured analysis to <OUT_DIR>/report.md using the Write tool:

Summary — Overall error health and key findings
Top Items — Highest impact error items with occurrence counts, levels, and first/last seen
Error Details — Breakdown of investigated items: stack traces, affected environments, occurrence patterns
Deploy Correlation — Recent deploys and any correlation with error spikes
Trends — Occurrence count trends over the time range
Recommendations — Suggested follow-up actions (items to resolve, investigate further, etc.)

Inform the user of the report location: <OUT_DIR>/report.md

Reference Files
Name	When to Read
references/setup-guide.md	Installation and configuration guide
references/rql-queries.md	RQL CLI flow, production-filtered query patterns, epoch helpers
Weekly Installs
25
Repository
delexw/claude-code-misc
GitHub Stars
1
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn