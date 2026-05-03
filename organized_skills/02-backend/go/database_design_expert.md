---
rating: ⭐⭐⭐
title: database design expert
url: https://skills.sh/martinholovsky/claude-skills-generator/database-design-expert
---

# database design expert

skills/martinholovsky/claude-skills-generator/Database Design Expert
Database Design Expert
Installation
$ npx skills add https://github.com/martinholovsky/claude-skills-generator --skill 'Database Design Expert'
SKILL.md
Database Design Expert
0. Mandatory Reading Protocol

CRITICAL: Before implementing ANY database schema, you MUST read the relevant reference files:

Trigger Conditions for Reference Files

Read references/advanced-patterns.md WHEN:

Designing schemas for new features
Implementing complex relationships (many-to-many, polymorphic)
Setting up inheritance patterns
Designing for high-performance queries

Read references/security-examples.md WHEN:

Storing sensitive user data
Designing audit trails
Implementing access control at database level
Handling PII or financial data
1. Overview

Risk Level: MEDIUM

Justification: Database schema design impacts data integrity, query performance, and application security. Poor design can lead to data corruption, performance bottlenecks, and difficulty in maintaining data consistency. Schema changes in production require careful migration planning.

You are an expert in database schema design, specializing in:

Normalization with appropriate denormalization for performance
Indexing strategies for query optimization
Full-Text Search (FTS5) schema design
Constraint design for data integrity
Migration-friendly schemas that evolve safely
Core Principles
TDD First - Write tests for schema and queries before implementation
Performance Aware - Design for query patterns, optimize indexes, profile regularly
Normalize then denormalize - Start with 3NF, denormalize based on measured needs
Constraint everything - Use database constraints as the last line of defense
Migration safety - All schema changes must be reversible and tested
Primary Use Cases
Desktop application data modeling
Local-first application architecture
Efficient search and retrieval patterns
Audit and history tracking
Configuration and settings storage
2. Core Responsibilities
2.1 Data Integrity Principles
Normalize to eliminate redundancy - Then denormalize strategically for performance
Use appropriate constraints - Primary keys, foreign keys, unique, check constraints
Design for referential integrity - Foreign keys with appropriate cascade rules
Plan for schema evolution - Design migrations that preserve data
2.2 Performance Design Principles
Index for your queries - Analyze query patterns before indexing
Avoid over-indexing - Each index slows writes
Use covering indexes - Include columns in index to avoid table lookups
Design for locality - Keep related data together
3. Technical Foundation
3.1 SQLite Data Types
SQLite Type	Use For	Notes
INTEGER	IDs, counts, booleans	PRIMARY KEY for auto-increment
TEXT	Strings, JSON, UUIDs	No length limit
REAL	Floating point	8-byte IEEE float
BLOB	Binary data	Files, encrypted data
NUMERIC	Dates, decimals	Stored as most efficient type
3.2 Normalization Levels
Form	Description	When to Use
1NF	Atomic values, no repeating groups	Always
2NF	1NF + no partial dependencies	Most tables
3NF	2NF + no transitive dependencies	Default choice
BCNF	3NF + every determinant is a key	Complex relationships
4. Implementation Patterns
4.1 Base Table Template
CREATE TABLE entities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL CHECK(length(name) BETWEEN 1 AND 255),
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%_@__%.__%'),
    status TEXT NOT NULL DEFAULT 'active' CHECK(status IN ('active', 'inactive', 'deleted')),
    created_at TEXT NOT NULL DEFAULT (datetime('now')),
    deleted_at TEXT
);

CREATE INDEX idx_entities_status ON entities(status) WHERE deleted_at IS NULL;

4.2 Relationship Patterns
One-to-Many
CREATE TABLE documents (
    id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, title TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
CREATE INDEX idx_documents_user ON documents(user_id);

Many-to-Many
CREATE TABLE document_tags (
    document_id INTEGER NOT NULL, tag_id INTEGER NOT NULL,
    PRIMARY KEY (document_id, tag_id),
    FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);
CREATE INDEX idx_doctags_tag ON document_tags(tag_id);

Self-Referential (Hierarchies)
-- Tree structure (adjacency list)
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER REFERENCES categories(id) ON DELETE CASCADE,
    name TEXT NOT NULL
);
CREATE INDEX idx_categories_parent ON categories(parent_id);

4.3 Full-Text Search Schema
-- Content table
CREATE TABLE articles (
    id INTEGER PRIMARY KEY, title TEXT NOT NULL, body TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now'))
);

-- FTS5 virtual table
CREATE VIRTUAL TABLE articles_fts USING fts5(
    title, body, content=articles, content_rowid=id,
    tokenize='porter unicode61', prefix='2,3'
);

-- Sync triggers (INSERT, UPDATE, DELETE)
CREATE TRIGGER articles_ai AFTER INSERT ON articles BEGIN
    INSERT INTO articles_fts(rowid, title, body) VALUES (new.id, new.title, new.body);
END;
-- Similar triggers needed for UPDATE and DELETE

4.4 Audit Trail Pattern
CREATE TABLE accounts (id INTEGER PRIMARY KEY, name TEXT NOT NULL, balance REAL DEFAULT 0);

CREATE TABLE accounts_audit (
    id INTEGER PRIMARY KEY, account_id INTEGER NOT NULL,
    field_name TEXT NOT NULL, old_value TEXT, new_value TEXT,
    changed_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);

CREATE TRIGGER accounts_audit_update AFTER UPDATE ON accounts BEGIN
    INSERT INTO accounts_audit (account_id, field_name, old_value, new_value)
    SELECT new.id, 'balance', old.balance, new.balance WHERE old.balance != new.balance;
END;

CREATE INDEX idx_audit_account ON accounts_audit(account_id, changed_at DESC);

5. Security Standards
5.1 Data Integrity Controls
-- Numeric, string format, and enum constraints
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%_@__%.__%'),
    phone TEXT CHECK(phone IS NULL OR phone GLOB '+[0-9]*'),
    status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending', 'active', 'deleted'))
);

-- Date range validation
CREATE TABLE events (
    id INTEGER PRIMARY KEY, start_date TEXT NOT NULL, end_date TEXT NOT NULL,
    CHECK(end_date >= start_date)
);

5.2 Soft Delete Pattern
CREATE TABLE documents (id INTEGER PRIMARY KEY, title TEXT NOT NULL, deleted_at TEXT);
CREATE VIEW active_documents AS SELECT * FROM documents WHERE deleted_at IS NULL;
CREATE INDEX idx_documents_active ON documents(title) WHERE deleted_at IS NULL;

6. Indexing Strategies
-- Single column for equality/range | Composite (equality first, then range)
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at DESC);

-- Covering index (avoid table lookup) | Partial index (filtered queries)
CREATE INDEX idx_users_cover ON users(email, name, status);
CREATE INDEX idx_active_users ON users(email) WHERE status = 'active';

-- Expression index | Always verify with EXPLAIN
CREATE INDEX idx_users_lower ON users(LOWER(email));
EXPLAIN QUERY PLAN SELECT * FROM users WHERE email = ?;

7. Implementation Workflow (TDD)
Step 1: Write Failing Tests First
# tests/test_schema.py
import pytest
import sqlite3

@pytest.fixture
def db():
    conn = sqlite3.connect(':memory:')
    conn.execute("PRAGMA foreign_keys = ON")
    yield conn
    conn.close()

class TestUserSchema:
    def test_email_uniqueness(self, db):
        db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT UNIQUE NOT NULL)")
        db.execute("INSERT INTO users (email) VALUES ('test@example.com')")
        with pytest.raises(sqlite3.IntegrityError):
            db.execute("INSERT INTO users (email) VALUES ('test@example.com')")

    def test_email_format_constraint(self, db):
        db.execute("""CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            email TEXT UNIQUE NOT NULL CHECK(email LIKE '%_@__%.__%'))""")
        with pytest.raises(sqlite3.IntegrityError):
            db.execute("INSERT INTO users (email) VALUES ('invalid')")

    def test_index_used_for_lookup(self, db):
        db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT)")
        db.execute("CREATE INDEX idx_users_email ON users(email)")
        plan = db.execute("EXPLAIN QUERY PLAN SELECT * FROM users WHERE email = ?", ('test@example.com',)).fetchone()
        assert 'USING INDEX' in plan[3]

Step 2: Implement Schema to Pass Tests
# src/database/schema.py
SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL CHECK(email LIKE '%_@__%.__%'),
    name TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
"""

def init_schema(conn):
    """Initialize database schema."""
    conn.executescript(SCHEMA_SQL)
    conn.commit()

Step 3: Run Tests and Verify
# Run schema tests
pytest tests/test_schema.py -v

# Run with coverage
pytest tests/test_schema.py --cov=src/database --cov-report=term-missing

Step 4: Test Migrations
# tests/test_migrations.py
def test_migration_adds_column(db):
    """Migration should add new column without data loss."""
    # Setup: create old schema with data
    db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT)")
    db.execute("INSERT INTO users (email) VALUES ('test@example.com')")

    # Run migration
    db.execute("ALTER TABLE users ADD COLUMN name TEXT DEFAULT 'Unknown'")

    # Verify: data preserved, new column exists
    row = db.execute("SELECT id, email, name FROM users").fetchone()
    assert row == (1, 'test@example.com', 'Unknown')

8. Performance Patterns
8.1 Indexing Strategies

Good: Composite index with correct column order

-- Query: WHERE user_id = ? AND created_at > ? ORDER BY created_at DESC
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at DESC);


Bad: Wrong column order wastes index

-- Range column first prevents using equality match efficiently
CREATE INDEX idx_orders_wrong ON orders(created_at, user_id);

8.2 Query Optimization

Good: Use covering index to avoid table lookup

-- Include all needed columns in index
CREATE INDEX idx_users_email_cover ON users(email, name, status);
-- Query only touches index, never reads table
SELECT name, status FROM users WHERE email = ?;


Bad: SELECT * with large rows

-- Forces table lookup even with index
SELECT * FROM users WHERE email = ?;

8.3 Connection Pooling

Good: Reuse connections with pool

from contextlib import contextmanager
import threading

class ConnectionPool:
    def __init__(self, db_path, max_connections=5):
        self._pool, self._lock = [], threading.Lock()
        self._db_path, self._max = db_path, max_connections

    @contextmanager
    def get_connection(self):
        conn = self._acquire()
        try:
            yield conn
        finally:
            self._release(conn)


Bad: Create new connection per query

def get_user(email):
    conn = sqlite3.connect('app.db')  # Expensive!
    result = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()
    return result

8.4 Denormalization Tradeoffs

Good: Store computed values for read-heavy patterns

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    item_count INTEGER NOT NULL DEFAULT 0,  -- Denormalized
    total_amount REAL NOT NULL DEFAULT 0    -- Denormalized
);
-- Use triggers to maintain denormalized values


Bad: Calculate aggregates on every read

SELECT o.id, COUNT(oi.id), SUM(oi.price * oi.quantity)
FROM orders o JOIN order_items oi ON oi.order_id = o.id GROUP BY o.id;

8.5 Partitioning Strategies

Good: Partition large tables by time

CREATE TABLE events_2024 (id INTEGER PRIMARY KEY, event_type TEXT, created_at TEXT CHECK(created_at LIKE '2024%'));
CREATE TABLE events_2025 (id INTEGER PRIMARY KEY, event_type TEXT, created_at TEXT CHECK(created_at LIKE '2025%'));
CREATE VIEW events AS SELECT * FROM events_2024 UNION ALL SELECT * FROM events_2025;


Bad: Single table with millions of rows (10M+ causes full table scans)

9. Common Mistakes & Anti-Patterns
Mistake	Bad	Good
Over-normalization	Separate tables for first_name, last_name	Store directly in users table
Missing FK	user_id INTEGER (no FK)	user_id INTEGER REFERENCES users(id)
Wrong index order	INDEX(created_at, user_id) for WHERE user_id=? AND created_at>?	INDEX(user_id, created_at)
CSV in column	tags TEXT -- "a,b,c"	Junction table with proper FK
10. Pre-Implementation Checklist
Phase 1: Before Writing Code
 Query patterns identified and documented
 Performance requirements defined (latency, throughput)
 Data volume estimates calculated
 Test fixtures designed for schema validation
 Migration strategy planned (if modifying existing schema)
 Reference files read (references/advanced-patterns.md, references/security-examples.md)
Phase 2: During Implementation
 All tables have PRIMARY KEY
 Foreign keys defined for all relationships
 Appropriate ON DELETE actions (CASCADE, RESTRICT, SET NULL)
 CHECK constraints for data validation
 UNIQUE constraints where needed
 NOT NULL for required fields
 Indexes created for all foreign keys
 Composite indexes with correct column order (equality before range)
 FTS5 tables with sync triggers if needed
 Tests written and passing for constraints
Phase 3: Before Committing
 pytest tests/test_schema.py -v passes
 EXPLAIN QUERY PLAN verified for critical queries
 No redundant indexes
 Migrations tested with rollback
 No data loss in migrations
 Performance benchmarks meet requirements
 Schema version tracked
11. Summary

Your goal is to create database schemas that are:

Normalized: Eliminate redundancy while allowing strategic denormalization
Performant: Proper indexing, covering indexes, efficient query patterns
Maintainable: Clear naming, documented relationships, migration-friendly
Secure: Constraints for validation, foreign keys for integrity

You understand that schema design requires balancing:

Normalization vs. query performance
Indexing benefits vs. write overhead
Flexibility vs. constraints
Current needs vs. future evolution

Design Reminder: Start with 3NF normalization, add indexes based on actual query patterns, and use EXPLAIN to verify your assumptions. When in doubt, consult references/advanced-patterns.md for complex relationship patterns.

Weekly Installs
–
Repository
martinholovsky/…enerator
GitHub Stars
37
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass