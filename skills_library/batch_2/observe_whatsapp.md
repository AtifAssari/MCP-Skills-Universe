---
title: observe-whatsapp
url: https://skills.sh/gokapso/agent-skills/observe-whatsapp
---

# observe-whatsapp

skills/gokapso/agent-skills/observe-whatsapp
observe-whatsapp
Installation
$ npx skills add https://github.com/gokapso/agent-skills --skill observe-whatsapp
Summary

Diagnose WhatsApp message delivery, webhook issues, and API errors in Kapso.

Investigate message delivery through phone number resolution, message listing, and conversation inspection using Kapso CLI or fallback Node scripts
Debug webhook deliveries and retries, inspect API logs, and triage message errors to identify root causes of production failures
Run health checks on projects and phone numbers to confirm configuration state and operational readiness
Includes reference guides for message debugging, error triage, and health checks; complementary to integrate-whatsapp for webhook setup and automate-whatsapp for workflows
SKILL.md
Observe WhatsApp
When to use

Use this skill for operational diagnostics: message delivery investigation, webhook delivery debugging, error triage, and WhatsApp health checks.

Setup

Preferred path:

Kapso CLI installed and authenticated (kapso login)
Start with kapso status to confirm project access and available WhatsApp numbers

Fallback path: Env vars:

KAPSO_API_BASE_URL (host only, no /platform/v1)
KAPSO_API_KEY
How to
Investigate message delivery

Preferred path:

Resolve the number: kapso whatsapp numbers resolve --phone-number "<display-number>" --output json
List recent messages: kapso whatsapp messages list --phone-number "<display-number>" --limit 50 --output json
Inspect a specific message: kapso whatsapp messages get <message-id> --phone-number-id <id> --output json
Inspect the conversation: kapso whatsapp conversations list --phone-number "<display-number>" --output json

Fallback path:

List messages: node scripts/messages.js --phone-number-id <id>
Inspect message: node scripts/message-details.js --message-id <id>
Find conversation: node scripts/lookup-conversation.js --phone-number <e164>
Triage errors

Preferred path:

Confirm project and number state: kapso status
Run number health: kapso whatsapp numbers health --phone-number "<display-number>" --output human
Inspect related templates when relevant: kapso whatsapp templates list --phone-number "<display-number>" --output json

Fallback path:

Message errors: node scripts/errors.js
API logs: node scripts/api-logs.js
Webhook deliveries: node scripts/webhook-deliveries.js
Run health checks

Preferred path:

Project overview: kapso status
Phone number health: kapso whatsapp numbers health --phone-number "<display-number>" --output human

Fallback path:

Project overview: node scripts/overview.js
Phone number health: node scripts/whatsapp-health.js --phone-number-id <id>
Scripts
Messages
Script	Purpose
messages.js	List messages
message-details.js	Get message details
lookup-conversation.js	Find conversation by phone or ID
Errors and logs
Script	Purpose
errors.js	List message errors
api-logs.js	List external API logs
webhook-deliveries.js	List webhook delivery attempts
Health
Script	Purpose
overview.js	Project overview
whatsapp-health.js	Phone number health check
OpenAPI
Script	Purpose
openapi-explore.mjs	Explore OpenAPI (search/op/schema/where)

Install deps (once):

npm i


Examples:

node scripts/openapi-explore.mjs --spec platform search "webhook deliveries"
node scripts/openapi-explore.mjs --spec platform op listWebhookDeliveries
node scripts/openapi-explore.mjs --spec platform schema WebhookDelivery

Notes
For webhook setup (create/update/delete, signature verification, event types), use integrate-whatsapp.
Prefer resolving a display phone number to the canonical phone_number_id before deep debugging.
Keep the scripts as the fallback path when the CLI is unavailable or when you need API-log or webhook-delivery inspection.
References
references/message-debugging-reference.md - Message debugging guide
references/triage-reference.md - Error triage guide
references/health-reference.md - Health check guide
Related skills
integrate-whatsapp - Onboarding, webhooks, messaging, templates, flows
automate-whatsapp - Workflows, agents, and automations
[observe-whatsapp file map]|root: .
|.:{package.json,SKILL.md}
|assets:{health-example.json,message-debugging-example.json,triage-example.json}
|references:{health-reference.md,message-debugging-reference.md,triage-reference.md}
|scripts:{api-logs.js,errors.js,lookup-conversation.js,message-details.js,messages.js,openapi-explore.mjs,overview.js,webhook-deliveries.js,whatsapp-health.js}
|scripts/lib/messages:{args.js,kapso-api.js}
|scripts/lib/status:{args.js,kapso-api.js}
|scripts/lib/triage:{args.js,kapso-api.js}

Weekly Installs
882
Repository
gokapso/agent-skills
GitHub Stars
110
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass