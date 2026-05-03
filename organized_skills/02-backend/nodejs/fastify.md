---
rating: ⭐⭐
title: fastify
url: https://skills.sh/bobmatnyc/claude-mpm-skills/fastify
---

# fastify

skills/bobmatnyc/claude-mpm-skills/fastify
fastify
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill fastify
SKILL.md
Fastify (TypeScript) - Production Backend Framework
Overview

Fastify is a high-performance Node.js web framework built around JSON schema validation, encapsulated plugins, and great developer ergonomics. In TypeScript, pair Fastify with a type provider (Zod or TypeBox) to keep runtime validation and static types aligned.

Quick Start
Minimal server

✅ Correct: basic server with typed response

import Fastify from "fastify";

const app = Fastify({ logger: true });

app.get("/health", async () => ({ status: "ok" as const }));

await app.listen({ host: "0.0.0.0", port: 3000 });


❌ Wrong: start server without awaiting listen

app.listen({ port: 3000 });
console.log("started"); // races startup and hides bind failures

Schema Validation + Type Providers

Fastify validates requests/responses via JSON schema. Use a type provider to avoid duplicating types.

Zod provider (recommended for full-stack TypeScript)

✅ Correct: Zod schema drives validation + types

import Fastify from "fastify";
import { z } from "zod";
import { ZodTypeProvider } from "fastify-type-provider-zod";

const app = Fastify({ logger: true }).withTypeProvider<ZodTypeProvider>();

const Query = z.object({ q: z.string().min(1) });

app.get(
  "/search",
  { schema: { querystring: Query } },
  async (req) => {
    return { q: req.query.q };
  },
);

await app.listen({ port: 3000 });

TypeBox provider (recommended for OpenAPI + performance)

✅ Correct: TypeBox schema

import Fastify from "fastify";
import { Type } from "@sinclair/typebox";
import { TypeBoxTypeProvider } from "@fastify/type-provider-typebox";

const app = Fastify({ logger: true }).withTypeProvider<TypeBoxTypeProvider>();

const Params = Type.Object({ id: Type.String({ minLength: 1 }) });
const Reply = Type.Object({ id: Type.String() });

app.get(
  "/users/:id",
  { schema: { params: Params, response: { 200: Reply } } },
  async (req) => ({ id: req.params.id }),
);

await app.listen({ port: 3000 });

Plugin Architecture (Encapsulation)

Use plugins to keep concerns isolated and testable (auth, db, routes).

✅ Correct: route plugin

import type { FastifyPluginAsync } from "fastify";

export const usersRoutes: FastifyPluginAsync = async (app) => {
  app.get("/", async () => [{ id: "1" }]);
  app.get("/:id", async (req) => ({ id: (req.params as any).id }));
};


✅ Correct: register with a prefix

app.register(usersRoutes, { prefix: "/api/v1/users" });

Error Handling

Centralize unexpected failures and return stable error shapes.

✅ Correct: setErrorHandler

app.setErrorHandler((err, req, reply) => {
  req.log.error({ err }, "request failed");
  reply.status(500).send({ error: "internal" as const });
});

Security Hardening (Baseline)

Add standard security plugins and enforce payload limits.

✅ Correct: Helmet + CORS + rate limiting

import helmet from "@fastify/helmet";
import cors from "@fastify/cors";
import rateLimit from "@fastify/rate-limit";

await app.register(helmet);
await app.register(cors, { origin: false });
await app.register(rateLimit, { max: 100, timeWindow: "1 minute" });

Graceful Shutdown

Close HTTP server and downstream clients (DB, queues) on SIGINT/SIGTERM.

✅ Correct: close on signals

const close = async (signal: string) => {
  app.log.info({ signal }, "shutting down");
  await app.close();
  process.exit(0);
};

process.on("SIGINT", () => void close("SIGINT"));
process.on("SIGTERM", () => void close("SIGTERM"));

Testing (Fastify inject)

Test routes in-memory without binding ports.

✅ Correct: inject request

import Fastify from "fastify";
import { describe, it, expect } from "vitest";

describe("health", () => {
  it("returns ok", async () => {
    const app = Fastify();
    app.get("/health", async () => ({ status: "ok" as const }));

    const res = await app.inject({ method: "GET", url: "/health" });
    expect(res.statusCode).toBe(200);
    expect(res.json()).toEqual({ status: "ok" });
  });
});

Decision Trees
Fastify vs Express
Prefer Fastify for schema-based validation, predictable plugins, and high throughput.
Prefer Express for minimal middleware and maximal ecosystem familiarity.
Zod vs TypeBox
Prefer Zod for app codebases that already standardize on Zod (forms, tRPC, shared types).
Prefer TypeBox for OpenAPI generation and performance-critical validation.
Anti-Patterns
Skip request validation; validate at boundaries with schemas.
Register everything in main.ts; isolate routes and dependencies into plugins.
Return raw error objects; return stable error shapes and log the details.
Resources
Fastify: https://www.fastify.io/
fastify-type-provider-zod: https://github.com/turkerdev/fastify-type-provider-zod
@fastify/type-provider-typebox: https://github.com/fastify/fastify-type-provider-typebox
Weekly Installs
345
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass