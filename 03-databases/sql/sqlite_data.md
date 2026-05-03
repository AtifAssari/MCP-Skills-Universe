---
rating: ⭐⭐
title: sqlite-data
url: https://skills.sh/johnrogers/claude-swift-engineering/sqlite-data
---

# sqlite-data

skills/johnrogers/claude-swift-engineering/sqlite-data
sqlite-data
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill sqlite-data
SKILL.md
SQLite Data

SQLiteData provides type-safe SQLite access through Swift macros, simplifying database modeling and queries while handling CloudKit sync, migrations, and async patterns automatically.

Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
Table Models	Defining tables with @Table, setting up primary keys, columns, or enums
Queries - Basics	Using @FetchAll, @FetchOne, @Selection, filtering, ordering, or joins
Queries - Advanced	Using @Fetch with FetchKeyRequest, dynamic queries, recursive CTEs, or direct reads
Writes	Inserting, updating, upserting, deleting records, or managing transactions
Views - SwiftUI	Using @FetchAll/@FetchOne in SwiftUI views, @Observable models, or animations
Views - Integration	UIKit integration, dynamic query loading, TCA integration, or observe {}
Migrations	Creating database migrations with DatabaseMigrator or #sql() macro
CloudKit Sync	Setting up CloudKit private database sync, sharing, or sync delegates
Dependencies	Injecting database/sync engine via @Dependency, bootstrap patterns, or TCA integration
Testing	Setting up test databases, seeding data, or writing assertions for SQLite code
Advanced - Queries	Implementing triggers, custom database functions, or full-text search (FTS5)
Advanced - Optimization	Performance tuning, indexes, custom aggregates, JSON aggregation, or self-joins
Schema Composition	Using @Selection column groups, single-table inheritance, or database views
Core Workflow

When working with SQLiteData:

Define table models with @Table macro
Use @FetchAll/@FetchOne property wrappers in views or @Observable models
Access database via @Dependency(\.defaultDatabase)
Perform writes in database.write { } transactions
Set up migrations before first use
Common Mistakes

N+1 query patterns — Loading records one-by-one in a loop (e.g., fetching user then fetching all their posts separately) kills performance. Use joins or batch fetches instead.

Missing migrations on schema changes — Modifying @Table without creating a migration causes crashes at runtime. Always create migrations for schema changes before deploying.

Improper transaction handling — Long-running transactions outside of database.write { } block can cause deadlocks or data loss. Keep write blocks short and focused.

Ignoring CloudKit sync delegates — Setting up CloudKit sync without implementing SyncDelegate means you miss error handling and conflict resolution. Implement all delegate methods for production.

Over-fetching in SwiftUI views — Using @FetchAll without filtering/limiting can load thousands of records, freezing the UI. Use predicates, limits, and sorting to keep in-memory footprint small.

Weekly Installs
114
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