---
title: vtex-io-service-paths-and-cdn
url: https://skills.sh/vtex/skills/vtex-io-service-paths-and-cdn
---

# vtex-io-service-paths-and-cdn

skills/vtex/skills/vtex-io-service-paths-and-cdn
vtex-io-service-paths-and-cdn
Installation
$ npx skills add https://github.com/vtex/skills --skill vtex-io-service-paths-and-cdn
SKILL.md
VTEX IO service paths and CDN behavior
When this skill applies

Use this skill when you define or change service.json routes for a VTEX IO backend and need the edge (CDN) to pass the right cookies and apply the right caching for that endpoint’s data.

Choosing between public, segment (/_v/segment/...), and private (/_v/private/...) path prefixes for a route
Setting Cache-Control (and related headers) on HTTP responses so public cache behavior matches data scope (anonymous vs segment vs authenticated shopper)
Explaining why a route does not receive vtex_session or vtex_segment cookies
Troubleshooting CloudFront or edge behavior when cookies are missing (see official troubleshooting)

Do not use this skill for:

Application-level LRU caches, VBase, or stale-while-revalidate orchestration → use vtex-io-application-performance
GraphQL field-level @cacheControl only → use vtex-io-graphql-api alongside this skill
Decision rules
Paths are declared in service.json under routes. The prefix you choose (/yourPath, /_v/segment/yourPath, /_v/private/yourPath) controls cookie forwarding and whether VTEX may cache the service response at the edge—see the Service path patterns table.
Public ({yourPath}): No guarantee the app receives request cookies. The edge may cache responses when possible. Use for non-user-specific data (e.g. static reference data that is safe to share across shoppers).
Segment (/_v/segment/{yourPath}): The app receives vtex_segment. The edge caches per segment. Use when the response depends on segment (currency, region, sales channel, etc.) but not on authenticated identity.
Private (/_v/private/{yourPath}): The app receives vtex_segment and vtex_session. The edge does not cache the service response. Use for identity- or session-scoped data (orders, addresses, profile).
Cache-Control on responses must align with classification: never signal CDN/shared cache for payloads that embed secrets, per-user data, or authorization decisions unless the contract is explicitly designed for that (e.g. immutable public assets). When in doubt, prefer private paths and no-store / private cache directives for shopper-specific JSON.
Read Sessions System overview for how cookies relate to paths and sessions.
Hard constraints
Constraint: Do not use a public or segment-cached path for private or auth-scoped payloads

Routes that return authenticated shopper data, PII, or authorization-sensitive JSON must not rely on public paths or edge-cached responses that could serve one user’s data to another.

Why this matters — The edge may cache or route without the session context you expect; misclassified data can leak across users or segments.

Detection — A route under a public path returns order history, addresses, tokens, or account-specific fields; or Cache-Control suggests long-lived public caching for such payloads.

Correct — Use /_v/private/... for the route (or a pattern that receives vtex_session), and set appropriate Cache-Control (e.g. private, no-store for JSON APIs that are not cacheable). Note: the path prefix (/_v/private/) controls CDN and cookie behavior; the "public": true field controls whether VTEX auth tokens are required to call the route—these are orthogonal.

{
  "routes": {
    "myOrders": {
      "path": "/_v/private/my-app/orders",
      "public": true
    }
  }
}


Wrong — Exposing GET /my-app/orders as a public path (no /_v/private/ or /_v/segment/ prefix) and returning per-user JSON while assuming the browser session is always visible to the service.

Preferred pattern
Classify the response (anonymous, segment, authenticated) before picking the path prefix.
Map to public / segment / private per Service path patterns.
Set response headers explicitly where the platform allows: align Cache-Control with the same classification (public immutable vs private vs no-store).
Document any path that must stay private for security or compliance so storefronts and BFFs do not link-cache it incorrectly.
Common failure modes
Assuming cookies on public routes — Services do not reliably receive vtex_session on public paths; identity logic fails intermittently.
Caching personalized JSON at the edge — Long max-age on user-specific responses without private path + correct cache policy.
Mixing concerns — One route returns both public catalog and private account data; split endpoints or use private + server-side auth checks.
Ignoring segment — Price or promo that varies by currency or segment is served on a public path and cached for the wrong segment.
Review checklist
 Is each route’s path prefix (public / /_v/segment / /_v/private) justified by cookie and Caching behavior in the official table?
 For shopper-specific or auth responses, is the route private (or otherwise protected) and not edge-cacheable inappropriately?
 Do Cache-Control (and related) headers match data sensitivity?
 Are parallel calls from the client using the correct path for each payload type?
Related skills
vtex-io-application-performance — Application performance (LRU, VBase, AppSettings, parallel fetches, tenant keys)
vtex-io-service-apps — service.json and Service entry
vtex-io-graphql-api — GraphQL cache and @cacheControl
headless-caching-strategy — Storefront / BFF caching
Reference
Service path patterns — Path formats, cookies, caching, use cases
Sessions System overview — vtex_segment, vtex_session, session behavior
App Development — VTEX IO app development hub
VTEX IO Engineering guidelines — Scalability and IO development practices
Weekly Installs
156
Repository
vtex/skills
GitHub Stars
25
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass