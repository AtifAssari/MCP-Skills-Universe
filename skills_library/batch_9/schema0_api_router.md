---
title: schema0-api-router
url: https://skills.sh/schema0/skills/schema0-api-router
---

# schema0-api-router

skills/schema0/skills/schema0-api-router
schema0-api-router
Installation
$ npx skills add https://github.com/schema0/skills --skill schema0-api-router
SKILL.md
API Router

STOP before writing any router.

New routers MUST use createDb() against a Drizzle table.
users.ts and files.ts are NOT templates. They call platform endpoints purpose-built for the users and files platform features — there is no Drizzle table behind them. Your application's entities are application data and go through your own tables; do not copy users.ts / files.ts for any new entity.
If your entity has no Drizzle table yet, invoke schema0-db-schema first to define one.
File Location
packages/api/src/
├── index.ts           # Base procedures (publicProcedure, protectedProcedure)
├── context.ts         # Request context type
└── routers/
    ├── index.ts       # App router (register all routers here)
    └── [entity].ts    # Entity-specific CRUD routers

Prerequisites

Every router provides 5 bulk CRUD operations: selectAll, selectById, insertMany, updateMany, deleteMany.

Base Procedures
import { ORPCError, os } from "@orpc/server";
import type { Context } from "./context";

export const o = os.$context<Context>();
export const publicProcedure = o;

const requireAuth = o.middleware(async ({ context, next }) => {
  if (!context.session?.user) {
    throw new ORPCError("UNAUTHORIZED");
  }
  return next({ context: { session: context.session } });
});

export const protectedProcedure = publicProcedure.use(requireAuth);

Error Handling (ORPCError)
import { ORPCError } from "@orpc/server";

// CORRECT -- string code + options object
throw new ORPCError("NOT_FOUND", { status: 404, message: "Resource not found" });
throw new ORPCError("CONFLICT", { status: 409, message: "Already exists" });

// WRONG -- object with code property
throw new ORPCError({ code: "NOT_FOUND", message: "Not found" });

Nested Routers
// packages/api/src/routers/admin/users.ts
export const adminUsersRouter = { list: protectedProcedure.handler(async () => { ... }) };

// packages/api/src/routers/admin/index.ts
export const adminRouter = { users: adminUsersRouter };

// packages/api/src/routers/index.ts
export const appRouter = { admin: adminRouter };
// Client: orpc.admin.users.list.queryOptions()

Key Rules
Use .handler() for ALL procedures -- NEVER .query() or .mutation() (tRPC patterns).
Use createDb() inside each handler -- never module-level singleton.
NEVER use fetchCustomResources for new routers -- only for built-in files.ts and users.ts.
Use import { z } from "zod/v4" -- NEVER import z from "zod".
Import schemas from @template/db/schema -- NEVER define z.object() schemas inline.
Use {entity}RouterOutputSchema for .output() -- must match DB return types.
Bulk operations only -- insertMany, updateMany, deleteMany for TanStack DB optimistic updates.
Data MUST be stored in database -- every mutation must hit DB and return persisted result.
Register in packages/api/src/routers/index.ts after creating.
References
references/crud-template.md -- Full CRUD router code template (selectAll, selectById, insertMany, updateMany, deleteMany) + registration example
Weekly Installs
17
Repository
schema0/skills
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass