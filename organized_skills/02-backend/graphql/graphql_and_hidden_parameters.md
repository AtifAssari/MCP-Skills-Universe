---
rating: ⭐⭐
title: graphql-and-hidden-parameters
url: https://skills.sh/yaklang/hack-skills/graphql-and-hidden-parameters
---

# graphql-and-hidden-parameters

skills/yaklang/hack-skills/graphql-and-hidden-parameters
graphql-and-hidden-parameters
Installation
$ npx skills add https://github.com/yaklang/hack-skills --skill graphql-and-hidden-parameters
SKILL.md
SKILL: GraphQL and Hidden Parameters — Introspection, Batching, and Undocumented Fields

AI LOAD INSTRUCTION: Use this skill when GraphQL exists or when REST documentation suggests optional, deprecated, or undocumented fields. Focus on schema discovery, hidden parameter abuse, and batching as a force multiplier.

1. GRAPHQL FIRST PASS
query { __typename }
query {
  __schema {
    types { name }
  }
}


If introspection is restricted, continue with:

field suggestions and error-based discovery
known type probes like __type(name: "User")
JS and mobile bundle route extraction
2. HIGH-VALUE GRAPHQL TESTS
Theme	Example
IDOR	user(id: "victim")
batching	array of login or object fetch operations
hidden fields	admin-only fields exposed in type definitions
nested authz gaps	related object fields with weaker checks
3. HIDDEN PARAMETER DISCOVERY

Look for:

fields present in admin docs but not public docs
additionalProperties or permissive schemas
frontend code using richer request bodies than visible UI controls
mobile endpoints carrying role, org, feature-flag, or internal filter fields
4. NEXT ROUTING
If hidden fields affect privilege: api authorization and bola
If GraphQL batching changes auth or rate behavior: api auth and jwt abuse
If endpoint discovery is incomplete: api recon and docs
Weekly Installs
319
Repository
yaklang/hack-skills
GitHub Stars
368
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn