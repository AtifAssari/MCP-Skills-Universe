---
title: data-lake-platform
url: https://skills.sh/vasilyu1983/ai-agents-public/data-lake-platform
---

# data-lake-platform

skills/vasilyu1983/ai-agents-public/data-lake-platform
data-lake-platform
Installation
$ npx skills add https://github.com/vasilyu1983/ai-agents-public --skill data-lake-platform
SKILL.md
Data Lake Platform

Build and operate production data lakes and lakehouses: ingest, transform, store in open formats, and serve analytics reliably.

When to Use
Design data lake/lakehouse architecture
Set up ingestion pipelines (batch, incremental, CDC)
Build SQL transformation layers (SQLMesh, dbt)
Choose table formats and catalogs (Iceberg, Delta, Hudi)
Deploy query/serving engines (Trino, ClickHouse, DuckDB)
Implement streaming pipelines (Kafka, Flink)
Set up orchestration (Dagster, Airflow, Prefect)
Add governance, lineage, data quality, and cost controls
Triage Questions
Batch, streaming, or hybrid? What is the freshness SLO?
Append-only vs upserts/deletes (CDC)? Is time travel required?
Primary query pattern: BI dashboards (high concurrency), ad-hoc joins, embedded analytics?
PII/compliance: row/column-level access, retention, audit logging?
Platform constraints: self-hosted vs cloud, preferred engines, team strengths?
Default Baseline (Good Starting Point)
Storage: object storage + open table format (usually Iceberg)
Catalog: REST/Hive/Glue/Nessie/Unity (match your platform)
Transforms: SQLMesh or dbt (pick one and standardize)
Lake query: Trino (or Spark for heavy compute/ML workloads)
Serving (optional): ClickHouse/StarRocks/Doris for low-latency BI
Governance: DataHub/OpenMetadata + OpenLineage
Orchestration: Dagster/Airflow/Prefect
Workflow
Pick table format + catalog: references/storage-formats.md (use assets/cross-platform/template-schema-evolution.md and assets/cross-platform/template-partitioning-strategy.md)
Design ingestion (batch/incremental/CDC): references/ingestion-patterns.md (use assets/cross-platform/template-ingestion-governance-checklist.md and assets/cross-platform/template-incremental-loading.md)
Design transformations (bronze/silver/gold or data products): references/transformation-patterns.md (use assets/cross-platform/template-data-pipeline.md)
Choose lake query vs serving engines: references/query-engine-patterns.md
Add governance, lineage, and quality gates: references/governance-catalog.md (use assets/cross-platform/template-data-quality-governance.md and assets/cross-platform/template-data-quality.md)
Plan operations + cost controls: references/operational-playbook.md and references/cost-optimization.md (use assets/cross-platform/template-data-quality-backfill-runbook.md and assets/cross-platform/template-cost-optimization.md)
Architecture Patterns
Medallion (bronze/silver/gold): references/architecture-patterns.md
Data mesh (domain-owned data products): references/architecture-patterns.md
Streaming-first (Kappa): references/streaming-patterns.md
Quick Start
dlt + ClickHouse
pip install "dlt[clickhouse]"
dlt init rest_api clickhouse
python pipeline.py

SQLMesh + DuckDB
pip install sqlmesh
sqlmesh init duckdb
sqlmesh plan && sqlmesh run

Reliability and Safety
Do
Define data contracts and owners up front
Add quality gates (freshness, volume, schema, distribution) per tier
Make every pipeline idempotent and re-runnable (backfills are normal)
Treat access control and audit logging as first-class requirements
Avoid
Skipping validation to "move fast"
Storing PII without access controls
Pipelines that can't be re-run safely
Manual schema changes without version control
Resources
Resource	Purpose
references/architecture-patterns.md	Medallion, data mesh
references/ingestion-patterns.md	dlt vs Airbyte, CDC
references/transformation-patterns.md	SQLMesh vs dbt
references/storage-formats.md	Iceberg vs Delta
references/query-engine-patterns.md	ClickHouse, DuckDB
references/streaming-patterns.md	Kafka, Flink
references/orchestration-patterns.md	Dagster, Airflow
references/bi-visualization-patterns.md	Metabase, Superset
references/cost-optimization.md	Cost levers and maintenance
references/operational-playbook.md	Monitoring and incident response
references/governance-catalog.md	Catalog, lineage, access control
references/data-mesh-patterns.md	Domain ownership, data products, federated governance
references/data-quality-patterns.md	Quality gates, validation frameworks, SLOs, anomaly detection
references/security-access-patterns.md	Row/column security, encryption, audit logging, compliance
Templates
Template	Purpose
assets/cross-platform/template-medallion-architecture.md	Baseline bronze/silver/gold plan
assets/cross-platform/template-data-pipeline.md	End-to-end pipeline skeleton
assets/cross-platform/template-ingestion-governance-checklist.md	Source onboarding checklist
assets/cross-platform/template-incremental-loading.md	Incremental + backfill plan
assets/cross-platform/template-schema-evolution.md	Schema change rules
assets/cross-platform/template-cost-optimization.md	Cost control checklist
assets/cross-platform/template-data-quality-governance.md	Quality contracts + SLOs
assets/cross-platform/template-data-quality-backfill-runbook.md	Backfill incident/runbook
Related Skills
Skill	Purpose
ai-mlops	ML deployment
ai-ml-data-science	Feature engineering
data-sql-optimization	OLTP optimization
Fact-Checking
Use web search/web fetch to verify current external facts, versions, pricing, deadlines, regulations, or platform behavior before final answers.
Prefer primary sources; report source links and dates for volatile information.
If web access is unavailable, state the limitation and mark guidance as unverified.
Weekly Installs
91
Repository
vasilyu1983/ai-…s-public
GitHub Stars
59
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass