---
title: aster-api-errors-v1
url: https://skills.sh/asterdex/aster-skills-hub/aster-api-errors-v1
---

# aster-api-errors-v1

skills/asterdex/aster-skills-hub/aster-api-errors-v1
aster-api-errors-v1
Installation
$ npx skills add https://github.com/asterdex/aster-skills-hub --skill aster-api-errors-v1
SKILL.md
Aster API Errors (v1)

Payload: { "code": -1121, "msg": "..." }. Handle by code (stable); messages may vary.

Rate limits: From GET /fapi/v1/exchangeInfo → rateLimits. REQUEST_WEIGHT: per IP (e.g. 2400/min); header X-MBX-USED-WEIGHT-*. ORDERS: per account (e.g. 1200/min); header X-MBX-ORDER-COUNT-*. 429: back off. 418: IP banned (2 min–3 days). Prefer WebSocket to reduce REST load.

Security: -1021 INVALID_TIMESTAMP → recvWindow or clock; use GET /fapi/v1/time. -1022 INVALID_SIGNATURE → check HMAC/secret.

Range	Category	Examples
10xx	Server/network	-1000, -1001, -1003, -1007, -1015, -1021, -1022
11xx	Request/params	-1102, -1121, -1130
20xx	Processing	-2010, -2011, -2013, -2018, -2019, -2021, -2025
40xx	Filters	-4004, -4014, -4023, -4047, -4048, -4164

HTTP: 4XX = client (403 WAF, 429, 418); 5XX = server. 503 = may have been processed—do not assume failure.

Payload shapes: reference.md.

Weekly Installs
17
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