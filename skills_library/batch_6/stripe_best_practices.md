---
title: stripe-best-practices
url: https://skills.sh/site/docs.stripe.com/stripe-best-practices
---

# stripe-best-practices

skills/docs.stripe.com/stripe-best-practices
stripe-best-practices
$ npx skills add https://docs.stripe.com
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
15.6K
Source
docs.stripe.com
First Seen
1 day ago