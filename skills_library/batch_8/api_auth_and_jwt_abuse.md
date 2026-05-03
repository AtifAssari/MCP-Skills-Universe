---
title: api-auth-and-jwt-abuse
url: https://skills.sh/yaklang/hack-skills/api-auth-and-jwt-abuse
---

# api-auth-and-jwt-abuse

skills/yaklang/hack-skills/api-auth-and-jwt-abuse
api-auth-and-jwt-abuse
Installation
$ npx skills add https://github.com/yaklang/hack-skills --skill api-auth-and-jwt-abuse
SKILL.md
SKILL: API Auth and JWT Abuse — Token Trust, Header Tricks, and Rate Limits

AI LOAD INSTRUCTION: Use this skill when APIs rely on JWT, bearer tokens, API keys, or weak request identity signals. Focus on token trust boundaries, claim misuse, header spoofing, and rate-limit bypass.

1. TOKEN TRIAGE

Inspect:

alg, kid, jku, x5u
role, org, tenant, scope, or privilege claims
issuer and audience mismatches
reuse of mobile and web tokens across products
2. QUICK ATTACK PICKS
Pattern	First Test
alg:none acceptance	unsigned token with trailing dot
RS256 confusion	switch to HS256 using public key as secret
kid lookup trust	path traversal or injection in kid
remote key fetch trust	attacker-controlled jku or x5u
weak secret	offline crack with targeted wordlists
3. HIDDEN FIELDS AND BATCH ABUSE
Mass assignment field picks
role
isAdmin
admin
verified
plan
tier
permissions
org
owner

Rate limit and batch abuse picks
X-Forwarded-For: 1.2.3.4
X-Real-IP: 5.6.7.8
Forwarded: for=9.9.9.9


GraphQL or JSON batch abuse candidates:

arrays of login mutations
bulk object fetches with varying IDs
repeated password reset or verification calls in one request
4. RATE LIMIT BYPASS FAMILIES
X-Forwarded-For
X-Real-IP
Forwarded
User-Agent rotation
Path case / slash variants

5. NEXT ROUTING
For GraphQL batching and hidden parameters: graphql and hidden parameters
For default credential and brute-force planning: authentication bypass
For full JWT and OAuth depth: jwt oauth token attacks
For OAuth or OIDC configuration flaws in browser and SSO flows: oauth oidc misconfiguration
For credentialed browser reads and origin trust bugs: cors cross origin misconfiguration
Weekly Installs
337
Repository
yaklang/hack-skills
GitHub Stars
368
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail