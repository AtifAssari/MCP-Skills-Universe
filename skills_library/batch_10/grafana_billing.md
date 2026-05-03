---
title: grafana-billing
url: https://skills.sh/nodnarbnitram/claude-code-extensions/grafana-billing
---

# grafana-billing

skills/nodnarbnitram/claude-code-extensions/grafana-billing
grafana-billing
Installation
$ npx skills add https://github.com/nodnarbnitram/claude-code-extensions --skill grafana-billing
SKILL.md
Grafana Billing Metrics Skill

Query key billing metrics from Prometheus and Loki through Grafana's data source proxy API.

Quick Start
# Query both staging and prod (default)
uv run .claude/skills/grafana-billing/scripts/billing_metrics.py

# Query specific environment
uv run .claude/skills/grafana-billing/scripts/billing_metrics.py --env staging
uv run .claude/skills/grafana-billing/scripts/billing_metrics.py --env prod

# JSON output for automation
uv run .claude/skills/grafana-billing/scripts/billing_metrics.py --json

# Filter to specific service
uv run .claude/skills/grafana-billing/scripts/billing_metrics.py --service prometheus
uv run .claude/skills/grafana-billing/scripts/billing_metrics.py --service loki

Environment Variables Required
GRAFANA_STAGING_API_KEY - API key for staging Grafana workspace
GRAFANA_PROD_API_KEY - API key for prod Grafana workspace
Key Metrics Captured
Prometheus
Metric	Description
Active Time Series	Current count of active series (billing dimension)
Samples/sec	Ingestion rate (DPM = samples/sec * 60)
TSDB Storage	On-disk storage bytes
Top Cardinality	Top 10 metrics by series count
Loki
Metric	Description
Ingestion Rate	GB/day being ingested
Total Bytes	Cumulative bytes received
Active Streams	Number of active log streams
Memory Chunks	Chunks held in memory
When to Use

Use this skill when the user asks about:

Observability billing or costs
Active time series counts
Prometheus cardinality analysis
Loki ingestion rates
Storage usage for metrics or logs
Comparing staging vs production usage
Instructions for Claude
Run the billing metrics script to gather current data
Present the results in a clear, formatted way
Highlight any concerning metrics (high cardinality, rapid growth)
Compare staging vs prod if both are queried
Suggest cost optimization if metrics are unusually high
Critical Rules
Always check that API keys are set before running
Use --json flag when you need to process the output programmatically
Default to querying both environments for comparison
Handle errors gracefully - missing data sources should not crash the script
Weekly Installs
48
Repository
nodnarbnitram/c…tensions
GitHub Stars
8
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass