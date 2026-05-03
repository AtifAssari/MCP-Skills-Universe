---
rating: ⭐⭐⭐
title: dodo-best-practices
url: https://skills.sh/dodopayments/skills/dodo-best-practices
---

# dodo-best-practices

skills/dodopayments/skills/dodo-best-practices
dodo-best-practices
Installation
$ npx skills add https://github.com/dodopayments/skills --skill dodo-best-practices
SKILL.md
Dodo Payments Integration Guide

Always consult docs.dodopayments.com for the latest API reference and code examples.

Dodo Payments is the all-in-one engine to launch, scale, and monetize worldwide. Designed for SaaS and AI products, it handles payments, billing, subscriptions, and distribution without extra engineering.

Quick Reference
Environment Variables
DODO_PAYMENTS_API_KEY - Your API key from the dashboard
DODO_PAYMENTS_WEBHOOK_SECRET - Webhook signing secret for verification
API Environments
Live Mode: https://api.dodopayments.com (default)
Test Mode: https://api.dodopayments.com with environment: 'test_mode'
Dashboard URLs
Main Dashboard: app.dodopayments.com
API Keys: Dashboard → Developer → API
Webhooks: Dashboard → Developer → Webhooks
Products: Dashboard → Products
SDK Installation
TypeScript/JavaScript
npm install dodopayments
# or
yarn add dodopayments
# or
pnpm add dodopayments

import DodoPayments from 'dodopayments';

const client = new DodoPayments({
  bearerToken: process.env.DODO_PAYMENTS_API_KEY,
  environment: 'live_mode', // or 'test_mode'
});

Python
pip install dodopayments

from dodopayments import DodoPayments

client = DodoPayments(bearer_token=os.environ["DODO_PAYMENTS_API_KEY"])

Go
go get github.com/dodopayments/dodopayments-go

import "github.com/dodopayments/dodopayments-go"

client := dodopayments.NewClient(
    option.WithBearerToken(os.Getenv("DODO_PAYMENTS_API_KEY")),
)

PHP
composer require dodopayments/client

use Dodopayments\Client;

$client = new Client(bearerToken: getenv('DODO_PAYMENTS_API_KEY'));

Core Concepts
Products

Products are the items you sell. Create them in the dashboard or via API:

One-time: Single purchase products
Subscription: Recurring billing products
Usage-based: Metered billing per consumption
Credit Entitlements

Credits are virtual balances (API calls, tokens, compute hours) attached to products. Create them in Dashboard → Products → Credits:

Custom Unit: Your own metric with configurable precision
Fiat Credits: Real currency value (USD, EUR, etc.)
Attach up to 3 credits per product
Configure rollover, overage, and expiration per entitlement
Checkout Sessions

The primary way to collect payments. Create a checkout session and redirect customers:

const session = await client.checkoutSessions.create({
  product_cart: [
    { product_id: 'prod_xxxxx', quantity: 1 }
  ],
  customer: {
    email: 'customer@example.com',
    name: 'John Doe',
  },
  return_url: 'https://yoursite.com/success',
});

// Redirect customer to: session.checkout_url

Webhooks

Listen to events for real-time updates:

payment.succeeded - Payment completed
payment.failed - Payment failed
subscription.active - Subscription activated
subscription.cancelled - Subscription cancelled
refund.succeeded - Refund processed
dispute.opened - Dispute received
license_key.created - License key generated
credit.added - Credits granted to customer
credit.deducted - Credits consumed
credit.balance_low - Credit balance below threshold
Common Integration Patterns
One-Time Payment Flow
Create product in dashboard
Create checkout session with product ID
Redirect customer to checkout URL
Handle payment.succeeded webhook
Fulfill order / grant access
// Create checkout for one-time payment
const session = await client.checkoutSessions.create({
  product_cart: [{ product_id: 'prod_one_time_product', quantity: 1 }],
  customer: { email: 'customer@example.com' },
  return_url: 'https://yoursite.com/success',
});

Subscription Flow
Create subscription product in dashboard
Create checkout session
Handle subscription.active webhook to grant access
Handle subscription.cancelled to revoke access
// Create checkout for subscription
const session = await client.checkoutSessions.create({
  product_cart: [{ product_id: 'prod_monthly_subscription', quantity: 1 }],
  subscription_data: { trial_period_days: 14 }, // Optional trial
  customer: { email: 'customer@example.com' },
  return_url: 'https://yoursite.com/success',
});

Webhook Verification

Always verify webhook signatures:

import crypto from 'crypto';

function verifyWebhook(payload: string, signature: string, secret: string): boolean {
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');
  
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}

API Key Management
Generation
Navigate to Dashboard → Developer → API
Click "Create API Key"
Copy and securely store the key
Security Best Practices
Never expose API keys in client-side code
Use environment variables
Rotate keys periodically
Use test mode keys for development
Customer Portal

Allow customers to manage their subscriptions:

const portal = await client.customers.createPortalSession({
  customer_id: 'cust_xxxxx',
  return_url: 'https://yoursite.com/account',
});

// Redirect to: portal.url

Error Handling

Handle API errors gracefully:

try {
  const session = await client.checkoutSessions.create({...});
} catch (error) {
  if (error.status === 400) {
    // Invalid request - check parameters
  } else if (error.status === 401) {
    // Invalid API key
  } else if (error.status === 429) {
    // Rate limited - implement backoff
  }
}

Testing
Test Mode
Use test API keys (start with sk_test_)
Test webhooks with dashboard tools
Use test card numbers:
4242 4242 4242 4242 - Success
4000 0000 0000 0002 - Decline
Local Development

Use ngrok or similar for webhook testing:

ngrok http 3000


Then configure the ngrok URL as your webhook endpoint in the dashboard.

Framework Integration
Next.js

Use API routes for server-side operations:

// app/api/checkout/route.ts
import { NextResponse } from 'next/server';
import DodoPayments from 'dodopayments';

const client = new DodoPayments({
  bearerToken: process.env.DODO_PAYMENTS_API_KEY!,
});

export async function POST(req: Request) {
  const { productId, email } = await req.json();
  
  const session = await client.checkoutSessions.create({
    product_cart: [{ product_id: productId, quantity: 1 }],
    customer: { email },
    return_url: `${process.env.NEXT_PUBLIC_URL}/success`,
  });

  return NextResponse.json({ url: session.checkout_url });
}

Express.js
import express from 'express';
import DodoPayments from 'dodopayments';

const app = express();
const client = new DodoPayments({ bearerToken: process.env.DODO_PAYMENTS_API_KEY! });

app.post('/create-checkout', async (req, res) => {
  const session = await client.checkoutSessions.create({
    product_cart: [{ product_id: req.body.productId, quantity: 1 }],
    customer: { email: req.body.email },
    return_url: 'https://yoursite.com/success',
  });
  res.json({ url: session.checkout_url });
});

Resources
Documentation
API Reference
SDK Repositories
Discord Community
Support
Credit-Based Billing
Weekly Installs
379
Repository
dodopayments/skills
GitHub Stars
8
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn