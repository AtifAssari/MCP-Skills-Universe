---
title: redis-development
url: https://skills.sh/redis/agent-skills/redis-development
---

# redis-development

skills/redis/agent-skills/redis-development
redis-development
Installation
$ npx skills add https://github.com/redis/agent-skills --skill redis-development
Summary

Redis performance optimization across data structures, query engines, vector search, and semantic caching.

Covers 29 prioritized rules across 11 categories including data modeling, memory management, Redis Query Engine (RQE), vector search with RedisVL, and LangCache semantic caching
Provides structured guidance for connection pooling, JSON document handling, streams, clustering, security (ACLs), and observability
Each rule includes explanations, correct examples, anti-patterns or usage guidance, and additional context for implementation
Organized by impact level (HIGH/MEDIUM) to help prioritize optimization efforts in automated code generation and performance tuning
SKILL.md
Redis Best Practices

Comprehensive performance optimization guide for Redis, including Redis Query Engine, vector search, and semantic caching. Contains 29 rules across 11 categories, prioritized by impact to guide automated optimization and code generation.

When to Apply

Reference these guidelines when:

Designing Redis data models and key structures
Implementing caching, sessions, or real-time features
Using Redis Query Engine (FT.CREATE, FT.SEARCH, FT.AGGREGATE)
Building vector search or RAG applications with RedisVL
Implementing semantic caching with LangCache
Optimizing Redis performance and memory usage
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Data Structures & Keys	HIGH	data-
2	Memory & Expiration	HIGH	ram-
3	Connection & Performance	HIGH	conn-
4	JSON Documents	MEDIUM	json-
5	Redis Query Engine	HIGH	rqe-
6	Vector Search & RedisVL	HIGH	vector-
7	Semantic Caching	MEDIUM	semantic-cache-
8	Streams & Pub/Sub	MEDIUM	stream-
9	Clustering & Replication	MEDIUM	cluster-
10	Security	HIGH	security-
11	Observability	MEDIUM	observe-
Quick Reference
1. Data Structures & Keys (HIGH)
data-choose-structure - Choose the Right Data Structure
data-key-naming - Use Consistent Key Naming Conventions
2. Memory & Expiration (HIGH)
ram-limits - Configure Memory Limits and Eviction Policies
ram-ttl - Set TTL on Cache Keys
3. Connection & Performance (HIGH)
conn-blocking - Avoid Slow Commands in Production
conn-pipelining - Use Pipelining for Bulk Operations
conn-pooling - Use Connection Pooling or Multiplexing
conn-timeouts - Configure Connection Timeouts
4. JSON Documents (MEDIUM)
json-partial-updates - Use JSON Paths for Partial Updates
json-vs-hash - Choose JSON vs Hash Appropriately
5. Redis Query Engine (HIGH)
rqe-dialect - Use DIALECT 2 for Query Syntax
rqe-field-types - Choose the Correct Field Type
rqe-index-creation - Index Only Fields You Query
rqe-index-management - Manage Indexes for Zero-Downtime Updates
rqe-query-optimization - Write Efficient Queries
6. Vector Search & RedisVL (HIGH)
vector-algorithm-choice - Choose HNSW vs FLAT Based on Requirements
vector-hybrid-search - Use Hybrid Search for Better Results
vector-index-creation - Configure Vector Indexes Properly
vector-rag-pattern - Implement RAG Pattern Correctly
7. Semantic Caching (MEDIUM)
semantic-cache-best-practices - Configure Semantic Cache Properly
semantic-cache-langcache-usage - Use LangCache for LLM Response Caching
8. Streams & Pub/Sub (MEDIUM)
stream-choosing-pattern - Choose Streams vs Pub/Sub Appropriately
9. Clustering & Replication (MEDIUM)
cluster-hash-tags - Use Hash Tags for Multi-Key Operations
cluster-read-replicas - Use Read Replicas for Read-Heavy Workloads
10. Security (HIGH)
security-acls - Use ACLs for Fine-Grained Access Control
security-auth - Always Use Authentication in Production
security-network - Secure Network Access
11. Observability (MEDIUM)
observe-commands - Use Observability Commands for Debugging
observe-metrics - Monitor Key Redis Metrics
How to Use

Read individual rule files for detailed explanations and code examples:

rules/rqe-index-creation.md
rules/vector-rag-pattern.md


Each rule file contains:

Brief explanation of why it matters
Correct example(s) with explanation
Either an "Incorrect" example (for anti-patterns that cause real harm) or "When to use / When NOT needed" guidance (for optional features)
Additional context and references
Full Compiled Document

For the complete guide with all rules expanded: AGENTS.md

Weekly Installs
2.4K
Repository
redis/agent-skills
GitHub Stars
47
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass