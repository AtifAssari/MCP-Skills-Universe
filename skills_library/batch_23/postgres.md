---
title: postgres
url: https://skills.sh/timescale/pg-aiguide/postgres
---

# postgres

skills/timescale/pg-aiguide/postgres
postgres
Installation
$ npx skills add https://github.com/timescale/pg-aiguide --skill postgres
SKILL.md
PostgreSQL Expert Skills

This skill provides comprehensive PostgreSQL expertise through specialized references. Load the appropriate reference based on the task.

Available References
Table Design
design-postgres-tables — Data types, constraints, indexes, JSONB patterns, partitioning, and PostgreSQL best practices. Use for any general table/schema design task.
design-postgis-tables — PostGIS spatial table design: geometry vs geography types, SRIDs, spatial indexing, and location-based query patterns. Use when the task involves geographic or spatial data.
Search
pgvector-semantic-search — Vector similarity search with pgvector: HNSW/IVFFlat indexes, halfvec storage, quantization, filtered search, and tuning. Use for embeddings, RAG, or semantic search.
postgres-hybrid-text-search — Hybrid search combining BM25 keyword search with pgvector semantic search using RRF. Use when combining keyword and meaning-based search.
TimescaleDB
setup-timescaledb-hypertables — Hypertable creation, compression, retention policies, continuous aggregates, and indexes. Use when setting up TimescaleDB from scratch.
find-hypertable-candidates — SQL queries to analyze existing tables and score them for hypertable conversion. Use when evaluating which tables to migrate.
migrate-postgres-tables-to-hypertables — Step-by-step migration: partition column selection, in-place vs blue-green, validation. Use when executing a migration.
How to Use
Identify which reference matches the user's task from the descriptions above.
Load the reference file to get detailed instructions and SQL patterns.
For tasks spanning multiple areas (e.g., "design a table with vector search"), load multiple references as needed.
Weekly Installs
198
Repository
timescale/pg-aiguide
GitHub Stars
1.7K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass