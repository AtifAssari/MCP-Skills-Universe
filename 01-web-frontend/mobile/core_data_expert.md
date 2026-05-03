---
rating: ⭐⭐
title: core-data-expert
url: https://skills.sh/avdlee/core-data-agent-skill/core-data-expert
---

# core-data-expert

skills/avdlee/core-data-agent-skill/core-data-expert
core-data-expert
Installation
$ npx skills add https://github.com/avdlee/core-data-agent-skill --skill core-data-expert
Summary

Expert Core Data guidance for iOS/macOS stack setup, migrations, threading, and CloudKit sync.

Covers stack initialization, fetch requests, NSFetchedResultsController, saving patterns, and merge conflict resolution across all Core Data store types
Provides threading best practices for both traditional perform/performAndWait patterns and Swift Concurrency with actors and Sendable types
Includes batch operations, persistent history tracking, lightweight and staged migrations, and performance profiling strategies
Addresses NSPersistentCloudKitContainer integration, schema immutability in production, and cross-context object communication via NSManagedObjectID
Offers rapid triage templates and error-to-reference routing for common crashes and configuration issues
SKILL.md
Core Data Expert

Fast, production-oriented guidance for building correct, performant Core Data stacks and fixing common crashes.

Agent behavior contract (follow these rules)
Determine OS/deployment target when advice depends on availability (iOS 14+/17+ features, etc.).
Identify the context type before proposing fixes: view context (UI) vs background context (heavy work).
Recommend NSManagedObjectID for cross-context/cross-task communication; never pass NSManagedObject instances across contexts.
Prefer lightweight migration when possible; use staged migration (iOS 17+) for complex changes.
When recommending batch operations, verify persistent history tracking is enabled (often required for UI updates).
For CloudKit integration, remind developers that Production schema is immutable.
Reference WWDC/external resources sparingly; prefer this skill’s references/.
First 60 seconds (triage template)
Clarify the goal: setup, bugfix, migration, performance, CloudKit?
Collect minimal facts:
platform + deployment target
store type (SQLite / in-memory) and whether CloudKit is enabled
context involved (view vs background) and whether Swift Concurrency is in use
exact error message + stack trace/logs
Branch immediately:
threading/crash → focus on context confinement + NSManagedObjectID handoff
migration error → identify model versions + migration strategy
batch ops not updating UI → persistent history tracking + merge pipeline
Routing map (pick the right reference fast)
Stack setup / merge policies / contexts → references/stack-setup.md
Saving patterns → references/saving.md
Fetch requests / list updates / aggregates → references/fetch-requests.md
Traditional threading (perform/performAndWait, object IDs) → references/threading.md
Swift Concurrency (async/await, actors, Sendable, DAOs) → references/concurrency.md
Batch insert/delete/update → references/batch-operations.md
Persistent history tracking + “batch ops not updating UI” → references/persistent-history.md
Model configuration (constraints, validation, derived/composite, transformables) → references/model-configuration.md
Schema migration (lightweight/staged/deferred) → references/migration.md
CloudKit integration & debugging → references/cloudkit-integration.md
Performance profiling & memory → references/performance.md
Testing patterns → references/testing.md
Terminology → references/glossary.md
Common errors → next best move
“Failed to find a unique match for an NSEntityDescription” → references/testing.md (shared NSManagedObjectModel)
NSPersistentStoreIncompatibleVersionHashError → references/migration.md (versioning + migration)
Cross-context/threading exceptions (e.g. delete/update from wrong context) → references/threading.md and/or references/concurrency.md (use NSManagedObjectID)
Sendable / actor-isolation warnings around Core Data → references/concurrency.md (don’t “paper over” with @unchecked Sendable)
NSMergeConflict / constraint violations → references/model-configuration.md + references/stack-setup.md (constraints + merge policy)
Batch operations not updating UI → references/persistent-history.md + references/batch-operations.md
CloudKit schema/sync issues → references/cloudkit-integration.md
Memory grows during fetch → references/performance.md + references/fetch-requests.md
Verification checklist (when changing Core Data code)
Confirm the context matches the work (UI vs background).
Ensure NSManagedObject instances never cross contexts; pass NSManagedObjectID instead.
If using batch ops, confirm persistent history tracking + merge pipeline.
If using constraints, confirm merge policy and conflict resolution strategy.
If performance-related, profile with Instruments and validate fetch batching/limits.
Reference files
references/_index.md (navigation)
references/stack-setup.md
references/saving.md
references/fetch-requests.md
references/threading.md
references/concurrency.md
references/batch-operations.md
references/persistent-history.md
references/model-configuration.md
references/migration.md
references/cloudkit-integration.md
references/performance.md
references/testing.md
references/glossary.md
Weekly Installs
1.4K
Repository
avdlee/core-dat…nt-skill
GitHub Stars
251
First Seen
Jan 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass