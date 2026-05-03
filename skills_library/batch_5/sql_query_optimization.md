---
title: sql-query-optimization
url: https://skills.sh/aj-geddes/useful-ai-prompts/sql-query-optimization
---

# sql-query-optimization

skills/aj-geddes/useful-ai-prompts/sql-query-optimization
sql-query-optimization
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill sql-query-optimization
SKILL.md
SQL Query Optimization
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Analyze SQL queries to identify performance bottlenecks and implement optimization techniques. Includes query analysis, indexing strategies, and rewriting patterns for improved performance.

When to Use
Slow query analysis and tuning
Query rewriting and refactoring
Index utilization verification
Join optimization
Subquery optimization
Query plan analysis (EXPLAIN)
Performance baseline establishment
Quick Start

PostgreSQL:

-- Analyze query plan with execution time
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON)
SELECT u.id, u.email, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at > NOW() - INTERVAL '1 year'
GROUP BY u.id, u.email;

-- Check table statistics
SELECT * FROM pg_stats
WHERE tablename = 'users' AND attname = 'created_at';

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Analyze Current Performance	Analyze Current Performance
Common Optimization Patterns	Common Optimization Patterns
Query Rewriting Techniques	Query Rewriting Techniques
Batch Operations	Batch Operations
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
317
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