---
rating: ⭐⭐
title: database-design
url: https://skills.sh/sickn33/antigravity-awesome-skills/database-design
---

# database-design

skills/sickn33/antigravity-awesome-skills/database-design
database-design
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill database-design
Summary

Structured guidance for database selection, schema design, and query optimization decisions.

Covers six core areas: database selection (PostgreSQL, Neon, Turso, SQLite), ORM choice (Drizzle, Prisma, Kysely), schema normalization, indexing strategy, query optimization, and safe migrations
Emphasizes context-driven decision-making rather than defaulting to PostgreSQL; includes a checklist for schema design prerequisites
Highlights common anti-patterns: unnecessary PostgreSQL adoption, missing indexes, SELECT * in production, JSON overuse, and N+1 queries
Organized as a modular reference with a content map directing you to relevant files based on your specific task
SKILL.md
Database Design

Learn to THINK, not copy SQL patterns.

🎯 Selective Reading Rule

Read ONLY files relevant to the request! Check the content map, find what you need.

File	Description	When to Read
database-selection.md	PostgreSQL vs Neon vs Turso vs SQLite	Choosing database
orm-selection.md	Drizzle vs Prisma vs Kysely	Choosing ORM
schema-design.md	Normalization, PKs, relationships	Designing schema
indexing.md	Index types, composite indexes	Performance tuning
optimization.md	N+1, EXPLAIN ANALYZE	Query optimization
migrations.md	Safe migrations, serverless DBs	Schema changes
⚠️ Core Principle
ASK user for database preferences when unclear
Choose database/ORM based on CONTEXT
Don't default to PostgreSQL for everything
Decision Checklist

Before designing schema:

 Asked user about database preference?
 Chosen database for THIS context?
 Considered deployment environment?
 Planned index strategy?
 Defined relationship types?
Anti-Patterns

❌ Default to PostgreSQL for simple apps (SQLite may suffice) ❌ Skip indexing ❌ Use SELECT * in production ❌ Store JSON when structured data is better ❌ Ignore N+1 queries

When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
1.2K
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass