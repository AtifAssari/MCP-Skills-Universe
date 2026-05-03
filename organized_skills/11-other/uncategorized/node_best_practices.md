---
rating: ⭐⭐
title: node-best-practices
url: https://skills.sh/mcollina/skills/node-best-practices
---

# node-best-practices

skills/mcollina/skills/node-best-practices
node-best-practices
Installation
$ npx skills add https://github.com/mcollina/skills --skill node-best-practices
Summary

Native TypeScript support in Node.js with type stripping, async patterns, error handling, and production best practices.

Covers type stripping (Node.js 22.6+) for running .ts files directly without build tools; includes tsconfig.json setup and import extension rules
Provides patterns for error handling, graceful shutdown, async/await, streams, and module resolution across the full Node.js stack
Includes diagnostic workflows for flaky tests, profiling slow paths, and performance optimization with concrete examples
Addresses environment configuration, logging, caching strategies, and testing approaches tailored to Node.js applications
SKILL.md
When to use

Use this skill whenever you are dealing with Node.js code to obtain domain-specific knowledge for building robust, performant, and maintainable Node.js applications.

TypeScript with Type Stripping

When writing TypeScript for Node.js, use type stripping (Node.js 22.6+) instead of build tools like ts-node or tsx. Type stripping runs TypeScript directly by removing type annotations at runtime without transpilation.

Key requirements for type stripping compatibility:

Use import type for type-only imports
Use const objects instead of enums
Avoid namespaces and parameter properties
Use .ts extensions in imports

Minimal example — a valid type-stripped TypeScript file:

// greet.ts
import type { IncomingMessage } from 'node:http';

const greet = (name: string): string => `Hello, ${name}!`;
console.log(greet('world'));


Run directly with:

node greet.ts


See rules/typescript.md for complete configuration and examples.

Common Workflows

For multi-step processes, follow these high-level sequences before consulting the relevant rule file:

Graceful shutdown: Register signal handlers (SIGTERM/SIGINT) → stop accepting new work → drain in-flight requests → close external connections (DB, cache) → exit with appropriate code. See rules/graceful-shutdown.md.

Error handling: Define a shared error base class → classify errors (operational vs programmer) → add async boundary handlers (process.on('unhandledRejection')) → propagate typed errors through the call stack → log with context before responding or crashing. See rules/error-handling.md.

Diagnosing flaky tests: Isolate the test with --test-only → check for shared state or timer dependencies → inspect async teardown order → add retry logic as a temporary diagnostic step → fix root cause. See rules/flaky-tests.md.

Profiling a slow path: Reproduce under realistic load → capture a CPU profile with --cpu-prof → identify hot functions → check for stream backpressure or unnecessary serialisation → validate improvement with a benchmark. See rules/profiling.md and rules/performance.md.

How to use

Read individual rule files for detailed explanations and code examples:

rules/error-handling.md - Error handling patterns in Node.js
rules/async-patterns.md - Async/await and Promise patterns
rules/streams.md - Working with Node.js streams
rules/modules.md - ES Modules and CommonJS patterns
rules/testing.md - Testing strategies for Node.js applications
rules/flaky-tests.md - Identifying and diagnosing flaky tests with node:test
rules/node-modules-exploration.md - Navigating and analyzing node_modules directories
rules/performance.md - Performance optimization techniques
rules/caching.md - Caching patterns and libraries
rules/profiling.md - Profiling and benchmarking tools
rules/logging.md - Logging and debugging patterns
rules/environment.md - Environment configuration and secrets management
rules/graceful-shutdown.md - Graceful shutdown and signal handling
rules/typescript.md - TypeScript configuration and type stripping in Node.js
Weekly Installs
418
Repository
mcollina/skills
GitHub Stars
1.8K
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass