---
rating: ⭐⭐⭐
title: stripe-local-dev
url: https://skills.sh/phrazzld/claude-config/stripe-local-dev
---

# stripe-local-dev

skills/phrazzld/claude-config/stripe-local-dev
stripe-local-dev
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill stripe-local-dev
SKILL.md
/stripe-local-dev

Ensure Stripe webhooks work in local development by auto-syncing ephemeral secrets.

The Problem

Stripe CLI generates a new webhook secret every time stripe listen starts. If your dev script auto-starts the listener but doesn't sync the secret, you get:

Webhook error: signature verification failed
No signatures found matching the expected signature for payload

The Solution Pattern

Auto-start requires auto-sync. Use dev-stripe.sh:

Extract secret via stripe listen --print-secret
Sync to environment (Convex env OR .env.local)
THEN start forwarding

Also: if checkout succeeds but access stays locked and you see:

stripe_webhook_missing_convex_token
Webhook token is not configured then CONVEX_WEBHOOK_TOKEN is missing/mismatched between Next runtime and Convex.
Architecture Decision
Webhook Location	Secret Sync Target	Restart?	Recommendation
Convex HTTP (convex/http.ts)	bunx convex env set (or npx)	No	Best
Next.js API Route	.env.local	Yes	Requires orchestration

Prefer Convex HTTP webhooks - secret sync is instant, no restart needed.

Implementation
Option A: Convex HTTP Webhooks (Recommended)

Copy script:

cp ~/.claude/skills/stripe-local-dev/scripts/dev-stripe-convex.sh scripts/dev-stripe.sh
chmod +x scripts/dev-stripe.sh


Update package.json:

"stripe:listen": "./scripts/dev-stripe.sh"

Option B: Next.js API Webhooks

Copy script:

cp ~/.claude/skills/stripe-local-dev/scripts/dev-stripe-nextjs.sh scripts/dev-stripe.sh
chmod +x scripts/dev-stripe.sh


Update package.json:

"stripe:listen": "./scripts/dev-stripe.sh"


Note: Next.js needs restart to pick up env changes. The script warns about this.

Verification

After setup, run:

bun run dev  # or: pnpm dev
# Then in another terminal:
stripe trigger checkout.session.completed
# Check logs for 200 response, not 400

Quick Diagnostics
Symptom	Cause	Fix
All webhooks return 400	Stale secret	Restart dev server or re-sync secret
"signature verification failed"	Secret mismatch	Check CLI output matches env
Works once, fails after restart	No auto-sync	Add dev-stripe.sh script
CLI shows delivered, app shows error	Wrong env target	Check sync target (Convex vs .env.local)
Checkout succeeds, still locked, confirm/webhook 5xx	Missing/mismatched CONVEX_WEBHOOK_TOKEN	Ensure token parity, restart Next.js
Related Skills
/check-stripe - Audit Stripe integration
/stripe-health - Webhook health diagnostics
/stripe-audit - Comprehensive Stripe audit
Weekly Installs
23
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