---
title: database-indexing
url: https://skills.sh/1mangesh1/dev-skills-collection/database-indexing
---

# database-indexing

skills/1mangesh1/dev-skills-collection/database-indexing
database-indexing
Installation
$ npx skills add https://github.com/1mangesh1/dev-skills-collection --skill database-indexing
SKILL.md
Database Indexing
What an Index Does

An index is a separate data structure that maps column values to the physical locations of rows. Without an index, the database must perform a sequential scan (full table scan), reading every row to find matches. With an index, the database navigates a much smaller structure to locate rows directly.

B-tree Structure

The default index in PostgreSQL and MySQL (InnoDB) is a B-tree -- a balanced, sorted tree where the root node contains boundary keys and pointers to child nodes, internal nodes narrow the search range at each level, and leaf nodes hold the indexed values paired with pointers to the actual table rows. Leaf nodes are linked in order, so range scans walk the leaf chain without returning to upper levels.

A lookup traverses from root to leaf in O(log n) steps. For a table with 10 million rows, a B-tree typically requires 3-4 page reads to locate a single value.

How a Lookup Works
The query planner determines that an index is useful for the query.
The database reads the root page and follows pointers through internal pages based on comparison with search keys.
It reaches a leaf page containing the target value and a pointer to the heap (table row).
It fetches the row from the heap (unless the index covers all required columns).
When to Add Indexes

Add indexes on columns that appear in:

WHERE clauses with equality or range conditions on selective columns.
JOIN conditions -- foreign key columns used in joins almost always need indexes.
ORDER BY / GROUP BY -- an index matching the sort order avoids a separate sort step.
Unique constraints -- these implicitly create indexes.

Index columns with high selectivity (many distinct values relative to row count). If a query runs frequently and scans a large portion of the table, it is a candidate. Measure before and after -- do not guess.

When NOT to Index
Small tables (under a few thousand rows). A sequential scan is often faster than the overhead of index lookups because the entire table fits in a few pages.
High-write, low-read tables (logging tables, event streams). Every INSERT, UPDATE, and DELETE must also update every index on the table.
Low-cardinality columns (boolean flags, status columns with 3-5 values). The index does not narrow the search enough to justify the overhead. Exception: partial indexes on a rare value can still help.
Columns rarely used in queries. An index that is never used wastes storage and slows writes.
Index Types
B-tree

Default in PostgreSQL and MySQL. Supports equality, range (<, >, BETWEEN), IS NULL, LIKE 'prefix%' (but not LIKE '%suffix'), and ORDER BY. Use B-tree unless you have a specific reason to choose something else.

Hash

Supports only equality comparisons (=). In PostgreSQL, hash indexes are WAL-logged since version 10 and are safe to use, but they rarely outperform B-tree. In MySQL (InnoDB), hash indexes exist only in the adaptive hash index (internal, automatic). Use hash indexes only when you are certain you will never need range queries on that column.

GIN (Generalized Inverted Index) -- PostgreSQL

Designed for values that contain multiple elements: arrays, JSONB, full-text search (tsvector), and trigram similarity. GIN indexes map each element to the set of rows containing it. They are larger and slower to update than B-tree but excel at containment queries (@>, &&, @@).

CREATE INDEX idx_tags ON articles USING gin(tags);
SELECT * FROM articles WHERE tags @> ARRAY['postgres', 'performance'];

GiST (Generalized Search Tree) -- PostgreSQL

Supports geometric data, range types, full-text search, and nearest-neighbor queries. GiST is lossy for some data types (it may return false positives that are rechecked). Use for spatial queries (<-> distance operator) and range overlap (&&).

CREATE INDEX idx_location ON places USING gist(coordinates);

BRIN (Block Range Index) -- PostgreSQL

Stores min/max summaries for each block range in the table. Extremely small index size. Effective only when physical row order correlates with column values -- common for timestamp columns on append-only tables. Useless if values are randomly distributed across pages.

CREATE INDEX idx_created ON events USING brin(created_at);

Composite Indexes

A composite (multi-column) index indexes two or more columns together.

Column Order and the Leftmost Prefix Rule

A composite index on (a, b, c) can satisfy queries that filter on:

a
a and b
a, b, and c

It cannot efficiently satisfy queries that filter only on b, only on c, or on b and c without a. The leftmost prefix must be present.

Choosing Column Order
Place equality columns first, range columns last. A query WHERE status = 'active' AND created_at > '2025-01-01' benefits from an index on (status, created_at), not (created_at, status).
If the same columns appear in different query patterns with different leading columns, you may need separate indexes.
CREATE INDEX idx_orders_status_date ON orders(status, created_at);

Partial Indexes

A partial index includes only rows that satisfy a condition. This reduces index size and maintenance cost.

CREATE INDEX idx_active_users ON users(email) WHERE active = true;


This index is used only when the query includes WHERE active = true (or a condition the planner can prove implies it). Useful for:

Indexing a small subset of a large table (e.g., unprocessed jobs, recent records).
Replacing a full index on a low-cardinality column with a filtered index on the rare value.

Partial indexes are supported in PostgreSQL. MySQL does not support them.

Covering Indexes (INCLUDE Columns)

A covering index contains all columns needed by a query, so the database never visits the heap (table) at all. This is called an index-only scan.

In PostgreSQL 11+, use INCLUDE to add non-searchable columns to the index:

CREATE INDEX idx_orders_cover ON orders(customer_id) INCLUDE (total, status);


The INCLUDE columns are stored in leaf pages but are not part of the tree structure, so they do not affect search or ordering. The query SELECT total, status FROM orders WHERE customer_id = 42 can be answered entirely from the index.

In MySQL (InnoDB), the primary key is appended to every secondary index automatically, which makes secondary indexes partially covering by default.

Expression Indexes

Index the result of a function or expression rather than a raw column value.

CREATE INDEX idx_lower_email ON users (lower(email));


This index is used only when the query matches the exact expression: WHERE lower(email) = 'user@example.com'. It will not be used for WHERE email = 'user@example.com'.

Common uses: case-insensitive lookups, extracting JSONB fields, date truncation (CREATE INDEX idx_year ON events ((extract(year FROM event_date)))).

Reading EXPLAIN and EXPLAIN ANALYZE
Basic Usage
EXPLAIN SELECT * FROM orders WHERE customer_id = 42;
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 42;


EXPLAIN shows the planned execution without running the query. EXPLAIN ANALYZE runs the query and shows actual timings and row counts. Use EXPLAIN ANALYZE in development -- never on production with destructive statements (it executes the query).

Key Scan Types
Seq Scan -- reads every row in the table. Expected on small tables or non-selective filters.
Index Scan -- traverses the index, then fetches rows from the heap. Standard index usage.
Index Only Scan -- reads only the index, never visits the heap. Requires a covering index and a recently vacuumed table (visibility map must be up to date).
Bitmap Index Scan -- builds a bitmap of matching pages from the index, then fetches pages in physical order. Used when too many rows match for a plain index scan but too few for a sequential scan.
What to Look For
Large gaps between estimated rows and actual rows indicate stale statistics. Run ANALYZE.
Seq Scan on a large table with a selective WHERE clause suggests a missing index.
Sort nodes with high cost may be eliminated by an index matching the ORDER BY.
Nested loop joins on unindexed columns produce O(n*m) behavior.
Index Maintenance
Bloat

UPDATE and DELETE operations in PostgreSQL do not remove index entries immediately. Dead tuples accumulate, causing index bloat. Autovacuum cleans up dead tuples, but under heavy write loads it may fall behind.

Monitor bloat:

SELECT schemaname, relname, indexrelname,
       pg_size_pretty(pg_relation_size(indexrelid)) AS index_size
FROM pg_stat_user_indexes
ORDER BY pg_relation_size(indexrelid) DESC;

REINDEX

Rebuilds an index from scratch, removing bloat. Locks the table for writes in standard mode. Use REINDEX CONCURRENTLY (PostgreSQL 12+) for online rebuilds.

REINDEX INDEX CONCURRENTLY idx_orders_status_date;

Finding Unused Indexes
SELECT indexrelname, idx_scan, pg_size_pretty(pg_relation_size(indexrelid)) AS size
FROM pg_stat_user_indexes
WHERE idx_scan = 0
ORDER BY pg_relation_size(indexrelid) DESC;


Indexes with zero scans since the last statistics reset are candidates for removal. Verify no rare but critical queries depend on them before dropping.

MySQL vs PostgreSQL Index Differences
Feature	PostgreSQL	MySQL (InnoDB)
Clustered index	Optional (via CLUSTER)	Always on primary key
Secondary indexes	Point to heap tuple (ctid)	Store the primary key value
Partial indexes	Supported	Not supported
Expression indexes	Supported	Supported (8.0.13+, functional indexes)
INCLUDE columns	Supported (11+)	Not supported
GIN, GiST, BRIN	Supported	Not available
Hash indexes	WAL-logged, explicit	Adaptive hash index (internal only)
Online DDL	CREATE INDEX CONCURRENTLY	ALTER TABLE ... ALGORITHM=INPLACE
Covering index syntax	INCLUDE (cols)	All InnoDB indexes include PK

In MySQL InnoDB, the table is a clustered B-tree ordered by primary key. Secondary index lookups require a second traversal (secondary index to PK, then PK to row), making primary key choice critical -- use a compact, auto-incrementing integer.

MongoDB Indexes
Single Field and Compound Indexes
db.orders.createIndex({ customer_id: 1 });
db.orders.createIndex({ customer_id: 1, created_at: -1 });


Compound indexes follow the same leftmost prefix rule as relational databases. The direction (1 ascending, -1 descending) matters for sort operations.

Text Indexes
db.articles.createIndex({ title: "text", body: "text" });


One text index per collection. Supports language-specific stemming and stop words.

TTL Indexes

Automatically delete documents after a specified time. Only works on Date fields, single-field only:

db.sessions.createIndex({ created_at: 1 }, { expireAfterSeconds: 3600 });

Sparse and Partial Filter Indexes

Sparse indexes include only documents where the field exists, reducing index size. Prefer partialFilterExpression (MongoDB 3.2+) for more control:

db.users.createIndex({ phone: 1 }, { partialFilterExpression: { phone: { $exists: true } } });

Common Anti-patterns

Indexing every column. Each index consumes storage and slows every write. A table with 15 indexes on 20 columns is almost certainly over-indexed.

Redundant indexes. An index on (a, b) makes a separate index on (a) redundant, because the composite index satisfies single-column lookups on a. Check for these and remove them.

Unused indexes. Query pg_stat_user_indexes (PostgreSQL) or sys.schema_unused_indexes (MySQL performance_schema) regularly. Drop indexes that have zero scans over a meaningful time period.

Indexing for queries that do not exist. Adding indexes based on schema rather than actual query patterns leads to waste. Index based on measured workload.

Ignoring index impact on writes. Every INSERT must update every index. On write-heavy tables, excessive indexing directly causes poor write throughput.

Index Impact on Writes

For each INSERT:

One write to the heap (table).
One write per index (B-tree insertion, possible page split).

For each UPDATE on an indexed column:

The old index entry is marked dead (PostgreSQL) or removed (MySQL).
A new index entry is inserted.

For each DELETE:

All index entries for that row must be cleaned up.

In PostgreSQL, HOT (Heap-Only Tuple) updates avoid index updates when the updated columns are not indexed and the new tuple fits on the same page. This is a strong argument against indexing columns that are frequently updated.

Benchmark write throughput before and after adding indexes on write-heavy tables.

Practical Example: Diagnosing and Fixing a Slow Query

Symptom: The following query takes 4 seconds on a table with 5 million rows:

SELECT id, email, created_at
FROM users
WHERE status = 'active' AND created_at > '2025-01-01'
ORDER BY created_at DESC
LIMIT 20;


Step 1: Run EXPLAIN ANALYZE. Output shows Seq Scan on users, actual time 3800ms, rows removed by filter: 4,200,000.

Step 2: Identify the problem. Full table scan. No index on status or created_at.

Step 3: Choose the right index. The query filters on status (equality) and created_at (range), then sorts by created_at. A composite index with the equality column first:

CREATE INDEX idx_users_status_created ON users(status, created_at DESC);


Step 4: Consider a covering index to avoid heap fetches:

CREATE INDEX idx_users_status_created_cover
ON users(status, created_at DESC) INCLUDE (email);


Step 5: Verify with EXPLAIN ANALYZE again. Expected result: Index Only Scan (or Index Scan), actual time under 1ms, reads only 20 rows from the index.

Step 6: Monitor. Check pg_stat_user_indexes after deployment to confirm the new index is being used and that it did not introduce regression on write operations.

References
PostgreSQL Index Types: https://www.postgresql.org/docs/current/indexes-types.html
Use The Index, Luke: https://use-the-index-luke.com/
MySQL InnoDB Indexes: https://dev.mysql.com/doc/refman/8.0/en/innodb-index-types.html
MongoDB Indexes: https://www.mongodb.com/docs/manual/indexes/
Weekly Installs
13
Repository
1mangesh1/dev-s…llection
GitHub Stars
3
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass