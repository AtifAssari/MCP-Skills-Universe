---
rating: ⭐⭐⭐
title: schema0-db-schema
url: https://skills.sh/schema0/skills/schema0-db-schema
---

# schema0-db-schema

skills/schema0/skills/schema0-db-schema
schema0-db-schema
Installation
$ npx skills add https://github.com/schema0/skills --skill schema0-db-schema
SKILL.md
Database Schema
File Location
packages/db/src/
├── index.ts          # Database client (createDb) and exports
├── schema/
│   ├── index.ts      # Barrel re-exports (export * from "./{entity}")
│   └── [entity].ts   # Table + all derived schemas (insert, select, update, form)
└── migrations/       # Auto-generated — never hand-write

7 Schemas Per Entity

Every entity file defines exactly 7 schemas:

Table definition -- pgTable(...) with text("id").primaryKey()
Insert schema -- createInsertSchema(table, overrides) with callback overrides for nullable columns
Select schema -- createSelectSchema(table, overrides) with callback overrides for nullable columns
Update schema -- selectSchema.partial().required({ id: true })
Form schema -- insertSchema.omit({ id, createdAt, updatedAt })
Edit form schema -- formSchema.partial() (NO id)
Router output schema -- z.object({...}) matching DB return types
Key Rules
Callback overrides for nullable columns: colName: (schema) => schema.optional() in both insert and select schemas
Server-stamped fields (e.g., userId, organizationId, createdBy): keep .notNull() on the table but mark .optional() in the insert schema. The server fills them in from session context. See references/schema-template.md > "Server-Stamped Fields".
NEVER use .transform() -- breaks .omit() and .partial() chaining
NEVER use serial() or bigint for primary keys -- only text("id").primaryKey()
Router output: every column WITHOUT .notNull() needs .nullable().optional()
timestamp() returns Date objects -- use z.date() in router output, NOT z.string()
Form schemas belong in the entity file, not in index.ts
Always use createDb() per request -- never singleton
Column Types Quick Reference
id: text("id").primaryKey(),
name: text("name").notNull(),
email: varchar("email", { length: 255 }).unique(),
age: integer("age"),
price: decimal("price", { precision: 10, scale: 2 }),
active: boolean("active").default(true),
metadata: jsonb("metadata").$type<{ key: string }>(),
createdAt: timestamp("created_at").defaultNow().notNull(),

References
references/schema-template.md -- Full 7-schema code template with naming conventions, export, migration workflow, transform utilities
references/column-types.md -- Column types reference, schema key rules, database client usage
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