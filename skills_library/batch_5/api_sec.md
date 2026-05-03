---
title: api-sec
url: https://skills.sh/yaklang/hack-skills/api-sec
---

# api-sec

skills/yaklang/hack-skills/api-sec
api-sec
Installation
$ npx skills add https://github.com/yaklang/hack-skills --skill api-sec
SKILL.md
API Security Router

This is the routing entry point for API security testing.

Use this skill first to decide whether the API issue is mostly recon/docs, object authorization, token trust, or GraphQL/hidden parameters, then route to a deeper topic skill.

When to Use
The target exposes REST APIs, mobile backends, or GraphQL endpoints
You need to define API testing order before going into specific topics
You want to handle object authorization, JWT, GraphQL, and hidden fields as separate tracks
Skill Map
API Recon and Docs: OpenAPI, Swagger, version drift, hidden documentation
API Authorization and BOLA: BOLA, BFLA, method abuse, hidden writable fields
API Auth and JWT Abuse: bearer token, header trust, claim abuse, rate-limit bypass
GraphQL and Hidden Parameters: introspection, batching, undocumented fields, hidden parameters
Quick Triage
Observation	Route
Swagger or OpenAPI is present	api-recon-and-docs
IDs appear in URL, JSON, headers, or GraphQL args	api-authorization-and-bola
JWT token visible in traffic	api-auth-and-jwt-abuse
/graphql or batched JSON arrays are present	graphql-and-hidden-parameters
Registration, login, or profile updates accept extra fields	api-authorization-and-bola then api-auth-and-jwt-abuse
Recommended Flow
Start with exposed endpoints and documentation assets
Then evaluate object-level and function-level authorization
Then evaluate token, header, signature, and rate-limit boundaries
If GraphQL or complex JSON is present, continue with hidden fields and schema abuse
Related Categories
auth-sec
business-logic-vuln
recon-for-sec
Weekly Installs
340
Repository
yaklang/hack-skills
GitHub Stars
368
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass