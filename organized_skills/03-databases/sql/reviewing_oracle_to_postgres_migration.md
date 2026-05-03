---
rating: ⭐⭐
title: reviewing-oracle-to-postgres-migration
url: https://skills.sh/github/awesome-copilot/reviewing-oracle-to-postgres-migration
---

# reviewing-oracle-to-postgres-migration

skills/github/awesome-copilot/reviewing-oracle-to-postgres-migration
reviewing-oracle-to-postgres-migration
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill reviewing-oracle-to-postgres-migration
SKILL.md
Oracle-to-PostgreSQL Database Migration

Surfaces migration risks and validates migration work against known Oracle/PostgreSQL behavioral differences documented in the references/ folder.

When to use
Planning — Before starting migration work on a procedure, trigger, query, or refcursor client. Identify which reference insights apply so risks are addressed up front.
Validating — After migration work is done, confirm every applicable insight was addressed and integration tests cover the new PostgreSQL semantics.
Workflow

Determine the task type:

Planning a migration? Follow the risk assessment workflow. Validating completed work? Follow the validation workflow.

Risk assessment workflow (planning)
Risk Assessment:
- [ ] Step 1: Identify the migration scope
- [ ] Step 2: Screen each insight for applicability
- [ ] Step 3: Document risks and recommended actions


Step 1: Identify the migration scope

List the affected database objects (procedures, triggers, queries, views) and the application code that calls them.

Step 2: Screen each insight for applicability

Review the reference index in references/REFERENCE.md. For each entry, determine whether the migration scope contains patterns affected by that insight. Read the full reference file only when the insight is potentially relevant.

Step 3: Document risks and recommended actions

For each applicable insight, note the specific risk and the recommended fix pattern from the reference file. Flag any insight that requires a design decision (e.g., whether to preserve Oracle empty-string-as-NULL semantics or adopt PostgreSQL behavior).

Validation workflow (post-migration)
Validation:
- [ ] Step 1: Map the migration artifact
- [ ] Step 2: Cross-check applicable insights
- [ ] Step 3: Verify integration test coverage
- [ ] Step 4: Gate the result


Step 1: Map the migration artifact

Identify the migrated object and summarize the change set.

Step 2: Cross-check applicable insights

For each reference in references/REFERENCE.md, confirm the behavior or test requirement is acknowledged and addressed in the migration work.

Step 3: Verify integration test coverage

Confirm tests exercise both the happy path and the failure scenarios highlighted in applicable insights (exceptions, sorting, refcursor consumption, concurrent transactions, timestamps, etc.).

Step 4: Gate the result

Return a checklist asserting each applicable insight was addressed, migration scripts run, and integration tests pass.

Weekly Installs
1.5K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass