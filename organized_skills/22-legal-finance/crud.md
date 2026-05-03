---
rating: ⭐⭐⭐
title: crud
url: https://skills.sh/chachamaru127/claude-code-harness/crud
---

# crud

skills/chachamaru127/claude-code-harness/crud
crud
Installation
$ npx skills add https://github.com/chachamaru127/claude-code-harness --skill crud
SKILL.md
CRUD Skill

Auto-generates CRUD functionality for specified entities (tables) at production-ready level.

Quick Reference
"Create CRUD for task management" → /crud tasks
"Want search and pagination too" → Includes all together
"Include permissions (who can view/edit)" → Sets up authorization/rules together
Deliverables
CRUD + validation + authorization + tests, complete production-safe set
Minimize diff to match existing DB/code

Features:

Validation (Zod) auto-add
Auth/authorization (Row Level Security) auto-config
Relations (one-to-many, many-to-many) support
Pagination, search, filters
Auto-generated test cases
Auto-invoke Skills

This skill must explicitly invoke the following skills with the Skill tool:

Skill	Purpose	When to Call
impl	Implementation (parent skill)	CRUD feature implementation
verify	Verification (parent skill)	Post-implementation verification
Execution Flow

Detailed steps are described in the phases below.

Phase 1: Entity Analysis
Parse entity name from $ARGUMENTS
Detect existing schema (Prisma, Drizzle, raw SQL)
Infer field types and relations
Phase 2: CRUD Generation
Generate model/schema if needed
Create API endpoints (REST or tRPC)
Add validation schemas (Zod)
Configure authorization rules
Phase 3: Test Generation
Create unit tests for each endpoint
Add integration tests
Generate test fixtures
Phase 4: Verification
Run type check
Run tests
Verify build
Supported Frameworks
Framework	Detection	Generated Files
Next.js + Prisma	prisma/schema.prisma	API routes, Prisma client
Next.js + Drizzle	drizzle.config.ts	API routes, Drizzle queries
Express	express in package.json	Controllers, routes
Hono	hono in package.json	Route handlers
Output Structure
src/
├── lib/
│   └── validations/
│       └── {entity}.ts        # Zod schemas
├── app/api/{entity}/
│   ├── route.ts              # GET (list), POST (create)
│   └── [id]/
│       └── route.ts          # GET, PUT, DELETE
└── tests/
    └── {entity}.test.ts      # Test cases

Related Skills
impl - Feature implementation
verify - Build verification
auth - Authentication/authorization
Weekly Installs
32
Repository
chachamaru127/c…-harness
GitHub Stars
598
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass