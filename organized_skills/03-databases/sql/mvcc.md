---
rating: ⭐⭐⭐
title: mvcc
url: https://skills.sh/tursodatabase/turso/mvcc
---

# mvcc

skills/tursodatabase/turso/mvcc
mvcc
Installation
$ npx skills add https://github.com/tursodatabase/turso --skill mvcc
Summary

Experimental multi-version concurrency control with row-level snapshot isolation for SQLite-compatible databases.

Enables per-transaction snapshot isolation where readers and writers don't block each other; enabled via PRAGMA journal_mode = 'mvcc' on a per-database basis
Tracks row versions with begin/end timestamps and uses a logical log (.db-log) instead of WAL for persistence; includes configurable checkpointing via PRAGMA mvcc_checkpoint_threshold
Architecture uses lock-free SkipMap structures for row versions and transactions, with per-connection transaction tracking and a shared MvStore
Current limitations: garbage collection not implemented, no recovery from logical log on restart, checkpointing blocks all transactions, and memory use concerns without disk spilling
Provides snapshot isolation only, not serializability; marked work-in-progress and not production-ready
SKILL.md
MVCC Guide (Experimental)

Multi-Version Concurrency Control. Work in progress, not production-ready.

CRITICAL: Ignore MVCC when debugging unless the bug is MVCC-specific.

Enabling MVCC
PRAGMA journal_mode = 'mvcc';


Runtime configuration, not a compile-time feature flag. Per-database setting.

How It Works

Standard WAL: single version per page, readers see snapshot at read mark time.

MVCC: multiple row versions, snapshot isolation. Each transaction sees consistent snapshot at begin time.

Key Differences from WAL
Aspect	WAL	MVCC
Write granularity	Every commit writes full pages	Affected rows only
Readers/Writers	Don't block each other	Don't block each other
Persistence	.db-wal	.db-log (logical log)
Isolation	Snapshot (page-level)	Snapshot (row-level)
Versioning

Each row version tracks:

begin - timestamp when visible
end - timestamp when deleted/replaced
btree_resident - existed before MVCC enabled
Architecture
Database
  └─ mv_store: MvStore
      ├─ rows: SkipMap<RowID, Vec<RowVersion>>
      ├─ txs: SkipMap<TxID, Transaction>
      ├─ Storage (.db-log file)
      └─ CheckpointStateMachine


Per-connection: mv_tx tracks current MVCC transaction.

Shared: MvStore with lock-free crossbeam_skiplist structures.

Key Files
core/mvcc/mod.rs - Module overview
core/mvcc/database/mod.rs - Main implementation (~3000 lines)
core/mvcc/cursor.rs - Merged MVCC + B-tree cursor
core/mvcc/persistent_storage/logical_log.rs - Disk format
core/mvcc/database/checkpoint_state_machine.rs - Checkpoint logic
Checkpointing

Flushes row versions to B-tree periodically.

PRAGMA mvcc_checkpoint_threshold = <pages>;


Process: acquire lock → begin pager txn → write rows → commit → truncate log → fsync → release.

Current Limitations

Not implemented:

Garbage collection (old versions accumulate)
Recovery from logical log on restart

Known issues:

Checkpoint blocks other transactions, even reads!
No spilling to disk; memory use concerns
Testing
# Run MVCC-specific tests
cargo test mvcc

# TCL tests with MVCC
make test-mvcc


Use #[turso_macros::test(mvcc)] attribute for MVCC-enabled tests.

#[turso_macros::test(mvcc)]
fn test_something() {
    // runs with MVCC enabled
}

References
core/mvcc/mod.rs documents data anomalies (dirty reads, lost updates, etc.)
Snapshot isolation vs serializability: MVCC provides the former, not the latter
Weekly Installs
528
Repository
tursodatabase/turso
GitHub Stars
18.4K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass