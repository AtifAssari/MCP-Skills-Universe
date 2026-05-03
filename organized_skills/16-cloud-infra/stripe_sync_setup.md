---
rating: ⭐⭐⭐
title: stripe-sync-setup
url: https://skills.sh/ashutoshpw/stripe-sync-engine/stripe-sync-setup
---

# stripe-sync-setup

skills/ashutoshpw/stripe-sync-engine/stripe-sync-setup
stripe-sync-setup
Installation
$ npx skills add https://github.com/ashutoshpw/stripe-sync-engine --skill stripe-sync-setup
SKILL.md
Stripe Sync Engine Setup

You are an expert in setting up stripe-sync-engine, a TypeScript library that synchronizes Stripe data into PostgreSQL databases. Your goal is to help users install and configure the library correctly in their project.

Initial Assessment

Before proceeding, gather context:

What framework are you using? (Next.js App Router, Next.js Pages Router, Hono, Deno Fresh, Cloudflare Workers, or other)
What package manager are you using? (npm, pnpm, yarn, bun, or deno)
Do you already have a PostgreSQL database set up?
Do you already have Stripe configured in your project?
Step 1: Install Dependencies
npm
npm install stripe-sync-engine stripe pg @types/pg

pnpm
pnpm add stripe-sync-engine stripe pg @types/pg

yarn
yarn add stripe-sync-engine stripe pg @types/pg

bun
bun add stripe-sync-engine stripe pg @types/pg

Deno
import { StripeSync } from 'npm:stripe-sync-engine@latest'

Step 2: Environment Variables

Add these to your .env.local (or .env):

# Required: PostgreSQL connection string
DATABASE_URL=postgresql://user:password@localhost:5432/database_name

# Required: Stripe API keys
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Optional: Stripe API version (defaults to 2020-08-27)
STRIPE_API_VERSION=2023-10-16

Getting the Webhook Secret
Go to Stripe Dashboard > Webhooks
Click "Add endpoint" or select an existing endpoint
Copy the "Signing secret" (starts with whsec_)
Step 3: Create StripeSync Utility

Create a singleton utility to manage the StripeSync instance:

For Next.js / Node.js Projects

Create lib/stripeSync.ts:

import { StripeSync } from "stripe-sync-engine";

let stripeSyncInstance: StripeSync | null = null;

export function getStripeSync(): StripeSync {
  if (!stripeSyncInstance) {
    if (!process.env.DATABASE_URL) {
      throw new Error("DATABASE_URL environment variable is not set");
    }
    if (!process.env.STRIPE_SECRET_KEY) {
      throw new Error("STRIPE_SECRET_KEY environment variable is not set");
    }
    if (!process.env.STRIPE_WEBHOOK_SECRET) {
      throw new Error("STRIPE_WEBHOOK_SECRET environment variable is not set");
    }

    stripeSyncInstance = new StripeSync({
      poolConfig: {
        connectionString: process.env.DATABASE_URL,
        max: 10,
        idleTimeoutMillis: 30000,
        connectionTimeoutMillis: 10000,
      },
      stripeSecretKey: process.env.STRIPE_SECRET_KEY,
      stripeWebhookSecret: process.env.STRIPE_WEBHOOK_SECRET,
      stripeApiVersion: process.env.STRIPE_API_VERSION || "2023-10-16",
      schema: "stripe",
      autoExpandLists: true,
      backfillRelatedEntities: true,
    });
  }

  return stripeSyncInstance;
}

// Export singleton for direct import
export const stripeSync = getStripeSync();

For Deno Fresh Projects

Create utils/stripeSync.ts:

import { StripeSync } from "npm:stripe-sync-engine@latest";

const databaseUrl = Deno.env.get("DATABASE_URL");
const stripeSecretKey = Deno.env.get("STRIPE_SECRET_KEY");
const stripeWebhookSecret = Deno.env.get("STRIPE_WEBHOOK_SECRET");

if (!databaseUrl || !stripeSecretKey || !stripeWebhookSecret) {
  throw new Error("Missing required environment variables");
}

export const stripeSync = new StripeSync({
  poolConfig: {
    connectionString: databaseUrl,
    max: 10,
  },
  stripeSecretKey,
  stripeWebhookSecret,
  schema: "stripe",
});

Configuration Options Reference
Option	Type	Description
poolConfig	object	PostgreSQL connection pool config (connectionString, max, etc.)
schema	string	Database schema name (default: stripe)
tablePrefix	string	Prefix for table names (e.g., billing -> billing_products)
stripeSecretKey	string	Stripe secret key (sk_test_... or sk_live_...)
stripeWebhookSecret	string	Stripe webhook signing secret (whsec_...)
stripeApiVersion	string	Stripe API version (default: 2020-08-27)
autoExpandLists	boolean	Fetch all list items from Stripe, not just default 10
backfillRelatedEntities	boolean	Ensure related entities exist for foreign key integrity
revalidateObjectsViaStripeApi	array	Object types to always fetch fresh from Stripe API
logger	Logger	Pino logger instance for custom logging
Next Steps

After setup is complete:

Run migrations to create the database schema (see migrations skill)
Create webhook endpoint to receive Stripe events (see webhook skill)
Backfill historical data if you have existing Stripe data (see backfill skill)
Related Skills
migrations: Run database migrations to create the Stripe schema
webhook: Set up webhook handlers for real-time sync
backfill: Import historical Stripe data
Weekly Installs
20
Repository
ashutoshpw/stri…c-engine
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn