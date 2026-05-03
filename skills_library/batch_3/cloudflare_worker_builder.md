---
title: cloudflare-worker-builder
url: https://skills.sh/jezweb/claude-skills/cloudflare-worker-builder
---

# cloudflare-worker-builder

skills/jezweb/claude-skills/cloudflare-worker-builder
cloudflare-worker-builder
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill cloudflare-worker-builder
Summary

Scaffold and deploy Cloudflare Workers projects with Hono routing, Vite dev server, and Static Assets.

Guides you through project setup in four steps: understanding requirements, scaffolding structure, configuring bindings (D1, R2, KV), and deploying to production
Provides ready-to-use asset files including wrangler.jsonc, vite.config.ts, Hono app entry point, and TypeScript configuration
Documents critical patterns for export syntax, SPA fallback with API route protection, Vite plugin setup, and scheduled/cron handlers
Includes troubleshooting reference for 10 common issues, architecture decisions, and deployment strategies with documented sources
SKILL.md
Cloudflare Worker Builder

Scaffold a working Cloudflare Worker project from a brief description. Produces a deployable project with Hono routing, Vite dev server, and Static Assets.

Workflow
Step 1: Understand the Project

Ask about the project to choose the right bindings and structure:

What does the app do? (API only, SPA + API, landing page)
What data storage? (D1 database, R2 files, KV cache, none)
Auth needed? (Clerk, better-auth, none)
Custom domain or workers.dev subdomain?

A brief like "todo app with database" is enough to proceed.

Step 2: Scaffold the Project
npm create cloudflare@latest my-worker -- --type hello-world --ts --git --deploy false --framework none
cd my-worker
npm install hono
npm install -D @cloudflare/vite-plugin vite


Copy and customise the asset files from this skill's assets/ directory:

wrangler.jsonc — Worker configuration
vite.config.ts — Vite + Cloudflare plugin
src/index.ts — Hono app with Static Assets fallback
package.json — Scripts and dependencies
tsconfig.json — TypeScript config
public/index.html — SPA entry point
Step 3: Configure Bindings

Add bindings to wrangler.jsonc based on project needs. Wrangler 4.45+ auto-provisions resources on first deploy — always specify explicit names:

{
  "name": "my-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-11-11",
  "assets": {
    "directory": "./public/",
    "binding": "ASSETS",
    "not_found_handling": "single-page-application",
    "run_worker_first": ["/api/*"]
  },
  // Add as needed:
  "d1_databases": [{ "binding": "DB", "database_name": "my-app-db" }],
  "r2_buckets": [{ "binding": "STORAGE", "bucket_name": "my-app-files" }],
  "kv_namespaces": [{ "binding": "CACHE", "title": "my-app-cache" }]
}

Step 4: Deploy
npm run dev           # Local dev at http://localhost:8787
wrangler deploy       # Production deploy

Critical Patterns
Export Syntax
// CORRECT — use this pattern
export default app

// WRONG — causes "Cannot read properties of undefined"
export default { fetch: app.fetch }


Source: honojs/hono #3955

Static Assets + API Routes

Without run_worker_first, SPA fallback intercepts API routes and returns index.html instead of JSON:

"assets": {
  "not_found_handling": "single-page-application",
  "run_worker_first": ["/api/*"]  // CRITICAL
}


Source: workers-sdk #8879

Vite Config
import { defineConfig } from 'vite'
import { cloudflare } from '@cloudflare/vite-plugin'

export default defineConfig({ plugins: [cloudflare()] })


Always set the main field in wrangler.jsonc — the Vite plugin needs it.

Scheduled/Cron Handlers

When adding cron triggers, switch to explicit export:

export default {
  fetch: app.fetch,
  scheduled: async (event, env, ctx) => { /* ... */ }
}

Reference Files

Read these for detailed troubleshooting:

references/common-issues.md — 10 documented issues with sources and fixes
references/architecture.md — Route priority, caching, Workers RPC
references/deployment.md — CI/CD, auto-provisioning, gradual rollouts
Weekly Installs
821
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass