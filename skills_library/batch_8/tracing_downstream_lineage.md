---
title: tracing-downstream-lineage
url: https://skills.sh/astronomer/agents/tracing-downstream-lineage
---

# tracing-downstream-lineage

skills/astronomer/agents/tracing-downstream-lineage
tracing-downstream-lineage
Installation
$ npx skills add https://github.com/astronomer/agents --skill tracing-downstream-lineage
Summary

Trace downstream data lineage to assess change impact before modifying tables or DAGs.

Identifies direct consumers of a target table or DAG through source code search, view dependencies, and BI tool connections
Builds a full dependency tree mapping all downstream impacts, from tables to dashboards to ML models
Categorizes dependencies by criticality (critical, high, medium, low) to prioritize stakeholder communication and testing
Generates an impact report with risk assessment, affected owners, and recommended mitigation steps before deployment
SKILL.md
Downstream Lineage: Impacts

Answer the critical question: "What breaks if I change this?"

Use this BEFORE making changes to understand the blast radius.

Impact Analysis
Step 1: Identify Direct Consumers

Find everything that reads from this target:

For Tables:

Search DAG source code: Look for DAGs that SELECT from this table

Use af dags list to get all DAGs
Use af dags source <dag_id> to search for table references
Look for: FROM target_table, JOIN target_table

Check for dependent views:

-- Snowflake
SELECT * FROM information_schema.view_table_usage
WHERE table_name = '<target_table>'

-- Or check SHOW VIEWS and search definitions


Look for BI tool connections:

Dashboards often query tables directly
Check for common BI patterns in table naming (rpt_, dashboard_)
On Astro

If you're running on Astro, the Lineage tab in the Astro UI provides visual dependency graphs across DAGs and datasets, making downstream impact analysis faster. It shows which DAGs consume a given dataset and their current status, reducing the need for manual source code searches.

For DAGs:

Check what the DAG produces: Use af dags source <dag_id> to find output tables
Then trace those tables' consumers (recursive)
Step 2: Build Dependency Tree

Map the full downstream impact:

SOURCE: fct.orders
    |
    +-- TABLE: agg.daily_sales --> Dashboard: Executive KPIs
    |       |
    |       +-- TABLE: rpt.monthly_summary --> Email: Monthly Report
    |
    +-- TABLE: ml.order_features --> Model: Demand Forecasting
    |
    +-- DIRECT: Looker Dashboard "Sales Overview"

Step 3: Categorize by Criticality

Critical (breaks production):

Production dashboards
Customer-facing applications
Automated reports to executives
ML models in production
Regulatory/compliance reports

High (causes significant issues):

Internal operational dashboards
Analyst workflows
Data science experiments
Downstream ETL jobs

Medium (inconvenient):

Ad-hoc analysis tables
Development/staging copies
Historical archives

Low (minimal impact):

Deprecated tables
Unused datasets
Test data
Step 4: Assess Change Risk

For the proposed change, evaluate:

Schema Changes (adding/removing/renaming columns):

Which downstream queries will break?
Are there SELECT * patterns that will pick up new columns?
Which transformations reference the changing columns?

Data Changes (values, volumes, timing):

Will downstream aggregations still be valid?
Are there NULL handling assumptions that will break?
Will timing changes affect SLAs?

Deletion/Deprecation:

Full dependency tree must be migrated first
Communication needed for all stakeholders
Step 5: Find Stakeholders

Identify who owns downstream assets:

DAG owners: Check owners field in DAG definitions
Dashboard owners: Usually in BI tool metadata
Team ownership: Look for team naming patterns or documentation
Output: Impact Report
Summary

"Changing fct.orders will impact X tables, Y DAGs, and Z dashboards"

Impact Diagram
                    +--> [agg.daily_sales] --> [Executive Dashboard]
                    |
[fct.orders] -------+--> [rpt.order_details] --> [Ops Team Email]
                    |
                    +--> [ml.features] --> [Demand Model]

Detailed Impacts
Downstream	Type	Criticality	Owner	Notes
agg.daily_sales	Table	Critical	data-eng	Updated hourly
Executive Dashboard	Dashboard	Critical	analytics	CEO views daily
ml.order_features	Table	High	ml-team	Retraining weekly
Risk Assessment
Change Type	Risk Level	Mitigation
Add column	Low	No action needed
Rename column	High	Update 3 DAGs, 2 dashboards
Delete column	Critical	Full migration plan required
Change data type	Medium	Test downstream aggregations
Recommended Actions

Before making changes:

 Notify owners: @data-eng, @analytics, @ml-team
 Update downstream DAG: transform_daily_sales
 Test dashboard: Executive KPIs
 Schedule change during low-impact window
Related Skills
Trace where data comes from: tracing-upstream-lineage skill
Check downstream freshness: checking-freshness skill
Debug any broken DAGs: debugging-dags skill
Add manual lineage annotations: annotating-task-lineage skill
Build custom lineage extractors: creating-openlineage-extractors skill
Weekly Installs
625
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