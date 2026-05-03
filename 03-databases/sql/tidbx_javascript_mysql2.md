---
rating: ⭐⭐
title: tidbx-javascript-mysql2
url: https://skills.sh/pingcap/agent-rules/tidbx-javascript-mysql2
---

# tidbx-javascript-mysql2

skills/pingcap/agent-rules/tidbx-javascript-mysql2
tidbx-javascript-mysql2
Installation
$ npx skills add https://github.com/pingcap/agent-rules --skill tidbx-javascript-mysql2
SKILL.md
TiDB + JavaScript (mysql2)

Use this skill to connect to TiDB from Node.js with the mysql2 driver (promise API), configure TLS correctly for TiDB Cloud, and provide small runnable snippets you can copy into a project.

Important: mysql vs mysql2

These two drivers are easy to mix up:

This skill is for mysql2 (npm i mysql2) and uses the promise API (mysql2/promise).
If you meant mysqljs/mysql (npm i mysql) which is callback-based, jump to the tidbx-javascript-mysqljs skill instead.
Recommendation: prefer an ORM for app code

For most application code (models, migrations, types), prefer an ORM/query builder:

Prisma ORM: use tidbx-prisma
Kysely query builder: use tidbx-kysely
When to use this skill
Connect to TiDB from JavaScript/TypeScript (Node.js runtime) via mysql2 / mysql2/promise.
Need TLS guidance (TiDB Cloud public endpoint) or CA certificate setup (TiDB Cloud Dedicated).
Want a minimal "connect -> SELECT VERSION() -> CRUD" template.
Code generation rules (Node.js)
Never hardcode credentials; use DATABASE_URL or TIDB_* env vars.
Prefer mysql2/promise and parameterized queries (? placeholders via execute() / query()).
Default to a pool for apps/services (createPool), and await pool.end() on shutdown.
When using a pool against TiDB Cloud, set an idle timeout <= 300s (e.g. idleTimeout: 300_000) and keep connectionLimit small in serverless environments.
Do not recommend multipleStatements: true unless the user explicitly needs it.
Connection checklist
Confirm deployment type: TiDB Cloud (Starter/Essential vs Dedicated) or self-managed.
Confirm endpoint type: public vs private/VPC.
Decide config style:
Preferred: DATABASE_URL (easy for deployment).
Alternative: TIDB_HOST/TIDB_USER/... options (handy for local/dev).
If using a public endpoint on TiDB Cloud, enable TLS.
Install
npm i mysql2


If you want .env support:

npm i dotenv

Minimal snippets
Option A: connect with DATABASE_URL (recommended)
import { createConnection } from 'mysql2/promise'

const conn = await createConnection(process.env.DATABASE_URL)
const [[row]] = await conn.query('SELECT VERSION() AS v')
console.log(row.v)
await conn.end()


Notes:

URL-encode special characters in passwords (best: copy the URL from the TiDB Cloud "Connect" dialog).
If the TiDB Cloud connect dialog provides TLS options in the URL, keep them as-is.
Option B: connect with connection options (TLS / CA)

Use this when you want explicit TLS config (common for TiDB Cloud Dedicated with a downloaded CA).

import { createPool } from 'mysql2/promise'
import fs from 'node:fs'

const pool = createPool({
  host: process.env.TIDB_HOST,
  port: Number(process.env.TIDB_PORT ?? 4000),
  user: process.env.TIDB_USER,
  password: process.env.TIDB_PASSWORD,
  database: process.env.TIDB_DATABASE ?? 'test',
  ssl: process.env.TIDB_ENABLE_SSL === 'true'
    ? {
        minVersion: 'TLSv1.2',
        ca: process.env.TIDB_CA_PATH ? fs.readFileSync(process.env.TIDB_CA_PATH) : undefined,
      }
    : undefined,
})


Suggested env vars:

TIDB_HOST=...
TIDB_PORT=4000
TIDB_USER=...
TIDB_PASSWORD=...
TIDB_DATABASE=test
TIDB_ENABLE_SSL=true
# Optional (commonly used for TiDB Cloud Dedicated):
TIDB_CA_PATH=/absolute/path/to/ca.pem

CRUD + safety patterns
Prefer execute() for parameterized SQL:
const [result] = await pool.execute(
  'INSERT INTO players (coins, goods) VALUES (?, ?)',
  [100, 100],
)

Use explicit transactions for multi-step updates:
const conn = await pool.getConnection()
try {
  await conn.beginTransaction()
  await conn.execute('UPDATE players SET coins = coins + ? WHERE id = ?', [50, id])
  await conn.commit()
} catch (e) {
  await conn.rollback()
  throw e
} finally {
  conn.release()
}

Templates & scripts in this skill
scripts/validate_connection.mjs -- reads DATABASE_URL or TIDB_*, connects, prints SELECT VERSION(), then exits.
templates/quickstart.mjs -- minimal end-to-end: connect -> create table -> insert -> query -> update -> delete.
Weekly Installs
15
Repository
pingcap/agent-rules
GitHub Stars
24
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass