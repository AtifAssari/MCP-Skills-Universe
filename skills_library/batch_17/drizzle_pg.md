---
title: drizzle-pg
url: https://skills.sh/jgamaraalv/ts-dev-kit/drizzle-pg
---

# drizzle-pg

skills/jgamaraalv/ts-dev-kit/drizzle-pg
drizzle-pg
Installation
$ npx skills add https://github.com/jgamaraalv/ts-dev-kit --skill drizzle-pg
SKILL.md
Drizzle ORM — PostgreSQL

Drizzle is a headless TypeScript ORM. Zero dependencies, SQL-like API, single-query output. Packages: drizzle-orm (runtime), drizzle-kit (CLI/migrations).

Table of Contents
Quick Start
Import Cheat Sheet
Common Patterns
Reference Files
Quick Start
Connect
import { drizzle } from "drizzle-orm/node-postgres";
import * as schema from "./schema";
import { relations } from "./relations";

const db = drizzle(process.env.DATABASE_URL, { schema, relations });


Or with existing Pool:

import { Pool } from "pg";
const pool = new Pool({ connectionString: process.env.DATABASE_URL });
const db = drizzle({ client: pool, schema, relations });

Define Schema
import {
  pgTable,
  pgEnum,
  serial,
  text,
  integer,
  timestamp,
  uuid,
  jsonb,
  index,
  uniqueIndex,
} from "drizzle-orm/pg-core";
import { sql } from "drizzle-orm";

export const statusEnum = pgEnum("status", ["active", "inactive", "banned"]);

export const users = pgTable(
  "users",
  {
    id: uuid("id")
      .default(sql`gen_random_uuid()`)
      .primaryKey(),
    name: text("name").notNull(),
    email: text("email").notNull().unique(),
    status: statusEnum().default("active").notNull(),
    metadata: jsonb("metadata").$type<{ roles: string[] }>(),
    createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
  },
  (t) => [index("users_email_idx").on(t.email)],
);

export const posts = pgTable("posts", {
  id: serial("id").primaryKey(),
  title: text("title").notNull(),
  authorId: uuid("author_id")
    .notNull()
    .references(() => users.id, { onDelete: "cascade" }),
  createdAt: timestamp("created_at", { withTimezone: true }).defaultNow().notNull(),
});

Define Relations
import { defineRelations } from "drizzle-orm";
import * as schema from "./schema";

export const relations = defineRelations(schema, (r) => ({
  users: {
    posts: r.many.posts({ from: r.users.id, to: r.posts.authorId }),
  },
  posts: {
    author: r.one.users({ from: r.posts.authorId, to: r.users.id }),
  },
}));

CRUD
import { eq, and, ilike, sql } from "drizzle-orm";

// SELECT
const allUsers = await db.select().from(users);
const user = await db.select().from(users).where(eq(users.id, id));

// INSERT
const [created] = await db
  .insert(users)
  .values({ name: "Dan", email: "dan@example.com" })
  .returning();

// UPDATE
await db.update(users).set({ name: "Updated" }).where(eq(users.id, id));

// DELETE
await db.delete(users).where(eq(users.id, id));

// UPSERT
await db
  .insert(users)
  .values({ id, name: "Dan", email: "dan@ex.com" })
  .onConflictDoUpdate({ target: users.id, set: { name: "Dan" } });

Relational Queries
// Nested eager loading (single SQL query)
const usersWithPosts = await db.query.users.findMany({
  with: { posts: true },
  where: { status: "active" },
  orderBy: { createdAt: "desc" },
  limit: 10,
});

const user = await db.query.users.findFirst({
  where: { id: userId },
  with: { posts: { columns: { id: true, title: true } } },
});

Migrations
# drizzle.config.ts -> see references/migrations.md
npx drizzle-kit generate     # schema diff -> SQL files
npx drizzle-kit migrate      # apply SQL to database
npx drizzle-kit push         # direct push (no SQL files)
npx drizzle-kit pull         # introspect DB -> Drizzle schema
npx drizzle-kit studio       # visual browser UI

Common Patterns
Conditional filters
const filters: SQL[] = [];
if (name) filters.push(ilike(users.name, `%${name}%`));
if (status) filters.push(eq(users.status, status));
await db
  .select()
  .from(users)
  .where(and(...filters));

Transactions
await db.transaction(async (tx) => {
  const [user] = await tx.insert(users).values({ name: "Dan" }).returning();
  await tx.insert(posts).values({ title: "Hello", authorId: user.id });
});

Type inference
type User = typeof users.$inferSelect;
type NewUser = typeof users.$inferInsert;


<quick_reference>

Import Cheat Sheet
Import path	Key exports
drizzle-orm/pg-core	pgTable, pgEnum, column types (serial, text, integer, uuid, timestamp, jsonb, varchar, boolean, numeric, bigint, geometry, vector, ...), index, uniqueIndex, unique, check, primaryKey, foreignKey
drizzle-orm	Operators: eq, ne, gt, gte, lt, lte, and, or, not, isNull, isNotNull, inArray, between, like, ilike, exists, sql, asc, desc. Utilities: getColumns, defineRelations, cosineDistance, l2Distance
drizzle-orm (types)	InferSelectModel, InferInsertModel
drizzle-zod	createInsertSchema, createSelectSchema

</quick_reference>

Reference Files

For detailed API coverage, see:

Column types, indexes, constraints, enums, PostGIS, pg_vector: references/schema-pg.md
Select, insert, update, delete, joins, filters: references/queries.md
Relations definition, relational query API (findMany/findFirst): references/relations.md
sql`` template: raw, empty, join, identifier, placeholders: references/sql-operator.md
drizzle-kit commands, drizzle.config.ts, migration workflows: references/migrations.md
Dynamic queries, transactions, custom types, Zod, utilities: references/advanced.md
Weekly Installs
17
Repository
jgamaraalv/ts-dev-kit
GitHub Stars
14
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass