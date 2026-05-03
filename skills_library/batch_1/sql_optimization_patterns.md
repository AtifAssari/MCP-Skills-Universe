---
title: sql-optimization-patterns
url: https://skills.sh/wshobson/agents/sql-optimization-patterns
---

# sql-optimization-patterns

skills/wshobson/agents/sql-optimization-patterns
sql-optimization-patterns
Installation
$ npx skills add https://github.com/wshobson/agents --skill sql-optimization-patterns
Summary

Master SQL query optimization, indexing strategies, and EXPLAIN analysis to eliminate slow queries.

Covers EXPLAIN plan analysis with key metrics (Seq Scan, Index Scan, cost, rows, execution time) and five index types (B-Tree, Hash, GIN, GiST, BRIN) for different query patterns
Includes five core optimization patterns: eliminating N+1 queries, cursor-based pagination, efficient aggregation, subquery transformation, and batch operations
Provides advanced techniques like materialized views, table partitioning, and query hints for large-scale performance tuning
Includes monitoring queries to identify slow queries, missing indexes, and unused indexes in PostgreSQL
SKILL.md
SQL Optimization Patterns

Transform slow database queries into lightning-fast operations through systematic optimization, proper indexing, and query plan analysis.

When to Use This Skill
Debugging slow-running queries
Designing performant database schemas
Optimizing application response times
Reducing database load and costs
Improving scalability for growing datasets
Analyzing EXPLAIN query plans
Implementing efficient indexes
Resolving N+1 query problems
Core Concepts
1. Query Execution Plans (EXPLAIN)

Understanding EXPLAIN output is fundamental to optimization.

PostgreSQL EXPLAIN:

-- Basic explain
EXPLAIN SELECT * FROM users WHERE email = 'user@example.com';

-- With actual execution stats
EXPLAIN ANALYZE
SELECT * FROM users WHERE email = 'user@example.com';

-- Verbose output with more details
EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT u.*, o.order_total
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.created_at > NOW() - INTERVAL '30 days';


Key Metrics to Watch:

Seq Scan: Full table scan (usually slow for large tables)
Index Scan: Using index (good)
Index Only Scan: Using index without touching table (best)
Nested Loop: Join method (okay for small datasets)
Hash Join: Join method (good for larger datasets)
Merge Join: Join method (good for sorted data)
Cost: Estimated query cost (lower is better)
Rows: Estimated rows returned
Actual Time: Real execution time
2. Index Strategies

Indexes are the most powerful optimization tool.

Index Types:

B-Tree: Default, good for equality and range queries
Hash: Only for equality (=) comparisons
GIN: Full-text search, array queries, JSONB
GiST: Geometric data, full-text search
BRIN: Block Range INdex for very large tables with correlation
-- Standard B-Tree index
CREATE INDEX idx_users_email ON users(email);

-- Composite index (order matters!)
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- Partial index (index subset of rows)
CREATE INDEX idx_active_users ON users(email)
WHERE status = 'active';

-- Expression index
CREATE INDEX idx_users_lower_email ON users(LOWER(email));

-- Covering index (include additional columns)
CREATE INDEX idx_users_email_covering ON users(email)
INCLUDE (name, created_at);

-- Full-text search index
CREATE INDEX idx_posts_search ON posts
USING GIN(to_tsvector('english', title || ' ' || body));

-- JSONB index
CREATE INDEX idx_metadata ON events USING GIN(metadata);

3. Query Optimization Patterns

Avoid SELECT *:

-- Bad: Fetches unnecessary columns
SELECT * FROM users WHERE id = 123;

-- Good: Fetch only what you need
SELECT id, email, name FROM users WHERE id = 123;


Use WHERE Clause Efficiently:

-- Bad: Function prevents index usage
SELECT * FROM users WHERE LOWER(email) = 'user@example.com';

-- Good: Create functional index or use exact match
CREATE INDEX idx_users_email_lower ON users(LOWER(email));
-- Then:
SELECT * FROM users WHERE LOWER(email) = 'user@example.com';

-- Or store normalized data
SELECT * FROM users WHERE email = 'user@example.com';


Optimize JOINs:

-- Bad: Cartesian product then filter
SELECT u.name, o.total
FROM users u, orders o
WHERE u.id = o.user_id AND u.created_at > '2024-01-01';

-- Good: Filter before join
SELECT u.name, o.total
FROM users u
JOIN orders o ON u.id = o.user_id
WHERE u.created_at > '2024-01-01';

-- Better: Filter both tables
SELECT u.name, o.total
FROM (SELECT * FROM users WHERE created_at > '2024-01-01') u
JOIN orders o ON u.id = o.user_id;

Optimization Patterns
Pattern 1: Eliminate N+1 Queries

Problem: N+1 Query Anti-Pattern

# Bad: Executes N+1 queries
users = db.query("SELECT * FROM users LIMIT 10")
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)
    # Process orders


Solution: Use JOINs or Batch Loading

-- Solution 1: JOIN
SELECT
    u.id, u.name,
    o.id as order_id, o.total
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.id IN (1, 2, 3, 4, 5);

-- Solution 2: Batch query
SELECT * FROM orders
WHERE user_id IN (1, 2, 3, 4, 5);

# Good: Single query with JOIN or batch load
# Using JOIN
results = db.query("""
    SELECT u.id, u.name, o.id as order_id, o.total
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    WHERE u.id IN (1, 2, 3, 4, 5)
""")

# Or batch load
users = db.query("SELECT * FROM users LIMIT 10")
user_ids = [u.id for u in users]
orders = db.query(
    "SELECT * FROM orders WHERE user_id IN (?)",
    user_ids
)
# Group orders by user_id
orders_by_user = {}
for order in orders:
    orders_by_user.setdefault(order.user_id, []).append(order)

Pattern 2: Optimize Pagination

Bad: OFFSET on Large Tables

-- Slow for large offsets
SELECT * FROM users
ORDER BY created_at DESC
LIMIT 20 OFFSET 100000;  -- Very slow!


Good: Cursor-Based Pagination

-- Much faster: Use cursor (last seen ID)
SELECT * FROM users
WHERE created_at < '2024-01-15 10:30:00'  -- Last cursor
ORDER BY created_at DESC
LIMIT 20;

-- With composite sorting
SELECT * FROM users
WHERE (created_at, id) < ('2024-01-15 10:30:00', 12345)
ORDER BY created_at DESC, id DESC
LIMIT 20;

-- Requires index
CREATE INDEX idx_users_cursor ON users(created_at DESC, id DESC);

Pattern 3: Aggregate Efficiently

Optimize COUNT Queries:

-- Bad: Counts all rows
SELECT COUNT(*) FROM orders;  -- Slow on large tables

-- Good: Use estimates for approximate counts
SELECT reltuples::bigint AS estimate
FROM pg_class
WHERE relname = 'orders';

-- Good: Filter before counting
SELECT COUNT(*) FROM orders
WHERE created_at > NOW() - INTERVAL '7 days';

-- Better: Use index-only scan
CREATE INDEX idx_orders_created ON orders(created_at);
SELECT COUNT(*) FROM orders
WHERE created_at > NOW() - INTERVAL '7 days';


Optimize GROUP BY:

-- Bad: Group by then filter
SELECT user_id, COUNT(*) as order_count
FROM orders
GROUP BY user_id
HAVING COUNT(*) > 10;

-- Better: Filter first, then group (if possible)
SELECT user_id, COUNT(*) as order_count
FROM orders
WHERE status = 'completed'
GROUP BY user_id
HAVING COUNT(*) > 10;

-- Best: Use covering index
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

Pattern 4: Subquery Optimization

Transform Correlated Subqueries:

-- Bad: Correlated subquery (runs for each row)
SELECT u.name, u.email,
    (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id) as order_count
FROM users u;

-- Good: JOIN with aggregation
SELECT u.name, u.email, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id, u.name, u.email;

-- Better: Use window functions
SELECT DISTINCT ON (u.id)
    u.name, u.email,
    COUNT(o.id) OVER (PARTITION BY u.id) as order_count
FROM users u
LEFT JOIN orders o ON o.user_id = u.id;


Use CTEs for Clarity:

-- Using Common Table Expressions
WITH recent_users AS (
    SELECT id, name, email
    FROM users
    WHERE created_at > NOW() - INTERVAL '30 days'
),
user_order_counts AS (
    SELECT user_id, COUNT(*) as order_count
    FROM orders
    WHERE created_at > NOW() - INTERVAL '30 days'
    GROUP BY user_id
)
SELECT ru.name, ru.email, COALESCE(uoc.order_count, 0) as orders
FROM recent_users ru
LEFT JOIN user_order_counts uoc ON ru.id = uoc.user_id;

Pattern 5: Batch Operations

Batch INSERT:

-- Bad: Multiple individual inserts
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com');
INSERT INTO users (name, email) VALUES ('Carol', 'carol@example.com');

-- Good: Batch insert
INSERT INTO users (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com'),
    ('Carol', 'carol@example.com');

-- Better: Use COPY for bulk inserts (PostgreSQL)
COPY users (name, email) FROM '/tmp/users.csv' CSV HEADER;


Batch UPDATE:

-- Bad: Update in loop
UPDATE users SET status = 'active' WHERE id = 1;
UPDATE users SET status = 'active' WHERE id = 2;
-- ... repeat for many IDs

-- Good: Single UPDATE with IN clause
UPDATE users
SET status = 'active'
WHERE id IN (1, 2, 3, 4, 5, ...);

-- Better: Use temporary table for large batches
CREATE TEMP TABLE temp_user_updates (id INT, new_status VARCHAR);
INSERT INTO temp_user_updates VALUES (1, 'active'), (2, 'active'), ...;

UPDATE users u
SET status = t.new_status
FROM temp_user_updates t
WHERE u.id = t.id;

Advanced Techniques
Materialized Views

Pre-compute expensive queries.

-- Create materialized view
CREATE MATERIALIZED VIEW user_order_summary AS
SELECT
    u.id,
    u.name,
    COUNT(o.id) as total_orders,
    SUM(o.total) as total_spent,
    MAX(o.created_at) as last_order_date
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name;

-- Add index to materialized view
CREATE INDEX idx_user_summary_spent ON user_order_summary(total_spent DESC);

-- Refresh materialized view
REFRESH MATERIALIZED VIEW user_order_summary;

-- Concurrent refresh (PostgreSQL)
REFRESH MATERIALIZED VIEW CONCURRENTLY user_order_summary;

-- Query materialized view (very fast)
SELECT * FROM user_order_summary
WHERE total_spent > 1000
ORDER BY total_spent DESC;

Partitioning

Split large tables for better performance.

-- Range partitioning by date (PostgreSQL)
CREATE TABLE orders (
    id SERIAL,
    user_id INT,
    total DECIMAL,
    created_at TIMESTAMP
) PARTITION BY RANGE (created_at);

-- Create partitions
CREATE TABLE orders_2024_q1 PARTITION OF orders
    FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

CREATE TABLE orders_2024_q2 PARTITION OF orders
    FOR VALUES FROM ('2024-04-01') TO ('2024-07-01');

-- Queries automatically use appropriate partition
SELECT * FROM orders
WHERE created_at BETWEEN '2024-02-01' AND '2024-02-28';
-- Only scans orders_2024_q1 partition

Query Hints and Optimization
-- Force index usage (MySQL)
SELECT * FROM users
USE INDEX (idx_users_email)
WHERE email = 'user@example.com';

-- Parallel query (PostgreSQL)
SET max_parallel_workers_per_gather = 4;
SELECT * FROM large_table WHERE condition;

-- Join hints (PostgreSQL)
SET enable_nestloop = OFF;  -- Force hash or merge join

Best Practices
Index Selectively: Too many indexes slow down writes
Monitor Query Performance: Use slow query logs
Keep Statistics Updated: Run ANALYZE regularly
Use Appropriate Data Types: Smaller types = better performance
Normalize Thoughtfully: Balance normalization vs performance
Cache Frequently Accessed Data: Use application-level caching
Connection Pooling: Reuse database connections
Regular Maintenance: VACUUM, ANALYZE, rebuild indexes
-- Update statistics
ANALYZE users;
ANALYZE VERBOSE orders;

-- Vacuum (PostgreSQL)
VACUUM ANALYZE users;
VACUUM FULL users;  -- Reclaim space (locks table)

-- Reindex
REINDEX INDEX idx_users_email;
REINDEX TABLE users;

Common Pitfalls
Over-Indexing: Each index slows down INSERT/UPDATE/DELETE
Unused Indexes: Waste space and slow writes
Missing Indexes: Slow queries, full table scans
Implicit Type Conversion: Prevents index usage
OR Conditions: Can't use indexes efficiently
LIKE with Leading Wildcard: LIKE '%abc' can't use index
Function in WHERE: Prevents index usage unless functional index exists
Monitoring Queries
-- Find slow queries (PostgreSQL)
SELECT query, calls, total_time, mean_time
FROM pg_stat_statements
ORDER BY mean_time DESC
LIMIT 10;

-- Find missing indexes (PostgreSQL)
SELECT
    schemaname,
    tablename,
    seq_scan,
    seq_tup_read,
    idx_scan,
    seq_tup_read / seq_scan AS avg_seq_tup_read
FROM pg_stat_user_tables
WHERE seq_scan > 0
ORDER BY seq_tup_read DESC
LIMIT 10;

-- Find unused indexes (PostgreSQL)
SELECT
    schemaname,
    tablename,
    indexname,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes
WHERE idx_scan = 0
ORDER BY pg_relation_size(indexrelid) DESC;

Weekly Installs
12.2K
Repository
wshobson/agents
GitHub Stars
34.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass