---
title: grdb
url: https://skills.sh/johnrogers/claude-swift-engineering/grdb
---

# grdb

skills/johnrogers/claude-swift-engineering/grdb
grdb
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill grdb
SKILL.md
GRDB

Direct SQLite access using GRDB.swift - type-safe Swift wrapper with full SQLite power when you need it.

Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
Getting Started	Setting up DatabaseQueue or DatabasePool
Queries	Writing raw SQL, Record types, type-safe queries
Value Observation	Reactive queries, SwiftUI integration
Migrations	DatabaseMigrator, schema evolution
Performance	EXPLAIN QUERY PLAN, indexing, profiling
When to Use GRDB vs SQLiteData
Scenario	Use
Type-safe @Table models	SQLiteData
CloudKit sync needed	SQLiteData
Complex joins (4+ tables)	GRDB
Window functions (ROW_NUMBER, RANK)	GRDB
Performance-critical raw SQL	GRDB
Reactive queries (ValueObservation)	GRDB
Core Workflow
Choose DatabaseQueue (single connection) or DatabasePool (concurrent reads)
Define migrations with DatabaseMigrator
Create Record types (Codable, FetchableRecord, PersistableRecord)
Write queries with raw SQL or QueryInterface
Use ValueObservation for reactive updates
Requirements
iOS 13+, macOS 10.15+
Swift 5.7+
GRDB.swift 6.0+
Common Mistakes

Performance assumptions without EXPLAIN PLAN — Assuming your query is fast or slow without checking EXPLAIN QUERY PLAN is guessing. Always profile queries with EXPLAIN before optimizing.

Missing indexes on WHERE clauses — Queries filtering on non-indexed columns scan the entire table. Index any column used in WHERE, JOIN, or ORDER BY clauses for large tables.

Improper migration ordering — Running migrations out of order or skipping intermediate versions breaks schema consistency. Always apply migrations sequentially; never jump versions.

Record conformance shortcuts — Not conforming Record types to PersistableRecord or FetchableRecord correctly leads to silent data loss or deserialization failures. Always implement all required protocols correctly.

ValueObservation without proper cleanup — Forgetting to cancel ValueObservation when views disappear causes memory leaks and stale data subscriptions. Store the cancellable and clean up in deinit.

Weekly Installs
91
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass