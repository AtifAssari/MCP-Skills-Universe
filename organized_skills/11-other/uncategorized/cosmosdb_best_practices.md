---
rating: ⭐⭐
title: cosmosdb-best-practices
url: https://skills.sh/azurecosmosdb/cosmosdb-agent-kit/cosmosdb-best-practices
---

# cosmosdb-best-practices

skills/azurecosmosdb/cosmosdb-agent-kit/cosmosdb-best-practices
cosmosdb-best-practices
Originally frommicrosoft/vscode-cosmosdb
Installation
$ npx skills add https://github.com/azurecosmosdb/cosmosdb-agent-kit --skill cosmosdb-best-practices
SKILL.md
Azure Cosmos DB Best Practices

Comprehensive performance optimization guide for Azure Cosmos DB applications, containing 75+ rules across 11 categories, prioritized by impact to guide automated refactoring and code generation.

When to Apply

Reference these guidelines when:

Designing data models for Cosmos DB
Choosing partition keys
Writing or optimizing queries
Implementing SDK patterns
Using the Cosmos DB Emulator for local development
Inspecting or managing Cosmos DB data with developer tooling
Implementing vector search or RAG features on Cosmos DB
Reviewing code for performance issues
Configuring throughput and scaling
Building globally distributed applications
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Data Modeling	CRITICAL	model-
2	Partition Key Design	CRITICAL	partition-
3	Query Optimization	HIGH	query-
4	SDK Best Practices	HIGH	sdk-
5	Indexing Strategies	MEDIUM-HIGH	index-
6	Throughput & Scaling	MEDIUM	throughput-
7	Global Distribution	MEDIUM	global-
8	Monitoring & Diagnostics	LOW-MEDIUM	monitoring-
9	Design Patterns	HIGH	pattern-
10	Developer Tooling	MEDIUM	tooling-
11	Vector Search	HIGH	vector-
Quick Reference
1. Data Modeling (CRITICAL)
model-embed-related - Embed related data retrieved together
model-reference-large - Reference data when items get too large
model-avoid-2mb-limit - Keep items well under 2MB limit
model-id-constraints - Follow ID value length and character constraints
model-nesting-depth - Stay within 128-level nesting depth limit
model-numeric-precision - Understand IEEE 754 numeric precision limits
model-denormalize-reads - Denormalize for read-heavy workloads including pre-computed aggregates
model-schema-versioning - Version your document schemas
model-type-discriminator - Use type discriminators for polymorphic data
model-json-serialization - Handle JSON serialization correctly for Cosmos DB documents
model-relationship-references - Use ID references with transient hydration for document relationships
2. Partition Key Design (CRITICAL)
partition-high-cardinality - Choose high-cardinality partition keys
partition-avoid-hotspots - Distribute writes evenly
partition-hierarchical - Use hierarchical partition keys for flexibility; order levels broad→narrow
partition-query-patterns - Align partition key with query patterns
partition-synthetic-keys - Create synthetic keys when needed
partition-key-length - Respect partition key value length limits
partition-immutable-key - Choose immutable properties as partition keys
partition-20gb-limit - Plan for 20GB logical partition limit
3. Query Optimization (HIGH)
query-aggregate-single-pass - Compute min/max/avg with one scoped aggregate query
query-avoid-cross-partition - Minimize cross-partition queries
query-use-projections - Project only needed fields; prefer dedicated result types for projections
query-pagination - Use continuation tokens for pagination
query-avoid-scans - Avoid full container scans
query-parameterize - Use parameterized queries
query-order-filters - Order filters by selectivity
query-top-literal - Use literal integers for TOP, never parameters
query-latest-by-timestamp - Query "latest" documents with explicit ORDER BY and TOP 1
query-olap-detection - Detect and redirect analytical queries away from transactional containers
query-point-reads - Use point reads (ReadItem) instead of queries when id and partition key are known
4. SDK Best Practices (HIGH)
sdk-singleton-client - Reuse CosmosClient as singleton
sdk-async-api - Use async APIs for throughput
sdk-retry-429 - Handle 429s with retry-after
sdk-connection-mode - Use Direct mode for production
sdk-preferred-regions - Configure preferred regions
sdk-excluded-regions - Exclude regions experiencing issues
sdk-availability-strategy - Configure availability strategy for resilience
sdk-circuit-breaker - Use circuit breaker for fault tolerance
sdk-diagnostics - Log diagnostics for troubleshooting
sdk-serialization-enums - Serialize enums as strings not integers
sdk-emulator-ssl - Configure SSL and connection mode for Cosmos DB Emulator
sdk-ifnonematch-create - Use setIfNoneMatchETag("*") on createItem to reject duplicates atomically (409 on conflict)
sdk-no-shared-request-options - Never reuse a CosmosItemRequestOptions instance across multiple createItem calls — SDK mutates it internally, causing wrong partition key on second call
sdk-patch-incr - Use CosmosPatchOperations.incr() for atomic counter increments — no read RU, no ETag conflict cycle
sdk-bypage-empty-token - Guard against empty-string continuation tokens before calling byPage() — pass null for first page, never ""
sdk-etag-concurrency - Use ETags for optimistic concurrency on read-modify-write operations
sdk-java-content-response - Enable content response on write operations (Java)
sdk-java-cosmos-config - Configure Cosmos DB initialization correctly in Spring Boot
sdk-java-spring-boot-versions - Match Java version to Spring Boot requirements
sdk-local-dev-config - Configure local development to avoid cloud conflicts
sdk-newtonsoft-dependency - Explicitly reference Newtonsoft.Json package
sdk-python-async-deps - Include aiohttp when using Python async SDK
sdk-spring-data-annotations - Annotate entities for Spring Data Cosmos
sdk-spring-data-repository - Use CosmosRepository correctly and handle Iterable return types
5. Indexing Strategies (MEDIUM-HIGH)
index-exclude-unused - Exclude paths never queried
index-composite - Use composite indexes for ORDER BY
index-composite-direction - Match composite index directions to ORDER BY
index-spatial - Add spatial indexes for geo queries
index-range-vs-hash - Choose appropriate index types
index-lazy-consistent - Understand indexing modes
6. Throughput & Scaling (MEDIUM)
throughput-autoscale - Use autoscale for variable workloads
throughput-right-size - Right-size provisioned throughput
throughput-serverless - Consider serverless for dev/test
throughput-burst - Understand burst capacity
throughput-container-vs-database - Choose allocation level wisely
7. Global Distribution (MEDIUM)
global-multi-region - Configure multi-region writes
global-consistency - Choose appropriate consistency level
global-conflict-resolution - Implement conflict resolution
global-failover - Configure automatic failover
global-read-regions - Add read regions near users
global-zone-redundancy - Enable zone redundancy for HA
8. Monitoring & Diagnostics (LOW-MEDIUM)
monitoring-ru-consumption - Track RU consumption
monitoring-latency - Monitor P99 latency
monitoring-throttling - Alert on throttling
monitoring-azure-monitor - Integrate Azure Monitor
monitoring-diagnostic-logs - Enable diagnostic logging
9. Design Patterns (HIGH)
pattern-change-feed-materialized-views - Use Change Feed for cross-partition query optimization
pattern-efficient-ranking - Use count-based or cached approaches for efficient ranking
pattern-service-layer-relationships - Use a service layer to hydrate document references
10. Developer Tooling (MEDIUM)
tooling-vscode-extension - Use the VS Code extension for routine inspection and management
tooling-emulator-setup - Use the Emulator for local development and testing
11. Vector Search (HIGH)
vector-enable-feature - Enable vector search on the account before using vector features
vector-embedding-policy - Define vector embedding policy for vector properties
vector-index-type - Configure vector indexes in the indexing policy
vector-normalize-embeddings - Normalize embeddings for cosine similarity
vector-distance-query - Use VectorDistance for similarity search
vector-repository-pattern - Implement a repository pattern for vector search
12. Full-Text Search (HIGH)
fts-enable-capability - Enable EnableNoSQLFullTextSearch capability on the account — prerequisite for all FTS functions
fts-full-text-policy - Define fullTextPolicy on the container with correct language code (en-US, case-sensitive)
fts-index-policy - Add fullTextIndexes entry in the indexing policy to build the inverted index
fts-contains-query - Use FullTextContains / FullTextContainsAll / FullTextContainsAny instead of CONTAINS(LOWER(...))
fts-score-ranking - Use ORDER BY RANK FullTextScore(path, term) for BM25 relevance ranking
fts-hybrid-query - Combine FTS predicates with range/equality filters; put most selective filter first
How to Use

Use the linked rule files above for detailed explanations and code examples. The links give the agent direct paths to the relevant guidance instead of relying on folder scanning or inferred filenames.

Each rule file contains:

Brief explanation of why it matters
Incorrect code example with explanation
Correct code example with explanation
Additional context and references
Full Compiled Document

For the complete guide with all rules expanded: AGENTS.md

Weekly Installs
346
Repository
azurecosmosdb/c…gent-kit
GitHub Stars
26
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass