---
title: drizzle-best-practices
url: https://skills.sh/honra-io/drizzle-best-practices/drizzle-best-practices
---

# drizzle-best-practices

skills/honra-io/drizzle-best-practices/drizzle-best-practices
drizzle-best-practices
Installation
$ npx skills add https://github.com/honra-io/drizzle-best-practices --skill drizzle-best-practices
SKILL.md
Drizzle ORM Best Practices (PostgreSQL)

Comprehensive best practices guide for Drizzle ORM with PostgreSQL. Contains guidance across 8 categories, prioritized by impact to help you write correct, performant, and maintainable database code.

When to Apply

Reference these guidelines when:

Defining table schemas with pgTable
Writing select, insert, update, or delete queries
Setting up relations between tables using defineRelations or the legacy relations API
Configuring drizzle-kit for migrations (generate, push, pull)
Inferring TypeScript types from your schema
Choosing between the SQL-like API and the relational query API
Optimizing query performance with prepared statements or batch operations
Integrating Drizzle with serverless Postgres providers (Neon, Supabase, etc.)
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Schema Design	CRITICAL	schema-
2	Query Patterns	CRITICAL	query-
3	Relations	HIGH	relations-
4	Migrations	HIGH	migrations-
5	Type Safety	MEDIUM-HIGH	types-
6	Performance	MEDIUM	perf-
7	Database Drivers	MEDIUM	driver-
8	Advanced Patterns	LOW	advanced-
How to Use

Read individual reference files for detailed explanations and code examples:

references/engine-postgres.md          # Postgres-specific types, features, and patterns
references/schema-table-definitions.md
references/query-select-patterns.md
references/relations-defining.md
references/_sections.md                # Full index of all references


Each reference file contains:

Brief explanation of why it matters
Incorrect code example with explanation
Correct code example with explanation
Links to official Drizzle documentation
References
https://orm.drizzle.team/docs/overview
https://orm.drizzle.team/docs/sql-schema-declaration
https://orm.drizzle.team/docs/relations-v2
https://orm.drizzle.team/docs/perf-queries
https://orm.drizzle.team/docs/kit-overview
https://orm.drizzle.team/llms.txt
Weekly Installs
108
Repository
honra-io/drizzl…ractices
GitHub Stars
7
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass