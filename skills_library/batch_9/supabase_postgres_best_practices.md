---
title: supabase-postgres-best-practices
url: https://skills.sh/supabase/agent-skills/supabase-postgres-best-practices
---

# supabase-postgres-best-practices

skills/supabase/agent-skills/supabase-postgres-best-practices
supabase-postgres-best-practices
Installation
$ npx skills add https://github.com/supabase/agent-skills --skill supabase-postgres-best-practices
Summary

Postgres performance optimization rules across 8 priority categories, from query tuning to advanced features.

Organized into 8 rule categories prioritized by impact: query performance and connection management (critical), security and RLS, schema design, concurrency, data access patterns, monitoring, and advanced features
Each rule includes detailed explanations, incorrect vs. correct SQL examples, EXPLAIN output analysis, and performance metrics to guide optimization decisions
Covers query indexing, connection pooling, Row-Level Security configuration, schema design patterns, locking behavior, and Postgres-specific tuning
Designed for use during SQL writing, schema design, performance reviews, and database scaling decisions
SKILL.md
Supabase Postgres Best Practices

Comprehensive performance optimization guide for Postgres, maintained by Supabase. Contains rules across 8 categories, prioritized by impact to guide automated query optimization and schema design.

When to Apply

Reference these guidelines when:

Writing SQL queries or designing schemas
Implementing indexes or query optimization
Reviewing database performance issues
Configuring connection pooling or scaling
Optimizing for Postgres-specific features
Working with Row-Level Security (RLS)
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Query Performance	CRITICAL	query-
2	Connection Management	CRITICAL	conn-
3	Security & RLS	CRITICAL	security-
4	Schema Design	HIGH	schema-
5	Concurrency & Locking	MEDIUM-HIGH	lock-
6	Data Access Patterns	MEDIUM	data-
7	Monitoring & Diagnostics	LOW-MEDIUM	monitor-
8	Advanced Features	LOW	advanced-
How to Use

Read individual rule files for detailed explanations and SQL examples:

references/query-missing-indexes.md
references/query-partial-indexes.md
references/_sections.md


Each rule file contains:

Brief explanation of why it matters
Incorrect SQL example with explanation
Correct SQL example with explanation
Optional EXPLAIN output or metrics
Additional context and references
Supabase-specific notes (when applicable)
References
https://www.postgresql.org/docs/current/
https://supabase.com/docs
https://wiki.postgresql.org/wiki/Performance_Optimization
https://supabase.com/docs/guides/database/overview
https://supabase.com/docs/guides/auth/row-level-security
Weekly Installs
138.1K
Repository
supabase/agent-skills
GitHub Stars
2.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass