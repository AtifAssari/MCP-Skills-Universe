---
title: debugging
url: https://skills.sh/tursodatabase/turso/debugging
---

# debugging

skills/tursodatabase/turso/debugging
debugging
Installation
$ npx skills add https://github.com/tursodatabase/turso --skill debugging
Summary

Debugging tools for Turso database using bytecode comparison, logging, and deterministic simulation.

Bytecode comparison workflow identifies whether behavior differences stem from code generation bugs or VM/storage layer issues by comparing SQLite and Turso EXPLAIN output
Logging via RUST_LOG environment variable captures detailed traces from turso_core and simulator components during test runs
ThreadSanitizer stress tests detect threading issues across configurable thread counts and iteration counts
Deterministic simulation with seed-based reproduction allows consistent bug recreation in both the simulator and concurrent DST (Whopper) environments
Corruption analysis tools available in scripts directory for diagnosing WAL corruption and database integrity problems
SKILL.md
Debugging Guide
Bytecode Comparison Flow

Turso aims for SQLite compatibility. When behavior differs:

1. EXPLAIN query in sqlite3
2. EXPLAIN query in tursodb
3. Compare bytecode
   ├─ Different → bug in code generation
   └─ Same but results differ → bug in VM or storage layer

Example
# SQLite
sqlite3 :memory: "EXPLAIN SELECT 1 + 1;"

# Turso
cargo run --bin tursodb :memory: "EXPLAIN SELECT 1 + 1;"

Manual Query Inspection
cargo run --bin tursodb :memory: 'SELECT * FROM foo;'
cargo run --bin tursodb :memory: 'EXPLAIN SELECT * FROM foo;'

Logging
# Trace core during tests
RUST_LOG=none,turso_core=trace make test

# Output goes to testing/test.log
# Warning: can be megabytes per test run

Threading Issues

Use stress tests with ThreadSanitizer:

rustup toolchain install nightly
rustup override set nightly
cargo run -Zbuild-std --target x86_64-unknown-linux-gnu \
  -p turso_stress -- --vfs syscall --nr-threads 4 --nr-iterations 1000

Deterministic Simulation

Reproduce bugs with seed. Note: simulator uses legacy "limbo" naming.

# Simulator
RUST_LOG=limbo_sim=debug cargo run --bin limbo_sim -- -s <seed>

# Whopper (concurrent DST)
SEED=1234 ./testing/concurrent-simulator/bin/run

Architecture Reference
Parser → AST from SQL strings
Code generator → bytecode from AST
Virtual machine → executes SQLite-compatible bytecode
Storage layer → B-tree operations, paging
Corruption Debugging

For WAL corruption and database integrity issues, use the corruption debug tools in scripts.

See references/CORRUPTION-TOOLS.md for detailed usage.

Weekly Installs
578
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