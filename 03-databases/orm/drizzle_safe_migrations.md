---
rating: ⭐⭐
title: drizzle-safe-migrations
url: https://skills.sh/pedronauck/skills/drizzle-safe-migrations
---

# drizzle-safe-migrations

skills/pedronauck/skills/drizzle-safe-migrations
drizzle-safe-migrations
Installation
$ npx skills add https://github.com/pedronauck/skills --skill drizzle-safe-migrations
SKILL.md
Drizzle Safe Migrations
Overview

Use this skill to run database migrations in a way that is auditable, deployment-safe, and consistent with Drizzle's migration model.

Core Rules
Always generate schema migrations with the project script (bun run db:generate).
Never hand-edit generated schema migration files.
Generate data backfills as custom migrations (bun run db:generate -- --custom --name <name>) and edit only that custom SQL file.
Apply data normalization before tightening constraints.
Keep one-off data fixes in migration history, not as hidden runtime logic, unless an emergency hotfix requires temporary mitigation.
Workflow
Classify the change:
schema-only: only column/table/index/default changes.
data+schema: old rows must be transformed before new constraints/defaults.
For data+schema, create custom migration first:
bun run db:generate -- --custom --name <descriptive_name>
Add idempotent backfill SQL.
Generate schema migration second:
bun run db:generate
Verify migration ordering in drizzle/meta/_journal.json:
backfill migration index must be lower than constraint-tightening migration index.
Verify generated SQL and snapshots:
backfill migration contains only intended data change.
schema migration contains constraint/default/type changes.
Run full backend verification:
bun run lint && bun run typecheck && bun run test
Document deployment notes:
expected data transformations,
lock-risk areas,
rollback strategy.
Backfill Requirements
Use restrictive WHERE clauses.
Prefer idempotent updates (UPDATE ... WHERE status = 'legacy_value').
Do not mix unrelated DDL/DML in the same migration.
Keep SQL explicit and minimal.
Constraint Tightening Pattern

When removing allowed values (enum/check):

Backfill existing rows to valid target value.
Update default to new value.
Tighten check/enum constraint.

For large tables or strict uptime targets, use staged PostgreSQL patterns (NOT VALID + VALIDATE CONSTRAINT) where applicable.

Anti-Patterns
Hand-editing generated schema migration files.
Tightening constraints before backfilling existing data.
Hiding one-time migration logic in app startup code without migration artifacts.
Running migrations without validating order in the Drizzle journal.
Reference
See references/production-playbook.md for command templates and review checklists.
Weekly Installs
78
Repository
pedronauck/skills
GitHub Stars
338
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass