---
rating: ⭐⭐⭐
title: hono-middleware
url: https://skills.sh/bobmatnyc/claude-mpm-skills/hono-middleware
---

# hono-middleware

skills/bobmatnyc/claude-mpm-skills/hono-middleware
hono-middleware
Installation
$ npx skills add https://github.com/bobmatnyc/claude-mpm-skills --skill hono-middleware
SKILL.md
Hono Middleware Patterns
Overview

Hono provides a powerful middleware system with an "onion" execution model. Middleware processes requests before handlers and responses after handlers, enabling cross-cutting concerns like authentication, logging, and CORS.

Key Features:

Onion-style execution order
Type-safe middleware creation with createMiddleware
25+ built-in middleware
Context variable passing between middleware
Async/await support throughout
When to Use This Skill

Use Hono middleware when:

Adding authentication/authorization
Implementing CORS for cross-origin requests
Adding request logging or timing
Compressing responses
Rate limiting API endpoints
Validating requests before handlers
Middleware Basics
Inline Middleware
import { Hono } from 'hono'

const app = new Hono()

// Simple logging middleware
app.use('*', async (c, next) => {
  console.log(`[${c.req.method}] ${c.req.url}`)
  await next()
})

// Path-specific middleware
app.use('/api/*', async (c, next) => {
  const start = Date.now()
  await next()
  const ms = Date.now() - start
  c.header('X-Response-Time', `${ms}ms`)
})

Execution Order (Onion Model)
app.use(async (c, next) => {
  console.log('1. Before (first in)')
  await next()
  console.log('6. After (first out)')
})

app.use(async (c, next) => {
  console.log('2. Before (second in)')
  await next()
  console.log('5. After (second out)')
})

app.use(async (c, next) => {
  console.log('3. Before (third in)')
  await next()
  console.log('4. After (third out)')
})

app.get('/', (c) => {
  console.log('Handler')
  return c.text('Hello!')
})

// Output:
// 1. Before (first in)
// 2. Before (second in)
// 3. Before (third in)
// Handler
// 4. After (third out)
// 5. After (second out)
// 6. After (first out)

Creating Reusable Middleware
import { createMiddleware } from 'hono/factory'

// Type-safe reusable middleware
const logger = createMiddleware(async (c, next) => {
  console.log(`[${new Date().toISOString()}] ${c.req.method} ${c.req.path}`)
  await next()
})

// Middleware with options
const timing = (headerName = 'X-Response-Time') => {
  return createMiddleware(async (c, next) => {
    const start = Date.now()
    await next()
    c.header(headerName, `${Date.now() - start}ms`)
  })
}

app.use(logger)
app.use(timing('X-Duration'))

Context Variables
Passing Data Between Middleware
import { createMiddleware } from 'hono/factory'

// Define variable types
type Variables = {
  user: { id: string; email: string; role: string }
  requestId: string
}

const app = new Hono<{ Variables: Variables }>()

// Auth middleware sets user
const auth = createMiddleware<{ Variables: Variables }>(async (c, next) => {
  const token = c.req.header('Authorization')?.replace('Bearer ', '')

  if (!token) {
    return c.json({ error: 'Unauthorized' }, 401)
  }

  const user = await verifyToken(token)
  c.set('user', user)  // Type-safe!
  await next()
})

// Request ID middleware
const requestId = createMiddleware<{ Variables: Variables }>(async (c, next) => {
  c.set('requestId', crypto.randomUUID())
  await next()
})

app.use(requestId)
app.use('/api/*', auth)

app.get('/api/profile', (c) => {
  const user = c.get('user')      // Type: { id, email, role }
  const reqId = c.get('requestId') // Type: string
  return c.json({ user, requestId: reqId })
})

Built-in Middleware
CORS
import { cors } from 'hono/cors'

// Simple - allow all origins
app.use('/api/*', cors())

// Configured
app.use('/api/*', cors({
  origin: ['https://example.com', 'https://app.example.com'],
  allowMethods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowHeaders: ['Content-Type', 'Authorization'],
  exposeHeaders: ['X-Total-Count'],
  credentials: true,
  maxAge: 86400
}))

// Dynamic origin
app.use('/api/*', cors({
  origin: (origin) => {
    return origin.endsWith('.example.com')
      ? origin
      : 'https://example.com'
  }
}))

Bearer Auth
import { bearerAuth } from 'hono/bearer-auth'

// Simple token validation
app.use('/api/*', bearerAuth({ token: 'my-secret-token' }))

// Multiple tokens
app.use('/api/*', bearerAuth({
  token: ['token1', 'token2', 'token3']
}))

// Custom verification
app.use('/api/*', bearerAuth({
  verifyToken: async (token, c) => {
    const user = await validateJWT(token)
    if (user) {
      c.set('user', user)
      return true
    }
    return false
  }
}))

Basic Auth
import { basicAuth } from 'hono/basic-auth'

app.use('/admin/*', basicAuth({
  username: 'admin',
  password: 'secret'  // pragma: allowlist secret
}))

// Multiple users
app.use('/admin/*', basicAuth({
  verifyUser: (username, password, c) => {
    return username === 'admin' && password === process.env.ADMIN_PASSWORD
  }
}))

JWT Auth
import { jwt } from 'hono/jwt'

app.use('/api/*', jwt({
  secret: 'my-jwt-secret'  // pragma: allowlist secret
}))

// Access payload in handler
app.get('/api/profile', (c) => {
  const payload = c.get('jwtPayload')
  return c.json({ userId: payload.sub })
})

// With algorithm
app.use('/api/*', jwt({
  secret: 'secret',  // pragma: allowlist secret
  alg: 'HS256'
}))

Logger
import { logger } from 'hono/logger'

// Default format
app.use(logger())

// Custom format
app.use(logger((str, ...rest) => {
  console.log(`[API] ${str}`, ...rest)
}))

// Output: <-- GET /api/users
//         --> GET /api/users 200 12ms

Pretty JSON
import { prettyJSON } from 'hono/pretty-json'

// Add ?pretty to format JSON responses
app.use(prettyJSON())

// GET /api/users         → {"users":[...]}
// GET /api/users?pretty  → formatted JSON

Compress
import { compress } from 'hono/compress'

app.use(compress())

// With options
app.use(compress({
  encoding: 'gzip'  // 'gzip' | 'deflate'
}))

ETag
import { etag } from 'hono/etag'

app.use(etag())

// Weak ETags
app.use(etag({ weak: true }))

Cache
import { cache } from 'hono/cache'

// Cloudflare Workers cache
app.use('/static/*', cache({
  cacheName: 'my-app',
  cacheControl: 'max-age=3600'
}))

Secure Headers
import { secureHeaders } from 'hono/secure-headers'

app.use(secureHeaders())

// Configured
app.use(secureHeaders({
  contentSecurityPolicy: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", "'unsafe-inline'"]
  },
  xFrameOptions: 'DENY',
  xXssProtection: '1; mode=block'
}))

CSRF Protection
import { csrf } from 'hono/csrf'

app.use(csrf())

// With options
app.use(csrf({
  origin: ['https://example.com']
}))

Timeout
import { timeout } from 'hono/timeout'

// 5 second timeout
app.use('/api/*', timeout(5000))

// Custom error
app.use('/api/*', timeout(5000, () => {
  return new Response('Request timeout', { status: 408 })
}))

Request ID
import { requestId } from 'hono/request-id'

app.use(requestId())

app.get('/', (c) => {
  const id = c.get('requestId')
  return c.json({ requestId: id })
})

Advanced Patterns
Conditional Middleware
// Apply middleware based on condition
const conditionalAuth = createMiddleware(async (c, next) => {
  // Skip auth for health checks
  if (c.req.path === '/health') {
    return next()
  }

  // Apply auth for everything else
  const token = c.req.header('Authorization')
  if (!token) {
    return c.json({ error: 'Unauthorized' }, 401)
  }

  await next()
})

Middleware Composition
import { every, some } from 'hono/combine'

// All middleware must pass
const strictAuth = every(
  bearerAuth({ token: 'secret' }),
  ipRestriction(['192.168.1.0/24']),
  rateLimiter({ max: 100 })
)

// Any middleware can pass
const flexibleAuth = some(
  bearerAuth({ token: 'api-key' }),
  basicAuth({ username: 'user', password: 'pass' })  // pragma: allowlist secret
)

app.use('/api/*', strictAuth)
app.use('/public/*', flexibleAuth)

Modifying Responses
const addHeaders = createMiddleware(async (c, next) => {
  await next()

  // Modify response after handler
  c.res.headers.set('X-Powered-By', 'Hono')
  c.res.headers.set('X-Request-Id', c.get('requestId'))
})

const transformResponse = createMiddleware(async (c, next) => {
  await next()

  // Replace response entirely
  const originalBody = await c.res.json()
  c.res = new Response(
    JSON.stringify({ data: originalBody, timestamp: Date.now() }),
    c.res
  )
})

Error Handling in Middleware
import { HTTPException } from 'hono/http-exception'

const safeMiddleware = createMiddleware(async (c, next) => {
  try {
    await next()
  } catch (error) {
    if (error instanceof HTTPException) {
      throw error  // Re-throw HTTP exceptions
    }

    // Log and convert other errors
    console.error('Middleware error:', error)
    throw new HTTPException(500, { message: 'Internal error' })
  }
})

Rate Limiting
// Simple in-memory rate limiter
const rateLimiter = (options: { max: number; window: number }) => {
  const requests = new Map<string, { count: number; reset: number }>()

  return createMiddleware(async (c, next) => {
    const ip = c.req.header('CF-Connecting-IP') || 'unknown'
    const now = Date.now()

    let record = requests.get(ip)

    if (!record || now > record.reset) {
      record = { count: 0, reset: now + options.window }
      requests.set(ip, record)
    }

    record.count++

    if (record.count > options.max) {
      c.header('Retry-After', String(Math.ceil((record.reset - now) / 1000)))
      return c.json({ error: 'Rate limit exceeded' }, 429)
    }

    c.header('X-RateLimit-Limit', String(options.max))
    c.header('X-RateLimit-Remaining', String(options.max - record.count))

    await next()
  })
}

app.use('/api/*', rateLimiter({ max: 100, window: 60000 }))

Middleware Order Best Practices
const app = new Hono()

// 1. Request ID (first - for tracking)
app.use(requestId())

// 2. Logger (early - to log all requests)
app.use(logger())

// 3. Security headers
app.use(secureHeaders())

// 4. CORS (before auth - for preflight)
app.use('/api/*', cors())

// 5. Compression
app.use(compress())

// 6. Rate limiting
app.use('/api/*', rateLimiter({ max: 100, window: 60000 }))

// 7. Authentication
app.use('/api/*', bearerAuth({ verifyToken }))

// 8. Request validation (after auth)
app.use('/api/*', validator)

// 9. Routes
app.route('/api', apiRoutes)

// 10. Not found handler (last)
app.notFound((c) => c.json({ error: 'Not found' }, 404))

Quick Reference
Built-in Middleware
Middleware	Import	Purpose
cors	hono/cors	Cross-origin requests
bearerAuth	hono/bearer-auth	Bearer token auth
basicAuth	hono/basic-auth	HTTP Basic auth
jwt	hono/jwt	JWT verification
logger	hono/logger	Request logging
prettyJSON	hono/pretty-json	JSON formatting
compress	hono/compress	Response compression
etag	hono/etag	ETag headers
cache	hono/cache	Response caching
secureHeaders	hono/secure-headers	Security headers
csrf	hono/csrf	CSRF protection
timeout	hono/timeout	Request timeout
requestId	hono/request-id	Request ID header
Third-Party Middleware
npm install @hono/zod-validator    # Zod validation
npm install @hono/graphql-server   # GraphQL
npm install @hono/swagger-ui       # Swagger UI
npm install @hono/prometheus       # Prometheus metrics
npm install @hono/sentry           # Sentry error tracking

Related Skills
hono-core - Framework fundamentals
hono-validation - Request validation with Zod
hono-cloudflare - Cloudflare-specific middleware

Version: Hono 4.x Last Updated: January 2025 License: MIT

Weekly Installs
232
Repository
bobmatnyc/claud…m-skills
GitHub Stars
40
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail