---
title: expo-api-routes
url: https://skills.sh/expo/skills/expo-api-routes
---

# expo-api-routes

skills/expo/skills/expo-api-routes
expo-api-routes
Installation
$ npx skills add https://github.com/expo/skills --skill expo-api-routes
Summary

API routes in Expo Router for server-side logic, secrets, and third-party integrations on EAS Hosting.

Create routes with +api.ts suffix in the app directory; export named functions for HTTP methods (GET, POST, PUT, DELETE)
Handle query parameters, headers, JSON bodies, and dynamic route segments; add CORS headers for web clients
Access server-side secrets via process.env; set variables locally in .env or via eas env:create for production
Deploy to EAS Hosting (Cloudflare Workers) with eas deploy; use cloud databases (Turso, Supabase, PlanetScale) since filesystem and Node.js modules are unavailable
Test locally with npx expo serve and curl; call routes from client with standard fetch to relative paths like /api/hello
SKILL.md
When to Use API Routes

Use API routes when you need:

Server-side secrets — API keys, database credentials, or tokens that must never reach the client
Database operations — Direct database queries that shouldn't be exposed
Third-party API proxies — Hide API keys when calling external services (OpenAI, Stripe, etc.)
Server-side validation — Validate data before database writes
Webhook endpoints — Receive callbacks from services like Stripe or GitHub
Rate limiting — Control access at the server level
Heavy computation — Offload processing that would be slow on mobile
When NOT to Use API Routes

Avoid API routes when:

Data is already public — Use direct fetch to public APIs instead
No secrets required — Static data or client-safe operations
Real-time updates needed — Use WebSockets or services like Supabase Realtime
Simple CRUD — Consider Firebase, Supabase, or Convex for managed backends
File uploads — Use direct-to-storage uploads (S3 presigned URLs, Cloudflare R2)
Authentication only — Use Clerk, Auth0, or Firebase Auth instead
File Structure

API routes live in the app directory with +api.ts suffix:

app/
  api/
    hello+api.ts          → GET /api/hello
    users+api.ts          → /api/users
    users/[id]+api.ts     → /api/users/:id
  (tabs)/
    index.tsx

Basic API Route
// app/api/hello+api.ts
export function GET(request: Request) {
  return Response.json({ message: "Hello from Expo!" });
}

HTTP Methods

Export named functions for each HTTP method:

// app/api/items+api.ts
export function GET(request: Request) {
  return Response.json({ items: [] });
}

export async function POST(request: Request) {
  const body = await request.json();
  return Response.json({ created: body }, { status: 201 });
}

export async function PUT(request: Request) {
  const body = await request.json();
  return Response.json({ updated: body });
}

export async function DELETE(request: Request) {
  return new Response(null, { status: 204 });
}

Dynamic Routes
// app/api/users/[id]+api.ts
export function GET(request: Request, { id }: { id: string }) {
  return Response.json({ userId: id });
}

Request Handling
Query Parameters
export function GET(request: Request) {
  const url = new URL(request.url);
  const page = url.searchParams.get("page") ?? "1";
  const limit = url.searchParams.get("limit") ?? "10";

  return Response.json({ page, limit });
}

Headers
export function GET(request: Request) {
  const auth = request.headers.get("Authorization");

  if (!auth) {
    return Response.json({ error: "Unauthorized" }, { status: 401 });
  }

  return Response.json({ authenticated: true });
}

JSON Body
export async function POST(request: Request) {
  const { email, password } = await request.json();

  if (!email || !password) {
    return Response.json({ error: "Missing fields" }, { status: 400 });
  }

  return Response.json({ success: true });
}

Environment Variables

Use process.env for server-side secrets:

// app/api/ai+api.ts
export async function POST(request: Request) {
  const { prompt } = await request.json();

  const response = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
    },
    body: JSON.stringify({
      model: "gpt-4",
      messages: [{ role: "user", content: prompt }],
    }),
  });

  const data = await response.json();
  return Response.json(data);
}


Set environment variables:

Local: Create .env file (never commit)
EAS Hosting: Use eas env:create or Expo dashboard
CORS Headers

Add CORS for web clients:

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
};

export function OPTIONS() {
  return new Response(null, { headers: corsHeaders });
}

export function GET() {
  return Response.json({ data: "value" }, { headers: corsHeaders });
}

Error Handling
export async function POST(request: Request) {
  try {
    const body = await request.json();
    // Process...
    return Response.json({ success: true });
  } catch (error) {
    console.error("API error:", error);
    return Response.json({ error: "Internal server error" }, { status: 500 });
  }
}

Testing Locally

Start the development server with API routes:

npx expo serve


This starts a local server at http://localhost:8081 with full API route support.

Test with curl:

curl http://localhost:8081/api/hello
curl -X POST http://localhost:8081/api/users -H "Content-Type: application/json" -d '{"name":"Test"}'

Deployment to EAS Hosting
Prerequisites
npm install -g eas-cli
eas login

Deploy
eas deploy


This builds and deploys your API routes to EAS Hosting (Cloudflare Workers).

Environment Variables for Production
# Create a secret
eas env:create --name OPENAI_API_KEY --value sk-xxx --environment production

# Or use the Expo dashboard

Custom Domain

Configure in eas.json or Expo dashboard.

EAS Hosting Runtime (Cloudflare Workers)

API routes run on Cloudflare Workers. Key limitations:

Missing/Limited APIs
No Node.js filesystem — fs module unavailable
No native Node modules — Use Web APIs or polyfills
Limited execution time — 30 second timeout for CPU-intensive tasks
No persistent connections — WebSockets require Durable Objects
fetch is available — Use standard fetch for HTTP requests
Use Web APIs Instead
// Use Web Crypto instead of Node crypto
const hash = await crypto.subtle.digest(
  "SHA-256",
  new TextEncoder().encode("data")
);

// Use fetch instead of node-fetch
const response = await fetch("https://api.example.com");

// Use Response/Request (already available)
return new Response(JSON.stringify(data), {
  headers: { "Content-Type": "application/json" },
});

Database Options

Since filesystem is unavailable, use cloud databases:

Cloudflare D1 — SQLite at the edge
Turso — Distributed SQLite
PlanetScale — Serverless MySQL
Supabase — Postgres with REST API
Neon — Serverless Postgres

Example with Turso:

// app/api/users+api.ts
import { createClient } from "@libsql/client/web";

const db = createClient({
  url: process.env.TURSO_URL!,
  authToken: process.env.TURSO_AUTH_TOKEN!,
});

export async function GET() {
  const result = await db.execute("SELECT * FROM users");
  return Response.json(result.rows);
}

Calling API Routes from Client
// From React Native components
const response = await fetch("/api/hello");
const data = await response.json();

// With body
const response = await fetch("/api/users", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ name: "John" }),
});

Common Patterns
Authentication Middleware
// utils/auth.ts
export async function requireAuth(request: Request) {
  const token = request.headers.get("Authorization")?.replace("Bearer ", "");

  if (!token) {
    throw new Response(JSON.stringify({ error: "Unauthorized" }), {
      status: 401,
      headers: { "Content-Type": "application/json" },
    });
  }

  // Verify token...
  return { userId: "123" };
}

// app/api/protected+api.ts
import { requireAuth } from "../../utils/auth";

export async function GET(request: Request) {
  const { userId } = await requireAuth(request);
  return Response.json({ userId });
}

Proxy External API
// app/api/weather+api.ts
export async function GET(request: Request) {
  const url = new URL(request.url);
  const city = url.searchParams.get("city");

  const response = await fetch(
    `https://api.weather.com/v1/current?city=${city}&key=${process.env.WEATHER_API_KEY}`
  );

  return Response.json(await response.json());
}

Rules
NEVER expose API keys or secrets in client code
ALWAYS validate and sanitize user input
Use proper HTTP status codes (200, 201, 400, 401, 404, 500)
Handle errors gracefully with try/catch
Keep API routes focused — one responsibility per endpoint
Use TypeScript for type safety
Log errors server-side for debugging
Weekly Installs
21.3K
Repository
expo/skills
GitHub Stars
1.8K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn