---
title: database-design-patterns
url: https://skills.sh/nickcrew/claude-ctx-plugin/database-design-patterns
---

# database-design-patterns

skills/nickcrew/claude-ctx-plugin/database-design-patterns
database-design-patterns
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill database-design-patterns
SKILL.md
Database Design Patterns

Expert guidance for designing scalable database schemas, optimizing query performance, and implementing robust data persistence layers across relational and NoSQL databases.

When to Use This Skill
Designing database schemas for new applications
Optimizing slow queries and database performance
Choosing between normalization and denormalization strategies
Implementing partitioning, sharding, or replication strategies
Migrating between database technologies (SQL to NoSQL or vice versa)
Designing for high availability and disaster recovery
Implementing caching strategies and read replicas
Scaling databases horizontally or vertically
Ensuring data consistency in distributed systems
Core Concepts
Data Modeling

Design schemas that reflect business domain, access patterns, and consistency requirements. Balance normalization (data integrity) with denormalization (read performance) based on workload characteristics.

ACID vs. BASE
ACID (Relational): Atomicity, Consistency, Isolation, Durability - strong guarantees
BASE (NoSQL): Basically Available, Soft state, Eventually consistent - flexibility
CAP Theorem

Distributed systems choose two of three: Consistency, Availability, Partition Tolerance.

Polyglot Persistence

Use the right database for each use case: PostgreSQL for transactions, MongoDB for documents, Redis for caching, Elasticsearch for search, Cassandra for time-series, Neo4j for graphs.

Quick Reference
Task	Load reference
Core database principles (ACID, BASE, CAP)	skills/database-design-patterns/references/core-principles.md
Schema patterns (normalization, star schema, documents)	skills/database-design-patterns/references/schema-design-patterns.md
Index types and strategies (B-tree, hash, covering)	skills/database-design-patterns/references/indexing-strategies.md
Partitioning and sharding approaches	skills/database-design-patterns/references/partitioning-patterns.md
Replication modes (primary-replica, multi-leader)	skills/database-design-patterns/references/replication-patterns.md
Query optimization and caching	skills/database-design-patterns/references/query-optimization.md
Workflow
Phase 1: Requirements Analysis
Identify access patterns (read-heavy vs. write-heavy)
Determine consistency requirements (strong vs. eventual)
Estimate data volume and growth rate
Define SLA requirements (latency, availability)
Phase 2: Schema Design
Model entities and relationships
Choose normalization level based on workload
Design for query patterns, not just storage
Consider data distribution strategy (partitioning/sharding)
Phase 3: Performance Optimization
Analyze query execution plans (EXPLAIN ANALYZE)
Add indexes for frequent queries
Implement caching where appropriate
Configure connection pooling
Monitor and iterate
Phase 4: Scaling Strategy
Implement read replicas for read scaling
Consider partitioning for large tables (>100M rows)
Plan sharding strategy for horizontal scaling
Design for high availability with replication
Common Mistakes

Over-normalization: Too many joins slow down reads. Denormalize for read-heavy workloads.

Missing indexes: Analyze query patterns and add indexes for frequent WHERE/JOIN columns.

Wrong index type: Use composite indexes with correct column order (equality first, then range).

Ignoring replication lag: Handle eventual consistency with read-your-writes pattern.

Poor partitioning key: Choose keys that distribute data evenly and align with query patterns.

N+1 queries: Use JOINs or batch loading instead of querying in loops.

Inefficient pagination: Use keyset pagination instead of OFFSET for large datasets.

Connection exhaustion: Implement connection pooling sized for your workload.

Best Practices
Model for access patterns - Design schemas around how data will be queried
Index strategically - Index frequently queried columns, avoid over-indexing
Partition large tables - Use for tables >100M rows or time-series data
Replicate for reads - Primary-replica for read scaling, multi-leader for geo-distribution
Optimize queries - Analyze execution plans, avoid N+1, use proper pagination
Cache hot data - Application-level caching with appropriate TTLs
Pool connections - Size connection pools based on workload
Monitor continuously - Track query performance, index usage, replication lag
Plan for growth - Design for 3x current load
Choose consistency wisely - Match consistency level to business requirements
Resources

Books:

"Designing Data-Intensive Applications" (Kleppmann)
"High Performance MySQL" (Schwartz)

Sites:

use-the-index-luke.com
PostgreSQL documentation
MongoDB documentation

Tools:

EXPLAIN ANALYZE
pg_stat_statements
Percona Toolkit
pt-query-digest
Weekly Installs
46
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass