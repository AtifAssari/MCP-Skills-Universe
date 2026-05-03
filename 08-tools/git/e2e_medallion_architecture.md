---
title: e2e-medallion-architecture
url: https://skills.sh/microsoft/skills-for-fabric/e2e-medallion-architecture
---

# e2e-medallion-architecture

skills/microsoft/skills-for-fabric/e2e-medallion-architecture
e2e-medallion-architecture
Installation
$ npx skills add https://github.com/microsoft/skills-for-fabric --skill e2e-medallion-architecture
SKILL.md

Update Check — ONCE PER SESSION (mandatory) The first time this skill is used in a session, run the check-updates skill before proceeding.

GitHub Copilot CLI / VS Code: invoke the check-updates skill.
Claude Code / Cowork / Cursor / Windsurf / Codex: compare local vs remote package.json version.
Skip if the check was already performed earlier in this session.

CRITICAL NOTES

To find the workspace details (including its ID) from workspace name: list all workspaces and, then, use JMESPath filtering
To find the item details (including its ID) from workspace ID, item type, and item name: list all items of that type in that workspace and, then, use JMESPath filtering
End-to-End Medallion Architecture
Prerequisite Knowledge

Read these companion documents — they contain the foundational context this skill depends on:

COMMON-CORE.md — Fabric REST API patterns, authentication, token audiences, item discovery
COMMON-CLI.md — az rest, az login, token acquisition, Fabric REST via CLI
SPARK-AUTHORING-CORE.md — Notebook deployment, lakehouse creation, job execution
notebook-api-operations.md — Required for notebook creation — .ipynb structure requirements, cell format, getDefinition/updateDefinition workflow

For Spark-specific optimization details, see data-engineering-patterns.md.

Architecture Overview

Medallion Architecture is a data lakehouse pattern with three progressive layers:

Layer	Purpose	Optimization Profile	Use Case
Bronze (Raw)	Land raw data exactly as received	Write-optimized, append-only, partitioned by ingestion date	Audit trail, reprocessing, lineage
Silver (Cleaned)	Deduplicated, validated, conformed data	Balanced read/write, partitioned by business date	Feature engineering, operational reporting
Gold (Aggregated)	Pre-calculated metrics for analytics	Read-optimized (ZORDER, compaction), partitioned by month/year	Power BI reports, dashboards, ad-hoc analytics via SQL endpoint
Bronze: Schema-on-read — flexible schema, Delta time travel supports audit and rollback
Silver: Schema enforcement — reject non-conforming writes; handle schema evolution with mergeSchema when sources change
Gold: Strict schema governance — curated, business-approved datasets only
Must/Prefer/Avoid
MUST DO
Create a separate lakehouse for each medallion layer (Bronze, Silver, Gold)
Add metadata columns in Bronze: ingestion timestamp, source file, batch ID
Apply data quality rules in the Bronze-to-Silver transformation (deduplication, null handling, range validation)
Use Delta Lake format for all medallion layer tables
Use partition-aware overwrite in Silver/Gold writes to avoid reprocessing unchanged data
Include validation steps after each layer (row counts, schema checks, anomaly detection)
Follow the .ipynb validation + Fabric nuances in notebook-api-operations.md when creating notebooks via REST API — every code cell must include "outputs": [] and "execution_count": null
Default to separate workspaces per layer for governance and access control: one workspace each for Bronze, Silver, and Gold
Complete the full end-to-end flow — do not stop after creating notebooks; always bind lakehouses, execute notebooks sequentially (Bronze → Silver → Gold), verify results, and connect Power BI to the Gold layer unless the user explicitly requests a partial setup
PREFER
Incremental processing (watermark pattern) over full refresh
Separate notebooks per layer for independent testing and debugging
ZORDER on frequently filtered columns in Gold tables
Running OPTIMIZE after writes in Silver and Gold layers
Environment-specific Spark configs (write-heavy for Bronze, balanced for Silver, read-heavy for Gold)
OneLake shortcuts to expose Gold data to consumer workspaces without duplication
Clear layer ownership: engineers own Bronze/Silver, analysts own Gold
Fabric Variable Libraries to centralize paths and configuration across layers
Multi-workspace deployment patterns for medium/high governance requirements (Bronze/Silver/Gold in separate workspaces)
AVOID
Storing all layers in a single lakehouse — this defeats isolation and independent optimization
Skipping the Silver layer and going directly from Bronze to Gold
Hardcoded workspace IDs, lakehouse IDs, or FQDNs — discover via REST API
SELECT * without LIMIT on Bronze tables (they grow unboundedly)
Running VACUUM without checking downstream dependencies
Chaining OneLake shortcuts between medallion layers (Bronze→Silver→Gold) — each layer must be physically materialized for lineage and governance
Copying complete implementation code into skills — guide the LLM to generate instead
Reading from external HTTP/HTTPS URLs directly in Spark — Fabric Spark cannot access arbitrary external URLs; land data in lakehouse Files/ first (via curl, OneLake API, or Fabric pipeline Copy activity), then read from the lakehouse path
Creating notebooks via REST API without validating .ipynb structure — missing execution_count: null or outputs: [] on code cells causes silent failures or "Job instance failed without detail error"
Workspace Setup Guidance

When setting up a medallion workspace, guide LLM to generate commands for:

Default architecture: create three workspaces (recommended):
{project}-bronze-{env}
{project}-silver-{env}
{project}-gold-{env}
Create one lakehouse per workspace:
Bronze workspace → {project}_bronze lakehouse
Silver workspace → {project}_silver lakehouse
Gold workspace → {project}_gold lakehouse
Assign RBAC per layer workspace:
Bronze: ingestion/engineering write permissions
Silver: engineering/data quality permissions
Gold: analytics/BI consumer access with stricter curation controls
Create notebooks for each layer (one per transformation stage) — follow .ipynb validation + Fabric nuances
Bind each notebook to its lakehouse — set metadata.dependencies.lakehouse with the correct lakehouse ID (see notebook-api-operations.md § Default Lakehouse Binding):
Bronze notebook → Bronze workspace/lakehouse
Silver notebook → Silver workspace/lakehouse (reads Bronze via cross-workspace oneLake access / fully qualified references)
Gold notebook → Gold workspace/lakehouse (reads Silver via cross-workspace access)
Confirm notebook deployment — check that updateDefinition returned Succeeded; this is sufficient confirmation that content and lakehouse binding persisted. Do NOT call getDefinition to re-verify — it is an async LRO and adds unnecessary latency.
Execute notebooks sequentially — Bronze first, then Silver, then Gold — using POST .../jobs/instances?jobType=RunNotebook with the correct defaultLakehouse in execution config (both id and name required)
Connect Power BI to Gold layer — discover the Gold lakehouse SQL endpoint, create a Direct Lake semantic model, create a report with visuals on the Gold summary table (see Gold Layer → Power BI Consumption)
Create pipeline to orchestrate the Bronze → Silver → Gold flow for recurring execution
Explicit Override: Single Workspace

If the user explicitly asks for a single workspace deployment (for example, POC/small team/monolithic pattern), keep the current approach:

One workspace with separate Bronze/Silver/Gold lakehouses
Preserve layer separation logically even when workspace is shared
Call out governance trade-offs versus multi-workspace design

Parameterize by environment: workspace name suffix (-dev, -prod), data volume (sample vs full), capacity SKU, and Bronze retention period.

Bronze Layer — Ingestion Patterns

When a user requests data ingestion into the Bronze layer, guide LLM to:

Land data in lakehouse first: External data must be staged into the lakehouse Files/ folder before Spark can read it — use one of:
Fabric Pipeline Copy activity (preferred for recurring loads) — connects to external sources (HTTP, FTP, databases, cloud storage) and writes to OneLake
OneLake API / curl — upload files via REST API using storage.azure.com token (see COMMON-CLI.md § OneLake Data Access)
OneLake Shortcut — for data already in Azure ADLS Gen2, S3, or another OneLake location
notebookutils.fs — copy from mounted storage paths within a notebook
⚠️ Fabric Spark cannot read from arbitrary HTTP/HTTPS URLs — spark.read.format("csv").load("https://...") will fail
Read from lakehouse path: Once data is in Files/, read using lakehouse-relative paths (e.g., spark.read.format("csv").load("Files/landing/daily/"))
Add metadata and write: Tracking columns (ingestion timestamp, source file, batch ID), Delta table with descriptive name, partition by ingestion date, append mode
Validate: Log row counts, validate schema structure, flag anomalies vs historical patterns
Silver Layer — Transformation Patterns

When a user requests Bronze-to-Silver transformation, guide LLM to:

Quality rules: Deduplicate on natural/composite key, filter invalid ranges, handle nulls (drop required, fill optional), validate logical constraints
Schema conformance: snake_case column names, standardized data types, derived columns (durations, percentages, categories)
Schema evolution: Use mergeSchema option when source schemas change; coordinate downstream updates to Gold tables and Power BI datasets
Write strategy: Partition by business date, partition-aware overwrite, run OPTIMIZE after write, log before/after metrics
Gold Layer — Aggregation Patterns

When a user requests Gold analytics tables, guide LLM to generate:

Common aggregates: Daily/weekly/monthly summaries, dimensional analysis (by location, category, type), trend breakdowns over time, demand patterns (hour-of-day, day-of-week)
Spark session config — set these properties in the Gold notebook before any write operations:
spark.conf.set("spark.sql.parquet.vorder.default", "true")
spark.conf.set("spark.databricks.delta.optimizeWrite.enabled", "true")
spark.conf.set("spark.databricks.delta.optimizeWrite.binSize", "1g")

V-Order (vorder.default) — applies Fabric's columnar sort optimization to all Parquet files, dramatically improving Direct Lake and SQL endpoint read performance
Optimize Write (optimizeWrite.enabled) — coalesces small partitions into optimally-sized files (target ~1 GB per binSize), reducing file count and improving scan efficiency
Optimization: ZORDER on filter columns, run OPTIMIZE after writes, pre-aggregate metrics to avoid runtime computation
End-to-End Execution Flow

When setting up medallion architecture end-to-end, the LLM must not stop after creating notebooks and deploying code. The complete lifecycle is:

Create Resources → Deploy Content → Bind Lakehouses → Execute → Verify Results

Step-by-Step
Create layer workspaces and lakehouses (default) — one workspace and one lakehouse per layer (Bronze, Silver, Gold); capture workspace IDs and lakehouse IDs
Create notebooks — one per layer, with valid .ipynb structure (see notebook-api-operations.md)
Bind lakehouse to each notebook — include metadata.dependencies.lakehouse in the .ipynb payload with:
default_lakehouse: the target lakehouse GUID
default_lakehouse_name: the lakehouse display name
default_lakehouse_workspace_id: the workspace GUID
Deploy notebook content — updateDefinition with the Base64-encoded .ipynb payload (content + lakehouse binding together)
Confirm deployment — check that each updateDefinition LRO returned Succeeded; that is sufficient. Do NOT call getDefinition to re-verify — it is an async LRO and adds significant latency per notebook.
Execute notebooks sequentially — use POST .../jobs/instances?jobType=RunNotebook:
Pass defaultLakehouse with both id and name in executionData.configuration
Run Bronze first → poll until Completed → run Silver → poll → run Gold → poll
Check for recent jobs before submitting (prevent duplicates — see SPARK-AUTHORING-CORE.md)
Verify results — after each notebook completes, confirm expected tables exist and row counts are reasonable
Connect Power BI to Gold — create semantic model + report on Gold summary tables (see Gold Layer → Power BI Consumption)
Common Failure: Stopping After Notebook Creation

If the flow stops after deploying notebook code without binding or executing:

Notebooks will have no lakehouse context → spark.sql() and relative paths (Tables/, Files/) fail at runtime
The user sees no output or results — the architecture is set up but never tested
Always complete through step 7 unless the user explicitly asks to stop at a specific step
Gold Layer → Power BI Consumption

After Gold tables are populated, connect Power BI to surface the analytics. Build a semantic model on top of the Gold lakehouse, using DirectLake.

Step-by-Step
Discover the Gold lakehouse SQL endpoint — call GET /v1/workspaces/{workspaceId}/lakehouses/{goldLakehouseId} and extract properties.sqlEndpointProperties.connectionString and provisioningStatus; wait until status is Success
Verify Gold tables via SQL — connect to the SQL endpoint using sqlcmd (see COMMON-CLI.md § SQL / TDS Data-Plane Access) and confirm the target table exists:
SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'nyc_taxi_daily_summary'

Create a semantic model — use the powerbi-authoring-cli skill for semantic model creation and TMDL deployment. Create via POST /v1/workspaces/{workspaceId}/items with type: "SemanticModel" then deploy definition via updateDefinition using TMDL format (see ITEM-DEFINITIONS-CORE.md § SemanticModel):
The model must reference the Gold lakehouse SQL endpoint as its data source
Define a table mapping to the Gold summary table (e.g., nyc_taxi_daily_summary)
Use Direct Lake mode — this connects directly to Delta tables in OneLake without data import
Include measures for key aggregations you find interesting (e.g., Total Trips, Avg Fare, Total Revenue, Month over Month Growth)
Create a Power BI report — POST /v1/workspaces/{workspaceId}/items with type: "Report" then deploy definition via updateDefinition using PBIR format (see ITEM-DEFINITIONS-CORE.md § Report):
Reference the semantic model created in step 3 via definition.pbir
Define at least one page with visuals on the Gold summary table
Suggested visuals: line chart (daily trend), card (KPI totals), bar chart (by category), table (detail view)
Verify end-to-end — use the powerbi-consumption-cli skill to run DAX queries against the semantic model and confirm data flows from Gold tables through to the report
Principles
Discover SQL endpoint dynamically — the connection string is in properties.sqlEndpointProperties.connectionString on the lakehouse response; never hardcode it
Wait for SQL endpoint provisioning — status must be Success before connecting; newly created lakehouses may take minutes to provision
Prefer Direct Lake mode — avoids data duplication; semantic model reads directly from OneLake Delta tables
Match table/column names exactly — the semantic model table definition must use the exact Delta table and column names from the Gold lakehouse
For semantic model authoring (TMDL, refresh, permissions), cross-reference the powerbi-authoring-cli skill
For DAX query validation, cross-reference the powerbi-consumption-cli skill
Pipeline Orchestration

When a user requests a pipeline for the medallion flow, guide LLM to design with:

Structure: Sequential activities (Bronze → Silver → Gold), each waiting for previous success; independent Gold aggregations can run in parallel; include validation and notification activities
Parameterization: Pipeline-level processing date (defaults to yesterday), passed to all notebooks; dynamic date expressions
Scheduling: Daily aligned with source refresh, watermark-based incremental processing, periodic full refresh for corrections
Error handling: Retry with backoff for transient failures, alerting for persistent failures, graceful degradation (downstream uses previous data if upstream fails)
Environment Optimization

For detailed Spark configurations and optimization strategies, see data-engineering-patterns.md.

Layer	Profile	Key Settings
Bronze	Write-heavy	Disable V-Order, enable autoCompact, large file targets, partition by ingestion_date
Silver	Balanced	Enable V-Order, adaptive query execution, partition by business date, ZORDER on filtered columns
Gold	Read-heavy	V-Order (spark.sql.parquet.vorder.default=true), Optimize Write (optimizeWrite.enabled=true, binSize=1g), vectorized readers, adaptive execution, ZORDER on all filter columns, pre-aggregate metrics
Examples
Example 1: Set Up Medallion Workspaces (Default)

Prompt: "Set up medallion architecture with separate Bronze, Silver, and Gold workspaces for sales analytics"

What the LLM should generate: REST API calls to:

Create workspaces: sales-bronze-dev, sales-silver-dev, sales-gold-dev
Create one lakehouse in each workspace: sales_bronze, sales_silver, sales_gold
Assign RBAC roles per workspace/layer
# Workspace creation (see COMMON-CLI.md for full patterns)
cat > /tmp/body.json << 'EOF'
{"displayName": "sales-analytics-dev"}
EOF
workspace_id=$(az rest --method post --resource "https://api.fabric.microsoft.com" \
  --url "https://api.fabric.microsoft.com/v1/workspaces" \
  --body @/tmp/body.json --query "id" --output tsv)

# Create Bronze lakehouse
cat > /tmp/body.json << 'EOF'
{"displayName": "sales_bronze", "type": "Lakehouse"}
EOF
az rest --method post --resource "https://api.fabric.microsoft.com" \
  --url "https://api.fabric.microsoft.com/v1/workspaces/$workspace_id/items" \
  --body @/tmp/body.json

Example 2: Design Bronze Ingestion

Prompt: "Ingest daily CSV files into bronze lakehouse with metadata columns"

What the LLM should generate: PySpark notebook that:

Reads source files with schema inference or explicit schema
Adds ingestion_timestamp, source_file, batch_id columns
Writes to Delta table partitioned by ingestion date
Logs row count and validation metrics
# Bronze ingestion pattern (guide LLM to generate full implementation)
from pyspark.sql.functions import current_timestamp, input_file_name, lit
import uuid

batch_id = str(uuid.uuid4())
df = (spark.read.format("csv").option("header", True).load("/Files/landing/daily/")
      .withColumn("ingestion_timestamp", current_timestamp())
      .withColumn("source_file", input_file_name())
      .withColumn("batch_id", lit(batch_id)))
df.write.mode("append").partitionBy("ingestion_date").format("delta").saveAsTable("bronze.events_raw")

Example 3: Bronze-to-Silver Transformation

Prompt: "Clean bronze data: remove duplicates, filter invalid records, add derived columns, write to silver"

What the LLM should generate: PySpark notebook applying quality rules, schema conformance, and partitioned write with optimization.

Example 4: End-to-End Pipeline

Prompt: "Create a pipeline that runs bronze ingestion, then silver transformation, then gold aggregation daily at 2 AM"

What the LLM should generate: Pipeline JSON definition with sequential notebook activities, date parameter, retry logic, and schedule trigger.

Weekly Installs
19
Repository
microsoft/skill…r-fabric
GitHub Stars
313
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass