---
rating: ⭐⭐⭐
title: abacatepay
url: https://skills.sh/andrehfp/tinyplate/abacatepay
---

# abacatepay

skills/andrehfp/tinyplate/abacatepay
abacatepay
Installation
$ npx skills add https://github.com/andrehfp/tinyplate --skill abacatepay
SKILL.md
AbacatePay Integration Helper

Assist with AbacatePay payment gateway integration for Brazilian SaaS applications.

Quick Reference
Installation
bun add abacatepay-nodejs-sdk

Environment Variables
ABACATEPAY_API_KEY="abp_live_..."      # API key from dashboard
ABACATEPAY_WEBHOOK_SECRET="whsec_..."  # Webhook secret
NEXT_PUBLIC_APP_URL="https://..."      # For callback URLs

SDK Initialization
import AbacatePay from "abacatepay-nodejs-sdk";
const abacate = AbacatePay(process.env.ABACATEPAY_API_KEY!);

Common Tasks
1. Create a PIX Payment
const response = await abacate.billing.create({
  frequency: "ONE_TIME",
  methods: ["PIX"],
  products: [{
    externalId: "plan-pro",
    name: "Plano Pro",
    quantity: 1,
    price: 2990, // R$ 29,90 in centavos
  }],
  customer: {
    email: "user@example.com",
    name: "João Silva",
  },
  returnUrl: "https://app.com/pricing",
  completionUrl: "https://app.com/billing/success",
});

// response.data: { id, url, status, amount }

2. Create PIX QR Code (Direct)
const response = await abacate.pixQrCode.create({
  amount: 2990, // R$ 29,90
  expiresIn: 3600, // 1 hour
  description: "Payment description",
});

// response.data: { id, brCode, brCodeBase64, status, expiresAt }

3. Check Payment Status
const response = await abacate.pixQrCode.check({ id: "pix_abc123" });
// response.data.status: "PENDING" | "PAID" | "EXPIRED" | "CANCELLED"

4. Simulate Payment (Dev Mode)
await abacate.pixQrCode.simulatePayment({ id: "pix_abc123" });

Webhook Handling
Signature Verification (HMAC-SHA256)
import crypto from "crypto";

function validateSignature(payload: string, signature: string, secret: string): boolean {
  const expected = crypto
    .createHmac("sha256", secret)
    .update(payload)
    .digest("hex");
  return crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(expected));
}

Webhook Events
Event	Description
billing.paid	Payment confirmed via PIX
withdraw.done	Withdrawal completed
withdraw.failed	Withdrawal failed
Webhook Payload Structure
interface WebhookPayload {
  id: string;              // Event ID (use for idempotency)
  event: string;           // Event type
  devMode: boolean;        // True if test environment
  data: {
    billing?: {
      id: string;
      amount: number;
      status: string;
    };
  };
}

Pricing
Method	Fee
PIX	R$ 0,80 flat per transaction
Credit Card	3.5% + R$ 0,60
Withdrawal	R$ 0,80 (up to 20/month)
Database Schema Overview
Plans Table
id: Plan identifier (e.g., "pro-monthly")
priceInCents: Price in centavos (R$ 29,90 = 2990)
interval: "monthly" | "yearly" | "lifetime"
limits: JSONB with feature limits
features: JSONB array of display features
Subscriptions Table
userId: One subscription per user (unique)
planId: Current plan
status: "active" | "cancelled" | "expired"
currentPeriodStart/End: Subscription validity
Payments Table
abacateBillingId: AbacatePay billing ID
status: "pending" | "paid" | "expired"
paidAt: Payment confirmation timestamp
Common Patterns

See references/integration-patterns.md for:

Subscription management
Idempotent webhook handling
Feature gating
Error handling
API Reference

See references/api-reference.md for complete endpoint documentation.

Testing Checklist
 Environment variables configured
 SDK connects successfully
 Checkout creates billing and returns URL
 Webhook receives events (use AbacatePay dashboard)
 Payment status updates correctly
 Subscription created after payment
 Idempotency prevents duplicates
Weekly Installs
39
Repository
andrehfp/tinyplate
GitHub Stars
73
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn