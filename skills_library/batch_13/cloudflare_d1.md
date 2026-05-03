---
title: cloudflare-d1
url: https://skills.sh/secondsky/claude-skills/cloudflare-d1
---

# cloudflare-d1

skills/secondsky/claude-skills/cloudflare-d1
cloudflare-d1
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill cloudflare-d1
SKILL.md
Cloudflare D1 Database

Status: Production Ready ✅ | Last Verified: 2025-01-15

Table of Contents
What Is D1?
Quick Start
Critical Rules
D1 API Methods
Top 5 Use Cases
Migrations Best Practices
Common Patterns
SQLite Type Affinity
Top 5 Errors Prevented
What Is D1?

Cloudflare D1 is serverless SQLite on the edge:

SQL database without servers
Global distribution
Zero cold starts
Standard SQLite syntax
Read replication for global performance
🆕 New in 2025

D1 received major updates throughout 2025:

Performance (January 2025)
40-60% latency reduction globally (P50 query times)
Optimized SQLite engine for edge execution
Reduced cold start impact for databases <100 MB
Reliability (September 2025)
Automatic query retries: Read queries retry up to 2x on transient failures
Transparent to application code (logged in wrangler tail)
Scalability (April 2025)
Read Replication (Public Beta): Deploy read replicas globally
Up to 2x read throughput for read-heavy workloads
Sessions API for read-write separation
Compliance (November 2025)
Data Localization: Specify EU/US jurisdiction for GDPR/data sovereignty
Configure via --jurisdiction flag or wrangler.jsonc
⚠️ Breaking Change (February 10, 2025)
Free tier hard limits enforced: 10 DBs, 500 MB each, 50 queries/invocation
Exceeding limits = 429 errors (previously warnings only)
Action: Review usage with wrangler d1 list and upgrade if needed

Full details: Load references/2025-features.md

Quick Start (5 Minutes)
1. Create Database
bunx wrangler d1 create my-database


Save the database_id from output!

2. Configure Binding

Add to wrangler.jsonc:

{
  "name": "my-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-10-11",
  "d1_databases": [
    {
      "binding": "DB",                    // env.DB
      "database_name": "my-database",
      "database_id": "<UUID>",
      "preview_database_id": "local-db"
    }
  ]
}

3. Create Migration
bunx wrangler d1 migrations create my-database create_users


Edit migrations/0001_create_users.sql:

CREATE TABLE IF NOT EXISTS users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL UNIQUE,
  username TEXT NOT NULL,
  created_at INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);

PRAGMA optimize;

4. Apply Migration
# Local
bunx wrangler d1 migrations apply my-database --local

# Production
bunx wrangler d1 migrations apply my-database --remote

5. Query from Worker
import { Hono } from 'hono';

type Bindings = {
  DB: D1Database;
};

const app = new Hono<{ Bindings: Bindings }>();

app.get('/users/:email', async (c) => {
  const { results } = await c.env.DB.prepare(
    'SELECT * FROM users WHERE email = ?'
  )
    .bind(c.req.param('email'))
    .all();

  return c.json(results);
});

export default app;


Load references/setup-guide.md for complete walkthrough.

Critical Rules
Always Do ✅
Use prepared statements with .bind() (never string concatenation)
Create indexes for WHERE/JOIN/ORDER BY columns
Use migrations for schema changes (never manual SQL)
Batch queries for multiple operations (.batch())
Run PRAGMA optimize after schema changes
Handle errors explicitly (try/catch)
Use INTEGER for timestamps (Date.now())
Test locally before deploying migrations
Use read replicas for global read performance
Validate input before SQL queries
Never Do ❌
Never concatenate user input into SQL
Never commit database_id to public repos
Never skip migrations for schema changes
Never use VARCHAR (use TEXT instead)
Never skip indexes for filtered columns
Never ignore SQLite type affinity rules
**Never use SELECT *** without LIMIT
Never run migrations without testing locally
Never exceed 1MB per row
Never use DATETIME (use INTEGER for timestamps)
D1 API Methods
prepare() - Execute Queries
// Single result
const { results } = await env.DB.prepare(
  'SELECT * FROM users WHERE email = ?'
)
  .bind(email)
  .all();

// First result only
const user = await env.DB.prepare(
  'SELECT * FROM users WHERE user_id = ?'
)
  .bind(userId)
  .first();

// Raw results (faster)
const { results } = await env.DB.prepare(
  'SELECT username FROM users'
)
  .raw();  // Returns arrays instead of objects

batch() - Multiple Queries
const results = await env.DB.batch([
  env.DB.prepare('INSERT INTO users (email, username, created_at) VALUES (?, ?, ?)')
    .bind('user1@example.com', 'user1', Date.now()),
  env.DB.prepare('INSERT INTO users (email, username, created_at) VALUES (?, ?, ?)')
    .bind('user2@example.com', 'user2', Date.now()),
  env.DB.prepare('SELECT COUNT(*) as count FROM users')
]);

console.log('Users count:', results[2].results[0].count);


All queries execute in single transaction (all succeed or all fail).

exec() - Run SQL String
// For migrations/setup only
await env.DB.exec(`
  CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    email TEXT NOT NULL
  );
  CREATE INDEX idx_email ON users(email);
`);


NEVER use for queries with user input!

Load references/query-patterns.md for complete API reference.

Top 5 Use Cases
Use Case 1: User CRUD
// Create
app.post('/users', async (c) => {
  const { email, username } = await c.req.json();

  const { results } = await c.env.DB.prepare(
    'INSERT INTO users (email, username, created_at) VALUES (?, ?, ?) RETURNING *'
  )
    .bind(email, username, Date.now())
    .all();

  return c.json(results[0]);
});

// Read
app.get('/users/:id', async (c) => {
  const user = await c.env.DB.prepare(
    'SELECT * FROM users WHERE user_id = ?'
  )
    .bind(c.req.param('id'))
    .first();

  if (!user) {
    return c.json({ error: 'Not found' }, 404);
  }

  return c.json(user);
});

// Update
app.patch('/users/:id', async (c) => {
  const { username } = await c.req.json();

  await c.env.DB.prepare(
    'UPDATE users SET username = ?, updated_at = ? WHERE user_id = ?'
  )
    .bind(username, Date.now(), c.req.param('id'))
    .run();

  return c.json({ success: true });
});

// Delete
app.delete('/users/:id', async (c) => {
  await c.env.DB.prepare(
    'DELETE FROM users WHERE user_id = ?'
  )
    .bind(c.req.param('id'))
    .run();

  return c.json({ success: true });
});

Use Case 2: Batch Operations
app.post('/users/bulk', async (c) => {
  const users = await c.req.json();  // Array of users

  const statements = users.map(user =>
    c.env.DB.prepare(
      'INSERT INTO users (email, username, created_at) VALUES (?, ?, ?)'
    ).bind(user.email, user.username, Date.now())
  );

  const results = await c.env.DB.batch(statements);

  return c.json({ inserted: results.length });
});

Use Case 3: Read Replication (Global Reads)
// Configure read replica (any region)
const session = c.env.DB.withSession({
  preferredRegion: 'auto'  // or 'weur', 'wnam', 'enam', 'apac'
});

// Read from nearest replica
const { results } = await session.prepare(
  'SELECT * FROM users WHERE email = ?'
)
  .bind(email)
  .all();

// Check which region served request
console.log('Served by:', results[0].served_by_region);


Load references/read-replication.md for complete guide.

Use Case 4: Transactions with Batch
// Transfer credits between users (atomic)
const results = await c.env.DB.batch([
  c.env.DB.prepare(
    'UPDATE users SET credits = credits - ? WHERE user_id = ?'
  ).bind(amount, fromUserId),
  c.env.DB.prepare(
    'UPDATE users SET credits = credits + ? WHERE user_id = ?'
  ).bind(amount, toUserId),
  c.env.DB.prepare(
    'INSERT INTO transactions (from_user, to_user, amount, created_at) VALUES (?, ?, ?, ?)'
  ).bind(fromUserId, toUserId, amount, Date.now())
]);

// All succeed or all fail (transaction)

Use Case 5: Pagination
app.get('/users', async (c) => {
  const page = parseInt(c.req.query('page') || '1');
  const limit = 20;
  const offset = (page - 1) * limit;

  const { results } = await c.env.DB.prepare(
    'SELECT * FROM users ORDER BY created_at DESC LIMIT ? OFFSET ?'
  )
    .bind(limit, offset)
    .all();

  return c.json({
    users: results,
    page,
    limit
  });
});

Migrations Best Practices
1. Always Use Migrations
bunx wrangler d1 migrations create my-database add_users_avatar

2. Make Migrations Idempotent
-- ✅ GOOD: Idempotent
CREATE TABLE IF NOT EXISTS users (...);
CREATE INDEX IF NOT EXISTS idx_email ON users(email);
DROP TABLE IF EXISTS old_table;

-- ❌ BAD: Fails on re-run
CREATE TABLE users (...);
CREATE INDEX idx_email ON users(email);

3. Test Locally First
bunx wrangler d1 migrations apply my-database --local
bunx wrangler d1 execute my-database --local --command "SELECT * FROM users"

4. Add PRAGMA optimize
-- End of migration
PRAGMA optimize;


Load templates/schema-example.sql for complete schema template.

When to Load References
Load references/setup-guide.md when:
First-time D1 setup
Creating first database
Configuring bindings
Applying first migration
Load references/query-patterns.md when:
Need complete API reference
Complex query patterns
Batch operations
Error handling
Load references/read-replication.md when:
Setting up global reads
Need low latency worldwide
Understanding Sessions API
Sequential consistency required
Load references/best-practices.md when:
Optimizing query performance
Schema design decisions
Index strategies
Production deployment checklist
Load references/limits.md when:
Encountering 429 errors or quota warnings
Planning capacity for free vs paid tiers
Understanding database/query limits
Migrating to paid plan
Load references/metrics-analytics.md when:
Investigating performance issues
Setting up monitoring and alerts
Using wrangler d1 insights command
Analyzing query efficiency
Load references/2025-features.md when:
Upgrading from v2.x to v3.x
Enabling new features (auto-retry, jurisdiction, replication)
Understanding breaking changes (Feb 10, 2025 enforcement)
Migrating before deadlines
Interactive Tools

Agents (Autonomous diagnostics):

agents/d1-debugger.md: 9-phase diagnostic (config, migrations, queries, bindings, errors, limits, performance, Time Travel)
agents/d1-query-optimizer.md: Performance analysis (slow queries, missing indexes, optimization recommendations)

Commands (Interactive wizards):

commands/cloudflare-d1:setup.md: Interactive first-time setup wizard
commands/d1-create-migration.md: Guided migration creation with validation
Using Bundled Resources
References (references/)
setup-guide.md - Complete setup walkthrough
query-patterns.md - Complete API reference with examples
read-replication.md - Global read replicas setup
best-practices.md - Performance and optimization
Templates (templates/)
schema-example.sql - Complete schema with indexes
d1-worker-queries.ts - All query patterns in Workers
cloudflare-d1:setup-migration.sh - Complete setup script
Common Patterns
Error Handling
try {
  const { results } = await env.DB.prepare(
    'SELECT * FROM users WHERE email = ?'
  )
    .bind(email)
    .all();

  return c.json(results);
} catch (error) {
  console.error('D1 Error:', error);
  return c.json({ error: 'Database error' }, 500);
}

Raw Mode (Performance)
// Returns arrays instead of objects (faster)
const { results } = await env.DB.prepare(
  'SELECT user_id, email FROM users'
)
  .raw();

// results = [[1, 'user1@example.com'], [2, 'user2@example.com']]

COUNT Queries
const count = await env.DB.prepare(
  'SELECT COUNT(*) as count FROM users'
)
  .first('count');  // Get single column value

console.log('Total users:', count);

SQLite Type Affinity

D1 uses SQLite type affinity:

Declared Type	Affinity
INTEGER, INT	INTEGER
TEXT, VARCHAR, CHAR	TEXT
REAL, FLOAT, DOUBLE	REAL
BLOB	BLOB
(no type)	BLOB

Best practices:

Use INTEGER for numbers
Use TEXT for strings (not VARCHAR)
Use INTEGER for timestamps (Date.now())
Use BLOB for binary data
Top 5 Errors Prevented
SQL Injection: Use .bind(), never string concatenation
Missing Indexes: Create indexes for WHERE/JOIN columns
Migration Failures: Test locally first
Type Confusion: Use INTEGER for timestamps
Batch Size: Limit batch to <500 statements

Load references/best-practices.md for complete error prevention.

Official Documentation
D1 Overview: https://developers.cloudflare.com/d1/
Get Started: https://developers.cloudflare.com/d1/get-started/
Client API: https://developers.cloudflare.com/d1/build-with-d1/d1-client-api/
Read Replication: https://developers.cloudflare.com/d1/reference/read-replication/

Questions? Issues?

Check references/setup-guide.md for setup
Review references/query-patterns.md for API reference
See references/read-replication.md for global reads
Load references/best-practices.md for optimization
Weekly Installs
115
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Mar 14, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass