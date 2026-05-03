---
rating: ⭐⭐⭐
title: stripe-sync-troubleshooting
url: https://skills.sh/ashutoshpw/stripe-sync-engine/stripe-sync-troubleshooting
---

# stripe-sync-troubleshooting

skills/ashutoshpw/stripe-sync-engine/stripe-sync-troubleshooting
stripe-sync-troubleshooting
Installation
$ npx skills add https://github.com/ashutoshpw/stripe-sync-engine --skill stripe-sync-troubleshooting
SKILL.md
Stripe Sync Engine Troubleshooting

You are an expert in debugging stripe-sync-engine issues. Your goal is to help users diagnose and fix common problems with their Stripe sync setup.

Initial Diagnosis

Ask the user:

What error message are you seeing? (exact text helps)
At what step does it fail? (migrations, webhooks, backfill, queries)
Is this a new setup or did it work before?
What environment? (local, production, serverless)
Common Issues and Solutions
1. Webhook Signature Verification Failed

Error: Webhook signature verification failed or No signatures found matching the expected signature

Causes and Solutions:

Wrong Webhook Secret
# Check your environment variable
echo $STRIPE_WEBHOOK_SECRET

# Should start with whsec_
# For local development, use the secret from `stripe listen` output


Solution: Get the correct secret:

Production: Stripe Dashboard > Webhooks > Your Endpoint > Signing Secret
Local: Use the secret printed by stripe listen --forward-to localhost:3000/api/webhooks/stripe
Body Already Parsed

If using a framework that auto-parses JSON, the raw body is lost.

Next.js Pages Router Fix:

// pages/api/webhooks/stripe.ts
export const config = {
  api: {
    bodyParser: false,  // Critical! Disable body parsing
  },
};

import { buffer } from 'micro';

export default async function handler(req, res) {
  const payload = await buffer(req);  // Get raw body
  await stripeSync.processWebhook(payload, signature);
}


Next.js App Router Fix:

// Use arrayBuffer, not json()
const arrayBuffer = await request.arrayBuffer();
const payload = Buffer.from(arrayBuffer);

Using String Instead of Buffer
// Wrong
await stripeSync.processWebhook(JSON.stringify(body), sig);

// Correct
await stripeSync.processWebhook(rawPayload, sig);  // Buffer or string from req.text()

2. Database Connection Errors

Error: Connection terminated unexpectedly or ECONNREFUSED

Solutions:

Check Connection String
# Verify DATABASE_URL format
# postgresql://username:password@host:port/database

# Test connection
psql $DATABASE_URL -c "SELECT 1"

SSL Issues
// For remote databases requiring SSL
const stripeSync = new StripeSync({
  poolConfig: {
    connectionString: process.env.DATABASE_URL,
    ssl: {
      rejectUnauthorized: false,  // For self-signed certs
    },
  },
  // ...
});

Connection String Encoding

Special characters in password need URL encoding:

// If password contains @, encode it as %40
// p@ssword -> p%40ssword

3. Connection Pool Exhaustion

Error: Too many connections or remaining connection slots are reserved

Solutions:

Reduce Pool Size
const stripeSync = new StripeSync({
  poolConfig: {
    connectionString: process.env.DATABASE_URL,
    max: 5,  // Reduce from default 10
    idleTimeoutMillis: 10000,  // Close idle connections faster
  },
});

Serverless Connection Pooling

For serverless environments, use a connection pooler like:

Supabase: Use the pooler connection string
Neon: Enable pooling in dashboard
PgBouncer: Set up connection pooling
# Use pooled connection for serverless
DATABASE_URL=postgresql://user:pass@pooler.host:6543/db?pgbouncer=true

4. Data Not Syncing

Symptoms: Webhook returns success but data not in database

Diagnostic Steps:

1. Verify Schema Exists
SELECT schema_name FROM information_schema.schemata
WHERE schema_name = 'stripe';


If missing, run migrations:

npm run stripe:migrate

2. Check Tables Exist
SELECT table_name FROM information_schema.tables
WHERE table_schema = 'stripe';

3. Verify Webhook is Being Called

Add logging:

export async function POST(request: Request) {
  console.log("Webhook received");
  const payload = await request.arrayBuffer();
  console.log("Payload size:", payload.byteLength);

  await stripeSync.processWebhook(Buffer.from(payload), signature);
  console.log("Sync completed");
}

4. Check Stripe Dashboard

Go to Webhooks > Your Endpoint > Recent Deliveries to see:

Was the event sent?
What was the response?
Any errors?
5. Migration Errors

Error: permission denied for schema stripe

Solution:

-- Grant permissions
GRANT CREATE ON DATABASE your_database TO your_user;
GRANT ALL ON SCHEMA stripe TO your_user;

-- Or create schema first
CREATE SCHEMA IF NOT EXISTS stripe;


Error: relation already exists

Solution: Migrations track state in stripe_migrations table. If corrupt:

-- Check migration state
SELECT * FROM stripe.stripe_migrations;

-- If needed, reset (careful!)
TRUNCATE stripe.stripe_migrations;

6. Serverless/Edge Runtime Issues

Error: Cannot use Node.js module in Edge Runtime

Cause: stripe-sync-engine requires Node.js runtime, not Edge.

Next.js Fix:

// app/api/webhooks/stripe/route.ts
export const runtime = 'nodejs';  // Force Node.js runtime


Cloudflare Workers: Use the forwarding pattern - Workers verify the signature, then forward to a Node.js service that runs stripe-sync-engine.

7. Environment Variable Issues

Symptoms: Works locally, fails in production

Diagnostic:

// Add to your API route temporarily
console.log("DATABASE_URL set:", !!process.env.DATABASE_URL);
console.log("STRIPE_SECRET_KEY set:", !!process.env.STRIPE_SECRET_KEY);
console.log("STRIPE_WEBHOOK_SECRET set:", !!process.env.STRIPE_WEBHOOK_SECRET);


Common Issues:

Variable not set in hosting platform
Variable has wrong name (case-sensitive)
Variable has extra whitespace
Using .env.local but platform expects .env
8. Type Errors

Error: TypeScript errors after installation

Solution:

# Ensure types are installed
npm install -D @types/pg

# If using strict mode, add to tsconfig.json
{
  "compilerOptions": {
    "skipLibCheck": true
  }
}

Debug Mode

Enable verbose logging:

import pino from "pino";

const logger = pino({
  level: "debug",
  transport: {
    target: "pino-pretty",
  },
});

const stripeSync = new StripeSync({
  // ... other config
  logger: logger,
});

Health Check Endpoint

Create a diagnostic endpoint:

// app/api/health/stripe/route.ts
import { NextResponse } from "next/server";
import { stripeSync } from "@/lib/stripeSync";

export async function GET() {
  const checks = {
    env: {
      DATABASE_URL: !!process.env.DATABASE_URL,
      STRIPE_SECRET_KEY: !!process.env.STRIPE_SECRET_KEY,
      STRIPE_WEBHOOK_SECRET: !!process.env.STRIPE_WEBHOOK_SECRET,
    },
    database: false,
    schema: false,
  };

  try {
    // Test database connection
    const { Pool } = await import("pg");
    const pool = new Pool({ connectionString: process.env.DATABASE_URL });
    await pool.query("SELECT 1");
    checks.database = true;

    // Check schema exists
    const result = await pool.query(
      "SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'stripe'"
    );
    checks.schema = result.rows.length > 0;

    await pool.end();
  } catch (error) {
    // checks remain false
  }

  const healthy = Object.values(checks.env).every(Boolean) &&
                  checks.database &&
                  checks.schema;

  return NextResponse.json({ healthy, checks }, { status: healthy ? 200 : 500 });
}

Getting Help

If issues persist:

Check GitHub Issues
Include: error message, code snippet, environment details
Check Stripe Dashboard webhook logs
Related Skills
setup: Initial configuration
migrations: Database schema setup
webhook: Webhook handler implementation
Weekly Installs
17
Repository
ashutoshpw/stri…c-engine
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass