---
title: payment-integration
url: https://skills.sh/404kidwiz/claude-supercode-skills/payment-integration
---

# payment-integration

skills/404kidwiz/claude-supercode-skills/payment-integration
payment-integration
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill payment-integration
SKILL.md
Payment Integration
Purpose

Provides expertise in integrating payment gateways and designing PCI-compliant billing systems. Specializes in implementing checkout flows, subscription management, and payment processing with providers like Stripe, PayPal, and Adyen.

When to Use
Integrating Stripe, PayPal, or other payment gateways
Implementing checkout and payment flows
Building subscription billing systems
Ensuring PCI-DSS compliance
Handling payment webhooks
Implementing payment retry logic
Setting up multi-currency payments
Building invoicing systems
Quick Start

Invoke this skill when:

Integrating payment gateways (Stripe, PayPal, Adyen)
Building checkout or subscription flows
Designing PCI-compliant payment systems
Implementing webhook handlers for payments
Setting up recurring billing

Do NOT invoke when:

General ledger/accounting systems → use /fintech-engineer
API design without payment focus → use /api-designer
Frontend checkout UI only → use /frontend-design
Security audit → use /security-auditor
Decision Framework
Payment Use Case?
├── One-time Purchase
│   └── Stripe Checkout / PayPal Buttons
├── Subscription
│   └── Stripe Billing / Recurly
├── Marketplace/Split Payments
│   └── Stripe Connect / PayPal Commerce
├── Enterprise/B2B
│   └── Invoicing with NET terms
└── Global Payments
    └── Adyen / Multi-gateway strategy

Core Workflows
1. Stripe Integration
Set up Stripe account and API keys
Create products and prices
Implement Checkout Session or Elements
Handle payment confirmation
Set up webhook endpoint
Process webhook events (succeeded, failed)
2. Subscription Billing
Define subscription plans and pricing
Create customer in payment provider
Implement subscription creation flow
Handle trial periods
Manage upgrades/downgrades
Implement dunning for failed payments
3. Webhook Handling
Create secure webhook endpoint
Verify webhook signatures
Make handlers idempotent
Process events in order
Handle retry scenarios
Log all webhook events
Best Practices
Never store full card numbers—use tokenization
Always verify webhook signatures
Implement idempotency for payment operations
Use test mode thoroughly before production
Handle all payment states (pending, succeeded, failed)
Store payment provider IDs for reconciliation
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
Storing card numbers	PCI violation	Use tokenization
No webhook verification	Security risk	Verify signatures
Synchronous payment only	Poor UX, timeouts	Async with webhooks
Missing idempotency	Duplicate charges	Idempotency keys
No retry logic	Lost revenue	Implement dunning
Weekly Installs
111
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn