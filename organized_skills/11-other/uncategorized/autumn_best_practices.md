---
rating: ⭐⭐⭐
title: autumn-best-practices
url: https://skills.sh/useautumn/skills/autumn-best-practices
---

# autumn-best-practices

skills/useautumn/skills/autumn-best-practices
autumn-best-practices
Installation
$ npx skills add https://github.com/useautumn/skills --skill autumn-best-practices
SKILL.md
Autumn Integration Guide

Always consult docs.useautumn.com for code examples and latest API.

Autumn is a TypeScript-first billing SDK supporting subscriptions, usage-based pricing, credits, trials, and more via Stripe.

Quick Reference
Environment Variables
AUTUMN_SECRET_KEY - API key (required). Get one at app.useautumn.com
Installation
npm install autumn-js    # Node.js
pip install autumn-py    # Python

Core Methods
Method	Purpose
customers.create	Create or get customer (idempotent)
checkout	Get Stripe URL or payment preview
attach	Confirm purchase (card on file)
cancel	Cancel subscription
check	Verify feature access
track	Record usage
products.list	Get products with billing scenarios
Core Config Options
Option	Notes
secretKey	Required. From env AUTUMN_SECRET_KEY
baseURL	Optional. Defaults to https://api.useautumn.com
Billing Patterns
Check → Work → Track

Always follow this order for protected actions:

const { data } = await autumn.check({ customer_id, feature_id: "api_calls" });
if (!data.allowed) return { error: "Limit reached" };

const result = await doWork();

await autumn.track({ customer_id, feature_id: "api_calls", value: 1 });
return result;

Two-Step Checkout
const { data } = await autumn.checkout({ customer_id, product_id: "pro" });

if (data.url) return redirect(data.url);  // New customer → Stripe

// Returning customer → show confirmation, then:
await autumn.attach({ customer_id, product_id: "pro" });

Product Scenarios

Use products.list to get scenarios. Don't build custom logic.

Scenario	Meaning
new	Not subscribed
active	Currently on plan
scheduled	Scheduled for future
upgrade	Higher tier available
downgrade	Lower tier available
renew	Cancelled, can reactivate
Feature Types
Type	Behavior
boolean	Access granted or denied
metered	Usage tracked against limit
credit_system	Pool for multiple features
React Hooks
Hook	Purpose
useCustomer	Get customer, checkout, attach, check
usePricingTable	Get products with scenarios
import { AutumnProvider } from "autumn-js/react";

<AutumnProvider>{children}</AutumnProvider>

Handler Imports
Framework	Import
Next.js	autumn-js/next
React Router	autumn-js/react-router
Hono	autumn-js/hono
Express	autumn-js/express
Fastify	autumn-js/fastify
Generic	autumn-js/backend
Common Gotchas
URL field - Checkout URL is data.url, not data.checkout_url
Frontend checks - For UX only. Always enforce on backend
Track after success - Only track usage after work completes
Credit systems - Track metered features, not the credit system itself
Cancel via free plan - Prefer attach({ product_id: "free" }) over cancel()
Idempotent creation - customers.create returns existing customer if ID exists
Resources
Docs
API Reference
LLMs.txt
GitHub
Weekly Installs
61
Repository
useautumn/skills
GitHub Stars
1
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn