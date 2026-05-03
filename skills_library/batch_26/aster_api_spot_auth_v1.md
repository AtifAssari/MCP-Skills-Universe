---
title: aster-api-spot-auth-v1
url: https://skills.sh/asterdex/aster-skills-hub/aster-api-spot-auth-v1
---

# aster-api-spot-auth-v1

skills/asterdex/aster-skills-hub/aster-api-spot-auth-v1
aster-api-spot-auth-v1
Installation
$ npx skills add https://github.com/asterdex/aster-skills-hub --skill aster-api-spot-auth-v1
SKILL.md
Aster Spot API Authentication (v1)

Base: https://sapi.asterdex.com. Path prefix: /api/v1/. API key + secret case sensitive. Signed: send timestamp, signature; optional recvWindow (default 5000 ms, keep ≤ 5000).

Param	Description
X-MBX-APIKEY	API key (header)
timestamp	Current time, ms
recvWindow	Request valid this long after timestamp
signature	HMAC SHA256(totalParams, secretKey), hex

Signature: Same as aster-api-auth-v1: totalParams = query + body; HMAC SHA256(secretKey, totalParams) → hex; add signature to query or body; header X-MBX-APIKEY.

Timing: Server accepts if timestamp < serverTime+1000 and serverTime - timestamp <= recvWindow. Use GET /api/v1/time if clock skew.

Payload shapes: reference.md.

Weekly Installs
16
Repository
asterdex/aster-…ills-hub
GitHub Stars
68
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykFail