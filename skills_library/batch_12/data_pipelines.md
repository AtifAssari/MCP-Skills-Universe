---
title: data-pipelines
url: https://skills.sh/kylelundstedt/dotfiles/data-pipelines
---

# data-pipelines

skills/kylelundstedt/dotfiles/data-pipelines
data-pipelines
Installation
$ npx skills add https://github.com/kylelundstedt/dotfiles --skill data-pipelines
SKILL.md

You are building data pipelines. The general pattern is ingest (get data in) → transform (clean, model, join) → query (analyze) → explore (notebooks, apps, visualizations).

The specific tools for each step depend on the project. Preferred defaults:

Step	Preferred Tool	Alternatives
Ingest	dlt	Plain Python scripts, shell + curl
Transform	sqlmesh	Plain SQL scripts, dbt, Python scripts
Query engine	DuckDB / MotherDuck	—
DataFrames	polars	—
Notebooks	marimo	—
Project mgmt	uv	—
Visualization	altair, seaborn	—
Language Preference

SQL first (DuckDB dialect), then Python, then bash. Use the simplest language that gets the job done.

Cross-references to other skills

This skill covers the opinionated stack for ingest/transform/notebook work. For the underlying tools, defer to:

DuckDB syntax (Friendly SQL, file reads, nested types) → motherduck-duckdb-sql or duckdb-docs
MotherDuck connections, exploration, sharing, Dives → motherduck-* skills
marimo notebooks (cells, reactivity, SQL cells) → marimo-notebook
Local DuckDB session management → attach-db, query, read-file
Project Layout

Data projects should follow this structure:

project/
├── ingest/              # Extraction and loading scripts
│   ├── <source>.py      # One file per data source
│   └── .dlt/            # dlt config (if using dlt)
├── transform/           # Transformation logic
│   ├── models/          # SQL models (sqlmesh or plain SQL)
│   └── config.yaml      # sqlmesh config (if using sqlmesh)
├── notebooks/           # Exploration and analysis
│   └── *.py             # marimo notebooks (plain .py files)
├── data/                # Local data files (gitignored)
├── pyproject.toml       # Dependencies
├── uv.lock              # Locked dependencies (committed)
└── *.duckdb             # Local database (gitignored)


Not every project needs all directories — a simple analysis might only have notebooks/ and a DuckDB file. Scale up as needed.

uv — Project Management

Never use pip directly. All Python work goes through uv.

uv init my-project                    # New project
uv add polars duckdb                  # Add dependencies
uv sync                               # Install into .venv
uv run python script.py               # Run in project venv
uv run --with requests script.py      # Ad-hoc dependency


Inline script dependencies (PEP 723) for standalone scripts:

# /// script
# dependencies = ["dlt[duckdb]", "polars"]
# requires-python = ">=3.12"
# ///


Run with uv run script.py — deps are resolved automatically.

Always commit uv.lock. Use pyproject.toml for dependency declarations, never requirements.txt.

polars — DataFrames

Use polars when Python logic is needed — complex string transforms, ML features, row-level conditionals. For joins, aggregations, and window functions, prefer SQL.

Key Patterns
import polars as pl

# Lazy evaluation (always prefer for production)
lf = pl.scan_parquet("events/*.parquet")
result = (
    lf.filter(pl.col("event_date") >= "2024-01-01")
    .group_by("user_id")
    .agg(pl.col("amount").sum().alias("total_spend"))
    .sort("total_spend", descending=True)
    .collect()
)

# Three contexts
df.select(...)         # Pick/transform columns (output has ONLY these)
df.with_columns(...)   # Add/overwrite columns (keeps all originals)
df.filter(...)         # Keep rows matching condition


DuckDB interop (zero-copy via Arrow):

import duckdb
result = duckdb.sql("SELECT * FROM df WHERE amount > 100").pl()

dlt — Ingestion

When a project uses dlt for ingestion. Handles API calls, pagination, schema inference, incremental loading, and state management.

Scaffold and Run
dlt init rest_api duckdb             # Scaffold pipeline
uv run python pipeline.py            # Run extraction
dlt pipeline <name> info             # Inspect state
dlt pipeline <name> schema           # View inferred schema

Pipeline Patterns

Minimal pipeline:

import dlt

pipeline = dlt.pipeline(
    pipeline_name="my_pipeline",
    destination="duckdb",
    dataset_name="raw",
)
info = pipeline.run(data, table_name="events")


Incremental loading:

@dlt.resource(write_disposition="merge", primary_key="id")
def users(updated_at=dlt.sources.incremental("updated_at")):
    yield from fetch_users(since=updated_at.last_value)


REST API source (declarative):

from dlt.sources.rest_api import rest_api_source

source = rest_api_source({
    "client": {"base_url": "https://api.example.com/v1"},
    "resource_defaults": {"primary_key": "id", "write_disposition": "merge"},
    "resources": [
        "users",
        {
            "name": "events",
            "write_disposition": "append",
            "endpoint": {
                "path": "events",
                "incremental": {"cursor_path": "created_at", "initial_value": "2024-01-01"},
            },
        },
    ],
})


Write dispositions:

Disposition	Behavior	Use For
append	Insert rows (default)	Immutable events, logs
replace	Drop and recreate	Small lookup tables
merge	Upsert by primary_key	Mutable records

Destinations: duckdb (local file), motherduck (cloud). Set motherduck_token env var or configure in .dlt/secrets.toml.

sqlmesh — Transformation

When a project uses sqlmesh for transformations. SQL-first, plan/apply workflow — no accidental production changes.

Scaffold and Run
sqlmesh init duckdb                              # New project
sqlmesh init -t dlt --dlt-pipeline <name>        # From dlt schema
sqlmesh plan                                     # Preview + apply (dev)
sqlmesh plan prod                                # Promote to production
sqlmesh fetchdf "SELECT * FROM analytics.users"  # Ad-hoc query
sqlmesh test                                     # Run unit tests
sqlmesh ui                                       # Web interface

Model Kinds
Kind	Behavior	Use For
FULL	Rewrite entire table	Small dimension tables
INCREMENTAL_BY_TIME_RANGE	Process new time intervals	Facts, events, logs
INCREMENTAL_BY_UNIQUE_KEY	Upsert by key	Mutable dimensions
SEED	Static CSV data	Reference/lookup data
VIEW	SQL view	Simple pass-throughs
SCD_TYPE_2	Slowly changing dimensions	Historical tracking
Model Example
MODEL (
    name analytics.stg_events,
    kind INCREMENTAL_BY_TIME_RANGE (time_column event_date),
    cron '@daily',
    grain (event_id),
    audits (NOT_NULL(columns=[event_id]))
);

SELECT
    event_id,
    user_id,
    event_type,
    event_date
FROM raw.events
WHERE event_date BETWEEN @start_date AND @end_date

Config (config.yaml)
gateways:
  local:
    connection:
      type: duckdb
      database: db.duckdb
default_gateway: local
model_defaults:
  dialect: duckdb

dlt Integration

sqlmesh init -t dlt auto-generates external models and incremental staging models from dlt's inferred schema. Schema changes from dlt are detected by sqlmesh plan.

Weekly Installs
58
Repository
kylelundstedt/dotfiles
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn