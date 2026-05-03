---
title: querying-mlflow-metrics
url: https://skills.sh/mlflow/skills/querying-mlflow-metrics
---

# querying-mlflow-metrics

skills/mlflow/skills/querying-mlflow-metrics
querying-mlflow-metrics
Installation
$ npx skills add https://github.com/mlflow/skills --skill querying-mlflow-metrics
SKILL.md
MLflow Metrics

Run scripts/fetch_metrics.py to query metrics from an MLflow tracking server.

Examples

Token usage summary:

python scripts/fetch_metrics.py -s http://localhost:5000 -x 1 -m total_tokens -a SUM,AVG


Output: AVG: 223.91 SUM: 7613

Hourly token trend (last 24h):

python scripts/fetch_metrics.py -s http://localhost:5000 -x 1 -m total_tokens -a SUM \
    -t 3600 --start-time="-24h" --end-time=now


Output: Time-bucketed token sums per hour

Latency percentiles by trace:

python scripts/fetch_metrics.py -s http://localhost:5000 -x 1 -m latency -a AVG,P95 -d trace_name


Error rate by status:

python scripts/fetch_metrics.py -s http://localhost:5000 -x 1 -m trace_count -a COUNT -d trace_status


Quality scores by evaluator (assessments):

python scripts/fetch_metrics.py -s http://localhost:5000 -x 1 -v ASSESSMENTS \
    -m assessment_value -a AVG,P50 -d assessment_name


Output: Average and median scores for each evaluator (e.g., correctness, relevance)

Assessment count by name:

python scripts/fetch_metrics.py -s http://localhost:5000 -x 1 -v ASSESSMENTS \
    -m assessment_count -a COUNT -d assessment_name


JSON output: Add -o json to any command.

Arguments
Arg	Required	Description
-s, --server	Yes	MLflow server URL
-x, --experiment-ids	Yes	Experiment IDs (comma-separated)
-m, --metric	Yes	trace_count, latency, input_tokens, output_tokens, total_tokens
-a, --aggregations	Yes	COUNT, SUM, AVG, MIN, MAX, P50, P95, P99
-d, --dimensions	No	Group by: trace_name, trace_status
-t, --time-interval	No	Bucket size in seconds (3600=hourly, 86400=daily)
--start-time	No	-24h, -7d, now, ISO 8601, or epoch ms
--end-time	No	Same formats as start-time
-o, --output	No	table (default) or json

For SPANS metrics (span_count, latency), add -v SPANS. For ASSESSMENTS metrics, add -v ASSESSMENTS.

See references/api_reference.md for filter syntax and full API details.

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
SnykPass