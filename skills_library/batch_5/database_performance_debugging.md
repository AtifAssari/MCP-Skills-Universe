---
title: database-performance-debugging
url: https://skills.sh/aj-geddes/useful-ai-prompts/database-performance-debugging
---

# database-performance-debugging

skills/aj-geddes/useful-ai-prompts/database-performance-debugging
database-performance-debugging
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill database-performance-debugging
SKILL.md
Database Performance Debugging
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Database performance issues directly impact application responsiveness. Debugging focuses on identifying slow queries and optimizing execution plans.

When to Use
Slow application response times
High database CPU
Slow queries identified
Performance regression
Under load stress
Quick Start

Minimal working example:

-- Enable slow query log (MySQL)
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 0.5;

-- View slow queries
SHOW GLOBAL STATUS LIKE 'Slow_queries';
SELECT * FROM mysql.slow_log;

-- PostgreSQL slow queries
CREATE EXTENSION pg_stat_statements;
SELECT mean_exec_time, calls, query
FROM pg_stat_statements
ORDER BY mean_exec_time DESC LIMIT 10;

-- SQL Server slow queries
SELECT TOP 10
  execution_count,
  total_elapsed_time,
  statement_text
FROM sys.dm_exec_query_stats
ORDER BY total_elapsed_time DESC;

-- Query profiling
EXPLAIN ANALYZE
SELECT * FROM orders WHERE user_id = 123;
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Identify Slow Queries	Identify Slow Queries
Common Issues & Solutions	Common Issues & Solutions
Execution Plan Analysis	Execution Plan Analysis
Debugging Process	Debugging Process
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
305
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass