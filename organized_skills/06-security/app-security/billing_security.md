---
rating: ⭐⭐⭐
title: billing-security
url: https://skills.sh/phrazzld/claude-config/billing-security
---

# billing-security

skills/phrazzld/claude-config/billing-security
billing-security
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill billing-security
SKILL.md
Billing & Security Integration Patterns

"Configuration is not reality. Verification must be active, not passive."

This skill codifies lessons from 3 prod incidents (chrondle, bibliomnomnom, volume) where Stripe integrations failed despite passing code review.

Core Principle

Code reviews catch code bugs, not configuration bugs. External service integrations require:

Format validation (API key patterns, URL formats)
Reachability verification (can we actually reach the webhook URL?)
Cross-deployment parity (Vercel and Convex must have same config)
Runtime reconciliation (compare external state vs database state)
Critical Patterns
1. Environment Variable Hygiene

Always trim env vars:

// WRONG - trailing whitespace causes "Invalid character in header"
const key = process.env.STRIPE_SECRET_KEY;

// RIGHT - always trim
const key = process.env.STRIPE_SECRET_KEY?.trim();


Validate format before use:

const STRIPE_KEY_PATTERN = /^sk_(test|live)_[a-zA-Z0-9]+$/;
if (!STRIPE_KEY_PATTERN.test(key)) {
  throw new Error("Invalid STRIPE_SECRET_KEY format");
}

2. Webhook URL Validation

Stripe does NOT follow redirects for POST requests. If your webhook URL returns 3xx, webhooks silently fail.

# Check for redirects BEFORE configuring webhook
curl -s -o /dev/null -w "%{http_code}" -I -X POST "https://your-domain.com/api/webhooks/stripe"
# Must return 4xx or 5xx, NOT 3xx


Use canonical domain:

If example.com redirects to www.example.com, configure webhook for www.example.com
3. Cross-Deployment Parity

When using Vercel + Convex (or similar split architectures):

Env vars must be set on BOTH platforms
Use --prod flag: npx convex env set --prod KEY value
Verify parity: compare vercel env ls with npx convex env list --prod
4. Stripe Parameter Constraints

Mode-dependent parameters:

Parameter	Valid Modes	Invalid Modes
customer_creation	payment, setup	subscription
subscription_data	subscription	payment, setup

Common trap: Using customer_creation: "always" in subscription mode throws an error at checkout time, not at compile time.

Pre-Deployment Checklist

Before deploying any billing integration:

 All env vars trimmed at read time
 API key formats validated
 Webhook URL returns non-3xx status
 Vercel and Convex have matching config
 Signature verification enabled
 Error handling returns 200 (prevent Stripe infinite retries)
Debugging Workflow (OODA-V)

When billing integration fails:

Observe - Check if request reaches server (look for logs)
Orient - If no logs, it is network/redirect, not code
Decide - Run curl -I on webhook URL
Act - Fix configuration
Verify - Resend event, watch pending_webhooks decrease
References
Stripe Constraints - API parameter rules
Env Var Hygiene - Validation patterns
Incident Patterns - Real failures from 3 projects
Scripts
scripts/verify-webhook-url.sh <url> - Check for redirects
scripts/verify-env-parity.sh - Compare Vercel/Convex config
scripts/audit-stripe-config.py - Full Stripe diagnostic
Weekly Installs
24
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn