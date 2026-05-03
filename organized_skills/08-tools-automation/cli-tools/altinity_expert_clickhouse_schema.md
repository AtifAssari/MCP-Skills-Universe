---
rating: ⭐⭐
title: altinity-expert-clickhouse-schema
url: https://skills.sh/altinity/skills/altinity-expert-clickhouse-schema
---

# altinity-expert-clickhouse-schema

skills/altinity/skills/altinity-expert-clickhouse-schema
altinity-expert-clickhouse-schema
Installation
$ npx skills add https://github.com/altinity/skills --skill altinity-expert-clickhouse-schema
SKILL.md
Table Schema and Design Analysis

Analyze table structure, partitioning, ORDER BY, materialized views, and identify design anti-patterns.

Diagnostics

Run all queries from the file checks.sql and analyze the results.

Deep Dive Queries (Placeholder-Based)
Partition Distribution for Specific Table
select
    database,
    table,
    count() as partitions,
    sum(rows) as total_rows,
    formatReadableSize(sum(bytes_on_disk)) as total_size,
    formatReadableSize(median(bytes_on_disk)) as median_partition_size,
    min(partition) as oldest_partition,
    max(partition) as newest_partition
from system.parts
where active and database = '{database}' and table = '{table}'
group by database, table, partition
order by partition desc
limit 100

Column Compression Analysis for Specific Table
select
    name,
    type,
    formatReadableSize(data_compressed_bytes) as compressed,
    formatReadableSize(data_uncompressed_bytes) as uncompressed,
    round(data_uncompressed_bytes / nullIf(data_compressed_bytes, 0), 2) as ratio,
    compression_codec
from system.columns
where database = '{database}' and table = '{table}'
order by data_compressed_bytes desc
limit 50


Look for:

Columns with ratio < 2 → consider better codec or data transformation
Large columns without codec → add CODEC(ZSTD) or LZ4HC
String columns with low cardinality → consider LowCardinality(String)
Index Usage Analysis for Specific Database
select
    database,
    table,
    name as index_name,
    type,
    expr,
    granularity
from system.data_skipping_indices
where database = '{database}'
order by database, table

Schema Design Recommendations
Partition Key Guidelines
Data Volume	Recommended Granularity	Example
< 10GB/month	No partitioning or yearly	toYear(ts)
10-100GB/month	Monthly	toYYYYMM(ts)
100GB-1TB/month	Weekly or daily	toMonday(ts)
> 1TB/month	Daily	toDate(ts)
ORDER BY Guidelines
First column: Low cardinality, frequently filtered (e.g., tenant_id, region)
Second column: Time-based if range queries common
Subsequent: Other filter columns by selectivity (most selective last)

Anti-patterns:

UUID/hash as first column
High-cardinality ID without tenant prefix
DateTime64 with microseconds as first column
Compression Codec Recommendations
Data Type	Recommended Codec
Integers (sequential)	Delta, ZSTD
Integers (random)	ZSTD or LZ4HC
Floats	Gorilla, ZSTD
Timestamps	DoubleDelta, ZSTD
Strings (long)	ZSTD(3)
Strings (repetitive)	LowCardinality + ZSTD
Cross-Module Triggers
Finding	Load Module	Reason
Many small partitions	altinity-expert-clickhouse-ingestion	Check batch sizing
Oversized partitions	altinity-expert-clickhouse-merges	Merge can't complete
High PK memory	altinity-expert-clickhouse-memory	Memory pressure
MV performance issues	altinity-expert-clickhouse-reporting	Query analysis
Too many parts per partition	altinity-expert-clickhouse-merges	Merge backlog
Settings Reference
Setting	Default	Recommendation
index_granularity	8192	Lower for point lookups, higher for scans
ttl_only_drop_parts	0	Set to 1 if TTL deletes entire partitions
min_bytes_for_wide_part	10MB	Increase if many small parts
Weekly Installs
63
Repository
altinity/skills
GitHub Stars
5
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass