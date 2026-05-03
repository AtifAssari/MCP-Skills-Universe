---
rating: ⭐⭐⭐⭐⭐
title: database-optimization
url: https://skills.sh/89jobrien/steve/database-optimization
---

# database-optimization

skills/89jobrien/steve/database-optimization
database-optimization
Installation
$ npx skills add https://github.com/89jobrien/steve --skill database-optimization
SKILL.md
Database Optimization

This skill optimizes database performance including query optimization, indexing strategies, N+1 problem resolution, and caching implementation.

When to Use This Skill
When optimizing slow database queries
When fixing N+1 query problems
When designing indexes
When implementing caching strategies
When optimizing database migrations
When improving database performance
What This Skill Does
Query Optimization: Analyzes and optimizes SQL queries
Index Design: Creates appropriate indexes
N+1 Resolution: Fixes N+1 query problems
Caching: Implements caching layers (Redis, Memcached)
Migration Optimization: Optimizes database migrations
Performance Monitoring: Sets up query performance monitoring
How to Use
Optimize Queries
Optimize this slow database query

Fix the N+1 query problem in this code

Specific Analysis
Analyze query performance and suggest indexes

Optimization Areas
Query Optimization

Techniques:

Use EXPLAIN ANALYZE
Optimize JOINs
Reduce data scanned
Use appropriate indexes
Avoid SELECT *
Index Design

Strategies:

Index frequently queried columns
Composite indexes for multi-column queries
Avoid over-indexing
Monitor index usage
Remove unused indexes
N+1 Problem

Pattern:

# Bad: N+1 queries
users = User.all()
for user in users:
    posts = Post.where(user_id=user.id)  # N queries

# Good: Single query with JOIN
users = User.all().includes(:posts)  # 1 query

Examples
Example 1: Query Optimization

Input: Optimize slow user query

Output:

## Database Optimization: User Query

### Current Query
```sql
SELECT * FROM users
WHERE email = 'user@example.com';
-- Execution time: 450ms

Analysis
Full table scan (no index on email)
Scanning 1M+ rows
Optimization
-- Add index
CREATE INDEX idx_users_email ON users(email);

-- Optimized query
SELECT id, email, name FROM users
WHERE email = 'user@example.com';
-- Execution time: 2ms

Impact
Query time: 450ms → 2ms (99.5% improvement)
Index size: ~50MB

## Best Practices

### Database Optimization

1. **Measure First**: Use EXPLAIN ANALYZE
2. **Index Strategically**: Not every column needs an index
3. **Monitor**: Track slow query logs
4. **Cache**: Cache expensive queries
5. **Denormalize**: When justified by read patterns

## Reference Files

- **`references/query_patterns.md`** - Common query optimization patterns, anti-patterns, and caching strategies

## Related Use Cases

- Query optimization
- Index design
- N+1 problem resolution
- Caching implementation
- Database performance improvement

Weekly Installs
24
Repository
89jobrien/steve
GitHub Stars
4
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass