---
title: sqlite-ops
url: https://skills.sh/0xdarkmatter/claude-mods/sqlite-ops
---

# sqlite-ops

skills/0xdarkmatter/claude-mods/sqlite-ops
sqlite-ops
Installation
$ npx skills add https://github.com/0xdarkmatter/claude-mods --skill sqlite-ops
SKILL.md
SQLite Operations

Patterns for SQLite databases in Python projects.

Quick Connection
import sqlite3

def get_connection(db_path: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.row_factory = sqlite3.Row  # Dict-like access
    conn.execute("PRAGMA journal_mode=WAL")  # Better concurrency
    conn.execute("PRAGMA foreign_keys=ON")
    return conn

Context Manager Pattern
from contextlib import contextmanager

@contextmanager
def db_transaction(conn: sqlite3.Connection):
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise

WAL Mode

Enable for concurrent read/write:

conn.execute("PRAGMA journal_mode=WAL")

Mode	Reads	Writes	Best For
DELETE (default)	Blocked during write	Single	Simple scripts
WAL	Concurrent	Single	Web apps, MCP servers
Common Gotchas
Issue	Solution
"database is locked"	Use WAL mode
Slow queries	Add indexes, check EXPLAIN QUERY PLAN
Thread safety	Use check_same_thread=False
FK not enforced	Run PRAGMA foreign_keys=ON
CLI Quick Reference
sqlite3 mydb.sqlite    # Open database
.tables                # Show tables
.schema items          # Show schema
.headers on && .mode csv && .output data.csv  # Export CSV
VACUUM;                # Reclaim space

When to Use
Local state/config storage
Caching layer
Event logging
MCP server persistence
Small to medium datasets
Additional Resources

For detailed patterns, load:

./references/schema-patterns.md - State, cache, event, queue table designs
./references/async-patterns.md - aiosqlite CRUD, batching, connection pools
./references/migration-patterns.md - Version migrations, JSON handling
Weekly Installs
47
Repository
0xdarkmatter/claude-mods
GitHub Stars
17
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass