---
title: transaction-correctness
url: https://skills.sh/tursodatabase/turso/transaction-correctness
---

# transaction-correctness

skills/tursodatabase/turso/transaction-correctness
transaction-correctness
Installation
$ npx skills add https://github.com/tursodatabase/turso --skill transaction-correctness
Summary

WAL mechanics, checkpointing, concurrency, and recovery in Turso's SQLite implementation.

Turso uses WAL (Write-Ahead Logging) exclusively with in-memory WAL index instead of SQLite's shared memory file, supporting one writer and concurrent readers without blocking
Checkpointing transfers WAL pages back to the main database in four modes: PASSIVE (non-blocking), FULL (waits for readers), RESTART (resets WAL), and TRUNCATE (truncates WAL file)
Each connection maintains private page cache, dirty pages, and snapshot view; shared state includes frame cache, read lock slots, write lock, and checkpoint lock across all connections
Recovery replays valid commits from WAL on crash; durability, atomicity, isolation, and no-lost-updates invariants enforced through fsync on COMMIT and checkpoint coordination
SKILL.md
Transaction Correctness Guide

Turso uses WAL (Write-Ahead Logging) mode exclusively.

Files: .db, .db-wal (no .db-shm - Turso uses in-memory WAL index)

WAL Mechanics
Write Path
Writer appends frames (page data) to WAL file (sequential I/O)
COMMIT = frame with non-zero db_size in header (marks transaction end)
Original DB unchanged until checkpoint
Read Path
Reader acquires read mark (mxFrame = last valid commit frame)
For each page: check WAL up to mxFrame, fall back to main DB
Reader sees consistent snapshot at its read mark
Checkpointing

Transfers WAL content back to main DB.

WAL grows → checkpoint triggered (default: 1000 pages) → pages copied to DB → WAL reused


Checkpoint types:

PASSIVE: Non-blocking, stops at pages needed by active readers
FULL: Waits for readers, checkpoints everything
RESTART: Like FULL, also resets WAL to beginning
TRUNCATE: Like RESTART, also truncates WAL file to zero length
WAL-Index

SQLite uses a shared memory file (-shm) for WAL index. Turso does not - it uses in-memory data structures (frame_cache hashmap, atomic read marks) since multi-process access is not supported.

Concurrency Rules
One writer at a time
Readers don't block writer, writer doesn't block readers
Checkpoint must stop at pages needed by active readers
Recovery

On crash:

First connection acquires exclusive lock
Replays valid commits from WAL
Releases lock, normal operation resumes
Turso Implementation

Key files:

WAL implementation - WAL implementation
Page management, transactions
Connection-Private vs Shared

Per-Connection (private):

Pager - page cache, dirty pages, savepoints, commit state
WalFile - connection's snapshot view:
max_frame / min_frame - frame range for this connection's snapshot
max_frame_read_lock_index - which read lock slot this connection holds
last_checksum - rolling checksum state

Shared across connections:

WalFileShared - global WAL state:
frame_cache - page-to-frame index (replaces .shm file)
max_frame / nbackfills - global WAL progress
read_locks[5] - read mark slots (TursoRwLock with embedded frame values)
write_lock - exclusive writer lock
checkpoint_lock - checkpoint serialization
file - WAL file handle
DatabaseStorage - main .db file
BufferPool - shared memory allocation
Correctness Invariants
Durability: COMMIT record must be fsynced before returning success
Atomicity: Partial transactions never visible to readers
Isolation: Each reader sees consistent snapshot
No lost updates: Checkpoint can't overwrite uncommitted changes
References
SQLite WAL
WAL File Format
Weekly Installs
536
Repository
tursodatabase/turso
GitHub Stars
18.4K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass