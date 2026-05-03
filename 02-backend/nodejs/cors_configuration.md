---
title: cors-configuration
url: https://skills.sh/patricio0312rev/skills/cors-configuration
---

# cors-configuration

skills/patricio0312rev/skills/cors-configuration
cors-configuration
Installation
$ npx skills add https://github.com/patricio0312rev/skills --skill cors-configuration
SKILL.md
CORS Configuration

Configure secure Cross-Origin Resource Sharing for APIs and web applications.

Core Workflow
Identify origins: Define allowed origins
Configure headers: Set CORS response headers
Handle preflight: OPTIONS request handling
Set credentials: Cookie and auth handling
Limit methods: Allowed HTTP methods
Test configuration: Verify CORS works
CORS Headers Reference
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
Access-Control-Allow-Headers: Content-Type, Authorization, X-Request-ID
Access-Control-Allow-Credentials: true
Access-Control-Max-Age: 86400
Access-Control-Expose-Headers: X-Request-ID, X-RateLimit-Remaining

Express.js Configuration
Basic CORS
// middleware/cors.ts
import cors from 'cors';
import { Express } from 'express';

const allowedOrigins = [
  'https://app.example.com',
  'https://admin.example.com',
];

// Add development origins
if (process.env.NODE_ENV === 'development') {
  allowedOrigins.push('http://localhost:3000');
  allowedOrigins.push('http://localhost:5173');
}

export function configureCors(app: Express) {
  app.use(cors({
    origin: (origin, callback) => {
      // Allow requests with no origin (mobile apps, Postman)
      if (!origin) {
        return callback(null, true);
      }

      if (allowedOrigins.includes(origin)) {
        return callback(null, true);
      }

      callback(new Error('Not allowed by CORS'));
    },
    methods: ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS'],
    allowedHeaders: [
      'Content-Type',
      'Authorization',
      'X-Request-ID',
      'X-CSRF-Token',
    ],
    exposedHeaders: [
      'X-Request-ID',
      'X-RateLimit-Limit',
      'X-RateLimit-Remaining',
    ],
    credentials: true,
    maxAge: 86400, // 24 hours
    preflightContinue: false,
    optionsSuccessStatus: 204,
  }));
}

Manual CORS Middleware
// middleware/manual-cors.ts
import { Request, Response, NextFunction } from 'express';

interface CorsOptions {
  origins: string[];
  methods: string[];
  allowedHeaders: string[];
  exposedHeaders: string[];
  credentials: boolean;
  maxAge: number;
}

const defaultOptions: CorsOptions = {
  origins: [],
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  exposedHeaders: [],
  credentials: false,
  maxAge: 86400,
};

export function createCorsMiddleware(options: Partial<CorsOptions> = {}) {
  const config = { ...defaultOptions, ...options };

  return (req: Request, res: Response, next: NextFunction) => {
    const origin = req.headers.origin;

    // Check if origin is allowed
    if (origin && config.origins.includes(origin)) {
      res.setHeader('Access-Control-Allow-Origin', origin);
    } else if (config.origins.includes('*')) {
      res.setHeader('Access-Control-Allow-Origin', '*');
    }

    // Set other CORS headers
    res.setHeader('Access-Control-Allow-Methods', config.methods.join(', '));
    res.setHeader('Access-Control-Allow-Headers', config.allowedHeaders.join(', '));

    if (config.exposedHeaders.length > 0) {
      res.setHeader('Access-Control-Expose-Headers', config.exposedHeaders.join(', '));
    }

    if (config.credentials) {
      res.setHeader('Access-Control-Allow-Credentials', 'true');
    }

    res.setHeader('Access-Control-Max-Age', String(config.maxAge));

    // Handle preflight request
    if (req.method === 'OPTIONS') {
      res.status(204).end();
      return;
    }

    next();
  };
}

Route-Specific CORS
// routes/api.ts
import { Router } from 'express';
import cors from 'cors';

const router = Router();

// Public endpoints - allow any origin
const publicCors = cors({
  origin: '*',
  methods: ['GET'],
});

// Private endpoints - restrict origin
const privateCors = cors({
  origin: ['https://app.example.com'],
  credentials: true,
});

// Webhook endpoints - specific origins
const webhookCors = cors({
  origin: ['https://stripe.com', 'https://github.com'],
  methods: ['POST'],
});

router.get('/public/data', publicCors, publicDataHandler);
router.post('/private/data', privateCors, privateDataHandler);
router.post('/webhooks/stripe', webhookCors, stripeWebhookHandler);

export default router;

Next.js Configuration
Middleware CORS
// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

const allowedOrigins = [
  'https://app.example.com',
  'https://admin.example.com',
];

if (process.env.NODE_ENV === 'development') {
  allowedOrigins.push('http://localhost:3000');
}

export function middleware(request: NextRequest) {
  const origin = request.headers.get('origin');
  const isApiRoute = request.nextUrl.pathname.startsWith('/api');

  // Only apply CORS to API routes
  if (!isApiRoute) {
    return NextResponse.next();
  }

  // Handle preflight
  if (request.method === 'OPTIONS') {
    const response = new NextResponse(null, { status: 204 });

    if (origin && allowedOrigins.includes(origin)) {
      response.headers.set('Access-Control-Allow-Origin', origin);
      response.headers.set('Access-Control-Allow-Credentials', 'true');
      response.headers.set('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
      response.headers.set('Access-Control-Allow-Headers', 'Content-Type, Authorization');
      response.headers.set('Access-Control-Max-Age', '86400');
    }

    return response;
  }

  // Handle actual request
  const response = NextResponse.next();

  if (origin && allowedOrigins.includes(origin)) {
    response.headers.set('Access-Control-Allow-Origin', origin);
    response.headers.set('Access-Control-Allow-Credentials', 'true');
  }

  return response;
}

export const config = {
  matcher: '/api/:path*',
};

API Route CORS
// app/api/data/route.ts
import { NextRequest, NextResponse } from 'next/server';

const allowedOrigins = ['https://app.example.com'];

function corsHeaders(origin: string | null) {
  const headers: Record<string, string> = {};

  if (origin && allowedOrigins.includes(origin)) {
    headers['Access-Control-Allow-Origin'] = origin;
    headers['Access-Control-Allow-Credentials'] = 'true';
  }

  return headers;
}

export async function OPTIONS(request: NextRequest) {
  const origin = request.headers.get('origin');

  return new NextResponse(null, {
    status: 204,
    headers: {
      ...corsHeaders(origin),
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
      'Access-Control-Max-Age': '86400',
    },
  });
}

export async function GET(request: NextRequest) {
  const origin = request.headers.get('origin');

  const data = { message: 'Hello' };

  return NextResponse.json(data, {
    headers: corsHeaders(origin),
  });
}

export async function POST(request: NextRequest) {
  const origin = request.headers.get('origin');

  // Verify origin for mutations
  if (!origin || !allowedOrigins.includes(origin)) {
    return new NextResponse('Forbidden', { status: 403 });
  }

  const body = await request.json();
  const result = await processData(body);

  return NextResponse.json(result, {
    headers: corsHeaders(origin),
  });
}

Fastify Configuration
// plugins/cors.ts
import fastifyCors from '@fastify/cors';
import { FastifyInstance } from 'fastify';

export async function configureCors(fastify: FastifyInstance) {
  await fastify.register(fastifyCors, {
    origin: (origin, callback) => {
      const allowedOrigins = [
        'https://app.example.com',
        'https://admin.example.com',
      ];

      if (!origin || allowedOrigins.includes(origin)) {
        callback(null, true);
      } else {
        callback(new Error('Not allowed'), false);
      }
    },
    methods: ['GET', 'POST', 'PUT', 'DELETE'],
    allowedHeaders: ['Content-Type', 'Authorization'],
    exposedHeaders: ['X-Request-ID'],
    credentials: true,
    maxAge: 86400,
    preflight: true,
    strictPreflight: true,
  });
}

Dynamic Origin Validation
// lib/cors/validator.ts
interface CorsConfig {
  allowedOrigins: string[];
  allowedPatterns: RegExp[];
  allowSubdomains: string[];
}

const config: CorsConfig = {
  allowedOrigins: [
    'https://app.example.com',
    'https://admin.example.com',
  ],
  allowedPatterns: [
    /^https:\/\/.*\.vercel\.app$/,
    /^https:\/\/.*\.netlify\.app$/,
  ],
  allowSubdomains: [
    'example.com', // Allows *.example.com
  ],
};

export function isOriginAllowed(origin: string): boolean {
  // Check exact match
  if (config.allowedOrigins.includes(origin)) {
    return true;
  }

  // Check patterns
  for (const pattern of config.allowedPatterns) {
    if (pattern.test(origin)) {
      return true;
    }
  }

  // Check subdomains
  for (const domain of config.allowSubdomains) {
    if (origin.endsWith(`.${domain}`) || origin === `https://${domain}`) {
      return true;
    }
  }

  return false;
}

// Usage in middleware
app.use((req, res, next) => {
  const origin = req.headers.origin;

  if (origin && isOriginAllowed(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
    res.setHeader('Vary', 'Origin');
  }

  next();
});

Credentials and Cookies
// Important: When using credentials
// 1. Cannot use Access-Control-Allow-Origin: *
// 2. Must specify exact origin
// 3. Must set Access-Control-Allow-Credentials: true

// Server
app.use(cors({
  origin: 'https://app.example.com', // Must be exact, not *
  credentials: true,
}));

// Client (fetch)
fetch('https://api.example.com/data', {
  credentials: 'include', // Required for cookies
  headers: {
    'Content-Type': 'application/json',
  },
});

// Client (axios)
axios.defaults.withCredentials = true;

Security Headers Companion
// middleware/security.ts
import helmet from 'helmet';
import { Express } from 'express';

export function configureSecurityHeaders(app: Express) {
  app.use(helmet({
    crossOriginResourcePolicy: { policy: 'cross-origin' },
    crossOriginOpenerPolicy: { policy: 'same-origin-allow-popups' },
    crossOriginEmbedderPolicy: false, // May conflict with third-party resources
  }));

  // Additional headers
  app.use((req, res, next) => {
    // Prevent clickjacking
    res.setHeader('X-Frame-Options', 'SAMEORIGIN');

    // Prevent MIME sniffing
    res.setHeader('X-Content-Type-Options', 'nosniff');

    // XSS protection
    res.setHeader('X-XSS-Protection', '1; mode=block');

    // Referrer policy
    res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');

    next();
  });
}

Testing CORS
// tests/cors.test.ts
import request from 'supertest';
import { app } from '../src/app';

describe('CORS', () => {
  it('allows requests from allowed origins', async () => {
    const response = await request(app)
      .get('/api/data')
      .set('Origin', 'https://app.example.com');

    expect(response.headers['access-control-allow-origin']).toBe('https://app.example.com');
  });

  it('blocks requests from disallowed origins', async () => {
    const response = await request(app)
      .get('/api/data')
      .set('Origin', 'https://evil.com');

    expect(response.headers['access-control-allow-origin']).toBeUndefined();
  });

  it('handles preflight requests', async () => {
    const response = await request(app)
      .options('/api/data')
      .set('Origin', 'https://app.example.com')
      .set('Access-Control-Request-Method', 'POST')
      .set('Access-Control-Request-Headers', 'Content-Type');

    expect(response.status).toBe(204);
    expect(response.headers['access-control-allow-methods']).toContain('POST');
  });

  it('includes credentials header when configured', async () => {
    const response = await request(app)
      .get('/api/data')
      .set('Origin', 'https://app.example.com');

    expect(response.headers['access-control-allow-credentials']).toBe('true');
  });
});

Common Patterns
// Pattern 1: Development vs Production
const corsOptions = {
  origin: process.env.NODE_ENV === 'production'
    ? ['https://app.example.com']
    : [/localhost/],
};

// Pattern 2: Environment-based configuration
const corsOptions = {
  origin: process.env.ALLOWED_ORIGINS?.split(',') || [],
};

// Pattern 3: Wildcard subdomain
const corsOptions = {
  origin: (origin, callback) => {
    if (!origin || /\.example\.com$/.test(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed'));
    }
  },
};

Best Practices
Never use * with credentials: Use specific origins
Validate dynamically: Check origins at runtime
Use Vary: Origin: For caching correctness
Limit methods: Only allow necessary HTTP methods
Limit headers: Only expose necessary headers
Set Max-Age: Cache preflight responses
Log blocked requests: Monitor for issues
Test thoroughly: Cover all scenarios
Output Checklist

Every CORS configuration should include:

 Specific allowed origins (not wildcard with credentials)
 Proper preflight handling (OPTIONS)
 Credentials configuration
 Allowed methods specification
 Allowed headers list
 Exposed headers configuration
 Max-Age for preflight caching
 Vary: Origin header
 Development origin handling
 Error handling for blocked requests
Weekly Installs
109
Repository
patricio0312rev/skills
GitHub Stars
35
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass