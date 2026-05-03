---
rating: ⭐⭐
title: android-room-database
url: https://skills.sh/krutikjain/android-agent-skills/android-room-database
---

# android-room-database

skills/krutikjain/android-agent-skills/android-room-database
android-room-database
Installation
$ npx skills add https://github.com/krutikjain/android-agent-skills --skill android-room-database
SKILL.md
Android Room Database
When To Use
Use this skill when the request is about: room database android, dao query migration android, room schema export.
Primary outcome: Model Room entities, DAOs, transactions, migrations, schema exports, and test-safe local persistence.
Reach for this skill when the hard part is schema design, DAO queries, transactions, migrations, or Room testing. Hand off to android-rxjava-to-coroutines-migration only if the main work is reactive API migration rather than the database contract itself.
Handoff skills when the scope expands:
android-local-persistence-datastore
android-testing-unit
Workflow
Start with the persistence contract: entities, keys, indexes, relations, and whether the data is source-of-truth, cache, or offline-first state.
Model DAO access patterns explicitly, including transaction boundaries, query shape, paging, and invalidation behavior.
Plan schema evolution before changing entities: exported schemas, migration steps, auto-migration eligibility, and destructive-fallback policy.
Validate migration and query behavior with deterministic tests rather than assuming Room annotations are enough.
Hand off DataStore, sync, or reactive API questions only after the Room boundary is correct.
Guardrails
Export schemas and treat them as part of the contract, not optional tooling noise.
Keep entities persistence-focused; map to domain/UI models instead of leaking table shape upward.
Use explicit transactions for multi-step writes that must remain consistent.
Test migrations against real old schemas before trusting them in release builds.
Anti-Patterns
Treating Room entities as the app's domain model everywhere.
Editing schemas without exporting or validating migration paths.
Writing broad SELECT * queries when the screen only needs a narrow projection.
Collapsing database, sync, and reactive-stream migration problems into one undifferentiated task.
Review Focus
Entity keys, indexes, relations, and schema ownership.
DAO query shape, transactions, and invalidation behavior.
Migration safety, schema exports, and test coverage.
Clear boundaries between Room models and higher-level app models.
Examples
Happy path
Scenario: Persist task items and reminder flags with schema-aware entities.
Command: cd examples/orbittasks-compose && ./gradlew :app:testDebugUnitTest
Edge case
Scenario: Recover from a failed schema change with an explicit migration path.
Command: python3 scripts/eval_triggers.py --skill android-room-database
Failure recovery
Scenario: Keep Room requests separate from DataStore, networking, and modernization prompts.
Command: cd examples/orbittasks-xml && ./gradlew :app:testDebugUnitTest
Done Checklist
Entities, DAOs, and transactions match the real persistence contract.
Schema export and migration strategy are explicit.
Query and migration tests cover the risky paths.
Non-Room concerns are handed off instead of mixed into the database task.
Official References
https://developer.android.com/training/data-storage/room
https://developer.android.com/training/data-storage/room/migrating-db-versions
https://developer.android.com/training/data-storage/room/accessing-data
https://developer.android.com/training/data-storage/room/prepopulate
https://developer.android.com/topic/performance/sqlite-performance-best-practices
Weekly Installs
19
Repository
krutikjain/andr…t-skills
GitHub Stars
5
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass