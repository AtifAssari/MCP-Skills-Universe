---
title: tidbx-kysely
url: https://skills.sh/pingcap/agent-rules/tidbx-kysely
---

# tidbx-kysely

skills/pingcap/agent-rules/tidbx-kysely
tidbx-kysely
Installation
$ npx skills add https://github.com/pingcap/agent-rules --skill tidbx-kysely
SKILL.md
TiDB Cloud + Kysely

Use this skill when a user wants to connect Kysely to TiDB Cloud (TiDB X). Default to standard TCP (Node server/runtime). Only use the TiDB Cloud serverless driver over HTTP for serverless or edge runtimes.

Workflow
Confirm runtime and deployment target (Node server vs serverless/edge).
Confirm cluster type. The serverless HTTP driver applies to Starter/Essential clusters.
Collect connection info (prefer a mysql:// URL in DATABASE_URL).
Choose the path:
Normal usage (default): TCP + mysql2 pool + Kysely MysqlDialect.
Serverless/edge: @tidbcloud/kysely dialect over HTTP.
Show only the matching snippet first. Include the other path only if the user asks. Use references/kysely-usage.md for full examples.
Normal usage (default)

Use this for Node servers, long-lived runtimes, or when TCP is available. This is the primary path unless the user explicitly needs serverless/edge. Uses TCP with a mysql2 pool.

import { Kysely, MysqlDialect } from 'kysely'
import { createPool } from 'mysql2'

const pool = createPool({ uri: process.env.DATABASE_URL })
const db = new Kysely({ dialect: new MysqlDialect({ pool }) })

Serverless/edge usage (HTTP)

Use this only when the runtime cannot keep TCP connections (serverless/edge). Requires the TiDB Cloud serverless driver and Starter/Essential clusters. Use from backend services only (browser origins may be blocked by CORS). See references/serverless-kysely-tutorial.md for the full walkthrough.

import { Kysely } from 'kysely'
import { TiDBCloudServerlessDialect } from '@tidbcloud/kysely'

const db = new Kysely({
  dialect: new TiDBCloudServerlessDialect({ url: process.env.DATABASE_URL }),
})

Notes
Many users say "instance" to mean "cluster"; treat them as the same.
Keep instructions concise; move any long docs into references.
Weekly Installs
16
Repository
pingcap/agent-rules
GitHub Stars
24
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass