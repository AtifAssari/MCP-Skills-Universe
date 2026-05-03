---
rating: ⭐⭐⭐
title: eve-fullstack-app-design
url: https://skills.sh/incept5/eve-skillpacks/eve-fullstack-app-design
---

# eve-fullstack-app-design

skills/incept5/eve-skillpacks/eve-fullstack-app-design
eve-fullstack-app-design
Installation
$ npx skills add https://github.com/incept5/eve-skillpacks --skill eve-fullstack-app-design
SKILL.md
Full-Stack App Design on Eve Horizon

Architect applications where the manifest is the blueprint, the platform handles infrastructure, and every design decision is intentional.

When to Use

Load this skill when:

Designing a new application from scratch on Eve
Migrating an existing app onto the platform
Evaluating whether your current architecture uses Eve's capabilities well
Planning service topology, database strategy, or deployment pipelines
Deciding between managed and external services

This skill teaches design thinking for Eve's PaaS layer. For CLI usage and operational detail, load the corresponding eve-se skills (eve-manifest-authoring, eve-deploy-debugging, eve-auth-and-secrets, eve-pipelines-workflows).

The Manifest as Blueprint

The manifest (.eve/manifest.yaml) is the single source of truth for your application's shape. Treat it as an architectural document, not just configuration.

What the Manifest Declares
Concern	Manifest Section	Design Decision
Service topology	services	What processes run, how they connect
Infrastructure	services[].x-eve	Managed DB, ingress, roles
Build strategy	services[].build + registry	What gets built, where images live
Release pipeline	pipelines	How code flows from commit to production
Environment shape	environments	Which environments exist, what pipelines they use
Agent configuration	x-eve.agents, x-eve.chat	Agent profiles, team dispatch, chat routing
Runtime defaults	x-eve.defaults	Harness, workspace, git policies

Design principle: If an agent or operator can't understand your app's shape by reading the manifest, the manifest is incomplete.

Service Topology
Choose Your Services

Most Eve apps follow one of these patterns:

API + Database (simplest):

services:
  api:        # HTTP service with ingress
  db:         # managed Postgres


API + Worker + Database:

services:
  api:        # HTTP service (user-facing)
  worker:     # Background processor (jobs, queues)
  db:         # managed Postgres


Multi-Service:

services:
  web:        # Frontend/SSR
  api:        # Backend API
  worker:     # Background jobs
  db:         # managed Postgres
  redis:      # external cache (x-eve.external: true)

Service Design Rules
One concern per service. Separate HTTP serving from background processing. An API service should not also run scheduled jobs.
Use managed DB for Postgres. Declare x-eve.role: managed_db and let the platform provision, connect, and inject credentials. No manual connection strings.
Mark external services explicitly. Use x-eve.external: true with x-eve.connection_url for services hosted outside Eve (Redis, third-party APIs).
Use x-eve.role: job for one-off tasks. Migrations, seeds, and data backfills are job services, not persistent processes.
Expose ingress intentionally. Only services that need external HTTP access get x-eve.ingress.public: true. Internal services communicate via cluster networking.
App Object Storage

Apps that need to store files (uploads, avatars, exports) can declare object store buckets in the manifest:

services:
  api:
    x-eve:
      object_store:
        buckets:
          - name: uploads
            visibility: private
          - name: avatars
            visibility: public


Note: The database schema for app object stores exists, but automatic provisioning from the manifest is not yet wired. See references/object-store-filesystem.md for current status.

When wired, the platform injects STORAGE_ENDPOINT, STORAGE_ACCESS_KEY, STORAGE_SECRET_KEY, STORAGE_BUCKET, and STORAGE_FORCE_PATH_STYLE into the service container.

Cloud FS / Google Drive Storage

For document-oriented storage, use cloud FS mounts. Each org connects its own Google Drive via BYOA OAuth credentials, then mounts folders into the org filesystem:

eve integrations configure google-drive --client-id "..." --client-secret "..."
eve integrations connect google-drive
eve cloud-fs mount --org org_xxx --provider google-drive --folder-id <id> --label "Shared Drive"


Apps can browse and search mounted Drive content through Eve's Cloud FS surface (eve cloud-fs ls, eve cloud-fs search, and the per-mount Cloud FS API routes). This is complementary to object store buckets -- use cloud FS for shared documents and collaboration, use object store for app-managed binary assets.

Platform-Injected Variables

Every deployed service receives EVE_API_URL, EVE_PUBLIC_API_URL, EVE_PROJECT_ID, EVE_ORG_ID, and EVE_ENV_NAME. Use EVE_API_URL for server-to-server calls. Use EVE_PUBLIC_API_URL for browser-facing code. Design your app to read these rather than hardcoding URLs.

Reference Architecture: SPA + API + Managed DB

The most common Eve fullstack pattern. A nginx-fronted SPA proxies API calls to an internal backend, with managed Postgres and eve-migrate for schema management.

Service Layout
services:
  web:        # nginx SPA (public ingress, proxies /api/ → api service)
  api:        # NestJS/Express backend (internal, no public ingress)
  db:         # managed Postgres 16
  migrate:    # eve-migrate job (runs SQL migrations)


Why nginx proxy? The web service's nginx reverse-proxies /api/ to the internal API service. This eliminates CORS, removes the need for hard-coded API hostnames, and gives the SPA same-origin access to the backend. The API service has no public ingress — it's only reachable inside the cluster.

Manifest Shape
services:
  api:
    build:
      context: ./apps/api
      dockerfile: ./apps/api/Dockerfile
    ports: [3000]
    environment:
      NODE_ENV: production
      DATABASE_URL: ${managed.db.url}
      CORS_ORIGIN: "https://myapp.eh1.incept5.dev"
    # No x-eve.ingress — API is internal only

  web:
    build:
      context: ./apps/web
      dockerfile: ./apps/web/Dockerfile
    ports: [80]
    environment:
      API_SERVICE_HOST: ${ENV_NAME}-api    # k8s service DNS for nginx proxy
    depends_on:
      api:
        condition: service_healthy
    x-eve:
      ingress:
        public: true
        port: 80
        alias: myapp                        # https://myapp.{org}-{project}-{env}.eh1.incept5.dev

  migrate:
    image: public.ecr.aws/w7c4v0w3/eve-horizon/migrate:latest
    environment:
      DATABASE_URL: ${managed.db.url}
      MIGRATIONS_DIR: /migrations
    x-eve:
      role: job
      files:
        - source: db/migrations
          target: /migrations

  db:
    x-eve:
      role: managed_db
      managed:
        class: db.p1
        engine: postgres
        engine_version: "16"

The nginx Proxy

The web service Dockerfile builds the SPA with Vite, then serves it via nginx. The nginx config uses envsubst to resolve ${API_SERVICE_HOST} at container startup:

server {
    listen 80;
    root /usr/share/nginx/html;
    index index.html;

    location /api/ {
        proxy_pass http://${API_SERVICE_HOST}:3000/;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_buffering off;
    }

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /health {
        return 200 "ok";
        add_header Content-Type text/plain;
    }
}


In the manifest, API_SERVICE_HOST: ${ENV_NAME}-api resolves to the k8s service name (e.g., sandbox-api), giving nginx a stable internal DNS target.

Eve-Migrate for Schema Management

Eve provides a purpose-built migration runner at public.ecr.aws/w7c4v0w3/eve-horizon/migrate:latest. It uses plain SQL files with timestamp prefixes, tracked in a schema_migrations table (idempotent, checksummed, transactional).

db/
  migrations/
    20260312000000_initial_schema.sql
    20260312100000_seed_data.sql
    20260315000000_add_status_column.sql


Mount migrations into the container via x-eve.files. The migrate step in the pipeline runs after deploy (the managed DB must be provisioned first).

Do not use TypeORM, Knex, or Flyway migrations — they add complexity and diverge from the Eve platform's migration tracking. The eve-migrate runner gives parity between local dev and staging.

Multi-Stage Dockerfiles

API Dockerfile (NestJS/Node):

FROM node:22-slim AS base
WORKDIR /app
ENV PNPM_HOME="/pnpm" PATH="$PNPM_HOME:$PATH"
RUN corepack enable && corepack prepare pnpm@latest --activate

FROM base AS deps
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile 2>/dev/null || pnpm install

FROM deps AS build
COPY tsconfig.json ./
COPY src ./src
RUN pnpm build

FROM node:22-slim AS production
WORKDIR /app
RUN groupadd --gid 1000 node || true && useradd --uid 1000 --gid node --shell /bin/bash --create-home node || true
COPY --from=deps /app/node_modules ./node_modules
COPY --from=build /app/dist ./dist
COPY package.json ./
USER node
ENV NODE_ENV=production PORT=3000
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD node -e "fetch('http://localhost:3000/health').then(r => r.ok ? process.exit(0) : process.exit(1)).catch(() => process.exit(1))"
CMD ["node", "dist/main.js"]


Web Dockerfile (Vite SPA + nginx):

FROM node:22-slim AS build
WORKDIR /app
ENV PNPM_HOME="/pnpm" PATH="$PNPM_HOME:$PATH"
RUN corepack enable && corepack prepare pnpm@latest --activate
COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile 2>/dev/null || pnpm install
COPY tsconfig.json vite.config.ts index.html ./
COPY src ./src
RUN pnpm build

FROM nginx:alpine AS production
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/templates/default.conf.template
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost/health || exit 1
CMD ["nginx", "-g", "daemon off;"]


Conventions: node:22-slim base, pnpm via corepack, frozen lockfiles, non-root user (API), health checks on both services.

Database Design
Provisioning

Declare a managed database in the manifest:

services:
  db:
    x-eve:
      role: managed_db
      managed:
        class: db.p1
        engine: postgres
        engine_version: "16"


Reference the connection URL in other services: ${managed.db.url}.

Schema Strategy
Migrations are plain SQL. Create timestamp-prefixed SQL files in db/migrations/ (e.g., 20260312000000_initial.sql). Run via eve-migrate (see Reference Architecture above). Never modify production schemas by hand.
Design for RLS from the start. Every table with multi-tenant data gets org_id TEXT NOT NULL, RLS policies, and a DatabaseService that sets the session context (see below). Retrofitting row-level security is painful.
Inspect before changing. Use eve db schema to examine current schema. Use eve db sql --env <env> for ad-hoc queries during development.
Separate app data from agent data. Use distinct schemas or naming conventions. App tables serve the product; agent tables serve memory and coordination (see eve-agent-memory for storage patterns).
RLS + DatabaseService Pattern (NestJS)

The proven pattern for multi-tenant RLS in NestJS uses raw pg.Pool (not an ORM) with a request-scoped transaction wrapper:

db.ts — Pool configuration with startup health check:

import { Pool } from 'pg';

const databaseUrl = process.env.DATABASE_URL || 'postgresql://app:app@localhost:5432/myapp';
const parsed = new URL(databaseUrl);
const isLocal = ['localhost', '127.0.0.1'].includes(parsed.hostname);

export const pool = new Pool({
  connectionString: databaseUrl,
  ssl: !isLocal ? { rejectUnauthorized: false } : undefined,
});


database.service.ts — Transaction wrapper with RLS context:

import { Injectable } from '@nestjs/common';
import type { PoolClient, QueryResult, QueryResultRow } from 'pg';
import { pool } from '../db';

export interface DbContext {
  org_id: string;
  user_id?: string;
}

@Injectable()
export class DatabaseService {
  async withClient<T>(context: DbContext | null, fn: (client: PoolClient) => Promise<T>): Promise<T> {
    const client = await pool.connect();
    try {
      await client.query('BEGIN');
      if (context?.org_id) {
        await client.query("SELECT set_config('app.org_id', $1, true)", [context.org_id]);
      }
      if (context?.user_id) {
        await client.query("SELECT set_config('app.user_id', $1, true)", [context.user_id]);
      }
      const result = await fn(client);
      await client.query('COMMIT');
      return result;
    } catch (error) {
      await client.query('ROLLBACK');
      throw error;
    } finally {
      client.release();
    }
  }

  async query<T extends QueryResultRow>(ctx: DbContext | null, sql: string, params?: unknown[]): Promise<QueryResult<T>> {
    return this.withClient(ctx, (client) => client.query<T>(sql, params));
  }

  async queryOne<T extends QueryResultRow>(ctx: DbContext | null, sql: string, params?: unknown[]): Promise<T | null> {
    const result = await this.query<T>(ctx, sql, params);
    return result.rows[0] ?? null;
  }
}


Why this pattern?

set_config('app.org_id', $1, true) is transaction-scoped — it automatically clears when the connection returns to the pool.
Every database access goes through withClient, guaranteeing RLS context is set before any query.
No ORM overhead — raw SQL gives full control over query plans and joins.
The DbContext object is derived from req.user (set by Eve auth middleware).

RLS policy template (applied per table in migration SQL):

ALTER TABLE my_table ENABLE ROW LEVEL SECURITY;

CREATE POLICY my_table_select ON my_table FOR SELECT
  USING (current_setting('app.org_id', true) IS NOT NULL
    AND org_id = current_setting('app.org_id', true));

CREATE POLICY my_table_insert ON my_table FOR INSERT
  WITH CHECK (current_setting('app.org_id', true) IS NOT NULL
    AND org_id = current_setting('app.org_id', true));

CREATE POLICY my_table_update ON my_table FOR UPDATE
  USING (current_setting('app.org_id', true) IS NOT NULL
    AND org_id = current_setting('app.org_id', true))
  WITH CHECK (current_setting('app.org_id', true) IS NOT NULL
    AND org_id = current_setting('app.org_id', true));


Table conventions: Every table gets id UUID PRIMARY KEY DEFAULT gen_random_uuid(), org_id TEXT NOT NULL, created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(), and updated_at TIMESTAMPTZ (with a trigger) on mutable tables. Enable pgcrypto extension in the first migration.

Access Patterns
Who Queries	How	Auth
App service	${managed.db.url} in service env	Connection string injected at deploy
Agent via CLI	eve db sql --env <env>	Job token scopes access
Agent via RLS	SQL with app.current_user_id()	Session context set by runtime
Build and Release Pipeline
The Canonical Flow

Every production app should follow build → release → deploy → migrate → smoke-test:

pipelines:
  deploy:
    steps:
      - name: build
        action:
          type: build          # Creates BuildSpec + BuildRun, produces image digests
      - name: release
        depends_on: [build]
        action:
          type: release        # Creates immutable release from build artifacts
      - name: deploy
        depends_on: [release]
        action:
          type: deploy         # Deploys release to target environment
      - name: migrate
        depends_on: [deploy]
        action:
          type: job
          service: migrate     # Runs eve-migrate against the managed DB
      - name: smoke-test
        depends_on: [migrate]
        script:
          run: ./scripts/smoke-test.sh
          timeout: 300


Why this order matters:

build produces SHA256 image digests. release pins those exact digests. deploy uses the pinned release. You deploy exactly what you built — no tag drift, no "latest" surprises.
migrate runs after deploy because the managed DB must be provisioned first. The eve-migrate job applies any pending SQL migrations.
smoke-test validates the deployed services end-to-end before the pipeline reports success.
Registry Decisions
Option	When to Use
registry: "eve"	Default. Internal registry with JWT auth. Simplest setup.
BYO registry (GHCR, ECR)	When you need images accessible outside Eve, or have existing CI.
registry: "none"	Public base images only. No custom builds.

For GHCR, add OCI labels to Dockerfiles for automatic repository linking:

LABEL org.opencontainers.image.source="https://github.com/YOUR_ORG/YOUR_REPO"

Build Configuration

Every service with a custom image needs a build section:

services:
  api:
    build:
      context: ./apps/api
      dockerfile: Dockerfile
    image: ghcr.io/org/my-api


Use multi-stage Dockerfiles. BuildKit handles them natively. Place the OCI label on the final stage.

Deployment and Environments
Environment Strategy
Environment	Type	Purpose	Pipeline
staging	persistent	Integration testing, demos	deploy
production	persistent	Live traffic	deploy (with promotion)
preview-*	temporary	PR previews, feature branches	deploy (auto-cleanup)

Link each environment to a pipeline in the manifest:

environments:
  staging:
    pipeline: deploy
  production:
    pipeline: deploy

Deployment Patterns

Standard deploy: eve env deploy staging --ref main --repo-dir . triggers the linked pipeline.

Direct deploy (bypass pipeline): eve env deploy staging --ref <sha> --direct for emergencies or simple setups.

Promotion: Build once in staging, then promote the same release artifacts to production. The build step's digests carry forward, guaranteeing identical images.

Recovery

When a deploy fails:

Diagnose: eve env diagnose <project> <env> — shows health, recent deploys, service status.
Logs: eve env logs <project> <env> — container output.
Rollback: Redeploy the previous known-good release.
Reset: eve env reset <project> <env> — nuclear option, reprovisions from scratch.

Design your app to be rollback-safe: migrations should be forward-compatible, and services should handle schema version mismatches gracefully during rolling deploys.

Per-Org OAuth for App Integrations

Apps that integrate with Google Drive, Slack, or other OAuth providers use per-org credentials (BYOA -- Bring Your Own App). Each org registers its own OAuth app, giving it control over branding, scopes, rate limits, and credential rotation.

eve integrations configure google-drive --client-id "..." --client-secret "..."
eve integrations connect google-drive


Design implications: Apps that consume Google Drive data or Slack messages should reference integration tokens through the Eve API, not store OAuth credentials themselves. The platform handles token refresh using the org's registered OAuth app credentials.

Event Triggers for Workflows

Workflows can be triggered by platform events, enabling reactive automation:

workflows:
  on-deploy:
    trigger:
      system.event: environment.deployed
    steps:
      - name: smoke-test
        script:
          run: ./scripts/smoke-test.sh

  on-ingest:
    trigger:
      system.event: doc.ingest.completed
    steps:
      - name: process
        agent: doc-processor


Event sources include: GitHub webhooks, Slack events, system events (deploy, build, ingest), cron schedules, and manual triggers. See eve-pipelines-workflows for trigger syntax and references/events.md for the full event catalog.

App CLI Framework — The Eve Way

Every app with an API should ship a CLI. This is the Eve way — agents interact with app data through CLI commands, not raw REST calls. A CLI gives agents discoverable, auth-transparent, type-safe access to your app's domain. It reduces LLM calls per operation from 3-5 (curl) to 1 (CLI command), eliminates URL construction and JSON quoting, and surfaces domain-specific error messages instead of HTTP status codes.

Why CLI-First Matters

When a coding agent needs to read or write app data, it faces a choice: construct a curl command with the right URL, auth header, and JSON body — or run eden projects list --json. The CLI approach wins on every dimension:

Dimension	CLI	Raw REST
Auth	Invisible (EVE_JOB_TOKEN read automatically)	Manual header construction
URL	None (CLI knows the service URL)	Build from EVE_APP_API_URL_*
Discoverability	myapp --help	Read OpenAPI spec or docs
Errors	Domain-specific messages	HTTP status codes
LLM cost	1 call per operation	3-5 calls per operation
Declare the CLI in the Manifest
services:
  api:
    x-eve:
      api_spec:
        type: openapi
      cli:
        name: myapp              # Binary name on $PATH
        bin: cli/bin/myapp       # Pre-bundled executable (repo-bundled mode)


The platform auto-discovers services with x-eve.cli from the manifest and makes them available on $PATH for all agent jobs in the project — no explicit with_apis needed. Just declare the CLI in the manifest and every agent gets it. Agents run myapp --help to discover capabilities. See eve-manifest-authoring for declaration details and references/app-cli.md for the full implementation pattern (bundling, env var contract, testing).

Design Guidance
Build the CLI early. Don't wait until the API is "done." Start the CLI alongside the first API endpoints. Agents will use it immediately.
Mirror the API surface. Every REST endpoint should have a CLI subcommand. GET /items → myapp items list, POST /items → myapp items create --file data.json.
Support --json everywhere. Default output is human-readable tables; --json gives machine-readable output for agent pipelines.
Bundle as a single file. Use esbuild to produce a self-contained Node.js script committed to the repo. Zero startup latency.
Point agent skills at the CLI. Skill instructions should say "Use myapp items list", never "curl the API at..."
App Undeploy/Delete Lifecycle

Manage the full lifecycle of environments and projects:

# Undeploy services (stops pods, keeps env record and history)
eve env undeploy <project> <env>

# Delete environment entirely (cascades to managed DB, secrets)
eve env delete <project> <env>

# Delete project (cascades to all environments, artifacts, history)
eve project delete <project-id>


Design your app for clean teardown: migrations should be idempotent, managed DB deletion is irreversible, and pipeline history is preserved in audit logs even after environment deletion.

Secrets and Configuration
Scoping Model

Secrets resolve with cascading precedence: project > user > org > system. A project-level API_KEY overrides an org-level API_KEY.

Design Rules
Set secrets per-project. Use eve secrets set KEY "value" --project proj_xxx. Keep project secrets self-contained.
Use interpolation in the manifest. Reference ${secret.KEY} in service environment blocks. The platform resolves at deploy time.
Validate before deploying. Run eve manifest validate --validate-secrets to catch missing secret references before they cause deploy failures.
Use .eve/dev-secrets.yaml for local development. Mirror the production secret keys with local values. This file is gitignored.
Never store secrets in environment variables directly. Always use ${secret.KEY} interpolation. This ensures secrets flow through the platform's resolution and audit chain.
Git Credentials

Agents need repository access. Set either github_token (HTTPS) or ssh_key (SSH) as project secrets. The worker injects these automatically during git operations.

SSO Authentication
Adding SSO to Your App

Eve provides shared auth packages that eliminate boilerplate. Add Eve SSO login in ~25 lines of code.

Backend (@eve-horizon/auth):

import { eveUserAuth, eveAuthGuard, eveAuthConfig } from '@eve-horizon/auth';

app.use(eveUserAuth());                                     // Parse tokens (non-blocking)
app.get('/auth/config', eveAuthConfig());                   // Serve SSO discovery
app.get('/auth/me', eveAuthGuard(), (req, res) => {
  res.json(req.eveUser);                                    // { id, email, orgId, role }
});
app.use('/api', eveAuthGuard());                            // Protect all API routes


Frontend (@eve-horizon/auth-react):

import { EveAuthProvider, EveLoginGate } from '@eve-horizon/auth-react';

function App() {
  return (
    <EveAuthProvider apiUrl="/api">
      <EveLoginGate>
        <ProtectedApp />
      </EveLoginGate>
    </EveAuthProvider>
  );
}


For authenticated API calls from components, use createEveClient:

import { createEveClient } from '@eve-horizon/auth-react';
const client = createEveClient('/api');
const res = await client.fetch('/data');


Custom auth gate — When you need control over loading and login states (custom login page, richer loading UI), use useEveAuth() directly instead of EveLoginGate:

import { EveAuthProvider, useEveAuth } from '@eve-horizon/auth-react';

function AuthGate() {
  const { user, loading, loginWithToken, loginWithSso, logout } = useEveAuth();
  if (loading) return <Spinner />;
  if (!user) return <LoginPage onSso={loginWithSso} onToken={loginWithToken} />;
  return <AppShell user={user} onLogout={logout}><Routes /></AppShell>;
}

export default function App() {
  return (
    <EveAuthProvider apiUrl={API_BASE}>
      <AuthGate />
    </EveAuthProvider>
  );
}

How It Works
EveAuthProvider checks sessionStorage for cached token
If no token, probes SSO broker /session (root-domain cookie)
If SSO session exists, gets fresh Eve RS256 token
If no session, shows login form (SSO redirect or token paste)
All API requests include Authorization: Bearer <token>
NestJS Backend

Apply eveUserAuth() as global middleware in main.ts. If existing controllers expect req.user rather than req.eveUser, add a thin bridge that maps Eve roles to app-specific roles in one place:

import { eveUserAuth } from '@eve-horizon/auth';

app.use(eveUserAuth());
app.use((req, _res, next) => {
  if (req.eveUser) {
    req.user = { ...req.eveUser, role: req.eveUser.role === 'member' ? 'viewer' : 'admin' };
  }
  next();
});

Auto-Injected Variables

The platform injects EVE_SSO_URL, EVE_API_URL, and EVE_ORG_ID into deployed containers. No manual configuration needed. Use ${SSO_URL} in manifest env blocks for frontend-accessible SSO URLs.

Design Rules
Use the SDK, not custom auth. The SDK replaces ~750 lines of hand-rolled auth with ~50 lines.
Non-blocking middleware first. Use eveUserAuth() globally, then eveAuthGuard() on protected routes. This enables mixed public/private routes.
The /auth/config endpoint is the handshake. The frontend discovers the SSO URL by calling the backend's eveAuthConfig() endpoint. This decouples the frontend from platform env vars and works identically in local dev and deployed environments.
Design for token staleness. The orgs JWT claim reflects membership at mint time (1-day TTL). Use strategy: 'remote' for immediate revocation if needed.

For full SDK reference, see references/auth-sdk.md in the eve-read-eve-docs skill.

Observability and Debugging
The Debugging Ladder

Escalate through these stages:

1. Status    → eve env show <project> <env>
2. Diagnose  → eve env diagnose <project> <env>
3. Logs      → eve env logs <project> <env>
4. Pipeline  → eve pipeline logs <pipeline> <run-id> --follow
5. Recover   → eve env deploy (rollback) or eve env reset


Start at the top. Each stage provides more detail and more cost. Most issues resolve at stages 1-2.

Pipeline Observability

Monitor pipeline execution in real time:

eve pipeline logs <pipeline> <run-id> --follow         # stream all steps
eve pipeline logs <pipeline> <run-id> --follow --step build  # stream one step


Failed steps include failure hints and link to build diagnostics when applicable.

Build Debugging

When builds fail:

eve build list --project <project_id>
eve build diagnose <build_id>
eve build logs <build_id>


Common causes: missing registry credentials, Dockerfile path mismatch, build context too large.

Health Checks

Design services with health endpoints. Eve polls health to determine deployment readiness. A deploy is complete when ready === true and active_pipeline_run === null.

Design Checklist

Service Topology:

 Each service has one responsibility
 Managed DB declared for Postgres needs
 External services marked with x-eve.external: true
 Only public-facing services have ingress enabled
 Platform-injected env vars used (not hardcoded URLs)

Database:

 Migrations are plain SQL files in db/migrations/ with timestamp prefixes
 eve-migrate job service declared in manifest with x-eve.files mount
 DatabaseService wraps all DB access with RLS context (set_config)
 RLS policies on every table with org_id
 pgcrypto extension enabled, UUID primary keys, updated_at triggers
 App data separated from agent data by schema or convention

Pipeline:

 Canonical build → release → deploy → migrate → smoke-test pipeline defined
 Migrate step runs after deploy (managed DB must exist first)
 Smoke test script validates deployed services end-to-end
 Registry chosen and credentials set as secrets
 OCI labels on Dockerfiles (for GHCR)
 Image digests flow through release (no tag-based deploys)

Environments:

 Staging and production environments defined
 Each environment linked to a pipeline
 Promotion workflow defined (build once, deploy many)
 Recovery procedure known (diagnose -> rollback -> reset)

Secrets:

 All secrets set per-project via eve secrets set
 Manifest uses ${secret.KEY} interpolation
 eve manifest validate --validate-secrets passes
 .eve/dev-secrets.yaml exists for local development
 Git credentials (github_token or ssh_key) configured

Authentication:

 @eve-horizon/auth middleware added to backend (eveUserAuth + eveAuthGuard)
 Auth config endpoint serves SSO discovery (eveAuthConfig)
 @eve-horizon/auth-react wraps frontend (EveAuthProvider + EveLoginGate or custom useEveAuth gate)
 createEveClient used for authenticated API calls from frontend
 Platform-injected auth env vars used (EVE_SSO_URL, EVE_ORG_ID)
 Eve roles mapped to app roles in one place (bridge middleware), not scattered across controllers

App CLI (the Eve way):

 App API wrapped in a domain CLI (e.g., eden projects list)
 CLI declared in manifest via x-eve.cli with name and bin
 CLI bundled as single-file executable (esbuild for Node.js)
 CLI reads EVE_APP_API_URL_{SERVICE} and EVE_JOB_TOKEN automatically
 All CLI commands support --json for machine-readable output
 Agent skill references CLI commands, not raw curl/REST calls

Observability:

 Services expose health endpoints
 The debugging ladder is understood (status -> diagnose -> logs -> recover)
 Pipeline logs are accessible via eve pipeline logs --follow
Cross-References
Manifest syntax and options: eve-manifest-authoring
Deploy commands and error resolution: eve-deploy-debugging
Secret management and access groups: eve-auth-and-secrets
Pipeline and workflow definitions: eve-pipelines-workflows
Local development workflow: eve-local-dev-loop
Layering agentic capabilities onto this foundation: eve-agentic-app-design
Auth SDK and SSO integration: eve-read-eve-docs → references/auth-sdk.md
Object storage and filesystem: eve-read-eve-docs → references/object-store-filesystem.md
External integrations (Slack, GitHub): eve-read-eve-docs → references/integrations.md
Weekly Installs
206
Repository
incept5/eve-skillpacks
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn