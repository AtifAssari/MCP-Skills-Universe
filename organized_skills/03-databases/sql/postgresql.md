---
rating: ⭐⭐
title: postgresql
url: https://skills.sh/itechmeat/llm-code/postgresql
---

# postgresql

skills/itechmeat/llm-code/postgresql
postgresql
Installation
$ npx skills add https://github.com/itechmeat/llm-code --skill postgresql
SKILL.md
PostgreSQL
RLS Multi-tenancy Pattern
Non-negotiables
RLS context is mandatory for any tenant-scoped query
Context must be set inside the same transaction as the queries
No fallbacks for tenant ID (fail fast if missing)
Async-only DB access when using async frameworks
Setting RLS Context

RLS works only if the current transaction has the context set:

SET LOCAL app.current_tenant_id = '<tenant_uuid>';


Must run before the first tenant-scoped query in that transaction.

Common Failure Modes
Setting SET LOCAL ... after the first select()
Setting the context in one session, then querying in another
Running queries outside the expected transaction scope
Typical RLS Policy
ALTER TABLE some_table ENABLE ROW LEVEL SECURITY;

CREATE POLICY some_table_tenant_isolation
ON some_table
USING (tenant_id = current_setting('app.current_tenant_id', true)::uuid);

Multi-tenant Table Checklist
Tenant ID column is UUID
FK to tenants table with ON DELETE CASCADE
Indexes aligned with access patterns (usually tenant_id first)
PostgreSQL does not auto-index FK columns — add explicit indexes
UNIQUE allows multiple NULLs unless using NULLS NOT DISTINCT (PG15+)
RLS is enabled and policies exist
Application code sets RLS context at transaction start
Alembic Migrations Checklist
Add/modify schema (columns, constraints, FKs)
Create/update indexes
Enable RLS and create/adjust policies
Add verification (tests) for isolation
Provide a real downgrade (no stubs)
RLS Isolation Testing Recipe

Goal:

Data for tenant A is visible to tenant A
Data for tenant A is NOT visible to tenant B

Canonical flow:

Setup data through an admin session (RLS bypass) for tenant A and B
Assert via an RLS session:
set context to tenant A → sees only tenant A data
set context to tenant B → does not see tenant A data
Destructive Operations Safety

Hard rules:

Never run DELETE without a narrow WHERE targeting specific data
Never run TRUNCATE/DROP without explicit confirmation

Pre-flight before destructive actions:

Confirm exact target (tables / IDs / date range)
Run a SELECT/row count first and show results
Ask for final confirmation, then execute
References
Schema & Design
table-design.md — Data types, constraints, indexing, partitioning, JSONB, safe schema evolution
charset-encoding.md — Character sets, encoding, collation, ICU, locale settings
Authentication
authentication.md — pg_hba.conf, SCRAM-SHA-256, md5, peer, cert, LDAP, GSSAPI
authentication-oauth.md — OAuth 2.0 (PostgreSQL 18+), SASL OAUTHBEARER, validators
user-management.md — CREATE/ALTER/DROP ROLE, membership, GRANT/REVOKE, predefined roles
Runtime Configuration
connection-settings.md — listen_addresses, max_connections, SSL, TCP keepalives
query-tuning.md — Planner settings, work_mem, parallel query, cost constants
replication.md — Streaming replication, WAL, synchronous commit, logical replication
vacuum.md — Autovacuum, vacuum cost model, freeze ages, per-table tuning
error-handling.md — exit_on_error, restart_after_crash, data_sync_retry
Internals
internals.md — Query processing pipeline, parser/rewriter/planner/executor, system catalogs, wire protocol, access methods
protocol.md — Wire protocol v3.2: message format, startup, auth, query, COPY, replication
Links
Documentation
Releases
GitHub
See Also
sql-expert — Query patterns, EXPLAIN workflow, optimization
Weekly Installs
61
Repository
itechmeat/llm-code
GitHub Stars
15
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass