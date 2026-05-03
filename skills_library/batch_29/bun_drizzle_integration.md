---
title: bun-drizzle-integration
url: https://skills.sh/secondsky/claude-skills/bun-drizzle-integration
---

# bun-drizzle-integration

skills/secondsky/claude-skills/bun-drizzle-integration
bun-drizzle-integration
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill bun-drizzle-integration
SKILL.md
Bun Drizzle Integration

Drizzle ORM provides type-safe database access with Bun's SQLite driver.

Quick Start
bun add drizzle-orm
bun add -D drizzle-kit

Schema Definition
// src/db/schema.ts
import { sqliteTable, text, integer } from "drizzle-orm/sqlite-core";

export const users = sqliteTable("users", {
  id: integer("id").primaryKey({ autoIncrement: true }),
  name: text("name").notNull(),
  email: text("email").notNull().unique(),
  createdAt: integer("created_at", { mode: "timestamp" })
    .notNull()
    .default(sql`(unixepoch())`),
});

export const posts = sqliteTable("posts", {
  id: integer("id").primaryKey({ autoIncrement: true }),
  title: text("title").notNull(),
  content: text("content"),
  authorId: integer("author_id")
    .notNull()
    .references(() => users.id),
});

Database Setup
// src/db/index.ts
import { drizzle } from "drizzle-orm/bun-sqlite";
import { Database } from "bun:sqlite";
import * as schema from "./schema";

const sqlite = new Database("app.db");
export const db = drizzle(sqlite, { schema });

Configuration
// drizzle.config.ts
import type { Config } from "drizzle-kit";

export default {
  schema: "./src/db/schema.ts",
  out: "./drizzle",
  dialect: "sqlite",
  dbCredentials: {
    url: "./app.db",
  },
} satisfies Config;

Migrations
# Generate migration
bun drizzle-kit generate

# Apply migrations
bun drizzle-kit migrate

# Push schema directly (dev only)
bun drizzle-kit push

# Open Drizzle Studio
bun drizzle-kit studio

CRUD Operations
Insert
import { db } from "./db";
import { users, posts } from "./db/schema";

// Single insert
const user = await db.insert(users).values({
  name: "Alice",
  email: "alice@example.com",
}).returning();

// Multiple insert
await db.insert(users).values([
  { name: "Bob", email: "bob@example.com" },
  { name: "Charlie", email: "charlie@example.com" },
]);

// Insert or ignore
await db.insert(users)
  .values({ name: "Alice", email: "alice@example.com" })
  .onConflictDoNothing();

// Upsert
await db.insert(users)
  .values({ name: "Alice", email: "alice@example.com" })
  .onConflictDoUpdate({
    target: users.email,
    set: { name: "Alice Updated" },
  });

Select
import { eq, gt, like, and, or, desc, asc } from "drizzle-orm";

// All rows
const allUsers = await db.select().from(users);

// With conditions
const activeUsers = await db
  .select()
  .from(users)
  .where(eq(users.status, "active"));

// Multiple conditions
const filtered = await db
  .select()
  .from(users)
  .where(and(
    gt(users.age, 18),
    like(users.name, "%Alice%")
  ));

// Specific columns
const names = await db
  .select({ name: users.name, email: users.email })
  .from(users);

// Order and limit
const topUsers = await db
  .select()
  .from(users)
  .orderBy(desc(users.createdAt))
  .limit(10);

// First result
const first = await db.query.users.findFirst({
  where: eq(users.id, 1),
});

Update
// Update with condition
await db
  .update(users)
  .set({ name: "Alice Updated" })
  .where(eq(users.id, 1));

// Update multiple fields
await db
  .update(users)
  .set({
    name: "New Name",
    updatedAt: new Date(),
  })
  .where(eq(users.email, "alice@example.com"));

Delete
// Delete with condition
await db.delete(users).where(eq(users.id, 1));

// Delete multiple
await db.delete(users).where(gt(users.createdAt, cutoffDate));

Relations
// schema.ts
import { relations } from "drizzle-orm";

export const usersRelations = relations(users, ({ many }) => ({
  posts: many(posts),
}));

export const postsRelations = relations(posts, ({ one }) => ({
  author: one(users, {
    fields: [posts.authorId],
    references: [users.id],
  }),
}));

// Query with relations
const usersWithPosts = await db.query.users.findMany({
  with: {
    posts: true,
  },
});

// Nested relations
const detailed = await db.query.users.findFirst({
  where: eq(users.id, 1),
  with: {
    posts: {
      with: {
        comments: true,
      },
    },
  },
});

Transactions
// Transaction
await db.transaction(async (tx) => {
  const [user] = await tx.insert(users)
    .values({ name: "Alice", email: "alice@example.com" })
    .returning();

  await tx.insert(posts).values({
    title: "First Post",
    authorId: user.id,
  });
});

// Rollback on error
await db.transaction(async (tx) => {
  await tx.insert(users).values({ name: "Bob" });

  if (someCondition) {
    tx.rollback(); // Throws to rollback
  }

  await tx.insert(posts).values({ ... });
});

Prepared Statements
// Create prepared statement
const getUserById = db
  .select()
  .from(users)
  .where(eq(users.id, sql.placeholder("id")))
  .prepare();

// Execute with parameter
const user = await getUserById.execute({ id: 1 });

// Reuse for performance
for (const id of userIds) {
  const user = await getUserById.execute({ id });
  processUser(user);
}

Raw SQL
import { sql } from "drizzle-orm";

// Raw query
const result = await db.run(sql`
  UPDATE users SET last_login = ${new Date()} WHERE id = ${userId}
`);

// In select
const users = await db.select({
  name: users.name,
  upperName: sql<string>`UPPER(${users.name})`,
}).from(users);

// Raw expressions in where
await db.select().from(users).where(
  sql`${users.age} > 18 AND ${users.status} = 'active'`
);

Column Types Reference
import {
  sqliteTable,
  text,
  integer,
  real,
  blob,
  numeric,
} from "drizzle-orm/sqlite-core";

const example = sqliteTable("example", {
  // Integer
  id: integer("id").primaryKey(),
  age: integer("age"),

  // Text
  name: text("name"),
  status: text("status", { enum: ["active", "inactive"] }),

  // Real (float)
  price: real("price"),

  // Blob
  data: blob("data", { mode: "buffer" }),

  // Boolean (stored as integer)
  active: integer("active", { mode: "boolean" }),

  // Timestamp (stored as integer)
  createdAt: integer("created_at", { mode: "timestamp" }),
  updatedMs: integer("updated_ms", { mode: "timestamp_ms" }),

  // JSON (stored as text)
  metadata: text("metadata", { mode: "json" }),
});

Common Errors
Error	Cause	Fix
SQLITE_CONSTRAINT	FK/unique violation	Check constraints
no such column	Schema mismatch	Run migrations
Cannot find module	Missing driver	Use drizzle-orm/bun-sqlite
Type mismatch	Wrong column type	Check schema definition
When to Load References

Load references/migrations.md when:

Complex migration scenarios
Migration squashing
Database seeding

Load references/performance.md when:

Query optimization
Indexing strategies
Connection pooling
Weekly Installs
92
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass