---
rating: ⭐⭐⭐
title: clickhouse-migrations
url: https://skills.sh/posthog/posthog/clickhouse-migrations
---

# clickhouse-migrations

skills/posthog/posthog/clickhouse-migrations
clickhouse-migrations
Installation
$ npx skills add https://github.com/posthog/posthog --skill clickhouse-migrations
SKILL.md
ClickHouse Migrations

Read posthog/clickhouse/migrations/AGENTS.md for comprehensive patterns, cluster setup, examples, and ingestion layer details.

Quick reference
Migration structure
operations = [
    run_sql_with_exceptions(
        SQL_FUNCTION(),
        node_roles=[...],
        sharded=False,  # True for sharded tables
        is_alter_on_replicated_table=False  # True for ALTER on replicated tables
    ),
]

Node roles (choose based on table type)
[NodeRole.DATA]: Sharded tables (data nodes only)
[NodeRole.DATA, NodeRole.COORDINATOR]: Non-sharded data tables, distributed read tables, replicated tables, views, dictionaries
[NodeRole.INGESTION_SMALL]: Writable tables, Kafka tables, materialized views on ingestion layer
Table engines quick reference

MergeTree engines:

AggregatingMergeTree(table, replication_scheme=ReplicationScheme.SHARDED) for sharded tables
ReplacingMergeTree(table, replication_scheme=ReplicationScheme.REPLICATED) for non-sharded
Other variants: CollapsingMergeTree, ReplacingMergeTreeDeleted

Distributed engine:

Sharded: Distributed(data_table="sharded_events", sharding_key="sipHash64(person_id)")
Non-sharded: Distributed(data_table="my_table", cluster=settings.CLICKHOUSE_SINGLE_SHARD_CLUSTER)
Critical rules
NEVER use ON CLUSTER clause in SQL statements
Always use IF EXISTS / IF NOT EXISTS clauses
When dropping and recreating replicated table in same migration, use DROP TABLE IF EXISTS ... SYNC
If a function generating SQL has on_cluster param, always set on_cluster=False
Use sharded=True when altering sharded tables
Use is_alter_on_replicated_table=True when altering non-sharded replicated tables
Testing

Delete entry from infi_clickhouse_orm_migrations table to re-run a migration.

Weekly Installs
98
Repository
posthog/posthog
GitHub Stars
34.2K
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass