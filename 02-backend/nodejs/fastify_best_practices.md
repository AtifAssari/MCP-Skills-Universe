---
rating: ⭐⭐
title: fastify-best-practices
url: https://skills.sh/jgamaraalv/ts-dev-kit/fastify-best-practices
---

# fastify-best-practices

skills/jgamaraalv/ts-dev-kit/fastify-best-practices
fastify-best-practices
Installation
$ npx skills add https://github.com/jgamaraalv/ts-dev-kit --skill fastify-best-practices
SKILL.md
Fastify 5 Best Practices
Table of Contents
Request lifecycle
Top anti-patterns
Quick patterns
Reference files

<quick_reference>

Request lifecycle (exact order)
Incoming Request
  └─ Routing
      └─ onRequest hooks
          └─ preParsing hooks
              └─ Content-Type Parsing
                  └─ preValidation hooks
                      └─ Schema Validation (→ 400 on failure)
                          └─ preHandler hooks
                              └─ Route Handler
                                  └─ preSerialization hooks
                                      └─ onSend hooks
                                          └─ Response Sent
                                              └─ onResponse hooks


Error at any stage → onError hooks → error handler → onSend → response → onResponse.

</quick_reference>

<anti_patterns>

Top anti-patterns

Mixing async/callback in handlers — Use async OR callbacks, never both. With async, return the value; don't call reply.send() AND return.

Returning undefined from async handler — Fastify treats this as "no response yet". Return the data or call reply.send().

Using arrow functions when you need this — Arrow functions don't bind this to the Fastify instance. Use function declarations for handlers that need this.

Forgetting fastify-plugin wrapper — Without it, decorators/hooks stay scoped to the child context. Parent and sibling plugins won't see them.

Decorating with reference types directly — decorateRequest('data', {}) shares the SAME object across all requests. Use null initial + onRequest hook to assign per-request.

Sending response in onError hook — onError is read-only for logging. Use setErrorHandler() to modify error responses.

Not handling reply.send() in async hooks — Call return reply after reply.send() in async hooks to prevent "Reply already sent" errors.

Ignoring encapsulation — Decorators/hooks registered in child plugins are invisible to parents. Design your plugin tree carefully.

String concatenation in SQL from route params — Always use parameterized queries. Fastify validates input shape, not content safety.

Missing response schema — Without response schema, Fastify serializes with JSON.stringify() (slow) and may leak sensitive fields. Use fast-json-stringify via response schemas.

</anti_patterns>

Quick patterns
Plugin with fastify-plugin (FastifyPluginCallback)

Project convention: use FastifyPluginCallback + done() (avoids require-await lint errors).

import fp from "fastify-plugin";
import type { FastifyPluginCallback } from "fastify";

const myPlugin: FastifyPluginCallback = (fastify, opts, done) => {
  fastify.decorate("myService", new MyService());
  done();
};

export default fp(myPlugin, { name: "my-plugin" });

Route with validation
fastify.post<{ Body: CreateUserBody }>("/users", {
  schema: {
    body: {
      type: "object",
      required: ["email", "name"],
      properties: {
        email: { type: "string", format: "email" },
        name: { type: "string", minLength: 1 },
      },
    },
    response: {
      201: {
        type: "object",
        properties: {
          id: { type: "string" },
          email: { type: "string" },
        },
      },
    },
  },
  handler: async (request, reply) => {
    const user = await createUser(request.body);
    return reply.code(201).send(user);
  },
});

Hook (application-level)
fastify.addHook("onRequest", async (request, reply) => {
  request.startTime = Date.now();
});

fastify.addHook("onResponse", async (request, reply) => {
  request.log.info({ elapsed: Date.now() - request.startTime }, "request completed");
});

Error handler
fastify.setErrorHandler((error, request, reply) => {
  request.log.error(error);
  const statusCode = error.statusCode ?? 500;
  reply.code(statusCode).send({
    error: statusCode >= 500 ? "Internal Server Error" : error.message,
  });
});

Reference files

Load the relevant file when you need detailed API information:

Server factory & options — constructor options, server methods, properties: references/server-and-options.md
Routes & handlers — declaration, URL params, async patterns, constraints: references/routes-and-handlers.md
Hooks & lifecycle — all 16 hook types, signatures, scope, early response: references/hooks-and-lifecycle.md
Plugins & encapsulation — creating plugins, fastify-plugin, context inheritance: references/plugins-and-encapsulation.md
Validation & serialization — JSON Schema, Ajv, response schemas, custom validators: references/validation-and-serialization.md
Request, Reply & errors — request/reply API, error handling, FST_ERR codes: references/request-reply-errors.md
TypeScript & logging — route generics, type providers, Pino config, decorators: references/typescript-and-logging.md
Weekly Installs
17
Repository
jgamaraalv/ts-dev-kit
GitHub Stars
14
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass