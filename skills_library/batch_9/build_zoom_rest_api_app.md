---
title: build-zoom-rest-api-app
url: https://skills.sh/anthropics/knowledge-work-plugins/build-zoom-rest-api-app
---

# build-zoom-rest-api-app

skills/anthropics/knowledge-work-plugins/build-zoom-rest-api-app
build-zoom-rest-api-app
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill build-zoom-rest-api-app
SKILL.md
/build-zoom-rest-api-app

Background reference for deterministic server-side Zoom automation and resource management. Prefer plan-zoom-product, plan-zoom-integration, or debug-zoom first, then route here for endpoint-level detail.

Zoom REST API

Expert guidance for building server-side integrations with the Zoom REST API. This API provides 600+ endpoints for managing meetings, users, webinars, recordings, reports, and all Zoom platform resources programmatically.

Official Documentation: https://developers.zoom.us/api-hub/ API Hub Reference: https://developers.zoom.us/api-hub/meetings/ OpenAPI Inventories: https://developers.zoom.us/api-hub/<domain>/methods/endpoints.json

Quick Links

New to Zoom REST API? Follow this path:

API Architecture - Base URLs, regional URLs, me keyword, ID vs UUID, time formats
Authentication Flows - OAuth setup (S2S, User, PKCE, Device Code)
Meeting URLs vs Meeting SDK - Stop mixing join_url with Meeting SDK
Meeting Lifecycle - Create → Update → Start → End → Delete with webhooks
Rate Limiting Strategy - Plan tiers, per-user limits, retry patterns

Reference:

Meetings - Meeting CRUD, types, settings
Users - User provisioning and management
Recordings - Cloud recording access and download
AI Services - Scribe endpoint inventory and current AI Services path surface
GraphQL Queries - Alternative query API (beta)
Integrated Index - see the section below in this file

Most domain files under references/ are aligned to the official API Hub endpoints.json inventories. Treat those files as the local source of truth for method/path discovery.

Having issues?

Start with preflight checks → 5-Minute Runbook
401 Unauthorized → Authentication Flows (check token expiry, scopes)
429 Too Many Requests → Rate Limiting Strategy
Error codes → Common Errors
Pagination confusion → Common Issues
Webhooks not arriving → Webhook Server
Forum-derived FAQs → Forum Top Questions
Token/scope failures → Token + Scope Playbook

Building event-driven integrations?

Webhook Server - Express.js server with CRC validation
Recording Pipeline - Auto-download via webhook events
Quick Start
Get an Access Token (Server-to-Server OAuth)
curl -X POST "https://zoom.us/oauth/token" \
  -H "Authorization: Basic $(echo -n 'CLIENT_ID:CLIENT_SECRET' | base64)" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=account_credentials&account_id=ACCOUNT_ID"


Response:

{
  "access_token": "eyJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 3600,
  "scope": "meeting:read meeting:write user:read"
}

Create a Meeting
curl -X POST "https://api.zoom.us/v2/users/HOST_USER_ID/meetings" \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Team Standup",
    "type": 2,
    "start_time": "2025-03-15T10:00:00Z",
    "duration": 30,
    "settings": {
      "join_before_host": false,
      "waiting_room": true
    }
  }'


For S2S OAuth, use an explicit host user ID or email in the path. Do not use me.

List Users with Pagination
curl "https://api.zoom.us/v2/users?page_size=300&status=active" \
  -H "Authorization: Bearer ACCESS_TOKEN"

Base URL
https://api.zoom.us/v2

Regional Base URLs

The api_url field in OAuth token responses indicates the user's region. Use regional URLs for data residency compliance:

Region	URL
Global (default)	https://api.zoom.us/v2
Australia	https://api-au.zoom.us/v2
Canada	https://api-ca.zoom.us/v2
European Union	https://api-eu.zoom.us/v2
India	https://api-in.zoom.us/v2
Saudi Arabia	https://api-sa.zoom.us/v2
Singapore	https://api-sg.zoom.us/v2
United Kingdom	https://api-uk.zoom.us/v2
United States	https://api-us.zoom.us/v2

Note: You can always use the global URL https://api.zoom.us regardless of the api_url value.

Key Features
Feature	Description
Meeting Management	Create, read, update, delete meetings with full scheduling control
User Provisioning	Automated user lifecycle (create, update, deactivate, delete)
Webinar Operations	Webinar CRUD, registrant management, panelist control
Cloud Recordings	List, download, delete recordings with file-type filtering
Reports & Analytics	Usage reports, participant data, daily statistics
Team Chat	Channel management, messaging, chatbot integration
Zoom Phone	Call management, voicemail, call routing
Zoom Rooms	Room management, device control, scheduling
Webhooks	Real-time event notifications for 100+ event types
WebSockets	Persistent event streaming without public endpoints
GraphQL (Beta)	Single-endpoint flexible queries at v3/graphql
AI Companion	Meeting summaries, transcripts, AI-generated content
AI Services / Scribe	File and archive transcription via Build-platform JWT-authenticated endpoints
Prerequisites
Zoom account (Free tier has API access with lower rate limits)
App registered on Zoom App Marketplace
OAuth credentials (Server-to-Server OAuth or User OAuth)
Appropriate scopes for target endpoints

Need help with authentication? See the zoom-oauth skill for complete OAuth flow implementation.

Critical Gotchas and Best Practices
⚠️ JWT App Type is Deprecated

The JWT app type is deprecated. Migrate to Server-to-Server OAuth. This does NOT affect JWT token signatures used in Video SDK — only the Marketplace "JWT" app type for REST API access.

// OLD (JWT app type - DEPRECATED)
const token = jwt.sign({ iss: apiKey, exp: expiry }, apiSecret);

// NEW (Server-to-Server OAuth)
const token = await getServerToServerToken(accountId, clientId, clientSecret);

⚠️ The me Keyword Rules
User-level OAuth apps: MUST use me instead of userId (otherwise: invalid token error)
Server-to-Server OAuth apps: MUST NOT use me — provide the actual userId or email
Account-level OAuth apps: Can use either me or userId
⚠️ Meeting ID vs UUID — Double Encoding

UUIDs that begin with / or contain // must be double URL-encoded:

// UUID: /abc==
// Single encode: %2Fabc%3D%3D
// Double encode: %252Fabc%253D%253D  ← USE THIS

const uuid = '/abc==';
const encoded = encodeURIComponent(encodeURIComponent(uuid));
const url = `https://api.zoom.us/v2/meetings/${encoded}`;

⚠️ Time Formats
yyyy-MM-ddTHH:mm:ssZ — UTC time (note the Z suffix)
yyyy-MM-ddTHH:mm:ss — Local time (no Z, uses timezone field)
Some report APIs only accept UTC. Check the API reference for each endpoint.
⚠️ Rate Limits Are Per-Account, Not Per-App

All apps on the same Zoom account share rate limits. One heavy app can impact others. Monitor X-RateLimit-Remaining headers proactively.

⚠️ Per-User Daily Limits

Meeting/Webinar create/update operations are limited to 100 per day per user (resets at 00:00 UTC). Distribute operations across different host users when doing bulk operations.

⚠️ Download URLs Require Auth and Follow Redirects

Recording download_url values require Bearer token authentication and may redirect. Always follow redirects:

curl -L -H "Authorization: Bearer ACCESS_TOKEN" "https://zoom.us/rec/download/..."

Use Webhooks Instead of Polling
// DON'T: Poll every minute (wastes API quota)
setInterval(() => getMeetings(), 60000);

// DO: Receive webhook events in real-time
app.post('/webhook', (req, res) => {
  if (req.body.event === 'meeting.started') {
    handleMeetingStarted(req.body.payload);
  }
  res.status(200).send();
});


Webhook setup details: See the zoom-webhooks skill for comprehensive webhook implementation.

Complete Documentation Library

This skill includes comprehensive guides organized by category:

Core Concepts
API Architecture - REST design, base URLs, regional routing, me keyword, ID vs UUID, time formats
Authentication Flows - All OAuth flows (S2S, User, PKCE, Device Code)
Rate Limiting Strategy - Limits by plan, retry patterns, request queuing
Complete Examples
Meeting Lifecycle - Full Create → Update → Start → End → Delete flow with webhook events
User Management - CRUD users, list with pagination, bulk operations
Recording Pipeline - Download recordings via webhooks + API
Webhook Server - Express.js server with CRC validation and signature verification
GraphQL Queries - GraphQL queries, mutations, cursor pagination
Troubleshooting
Common Errors - HTTP status codes, Zoom error codes, error response formats
Common Issues - Rate limits, token refresh, pagination pitfalls, gotchas
References (39 files covering all Zoom API domains)
Core APIs
references/meetings.md - Meeting CRUD, types, settings
references/users.md - User provisioning, types, scopes
references/webinars.md - Webinar management, registrants
references/recordings.md - Cloud recording access
references/reports.md - Usage reports, analytics
references/accounts.md - Account management
Communication
references/team-chat.md - Team Chat messaging
references/chatbot.md - Interactive chatbots
references/phone.md - Zoom Phone
references/mail.md - Zoom Mail
references/calendar.md - Zoom Calendar
Infrastructure
references/rooms.md - Zoom Rooms
references/scim2.md - SCIM 2.0 provisioning APIs
references/rate-limits.md - Rate limit details
references/qss.md - Quality of Service Subscription
Advanced
references/graphql.md - GraphQL API (beta)
references/ai-companion.md - AI features
references/authentication.md - Auth reference
references/openapi.md - OpenAPI specs, Postman, code generation
Additional API Domains
references/events.md - Events and event platform APIs
references/scheduler.md - Zoom Scheduler APIs
references/tasks.md - Tasks APIs
references/whiteboard.md - Whiteboard APIs
references/video-management.md - Video management APIs
references/video-sdk-api.md - Video SDK REST APIs
references/marketplace-apps.md - Marketplace app management
references/commerce.md - Commerce and billing APIs
references/contact-center.md - Contact Center APIs
references/quality-management.md - Quality management APIs
references/workforce-management.md - Workforce management APIs
references/healthcare.md - Healthcare APIs
references/auto-dialer.md - Auto dialer APIs
references/number-management.md - Number management APIs
references/revenue-accelerator.md - Revenue Accelerator APIs
references/virtual-agent.md - Virtual Agent APIs
references/cobrowse-sdk-api.md - Cobrowse SDK APIs
references/crc.md - Cloud Room Connector APIs
references/clips.md - Clips APIs
references/zoom-docs.md - Zoom docs and source references
Sample Repositories
Official (by Zoom)
Type	Repository
OAuth Sample	oauth-sample-app
S2S OAuth Starter	server-to-server-oauth-starter-api
User OAuth	user-level-oauth-starter
S2S Token	server-to-server-oauth-token
Rivet Library	rivet-javascript
WebSocket Sample	websocket-js-sample
Webhook Sample	webhook-sample-node.js
Python S2S	server-to-server-python-sample
Resources
API Reference: https://developers.zoom.us/api-hub/
GraphQL Playground: https://nws.zoom.us/graphql/playground
Postman Collection: https://marketplace.zoom.us/docs/api-reference/postman
Developer Forum: https://devforum.zoom.us/
Changelog: https://developers.zoom.us/changelog/
Status Page: https://status.zoom.us/

Need help? Start with Integrated Index section below for complete navigation.

Integrated Index

This section was migrated from SKILL.md.

Quick Start Path

If you're new to the Zoom REST API, follow this order:

Run preflight checks first → RUNBOOK.md

Understand the API design → concepts/api-architecture.md

Base URLs, regional endpoints, me keyword rules
Meeting ID vs UUID, double-encoding, time formats

Set up authentication → concepts/authentication-flows.md

Server-to-Server OAuth (backend automation)
User OAuth with PKCE (user-facing apps)
Cross-reference: zoom-oauth

Create your first meeting → examples/meeting-lifecycle.md

Full CRUD with curl and Node.js examples
Webhook event integration

Handle rate limits → concepts/rate-limiting-strategy.md

Plan-based limits, retry patterns, request queuing

Set up webhooks → examples/webhook-server.md

CRC validation, signature verification, event handling

Troubleshoot issues → troubleshooting/common-issues.md

Token refresh, pagination pitfalls, common gotchas
Documentation Structure
rest-api/
├── SKILL.md                              # Main skill overview + quick start
├── SKILL.md                              # This file - navigation guide
│
├── concepts/                             # Core architectural concepts
│   ├── api-architecture.md              # REST design, URLs, IDs, time formats
│   ├── authentication-flows.md          # OAuth flows (S2S, User, PKCE, Device)
│   └── rate-limiting-strategy.md        # Limits by plan, retry, queuing
│
├── examples/                             # Complete working code
│   ├── meeting-lifecycle.md             # Create→Update→Start→End→Delete
│   ├── user-management.md              # CRUD users, pagination, bulk ops
│   ├── recording-pipeline.md           # Download recordings via webhooks
│   ├── webhook-server.md               # Express.js CRC + signature verification
│   └── graphql-queries.md              # GraphQL queries, mutations, pagination
│
├── troubleshooting/                      # Problem solving
│   ├── common-errors.md                # HTTP codes, Zoom error codes table
│   └── common-issues.md               # Rate limits, tokens, pagination pitfalls
│
└── references/                           # 39 domain-specific reference files
    ├── authentication.md                # Auth methods reference
    ├── meetings.md                      # Meeting endpoints
    ├── users.md                         # User management endpoints
    ├── webinars.md                      # Webinar endpoints
    ├── recordings.md                    # Cloud recording endpoints
    ├── reports.md                       # Reports & analytics
    ├── accounts.md                      # Account management
    ├── rate-limits.md                   # Rate limit details
    ├── graphql.md                       # GraphQL API (beta)
    ├── zoom-team-chat.md                     # Team Chat messaging
    ├── chatbot.md                       # Chatbot integration
    ├── phone.md                         # Zoom Phone
    ├── rooms.md                         # Zoom Rooms
    ├── calendar.md                      # Zoom Calendar
    ├── mail.md                          # Zoom Mail
    ├── ai-companion.md                  # AI features
    ├── openapi.md                       # OpenAPI specs
    ├── qss.md                           # Quality of Service
    ├── contact-center.md                # Contact Center
    ├── events.md                        # Zoom Events
    ├── whiteboard.md                    # Whiteboard
    ├── clips.md                         # Zoom Clips
    ├── scheduler.md                     # Scheduler
    ├── scim2.md                         # SCIM 2.0
    ├── marketplace-apps.md              # App management
    ├── zoom-video-sdk-api.md                 # Video SDK REST
    └── ... (39 total files)

By Use Case
I want to create and manage meetings
API Architecture - Base URL, time formats
Meeting Lifecycle - Full CRUD + webhook events
Meetings Reference - All endpoints, types, settings
I want to manage users programmatically
User Management - CRUD, pagination, bulk ops
Users Reference - Endpoints, user types, scopes
I want to download recordings automatically
Recording Pipeline - Webhook-triggered downloads
Recordings Reference - File types, download auth
I want to receive real-time events
Webhook Server - CRC validation, signature check
Cross-reference: zoom-webhooks for comprehensive webhook docs
Cross-reference: zoom-websockets for WebSocket events
I want to use GraphQL instead of REST
GraphQL Queries - Queries, mutations, pagination
GraphQL Reference - Available entities, scopes, rate limits
I want to set up authentication
Authentication Flows - All OAuth methods
Cross-reference: zoom-oauth for full OAuth implementation
I'm hitting rate limits
Rate Limiting Strategy - Limits by plan, strategies
Rate Limits Reference - Detailed tables
Common Issues - Practical solutions
I'm getting errors
Common Errors - Error code tables
Common Issues - Diagnostic workflow
I want to build webinars
Webinars Reference - Endpoints, types, registrants
Meeting Lifecycle - Similar patterns apply
I want to integrate Zoom Phone
Phone Reference - Phone API endpoints
Rate Limiting Strategy - Separate Phone rate limits
Most Critical Documents
1. API Architecture (FOUNDATION)

concepts/api-architecture.md

Essential knowledge before making any API call:

Base URLs and regional endpoints
The me keyword rules (different per app type!)
Meeting ID vs UUID double-encoding
ISO 8601 time formats (UTC vs local)
Download URL authentication
2. Rate Limiting Strategy (MOST COMMON PRODUCTION ISSUE)

concepts/rate-limiting-strategy.md

Rate limits are per-account, shared across all apps:

Free: 4/sec Light, 2/sec Medium, 1/sec Heavy
Pro: 30/sec Light, 20/sec Medium, 10/sec Heavy
Business+: 80/sec Light, 60/sec Medium, 40/sec Heavy
Per-user: 100 meeting create/update per day
3. Meeting Lifecycle (MOST COMMON TASK)

examples/meeting-lifecycle.md

Complete CRUD with webhook integration — the pattern most developers need first.

Key Learnings
Critical Discoveries:

JWT app type is deprecated — use Server-to-Server OAuth

The JWT app type on Marketplace is deprecated, NOT JWT token signatures
See: Authentication Flows

me keyword behaves differently by app type

User OAuth: MUST use me
S2S OAuth: MUST NOT use me
See: API Architecture

Rate limiting is nuanced (don’t assume a single global rule)

Limits can vary by endpoint and may be enforced at account/app/user levels
Treat quotas as potentially shared across your account and implement backoff
Monitor rate limit response headers (for example X-RateLimit-Remaining)
See: Rate Limiting Strategy

100 meeting creates per user per day

This is a hard per-user limit, not related to rate limits
Distribute across host users for bulk operations
See: Rate Limiting Strategy

UUID double-encoding is required for certain UUIDs

UUIDs starting with / or containing // must be double-encoded
See: API Architecture

Pagination: use next_page_token, not page_number

page_number is legacy and being phased out
next_page_token is the recommended approach
See: Common Issues

GraphQL is at /v3/graphql, not /v2/

Single endpoint, cursor-based pagination
Rate limits apply per-field (each field = one REST equivalent)
See: GraphQL Queries
Quick Reference
"401 Unauthorized"

→ Authentication Flows - Token expired or wrong scopes

"429 Too Many Requests"

→ Rate Limiting Strategy - Check headers for reset time

"Invalid token" when using userId

→ API Architecture - User OAuth apps must use me

"How do I paginate results?"

→ Common Issues - Use next_page_token

"Webhooks not arriving"

→ Webhook Server - CRC validation required

"Recording download fails"

→ Recording Pipeline - Bearer auth + follow redirects

"How do I create a meeting?"

→ Meeting Lifecycle - Full working examples

Related Skills
Skill	Use When
zoom-oauth	Implementing OAuth flows, token management
zoom-webhooks	Deep webhook implementation, event catalog
zoom-websockets	WebSocket event streaming
zoom-general	Cross-product patterns, community repos

Based on Zoom REST API v2 (current) and GraphQL v3 (beta)

Environment Variables
See references/environment-variables.md for standardized .env keys and where to find each value.
Weekly Installs
299
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn