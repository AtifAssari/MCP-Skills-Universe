---
rating: ⭐⭐
title: drizzle
url: https://skills.sh/lobehub/lobehub/drizzle
---

# drizzle

skills/lobehub/lobehub/drizzle
drizzle
Installation
$ npx skills add https://github.com/lobehub/lobehub --skill drizzle
Summary

Drizzle ORM schema definitions, type inference, and query patterns for PostgreSQL databases.

Enforces snake_case naming (tables plural, columns lowercase), helper functions for timestamps, and ID prefixes for entity type distinction
Provides type inference patterns ($inferInsert, $inferSelect) and schema validation via createInsertSchema
Requires db.select() builder API for all queries; explicitly forbids the relational API (findMany, with:) due to fragile lateral join generation
Covers common patterns: junction tables with composite keys, explicit JOINs with object selection, aggregations via groupBy, and one-to-many relationships via separate queries
SKILL.md
Drizzle ORM Schema Style Guide
Configuration
Config: drizzle.config.ts
Schemas: src/database/schemas/
Migrations: src/database/migrations/
Dialect: postgresql with strict: true
Helper Functions

Location: src/database/schemas/_helpers.ts

timestamptz(name): Timestamp with timezone
createdAt(), updatedAt(), accessedAt(): Standard timestamp columns
timestamps: Object with all three for easy spread
Naming Conventions
Tables: Plural snake_case (users, session_groups)
Columns: snake_case (user_id, created_at)
Column Definitions
Primary Keys
id: text('id')
  .primaryKey()
  .$defaultFn(() => idGenerator('agents'))
  .notNull(),


ID prefixes make entity types distinguishable. For internal tables, use uuid.

Foreign Keys
userId: text('user_id')
  .references(() => users.id, { onDelete: 'cascade' })
  .notNull(),

Timestamps
...timestamps,  // Spread from _helpers.ts

Indexes
// Return array (object style deprecated)
(t) => [uniqueIndex('client_id_user_id_unique').on(t.clientId, t.userId)],

Type Inference
export const insertAgentSchema = createInsertSchema(agents);
export type NewAgent = typeof agents.$inferInsert;
export type AgentItem = typeof agents.$inferSelect;

Example Pattern
export const agents = pgTable(
  'agents',
  {
    id: text('id')
      .primaryKey()
      .$defaultFn(() => idGenerator('agents'))
      .notNull(),
    slug: varchar('slug', { length: 100 })
      .$defaultFn(() => randomSlug(4))
      .unique(),
    userId: text('user_id')
      .references(() => users.id, { onDelete: 'cascade' })
      .notNull(),
    clientId: text('client_id'),
    chatConfig: jsonb('chat_config').$type<LobeAgentChatConfig>(),
    ...timestamps,
  },
  (t) => [uniqueIndex('client_id_user_id_unique').on(t.clientId, t.userId)],
);

Common Patterns
Junction Tables (Many-to-Many)
export const agentsKnowledgeBases = pgTable(
  'agents_knowledge_bases',
  {
    agentId: text('agent_id')
      .references(() => agents.id, { onDelete: 'cascade' })
      .notNull(),
    knowledgeBaseId: text('knowledge_base_id')
      .references(() => knowledgeBases.id, { onDelete: 'cascade' })
      .notNull(),
    userId: text('user_id')
      .references(() => users.id, { onDelete: 'cascade' })
      .notNull(),
    enabled: boolean('enabled').default(true),
    ...timestamps,
  },
  (t) => [primaryKey({ columns: [t.agentId, t.knowledgeBaseId] })],
);

Query Style

Always use db.select() builder API. Never use db.query.* relational API (findMany, findFirst, with:).

The relational API generates complex lateral joins with json_build_array that are fragile and hard to debug.

Select Single Row
// ✅ Good
const [result] = await this.db
  .select()
  .from(agents)
  .where(eq(agents.id, id))
  .limit(1);
return result;

// ❌ Bad: relational API
return this.db.query.agents.findFirst({
  where: eq(agents.id, id),
});

Select with JOIN
// ✅ Good: explicit select + leftJoin
const rows = await this.db
  .select({
    runId: agentEvalRunTopics.runId,
    score: agentEvalRunTopics.score,
    testCase: agentEvalTestCases,
    topic: topics,
  })
  .from(agentEvalRunTopics)
  .leftJoin(agentEvalTestCases, eq(agentEvalRunTopics.testCaseId, agentEvalTestCases.id))
  .leftJoin(topics, eq(agentEvalRunTopics.topicId, topics.id))
  .where(eq(agentEvalRunTopics.runId, runId))
  .orderBy(asc(agentEvalRunTopics.createdAt));

// ❌ Bad: relational API with `with:`
return this.db.query.agentEvalRunTopics.findMany({
  where: eq(agentEvalRunTopics.runId, runId),
  with: { testCase: true, topic: true },
});

Select with Aggregation
// ✅ Good: select + leftJoin + groupBy
const rows = await this.db
  .select({
    id: agentEvalDatasets.id,
    name: agentEvalDatasets.name,
    testCaseCount: count(agentEvalTestCases.id).as('testCaseCount'),
  })
  .from(agentEvalDatasets)
  .leftJoin(agentEvalTestCases, eq(agentEvalDatasets.id, agentEvalTestCases.datasetId))
  .groupBy(agentEvalDatasets.id);

One-to-Many (Separate Queries)

When you need a parent record with its children, use two queries instead of relational with::

// ✅ Good: two simple queries
const [dataset] = await this.db
  .select()
  .from(agentEvalDatasets)
  .where(eq(agentEvalDatasets.id, id))
  .limit(1);

if (!dataset) return undefined;

const testCases = await this.db
  .select()
  .from(agentEvalTestCases)
  .where(eq(agentEvalTestCases.datasetId, id))
  .orderBy(asc(agentEvalTestCases.sortOrder));

return { ...dataset, testCases };

Database Migrations

See the db-migrations skill for the detailed migration guide.

Weekly Installs
954
Repository
lobehub/lobehub
GitHub Stars
75.9K
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass