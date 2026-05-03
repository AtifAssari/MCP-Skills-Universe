---
rating: ⭐⭐⭐
title: polar-better-auth
url: https://skills.sh/tuzzy08/skills/polar-better-auth
---

# polar-better-auth

skills/tuzzy08/skills/polar-better-auth
polar-better-auth
Installation
$ npx skills add https://github.com/tuzzy08/skills --skill polar-better-auth
SKILL.md
Polar + Better Auth Integration

A Better Auth plugin for integrating Polar payments and subscriptions into your authentication flow.

Note: Fetch complete documentation index at: https://polar.sh/docs/llms.txt

Features
Automatic Customer Creation: Syncs signup users to Polar customers.
Sync Deletion: Deletes Polar customer when user is deleted.
Reference System: Associates purchases with organizations/users.
Plugins: Checkout, Usage (Billing), Webhooks, and Customer Portal.
Installation
npm install better-auth @polar-sh/better-auth @polar-sh/sdk
# or
yarn add better-auth @polar-sh/better-auth @polar-sh/sdk
# or
pnpm add better-auth @polar-sh/better-auth @polar-sh/sdk

Server Configuration

Initialize the Polar client and add the plugin to your Better Auth configuration.

Environment Variables
POLAR_ACCESS_TOKEN=polar_oat_...
POLAR_WEBHOOK_SECRET=...

Full Server Setup
import { betterAuth } from "better-auth";
import {
  polar,
  checkout,
  portal,
  usage,
  webhooks,
} from "@polar-sh/better-auth";
import { Polar } from "@polar-sh/sdk";

const polarClient = new Polar({
  accessToken: process.env.POLAR_ACCESS_TOKEN,
  server: "sandbox", // Use 'sandbox' for testing, defaults to 'production'
});

const auth = betterAuth({
  plugins: [
    polar({
      client: polarClient,
      createCustomerOnSignUp: true, // Auto-create Polar customer
      // Optional: Custom metadata for new customers
      getCustomerCreateParams: ({ user }, request) => ({
        metadata: { source: "better-auth" },
      }),
      use: [
        // 1. Checkout Plugin
        checkout({
          products: [{ productId: "prod_123", slug: "pro" }],
          successUrl: "/success?checkout_id={CHECKOUT_ID}",
          authenticatedUsersOnly: true,
          returnUrl: "https://myapp.com",
          theme: "dark", // 'light' or 'dark'
        }),

        // 2. Customer Portal Plugin
        portal({
          returnUrl: "https://myapp.com",
        }),

        // 3. Usage Billing Plugin
        usage(),

        // 4. Webhooks Plugin
        webhooks({
          secret: process.env.POLAR_WEBHOOK_SECRET,
          onOrderPaid: (payload) => console.log("💸 Order Paid:", payload),
          onCustomerStateChanged: (payload) =>
            console.log("👤 State Changed:", payload),
          onPayload: (payload) => console.log("📨 Other Event:", payload),
        }),
      ],
    }),
  ],
});

Server Options Dictionary
Option	Type	Description
client	Polar	Required. The Polar SDK instance.
createCustomerOnSignUp	boolean	Auto-create Polar customer on signup.
use	Plugin[]	Array of sub-plugins (checkout, portal, usage, webhooks).
getCustomerCreateParams	Function	Returns metadata/params for interaction.
Client Configuration
import { createAuthClient } from "better-auth/react";
import { polarClient } from "@polar-sh/better-auth";

export const authClient = createAuthClient({
  plugins: [polarClient()],
});

Plugins Summary
1. Checkout Plugin

Enables creating checkout sessions directly from the client.

Configuration:

products: Array of { productId, slug }. Allows referencing products by slug.
successUrl: Redirect URL after payment. Supports {CHECKOUT_ID}.
authenticatedUsersOnly: true forces user login before checkout.
returnUrl: Back button URL in checkout.
theme: light or dark.

Client Usage:

await authClient.checkout({
  // Option A: Use slug defined in config
  slug: "pro",
  // Option B: Use direct Product ID
  products: ["prod_123"],
  // Optional: Link to an Organization (B2B)
  referenceId: "org_123",
});

2. Usage Plugin (Billing)

Handles Event Ingestion and Meter retrieval for Usage-Based Billing.

Client Usage:

A. Ingest Events:

await authClient.usage.ingestion({
  event: "ai_generation", // Must match Meter definition in Dashboard
  metadata: {
    tokens: 156,
    model: "gpt-4",
  },
});


Note: Automatically links event to the authenticated user.

B. List Meters:

const { data: meters } = await authClient.usage.meters.list({
  query: { page: 1, limit: 10 },
});
// Returns: consumed units, credited units, current balance

3. Portal Plugin

Manages customer access to the hosted Customer Portal.

Client Usage:

A. Open Portal:

// Redirects user to Polar Customer Portal
await authClient.customer.portal();


B. Get Customer State: Returns active subscriptions, granted benefits, and meter balances.

const { data: state } = await authClient.customer.state();


C. List Resources:

// List Active Subscriptions
const { data: subs } = await authClient.customer.subscriptions.list({
  query: { active: true },
});

// List Orders (Purchases)
const { data: orders } = await authClient.customer.orders.list();

// List Benefits
const { data: benefits } = await authClient.customer.benefits.list();

4. Webhooks Plugin

The webhooks plugin captures incoming events from your Polar organization.

Setup Steps:

Configure Endpoint: Go to Polar Dashboard > Webhooks and set endpoint to /api/auth/polar/webhooks.
Set Secret: Add POLAR_WEBHOOK_SECRET to your environment variables.
Add Plugin:
import { polar, webhooks } from "@polar-sh/better-auth";

const auth = betterAuth({
  plugins: [
    polar({
      client: polarClient,
      use: [
        webhooks({
          secret: process.env.POLAR_WEBHOOK_SECRET,
          // Handlers
          onCustomerStateChanged: (payload) => {
            console.log("Customer state changed:", payload);
          },
          onOrderPaid: (payload) => {
            console.log("Order paid:", payload);
          },
          // ... over 25+ handlers available
          onPayload: (payload) => {
            console.log("Catch-all event:", payload);
          },
        }),
      ],
    }),
  ],
});


Supported Events:

onPayload (Catch-all)
onCheckoutCreated, onCheckoutUpdated
onOrderCreated, onOrderPaid, onOrderRefunded
onRefundCreated, onRefundUpdated
onSubscriptionCreated, onSubscriptionUpdated
onSubscriptionActive, onSubscriptionCanceled, onSubscriptionRevoked
onProductCreated, onProductUpdated
onCustomerCreated, onCustomerUpdated, onCustomerDeleted, onCustomerStateChanged
onBenefitCreated, onBenefitGrantCreated, onBenefitGrantRevoked
Common Workflows
Sync Customer Deletion

To delete the Polar customer when a user is deleted in your database:

const auth = betterAuth({
  user: {
    deleteUser: {
      enabled: true,
      afterDelete: async (user) => {
        await polarClient.customers.deleteExternal({
          externalId: user.id,
        });
      },
    },
  },
});

Check Organization Access

Check if a user has access via an Organization subscription (B2B):

const orgId = (await authClient.organization.list())?.data?.[0]?.id;

const { data: orders } = await authClient.customer.orders.list({
  query: {
    active: true,
    referenceId: orgId, // Filter by Org ID
  },
});

const hasAccess = orders.length > 0;

Weekly Installs
60
Repository
tuzzy08/skills
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn