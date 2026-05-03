---
rating: ⭐⭐
title: csv-data-wrangler
url: https://skills.sh/404kidwiz/claude-supercode-skills/csv-data-wrangler
---

# csv-data-wrangler

skills/404kidwiz/claude-supercode-skills/csv-data-wrangler
csv-data-wrangler
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill csv-data-wrangler
SKILL.md
CSV Data Wrangler
Purpose

Provides expertise in efficient CSV file processing, data cleaning, and transformation. Handles large files, encoding issues, malformed data, and performance optimization for tabular data workflows.

When to Use
Processing large CSV files efficiently
Cleaning and validating CSV data
Transforming and reshaping datasets
Handling encoding and delimiter issues
Merging or splitting CSV files
Converting between tabular formats
Querying CSV with SQL (DuckDB)
Quick Start

Invoke this skill when:

Processing large CSV files efficiently
Cleaning and validating CSV data
Transforming and reshaping datasets
Handling encoding and delimiter issues
Querying CSV with SQL

Do NOT invoke when:

Building Excel files with formatting (use xlsx-skill)
Statistical analysis of data (use data-analyst)
Building data pipelines (use data-engineer)
Database operations (use sql-pro)
Decision Framework
Tool Selection by File Size:
├── < 100MB → pandas
├── 100MB - 1GB → pandas with chunking or polars
├── 1GB - 10GB → DuckDB or polars
├── > 10GB → DuckDB, Spark, or streaming
└── Quick exploration → csvkit or xsv CLI

Processing Type:
├── SQL-like queries → DuckDB
├── Complex transforms → pandas/polars
├── Simple filtering → csvkit/xsv
└── Streaming → Python csv module

Core Workflows
1. Large CSV Processing
Profile file (size, encoding, delimiter)
Choose appropriate tool for scale
Process in chunks if memory-constrained
Handle encoding issues (UTF-8, Latin-1)
Validate data types per column
Write output with proper quoting
2. Data Cleaning Pipeline
Load sample to understand structure
Identify missing and malformed values
Define cleaning rules per column
Apply transformations
Validate output quality
Log cleaning statistics
3. CSV Query with DuckDB
Point DuckDB at CSV file(s)
Let DuckDB infer schema
Write SQL queries directly
Export results to new CSV
Optionally persist as Parquet
Best Practices
Always specify encoding explicitly
Use chunked reading for large files
Profile before choosing tools
Preserve original files, write to new
Validate row counts before/after
Handle quoted fields and escapes properly
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
Loading all to memory	OOM on large files	Use chunking or streaming
Guessing encoding	Corrupted characters	Detect with chardet first
Ignoring quoting	Broken field parsing	Use proper CSV parser
No validation	Silent data corruption	Validate row/column counts
Manual string splitting	Breaks on edge cases	Use csv module or pandas
Weekly Installs
187
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass