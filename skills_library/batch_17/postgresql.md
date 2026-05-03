---
title: postgresql
url: https://skills.sh/jgamaraalv/ts-dev-kit/postgresql
---

# postgresql

skills/jgamaraalv/ts-dev-kit/postgresql
postgresql
Installation
$ npx skills add https://github.com/jgamaraalv/ts-dev-kit --skill postgresql
SKILL.md
PostgreSQL 16+ Reference

Version: 16+. All syntax is standard; most features apply to PostgreSQL 13+.

<quick_reference>

Quick patterns
-- Check running queries
SELECT pid, state, wait_event_type, query FROM pg_stat_activity WHERE state != 'idle';

-- Explain a slow query
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT) SELECT ...;

-- List table sizes
SELECT relname, pg_size_pretty(pg_total_relation_size(oid)) FROM pg_class
WHERE relkind = 'r' ORDER BY pg_total_relation_size(oid) DESC;

-- Kill a blocking query
SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE pid = <pid>;


</quick_reference>

Key non-obvious facts
Every statement runs in a transaction. Without BEGIN, each statement auto-commits.
jsonb stores parsed binary (faster queries); json stores raw text (exact input preserved). Prefer jsonb.
LIKE 'foo%' can use B-tree; LIKE '%foo' cannot — use pg_trgm GIN for suffix search.
CREATE INDEX CONCURRENTLY avoids table lock but cannot run inside a transaction block.
EXPLAIN without ANALYZE shows the planner's estimate. Always use EXPLAIN (ANALYZE, BUFFERS) for real data.
Null values are stored in indexes by B-tree (unlike some other databases). IS NULL can use an index.
SERIAL/BIGSERIAL are shorthand for sequence + default; prefer GENERATED ALWAYS AS IDENTITY (SQL standard).
Default isolation level is Read Committed. SERIALIZABLE prevents all anomalies but may abort transactions.
Reference files

Load the relevant file when working on a specific topic:

Topic	File	When to read
SELECT, JOINs, CTEs, window functions	references/queries.md	Writing or debugging any query
CREATE TABLE, ALTER TABLE, constraints	references/ddl-schema.md	Designing or modifying schemas
Index types, creation, strategy	references/indexes.md	Adding indexes or fixing slow queries
Transactions, savepoints, isolation	references/transactions.md	Concurrency, locking, isolation issues
JSONB operators, GIN, jsonpath	references/jsonb.md	Working with JSON/JSONB columns
EXPLAIN output, VACUUM, stats	references/performance.md	Query tuning or performance analysis
psql meta-commands	references/psql-cli.md	Working interactively in psql
Weekly Installs
17
Repository
jgamaraalv/ts-dev-kit
GitHub Stars
14
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass