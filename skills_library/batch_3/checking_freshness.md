---
title: checking-freshness
url: https://skills.sh/astronomer/agents/checking-freshness
---

# checking-freshness

skills/astronomer/agents/checking-freshness
checking-freshness
Installation
$ npx skills add https://github.com/astronomer/agents --skill checking-freshness
Summary

Verify data freshness by checking table timestamps and update patterns against a staleness scale.

Identifies timestamp columns using common ETL naming patterns (_loaded_at, _updated_at, created_at, etc.) and queries their maximum values to determine age
Classifies data into four freshness statuses: Fresh (< 4 hours), Stale (4–24 hours), Very Stale (> 24 hours), or Unknown (no timestamp found)
Provides SQL templates for checking last update time and row count trends over recent days to spot update gaps
Integrates with Airflow to diagnose stale data by checking DAG status, run history, and SLA misses; links to the debugging-dags skill for failed pipeline investigation
Supports both quick yes/no answers and detailed freshness reports with actionable next steps
SKILL.md
Data Freshness Check

Quickly determine if data is fresh enough to use.

Freshness Check Process

For each table to check:

1. Find the Timestamp Column

Look for columns that indicate when data was loaded or updated:

_loaded_at, _updated_at, _created_at (common ETL patterns)
updated_at, created_at, modified_at (application timestamps)
load_date, etl_timestamp, ingestion_time
date, event_date, transaction_date (business dates)

Query INFORMATION_SCHEMA.COLUMNS if you need to see column names.

2. Query Last Update Time
SELECT
    MAX(<timestamp_column>) as last_update,
    CURRENT_TIMESTAMP() as current_time,
    TIMESTAMPDIFF('hour', MAX(<timestamp_column>), CURRENT_TIMESTAMP()) as hours_ago,
    TIMESTAMPDIFF('minute', MAX(<timestamp_column>), CURRENT_TIMESTAMP()) as minutes_ago
FROM <table>

3. Check Row Counts by Time

For tables with regular updates, check recent activity:

SELECT
    DATE_TRUNC('day', <timestamp_column>) as day,
    COUNT(*) as row_count
FROM <table>
WHERE <timestamp_column> >= DATEADD('day', -7, CURRENT_DATE())
GROUP BY 1
ORDER BY 1 DESC

Freshness Status

Report status using this scale:

Status	Age	Meaning
Fresh	< 4 hours	Data is current
Stale	4-24 hours	May be outdated, check if expected
Very Stale	> 24 hours	Likely a problem unless batch job
Unknown	No timestamp	Can't determine freshness
If Data is Stale

Check Airflow for the source pipeline:

Find the DAG: Which DAG populates this table? Use af dags list and look for matching names.

Check DAG status:

Is the DAG paused? Use af dags get <dag_id>
Did the last run fail? Use af dags stats
Is a run currently in progress?

Diagnose if needed: If the DAG failed, use the debugging-dags skill to investigate.

On Astro

If you're running on Astro, you can also:

DAG history in the Astro UI: Check the deployment's DAG run history for a visual timeline of recent runs and their outcomes
Astro alerts for SLA monitoring: Configure alerts to get notified when DAGs miss their expected completion windows, catching staleness before users report it
On OSS Airflow
Airflow UI: Use the DAGs view and task logs to verify last successful runs and SLA misses
Output Format

Provide a clear, scannable report:

FRESHNESS REPORT
================

TABLE: database.schema.table_name
Last Update: 2024-01-15 14:32:00 UTC
Age: 2 hours 15 minutes
Status: Fresh

TABLE: database.schema.other_table
Last Update: 2024-01-14 03:00:00 UTC
Age: 37 hours
Status: Very Stale
Source DAG: daily_etl_pipeline (FAILED)
Action: Investigate with **debugging-dags** skill

Quick Checks

If user just wants a yes/no answer:

"Is X fresh?" -> Check and respond with status + one line
"Can I use X for my 9am meeting?" -> Check and give clear yes/no with context
Weekly Installs
612
Repository
astronomer/agents
GitHub Stars
354
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass