---
rating: ⭐⭐⭐
title: stripe-sync-minimal
url: https://skills.sh/ashutoshpw/stripe-sync-engine/stripe-sync-minimal
---

# stripe-sync-minimal

skills/ashutoshpw/stripe-sync-engine/stripe-sync-minimal
stripe-sync-minimal
Installation
$ npx skills add https://github.com/ashutoshpw/stripe-sync-engine --skill stripe-sync-minimal
SKILL.md
Stripe Sync Engine - Complete Guide

You are an expert in stripe-sync-engine. This skill covers setup, migrations, webhooks, backfill, and querying in one place.

1. Installation
npm install stripe-sync-engine stripe pg

2. Environment Variables
DATABASE_URL=postgresql://user:password@host:5432/database
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...

3. Create StripeSync Utility
// lib/stripeSync.ts
import { StripeSync } from "stripe-sync-engine";

export const stripeSync = new StripeSync({
  stripe: { apiKey: process.env.STRIPE_SECRET_KEY! },
  webhookSecret: process.env.STRIPE_WEBHOOK_SECRET!,
  databaseUrl: process.env.DATABASE_URL!,
});

4. Run Migrations
// scripts/run-migrations.ts
import { stripeSync } from "../lib/stripeSync";

async function main() {
  await stripeSync.runMigrations();
  console.log("Migrations complete");
  process.exit(0);
}
main();

npx tsx scripts/run-migrations.ts

5. Webhook Handler

Next.js App Router:

// app/api/webhooks/stripe/route.ts
import { NextResponse } from "next/server";
import { stripeSync } from "@/lib/stripeSync";

export async function POST(request: Request) {
  const signature = request.headers.get("stripe-signature") ?? undefined;
  const payload = Buffer.from(await request.arrayBuffer());

  await stripeSync.processWebhook(payload, signature);
  return NextResponse.json({ received: true });
}


Hono:

app.post("/webhooks/stripe", async (c) => {
  const signature = c.req.header("stripe-signature");
  const payload = await c.req.text();

  await stripeSync.processWebhook(payload, signature);
  return c.json({ received: true });
});

6. Backfill Historical Data
// Backfill all data types
await stripeSync.syncBackfill();

// Backfill specific types
await stripeSync.syncBackfill({
  objectTypes: ["customer", "subscription", "invoice"],
});

// Backfill with date range
await stripeSync.syncBackfill({
  created: { gte: Math.floor(Date.now() / 1000) - 30 * 24 * 60 * 60 },
});

// Sync single entity
await stripeSync.syncSingleEntity("cus_ABC123");

7. Query Synced Data

Tables available:

stripe.customers, stripe.products, stripe.prices
stripe.subscriptions, stripe.subscription_items
stripe.invoices, stripe.invoice_line_items
stripe.charges, stripe.payment_intents, stripe.payment_methods
stripe.coupons, stripe.disputes, stripe.setup_intents

Example queries:

-- Active subscriptions
SELECT c.email, s.status, p.name as product
FROM stripe.subscriptions s
JOIN stripe.customers c ON s.customer_id = c.id
JOIN stripe.prices pr ON s.items->0->>'price_id' = pr.id
JOIN stripe.products p ON pr.product_id = p.id
WHERE s.status = 'active';

-- Monthly revenue
SELECT DATE_TRUNC('month', created) as month,
       SUM(amount_paid) / 100.0 as revenue
FROM stripe.invoices
WHERE status = 'paid'
GROUP BY 1 ORDER BY 1;

8. Local Testing
# Terminal 1: Start your server
npm run dev

# Terminal 2: Forward Stripe events
stripe listen --forward-to localhost:3000/api/webhooks/stripe

# Terminal 3: Trigger test events
stripe trigger customer.created
stripe trigger invoice.payment_succeeded

Quick Troubleshooting
Issue	Solution
Signature failed	Use raw body (Buffer), not parsed JSON
Connection error	Check DATABASE_URL format and SSL settings
Data not syncing	Run migrations first, check schema exists
Edge runtime error	Add export const runtime = 'nodejs'
Weekly Installs
17
Repository
ashutoshpw/stri…c-engine
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn