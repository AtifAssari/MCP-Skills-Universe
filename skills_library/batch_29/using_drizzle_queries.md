---
title: using-drizzle-queries
url: https://skills.sh/andrelandgraf/fullstackrecipes/using-drizzle-queries
---

# using-drizzle-queries

skills/andrelandgraf/fullstackrecipes/using-drizzle-queries
using-drizzle-queries
Installation
$ npx skills add https://github.com/andrelandgraf/fullstackrecipes --skill using-drizzle-queries
SKILL.md
Working with Drizzle

Write type-safe database queries with Drizzle ORM. Covers select, insert, update, delete, relational queries, and adding new tables.

Implement Working with Drizzle

Write type-safe database queries with Drizzle ORM. Covers select, insert, update, delete, relational queries, and adding new tables.

See:

Resource: using-drizzle-queries in Fullstack Recipes
URL: https://fullstackrecipes.com/recipes/using-drizzle-queries
Writing Queries

Use Drizzle's query API for type-safe database operations:

import { db } from "@/lib/db/client";
import { chats } from "@/lib/chat/schema";
import { eq, desc } from "drizzle-orm";

// Select all
const allChats = await db.select().from(chats);

// Select with filter
const userChats = await db
  .select()
  .from(chats)
  .where(eq(chats.userId, userId))
  .orderBy(desc(chats.createdAt));

// Select single record
const chat = await db
  .select()
  .from(chats)
  .where(eq(chats.id, chatId))
  .limit(1)
  .then((rows) => rows[0]);

Inserting Data
import { db } from "@/lib/db/client";
import { chats } from "@/lib/chat/schema";

// Insert single record
const [newChat] = await db
  .insert(chats)
  .values({
    userId,
    title: "New Chat",
  })
  .returning();

// Insert multiple records
await db.insert(messages).values([
  { chatId, role: "user", content: "Hello" },
  { chatId, role: "assistant", content: "Hi there!" },
]);

Updating Data
import { db } from "@/lib/db/client";
import { chats } from "@/lib/chat/schema";
import { eq } from "drizzle-orm";

await db
  .update(chats)
  .set({ title: "Updated Title" })
  .where(eq(chats.id, chatId));

Deleting Data
import { db } from "@/lib/db/client";
import { chats } from "@/lib/chat/schema";
import { eq } from "drizzle-orm";

await db.delete(chats).where(eq(chats.id, chatId));

Using Relational Queries

For queries with relations, use the query API:

import { db } from "@/lib/db/client";

const chatWithMessages = await db.query.chats.findFirst({
  where: eq(chats.id, chatId),
  with: {
    messages: {
      orderBy: (messages, { asc }) => [asc(messages.createdAt)],
    },
  },
});

Adding New Tables
Create the schema in the feature's library folder:
// src/lib/feature/schema.ts
import { pgTable, text, uuid, timestamp } from "drizzle-orm/pg-core";

export const items = pgTable("items", {
  id: uuid("id").primaryKey().defaultRandom(),
  name: text("name").notNull(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

Import the schema in src/lib/db/client.ts:
import * as itemSchema from "@/lib/feature/schema";

const schema = {
  ...authSchema,
  ...chatSchema,
  ...itemSchema,
};

Generate and run migrations:
bun run db:generate
bun run db:migrate

References
Drizzle ORM Select
Drizzle ORM Insert
Drizzle ORM Relational Queries
Weekly Installs
101
Repository
andrelandgraf/f…krecipes
GitHub Stars
14
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass