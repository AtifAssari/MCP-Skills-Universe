---
rating: ⭐⭐⭐
title: zenstack
url: https://skills.sh/beshkenadze/claude-skills-marketplace/zenstack
---

# zenstack

skills/beshkenadze/claude-skills-marketplace/zenstack
zenstack
Installation
$ npx skills add https://github.com/beshkenadze/claude-skills-marketplace --skill zenstack
SKILL.md
ZenStack Skill

ZenStack is a TypeScript toolkit that enhances Prisma ORM with flexible Authorization layer (RBAC/ABAC/PBAC/ReBAC) and auto-generated type-safe APIs.

When to Use
Defining access control policies in ZModel
Setting up ZenStack with Prisma/tRPC/Next.js
Implementing RBAC, ABAC, or multi-tenant authorization
Generating tRPC routers from ZModel
Adding field-level validation
Quick Start
Installation
npm install zenstack @zenstackhq/runtime
npx zenstack init

Generate from ZModel
npx zenstack generate

Access Policy Syntax
Model-Level Policies
model Post {
    id        Int     @id @default(autoincrement())
    title     String
    published Boolean @default(false)
    author    User    @relation(fields: [authorId], references: [id])
    authorId  Int

    // Deny anonymous access
    @@deny('all', auth() == null)

    // Published posts readable by anyone
    @@allow('read', published)

    // Author has full access
    @@allow('all', auth().id == authorId)
}

Operations
Operation	Description
'all'	All CRUD operations
'create'	Create only
'read'	Read only
'update'	Update only
'delete'	Delete only
'create,read'	Multiple operations
Policy Rules
@@deny takes precedence over @@allow
Policies are evaluated at runtime
auth() returns current user or null
RBAC Example
model Post {
    id    Int    @id @default(autoincrement())
    title String

    // Only admins have full access
    @@allow('all', auth().role == 'ADMIN')

    // Users can read
    @@allow('read', auth().role == 'USER')
}

ABAC Example
model Resource {
    id        Int     @id @default(autoincrement())
    name      String
    published Boolean @default(false)
    owner     User    @relation(fields: [ownerId], references: [id])
    ownerId   Int

    // Reputation-based creation
    @@allow('create', auth().reputation >= 100)

    // Published resources are public
    @@allow('read', published)

    // Owner has full access
    @@allow('read,update,delete', owner == auth())
}

Multi-Tenant Example
model Organization {
    id      Int    @id @default(autoincrement())
    name    String
    members User[]
    posts   Post[]
}

model Post {
    id     Int          @id @default(autoincrement())
    title  String
    org    Organization @relation(fields: [orgId], references: [id])
    orgId  Int

    // Only org members can access
    @@allow('all', org.members?[id == auth().id])
}

Field-Level Policies
model User {
    id       Int    @id
    email    String @allow('read', auth().id == id)
    password String @deny('read', true) // Never readable
    salary   Int    @allow('read', auth().role == 'HR')
}

Field-Level Attributes
@allow('read', condition) — Allow field read
@allow('update', condition) — Allow field update
@deny('read', condition) — Deny field read
@deny('update', condition) — Deny field update
Data Validation
model User {
    id       String @id @default(cuid())
    name     String @length(min: 3, max: 20)
    email    String @email
    age      Int?   @gte(18)
    password String @length(min: 8, max: 32)
    url      String @url
}

Validation Attributes
Attribute	Description
@email	Valid email format
@url	Valid URL format
@length(min, max)	String length
@gt(n) / @gte(n)	Greater than (or equal)
@lt(n) / @lte(n)	Less than (or equal)
@regex(pattern)	Regex match
@startsWith(str)	String prefix
@endsWith(str)	String suffix
tRPC Integration
Plugin Configuration
plugin trpc {
    provider = '@zenstackhq/trpc'
    output = 'src/server/routers/generated'
}

Context Setup
import { enhance } from '@zenstackhq/runtime';
import { prisma } from './db';
import { getSession } from './auth';

export const createContext = async ({ req, res }) => {
    const session = await getSession(req, res);
    return {
        session,
        // Enhanced Prisma client with access policies
        prisma: enhance(prisma, { user: session?.user }),
    };
};

Using Generated Routers
import { createTRPCRouter } from './trpc';
import { createRouter } from './routers/generated/routers';

export const appRouter = createTRPCRouter({
    ...createRouter(createTRPCRouter, procedure),
});

Enhanced Prisma Client
import { PrismaClient } from '@prisma/client';
import { enhance } from '@zenstackhq/runtime';

const prisma = new PrismaClient();

// Create enhanced client with user context
const db = enhance(prisma, { user: currentUser });

// All queries now respect access policies
const posts = await db.post.findMany(); // Only returns allowed posts

Common Patterns
Soft Delete with Policy
model Post {
    id        Int      @id
    deleted   Boolean  @default(false)
    deletedAt DateTime?

    // Hide soft-deleted posts
    @@deny('read', deleted)

    // Allow owner to "delete" (soft delete)
    @@allow('update', auth().id == authorId && future().deleted)
}

Time-Based Access
model Content {
    id          Int      @id
    publishedAt DateTime?

    // Only show published content
    @@allow('read', publishedAt != null && publishedAt <= now())
}

Hierarchical Access
model Document {
    id       Int       @id
    parent   Document? @relation("children", fields: [parentId], references: [id])
    parentId Int?
    children Document[] @relation("children")

    // Access if user can access parent
    @@allow('read', parent == null || parent.canRead(auth()))
}

CLI Commands
# Initialize ZenStack in project
npx zenstack init

# Generate Prisma schema and artifacts
npx zenstack generate

# Format ZModel file
npx zenstack format

Examples
Example: Add RBAC to Existing Model

Input:

Add role-based access control to my Post model


Output:

model Post {
  id        Int     @id @default(autoincrement())
  title     String
  published Boolean @default(false)
  author    User    @relation(fields: [authorId], references: [id])
  authorId  Int

  // Deny anonymous access
  @@deny('all', auth() == null)

  // Admins have full access
  @@allow('all', auth().role == 'ADMIN')

  // Authors can manage their own posts
  @@allow('all', auth().id == authorId)

  // Anyone can read published posts
  @@allow('read', published)
}

Example: Multi-tenant Data Isolation

Input:

Isolate data by organization in a SaaS app


Output:

model Organization {
  id      Int    @id
  members User[]
  posts   Post[]
}

model Post {
  id    Int          @id
  org   Organization @relation(fields: [orgId], references: [id])
  orgId Int

  // Only org members can access posts
  @@allow('all', org.members?[id == auth().id])
}

Example: Soft Delete Pattern

Input:

Implement soft delete that hides deleted records automatically


Output:

model Post {
  id        Int       @id
  deleted   Boolean   @default(false)
  deletedAt DateTime?
  authorId  Int

  // Hide soft-deleted from normal queries
  @@deny('read', deleted)

  // Allow "delete" = set deleted flag
  @@allow('update', auth().id == authorId && future().deleted)
}

Example: v3 Migration Script

Input:

Update my package.json for ZenStack v3


Output:

{
  "scripts": {
    "generate": "zen generate",
    "db:push": "zen db push",
    "migrate:dev": "zen migrate dev",
    "migrate:deploy": "zen migrate deploy"
  }
}

Tips
Tip 1: Deny by Default Pattern

Start strict, then open up:

model Secret {
  id    Int    @id
  value String

  // Start with deny all
  @@deny('all', true)

  // Then whitelist specific access
  @@allow('read', auth().role == 'ADMIN')
}

Tip 2: Debug Policies with check()

Test permissions without hitting DB:

import { check } from '@zenstackhq/runtime';

const canCreate = await check(db).post.create({
  data: { title: 'Test' }
});
// Returns: { allowed: true/false, reason?: string }

Tip 3: Use future() for Update Validation

Validate the result of an update:

model User {
  id     Int    @id
  role   String
  salary Int

  // Can't give yourself a raise > 10%
  @@allow('update', future().salary <= salary * 1.1)
}

Tip 4: Field-Level Sensitive Data

Hide sensitive fields from unauthorized users:

model User {
  id       Int    @id
  email    String @allow('read', auth().id == id || auth().role == 'ADMIN')
  password String @deny('read', true) // Never readable via API
  ssn      String @allow('read', auth().role == 'HR')
}

Tip 5: v3 — Use Kysely for Complex Queries

When Prisma API isn't enough:

// Complex aggregation with window functions
const result = await db.$qb
  .selectFrom('Order')
  .select([
    'userId',
    sql`SUM(amount) OVER (PARTITION BY userId)`.as('totalSpent'),
    sql`ROW_NUMBER() OVER (ORDER BY amount DESC)`.as('rank')
  ])
  .execute();

Best Practices
Deny by default — Start with @@deny('all', true) then add specific allows
Use auth() consistently — Always check for null: auth() != null
Validate at schema level — Use validation attributes instead of app code
Test policies — Write tests for access control rules
Keep policies simple — Complex logic should be in helper functions
Prefer v3 for new projects — Lighter footprint, more features
Use check() for UI — Show/hide buttons based on permissions
Integration with Better Auth
// auth.ts
import { betterAuth } from 'better-auth';
import { prismaAdapter } from 'better-auth/adapters/prisma';
import { prisma } from './db';

export const auth = betterAuth({
    database: prismaAdapter(prisma, { provider: 'postgresql' }),
});

// context.ts - combine with ZenStack
import { enhance } from '@zenstackhq/runtime';

export const createContext = async ({ req }) => {
    const session = await auth.api.getSession({ headers: req.headers });
    return {
        prisma: enhance(prisma, { user: session?.user }),
    };
};

ZenStack v3 (Kysely-based)

ZenStack v3 is a complete rewrite — replaced Prisma ORM with its own engine built on Kysely.

Why v3?
Aspect	v2 (Prisma-based)	v3 (Kysely-based)
ORM Engine	Prisma runtime	Custom Kysely-based
node_modules	~224 MB (Prisma 7)	~33 MB
Architecture	Rust/WASM binaries	100% TypeScript
Query API	Prisma API only	Dual: Prisma + Kysely
Extensibility	Limited	Runtime plugins
JSON Fields	Generic object	Strongly typed
Inheritance	Not supported	Polymorphic @@delegate
v3 Dual API Design
// High-level ORM (Prisma-compatible)
await db.user.findMany({
  where: { age: { gt: 18 } },
  include: { posts: true }
});

// Low-level Kysely query builder (for complex queries)
await db.$qb
    .selectFrom('User')
    .leftJoin('Post', 'Post.authorId', 'User.id')
    .select(['User.id', 'User.email', 'Post.title'])
    .where('User.age', '>', 18)
    .execute();

v3 Strongly Typed JSON
type Address {
  street String
  city   String
  zip    String
}

model User {
  id      Int     @id
  address Address // Full type safety for JSON column
}

v3 Polymorphic Models
model Asset {
  id   Int    @id
  name String
  @@delegate(type)
}

model Image extends Asset {
  width  Int
  height Int
}

model Video extends Asset {
  duration Int
}

// Query returns discriminated union
const assets = await db.asset.findMany();
// assets[0].type === 'Image' → has width, height
// assets[0].type === 'Video' → has duration

v3 Computed Fields
model User {
  firstName String
  lastName  String
  fullName  String @computed
}

const db = new ZenStackClient(schema, {
  computedFields: {
    User: {
      // SQL: CONCAT(firstName, ' ', lastName)
      fullName: (eb) => eb.fn('concat', ['firstName', eb.val(' '), 'lastName'])
    },
  },
});

v3 Runtime Plugins
// Plugin to filter by age on all user queries
const extDb = db.$use({
  id: 'adult-only',
  onQuery: {
    user: {
      async findMany({ args, proceed }) {
        args.where = { ...args.where, age: { gt: 18 } };
        return proceed(args);
      },
    },
  },
});

Migration Guides
From Prisma to ZenStack
# Initialize ZenStack in existing Prisma project
npx zenstack@latest init

# With custom Prisma schema location
npx zenstack@latest init --prisma prisma/my.schema

# With specific package manager
npx zenstack@latest init --package-manager pnpm


Update package.json scripts:

{
  "scripts": {
    "db:push": "zen db push",
    "migrate:dev": "zen migrate dev",
    "migrate:deploy": "zen migrate deploy"
  }
}

From ZenStack v2 to v3
Replace Prisma dependencies with ZenStack
Update PrismaClient creation code
See v2 Migration Guide
See Prisma Migration Guide
Resources
ZenStack Docs
GitHub
ZModel Reference
tRPC Plugin
Migrate from Prisma
Migrate from v2
Weekly Installs
23
Repository
beshkenadze/cla…ketplace
GitHub Stars
2
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass