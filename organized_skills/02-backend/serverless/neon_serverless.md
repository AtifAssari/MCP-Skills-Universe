---
rating: ⭐⭐
title: neon-serverless
url: https://skills.sh/neondatabase/ai-rules/neon-serverless
---

# neon-serverless

skills/neondatabase/ai-rules/neon-serverless
neon-serverless
Installation
$ npx skills add https://github.com/neondatabase/ai-rules --skill neon-serverless
SKILL.md
Neon Serverless Skill

Configures the Neon Serverless Driver for optimal performance in serverless and edge computing environments.

When to Use
Setting up connections for edge functions (Vercel Edge, Cloudflare Workers)
Configuring serverless APIs (AWS Lambda, Google Cloud Functions)
Optimizing for low-latency database access
Implementing connection pooling for high-throughput apps

Not recommended for: Complex multi-statement transactions (use WebSocket Pool), persistent servers (use native PostgreSQL drivers), or offline-first applications.

Code Generation Rules

When generating TypeScript/JavaScript code:

BEFORE generating import statements, check tsconfig.json for path aliases (compilerOptions.paths)
If path aliases exist (e.g., "@/": ["./src/"]), use them (e.g., import { x } from '@/lib/utils')
If NO path aliases exist or unsure, ALWAYS use relative imports (e.g., import { x } from '../../../lib/utils')
Verify imports match the project's configuration
Default to relative imports - they always work regardless of configuration
Reference Documentation

Primary Resource: See [neon-serverless.mdc](https://raw.githubusercontent.com/neondatabase-labs/ai-rules/main/neon-serverless.mdc) in project root for comprehensive guidelines including:

Installation and compatibility requirements
HTTP vs WebSocket adapter selection
Connection pooling strategies
Query optimization patterns
Error handling and troubleshooting
Quick Setup
Installation
npm install @neondatabase/serverless

Connection Patterns

HTTP Client (recommended for edge/serverless):

import { neon } from '@neondatabase/serverless';
const sql = neon(process.env.DATABASE_URL!);
const rows = await sql`SELECT * FROM users WHERE id = ${userId}`;


WebSocket Pool (for Node.js long-lived connections):

import { Pool } from '@neondatabase/serverless';
const pool = new Pool({ connectionString: process.env.DATABASE_URL! });
const result = await pool.query('SELECT * FROM users WHERE id = $1', [userId]);


See templates/ for complete examples:

templates/http-connection.ts - HTTP client setup
templates/websocket-pool.ts - WebSocket pool configuration
Validation

Use scripts/validate-connection.ts to test your database connection before deployment.

Related Skills
neon-auth - Add authentication
neon-js - Full SDK with auth + data API
neon-drizzle - For ORM with serverless connections
neon-toolkit - For ephemeral database testing

Want best practices in your project? Run neon-plugin:add-neon-docs with parameter SKILL_NAME="neon-serverless" to add reference links.

Weekly Installs
127
Repository
neondatabase/ai-rules
GitHub Stars
83
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass