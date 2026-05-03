---
rating: ⭐⭐⭐
title: bun-expert
url: https://skills.sh/abpai/skills/bun-expert
---

# bun-expert

skills/abpai/skills/bun-expert
bun-expert
Installation
$ npx skills add https://github.com/abpai/skills --skill bun-expert
SKILL.md
Bun Runtime Development Guide

This skill is intentionally grounded in official Bun documentation. Bun moves quickly, so prefer current docs over hard-coded release timelines or benchmark claims.

Project Setup
Initialize a new project
bun init                      # Interactive setup (package.json + tsconfig.json)
bun init -y                   # Accept defaults
bun create <template> <dir>   # Scaffold from a template

TypeScript notes
Bun runs TypeScript directly.
bun init generates a compatible tsconfig.json.
Add extra typing packages only when your editor/toolchain requires them.
Package Management
Essential commands
bun install
bun add <pkg>
bun add -d <pkg>
bun add -g <pkg>
bun remove <pkg>
bun update
bunx <pkg>

Lockfile
bun.lock is the default text lockfile format in modern Bun.
bun.lockb remains supported for compatibility.
Force text lockfile output:
bun install --save-text-lockfile

Diagnostics and security
bun why <pkg>
bun audit
bun list
bun pm migrate

Monorepo catalogs

Bun supports dependency catalogs in workspace roots:

{
  "workspaces": {
    "packages": ["packages/*"],
    "catalog": {
      "react": "^19.0.0",
      "typescript": "^5.7.0"
    }
  }
}


Reference from packages:

{
  "dependencies": {
    "react": "catalog:"
  }
}

Running Code
bun index.ts
bun run start
bun --watch index.ts
bun --hot index.ts
bun run --parallel script1 script2    # run concurrently
bun run --sequential script1 script2  # run one after another

Environment variables

Bun auto-loads .env files. Order is:

.env
.env.{NODE_ENV} (development, production, test)
.env.local
const apiKey = process.env.API_KEY;
const bunApiKey = Bun.env.API_KEY;

HTML entrypoints (zero-config)
bun --hot index.html
bun --watch index.html

HTTP Server

Bun supports route-based servers with Bun.serve().

Bun.serve({
  port: 3000,
  routes: {
    "/": new Response("Hello"),
    "/api/users/:id": (req) => Response.json({ id: req.params.id }),
    "/api/posts": {
      GET: () => Response.json({ posts: [] }),
      POST: async (req) => Response.json(await req.json(), { status: 201 }),
    },
  },
  fetch() {
    return new Response("Not Found", { status: 404 });
  },
});

Built-in API Map
Need	Bun API
HTTP server + WebSockets	Bun.serve()
SQL databases	sql, SQL, Bun.sql, Bun.SQL
S3-compatible storage	s3, S3Client
Redis	redis, RedisClient
Scheduled tasks (cron)	Bun.cron, Bun.cron.parse
Shell scripting	Bun.$ / $
Local files	Bun.file, Bun.write
SQLite (embedded)	bun:sqlite
Password hashing	Bun.password
Testing and Bundling
Test runner (bun test)
bun test
bun test --watch
bun test --test-name-pattern "auth"
bun test --bail
bun test --coverage
bun test --coverage-reporter text
bun test --path-ignore-patterns "*/fixtures/*"

Bundling
bun build ./src/index.ts --outdir ./dist
bun build --target=bun ./src/server.ts --outfile ./dist/server.js
bun build --compile ./src/cli.ts --outfile ./dist/my-cli
bun build --compile --target=browser ./src/app.ts  # self-contained HTML output

Node.js Migration Checklist
Install Bun and run bun install.
Keep existing Node APIs where they work; Bun is highly Node-compatible.
Replace tooling incrementally (bun test, bun build, bun run).
Adopt Bun-native APIs where they simplify code (Bun.serve, sql, redis, s3, Bun.$).
Run your full tests in CI on Bun before removing Node-specific fallbacks.
Deep-Dive References
Reference	Contents
references/builtin-apis.md	Bun.serve, SQL, S3, Redis, cron, shell, filesystem, crypto/password utilities
references/testing-and-bundling.md	bun test usage, mocking patterns, bun build CLI and API
references/node-migration.md	Practical Node-to-Bun migration steps and compatibility guidance
Authoritative Docs
https://bun.com/docs
https://bun.com/docs/cli/test
https://bun.com/docs/cli/pm
https://bun.com/docs/runtime/http/routing
https://bun.com/docs/runtime/env
https://bun.com/docs/runtime/sql
https://bun.com/docs/runtime/s3
https://bun.com/docs/runtime/redis
https://bun.com/docs/runtime/cron
https://bun.com/docs/guides/ecosystem/migrate-from-nodejs
Update Check

On first use in a session, silently check for a newer version:

Fetch https://raw.githubusercontent.com/abpai/skills/main/versions.json.
Compare the version for bun-expert against this file's metadata.version.
If the remote version is newer, pause before the main task and ask:

bun-expert update available (local {X.Y} → remote {A.B}). Would you like me to update it for you first? I can run npx skills update bun-expert for you.

If the user says yes, run the update before continuing.
If the user says no, continue with the current local version.
If the fetch fails or web access is unavailable, skip silently.
Weekly Installs
23
Repository
abpai/skills
First Seen
Feb 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn