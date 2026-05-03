---
title: effect-ts
url: https://skills.sh/kastalien-research/thoughtbox-dot-claude/effect-ts
---

# effect-ts

skills/kastalien-research/thoughtbox-dot-claude/effect-ts
effect-ts
Installation
$ npx skills add https://github.com/kastalien-research/thoughtbox-dot-claude --skill effect-ts
SKILL.md
Effect-TS Expert Guide

Effect-TS is a functional TypeScript library providing typed effects, structured concurrency, and a robust runtime. This skill covers correct usage patterns and addresses common misconceptions from LLM-generated content.

Quick Reference
import { Effect, Layer, Context, Fiber, Schedule, Cache, Scope } from "effect";
import { Schema, JSONSchema } from "@effect/schema";


Core Type Signature:

Effect<Success, Error, Requirements>
//      ↑        ↑       ↑
//      |        |       └── Dependencies (provided via Layers)
//      |        └── Expected errors (typed, must be handled)
//      └── Success value

Common Misconceptions

LLM outputs often contain incorrect APIs. Use this table to correct them:

Wrong (common in AI outputs)	Correct
Effect.cachedWithTTL(...)	Cache.make({ timeToLive: Duration })
Effect.cachedInvalidateWithTTL(...)	cache.invalidate(key) / cache.invalidateAll()
Effect.match(...)	Effect.either + Either.match, or Effect.catchTag
"thread-local storage"	"fiber-local storage" via FiberRef
JSON Schema Draft 2020-12	@effect/schema generates Draft-07
fibers are "cancelled"	fibers are "terminated" or "interrupted"
all queues have back-pressure	only bounded queues; sliding/dropping do not
--only=production	--omit=dev (npm 7+)
Error Handling: Two Error Types

Effect distinguishes between:

Expected Errors (Failures) - Typed in E channel, must be handled
Unexpected Errors (Defects) - Runtime bugs, captured but not typed
// Expected error - typed
const fetchUser = (id: string): Effect.Effect<User, UserNotFoundError | NetworkError> => ...

// Handle expected errors
const handled = pipe(
  fetchUser("123"),
  Effect.catchTag("UserNotFoundError", (e) => Effect.succeed(defaultUser)),
  Effect.catchTag("NetworkError", (e) => Effect.retry(schedule))
);

// Unexpected errors (defects) - captured by runtime
Effect.catchAllDefect(program, (defect) =>
  Console.error("Unexpected error", defect)
);

Fibers & Cancellation (Critical for MCP)

Fibers are lightweight virtual threads with native interruption:

// Fork a fiber
const fiber = yield* Effect.fork(longRunningTask);

// Interrupt it (e.g., when MCP client disconnects)
yield* Fiber.interrupt(fiber);

// Structured concurrency: child fibers auto-terminate with parent
const parent = Effect.gen(function* () {
  yield* Effect.fork(backgroundTask);  // Auto-interrupted when parent ends
  yield* mainTask;
});

// Daemon fibers outlive their parent
yield* Effect.forkDaemon(longLivedBackgroundTask);

Concurrency Primitives
Effect.race - First Wins, Losers Interrupted
// First to succeed wins; other is automatically interrupted
const result = yield* Effect.race(
  fetchFromCache,
  fetchFromDatabase
);

Effect.all with Concurrency Control
// Process 50 documents with max 5 concurrent
const results = yield* Effect.all(documents.map(processDoc), {
  concurrency: 5  // NOT a "worker pool" - limits concurrent tasks
});

Queue Types
// Bounded - applies back-pressure (offer suspends when full)
const bounded = yield* Queue.bounded<string>(100);

// Dropping - discards new items when full (no back-pressure)
const dropping = yield* Queue.dropping<string>(100);

// Sliding - discards oldest items when full (no back-pressure)
const sliding = yield* Queue.sliding<string>(100);

Layers for Dependency Injection

Layers construct services without leaking dependencies:

// Define a service
class Database extends Context.Tag("Database")<
  Database,
  { query: (sql: string) => Effect.Effect<Result> }
>() {}

// Create layer (dependencies handled at construction)
const DatabaseLive = Layer.effect(
  Database,
  Effect.gen(function* () {
    const config = yield* Config;  // Dependency injected here
    return {
      query: (sql) => Effect.tryPromise(() => runQuery(sql, config))
    };
  })
);

// Provide to program
const runnable = program.pipe(Effect.provide(DatabaseLive));

// For testing - swap implementation
const DatabaseTest = Layer.succeed(Database, {
  query: () => Effect.succeed(mockResult)
});

Resource Management
Effect.ensuring - Always Runs Finalizer
const program = pipe(
  Effect.tryPromise(() => openConnection()),
  Effect.ensuring(Console.log("Cleanup"))  // Runs on success, failure, OR interrupt
);

acquireUseRelease Pattern
const withConnection = Effect.acquireUseRelease(
  Effect.tryPromise(() => db.connect()),     // Acquire
  (conn) => Effect.tryPromise(() => conn.query("SELECT *")),  // Use
  (conn) => Effect.promise(() => conn.close())  // Release (always runs)
);

Scope for Resource Lifecycle
Effect.scoped(
  Effect.gen(function* () {
    const file = yield* openFile("data.txt");  // Acquired
    const data = yield* file.read();
    return data;
  })  // File automatically released when scope closes
);

Caching

There is no Effect.cachedWithTTL. Use the Cache module:

import { Cache } from "effect";

const cache = yield* Cache.make({
  capacity: 100,
  timeToLive: Duration.minutes(5),
  lookup: (key: string) => fetchExpensiveData(key)
});

// Use the cache
const value = yield* cache.get("my-key");

// Invalidate
yield* cache.invalidate("my-key");
yield* cache.invalidateAll();

Retry with Schedule
import { Schedule } from "effect";

// Retry 3 times with exponential backoff
const policy = Schedule.exponential("100 millis").pipe(
  Schedule.intersect(Schedule.recurs(3))
);

const robust = Effect.retry(unstableOperation, policy);

// Retry until condition
const untilSuccess = Effect.retry(operation, {
  until: (err) => err.code === "RATE_LIMITED"
});

Schema & JSON Schema

@effect/schema generates JSON Schema Draft-07 (not 2020-12):

import { Schema, JSONSchema } from "@effect/schema";

const User = Schema.Struct({
  id: Schema.String,
  age: Schema.Number.pipe(Schema.positive())
});

// Generate JSON Schema (Draft-07)
const jsonSchema = JSONSchema.make(User);
// { "$schema": "http://json-schema.org/draft-07/schema#", ... }

// Decode (parse)
const user = Schema.decodeUnknownSync(User)(rawData);

// Encode
const json = Schema.encodeSync(User)(user);

Observability & OpenTelemetry

Effect has native OpenTelemetry integration:

import { NodeSdk } from "@effect/opentelemetry";
import { OTLPTraceExporter } from "@opentelemetry/exporter-trace-otlp-http";

// Add tracing to any effect
const traced = Effect.withSpan("processRequest")(myEffect);

// Logging with context
yield* Effect.log("Processing request");
yield* Effect.annotateLogs("requestId", "abc-123");

// FiberRef for fiber-local context propagation
const RequestId = FiberRef.unsafeMake<string>("");
yield* FiberRef.set(RequestId, "req-456");

When NOT to Use Effect
Scenario	Recommendation
Simple MCP tool (< 100 LOC)	Use FastMCP or vanilla SDK
Team unfamiliar with FP	Steep learning curve; consider NestJS
Bundle size critical	Effect adds 15-25kb gzipped minimum
Existing NestJS/TypeORM codebase	Impedance mismatch with class-based DI
MCP Server Patterns
Tool Handler with Typed Errors
const searchTool = Effect.gen(function* () {
  const args = yield* parseArgs(input);
  const db = yield* Database;
  const results = yield* db.query(args.query);
  return formatResults(results);
}).pipe(
  Effect.catchTag("ParseError", () =>
    Effect.fail({ code: -32602, message: "Invalid params" })
  ),
  Effect.catchTag("DatabaseError", () =>
    Effect.fail({ code: -32603, message: "Internal error" })
  )
);

Request Scoping
// Each MCP request gets its own scope
const handleRequest = (request: MCPRequest) =>
  Effect.scoped(
    Effect.gen(function* () {
      // Resources acquired here auto-release when request completes
      const tempFile = yield* createTempFile();
      const result = yield* processRequest(request, tempFile);
      return result;
    })
  );

Resources
Effect Documentation
Effect GitHub
@effect/schema JSON Schema
@effect/opentelemetry
Weekly Installs
285
Repository
kastalien-resea…t-claude
GitHub Stars
6
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass