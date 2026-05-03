---
rating: ⭐⭐
title: typebox + fastify
url: https://skills.sh/blockmatic/basilic/typebox-+-fastify
---

# typebox + fastify

skills/blockmatic/basilic/TypeBox + Fastify
TypeBox + Fastify
Installation
$ npx skills add https://github.com/blockmatic/basilic --skill 'TypeBox + Fastify'
SKILL.md
Skill: fastify
Scope
Applies to: Fastify v5+ with TypeBox schemas, type-safe route definitions, automatic OpenAPI generation, plugins, hooks, testing
Does NOT cover: Database integration (see drizzle-orm)
Assumptions
Fastify v5+
@fastify/type-provider-typebox for TypeBox type provider
@sinclair/typebox for schema definitions
TypeScript v5+ with strict mode
Principles
Use TypeBox schemas for route validation (params, query, body, response)
Use TypeBoxTypeProvider for automatic type inference from schemas
Define response schemas for all status codes
Use OpenAPI generation from schemas (via @fastify/swagger)
Request types (request.params, request.query, request.body) are inferred from schemas
Response validation happens automatically based on schema
Constraints
MUST
Use TypeBoxTypeProvider for type safety: fastify.withTypeProvider<TypeBoxTypeProvider>()
Define response schemas for all status codes
Use TypeBox Type.* constructors for schema definitions
SHOULD
Use operationId in route schemas for OpenAPI generation
Use tags for route organization in OpenAPI docs
Define error response schemas for error cases
AVOID
Manual type assertions (types inferred from schemas)
Skipping response schema definitions
Mixing TypeBox with other schema libraries in same route
Interactions
Complements drizzle-orm for database integration
Generates OpenAPI specs compatible with openapi-ts codegen
Patterns
Route Schema Pattern
import { Type } from '@sinclair/typebox'
import type { FastifyPluginAsync } from 'fastify'

const UserSchema = Type.Object({
  id: Type.String(),
  email: Type.String({ format: 'email' }),
  name: Type.String(),
})

const userRoutes: FastifyPluginAsync = async fastify => {
  fastify.get('/users/:id', {
    schema: {
      operationId: 'getUser',
      params: Type.Object({ id: Type.String() }),
      response: {
        200: UserSchema,
        404: Type.Object({ code: Type.String(), message: Type.String() }),
      },
    },
  }, async (request, reply) => {
    // request.params.id is typed
    const { id } = request.params
    return reply.send(user)
  })
}

Schema Types
Type.String()
Type.Number()
Type.Boolean()
Type.Object({ id: Type.String() })
Type.Array(Type.String())
Type.Optional(Type.String())
Type.Union([Type.String(), Type.Number()])


See Route Schema Template for complete example.

Instance Configuration

Configure Fastify instance with TypeBox type provider, logger, and request settings:

import type { TypeBoxTypeProvider } from '@fastify/type-provider-typebox'
import Fastify from 'fastify'

const fastify = Fastify({
  logger: {
    level: 'info',
    transport: process.env.NODE_ENV === 'development' ? {
      target: 'pino-pretty',
    } : undefined,
  },
  trustProxy: true,
  bodyLimit: 1048576, // 1MB
  requestTimeout: 30000,
  requestIdHeader: 'x-request-id',
  requestIdLogLabel: 'reqId',
}).withTypeProvider<TypeBoxTypeProvider>()


See Instance Configuration for complete setup.

Plugin Development

Create reusable plugins with fastify-plugin for non-encapsulated behavior:

import type { FastifyPluginAsync } from 'fastify'
import fp from 'fastify-plugin'

const myPlugin: FastifyPluginAsync = async fastify => {
  // Plugin logic
}

export default fp(myPlugin, {
  name: 'my-plugin',
})


See Plugin Patterns and Plugin Template for examples.

Hooks (Request Lifecycle)

Use hooks to intercept requests, modify responses, or handle errors:

fastify.addHook('onRequest', async (request, reply) => {
  // Add security headers, logging, etc.
})

fastify.addHook('onResponse', async (request, reply) => {
  // Modify response, add headers, etc.
})

fastify.addHook('onError', async (request, reply, error) => {
  // Handle errors
})


See Hooks Guide and Hook Plugin Template for patterns.

Testing with inject()

Test routes using Fastify's inject() method for blackbox testing:

const response = await fastify.inject({
  method: 'GET',
  url: '/users/123',
})

expect(response.statusCode).toBe(200)
const data = JSON.parse(response.body)


See Testing Patterns and Test Utils Template for setup.

Streaming Responses

Handle streaming responses (e.g., Server-Sent Events, text streams):

fastify.post('/stream', {
  schema: {
    response: {
      200: Type.String({ description: 'Streaming response' }),
    },
  },
}, async (request, reply) => {
  reply.header('Content-Type', 'text/event-stream')
  reply.header('Cache-Control', 'no-cache')
  return reply.send(stream)
})

Common Plugins
Rate Limiting
import rateLimit from '@fastify/rate-limit'

await fastify.register(rateLimit, {
  max: 100,
  timeWindow: 60000,
  keyGenerator: request => request.ip,
})

CORS
import cors from '@fastify/cors'

await fastify.register(cors, {
  origin: (origin, callback) => {
    // Validate origin
    callback(null, true)
  },
  credentials: false,
})

Error Handler
fastify.setErrorHandler((error, request, reply) => {
  // Global error handling
  reply.status(error.statusCode ?? 500).send({
    code: 'ERROR',
    message: error.message,
  })
})

Graceful Shutdown

Handle process signals for graceful shutdown:

const shutdown = async (signal: string) => {
  fastify.log.info({ signal }, 'Shutting down')
  await fastify.close()
  process.exit(0)
}

process.on('SIGTERM', () => shutdown('SIGTERM'))
process.on('SIGINT', () => shutdown('SIGINT'))

AutoLoad Pattern

Use @fastify/autoload for automatic plugin/route discovery:

import AutoLoad from '@fastify/autoload'

await fastify.register(AutoLoad, {
  dir: path.join(__dirname, 'plugins'),
  forceESM: true,
})

References
OpenAPI Integration - OpenAPI generation patterns
Plugin Patterns - Plugin development with fastify-plugin
Hooks Guide - Request lifecycle hooks
Testing Patterns - Testing with inject()
Instance Configuration - Fastify instance setup
Weekly Installs
–
Repository
blockmatic/basilic
GitHub Stars
88
First Seen
–