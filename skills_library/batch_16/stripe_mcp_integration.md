---
title: stripe mcp integration
url: https://skills.sh/wrsmith108/stripe-mcp-skill/stripe-mcp-integration
---

# stripe mcp integration

skills/wrsmith108/stripe-mcp-skill/Stripe MCP Integration
Stripe MCP Integration
Installation
$ npx skills add https://github.com/wrsmith108/stripe-mcp-skill --skill 'Stripe MCP Integration'
SKILL.md
Stripe MCP Integration

Connect Claude to Stripe's payment infrastructure via the Model Context Protocol (MCP). This skill enables direct interaction with Stripe APIs for customer management, subscriptions, invoices, and documentation search.

What This Skill Does
Customer Management: Create, retrieve, update, and list customers
Subscription Handling: Manage subscription lifecycles, billing cycles, and pricing
Invoice Operations: Create, finalize, send, and retrieve invoices
Product Catalog: Manage products and prices for your offerings
Documentation Search: Query Stripe's official docs directly
Quick Start

Choose your installation method:

Option 1: Remote HTTP (Recommended)

Add to ~/.claude/settings.json:

{
  "mcpServers": {
    "stripe": {
      "type": "http",
      "url": "https://mcp.stripe.com/v1/sse"
    }
  }
}


Authenticate when prompted with stripe_sk_... key.

Option 2: Local npm
# Install the MCP server
npm install -g @stripe/mcp

# Add to settings
claude mcp add stripe -- npx -y @stripe/mcp

Option 3: Project .mcp.json

Create .mcp.json in your project root:

{
  "mcpServers": {
    "stripe": {
      "command": "npx",
      "args": ["-y", "@stripe/mcp"],
      "env": {
        "STRIPE_SECRET_KEY": "${STRIPE_SECRET_KEY}"
      }
    }
  }
}

Available MCP Tools
Tool	Description	Example Usage
stripe_create_customer	Create a new customer	"Create customer with email user@example.com"
stripe_retrieve_customer	Get customer by ID	"Get customer cus_xxx"
stripe_list_customers	List all customers	"Show my Stripe customers"
stripe_create_product	Create a product	"Create product 'Pro Plan' for $29/month"
stripe_list_products	List products	"Show all products"
stripe_create_subscription	Start a subscription	"Subscribe customer to price_xxx"
stripe_cancel_subscription	Cancel subscription	"Cancel subscription sub_xxx"
stripe_create_invoice	Create draft invoice	"Create invoice for customer cus_xxx"
stripe_finalize_invoice	Finalize for payment	"Finalize invoice in_xxx"
stripe_search_documentation	Search Stripe docs	"Search Stripe docs for webhooks"
Stripe ID Prefixes

Use these prefixes to validate IDs in your code:

Object	Prefix	Example
Customer	cus_	cus_NffrFeUfNV2Hib
Subscription	sub_	sub_1MowQVLkdIwHu7ixeRlqHVzs
Price	price_	price_1MowQULkdIwHu7ixspc
Product	prod_	prod_NWjs8kKbJWmuuc
Invoice	in_	in_1MtHbELkdIwHu7ixl4OzzPMI
Payment Intent	pi_	pi_3MtwBwLkdIwHu7ix28a3tqPa
Event	evt_	evt_1NG8Du2eZvKYlo2CUI79vXWy
Webhook Endpoint	we_	we_1Mr5jALkdIwHu7ixNsD8AdJZ
Checkout Session	cs_	cs_test_a1b2c3d4
Test Mode Development
Test Cards
Card Number	Scenario
4242424242424242	Successful payment
4000000000000002	Card declined
4000002500003155	Requires 3D Secure
4000000000009995	Insufficient funds
4000000000000341	Attach fails
Stripe CLI Testing
# Install Stripe CLI
brew install stripe/stripe-cli/stripe

# Login to your account
stripe login

# Listen for webhooks locally
stripe listen --forward-to localhost:3000/api/webhooks/stripe

# Trigger test events
stripe trigger checkout.session.completed
stripe trigger customer.subscription.created
stripe trigger invoice.payment_succeeded

Environment Variables
Variable	Required	Description
STRIPE_SECRET_KEY	Yes	API key (sk_test_... or sk_live_...)
STRIPE_WEBHOOK_SECRET	For webhooks	Webhook signing secret (whsec_...)
STRIPE_API_VERSION	No	Lock API version (e.g., 2024-12-18.acacia)
Secure Key Storage

Never commit keys to version control. Use environment variables or a secrets manager:

# Development: Use .env file (gitignored)
echo "STRIPE_SECRET_KEY=sk_test_..." >> .env

# Production: Use your platform's secrets manager
# - Cloud platforms: Environment variables or secret managers
# - AWS: Secrets Manager or Parameter Store
# - Self-hosted: HashiCorp Vault or similar

Webhook Signature Verification
Node.js Pattern
import Stripe from 'stripe';

const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);

export async function handleWebhook(request: Request) {
  const body = await request.text();
  const signature = request.headers.get('stripe-signature')!;

  let event: Stripe.Event;

  try {
    event = stripe.webhooks.constructEvent(
      body,
      signature,
      process.env.STRIPE_WEBHOOK_SECRET!
    );
  } catch (err) {
    console.error('Webhook signature verification failed:', err);
    return new Response('Webhook Error', { status: 400 });
  }

  // Handle the event
  switch (event.type) {
    case 'checkout.session.completed':
      const session = event.data.object as Stripe.Checkout.Session;
      await fulfillOrder(session);
      break;
    case 'customer.subscription.updated':
      const subscription = event.data.object as Stripe.Subscription;
      await updateSubscriptionStatus(subscription);
      break;
    // ... handle other events
  }

  return new Response('OK', { status: 200 });
}

Deno/Edge Function Pattern
import Stripe from 'npm:stripe@latest';

const stripe = new Stripe(Deno.env.get('STRIPE_SECRET_KEY')!, {
  apiVersion: '2024-12-18.acacia',
});

Deno.serve(async (req) => {
  const body = await req.text();
  const signature = req.headers.get('stripe-signature')!;

  // IMPORTANT: Deno requires async verification
  const event = await stripe.webhooks.constructEventAsync(
    body,
    signature,
    Deno.env.get('STRIPE_WEBHOOK_SECRET')!
  );

  // Handle event...
  return new Response(JSON.stringify({ received: true }));
});


Critical: Deno and edge runtimes require constructEventAsync(), not constructEvent().

Common Webhook Events
Event	When It Fires	Typical Action
checkout.session.completed	Successful checkout	Grant access, send confirmation
customer.subscription.created	New subscription	Provision account, welcome email
customer.subscription.updated	Plan change, renewal	Update access level
customer.subscription.deleted	Cancellation	Revoke access, send offboarding
invoice.payment_succeeded	Successful charge	Update billing records
invoice.payment_failed	Failed charge	Notify customer, retry logic
Troubleshooting
"No such customer" Error
StripeInvalidRequestError: No such customer: 'cus_xxx'


Cause: Customer ID doesn't exist or using test ID in live mode. Fix: Verify the ID exists in your Stripe Dashboard. Check you're using matching test/live keys.

Webhook Signature Mismatch
Webhook signature verification failed


Cause: Wrong webhook secret or modified payload. Fix:

Get the correct secret from Stripe Dashboard → Webhooks → Signing secret
For local testing, use the secret printed by stripe listen
Ensure you're reading the raw body, not parsed JSON
Rate Limiting
StripeRateLimitError: Too many requests


Cause: Exceeding 100 read or 100 write requests per second. Fix: Implement exponential backoff, batch operations where possible, cache read results.

Sub-Documentation
Webhook Security Patterns - Secrets rotation, idempotency, retry handling
Testing Guide - Test cards, CLI workflows, E2E patterns
Resources
Stripe MCP Documentation
Stripe API Reference
Webhook Events Reference
Stripe CLI Documentation
Weekly Installs
–
Repository
wrsmith108/stri…cp-skill
GitHub Stars
1
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn