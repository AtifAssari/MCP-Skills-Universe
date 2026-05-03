---
rating: ⭐⭐⭐
title: database-layer
url: https://skills.sh/mgd34msu/goodvibes-plugin/database-layer
---

# database-layer

skills/mgd34msu/goodvibes-plugin/database-layer
database-layer
Installation
$ npx skills add https://github.com/mgd34msu/goodvibes-plugin --skill database-layer
SKILL.md
Resources
scripts/
  database-checklist.sh
references/
  orm-comparison.md

Database Layer Implementation

This skill guides you through implementing database layers in applications, from initial schema design to query optimization. It leverages GoodVibes precision tools and project analysis tools for type-safe, production-ready database implementations.

When to Use This Skill

Use this skill when you need to:

Set up a new database connection and ORM
Design and implement database schemas
Create and run migrations
Generate type-safe database clients
Write queries and handle relationships
Optimize database performance
Integrate with existing database infrastructure
Workflow

Follow this sequence for database layer implementation:

1. Discover Existing Database Infrastructure

Before implementing any database changes, understand the current state using the detect_stack analysis tool:

detect_stack:
  project_root: "."
  categories: ["database", "orm"]


This identifies:

Existing database technology (PostgreSQL, MySQL, MongoDB, SQLite)
ORM/query builder in use (Prisma, Drizzle, Kysely, Mongoose)
Schema definition files
Migration tooling
Connection management patterns

Check project memory for database decisions:

precision_read:
  files:
    - path: ".goodvibes/memory/decisions.json"
    - path: ".goodvibes/memory/patterns.json"
  verbosity: minimal


Look for:

Previous database technology choices ("Use Prisma for type safety")
Migration strategies ("Always use reversible migrations")
Performance patterns ("Add indexes for foreign keys")
Known issues ("Avoid N+1 queries in user endpoints")

If database already exists, map the current schema:

get_database_schema:
  project_root: "."
  include_relations: true
  include_indexes: true


This returns:

Table/collection definitions
Column types and constraints
Relationships (foreign keys, references)
Indexes and unique constraints
Enums and custom types
2. Choose Database Technology

If starting fresh, consult the ORM comparison reference to select the appropriate technology stack.

See: references/orm-comparison.md for decision trees.

Key decision factors:

Factor	Recommendation
Type safety priority	Prisma or Drizzle
Maximum SQL control	Kysely or Drizzle
Document database	Mongoose (MongoDB)
Serverless/edge	Drizzle with libSQL/Turso
Existing PostgreSQL	Prisma or Drizzle
Learning curve	Prisma (best DX)

Record your decision in memory:

After choosing, document the decision in .goodvibes/memory/decisions.json for future reference.

3. Design Schema

Identify entities and relationships first:

Entities: User, Post, Comment, Category

Relationships:
- User 1:N Post (author)
- Post N:M Category (through PostCategory)
- Post 1:N Comment
- User 1:N Comment (author)


Create schema files using precision_write:

For Prisma:

precision_write:
  files:
    - path: "prisma/schema.prisma"
      content: |
        generator client {
          provider = "prisma-client-js"
        }

        datasource db {
          provider = "postgresql"
          url      = env("DATABASE_URL")
        }

        model User {
          id        String   @id @default(cuid())
          email     String   @unique
          name      String?
          posts     Post[]
          comments  Comment[]
          createdAt DateTime @default(now())
          updatedAt DateTime @updatedAt
        }

        model Post {
          id         String     @id @default(cuid())
          title      String
          content    String
          published  Boolean    @default(false)
          author     User       @relation(fields: [authorId], references: [id])
          authorId   String
          categories Category[]
          comments   Comment[]
          createdAt  DateTime   @default(now())
          updatedAt  DateTime   @updatedAt

          @@index([authorId])
          @@index([published, createdAt])
        }

        model Category {
          id    String @id @default(cuid())
          name  String @unique
          posts Post[]
        }

        model Comment {
          id        String   @id @default(cuid())
          content   String
          post      Post     @relation(fields: [postId], references: [id])
          postId    String
          author    User     @relation(fields: [authorId], references: [id])
          authorId  String
          createdAt DateTime @default(now())

          @@index([postId])
          @@index([authorId])
        }
  verbosity: minimal


For Drizzle:

precision_write:
  files:
    - path: "src/db/schema.ts"
      content: |
        import { pgTable, text, timestamp, boolean, index } from 'drizzle-orm/pg-core';
        import { relations } from 'drizzle-orm';

        export const users = pgTable('users', {
          id: text('id').primaryKey().$defaultFn(() => crypto.randomUUID()),
          email: text('email').notNull().unique(),
          name: text('name'),
          createdAt: timestamp('created_at').defaultNow().notNull(),
          updatedAt: timestamp('updated_at').defaultNow().notNull(),
        });

        export const posts = pgTable('posts', {
          id: text('id').primaryKey().$defaultFn(() => crypto.randomUUID()),
          title: text('title').notNull(),
          content: text('content').notNull(),
          published: boolean('published').default(false).notNull(),
          authorId: text('author_id').notNull().references(() => users.id),
          createdAt: timestamp('created_at').defaultNow().notNull(),
          updatedAt: timestamp('updated_at').defaultNow().notNull(),
        }, (table) => ({
          authorIdx: index('author_idx').on(table.authorId),
          publishedCreatedIdx: index('published_created_idx').on(table.published, table.createdAt),
        }));

        export const usersRelations = relations(users, ({ many }) => ({
          posts: many(posts),
        }));

        export const postsRelations = relations(posts, ({ one }) => ({
          author: one(users, {
            fields: [posts.authorId],
            references: [users.id],
          }),
        }));
  verbosity: minimal


Schema best practices:

Use appropriate ID strategy:

CUID/UUID for distributed systems
Auto-increment for simple apps
Composite keys for join tables

Add timestamps:

Always include createdAt
Include updatedAt for mutable entities
Consider deletedAt for soft deletes

Index strategically:

Foreign keys (for joins)
Frequently queried fields
Composite indexes for multi-column filters
Unique constraints where applicable

Plan for scale:

Text vs VARCHAR limits
JSONB for flexible data (PostgreSQL)
Separate tables for large text/blobs
4. Configure Database Connection

Create environment configuration:

precision_write:
  files:
    - path: ".env.example"
      content: |
        # Database
        DATABASE_URL="postgresql://user:password@localhost:5432/dbname"
        # For Prisma with connection pooling
        # DATABASE_URL="postgresql://user:password@localhost:5432/dbname?pgbouncer=true"
        # DIRECT_URL="postgresql://user:password@localhost:5432/dbname"
      mode: overwrite
  verbosity: minimal


Create database client module:

For Prisma:

precision_write:
  files:
    - path: "src/lib/db.ts"
      content: |
        import { PrismaClient } from '@prisma/client';

        const globalForPrisma = globalThis as unknown as {
          prisma: PrismaClient | undefined;
        };

        export const db =
          globalForPrisma.prisma ??
          new PrismaClient({
            log:
              process.env.NODE_ENV === 'development'
                ? ['query', 'error', 'warn']
                : ['error'],
          });

        if (process.env.NODE_ENV !== 'production') {
          globalForPrisma.prisma = db;
        }
  verbosity: minimal


For Drizzle:

precision_write:
  files:
    - path: "src/lib/db.ts"
      content: |
        import { drizzle } from 'drizzle-orm/postgres-js';
        import postgres from 'postgres';
        import * as schema from '@/db/schema';

        const connectionString = process.env.DATABASE_URL!;

        const client = postgres(connectionString, {
          max: process.env.NODE_ENV === 'production' ? 10 : 1,
        });

        export const db = drizzle(client, { schema });
  verbosity: minimal

5. Run Migrations

Use precision_exec to run migration commands with expectations:

For Prisma:

precision_exec:
  commands:
    - cmd: "npx prisma migrate dev --name init"
      timeout_ms: 60000
      expect:
        exit_code: 0
      # Note: Prisma outputs progress to stderr; this is expected behavior
    - cmd: "npx prisma generate"
      expect:
        exit_code: 0
  verbosity: standard


For Drizzle:

precision_exec:
  commands:
    - cmd: "npx drizzle-kit generate"
      expect:
        exit_code: 0
    - cmd: "npx drizzle-kit push"
      timeout_ms: 60000
      expect:
        exit_code: 0
  verbosity: standard


Migration best practices:

Always review generated migrations before applying
Use reversible migrations (include both up and down)
Test migrations on dev database before production
Backup production data before running migrations
Use transactions for multi-step migrations
6. Generate Type-Safe Client

Use the generate_types project tool to generate TypeScript types from your schema:

generate_types:
  project_root: "."
  source: "database"
  output_path: "src/types/db.ts"


This creates type definitions for:

Table/collection types
Insert types (omitting auto-generated fields)
Update types (all fields optional)
Select types (with relations)

Verify type generation:

precision_exec:
  commands:
    - cmd: "npm run typecheck"
      expect:
        exit_code: 0
  verbosity: minimal

7. Implement Queries

Start with basic CRUD operations:

precision_write:
  files:
    - path: "src/db/queries/users.ts"
      content: |
        import { db } from '@/lib/db';

        export async function createUser(data: { email: string; name?: string }) {
          return db.user.create({
            data,
          });
        }

        export async function getUserById(id: string) {
          return db.user.findUnique({
            where: { id },
            include: {
              posts: true,
            },
          });
        }

        export async function updateUser(
          id: string,
          data: { email?: string; name?: string }
        ) {
          return db.user.update({
            where: { id },
            data,
          });
        }

        export async function deleteUser(id: string) {
          return db.user.delete({
            where: { id },
          });
        }
  verbosity: minimal


Check for N+1 query patterns using project tools:

get_prisma_operations:
  project_root: "."
  analyze_performance: true


This identifies:

N+1 query opportunities (missing include or select)
Missing indexes on frequently queried fields
Inefficient relationship loading

Optimize queries:

Use select to limit fields:

db.user.findMany({
  select: { id: true, email: true }, // Don't fetch unused fields
});


Eager load relationships:

db.post.findMany({
  include: { author: true }, // Prevents N+1
});


Use pagination:

db.post.findMany({
  take: 20,
  skip: (page - 1) * 20,
});


Add database-level constraints:

@@index([userId, createdAt(sort: Desc)])

8. Implement Transactions

For multi-step operations, use transactions:

Prisma:

export async function createPostWithCategories(
  postData: { title: string; content: string; authorId: string },
  categoryIds: string[]
) {
  return db.$transaction(async (tx) => {
    const post = await tx.post.create({
      data: {
        ...postData,
        categories: {
          connect: categoryIds.map((id) => ({ id })),
        },
      },
    });

    await tx.user.update({
      where: { id: postData.authorId },
      data: { updatedAt: new Date() },
    });

    return post;
  });
}


Drizzle:

export async function createPostWithCategories(
  postData: { title: string; content: string; authorId: string },
  categoryIds: string[]
) {
  return db.transaction(async (tx) => {
    const [post] = await tx.insert(posts).values(postData).returning();

    await tx.insert(postCategories).values(
      categoryIds.map((categoryId) => ({
        postId: post.id,
        categoryId,
      }))
    );

    return post;
  });
}

9. Seed Development Data

Create seed script for local development:

precision_write:
  files:
    - path: "prisma/seed.ts"
      content: |
        import { PrismaClient } from '@prisma/client';

        const prisma = new PrismaClient();

        async function main() {
          // Clear existing data
          await prisma.comment.deleteMany();
          await prisma.post.deleteMany();
          await prisma.user.deleteMany();
          await prisma.category.deleteMany();

          // Create users
          const alice = await prisma.user.create({
            data: {
              email: 'alice@example.com',
              name: 'Alice',
            },
          });

          const bob = await prisma.user.create({
            data: {
              email: 'bob@example.com',
              name: 'Bob',
            },
          });

          // Create categories
          const tech = await prisma.category.create({
            data: { name: 'Technology' },
          });

          const news = await prisma.category.create({
            data: { name: 'News' },
          });

          // Create posts
          await prisma.post.create({
            data: {
              title: 'First Post',
              content: 'This is the first post',
              published: true,
              authorId: alice.id,
              categories: {
                connect: [{ id: tech.id }],
              },
            },
          });

          console.log('Database seeded successfully');
        }

        main()
          .catch((e) => {
            console.error(e);
            process.exit(1);
          })
          .finally(async () => {
            await prisma.$disconnect();
          });
  verbosity: minimal


Update package.json:

precision_edit:
  edits:
    - path: "package.json"
      find: '"scripts": {'
      hints:
        near_line: 2
      replace: |
        "prisma": {
          "seed": "tsx prisma/seed.ts"
        },
        "scripts": {
  verbosity: minimal

10. Validate Implementation

Run the database checklist script:

./plugins/goodvibes/skills/outcome/database-layer/scripts/database-checklist.sh .


This validates:

Schema file exists and is valid
Migration directory present
Database URL documented in .env.example
Type generation configured
No SQL injection vulnerabilities (string concatenation)
Connection pooling configured
Indexes on foreign keys

Run type checking and tests:

precision_exec:
  commands:
    - cmd: "npm run typecheck"
      expect:
        exit_code: 0
    - cmd: "npm run test -- db"
      expect:
        exit_code: 0
  verbosity: minimal


Use query_database to verify data integrity:

query_database:
  project_root: "."
  query: "SELECT COUNT(*) FROM users;"

Common Patterns
Soft Deletes

Add deletedAt field and filter in queries:

model Post {
  id        String    @id
  deletedAt DateTime?
}

// Soft delete
await db.post.update({
  where: { id },
  data: { deletedAt: new Date() },
});

// Query only active records
await db.post.findMany({
  where: { deletedAt: null },
});

Optimistic Locking

Use version field to prevent concurrent updates:

model Post {
  id      String @id
  version Int    @default(0)
}

await db.post.update({
  where: {
    id: postId,
    version: currentVersion,
  },
  data: {
    title: newTitle,
    version: { increment: 1 },
  },
});

Connection Pooling

For serverless environments, use connection pooling:

# PgBouncer
DATABASE_URL="postgresql://user:password@localhost:6543/db?pgbouncer=true"
DIRECT_URL="postgresql://user:password@localhost:5432/db"

datasource db {
  provider  = "postgresql"
  url       = env("DATABASE_URL")
  directUrl = env("DIRECT_URL")
}

Full-Text Search

PostgreSQL:

@@index([content(ops: raw("gin_trgm_ops"))], type: Gin)

await db.$queryRaw`
  SELECT * FROM posts
  WHERE to_tsvector('english', content) @@ to_tsquery('search terms')
`;

Security Checklist
 Database credentials in environment variables (not committed)
 Input validation on all user-provided data
 Parameterized queries (no string concatenation)
 Row-level security for multi-tenant apps
 Rate limiting on expensive queries
 Audit logging for sensitive operations
 Least privilege database user permissions
 SSL/TLS for database connections in production
Performance Checklist
 Indexes on foreign keys
 Composite indexes for multi-column filters
 Connection pooling configured
 Query result pagination
 Eager loading to prevent N+1 queries
 Database query logging in development
 Explain/analyze for slow queries
 Caching for frequently accessed data
Troubleshooting
Migration fails with constraint violation
Check existing data conflicts with new constraints
Add data migration before schema migration
Use multi-step migrations (add column nullable, populate, make required)
N+1 query detected
Use get_prisma_operations to identify location
Add include or select with relations
Consider using dataloader for complex cases
Connection pool exhausted
Increase pool size in connection string (?pool_timeout=10)
Check for missing await (connections not released)
Use connection pooler (PgBouncer, Prisma Accelerate)
Type generation fails
Verify schema syntax with npx prisma validate
Clear generated files and regenerate
Check for circular dependencies in relations
Next Steps

After implementing the database layer:

Add caching - Use Redis for frequently accessed data
Implement search - Add full-text search or Elasticsearch
Add monitoring - Track query performance and slow queries
Write tests - Unit tests for queries, integration tests for transactions
Document schema - Add comments to schema for team reference
Plan backups - Set up automated database backups

For additional reference material and decision trees, see:

references/orm-comparison.md - ORM selection guide
scripts/database-checklist.sh - Validation script
Weekly Installs
52
Repository
mgd34msu/goodvi…s-plugin
GitHub Stars
6
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass