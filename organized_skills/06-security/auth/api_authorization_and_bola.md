---
rating: ⭐⭐
title: api-authorization-and-bola
url: https://skills.sh/yaklang/hack-skills/api-authorization-and-bola
---

# api-authorization-and-bola

skills/yaklang/hack-skills/api-authorization-and-bola
api-authorization-and-bola
Installation
$ npx skills add https://github.com/yaklang/hack-skills --skill api-authorization-and-bola
SKILL.md
SKILL: API Authorization and BOLA — Object Access, Function Access, and Mass Assignment

AI LOAD INSTRUCTION: Use this skill when an API exposes object IDs, nested resources, or role-sensitive functions and you need a focused authorization test path: BOLA, BFLA, method abuse, and hidden field control.

1. CORE TEST LOOP
Create Account A and Account B.
As Account A, capture create, read, update, and delete flows.
Replay with Account B's token.
Test sibling endpoints, nested endpoints, and alternate HTTP verbs.
2. TEST SURFACES
Surface	Example
object read	/api/v1/orders/123
nested object	/api/v1/users/1/invoices/9
admin or internal function	/api/v1/admin/users
update path	PUT, PATCH, DELETE variants
hidden JSON fields	role, org, verified, tier
3. QUICK PAYLOADS
{"role":"admin"}
{"isAdmin":true}
{"org":"target-company"}
{"verified":true}

4. WHAT TESTERS MISS
object IDs in headers, cookies, GraphQL args, and nested objects
alternate methods sharing the same route but weaker authz
parent check present, child resource check missing
admin docs revealing extra writable fields
5. NEXT ROUTING
For JWT or token-layer abuse: api auth and jwt abuse
For GraphQL and hidden parameter discovery: graphql and hidden parameters
For broader IDOR patterns outside APIs: idor broken object authorization
Weekly Installs
329
Repository
yaklang/hack-skills
GitHub Stars
368
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass