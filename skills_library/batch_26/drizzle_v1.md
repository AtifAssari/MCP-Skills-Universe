---
title: drizzle-v1
url: https://skills.sh/habibium/agent-skills/drizzle-v1
---

# drizzle-v1

skills/habibium/agent-skills/drizzle-v1
drizzle-v1
Installation
$ npx skills add https://github.com/habibium/agent-skills --skill drizzle-v1
SKILL.md
Drizzle ORM v1 RC Upgrade Guide
Installation
npm i drizzle-orm@beta drizzle-kit@beta -D

Upgrade Steps
Step 1: Run drizzle-kit up

Migrate previous migrations folder to new format (removes journal.json, groups SQL files and snapshots):

npx drizzle-kit up

Step 2: Update Relational Queries to v2

See references/relational-queries-v2.md for complete migration patterns.

Quick Reference: Key Changes
Relations Definition

v1 - Separate relations() calls for each table:

import { relations } from "drizzle-orm/_relations"; // Note: moved import
export const usersRelation = relations(users, ({ one, many }) => ({
  posts: many(posts),
}));


v2 - Single defineRelations() for all tables:

import { defineRelations } from "drizzle-orm";
import * as schema from "./schema";

export const relations = defineRelations(schema, (r) => ({
  users: {
    posts: r.many.posts({
      from: r.users.id,
      to: r.posts.authorId,
    }),
  },
}));

Database Instance

v1:

const db = drizzle(url, { schema, mode: "planetscale" });


v2 - No mode needed, use relations:

import { relations } from './relations';
const db = drizzle(url, { relations });

Queries

v1 - Function-based where/orderBy:

await db.query.users.findMany({
  where: (users, { eq }) => eq(users.id, 1),
  orderBy: (users, { asc }) => [asc(users.id)],
});


v2 - Object-based syntax:

await db.query.users.findMany({
  where: { id: 1 },
  orderBy: { id: "asc" },
});

Many-to-Many with through

v2 (new feature):

export const relations = defineRelations(schema, (r) => ({
  users: {
    groups: r.many.groups({
      from: r.users.id.through(r.usersToGroups.userId),
      to: r.groups.id.through(r.usersToGroups.groupId),
    }),
  },
}));

Partial Upgrade (Keep RQB v1)

Use old syntax while migrating gradually:

Import from drizzle-orm/_relations
Use db._query instead of db.query
v2 Filter Operators

Object-based filters with AND, OR, NOT, RAW:

await db.query.users.findMany({
  where: {
    AND: [
      { OR: [{ name: { like: "John%" } }, { name: { ilike: "jane%" } }] },
      { age: { gt: 18 } },
      { NOT: { status: "banned" } },
      { RAW: (t) => sql`${t.createdAt} > NOW() - INTERVAL '30 days'` },
    ],
  },
});

New Features in v2
optional: false - Make relation required at type level
through - Direct many-to-many without manual junction table queries
Predefined filters - where in relation definition
Relation filtering - Filter parent by child properties
Offset on related objects - Pagination in nested relations
Weekly Installs
24
Repository
habibium/agent-skills
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass