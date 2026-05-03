---
rating: ⭐⭐
title: building-with-effect
url: https://skills.sh/felixnorden/skills/building-with-effect
---

# building-with-effect

skills/felixnorden/skills/building-with-effect
building-with-effect
Installation
$ npx skills add https://github.com/felixnorden/skills --skill building-with-effect
SKILL.md
Building with Effect

Effect is a powerful TypeScript library for building complex, type-safe programs with composable abstractions for error handling, dependency injection, concurrency, and resource management.

Quick Start

Using Effect.fn (Recommended)

import { Effect, Schema } from "effect";

// Define errors with Schema.TaggedErrorClass
class FetchError extends Schema.TaggedErrorClass<FetchError>()("FetchError", {
  message: Schema.String,
}) {}

// Create functions with Effect.fn
export const fetchUser = Effect.fn("fetchUser")(
  function* (id: number) {
    yield* Effect.logInfo("Fetching user:", id);

    // Always return when raising an error
    return yield* new FetchError({ message: "Failed to fetch" });
  },
  // Add combinators as additional arguments (no .pipe needed)
  Effect.catch((error) => Effect.logError(`Error: ${error}`)),
  Effect.withSpan("fetchUser", { attributes: { method: "Effect.fn" } }),
);


Generator Style

const program = Effect.gen(function* () {
  const a = yield* Effect.succeed(10);
  const b = yield* Effect.succeed(20);
  return a + b;
});


Running Effects

// As Promise
Effect.runPromise(program).then(console.log);

// With NodeRuntime (recommended for apps)
import { NodeRuntime } from "@effect/platform-node";
NodeRuntime.runMain(program);

// Using Layer.launch as entry point
Layer.launch(WorkerLayer).pipe(NodeRuntime.runMain);

Degrees of Freedom

Match the level of specificity to the task's fragility:

Low Freedom (specific patterns, consistency critical)

These operations have a narrow safe path - follow exactly:

Error definition: Always use Schema.TaggedErrorClass with descriptive _tag
Service structure: Extend Context.Service with static layer property
Effect.fn usage: Always use Effect.fn("name") for functions returning Effects
Resource cleanup: Always use acquireUseRelease or Effect.addFinalizer
Resource pattern selection: Use acquireUseRelease for external resources, Ref for shared mutable state, addFinalizer for cleanup within existing scope
Error recovery vs propagation: Use catchTags/orElse to recover; use return yield* new Error() to propagate (ALWAYS use return yield* to signal the function stops)

Medium Freedom (preferred patterns, some variation acceptable)

These have recommended approaches but context matters:

Combinator selection: Choose based on need - catchTag for specific errors, catchTags for multiple, catch for all
Layer composition: Use Layer.provide for dependency injection, order matters for overrides
Concurrency control: Use Effect.all or Effect.forEach with appropriate concurrency option
Error recovery: Select retry schedules based on failure characteristics

High Freedom (multiple valid approaches, context-dependent)

These depend on application needs:

Application architecture: Service boundaries, layer organization, entry point structure
Testing strategies: Test at service level, effect level, or integration level based on needs
Performance optimization: Caching strategies, batching decisions, bundle size tradeoffs
Observability setup: Logging granularity, tracing scope, metric selection
Core Type
Effect<Success, Error, Requirements>;

Success: Value type on success
Error: Type-tracked errors
Requirements: Services needed (use never if none)
Key Operators

Transformation

map - Transform success value
flatMap / andThen - Chain effects
tap - Side effects without changing value
mapError - Transform error type

Error Handling

catch - Handle all errors (renamed from catchAll in earlier versions)
catchTag - Handle specific error types
catchTags - Handle multiple tagged errors at once
catchReason / catchReasons - Handle errors with reasons
catchFilter - Handle filtered errors (renamed from catchSome in earlier versions)
orElse - Fallback effect
retry - Retry with policy

Composition

all - Run multiple effects
forEach - Map over collection
zip / zipWith - Combine effects
provide - Supply dependencies
Best Practices
Use Effect.fn for functions that return Effects (not Effect.gen alone)
Define errors with Schema.TaggedErrorClass for type safety
Use Context.Service for dependency injection
Build layers explicitly with Layer.effect and compose with Layer.provide
Use ExecutionPlan for AI provider fallback strategies
Handle interruptions with acquireRelease for resources
Use Layer.launch as application entry point for long-running apps
Enable dual APIs when appropriate (data-first + data-last)
Choose resource patterns deliberately: See Resource Pattern Selector
Use error recovery for resilience: See Error Handling Decision Tree
Prefer Effect.forEach with concurrency: See Concurrency Anti-Patterns
Workflows

Use these checklists for complex multi-step tasks:

Creating a New Service

Copy this checklist and track progress:

Service Creation Progress:
- [ ] Step 1: Define error types with Schema.TaggedErrorClass
- [ ] Step 2: Create service class extending Context.Service
- [ ] Step 3: Implement methods using Effect.fn
- [ ] Step 4: Build Layer.effect with service implementation
- [ ] Step 5: Provide dependencies via Layer.provide
- [ ] Step 6: Test the service layer


Step 1: Define error types

class ServiceError extends Schema.TaggedErrorClass<ServiceError>()(
  "ServiceError",
  { cause: Schema.Defect },
) {}


Step 2: Create service class

export class MyService extends Context.Service<
  MyService,
  {
    method(): Effect.Effect<ReturnType, ServiceError>;
  }
>()("namespace/MyService") {}


Step 3: Implement methods

const method = Effect.fn("MyService.method")(function* () {
  // Implementation
});


Step 4-6: Build and test layer

See Services & Layers for complete examples.

Setting Up AI Integration

Copy this checklist and track progress:

AI Setup Progress:
- [ ] Step 1: Install provider packages (@effect/ai-openai, @effect/ai-anthropic)
- [ ] Step 2: Configure client layers with API keys
- [ ] Step 3: Define ExecutionPlan for fallback strategy
- [ ] Step 4: Create AI service with Effect.fn
- [ ] Step 5: Implement error handling with mapError
- [ ] Step 6: Provide client layers to service layer


See AI Modules for detailed implementation.

Error Handling Strategy

Copy this checklist and track progress:

Error Handling Progress:
- [ ] Step 1: Define all error types with Schema.TaggedErrorClass
- [ ] Step 2: Use catchTags for multiple specific error handlers
- [ ] Step 3: Add catch for final fallback if needed
- [ ] Step 4: Consider retry with Schedule for transient failures
- [ ] Step 5: Log errors at appropriate layers
- [ ] Step 6: Test error scenarios


See Error Handling for patterns and examples.

Common Patterns
Service with Effect.fn
import { Effect, Context, Layer, Schema } from "effect";

class DatabaseError extends Schema.TaggedErrorClass<DatabaseError>()(
  "DatabaseError",
  { cause: Schema.Defect },
) {}

export class Database extends Context.Service<
  Database,
  {
    query(sql: string): Effect.Effect<unknown[], DatabaseError>;
  }
>()("app/Database") {
  static readonly layer = Layer.effect(
    Database,
    Effect.gen(function* () {
      const query = Effect.fn("Database.query")(function* (sql: string) {
        yield* Effect.log("Executing SQL:", sql);
        return [{ id: 1, name: "Alice" }];
      });
      return Database.of({ query });
    }),
  );
}

// Exported type with proper inference
export type DatabaseService = Database["Service"];

Error Handling with catchTags
const configWithFallback = loadConfig().pipe(
  Effect.catchTags({
    ParseError: () => Effect.succeed(defaultConfig),
    FileError: () => Effect.succeed(defaultConfig),
  }),
);

Resource Safety
const program = Effect.acquireUseRelease(
  openFile("data.txt"),
  (file) => processFile(file),
  (file) => closeFile(file),
);

Package Structure

Core Package

import { Effect } from "effect";


Unstable Modules (may have breaking changes in minor releases)

import { Schema } from "effect/unstable/schema";
import { HttpClient } from "effect/unstable/http";
import { LanguageModel } from "effect/unstable/ai";
import { PubSub } from "effect/unstable/pubsub";


Platform-Specific Packages (separate packages)

import { NodeRuntime } from "@effect/platform-node";
import { SqlClient } from "@effect/sql-pg";
import { OpenAiClient } from "@effect/ai-openai";

References

Dive deeper into specific topics and patterns:

Core Patterns - Foundational Effect patterns with Effect.fn
Error Handling - Schema.TaggedErrorClass, catchTags, catchReason
Services & Layers - Dependency injection with Context
Concurrency - Fibers, racing, interruption, coordination
Data Types - Option, Either, Chunk, HashSet, Stream
Streams - Creating and consuming streams
PubSub - Event broadcasting and subscription
Schedules - Retry, repeat, and scheduling patterns
AI Modules - LLM integration with tools and chat
HTTP Client/Server - HttpClient and HttpApi
Resource Management - Scope, acquire/release patterns
Schema - Quick start & index
Observability - Logging, metrics, tracing with Otlp
Testing - @effect/vitest patterns
Integration - ManagedRuntime for non-Effect code
Batching - RequestResolver for batching
Child Process - Process management
CLI - CLI application building
Cluster - Distributed entities
Migration Guide - Migrating from Effect v3 to v4
Anti-Patterns to Avoid
Using try/catch with Effect (defeats type safety)
Mixing Promise-based and Effect-based code without conversion
Not handling all error cases (use catch or match)
Ignoring resource cleanup (always use acquireRelease)
Running effects at module level (breaks composability)
Using global state instead of Services
Overusing Effect for simple synchronous operations
Using Effect.gen alone instead of Effect.fn for functions
Troubleshooting

Type errors with Requirements

Ensure all services are provided via Effect.provide
Check Layer composition matches service dependencies
Use Effect.provideService for quick inline provisions

Effects not executing

Effects are lazy - must be run with runPromise, runSync, or runFork
Check that effect is actually yielded in generator context

Performance issues

Avoid excessive allocations in hot loops
Use Effect.cached for expensive computations
Consider Micro module for bundle-size sensitive apps
Example Files

Browse detailed examples in the effect-smol/ai-docs/src/ directory:

Effect Basics - Creating effects, pipe composition
Services - Context.Service, Layer composition
Error Handling - catchTags, catchReason, error hierarchies
Resources - acquireRelease, Scope
PubSub - Event broadcasting
Streams - Creating, consuming, encoding
Integration - ManagedRuntime for non-Effect code
Batching - RequestResolver patterns
Schedules - Retry and repeat strategies
Observability - Logging, tracing, metrics
Testing - @effect/vitest patterns
HTTP - HttpClient and HttpApi
Child Process - Process management
CLI - CLI application building
AI - Language models, tools, chat
Cluster - Distributed entities
Weekly Installs
8
Repository
felixnorden/skills
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn