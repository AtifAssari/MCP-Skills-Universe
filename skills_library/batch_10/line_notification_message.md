---
title: line-notification-message
url: https://skills.sh/abgne/line-dev/line-notification-message
---

# line-notification-message

skills/abgne/line-dev/line-notification-message
line-notification-message
Installation
$ npx skills add https://github.com/abgne/line-dev --skill line-notification-message
SKILL.md
LINE Notification Messages

Do not answer LINE Notification Messages questions from memory — LINE updates APIs frequently and training data is unreliable. Always consult the references below.

LINE Notification Messages allow sending messages to users by specifying their phone number (SHA256-hashed E.164 format), even if they haven't added the LINE Official Account as a friend. Corporate-only service available in Japan, Thailand, and Taiwan. Not for advertising or commercial purposes.

Workflow
Build
Read references/api-common.md (rate limits, forward compatibility, error handling)
Load the relevant reference for the feature being implemented
For architecture or design choices, consult references/experts.md for directional guidance
Write code following specs and constraints from references
Review / Debug
Read references/api-common.md (rate limits, error codes)
Load relevant references for the code being reviewed
Cross-check code against specs (phone hashing format, sending conditions, consent states, billing rules, IP restriction warnings)
For design pattern concerns, consult references/experts.md
Report violations with reference to specific constraints
Environment Variables
LINE_CHANNEL_ACCESS_TOKEN=Bot access token (Messaging API channel)
LINE_CHANNEL_SECRET=Channel secret (webhook signature verification)

Common Specifications

Read references/api-common.md before writing any notification message code. Contains rules that affect all API interactions: forward compatibility (don't use strict schemas — LINE adds fields without notice), rate limits, error handling, and logging recommendations.

Two Message Types
Type	Description	UX Review	Send Endpoint
Template	Predefined layout with templateKey, itemKey, buttonKey. Easy to set up.	Not required	POST /v2/bot/message/pnp/templated/push
Flexible	Free-form message objects (Flex Message, text, etc.). Greater design freedom.	Required	POST /bot/pnp/push
Template type added June 2025 — simpler, no UX review needed
Flexible type (formerly just "LINE notification messages") — allows custom message objects but requires prior UX review
Both types: no images, video, or audio allowed

Full type comparison → references/sending-api.md

Minimal Flow (pseudocode)
# 1. Hash phone number (E.164 → SHA256)
phone = "+818000001234"                    # E.164 format, no hyphens
hashed = SHA256(phone.encode()).hexdigest() # 64-char lowercase hex

# 2a. Send via template type
POST https://api.line.me/v2/bot/message/pnp/templated/push
Authorization: Bearer {channel_access_token}
X-Line-Delivery-Tag: {optional_tracking_tag}
{
  "to": hashed,
  "templateKey": "shipment_completed_ja",
  "body": {
    "emphasizedItem": {"itemKey": "date_002_ja", "content": "August 10"},
    "items": [{"itemKey": "number_001_ja", "content": "1234567"}],
    "buttons": [{"buttonKey": "contact_ja", "url": "https://example.com"}]
  }
}
# → Response: 202 Accepted

# 2b. OR send via flexible type
POST https://api.line.me/bot/pnp/push
Authorization: Bearer {channel_access_token}
{
  "to": hashed,
  "messages": [{"type": "text", "text": "Your order has shipped"}]
}
# → Response: 200 OK

# 3. IMPORTANT: 200/202 does NOT guarantee delivery
#    User may be blocked, consent not given, SMS auth expired, etc.

# 4. Delivery confirmation arrives via webhook
#    event.type = "delivery", delivery.data = hashed phone or delivery tag

API Endpoint Summary
Operation	Endpoint	Response
Send (Template)	POST /v2/bot/message/pnp/templated/push	202
Send (Flexible)	POST /bot/pnp/push	200
Count (Template)	GET /v2/bot/message/delivery/pnp/templated?date=yyyyMMdd	200
Count (Flexible)	GET /v2/bot/message/delivery/pnp?date=yyyyMMdd	200
Domain: api.line.me
Rate limit: 2,000 req/sec for all endpoints
X-Line-Retry-Key is NOT supported — do not use retry keys
Do NOT restrict server IP in channel Security Settings — may cause sending failure

Full API specs, parameters, error codes → references/sending-api.md

Key Concepts
Phone Number Hashing
Normalize to E.164 format (country code, no hyphens): +818000001234
Hash with SHA256: hashlib.sha256("+818000001234".encode()).hexdigest()
Result: 64-char lowercase hex string
Sending Conditions (ALL must be met)
Phone number matches user's LINE account
Phone number is valid (SMS authenticated)
User agrees to receive LINE notification messages
User has not blocked the LINE Official Account
Phone number issued in Japan, Thailand, or Taiwan
User has agreed to LINE's Privacy Policy (revised March 2022)
User Consent States
State	Behavior
Agree (on)	Message delivered normally
Reject (off)	Message deleted, not delivered
Not set	User receives consent prompt; 24 hours to agree or message is deleted
Consent is comprehensive — once agreed, applies to ALL LINE Official Accounts
SMS Authentication
Required once every 180 days
Not required within 180 days of account creation or phone number change
Delivery Confirmation
API response 200/202 does NOT guarantee delivery
Use delivery completion webhook (type: "delivery") to confirm actual delivery
No webhook within 24 hours = message was not delivered

Full technical specs → references/technical-specs.md Template system details → references/template-system.md Webhook details → references/delivery-webhook.md

Reference Index
File	Topic
references/api-common.md	Read first. Rate limits, status codes, error handling, forward compatibility
references/sending-api.md	Send APIs (template + flexible), count APIs, request/response specs, error codes
references/template-system.md	Template structure: templateKey, itemKey, buttonKey, field limits, country suffixes
references/technical-specs.md	Phone hashing, sending conditions, consent flow, SMS auth, billing, IP restrictions
references/delivery-webhook.md	Delivery completion event, X-Line-Delivery-Tag, user consent flows, non-friend behavior
references/experts.md	LINE Notification Messages domain experts for architecture guidance
SDK

Official SDKs: Python | Node.js | Go | Java | PHP | Ruby

Other languages: use LINE OpenAPI specs with OpenAPI Generator.

Weekly Installs
21
Repository
abgne/line-dev
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass