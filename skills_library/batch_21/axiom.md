---
title: axiom
url: https://skills.sh/vm0-ai/vm0-skills/axiom
---

# axiom

skills/vm0-ai/vm0-skills/axiom
axiom
Installation
$ npx skills add https://github.com/vm0-ai/vm0-skills --skill axiom
SKILL.md
Troubleshooting

If requests fail, run zero doctor check-connector --env-name AXIOM_TOKEN or zero doctor check-connector --url https://api.axiom.co/v2/datasets --method GET

Datasets
List Datasets
curl -s "https://api.axiom.co/v2/datasets" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Get Dataset
curl -s "https://api.axiom.co/v2/datasets/<dataset-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Create Dataset
curl -s -X POST "https://api.axiom.co/v2/datasets" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"my-logs\", \"description\": \"Application logs\"}"

Update Dataset
curl -s -X PUT "https://api.axiom.co/v2/datasets/<dataset-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"description\": \"Updated description\"}"

Delete Dataset
curl -s -X DELETE "https://api.axiom.co/v2/datasets/<dataset-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Trim Dataset

Remove data older than a specified duration.

curl -s -X POST "https://api.axiom.co/v2/datasets/<dataset-id>/trim" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"maxDuration\": \"30d\"}"

Get Dataset Fields
curl -s "https://api.axiom.co/v2/datasets/<dataset-id>/fields" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Get Field Info
curl -s "https://api.axiom.co/v2/datasets/<dataset-id>/fields/<field-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Update Field
curl -s -X PUT "https://api.axiom.co/v2/datasets/<dataset-id>/fields/<field-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"description\": \"Response time in ms\", \"unit\": \"ms\"}"

Ingest
Ingest JSON
curl -s -X POST "https://us-east-1.aws.edge.axiom.co/v1/datasets/<dataset-name>/ingest" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "[{\"message\": \"User logged in\", \"user_id\": \"123\", \"level\": \"info\"}]"

Ingest NDJSON
curl -s -X POST "https://us-east-1.aws.edge.axiom.co/v1/datasets/<dataset-name>/ingest" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/x-ndjson" \
  --data-binary @events.ndjson


Tip: Batch multiple events in a single request for better performance. Events without _time field will use server receive time.

Queries (APL)

APL (Axiom Processing Language) is similar to Kusto Query Language (KQL).

Run APL Query
curl -s -X POST "https://api.axiom.co/v1/datasets/_apl?format=tabular" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"apl\": \"['my-logs'] | where level == 'error' | limit 10\", \"startTime\": \"2026-01-01T00:00:00Z\", \"endTime\": \"2026-12-31T23:59:59Z\"}"

Query with Aggregation
curl -s -X POST "https://api.axiom.co/v1/datasets/_apl?format=tabular" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"apl\": \"['my-logs'] | summarize count() by level\", \"startTime\": \"2026-01-01T00:00:00Z\", \"endTime\": \"2026-12-31T23:59:59Z\"}"

APL Examples
Query	Description
['dataset'] | limit 10	Get first 10 events
['dataset'] | where level == "error"	Filter by field value
['dataset'] | where message contains "timeout"	Search in text
['dataset'] | summarize count() by level	Count by group
['dataset'] | summarize avg(duration_ms) by bin(_time, 1h)	Hourly average
['dataset'] | sort by _time desc | limit 100	Latest 100 events
['dataset'] | where _time > ago(1h)	Events in last hour
Monitors
List Monitors
curl -s "https://api.axiom.co/v2/monitors" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Get Monitor
curl -s "https://api.axiom.co/v2/monitors/<monitor-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Get Monitor History
curl -s "https://api.axiom.co/v2/monitors/<monitor-id>/history" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Create Monitor
curl -s -X POST "https://api.axiom.co/v2/monitors" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"High Error Rate\", \"aplQuery\": \"['my-logs'] | where level == 'error' | summarize count()\", \"threshold\": 100, \"comparison\": \"Above\", \"frequency\": \"5m\", \"range\": \"5m\", \"notifierIds\": [\"<notifier-id>\"]}"

Update Monitor
curl -s -X PUT "https://api.axiom.co/v2/monitors/<monitor-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"High Error Rate v2\", \"threshold\": 50}"

Delete Monitor
curl -s -X DELETE "https://api.axiom.co/v2/monitors/<monitor-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Notifiers
List Notifiers
curl -s "https://api.axiom.co/v2/notifiers" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Get Notifier
curl -s "https://api.axiom.co/v2/notifiers/<notifier-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Create Notifier
curl -s -X POST "https://api.axiom.co/v2/notifiers" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"Slack Alerts\", \"type\": \"slack\", \"properties\": {\"slackUrl\": \"https://hooks.slack.com/services/xxx\"}}"


Types: slack, email, pagerduty, webhook, opsgenie, discord, msteams.

Update Notifier
curl -s -X PUT "https://api.axiom.co/v2/notifiers/<notifier-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"Slack Alerts v2\"}"

Delete Notifier
curl -s -X DELETE "https://api.axiom.co/v2/notifiers/<notifier-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Annotations
List Annotations
curl -s "https://api.axiom.co/v2/annotations" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Get Annotation
curl -s "https://api.axiom.co/v2/annotations/<annotation-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Create Annotation
curl -s -X POST "https://api.axiom.co/v2/annotations" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"datasets\": [\"my-logs\"], \"type\": \"deployment\", \"title\": \"v1.2.0 deployed\", \"time\": \"2026-04-08T10:00:00Z\"}"

Update Annotation
curl -s -X PUT "https://api.axiom.co/v2/annotations/<annotation-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"title\": \"v1.2.0 deployed (hotfix)\"}"

Delete Annotation
curl -s -X DELETE "https://api.axiom.co/v2/annotations/<annotation-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Dashboards
List Dashboards
curl -s "https://api.axiom.co/v2/dashboards" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Get Dashboard
curl -s "https://api.axiom.co/v2/dashboards/uid/<dashboard-uid>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Create Dashboard
curl -s -X POST "https://api.axiom.co/v2/dashboards" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"API Overview\", \"description\": \"Key API metrics\"}"

Update Dashboard
curl -s -X PUT "https://api.axiom.co/v2/dashboards/uid/<dashboard-uid>" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"API Overview v2\"}"

Delete Dashboard
curl -s -X DELETE "https://api.axiom.co/v2/dashboards/uid/<dashboard-uid>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Starred Queries
List Starred Queries
curl -s "https://api.axiom.co/v2/apl-starred-queries" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Create Starred Query
curl -s -X POST "https://api.axiom.co/v2/apl-starred-queries" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"Error count by service\", \"query\": \"['my-logs'] | where level == 'error' | summarize count() by service\"}"

Update Starred Query
curl -s -X PUT "https://api.axiom.co/v2/apl-starred-queries/<id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"Error count by service (updated)\"}"

Delete Starred Query
curl -s -X DELETE "https://api.axiom.co/v2/apl-starred-queries/<id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Virtual Fields
List Virtual Fields
curl -s "https://api.axiom.co/v2/vfields" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Create Virtual Field
curl -s -X POST "https://api.axiom.co/v2/vfields" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"is_slow\", \"dataset\": \"my-logs\", \"expression\": \"duration_ms > 1000\"}"

Update Virtual Field
curl -s -X PUT "https://api.axiom.co/v2/vfields/<id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"expression\": \"duration_ms > 2000\"}"

Delete Virtual Field
curl -s -X DELETE "https://api.axiom.co/v2/vfields/<id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Views (Saved Views)
List Views
curl -s "https://api.axiom.co/v2/views" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Create View
curl -s -X POST "https://api.axiom.co/v2/views" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"Error Logs\", \"dataset\": \"my-logs\", \"query\": \"['my-logs'] | where level == 'error'\"}"

Update View
curl -s -X PUT "https://api.axiom.co/v2/views/<id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"Critical Errors\"}"

Delete View
curl -s -X DELETE "https://api.axiom.co/v2/views/<id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Organization & Users
Get Organization
curl -s "https://api.axiom.co/v2/orgs" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Get Current User
curl -s "https://api.axiom.co/v2/user" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

List Users
curl -s "https://api.axiom.co/v2/users" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Get User
curl -s "https://api.axiom.co/v2/users/<user-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

API Tokens
List Tokens
curl -s "https://api.axiom.co/v2/tokens" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Create Token
curl -s -X POST "https://api.axiom.co/v2/tokens" \
  --header "Authorization: Bearer $AXIOM_TOKEN" \
  --header "Content-Type: application/json" \
  -d "{\"name\": \"CI Pipeline\", \"description\": \"Token for CI/CD\"}"

Regenerate Token
curl -s -X POST "https://api.axiom.co/v2/tokens/<token-id>/regenerate" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Delete Token
curl -s -X DELETE "https://api.axiom.co/v2/tokens/<token-id>" \
  --header "Authorization: Bearer $AXIOM_TOKEN"

Guidelines
Use Edge URLs for Ingest: Always use the edge endpoint (us-east-1.aws.edge.axiom.co or eu-central-1.aws.edge.axiom.co) for data ingestion, not api.axiom.co.
Batch Events: Send multiple events in a single request for better performance.
Include Timestamps: Events without _time field will use server receive time.
Rate Limits: Check X-RateLimit-Remaining header to avoid hitting limits.
APL Time Range: Always specify startTime and endTime for queries to improve performance.
Data Formats: JSON array is recommended for ingest; NDJSON and CSV are also supported.
Dataset Names: In APL queries, use ['dataset-name'] syntax (square brackets + quotes) for dataset names.
Monitors + Notifiers: Monitors define alert conditions (APL query + threshold); notifiers define delivery channels (Slack, email, PagerDuty, etc.). Link them via notifierIds.
How to Look Up More API Details
REST API Intro: https://axiom.co/docs/restapi/introduction
Datasets: https://axiom.co/docs/restapi/datasets
Ingest: https://axiom.co/docs/restapi/ingest
Query (APL): https://axiom.co/docs/restapi/query
APL Reference: https://axiom.co/docs/apl/introduction
Monitors: https://axiom.co/docs/restapi/monitors
Annotations: https://axiom.co/docs/restapi/annotations
Dashboards: https://axiom.co/docs/restapi/dashboards
Weekly Installs
62
Repository
vm0-ai/vm0-skills
GitHub Stars
57
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass