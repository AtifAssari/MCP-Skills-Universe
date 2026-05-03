---
rating: ⭐⭐⭐
title: differential-fuzzer
url: https://skills.sh/tursodatabase/turso/differential-fuzzer
---

# differential-fuzzer

skills/tursodatabase/turso/differential-fuzzer
differential-fuzzer
Installation
$ npx skills add https://github.com/tursodatabase/turso --skill differential-fuzzer
Summary

Property-based fuzzer that compares Turso against SQLite to catch SQL correctness bugs.

Generates random SQL statements and schemas, then executes them on both Turso and SQLite to detect mismatches in row sets, error handling, or schema state
Supports deterministic reproduction via seed-based runs, configurable statement/table/column counts, and verbose output for debugging
Includes continuous loop mode for extended fuzzing campaigns and Docker runner for CI with configurable timeouts, GitHub issue auto-filing, and Slack notifications
Outputs detailed logs (test.sql, schema.json) and persists database files on demand for manual inspection and minimal reproducer creation
SKILL.md
Differential Fuzzer

Always load Debugging skill for reference

The differential fuzzer compares Turso results against SQLite for generated SQL statements to find correctness bugs.

Location

testing/differential-oracle/fuzzer/

Running the Fuzzer
Single Run
# Basic run (100 statements, random seed)
cargo run --bin differential_fuzzer

# With specific seed for reproducibility
cargo run --bin differential_fuzzer -- --seed 12345

# More statements with verbose output
cargo run --bin differential_fuzzer -- -n 1000 --verbose

# Keep database files after run (for debugging)
cargo run --bin differential_fuzzer -- --seed 12345 --keep-files

# All options
cargo run --bin differential_fuzzer -- \
  --seed <SEED>           # Deterministic seed
  -n <NUM>                # Number of statements (default: 100)
  -t <NUM>                # Number of tables (default: 2)
  -c <NUM>                # Columns per table (default: 5)
  --verbose               # Print each SQL statement
  --keep-files            # Persist .db files to disk

Continuous Fuzzing (Loop Mode)
# Run forever with random seeds
cargo run --bin differential_fuzzer -- loop

# Run 50 iterations
cargo run --bin differential_fuzzer -- loop 50

Docker Runner (CI/Production)
# Build and run from repo root
docker build -f testing/differential-oracle/fuzzer/docker-runner/Dockerfile -t fuzzer .
docker run -e GITHUB_TOKEN=xxx -e SLACK_WEBHOOK_URL=xxx fuzzer


Environment variables for docker-runner:

TIME_LIMIT_MINUTES - Total runtime (default: 1440 = 24h)
PER_RUN_TIMEOUT_SECONDS - Per-run timeout (default: 1200 = 20min)
NUM_STATEMENTS - Statements per run (default: 1000)
LOG_TO_STDOUT - Print fuzzer output (default: false)
GITHUB_TOKEN - For auto-filing issues
SLACK_WEBHOOK_URL - For notifications
Output Files

All output goes to simulator-output/ directory:

File	Description
test.sql	All executed SQL statements. Failed statements prefixed with -- FAILED:, errors with -- ERROR:
schema.json	Database schema at end of run (or at failure)
test.db	Turso database file (only with --keep-files)
test-sqlite.db	SQLite database file (only with --keep-files)
Reproducing Errors

Always follow these steps

Find the seed in the error output:

INFO: Starting differential_fuzzer with config: SimConfig { seed: 12345, ... }


Re-run with that seed:

cargo run --bin differential_fuzzer -- --seed 12345 --verbose --keep-files


Check output files:

simulator-output/test.sql - Find the failing statement (look for -- FAILED:)
simulator-output/schema.json - Check table structure at failure time

Create a minimal reproducer

Create reproducer in .sqltest or in .rs always load Debugging skill for reference

Compare behavior manually: If needed try to compare the behaviour and produce a report in the end. Always write to a tmp file first with Edit tool to test the sql and then pass it to the binaries.

# Run failing SQL against SQLite
sqlite3 :memory: < simulator-output/test.sql

# Run against tursodb CLI
tursodb :memory: < simulator-output/test.sql

Understanding Failures
Oracle Failure Types
Row set mismatch - Turso returned different rows than SQLite
Turso errored but SQLite succeeded - Turso rejected valid SQL
SQLite errored but Turso succeeded - Turso accepted invalid SQL
Schema mismatch - Tables/columns differ after DDL
Warning (non-fatal)
Unordered LIMIT mismatch - LIMIT without ORDER BY may return different valid rows
Key Source Files
File	Purpose
main.rs	CLI parsing, entry point
runner.rs	Main simulation loop, executes statements on both DBs
oracle.rs	Compares Turso vs SQLite results
schema.rs	Introspects schema from both databases
memory/	In-memory IO for deterministic simulation
Tracing

Set RUST_LOG for more detailed output:

RUST_LOG=debug cargo run --bin differential_fuzzer -- --seed 12345

Weekly Installs
527
Repository
tursodatabase/turso
GitHub Stars
18.4K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass