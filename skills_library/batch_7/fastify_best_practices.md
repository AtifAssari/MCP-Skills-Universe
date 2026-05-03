---
title: fastify-best-practices
url: https://skills.sh/mcollina/skills/fastify-best-practices
---

# fastify-best-practices

skills/mcollina/skills/fastify-best-practices
fastify-best-practices
Installation
$ npx skills add https://github.com/mcollina/skills --skill fastify-best-practices
Summary

Comprehensive guidance for building Fastify Node.js backends with TypeScript, covering routes, plugins, validation, and production deployment.

Covers 16+ core topics including plugins, route organization, JSON Schema validation, error handling, hooks, authentication, testing, logging with Pino, and TypeScript integration via strip types
Includes recommended reading paths for common scenarios: new projects, adding authentication, performance optimization, testing setup, and production deployment
Addresses full request lifecycle management, response serialization, CORS and security headers, WebSocket support, database integration, and HTTP proxying
Emphasizes schema-first development, plugin encapsulation, async/await patterns, and Fastify's built-in performance optimizations with minimal external dependencies
SKILL.md
When to use

Use this skill when you need to:

Develop backend applications using Fastify
Implement Fastify plugins and route handlers
Get guidance on Fastify architecture and patterns
Use TypeScript with Fastify (strip types)
Implement testing with Fastify's inject method
Configure validation, serialization, and error handling
Quick Start

A minimal, runnable Fastify server to get started immediately:

import Fastify from 'fastify'

const app = Fastify({ logger: true })

app.get('/health', async (request, reply) => {
  return { status: 'ok' }
})

const start = async () => {
  await app.listen({ port: 3000, host: '0.0.0.0' })
}
start()

Recommended Reading Order for Common Scenarios
New to Fastify? Start with plugins.md → routes.md → schemas.md
Adding authentication: plugins.md → hooks.md → authentication.md
Improving performance: schemas.md → serialization.md → performance.md
Setting up testing: routes.md → testing.md
Going to production: logging.md → configuration.md → deployment.md
How to use

Read individual rule files for detailed explanations and code examples:

rules/plugins.md - Plugin development and encapsulation
rules/routes.md - Route organization and handlers
rules/schemas.md - JSON Schema validation
rules/error-handling.md - Error handling patterns
rules/hooks.md - Hooks and request lifecycle
rules/authentication.md - Authentication and authorization
rules/testing.md - Testing with inject()
rules/performance.md - Performance optimization
rules/logging.md - Logging with Pino
rules/typescript.md - TypeScript integration
rules/decorators.md - Decorators and extensions
rules/content-type.md - Content type parsing
rules/serialization.md - Response serialization
rules/cors-security.md - CORS and security headers
rules/websockets.md - WebSocket support
rules/database.md - Database integration patterns
rules/configuration.md - Application configuration
rules/deployment.md - Production deployment
rules/http-proxy.md - HTTP proxying and reply.from()
Core Principles
Encapsulation: Fastify's plugin system provides automatic encapsulation
Schema-first: Define schemas for validation and serialization
Performance: Fastify is optimized for speed; use its features correctly
Async/await: All handlers and hooks support async functions
Minimal dependencies: Prefer Fastify's built-in features and official plugins
Weekly Installs
1.8K
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