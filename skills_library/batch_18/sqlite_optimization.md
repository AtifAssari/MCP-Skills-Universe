---
title: sqlite-optimization
url: https://skills.sh/jrajasekera/claude-skills/sqlite-optimization
---

# sqlite-optimization

skills/jrajasekera/claude-skills/sqlite-optimization
sqlite-optimization
Installation
$ npx skills add https://github.com/jrajasekera/claude-skills --skill sqlite-optimization
SKILL.md
SQLite Performance Optimization
Quick Start: Baseline Configuration

Set these PRAGMAs on every connection for most applications:

PRAGMA journal_mode = WAL;          -- Non-blocking concurrent reads/writes
PRAGMA synchronous = NORMAL;        -- Fast commits, safe for WAL mode
PRAGMA foreign_keys = ON;           -- Data integrity
PRAGMA cache_size = -64000;         -- 64MB cache (negative = KB)
PRAGMA temp_store = MEMORY;         -- In-memory temp tables/sorting
PRAGMA busy_timeout = 5000;         -- 5s retry on lock contention
PRAGMA mmap_size = 2147483648;      -- 2GB memory-mapped I/O (benchmark first)


Run periodically:

PRAGMA optimize;  -- Update query planner statistics

Optimization Workflow
1. Diagnose with EXPLAIN QUERY PLAN
EXPLAIN QUERY PLAN SELECT ...;


Key indicators:

SCAN TABLE → Full table scan (O(N)) — needs index or query rewrite
SEARCH TABLE USING INDEX → Index lookup (O(log N)) — good
COVERING INDEX → Index-only scan, no table lookup — optimal
USE TEMP B-TREE → Sorting not covered by index — consider index with ORDER BY columns
2. Schema Design

Use INTEGER PRIMARY KEY for rowid alias:

CREATE TABLE users (
    id INTEGER PRIMARY KEY,  -- Alias for rowid, no extra index
    email TEXT NOT NULL,
    created_at TEXT
);


Choose appropriate types:

INTEGER for IDs, counters, booleans
REAL for floats
TEXT for strings
Avoid large BLOBs in hot tables; use separate table or external files

WITHOUT ROWID for junction tables:

CREATE TABLE user_roles (
    user_id INTEGER,
    role_id INTEGER,
    PRIMARY KEY (user_id, role_id)
) WITHOUT ROWID;  -- Clustered index, no rowid overhead

3. Indexing Strategy

Create indexes for real query patterns:

-- For: WHERE user_id = ? AND created_at >= ? ORDER BY created_at DESC
CREATE INDEX idx_orders_user_created 
ON orders (user_id, created_at DESC);


Covering indexes eliminate table lookups:

-- For: SELECT user_id, total FROM orders WHERE user_id = ?
CREATE INDEX idx_orders_cover 
ON orders (user_id, created_at DESC, total);


Partial indexes for subsets:

CREATE INDEX idx_active_users 
ON users (email) WHERE status = 'active';


Expression indexes:

CREATE INDEX idx_users_lower_email 
ON users (lower(email));


Avoid indexing:

Small tables (< hundreds of rows)
Low-cardinality columns alone (booleans)
Columns rarely in WHERE/JOIN/ORDER BY
4. Write Optimization

Always batch writes in transactions:

BEGIN TRANSACTION;
INSERT INTO logs (...) VALUES (...);
-- ... many more inserts
COMMIT;


Throughput jumps from ~50 inserts/sec (autocommit) to 50,000+ inserts/sec.

Use prepared statements:

stmt = conn.prepare("INSERT INTO logs (ts, level, msg) VALUES (?, ?, ?)")
for row in data:
    stmt.execute(row)


Optimal batch size: 1,000–10,000 rows balances throughput vs memory.

5. Concurrency Configuration

WAL mode enables concurrent readers + one writer:

Readers don't block writers
Writers don't block readers
Uses .wal and .shm files alongside main DB

Handle contention:

PRAGMA busy_timeout = 5000;  -- Retry for 5 seconds before SQLITE_BUSY


Architecture pattern: Single writer thread/process + many reader connections.

6. Maintenance

VACUUM after large deletes:

VACUUM;  -- Rebuilds and defragments DB file

Run during maintenance windows (blocking operation)
Requires free disk space ≈ DB size

Auto-vacuum for incremental reclaim:

PRAGMA auto_vacuum = INCREMENTAL;
VACUUM;  -- Apply change
-- Then periodically:
PRAGMA incremental_vacuum;


Keep statistics fresh:

PRAGMA optimize;  -- Smart, selective ANALYZE
-- Or full:
ANALYZE;

Reference Files
pragma-reference.md — Complete PRAGMA settings with tradeoffs
indexing-guide.md — Advanced indexing patterns and diagnostics
architecture.md — SQLite internals: B-trees, VDBE, Pager, concurrency mechanics
Common Anti-Patterns
Problem	Solution
SELECT *	List only needed columns
Loop with single inserts	Batch in transaction
Correlated subquery per row	Rewrite as JOIN
Index on every column	Index only queried columns
No busy_timeout	Set appropriate timeout
Rollback journal mode	Switch to WAL
Never running ANALYZE	Run PRAGMA optimize periodically
Environment-Specific Notes

Mobile (iOS/Android):

WAL + synchronous = NORMAL
Background maintenance jobs for VACUUM
Local storage only (not SD card)

Server/Desktop:

Centralize writes in single thread if possible
Set PRAGMAs immediately after connection open
Consider connection pooling with writer serialization
Weekly Installs
15
Repository
jrajasekera/cla…e-skills
GitHub Stars
1
First Seen
Feb 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass