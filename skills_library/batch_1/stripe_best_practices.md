---
title: stripe-best-practices
url: https://skills.sh/stripe/ai/stripe-best-practices
---

# stripe-best-practices

skills/stripe/ai/stripe-best-practices
stripe-best-practices
Installation
$ npx skills add https://github.com/stripe/ai --skill stripe-best-practices
Summary

Decision guide for Stripe API selection, Connect setup, billing, and integration patterns.

Routes integration decisions across six domains: one-time payments (Checkout Sessions), custom payment forms (Payment Element), saved payment methods (Setup Intents), marketplaces (Accounts v2), subscriptions (Billing APIs), and embedded financial accounts (Treasury)
Provides reference documentation for each integration type, including API version guidance (latest: 2026-02-25.clover) and pre-launch checklists
Covers migration paths from deprecated Stripe APIs and best practices for controller properties, account setup, and integration surfaces
SKILL.md

Latest Stripe API version: 2026-04-22.dahlia. Always use the latest API version and SDK unless the user specifies otherwise.

Integration routing
Building…	Recommended API	Details
One-time payments	Checkout Sessions	<references/payments.md>
Custom payment form with embedded UI	Checkout Sessions + Payment Element	<references/payments.md>
Saving a payment method for later	Setup Intents	<references/payments.md>
Connect platform or marketplace	Accounts v2 (/v2/core/accounts)	<references/connect.md>
Subscriptions or recurring billing	Billing APIs + Checkout Sessions	<references/billing.md>
Embedded financial accounts / banking	v2 Financial Accounts	<references/treasury.md>
Security (key management, RAKs, webhooks, OAuth, 2FA, Connect liability)	See security reference	<references/security.md>

Read the relevant reference file before answering any integration question or writing code.

Key documentation

When the user’s request does not clearly fit a single domain above, consult:

Integration Options — Start here when designing any integration.
API Tour — Overview of Stripe’s API surface.
Go Live Checklist — Review before launching.
Weekly Installs
6.5K
Repository
stripe/ai
GitHub Stars
1.5K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn