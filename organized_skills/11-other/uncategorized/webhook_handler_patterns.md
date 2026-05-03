---
rating: ⭐⭐
title: webhook-handler-patterns
url: https://skills.sh/hookdeck/webhook-skills/webhook-handler-patterns
---

# webhook-handler-patterns

skills/hookdeck/webhook-skills/webhook-handler-patterns
webhook-handler-patterns
Installation
$ npx skills add https://github.com/hookdeck/webhook-skills --skill webhook-handler-patterns
SKILL.md
Webhook Handler Patterns
When to Use This Skill
Following the correct webhook handler order (verify → parse → handle idempotently)
Implementing idempotent webhook handlers
Handling errors and configuring retry behavior
Understanding framework-specific gotchas (raw body, middleware order)
Building production-ready webhook infrastructure
Resources
Handler Sequence
references/handler-sequence.md - Verify first, parse second, handle idempotently third
Best Practices
references/idempotency.md - Prevent duplicate processing
references/error-handling.md - Return codes, logging, dead letter queues
references/retry-logic.md - Provider retry schedules, backoff patterns
Framework Guides
references/frameworks/express.md - Express.js patterns and gotchas
references/frameworks/nextjs.md - Next.js App Router patterns
references/frameworks/fastapi.md - FastAPI/Python patterns
Quick Reference
Handler Sequence
Verify signature first — Use raw body; reject invalid requests with 4xx.
Parse payload second — After verification, parse or construct the event.
Handle idempotently third — Check event ID, then process; return 2xx for duplicates.

See references/handler-sequence.md for details and links to provider verification and idempotency patterns.

Response Codes
Code	Meaning	Provider Behavior
2xx	Success	No retry
4xx	Client error	Usually no retry (except 429)
5xx	Server error	Retry with backoff
429	Rate limited	Retry after delay
Idempotency Checklist
Extract unique event ID from payload
Check if event was already processed
Process event within transaction
Store event ID after successful processing
Return success for duplicate events
Related Skills
stripe-webhooks - Stripe payment webhook handling
shopify-webhooks - Shopify e-commerce webhook handling
github-webhooks - GitHub repository webhook handling
resend-webhooks - Resend email webhook handling
chargebee-webhooks - Chargebee billing webhook handling
clerk-webhooks - Clerk auth webhook handling
elevenlabs-webhooks - ElevenLabs webhook handling
openai-webhooks - OpenAI webhook handling
paddle-webhooks - Paddle billing webhook handling
hookdeck-event-gateway - Webhook infrastructure that replaces your queue — guaranteed delivery, automatic retries, replay, rate limiting, and observability for your webhook handlers
Weekly Installs
137
Repository
hookdeck/webhook-skills
GitHub Stars
69
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn