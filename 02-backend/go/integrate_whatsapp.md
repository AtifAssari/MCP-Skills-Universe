---
rating: ⭐⭐
title: integrate-whatsapp
url: https://skills.sh/gokapso/agent-skills/integrate-whatsapp
---

# integrate-whatsapp

skills/gokapso/agent-skills/integrate-whatsapp
integrate-whatsapp
Installation
$ npx skills add https://github.com/gokapso/agent-skills --skill integrate-whatsapp
Summary

End-to-end WhatsApp integration with onboarding, messaging, templates, interactive messages, and native Flows.

Onboard customers via hosted setup links with CLI or direct API; detect connections through webhooks or redirect URLs
Send text messages, templates (with named parameters and buttons), interactive messages, and media; read inbox data via CLI, SDK, or API
Build native WhatsApp Flows (forms) with static or dynamic endpoints; manage encryption, versioning, and testing
Receive project and phone-number events via webhooks with configurable buffering, payload versions, and signature verification
Includes 40+ helper scripts for templates, flows, webhooks, messaging, and OpenAPI exploration; full reference docs and asset examples
SKILL.md
Integrate WhatsApp
Setup

Preferred path:

Kapso CLI installed and authenticated (kapso login)
Use kapso status to confirm project access before onboarding or messaging

Fallback path: Env vars:

KAPSO_API_BASE_URL (host only, no /platform/v1)
KAPSO_API_KEY
META_GRAPH_VERSION (optional, default v24.0)

Auth header (direct API calls):

X-API-Key: <api_key>


Install deps (once):

npm i

Connect WhatsApp (setup links)

Preferred onboarding path (CLI):

Start onboarding: kapso setup
If setup is blocked, resolve context with:
kapso projects list
kapso projects use <project-id>
kapso customers list
kapso customers new --name "<customer-name>" --external-id <external-id>
kapso setup --customer <customer-id>
Complete the hosted onboarding URL
Confirm connected numbers: kapso whatsapp numbers list --output json
Resolve the exact number you want to operate: kapso whatsapp numbers resolve --phone-number "<display-number>" --output json

Fallback onboarding flow (direct API):

Create customer: POST /platform/v1/customers
Generate setup link: POST /platform/v1/customers/:id/setup_links
Customer completes embedded signup
Use phone_number_id to send messages and configure webhooks

Detect connection:

Project webhook whatsapp.phone_number.created (recommended)
Success redirect URL query params (use for frontend UX)

Recommended Kapso setup-link defaults:

{
  "setup_link": {
    "allowed_connection_types": ["dedicated"],
    "provision_phone_number": true,
    "phone_number_country_isos": ["US"]
  }
}


Notes:

kapso setup and kapso whatsapp numbers new use dedicated plus provisioning by default.

Keep phone_number_country_isos, phone_number_area_code, language, and redirect URLs as optional overrides.

Platform API base: /platform/v1

Meta proxy base: /meta/whatsapp/v24.0 (messaging, templates, media)

Use phone_number_id as the primary WhatsApp identifier

Receive events (webhooks)

Use webhooks to receive:

Project events (connection lifecycle, workflow events)
Phone-number events (messages, conversations, delivery status)

Scope rules:

Project webhooks: only project-level events (connection lifecycle, workflow events)
Phone-number webhooks: only WhatsApp message + conversation events for that phone_number_id
WhatsApp message/conversation events (whatsapp.message.*, whatsapp.conversation.*) are phone-number only

Create a webhook:

Project-level: node scripts/create.js --scope project --url <https://...> --events <csv>
Phone-number: node scripts/create.js --phone-number-id <id> --url <https://...> --events <csv>

Common flags for create/update:

--url <https://...> - webhook destination
--events <csv|json-array> - event types (Kapso webhooks)
--kind <kapso|meta> - Kapso (event-based) vs raw Meta forwarding
--payload-version <v1|v2> - payload format (v2 recommended)
--buffer-enabled <true|false> - enable buffering for whatsapp.message.received
--buffer-window-seconds <n> - 1-60 seconds
--max-buffer-size <n> - 1-100
--active <true|false> - enable/disable

Test delivery:

node scripts/test.js --webhook-id <id>


Always verify signatures. See:

references/webhooks-overview.md
references/webhooks-reference.md
Send and read messages
Discover IDs first

Two Meta IDs are needed for different operations:

ID	Used for	How to discover
business_account_id (WABA)	Template CRUD	kapso whatsapp numbers resolve --phone-number "<display-number>" --output json or node scripts/list-platform-phone-numbers.mjs
phone_number_id	Sending messages, media upload	kapso whatsapp numbers resolve --phone-number "<display-number>" --output json or node scripts/list-platform-phone-numbers.mjs
Operate with the CLI first

Common commands:

kapso whatsapp numbers list --output json
kapso whatsapp numbers resolve --phone-number "<display-number>" --output json
kapso whatsapp messages send --phone-number-id <PHONE_NUMBER_ID> --to <wa-id> --text "Hello from Kapso"
kapso whatsapp messages list --phone-number-id <PHONE_NUMBER_ID> --limit 50 --output json
kapso whatsapp messages get <MESSAGE_ID> --phone-number-id <PHONE_NUMBER_ID> --output json
kapso whatsapp conversations list --phone-number-id <PHONE_NUMBER_ID> --output json
kapso whatsapp templates list --phone-number-id <PHONE_NUMBER_ID> --output json
kapso whatsapp templates get <TEMPLATE_ID> --phone-number-id <PHONE_NUMBER_ID> --output json

SDK setup

Install:

npm install @kapso/whatsapp-cloud-api


Create client:

import { WhatsAppClient } from "@kapso/whatsapp-cloud-api";

const client = new WhatsAppClient({
  baseUrl: "https://api.kapso.ai/meta/whatsapp",
  kapsoApiKey: process.env.KAPSO_API_KEY!
});

Send a text message

Via SDK:

await client.messages.sendText({
  phoneNumberId: "<PHONE_NUMBER_ID>",
  to: "+15551234567",
  body: "Hello from Kapso"
});

Send a template message
Discover IDs: node scripts/list-platform-phone-numbers.mjs
Draft template payload from assets/template-utility-order-status-update.json
Create: node scripts/create-template.mjs --business-account-id <WABA_ID> --file <payload.json>
Check status: node scripts/template-status.mjs --business-account-id <WABA_ID> --name <name>
Send: node scripts/send-template.mjs --phone-number-id <ID> --file <send-payload.json>
Send an interactive message

Interactive messages require an active 24-hour session window. For outbound notifications outside the window, use templates.

Discover phone_number_id
Pick payload from assets/send-interactive-*.json
Send: node scripts/send-interactive.mjs --phone-number-id <ID> --file <payload.json>
Read inbox data

Preferred path:

CLI: kapso whatsapp messages ..., kapso whatsapp conversations ..., kapso whatsapp templates ...

Fallback path:

Proxy: GET /{phone_number_id}/messages, GET /{phone_number_id}/conversations
SDK: client.messages.query(), client.messages.get(), client.conversations.list(), client.conversations.get(), client.templates.get()
Template rules

Creation:

Use parameter_format: "NAMED" with {{param_name}} (preferred over positional)
Include examples when using variables in HEADER/BODY
Use language (not language_code)
Don't interleave QUICK_REPLY with URL/PHONE_NUMBER buttons
URL button variables must be at the end of the URL and use positional {{1}}

Send-time:

For NAMED templates, include parameter_name in header/body params
URL buttons need a button component with sub_type: "url" and index
Media headers use either id or link (never both)
WhatsApp Flows

Use Flows to build native WhatsApp forms. Read references/whatsapp-flows-spec.md before editing Flow JSON.

Create and publish a flow
Create flow: node scripts/create-flow.js --phone-number-id <id> --name <name>
Update JSON: node scripts/update-flow-json.js --flow-id <id> --json-file <path>
Publish: node scripts/publish-flow.js --flow-id <id>
Test: node scripts/send-test-flow.js --phone-number-id <id> --flow-id <id> --to <phone>
Attach a data endpoint (dynamic flows)
Set up encryption: node scripts/setup-encryption.js --flow-id <id>
Create endpoint: node scripts/set-data-endpoint.js --flow-id <id> --code-file <path>
Deploy: node scripts/deploy-data-endpoint.js --flow-id <id>
Register: node scripts/register-data-endpoint.js --flow-id <id>
Flow JSON rules

Static flows (no data endpoint):

Use version: "7.3"
routing_model and data_api_version are optional
See assets/sample-flow.json

Dynamic flows (with data endpoint):

Use version: "7.3" with data_api_version: "3.0"
routing_model is required (defines valid screen transitions)
See assets/dynamic-flow.json
Data endpoint rules

Handler signature:

async function handler(request, env) {
  const body = await request.json();
  // body.data_exchange.action: INIT | data_exchange | BACK
  // body.data_exchange.screen: current screen id
  // body.data_exchange.data: user inputs
  return Response.json({
    version: "3.0",
    screen: "NEXT_SCREEN_ID",
    data: { }
  });
}

Do not use export or module.exports
Completion uses screen: "SUCCESS" with extension_message_response.params
Do not include endpoint_uri or data_channel_uri (Kapso injects these)
Troubleshooting
Preview shows "flow_token is missing": flow is dynamic without a data endpoint. Attach one and refresh.
Encryption setup errors: enable encryption in Settings for the phone number/WABA.
OAuthException 139000 (Integrity): WABA must be verified in Meta security center.
Scripts
Webhooks
Script	Purpose
list.js	List webhooks
get.js	Get webhook details
create.js	Create a webhook
update.js	Update a webhook
delete.js	Delete a webhook
test.js	Send a test event
Messaging and templates
Script	Purpose	Required ID
list-platform-phone-numbers.mjs	Discover business_account_id + phone_number_id	—
list-connected-numbers.mjs	List WABA phone numbers	business_account_id
list-templates.mjs	List templates (with filters)	business_account_id
template-status.mjs	Check single template status	business_account_id
create-template.mjs	Create a template	business_account_id
update-template.mjs	Update existing template	business_account_id
send-template.mjs	Send template message	phone_number_id
send-interactive.mjs	Send interactive message	phone_number_id
upload-media.mjs	Upload media for send-time headers	phone_number_id
Flows
Script	Purpose
list-flows.js	List all flows
create-flow.js	Create a new flow
get-flow.js	Get flow details
read-flow-json.js	Read flow JSON
update-flow-json.js	Update flow JSON (creates new version)
publish-flow.js	Publish a flow
get-data-endpoint.js	Get data endpoint config
set-data-endpoint.js	Create/update data endpoint code
deploy-data-endpoint.js	Deploy data endpoint
register-data-endpoint.js	Register data endpoint with Meta
get-encryption-status.js	Check encryption status
setup-encryption.js	Set up flow encryption
send-test-flow.js	Send a test flow message
delete-flow.js	Delete a flow
list-flow-responses.js	List stored flow responses
list-function-logs.js	List function logs
list-function-invocations.js	List function invocations
OpenAPI
Script	Purpose
openapi-explore.mjs	Explore OpenAPI (search/op/schema/where)

Examples:

node scripts/openapi-explore.mjs --spec whatsapp search "template"
node scripts/openapi-explore.mjs --spec whatsapp op sendMessage
node scripts/openapi-explore.mjs --spec whatsapp schema TemplateMessage
node scripts/openapi-explore.mjs --spec platform ops --tag "WhatsApp Flows"
node scripts/openapi-explore.mjs --spec platform op setupWhatsappFlowEncryption
node scripts/openapi-explore.mjs --spec platform search "setup link"

Assets
File	Description
template-utility-order-status-update.json	UTILITY template with named params + URL button
send-template-order-status-update.json	Send-time payload for order_status_update
template-utility-named.json	UTILITY template showing button ordering rules
template-marketing-media-header.json	MARKETING template with IMAGE header
template-authentication-otp.json	AUTHENTICATION OTP template (COPY_CODE)
send-interactive-buttons.json	Interactive button message
send-interactive-list.json	Interactive list message
send-interactive-cta-url.json	Interactive CTA URL message
send-interactive-location-request.json	Location request message
send-interactive-catalog-message.json	Catalog message
sample-flow.json	Static flow example (no endpoint)
dynamic-flow.json	Dynamic flow example (with endpoint)
webhooks-example.json	Webhook create/update payload example
References
references/getting-started.md - Platform onboarding
references/platform-api-reference.md - Full endpoint reference
references/setup-links.md - Setup link configuration
references/detecting-whatsapp-connection.md - Connection detection methods
references/webhooks-overview.md - Webhook types, signature verification, retries
references/webhooks-event-types.md - Available events
references/webhooks-reference.md - Webhook API and payload notes
references/templates-reference.md - Template creation rules, components cheat sheet, send-time components
references/whatsapp-api-reference.md - Meta proxy payloads for messages and conversations
references/whatsapp-cloud-api-js.md - SDK usage for sending and reading messages
references/whatsapp-flows-spec.md - Flow JSON spec
Related skills
automate-whatsapp - Workflows, agents, and automations
observe-whatsapp - Debugging, logs, health checks
[integrate-whatsapp file map]|root: .
|.:{package.json,SKILL.md}
|assets:{dynamic-flow.json,sample-flow.json,send-interactive-buttons.json,send-interactive-catalog-message.json,send-interactive-cta-url.json,send-interactive-list.json,send-interactive-location-request.json,send-template-order-status-update.json,template-authentication-otp.json,template-marketing-media-header.json,template-utility-named.json,template-utility-order-status-update.json,webhooks-example.json}
|references:{detecting-whatsapp-connection.md,getting-started.md,platform-api-reference.md,setup-links.md,templates-reference.md,webhooks-event-types.md,webhooks-overview.md,webhooks-reference.md,whatsapp-api-reference.md,whatsapp-cloud-api-js.md,whatsapp-flows-spec.md}
|scripts:{create-flow.js,create-function.js,create-template.mjs,create.js,delete-flow.js,delete.js,deploy-data-endpoint.js,deploy-function.js,get-data-endpoint.js,get-encryption-status.js,get-flow.js,get-function.js,get.js,list-connected-numbers.mjs,list-flow-responses.js,list-flows.js,list-function-invocations.js,list-function-logs.js,list-platform-phone-numbers.mjs,list-templates.mjs,list.js,openapi-explore.mjs,publish-flow.js,read-flow-json.js,register-data-endpoint.js,send-interactive.mjs,send-template.mjs,send-test-flow.js,set-data-endpoint.js,setup-encryption.js,submit-template.mjs,template-status.mjs,test.js,update-flow-json.js,update-function.js,update-template.mjs,update.js,upload-media.mjs,upload-template-header-handle.mjs}
|scripts/lib:{args.mjs,cli.js,env.js,env.mjs,http.js,output.js,output.mjs,request.mjs,run.js,whatsapp-flow.js}
|scripts/lib/webhooks:{args.js,kapso-api.js,webhook.js}

Weekly Installs
1.4K
Repository
gokapso/agent-skills
GitHub Stars
110
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn