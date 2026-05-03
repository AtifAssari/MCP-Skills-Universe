---
rating: ⭐⭐
title: supabase-postgres-best-practices
url: https://skills.sh/davila7/claude-code-templates/supabase-postgres-best-practices
---

# supabase-postgres-best-practices

skills/davila7/claude-code-templates/supabase-postgres-best-practices
supabase-postgres-best-practices
Originally fromsupabase/agent-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill supabase-postgres-best-practices
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

rules/query-missing-indexes.md
rules/schema-partial-indexes.md
rules/_sections.md


Each rule file contains:

Brief explanation of why it matters
Incorrect SQL example with explanation
Correct SQL example with explanation
Optional EXPLAIN output or metrics
Additional context and references
Supabase-specific notes (when applicable)
Full Compiled Document

For the complete guide with all rules expanded: AGENTS.md

Weekly Installs
373
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass