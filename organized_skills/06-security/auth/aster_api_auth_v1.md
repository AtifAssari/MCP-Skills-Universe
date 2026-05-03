---
rating: ⭐⭐
title: aster-api-auth-v1
url: https://skills.sh/asterdex/aster-skills-hub/aster-api-auth-v1
---

# aster-api-auth-v1

skills/asterdex/aster-skills-hub/aster-api-auth-v1
aster-api-auth-v1
Installation
$ npx skills add https://github.com/asterdex/aster-skills-hub --skill aster-api-auth-v1
SKILL.md
Aster API Authentication (v1)

Base: https://fapi.asterdex.com. API key + secret case sensitive. Signed: send timestamp, signature; optional recvWindow (default 5000 ms, keep ≤ 5000).

Param	Description
X-MBX-APIKEY	API key (header)
timestamp	Current time, ms
recvWindow	Request valid this long after timestamp
signature	HMAC SHA256(totalParams, secretKey), hex

Signature: (1) totalParams = query + body (no & between; GET = query only; POST/PUT/DELETE = query + body as sent). (2) HMAC SHA256(secretKey, totalParams) → hex. (3) Add signature to query or body (last param); header X-MBX-APIKEY. Signature not case sensitive.

Timing: Server accepts if timestamp < serverTime+1000 and serverTime - timestamp <= recvWindow. Use GET /fapi/v1/time if clock skew. Security: Env vars for key/secret; keys can be restricted (TRADE-only etc.).

Payload shapes: reference.md.

Weekly Installs
19
Repository
asterdex/aster-…ills-hub
GitHub Stars
68
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn