---
rating: ⭐⭐
title: turso
url: https://skills.sh/itechmeat/llm-code/turso
---

# turso

skills/itechmeat/llm-code/turso
turso
Installation
$ npx skills add https://github.com/itechmeat/llm-code --skill turso
SKILL.md
Turso Database

SQLite-compatible embedded database for modern applications, AI agents, and edge computing.

Links
Documentation
Changelog
GitHub
Quick Navigation
Topic	Reference
Installation	installation.md
Encryption	encryption.md
Authorization	auth.md
Sync	sync.md
Agent DBs	agents.md
When to Use
Embedded SQLite database with cloud sync
AI agent state management and multi-agent coordination
Offline-first applications
Encrypted databases (AEGIS, AES-GCM)
Edge computing and IoT devices
Core Concepts
libSQL

Turso is built on libSQL, an open-source fork of SQLite with:

Native encryption (AEGIS-256, AES-GCM)
Async I/O (Linux io_uring)
Cloud sync capabilities
Deployment Options
Embedded — runs locally in your app
Turso Cloud — managed platform with branching, backups
Hybrid — local with cloud sync (push/pull)
Common Patterns
Encrypted Database
openssl rand -hex 32  # Generate key
tursodb --experimental-encryption "file:db.db?cipher=aegis256&hexkey=YOUR_KEY"

Cloud Sync
import { connect } from "@tursodatabase/sync";

const db = await connect({
  path: "./local.db",
  url: "libsql://...",
  authToken: process.env.TURSO_AUTH_TOKEN,
});

await db.push(); // local → cloud
await db.pull(); // cloud → local

Agent Database
import { connect } from "@tursodatabase/database";

// Local-first
const db = await connect("agent.db");

// Or with sync
const db = await connect({
  path: "agent.db",
  url: "https://db.turso.io",
  authToken: "...",
  sync: "full",
});

Version

Based on product version: 0.5.3

Links
Documentation
Changelog
GitHub
Weekly Installs
46
Repository
itechmeat/llm-code
GitHub Stars
15
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail