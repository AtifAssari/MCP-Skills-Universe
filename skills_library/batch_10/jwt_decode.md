---
title: jwt-decode
url: https://skills.sh/jsonwebtoken/jwt-skills/jwt-decode
---

# jwt-decode

skills/jsonwebtoken/jwt-skills/jwt-decode
jwt-decode
Installation
$ npx skills add https://github.com/jsonwebtoken/jwt-skills --skill jwt-decode
SKILL.md
JWT Decode

Decode a JWT by base64url-decoding its header and payload. Does NOT verify signatures — use jwt-validate for that.

Steps
Split the token on . into three parts (header, payload, signature).
Base64url-decode and parse parts 1 and 2 as JSON.
Display header, payload (with all claims), and the raw signature string.
For exp, nbf, iat — show both the Unix timestamp and human-readable UTC. If exp is past, note expired and by how long.
Run security checks (see below).
Output Format
## Header
{ "alg": "RS256", "typ": "JWT", "kid": "abc123" }

## Payload
{ "iss": "https://auth.example.com/", "sub": "user|12345", "exp": 1735689600 }

exp: 2025-01-01T00:00:00Z — EXPIRED (3 months ago)
iat: 2024-12-31T00:00:00Z

## Signature
Algorithm: RS256 | Signature: [base64url string]
(Not verified — use jwt-validate to verify)

Security Checks

Flag these prominently when found:

alg: none — Token is unsigned. Warn: "This token has no signature and cannot be trusted. Any party could have created or modified it." This is a known attack vector (CVE-2015-9235) where attackers strip signatures to bypass verification.
Sensitive data in payload — JWTs are encoded, not encrypted. Warn if you spot passwords, secrets, API keys, or PII in claims.
Missing exp — Token never expires. Flag as a security risk.
jku/jwk/x5u in header — These can be used to trick verifiers into fetching attacker-controlled keys. Flag if present.
Notes
If cty header is "JWT", the payload is a nested JWT — decode recursively.
On decode failure, report the specific error (malformed base64, invalid JSON, wrong segment count).
This skill only reveals token contents — it says nothing about authenticity. Direct users to jwt-validate for verification.
Weekly Installs
111
Repository
jsonwebtoken/jwt-skills
GitHub Stars
2
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail