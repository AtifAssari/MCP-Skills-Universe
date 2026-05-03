---
rating: ⭐⭐
title: sqlalchemy-code-review
url: https://skills.sh/existential-birds/beagle/sqlalchemy-code-review
---

# sqlalchemy-code-review

skills/existential-birds/beagle/sqlalchemy-code-review
sqlalchemy-code-review
Installation
$ npx skills add https://github.com/existential-birds/beagle --skill sqlalchemy-code-review
SKILL.md
SQLAlchemy Code Review
Quick Reference
Issue Type	Reference
Session lifecycle, context managers, async sessions	references/sessions.md
relationship(), lazy loading, N+1, joinedload	references/relationships.md
select() vs query(), ORM overhead, bulk ops	references/queries.md
Alembic patterns, reversible migrations, data migrations	references/migrations.md
Review Checklist
 Sessions use context managers (with, async with)
 No session sharing across requests or threads
 Sessions closed/cleaned up properly
 relationship() uses appropriate lazy strategy
 Explicit joinedload/selectinload to avoid N+1
 No lazy loading in loops (N+1 queries)
 Using SQLAlchemy 2.0 select() syntax, not legacy query()
 Bulk operations use bulk_insert/bulk_update, not ORM loops
 Async sessions use proper async context managers
 Migrations are reversible with downgrade()
 Data migrations use op.execute() not ORM models
 Migration dependencies properly ordered
When to Load References
Reviewing session creation/cleanup → sessions.md
Reviewing model relationships → relationships.md
Reviewing database queries → queries.md
Reviewing Alembic migration files → migrations.md
Review Questions
Are all sessions properly managed with context managers?
Are relationships configured to avoid N+1 queries?
Are queries using SQLAlchemy 2.0 select() syntax?
Are all migrations reversible and properly tested?
Weekly Installs
115
Repository
existential-birds/beagle
GitHub Stars
56
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass