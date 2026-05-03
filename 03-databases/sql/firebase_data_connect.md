---
rating: ⭐⭐⭐
title: firebase-data-connect
url: https://skills.sh/firebase/agent-skills/firebase-data-connect
---

# firebase-data-connect

skills/firebase/agent-skills/firebase-data-connect
firebase-data-connect
Installation
$ npx skills add https://github.com/firebase/agent-skills --skill firebase-data-connect
Summary

PostgreSQL-backed GraphQL backend with auto-generated type-safe SDKs for web, mobile, and Flutter.

Define GraphQL schema with @table decorators and relationships; Data Connect generates SQL and GraphQL operations automatically
Write queries and mutations in GraphQL with filtering, ordering, pagination, and upsert support; transactions available via @transaction
Secure operations with @auth levels (PUBLIC, USER, NO_ACCESS) and row-level controls using @check and @redact
Generate type-safe SDKs for TypeScript, Kotlin, Swift, and Dart with nested data access and local emulator support for development
SKILL.md
Firebase SQL Connect

Firebase SQL Connect is a relational database service using Cloud SQL for PostgreSQL with GraphQL schema, auto-generated queries/mutations, and type-safe SDKs.

[!NOTE] Product Rename: Firebase Data Connect was renamed to Firebase SQL Connect. All instructions, references, and examples in this skill repository referring to "Data Connect" or "Firebase Data Connect" apply to "SQL Connect" and "Firebase SQL Connect" as well.

Project Structure
dataconnect/
├── dataconnect.yaml      # Service configuration
├── schema/
│   └── schema.gql        # Data model (types with @table)
└── connector/
    ├── connector.yaml    # Connector config + SDK generation
    ├── queries.gql       # Queries
    └── mutations.gql     # Mutations

Key Tools for Validation

Rely on these two mechanisms to ensure project correctness:

Review GraphQL Schema: Both user-defined and generated extensions (in .dataconnect/schema/main/).
Validate Operations: Run npx -y firebase-tools@latest dataconnect:compile against the schema.
Operation Strategies: GraphQL vs. Native SQL

Always default to Native GraphQL. Native SQL lacks type safety and bypasses schema-enforced structures. Only use Native SQL when the user explicitly requests it or when the task requires advanced database features.

Strategy	When to use	Implementation
Native GraphQL (Default)	Almost all use cases. Standard CRUD, basic filtering/sorting, simple relational joins. Requires full type safety.	Auto-generated fields (movie_insert, movies). Strong typing and schema enforcement.
Native SQL (Advanced)	PostgreSQL extensions (e.g., PostGIS), window functions (RANK()), complex aggregations, or highly tuned sub-queries.	Raw SQL string literals via _select, _execute, etc. Requires strict positional parameters ($1). No type safety.
Development Workflow

Follow this strict workflow to build your application. You must read the linked reference files for each step to understand the syntax and available features.

1. Define Data Model (schema/schema.gql)

Define your GraphQL types, tables, and relationships (which map to a Postgres schema).

Read reference/schema.md for:

@table, @col, @default
Relationships (@ref, one-to-many, many-to-many)
Data types (UUID, Vector, JSON, etc.)
2. Define Authorized Operations (connector/queries.gql, connector/mutations.gql)

Write the queries and mutations your client will use, including authorization logic. SQL Connect is secure by default.

Read reference/operations.md for:

Queries: Filtering (where), Ordering (orderBy), Pagination (limit/offset).
Mutations: Create (_insert), Update (_update), Delete (_delete).
Upserts: Use _upsert to "insert or update" records (CRITICAL for user profiles).
Transactions: Use @transaction for multi-step atomic operations. Use _expr: "response.<prevStep>" to pass data between steps.

Read reference/security.md for authorization:

@auth(level: ...) for PUBLIC, USER, or NO_ACCESS.
@check and @redact for row-level security and validation.

Read reference/native_sql.md for Native SQL operations:

Embedding raw SQL with _select, _selectFirst, _execute
Strict rules for positional parameters ($1, $2), quoting, and CTEs
Advanced PostgreSQL features (PostGIS, Window Functions)
3. Use type-safe SDK in your apps

Generate type-safe code for your client platform.

Read reference/sdks.md for:

Android (Kotlin), iOS (Swift), Web (TypeScript), Flutter (Dart).
How to initialize and call your queries/mutations.
Nested Data: See how to access related fields (e.g., movie.reviews).
4. Add Real-time Subscriptions (Optional)

Enable live data updates to push changes to connected clients.

Read reference/realtime.md for:

@refresh directive for time-based polling and event-driven updates.
CEL conditions to scope refresh triggers precisely.
Feature Capability Map

If you need to implement a specific feature, consult the mapped reference file:

Feature	Reference File	Key Concepts
Data Modeling	reference/schema.md	@table, @unique, @index, Relations
Vector Search	reference/advanced.md	Vector, @col(dataType: "vector")
Full-Text Search	reference/advanced.md	@searchable
Upserting Data	reference/operations.md	_upsert mutations
Complex Filters	reference/operations.md	_or, _and, _not, eq, contains
Transactions	reference/operations.md	@transaction, response binding
Environment Config	reference/config.md	dataconnect.yaml, connector.yaml
Realtime Subscriptions	reference/realtime.md	@refresh, subscribe(), auto-refresh
Starter Templates	templates.md	CRUD, user-owned resources, many-to-many, SDK init
Deployment & CLI

Read reference/config.md for deep dive on configuration.

Follow these patterns based on your current task:

How to initialize SQL Connect in a Firebase project
Understand the app idea. Ask clarification questions if unclear.
Run npx -y firebase-tools@latest init dataconnect.
Validate that the app template and generated SDK are setup.
How to build apps using SQL Connect locally
Start the emulator: npx -y firebase-tools@latest emulators:start --only dataconnect.
Write schema and operations.
Run npx -y firebase-tools@latest dataconnect:compile or npx -y firebase-tools@latest dataconnect:sdk:generate to validate them.
Use the operations in your app and build it.
How to deploy SQL Connect to Cloud SQL
Run npx -y firebase-tools@latest deploy --only dataconnect.
Examples

For complete, working code examples of schemas and operations, see examples.md.

For ready-to-use starter templates (CRUD, user-owned resources, many-to-many, YAML configs, SDK init), see templates.md.

Weekly Installs
38.9K
Repository
firebase/agent-skills
GitHub Stars
264
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn