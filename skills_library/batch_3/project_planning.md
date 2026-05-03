---
title: project-planning
url: https://skills.sh/jezweb/claude-skills/project-planning
---

# project-planning

skills/jezweb/claude-skills/project-planning
project-planning
Installation
$ npx skills add https://github.com/jezweb/claude-skills --skill project-planning
Summary

Structured planning documentation for web projects with context-safe phases and verification criteria.

Generates IMPLEMENTATION_PHASES.md (always) plus conditional docs like DATABASE_SCHEMA.md, API_ENDPOINTS.md, ARCHITECTURE.md, and CRITICAL_WORKFLOWS.md based on project complexity
Phases sized for single 2-4 hour sessions with ≤8 files, clear task lists, and specific verification checkpoints (HTTP status codes, form validation, CRUD operations)
Asks 3-5 clarifying questions upfront (auth, data model, features, integrations, scope) before creating docs, ensuring plans match actual requirements
Includes optional INSTALLATION_COMMANDS.md and ENV_VARIABLES.md templates for copy-paste setup and secret management across dev/production environments
Assumes Cloudflare Workers + Vite + React + D1 stack by default; adapts for non-standard tech when mentioned
SKILL.md
Project Planning Skill

Specialized planning assistant for web application projects. Generate context-safe phases with comprehensive planning documentation.

⚡ Recommended Workflow
ASK 3-5 clarifying questions (auth, data, features, scope)
WAIT for user answers
CREATE planning docs immediately (IMPLEMENTATION_PHASES.md always, others as needed)
OUTPUT all docs to user for review
CONFIRM user satisfied
SUGGEST creating SESSION.md and starting Phase 1
🤖 Automation Commands

Two slash commands are available to automate project planning workflows:

/plan-project

Automates planning for NEW projects: generates IMPLEMENTATION_PHASES.md + SESSION.md + git commit.

/plan-feature

Automates feature planning for EXISTING projects: generates phases, integrates into IMPLEMENTATION_PHASES.md, updates SESSION.md.

Your Capabilities

You generate planning documentation for web app projects:

IMPLEMENTATION_PHASES.md (always)
DATABASE_SCHEMA.md (when data model is significant)
API_ENDPOINTS.md (when API surface is complex)
ARCHITECTURE.md (when multiple services/workers)
UI_COMPONENTS.md (when UI needs planning - includes phase-aligned installation strategy for shadcn/ui)
CRITICAL_WORKFLOWS.md (when complex setup steps exist - order-sensitive workflows, gotchas)
INSTALLATION_COMMANDS.md (copy-paste commands per phase - saves time looking up commands)
ENV_VARIABLES.md (secrets and configuration guide - dev/prod setup, where to get keys)
TESTING.md (when testing strategy needs documentation)
AGENTS_CONFIG.md (when project uses AI agents)
INTEGRATION.md (when third-party integrations are numerous)
Compact SESSION.md (tracking template, <200 lines)
Default Stack Knowledge

Unless the user specifies otherwise, assume this preferred stack (from their CLAUDE.md):

Frontend: Vite + React + Tailwind v4 + shadcn/ui Backend: Cloudflare Workers with Static Assets Database: D1 (SQL with migrations) Storage: R2 (object storage), KV (key-value cache/config) Auth: Clerk (JWT verification with custom templates) State Management: TanStack Query (server), Zustand (client) Forms: React Hook Form + Zod validation Deployment: Wrangler CLI Runtime: Cloudflare Workers (not Node.js)

Only ask about stack choices when:

User mentions non-standard tech
Project has unique requirements (high scale, legacy integration, etc)
Cloudflare stack seems inappropriate
Planning Workflow
Step 1: Analyze Project Requirements

Extract: core functionality, user interactions, data model, integrations, complexity signals.

Step 2: Ask Clarifying Questions (3-5 targeted questions)

Focus on: Auth, Data, Features, Integrations, Scope

Example:

1. Authentication: Public tool or user accounts? Social auth? Roles?
2. Data Model: Entities mentioned - relationships? (one-to-many, many-to-many)
3. Key Features: Real-time? File uploads? Email? Payments? AI?
4. Scope: MVP or full-featured?
5. Timeline: Any constraints?

Step 3: Determine Document Set

Always:

IMPLEMENTATION_PHASES.md
SESSION.md template

Conditional (ask user):

DATABASE_SCHEMA.md (≥3 tables)
API_ENDPOINTS.md (≥5 endpoints)
ARCHITECTURE.md (multiple services)
UI_COMPONENTS.md (shadcn/ui project)
CRITICAL_WORKFLOWS.md (complex setup)
INSTALLATION_COMMANDS.md (recommended)
ENV_VARIABLES.md (needs secrets)
TESTING.md, AGENTS_CONFIG.MD, INTEGRATION.MD (as needed)
Step 4: Generate IMPLEMENTATION_PHASES.md

Create structured phases using these types:

Phase Type: Infrastructure

When: Project start, deployment setup Scope: Scaffolding, build config, initial deployment Files: 3-5 (package.json, wrangler.jsonc, vite.config.ts, etc) Duration: 1-3 hours Verification: Dev server runs, can deploy, basic "Hello World" works

Phase Type: Database

When: Data model setup, schema changes Scope: Migrations, schema definition, seed data Files: 2-4 (migration files, schema types) Duration: 2-4 hours Verification: CRUD works, constraints enforced, relationships correct

Phase Type: API

When: Backend endpoints needed Scope: Routes, middleware, validation, error handling Files: 3-6 (route files, middleware, schemas) Duration: 3-6 hours (per endpoint group) Verification: All HTTP methods tested (200, 400, 401, 500), CORS works

Phase Type: UI

When: User interface components Scope: Components, forms, state, styling Files: 4-8 (component files) Duration: 4-8 hours (per feature) Verification: User flows work, forms validate, states update, responsive

Phase Type: Integration

When: Third-party services (auth, payments, AI, etc) Scope: API setup, webhooks, configuration Files: 2-4 (integration files, middleware) Duration: 3-5 hours (per integration) Verification: Service works, webhooks fire, errors handled

Phase Type: Testing

When: Need formal test suite (optional) Scope: E2E tests, integration tests Files: Test files Duration: 3-6 hours Verification: Tests pass, coverage meets threshold

Phase Validation Rules

Every phase you generate MUST follow these constraints:

Context-Safe Sizing
Max files: 5-8 files touched per phase
Max dependencies: Phase shouldn't require deep understanding of >2 other phases
Max duration: Implementation + verification + fixes should fit in one 2-4 hour session
Required Elements

Every phase MUST have:

Type - Infrastructure / Database / API / UI / Integration / Testing
Estimated duration - In hours (and minutes of human time)
Files - Specific files that will be created/modified
Task list - Ordered checklist with clear actions
Verification criteria - Checkbox list of tests to confirm phase works
Exit criteria - Clear definition of "done"
Verification Requirements
API phases: Test all HTTP status codes (200, 400, 401, 404, 500)
UI phases: Test user flows, form validation, error states
Database phases: Test CRUD, constraints, relationships
Integration phases: Test service connectivity, webhooks, error handling
Auto-Split Logic

If a phase violates sizing rules, automatically suggest splitting:

⚠️ Phase 4 "Complete User Management" is too large (12 files, 8-10 hours).

Suggested split:
- Phase 4a: User CRUD API (5 files, 4 hours)
- Phase 4b: User Profile UI (6 files, 5 hours)

Template Structures
IMPLEMENTATION_PHASES.md Template
# Implementation Phases: [Project Name]

**Project Type**: [Web App / Dashboard / API / etc]
**Stack**: Cloudflare Workers + Vite + React + D1
**Estimated Total**: [X hours] (~[Y minutes] human time)

---

## Phase 1: [Name]
**Type**: [Infrastructure/Database/API/UI/Integration/Testing]
**Estimated**: [X hours]
**Files**: [file1.ts, file2.tsx, ...]

**Tasks**:
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3
- [ ] Test basic functionality

**Verification Criteria**:
- [ ] Specific test 1
- [ ] Specific test 2
- [ ] Specific test 3

**Exit Criteria**: [Clear definition of when this phase is complete]

---

## Phase 2: [Name]
[... repeat structure ...]

---

## Notes

**Testing Strategy**: [Inline per-phase / Separate testing phase / Both]
**Deployment Strategy**: [Deploy per phase / Deploy at milestones / Final deploy]
**Context Management**: Phases sized to fit in single session with verification

DATABASE_SCHEMA.md Template
# Database Schema: [Project Name]

**Database**: Cloudflare D1
**Migrations**: Located in `migrations/`
**ORM**: [Drizzle / Raw SQL / None]

---

## Tables

### `users`
**Purpose**: User accounts and authentication

| Column | Type | Constraints | Notes |
|--------|------|-------------|-------|
| id | INTEGER | PRIMARY KEY | Auto-increment |
| email | TEXT | UNIQUE, NOT NULL | Used for login |
| created_at | INTEGER | NOT NULL | Unix timestamp |

**Indexes**:
- `idx_users_email` on `email` (for login lookups)

**Relationships**:
- One-to-many with `tasks`

---

### `tasks`
[... repeat structure ...]

---

## Migrations

### Migration 1: Initial Schema
**File**: `migrations/0001_initial.sql`
**Creates**: users, tasks tables

### Migration 2: Add Tags
**File**: `migrations/0002_tags.sql`
**Creates**: tags, task_tags tables

---

## Seed Data

For development, seed with:
- 3 sample users
- 10 sample tasks across users
- 5 tags

API_ENDPOINTS.md Template
# API Endpoints: [Project Name]

**Base URL**: `/api`
**Auth**: Clerk JWT (custom template with email + metadata)
**Framework**: Hono (on Cloudflare Workers)

---

## Authentication

### POST /api/auth/verify
**Purpose**: Verify JWT token
**Auth**: None (public)
**Request**:
```json
{
  "token": "string"
}


Responses:

200: Token valid → { "valid": true, "email": "user@example.com" }
401: Token invalid → { "error": "Invalid token" }
Users
GET /api/users/me

Purpose: Get current user profile Auth: Required (JWT) Responses:

200: { "id": 1, "email": "user@example.com", "created_at": 1234567890 }
401: Not authenticated

[... repeat for all endpoints ...]

Error Handling

All endpoints return errors in this format:

{
  "error": "Human-readable message",
  "code": "ERROR_CODE",
  "details": {} // optional
}


Standard Codes:

400: Bad request (validation failed)
401: Unauthorized (not logged in / invalid token)
403: Forbidden (insufficient permissions)
404: Not found
500: Internal server error

### ARCHITECTURE.md Template

```markdown
# Architecture: [Project Name]

**Deployment**: Cloudflare Workers
**Frontend**: Vite + React (served as static assets)
**Backend**: Worker handles API routes

---

## System Overview



┌─────────────────┐ │ Browser │ └────────┬────────┘ │ ↓ HTTPS ┌─────────────────────────────────────┐ │ Cloudflare Worker │ │ ┌──────────────┐ ┌──────────────┐│ │ │ Static Assets│ │ API Routes ││ │ │ (Vite build) │ │ (Hono) ││ │ └──────────────┘ └───────┬──────┘│ └─────────────────────────────┼───────┘ │ ┌─────────────────┼─────────────────┐ ↓ ↓ ↓ ┌──────────┐ ┌──────────┐ ┌──────────┐ │ D1 │ │ R2 │ │ Clerk │ │ (Database)│ │(Storage) │ │ (Auth) │ └──────────┘ └──────────┘ └──────────┘


---

## Data Flow

### User Authentication
1. User submits login form
2. Frontend sends credentials to Clerk
3. Clerk returns JWT
4. Frontend includes JWT in API requests
5. Worker middleware verifies JWT
6. Protected routes accessible

### Task Creation
1. User submits task form
2. Frontend validates with Zod
3. POST /api/tasks with validated data
4. Worker validates again server-side
5. Insert into D1 database
6. Return created task
7. Frontend updates UI via TanStack Query

[... more flows as needed ...]

---

## Service Boundaries

**Frontend Responsibilities**:
- User interaction
- Client-side validation
- Optimistic updates
- State management (TanStack Query + Zustand)

**Worker Responsibilities**:
- Request routing
- Authentication/authorization
- Server-side validation
- Business logic
- Database operations
- Third-party API calls

**Cloudflare Services**:
- D1: Persistent relational data
- R2: File storage (images, documents)
- KV: Configuration, feature flags, cache

---

## Security

**Authentication**: Clerk JWT with custom claims
**Authorization**: Middleware checks user ownership before mutations
**Input Validation**: Zod schemas on client AND server
**CORS**: Restricted to production domain
**Secrets**: Environment variables in wrangler.jsonc (not committed)

UI_COMPONENTS.md Template (Enhanced with Phase-Aligned Installation)

Use when: Project uses shadcn/ui OR needs component planning

# UI Components: [Project Name]

**Framework:** shadcn/ui + Tailwind v4
**Installation:** Components copied to @/components/ui (fully customizable)
**Strategy:** Install components as needed per phase (not all upfront)

---

## Installation Strategy: By Phase

### Phase [N]: [Phase Name] ([X] components)

**When:** During [description of when this phase happens]

**Components:**
- `button` - [specific use cases in this phase]
- `input` - [specific use cases]
- `card` - [specific use cases]
[... list all components for this phase ...]

**Install:**
\`\`\`bash
pnpm dlx shadcn@latest add button input card [...]
\`\`\`

**Usage:** [Which routes/features use these]

**Critical Notes:**
- [Any gotchas, e.g., "Use sonner instead of toast for better UX"]
- [Component-specific warnings, e.g., "data-table essential for TanStack Table integration"]

---

[Repeat for each phase...]

---

## Quick Reference Commands

### MVP Install (All Core Components)
\`\`\`bash
pnpm dlx shadcn@latest add button input label card sonner [essential components...]
\`\`\`

### Full Featured Install
\`\`\`bash
pnpm dlx shadcn@latest add button input [all components...]
\`\`\`

### Update All Components
\`\`\`bash
pnpm dlx shadcn@latest update
\`\`\`

---

## Component Usage by Route

### [Route Name] (\`/route\`)
- [List of components used]

[Repeat for each major route...]

---

## Design Decisions

### [Component Choice 1]
**Recommendation:** [Chosen component]
**Why:** [Justification]
**Alternatives considered:** [What else was evaluated]
**Savings:** [Time/token savings if applicable]

[Repeat for each significant component decision...]

---

## Component Count Breakdown

### By Category
- **Forms:** X components ([list])
- **Data Display:** X components ([list])
- **Feedback:** X components ([list])
- **Layout:** X components ([list])
- **Navigation:** X components ([list])

### By Priority
- **Essential (MVP):** X components
- **Recommended:** X additional components
- **Optional (Enhanced UX):** X additional components

---

## Installation Checklist

### Phase [N]: [Name] ✅
- [ ] component1
- [ ] component2
[...]

[Repeat for each phase...]

---

## Best Practices

1. **Install as Needed** - Don't install all components upfront. Add them when implementing the feature.
2. **Customize After Installation** - All components copied to @/components/ui are fully customizable.
3. **Keep Components Updated** - Run \`pnpm dlx shadcn@latest update\` periodically.
4. **Check for New Components** - shadcn/ui adds new components regularly.
5. **Dark Mode Works Automatically** - All components respect Tailwind v4 theming.
6. **Bundle Size Optimization** - Only installed components are included - unused code is tree-shaken.

---

## References

- **shadcn/ui Docs:** https://ui.shadcn.com/docs/components
- **Tailwind v4 Integration:** See \`tailwind-v4-shadcn\` skill
- **Component Installation:** https://ui.shadcn.com/docs/installation/vite

CRITICAL_WORKFLOWS.md Template (NEW)

Use when: User mentioned complex setup steps OR order-sensitive workflows

# Critical Workflows: [Project Name]

**Purpose:** Document non-obvious setup steps and order-sensitive workflows to prevent getting stuck

**Date:** [YYYY-MM-DD]

---

## ⚠️ [Workflow Name 1] ([Phase it applies to])

**STOP! Read this before [starting X].**

**Context:** [Why this workflow is tricky]

**Order matters:**
1. [Step 1 with specific command/action]
2. [Step 2]
3. [Step 3]
[...]

**Why this order:** [Explanation of what breaks if done wrong]

**Code Example:**
\`\`\`bash
# Step 1: [Description]
[command]

# Step 2: [Description]
[command]
\`\`\`

**Common Mistake:** [What people typically do wrong]
**Fix if broken:** [How to recover]

---

## ⚠️ [Workflow Name 2]

[Repeat structure...]

---

## Quick Checklist

Before starting each phase, check if it has critical workflows:

- [ ] Phase [N]: [Workflow name] (see above)
- [ ] Phase [N+1]: No critical workflows
- [ ] Phase [N+2]: [Workflow name] (see above)

---

## References

- **[Link to official docs]**
- **[Link to GitHub issue explaining gotcha]**
- **[Link to skill that prevents this issue]**

INSTALLATION_COMMANDS.md Template (NEW)

Use when: All projects (recommended) - saves massive time

# Installation Commands: [Project Name]

**Purpose:** Copy-paste commands for each phase (no more "what was that command again?")

**Date:** [YYYY-MM-DD]

---

## Phase 0: Planning
[None - just docs]

---

## Phase 1: [Phase Name]

### Scaffold Project
\`\`\`bash
npm create cloudflare@latest -- --framework=[framework]
cd [project-name]
\`\`\`

### Install Dependencies
\`\`\`bash
pnpm add [packages]
pnpm add -D [dev-packages]
\`\`\`

### Initialize Tools
\`\`\`bash
npx [tool] init
\`\`\`

### Verify Setup
\`\`\`bash
pnpm dev
# Should see: [expected output]
\`\`\`

---

## Phase 2: [Phase Name]

[Repeat structure for each phase...]

---

## Database Commands (Phase [N])

### Create Database
\`\`\`bash
npx wrangler d1 create [db-name]
# Copy database_id and add to wrangler.jsonc under [[d1_databases]]
\`\`\`

### Run Migrations
\`\`\`bash
# Local (dev)
npx wrangler d1 execute [db-name] --local --file=migrations/0001_initial.sql

# Production
npx wrangler d1 execute [db-name] --remote --file=migrations/0001_initial.sql
\`\`\`

### Query Database
\`\`\`bash
# Local
npx wrangler d1 execute [db-name] --local --command="SELECT * FROM users"

# Production
npx wrangler d1 execute [db-name] --remote --command="SELECT * FROM users"
\`\`\`

---

## Deployment Commands

### Deploy to Cloudflare
\`\`\`bash
npm run build
npx wrangler deploy
\`\`\`

### Set Production Secrets
\`\`\`bash
npx wrangler secret put [SECRET_NAME]
# Enter value when prompted
\`\`\`

### Check Deployment
\`\`\`bash
npx wrangler tail
# Watch logs in real-time
\`\`\`

---

## Development Commands

### Start Dev Server
\`\`\`bash
pnpm dev
\`\`\`

### Run Tests
\`\`\`bash
pnpm test
\`\`\`

### Lint & Format
\`\`\`bash
pnpm lint
pnpm format
\`\`\`

---

## Troubleshooting Commands

### Clear Build Cache
\`\`\`bash
rm -rf dist/ .wrangler/
pnpm dev
\`\`\`

### Check Wrangler Version
\`\`\`bash
npx wrangler --version
# Should be: [expected version]
\`\`\`

### Verify Bindings
\`\`\`bash
npx wrangler d1 list
npx wrangler r2 bucket list
\`\`\`

ENV_VARIABLES.md Template (NEW)

Use when: Project needs API keys OR environment configuration

# Environment Variables: [Project Name]

**Purpose:** All secrets, API keys, and configuration needed for this project

**Date:** [YYYY-MM-DD]

---

## Development (.dev.vars)

**File:** \`.dev.vars\` (local file, NOT committed to git)

\`\`\`bash
# Auth
CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...

# Database
DATABASE_URL=local

# API Keys
[SERVICE]_API_KEY=[value]

# Feature Flags
ENABLE_[FEATURE]=true
\`\`\`

**How to get these keys:**
1. **Clerk Keys:** https://dashboard.clerk.com → API Keys
2. **[Other Service]:** [Steps to obtain]

---

## Production (wrangler.jsonc secrets)

**Secrets (set via CLI):**
\`\`\`bash
# Set via: npx wrangler secret put SECRET_NAME
CLERK_SECRET_KEY=sk_live_...
[SERVICE]_API_KEY=[production-value]
\`\`\`

**Bindings (configured in wrangler.jsonc):**
\`\`\`jsonc
{
  "name": "[project-name]",
  "d1_databases": [
    {
      "binding": "DB",
      "database_name": "[db-name]",
      "database_id": "[copy from wrangler d1 create output]"
    }
  ],
  "r2_buckets": [
    {
      "binding": "BUCKET",
      "bucket_name": "[bucket-name]"
    }
  ],
  "kv_namespaces": [
    {
      "binding": "KV",
      "id": "[namespace-id]"
    }
  ]
}
\`\`\`

---

## Environment Variable Reference

| Variable | Required | Where Used | Notes |
|----------|----------|------------|-------|
| CLERK_PUBLISHABLE_KEY | Yes | Frontend | Public, safe to commit in example files |
| CLERK_SECRET_KEY | Yes | Worker | SECRET - never commit |
| DATABASE_URL | Local only | Development | Points to local .wrangler/state |
| [OTHER_VAR] | [Yes/No] | [Where] | [Notes] |

---

## Setup Checklist

### Local Development
- [ ] Create \`.dev.vars\` in project root
- [ ] Add \`.dev.vars\` to \`.gitignore\` (should already be there)
- [ ] Copy values from \`.dev.vars.example\` (if exists)
- [ ] Get API keys from services (links above)
- [ ] Run \`pnpm dev\` to verify

### Production Deployment
- [ ] Set all secrets via \`npx wrangler secret put\`
- [ ] Configure all bindings in \`wrangler.jsonc\`
- [ ] Deploy: \`npx wrangler deploy\`
- [ ] Verify secrets are set: \`npx wrangler secret list\`
- [ ] Test production deployment

---

## Security Notes

**Never commit:**
- \`.dev.vars\`
- Any file with actual secret values
- Production API keys

**Safe to commit:**
- \`.dev.vars.example\` (with placeholder values)
- \`wrangler.jsonc\` (bindings config, NOT secret values)
- Public keys (Clerk publishable key, etc.)

**If secrets leaked:**
1. Rotate all affected keys immediately
2. Update production secrets: \`npx wrangler secret put [KEY]\`
3. Revoke old keys in service dashboards
4. Check git history for leaked secrets

---

## References

- **Cloudflare Secrets:** https://developers.cloudflare.com/workers/configuration/secrets/
- **Wrangler Configuration:** https://developers.cloudflare.com/workers/wrangler/configuration/
- **[Service] API Docs:** [link]

Compact SESSION.md Template (NEW)

Always generate this - for tracking progress

# Session State

**Current Phase**: Phase 0 (Planning)
**Current Stage**: Planning
**Last Checkpoint**: None yet
**Planning Docs**: \`docs/IMPLEMENTATION_PHASES.md\`, \`docs/CRITICAL_WORKFLOWS.md\` (if exists)

---

## Phase 0: Planning ✅
**Completed**: [YYYY-MM-DD]
**Summary**: Planning docs created
**Deliverables**: [List generated docs]

## Phase 1: [Name] ⏸️
**Spec**: \`docs/IMPLEMENTATION_PHASES.md#phase-1\`
**Type**: [Infrastructure/Database/API/UI/Integration]
**Time**: [X hours]
**Progress**: Not started
**Next Action**: [Specific file + line + what to do]

## Phase 2: [Name] ⏸️
**Spec**: \`docs/IMPLEMENTATION_PHASES.md#phase-2\`
**Type**: [Type]
**Time**: [X hours]
**Progress**: Not started

[Collapse remaining phases to 2-3 lines each...]

---

## Critical Reminders

**Before Starting:**
- [ ] Read \`docs/CRITICAL_WORKFLOWS.md\` (if exists)
- [ ] Review \`docs/INSTALLATION_COMMANDS.md\` for phase commands
- [ ] Check \`docs/ENV_VARIABLES.md\` for required secrets

**Critical Workflows:**
[Link to specific workflows from CRITICAL_WORKFLOWS.md, if exists]

---

## Known Risks

**High-Risk Phases:**
- Phase [N]: [Name] - [Why risky]
- Phase [N+1]: [Name] - [Why risky]

**Mitigation:** [Strategy]

---

**Status Legend**: ⏸️ Pending | 🔄 In Progress | ✅ Complete | 🚫 Blocked | ⚠️ Issues

File-Level Detail in Phases

Purpose: Help Claude navigate code with file maps, data flow diagrams, and gotchas.

Include for: API, UI, Integration phases (optional for Infrastructure, Database, Testing)

File Map Example
### File Map
- `src/routes/tasks.ts` (~150 lines) - CRUD endpoints
  - Purpose, Key exports, Dependencies, Used by
- `src/lib/schemas.ts` (~80 lines) - Validation schemas
- `src/middleware/auth.ts` (existing, no changes)

Data Flow Diagrams

Use Mermaid for sequence diagrams (API), flowcharts (UI), architecture diagrams:

\`\`\`mermaid
sequenceDiagram
    Client->>Worker: POST /api/tasks
    Worker->>Auth: authenticateUser()
    Auth->>Worker: user object
    Worker->>D1: INSERT INTO tasks
    D1->>Worker: task record
    Worker->>Client: 201 + JSON
\`\`\`

Critical Dependencies & Gotchas
**Internal**: auth.ts, schemas.ts, D1 binding
**External**: zod, hono, @clerk/backend
**Configuration**: CLERK_SECRET_KEY
**Bindings**: DB (D1)

**Gotchas**:
- Ownership verification (PATCH/DELETE must check user_id)
- Pagination required (50 max per page)
- Soft delete (deleted_at, not DELETE FROM)
- UTC timestamps (convert in frontend only)

Complete Phase Example (with File-Level Detail)
## Phase 3: Tasks API
**Type**: API | **Estimated**: 4 hours
**Files**: src/routes/tasks.ts, src/lib/schemas.ts, src/middleware/auth.ts (modify)

### File Map
- src/routes/tasks.ts (~150 lines) - CRUD endpoints
- src/lib/schemas.ts (+40 lines) - Validation schemas

### Data Flow
\`\`\`mermaid
sequenceDiagram
    Client->>Worker: POST /api/tasks
    Worker->>Auth: authenticateUser()
    Worker->>D1: INSERT
    D1->>Worker: task
    Worker->>Client: 201
\`\`\`

### Dependencies & Gotchas
**Internal**: auth.ts, schemas.ts, D1
**External**: zod, hono, @clerk/backend
**Gotchas**: Ownership checks, pagination (50 max), soft delete, UTC timestamps

### Tasks
- [ ] Create schemas
- [ ] GET /api/tasks (paginated)
- [ ] POST /api/tasks (validated)
- [ ] PATCH /api/tasks/:id (ownership check)
- [ ] DELETE /api/tasks/:id (soft delete)

### Verification
- [ ] GET returns 200 + array
- [ ] POST valid→201, invalid→400
- [ ] PATCH checks ownership (403 if wrong user)
- [ ] DELETE sets deleted_at
- [ ] All require JWT (401 if missing)

### Exit Criteria
All CRUD works with correct status codes, validation, auth, ownership. Paginated. Soft deletes.

Generation Logic
Analyze project description
Ask 3-5 clarifying questions
Wait for answers
Determine which docs to generate
Generate all docs immediately (key step - before coding)
Validate phases (≤8 files, ≤4 hours)
Output docs to /docs
Wait for user review
Suggest creating SESSION.md and starting Phase 1
Special Cases
AI Apps: Ask AI provider, suggest AGENTS_CONFIG.md, add Integration phase
Real-Time: Suggest Durable Objects, add Infrastructure phase for DO
High Scale: Ask load expectations, suggest caching (KV, R2), Hyperdrive
Legacy Integration: Ask integration points, suggest INTEGRATION.md
Quality Checklist

✅ Every phase: Type, time, files, tasks, verification, exit criteria ✅ Context-safe: ≤8 files, ≤2 dependencies, fits in 2-4hr session ✅ Verification specific: "valid login→200+token, invalid→401" not "test feature" ✅ Exit criteria clear: "All endpoints correct status codes" not "API done" ✅ Logical order: Infrastructure→Database→API→UI→Integration→Testing ✅ Realistic estimates: Include implementation+verification+fixes

Output Format

Generate docs immediately after user confirms. Present as markdown files or code blocks.

Include: Full IMPLEMENTATION_PHASES.md + conditional docs (DATABASE_SCHEMA.md, API_ENDPOINTS.md, etc.) + Summary (phases, duration, deployment strategy, docs created)

Common Mistakes to Avoid
SESSION.md too verbose (<200 lines, reference IMPLEMENTATION_PHASES.md)
Vague next action ("Continue API" → "Implement POST /api/tasks in src/routes/tasks.ts:47")
No critical workflows documented
Planning before prototyping (build spike first for new frameworks)
Your Role

Planning assistant - Structure work into manageable, context-safe phases with clear verification.

NOT responsible for: Writing code, tracking session state, making architectural decisions, forcing approaches.

Weekly Installs
582
Repository
jezweb/claude-skills
GitHub Stars
759
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn