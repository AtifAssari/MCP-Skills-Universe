---
title: messaging-api
url: https://skills.sh/abgne/line-dev/messaging-api
---

# messaging-api

skills/abgne/line-dev/messaging-api
messaging-api
Installation
$ npx skills add https://github.com/abgne/line-dev --skill messaging-api
SKILL.md
LINE Messaging API

Do not answer LINE API questions from memory — LINE updates APIs frequently and training data is unreliable. Always consult the references below.

Reference for building, reviewing, and debugging LINE Bots and LINE Messaging API integrations.

Workflow
Build
Read references/api-common.md (rate limits, forward compatibility, error handling)
Load the relevant reference for the feature being implemented
For architecture or design choices, consult references/experts.md for directional guidance
Write code following specs and constraints from references
Review / Debug
Read references/api-common.md (rate limits, error codes)
Load relevant references for the code being reviewed
Cross-check code against specs (size limits, token expiry, counting rules, required fields)
For design pattern concerns, consult references/experts.md
Report violations with reference to specific constraints
Environment Variables
LINE_CHANNEL_ACCESS_TOKEN=Bot access token
LINE_CHANNEL_SECRET=Channel secret (webhook signature verification)

Common Specifications

Read references/api-common.md before writing any LINE bot code. Contains rules that affect all API interactions: forward compatibility (don't use strict schemas — LINE adds fields without notice), rate limits, error handling, retry policy, and logging recommendations.

Webhook
Verification: x-line-signature header (HMAC-SHA256, base64, key = Channel Secret)
Body: {"destination": "U...", "events": [...]}
Bot server must return 200
Signature Verification (pseudocode)
channel_secret = ENV['LINE_CHANNEL_SECRET']
signature = request.headers['x-line-signature']
body = request.body   # raw bytes, do NOT parse/reformat before verification

digest = HMAC_SHA256(key = channel_secret, message = body)
expected = Base64.encode(digest)

if signature != expected:
    return 403  # reject — not from LINE

events = JSON.parse(body)['events']
for event in events:
    handle(event)
return 200

Never deserialize or re-format the body before verification
Use UTF-8 encoding exclusively
Official SDKs handle this automatically — use them when possible

Full event types, properties, and webhook settings → references/webhook-events.md

Message Sending

All require Authorization: Bearer {channel access token}:

Mode	Endpoint	Purpose
Reply	POST /v2/bot/message/reply	Reply to user (requires one-time replyToken)
Push	POST /v2/bot/message/push	Send to a specific user/group at any time
Multicast	POST /v2/bot/message/multicast	Send to multiple users (max 500)
Broadcast	POST /v2/bot/message/broadcast	Send to all friends
Max 5 messages per request
Domain: api.line.me (general) / api-data.line.me (content upload)

Message objects → references/message-objects.md Full sending API (Narrowcast, statistics, validation, etc.) → references/message-sending.md

Flex Message

Three-layer structure:

Container (Bubble / Carousel)
  └── Block (Header / Hero / Body / Footer)
       └── Component (Box / Button / Image / Video / Icon / Text / Span / Separator)


Minimal Flex Message:

{
  "type": "flex", "altText": "Notification",
  "contents": {
    "type": "bubble",
    "body": {
      "type": "box", "layout": "vertical",
      "contents": [{"type": "text", "text": "Hello Flex!", "weight": "bold"}]
    }
  }
}


Full component specs, layout, video → references/flex-message.md Official Flex Message Simulator examples → assets/examples/

Reference Index
File	Topic
references/api-common.md	Read first. Rate limits, error handling, forward compatibility
references/webhook-events.md	Webhook event types and JSON structure
references/message-objects.md	Message objects, Quick Reply, sender customization
references/action-objects.md	Action objects (postback, URI, datetimepicker, etc.)
references/message-sending.md	Reply/Push/Multicast/Narrowcast/Broadcast, statistics
references/flex-message.md	Flex Message components, layout, styles
references/rich-menu.md	Rich Menu CRUD, tab switching, display priority
references/user.md	User profile, follower IDs, account link
references/group-chat.md	Group/Room messaging and member APIs
references/audience.md	Audience management (create/add/get/delete)
references/insights.md	Delivery, follower, and interaction insights
references/channel-token.md	Channel access token lifecycle
references/coupon.md	Coupon CRUD, reward types, sending
references/url-schemes.md	LINE URL schemes for deep linking
references/experts.md	Expert domain routing and 17 specialist profiles
assets/examples/	Flex Message JSON examples (11 showcases)
SDK

Official SDKs: Python | Node.js | Go | Java | PHP | Ruby

Other languages: use LINE OpenAPI specs with OpenAPI Generator.

Weekly Installs
45
Repository
abgne/line-dev
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass