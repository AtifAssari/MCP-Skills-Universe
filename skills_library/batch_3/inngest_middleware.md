---
title: inngest-middleware
url: https://skills.sh/inngest/inngest-skills/inngest-middleware
---

# inngest-middleware

skills/inngest/inngest-skills/inngest-middleware
inngest-middleware
Installation
$ npx skills add https://github.com/inngest/inngest-skills --skill inngest-middleware
SKILL.md
Inngest Middleware

Master Inngest middleware to handle cross-cutting concerns like logging, error tracking, dependency injection, and data transformation. Middleware runs at key points in the function lifecycle, enabling powerful patterns for observability and shared functionality.

These skills are focused on TypeScript. For Python or Go, refer to the Inngest documentation for language-specific guidance. Core concepts apply across all languages.

Note: The middleware system was significantly rewritten in v4. The lifecycle hooks documented here reflect the v4 API. If migrating from v3, consult the migration guide for details on breaking changes.

What is Middleware?

Middleware allows code to run at various points in an Inngest client's lifecycle - during function execution, event sending, and more. Think of middleware as hooks into the Inngest execution pipeline.

When to use middleware:

Observability: Add logging, tracing, or metrics
Dependency injection: Share client instances across functions
Data transformation: Encrypt/decrypt, validate, or enrich data
Error handling: Custom error tracking and alerting
Authentication: Validate user context or permissions
Middleware Lifecycle

Middleware can be registered at client-level (affects all functions) or function-level (affects specific functions).

Execution Order
const inngest = new Inngest({
  id: "my-app",
  middleware: [
    loggingMiddleware, // Runs 1st
    errorMiddleware // Runs 2nd
  ]
});

inngest.createFunction(
  {
    id: "example",
    middleware: [
      authMiddleware, // Runs 3rd
      metricsMiddleware // Runs 4th
    ],
    triggers: [{ event: "test" }]
  },
  async () => {
    /* function code */
  }
);


Order matters: Client middleware runs first, then function middleware, in the order specified.

Creating Custom Middleware
Basic Middleware Structure
import { InngestMiddleware } from "inngest";

const loggingMiddleware = new InngestMiddleware({
  name: "Logging Middleware",
  init() {
    // Setup phase - runs when client initializes
    const logger = setupLogger();

    return {
      // Function execution lifecycle
      // Note: `fn` is loosely typed in middleware generics; fn.id works at runtime
      onFunctionRun({ ctx, fn }) {
        return {
          beforeExecution() {
            logger.info("Function starting", {
              functionId: fn.id,
              eventName: ctx.event.name,
              runId: ctx.runId
            });
          },

          afterExecution() {
            logger.info("Function completed", {
              functionId: fn.id,
              runId: ctx.runId
            });
          },

          transformOutput({ result }) {
            // Log function output
            logger.debug("Function output", {
              functionId: fn.id,
              output: result.data
            });

            // Return unmodified result
            return { result };
          }
        };
      },

      // Event sending lifecycle
      onSendEvent() {
        return {
          transformInput({ payloads }) {
            logger.info("Sending events", {
              count: payloads.length,
              events: payloads.map((p) => p.name)
            });

            // Spread to convert readonly array to mutable array
            return { payloads: [...payloads] };
          }
        };
      }
    };
  }
});

Python Implementation

Python middleware follows a similar pattern. See Dependency Injection Reference for complete Python examples.


## Dependency Injection

Share expensive or stateful clients across all functions. **See [Dependency Injection Reference](./references/dependency-injection.md) for detailed patterns.**

### Quick Example - Built-in DI

```typescript
import { dependencyInjectionMiddleware } from "inngest";

const inngest = new Inngest({
  id: 'my-app',
  middleware: [
    dependencyInjectionMiddleware({
      openai: new OpenAI(),
      db: new PrismaClient(),
    }),
  ],
});

// Functions automatically get injected dependencies
inngest.createFunction(
  { id: "ai-summary", triggers: [{ event: "document/uploaded" }] },
  async ({ event, openai, db }) => {
    // Dependencies available in function context
    const summary = await openai.chat.completions.create({
      messages: [{ role: "user", content: event.data.content }],
      model: "gpt-4",
    });

    await db.document.update({
      where: { id: event.data.documentId },
      data: { summary: summary.choices[0].message.content }
    });
  }
);

Middleware Packages

Beyond dependencyInjectionMiddleware (built-in, shown above), Inngest provides official middleware as separate packages. See Middleware Reference for complete details.

Encryption Middleware
npm install @inngest/middleware-encryption

import { encryptionMiddleware } from "@inngest/middleware-encryption";

const inngest = new Inngest({
  id: "my-app",
  middleware: [
    encryptionMiddleware({
      key: process.env.ENCRYPTION_KEY
    })
  ]
});


Automatically encrypts all step data, function output, and event data.encrypted field. Supports key rotation via fallbackDecryptionKeys.

Sentry Error Tracking
npm install @inngest/middleware-sentry

import * as Sentry from "@sentry/node";
import { sentryMiddleware } from "@inngest/middleware-sentry";

Sentry.init({
  /* your Sentry config */
});

const inngest = new Inngest({
  id: "my-app",
  middleware: [sentryMiddleware()]
});


Captures exceptions, adds tracing to each function run, and includes function ID and event names as context. Requires @sentry/*@>=8.0.0.

Common Middleware Patterns
Metrics and Performance Tracking
const metricsMiddleware = new InngestMiddleware({
  name: "Metrics Tracking",
  init() {
    return {
      onFunctionRun({ ctx, fn }) {
        let startTime: number;

        return {
          beforeExecution() {
            startTime = Date.now();
            metrics.increment("inngest.step.started", {
              function: fn.id,
              event: ctx.event.name
            });
          },

          afterExecution() {
            const duration = Date.now() - startTime;
            metrics.histogram("inngest.step.duration", duration, {
              function: fn.id,
              event: ctx.event.name
            });
          },

          transformOutput({ result }) {
            const status = result.error ? "error" : "success";
            metrics.increment("inngest.step.completed", {
              function: fn.id,
              status: status
            });

            return { result };
          }
        };
      }
    };
  }
});

Advanced Patterns

Authentication: Validate tokens and inject user context Conditional logic: Apply middleware based on event type or function Circuit breakers: Prevent cascading failures from external services

Configuration-Based Middleware

Create reusable middleware with configuration options for different environments and use cases. See reference documentation for complete examples.

Best Practices
Design Principles
Keep middleware focused: One concern per middleware
Handle errors gracefully: Don't let middleware crash functions
Consider performance: Middleware runs on every execution
Use proper typing: Let TypeScript infer middleware types
Test thoroughly: Middleware affects all functions that use it
Common Use Cases to Implement
Retry logic for transient failures
Circuit breakers for external service calls
Request/response logging for debugging
User context enrichment from external sources
Feature flags for gradual rollouts
Custom authentication and authorization checks
Error Handling in Middleware
const robustMiddleware = new InngestMiddleware({
  name: "Robust Middleware",
  init() {
    return {
      onFunctionRun({ ctx, fn }) {
        return {
          transformOutput({ result }) {
            try {
              // Your middleware logic here
              return performTransformation(result);
            } catch (middlewareError) {
              // Log error but don't break the function
              console.error("Middleware error:", middlewareError);

              // Return original result on middleware failure
              return { result };
            }
          }
        };
      }
    };
  }
});

Testing Middleware

Use Inngest's testing utilities (createMockContext, createMockFunction) to unit test middleware behavior.

For complete implementation examples and advanced patterns, see:

Dependency Injection Reference
Built-in Middleware Reference
Weekly Installs
539
Repository
inngest/inngest-skills
GitHub Stars
17
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn