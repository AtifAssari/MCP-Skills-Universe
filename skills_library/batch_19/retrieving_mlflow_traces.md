---
title: retrieving-mlflow-traces
url: https://skills.sh/mlflow/skills/retrieving-mlflow-traces
---

# retrieving-mlflow-traces

skills/mlflow/skills/retrieving-mlflow-traces
retrieving-mlflow-traces
Installation
$ npx skills add https://github.com/mlflow/skills --skill retrieving-mlflow-traces
SKILL.md
Retrieving MLflow Traces
Single Fetch vs Search

Choose the right approach based on what you have:

You have...	Use	Command
Trace ID	Single fetch	mlflow traces get --trace-id <id>
Session/user/filters	Search	mlflow traces search --experiment-id <id> --filter-string "..."

Single fetch - Use when you have a specific trace ID (e.g., from UI, logs, or API response):

mlflow traces get --trace-id tr-69f72a3772570019f2f91b75b8b5ded9


Search - Use when you need to find traces by criteria (session, user, status, time range, etc.):

mlflow traces search --experiment-id 1 --filter-string "metadata.\`mlflow.trace.session\` = 'session_abc'"

Trace Data Structure
TraceInfo: trace_id, status (OK/ERROR), timestamp_ms, execution_time_ms, tags, metadata, assessments (human feedback, evaluation results)
Spans: Tree of operations with name, type, attributes, start_time, end_time
Workflow
Check CLI usage (required): mlflow traces search --help
Build filter query using syntax below
Execute search with appropriate flags
Retrieve details for specific traces if needed
Prerequisite: Check CLI Usage
mlflow traces search --help


Always run this first to get accurate flags for the installed MLflow version.

Searching Traces

The mlflow traces search command is used to search for traces in an MLflow experiment.

By Run ID

Filter traces associated with a specific MLflow run:

# All traces for a run
mlflow traces search --run-id <run_id>

# Failed traces for a run
mlflow traces search --run-id <run_id> --filter-string "trace.status = 'ERROR'"

# Can combine with experiment-id
mlflow traces search --experiment-id 1 --run-id <run_id>

By Session or User (Common for Debugging)

When debugging an issue from the MLflow UI, filter by session or user ID to get all related traces:

# All traces for a specific session (use backticks for special characters in key)
mlflow traces search --experiment-id 1 --filter-string "metadata.\`mlflow.trace.session\` = 'session_abc123'"

# All traces for a specific user
mlflow traces search --experiment-id 1 --filter-string "metadata.\`mlflow.trace.user\` = 'user_456'"

# Failed traces in a session (for root cause analysis)
mlflow traces search --experiment-id 1 --filter-string "metadata.\`mlflow.trace.session\` = 'session_abc123' AND trace.status = 'ERROR'"

# Session traces ordered by time (to see sequence of events)
mlflow traces search --experiment-id 1 --filter-string "metadata.\`mlflow.trace.session\` = 'session_abc123'" --order-by "timestamp_ms ASC"

By Status
mlflow traces search --experiment-id 1 --filter-string "trace.status = 'ERROR'"
mlflow traces search --experiment-id 1 --filter-string "trace.status = 'OK'"

By Time Range
# Timestamps are in milliseconds since epoch
# Get current time in ms: $(date +%s)000
# Last hour: $(( $(date +%s)000 - 3600000 ))

mlflow traces search --experiment-id 1 --filter-string "trace.timestamp_ms > $(( $(date +%s)000 - 3600000 ))"

By Execution Time (Slow Traces)
# Traces slower than 1 second
mlflow traces search --experiment-id 1 --filter-string "trace.execution_time_ms > 1000"

By Tags and Metadata
# By tag
mlflow traces search --experiment-id 1 --filter-string "tag.environment = 'production'"

# By metadata
mlflow traces search --experiment-id 1 --filter-string "metadata.user_id = 'user_123'"

# Escape special characters in key names with backticks
mlflow traces search --experiment-id 1 --filter-string "tag.\`model-name\` = 'gpt-4'"
mlflow traces search --experiment-id 1 --filter-string "metadata.\`user.id\` = 'abc'"

By Assessment/Feedback
mlflow traces search --experiment-id 1 --filter-string "feedback.rating = 'positive'"

Full Text Search
mlflow traces search --experiment-id 1 --filter-string "trace.text LIKE '%error%'"

Pagination

Control result count and iterate through pages:

# Limit results per page
mlflow traces search --experiment-id 1 --max-results 50

# Output includes "Next page token: <token>" if more results exist
# Use --page-token to fetch next page
mlflow traces search --experiment-id 1 --max-results 50 --page-token "eyJvZmZzZXQiOiA1MH0="

Output Options
# Output format (table or json)
mlflow traces search --experiment-id 1 --output json

# Include span details in output
mlflow traces search --experiment-id 1 --include-spans

# Order results
mlflow traces search --experiment-id 1 --order-by "timestamp_ms DESC"

Retrieving Single Trace

When you need to retrieve details about a specific trace, use the mlflow traces get command.

mlflow traces get --trace-id <trace_id>

Filter Syntax

For detailed syntax, fetch from documentation:

WebFetch(
  url: "https://mlflow.org/docs/latest/genai/tracing/search-traces.md",
  prompt: "Extract the filter syntax table showing supported fields, operators, and examples."
)


Common filters:

trace.status: OK, ERROR, IN_PROGRESS
trace.execution_time_ms, trace.timestamp_ms: numeric comparison
metadata.\mlflow.trace.session`, metadata.`mlflow.trace.user``: session/user filtering
tag.<key>, metadata.<key>: exact match or pattern
span.name, span.type: exact match or pattern
feedback.<name>, expectation.<name>: assessments

Pattern operators: LIKE, ILIKE (case-insensitive), RLIKE (regex)

Python API

For mlflow.search_traces(), see: https://mlflow.org/docs/latest/genai/tracing/search-traces.md

Weekly Installs
199
Repository
mlflow/skills
GitHub Stars
36
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn