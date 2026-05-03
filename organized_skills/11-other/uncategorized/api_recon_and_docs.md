---
rating: ⭐⭐
title: api-recon-and-docs
url: https://skills.sh/yaklang/hack-skills/api-recon-and-docs
---

# api-recon-and-docs

skills/yaklang/hack-skills/api-recon-and-docs
api-recon-and-docs
Installation
$ npx skills add https://github.com/yaklang/hack-skills --skill api-recon-and-docs
SKILL.md
SKILL: API Recon and Docs — Endpoints, Schemas, and Version Surface

AI LOAD INSTRUCTION: Use this skill first when the target is a REST, mobile, or GraphQL API and you need to enumerate endpoints, documentation, versions, and hidden surface area before exploitation.

1. PRIMARY GOALS
Discover all reachable API entrypoints.
Extract schemas, optional fields, and role differences.
Identify old versions, mobile paths, GraphQL endpoints, and undocumented parameters.
2. RECON CHECKLIST
JavaScript and client mining
curl https://target/app.js | grep -oE '(/api|/rest|/graphql)[^"'\'' ]+' | sort -u

Common documentation and schema paths
/swagger.json
/openapi.json
/api-docs
/docs
/.well-known/
/graphql
/gql

Version and product drift
/api/v1/
/api/v2/
/api/mobile/v1/
/legacy/

3. WHAT TO EXTRACT FROM DOCS
optional and undocumented fields
admin-only request examples
deprecated endpoints that may still be active
schema hints like additionalProperties: true
parameter names tied to filtering, sorting, IDs, roles, or tenancy
4. NEXT ROUTING
Finding	Next Skill
object IDs everywhere	api authorization and bola
JWT, OAuth, role claims	api auth and jwt abuse
GraphQL or hidden fields	graphql and hidden parameters
strong auth boundary but suspicious business flow	business logic vulnerabilities
Weekly Installs
334
Repository
yaklang/hack-skills
GitHub Stars
368
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn