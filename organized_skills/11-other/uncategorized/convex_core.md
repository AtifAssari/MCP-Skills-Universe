---
rating: ⭐⭐
title: convex-core
url: https://skills.sh/igorwarzocha/opencode-workflows/convex-core
---

# convex-core

skills/igorwarzocha/opencode-workflows/convex-core
convex-core
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill convex-core
SKILL.md
Schema Rules
You MUST define all tables in convex/schema.ts with defineSchema / defineTable.
System Fields: _id (v.id(tableName)) and _creationTime (v.number()) are added automatically.
You MUST use v.* validators for every field; SHOULD avoid v.any() unless necessary.
Index naming: include all fields in the name, e.g., "by_field1_and_field2".
Index rules:
You MUST use .index(name, [fields...]).
Field order matters; range expressions MUST follow index order.
Limits: 16 fields per index, 32 indexes per table.
Function Rules
You MUST use new function syntax with args, returns, and handler.
You MUST always validate args and returns (HTTP actions excluded).
Use query for reads, mutation for writes, and action for external/long-running.
Actions MUST NOT access ctx.db; You MUST use ctx.runQuery / ctx.runMutation.
Circular Dependencies: When calling a function in the same file via ctx.run*, You MUST add explicit return type annotations to the receiver variable.
Database Operations
You MUST provide the explicit table name as the first argument to ctx.db.get, ctx.db.patch, ctx.db.replace, and ctx.db.delete.
Replacement: Use ctx.db.replace for full document replacement (throws if missing).
Patching: Use ctx.db.patch for shallow merge updates (throws if missing).
Deletion: Convex queries do NOT support .delete(). You MUST .collect() results and iterate to call ctx.db.delete(id).
Unique: Use .unique() for single document results; it MUST throw if multiple documents match.
You MUST NOT use filter in production queries; use indexes and .withIndex.
TypeScript Best Practices
You MUST use as const for string literals in discriminated unions.
You MUST define arrays as const array: Array<T> = [...] and records as const record: Record<K, V> = {...}.
You MUST prefer Id<"table"> over string for all document identifiers.
Query Performance
You SHOULD prefer .withIndex over .filter on large tables.
If using .withIndex without a range, You MUST pair it with take, first, unique, or paginate.
Search limits: collect() throws if >1024 docs; You SHOULD use take(n), paginate(), or for await iteration for large sets.
Async iteration: Use for await (const row of query) instead of .collect() for streaming large result sets.
Pagination
You MUST use paginationOptsValidator in args.
.paginate() returns { page, isDone, continueCursor }.
Pages are reactive; size MAY change.
You SHOULD avoid strict returns validators for the full .paginate() result object; validate page or use v.any().
Client Patterns
You MUST use api.* references from convex/_generated/api.
React hooks: useQuery, useMutation, useAction, usePaginatedQuery.
You MUST NOT call mutations or actions during render.
Safety
You MUST enforce auth per function; check identity via ctx.auth helpers.
You MUST NOT expose sensitive logic in public functions; MUST use internal ones.
Weekly Installs
37
Repository
igorwarzocha/op…orkflows
GitHub Stars
111
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass