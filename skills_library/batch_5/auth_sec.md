---
title: auth-sec
url: https://skills.sh/yaklang/hack-skills/auth-sec
---

# auth-sec

skills/yaklang/hack-skills/auth-sec
auth-sec
Installation
$ npx skills add https://github.com/yaklang/hack-skills --skill auth-sec
SKILL.md
Authentication and Authorization Router

This is the routing entry point for authentication, sessions, and authorization boundaries.

Use it to decide whether the issue is mainly login mechanics, object-level authorization, browser trust boundaries, or identity protocols such as OAuth/JWT/SAML before going deeper.

When to Use
The target includes login, registration, password reset, 2FA, sessions, JWT, OAuth, or SSO
You suspect object authorization flaws, cross-tenant access, cross-origin reads, CSRF, or protocol misconfiguration
You need to decide whether to test authentication or authorization first
Skill Map
Authentication Bypass: login bypass, password reset, 2FA, enumeration, brute-force protections
IDOR Broken Object Authorization: IDOR, BOLA, BFLA, missing object permissions
JWT OAuth Token Attacks: algorithm confusion, key trust issues, claim abuse, token forgery
OAuth OIDC Misconfiguration: redirect URI, state, nonce, PKCE, account binding
CSRF Cross Site Request Forgery: CSRF tokens, SameSite, JSON CSRF, login CSRF
CORS Cross Origin Misconfiguration: reflected Origin, credentialed cross-origin reads, allowlist bypass
SAML SSO Assertion Attacks: assertion wrapping, signature validation, audience, ACS boundaries
Recommended Flow
First confirm the authentication model and session boundaries
Then confirm object-level and function-level authorization
Then move to token, cross-origin, and protocol details
If enterprise federation exists, continue with OAuth, OIDC, or SAML topics
Related Categories
api-sec
Default credentials, username variants, wordlist sizing, and port focus are consolidated in authbypass-authentication-flaws
Weekly Installs
335
Repository
yaklang/hack-skills
GitHub Stars
368
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass