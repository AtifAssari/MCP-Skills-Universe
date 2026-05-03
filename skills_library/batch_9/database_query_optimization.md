---
title: database-query-optimization
url: https://skills.sh/aj-geddes/useful-ai-prompts/database-query-optimization
---

# database-query-optimization

skills/aj-geddes/useful-ai-prompts/database-query-optimization
database-query-optimization
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill database-query-optimization
SKILL.md
Database Query Optimization
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Slow database queries are a common performance bottleneck. Optimization through indexing, efficient queries, and caching dramatically improves application performance.

When to Use
Slow response times
High database CPU usage
Performance regression
New feature deployment
Regular maintenance
Quick Start

Minimal working example:

-- Analyze query performance

EXPLAIN ANALYZE
SELECT users.id, users.name, COUNT(orders.id) as order_count
FROM users
LEFT JOIN orders ON users.id = orders.user_id
WHERE users.created_at > '2024-01-01'
GROUP BY users.id, users.name
ORDER BY order_count DESC;

-- Results show:
-- - Seq Scan (slow) vs Index Scan (fast)
-- - Rows: actual vs planned (high variance = bad)
-- - Execution time (milliseconds)

-- Key metrics:
-- - Sequential Scan: Full table read (slow)
-- - Index Scan: Uses index (fast)
-- - Nested Loop: Joins with loops
-- - Sort: In-memory or disk sort

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Query Analysis	Query Analysis
Indexing Strategy	Indexing Strategy
Query Optimization Techniques	Query Optimization Techniques
Optimization Checklist	Optimization Checklist
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
356
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