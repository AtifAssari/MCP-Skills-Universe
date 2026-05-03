---
rating: ⭐⭐
title: configuring-oauth2-authorization-flow
url: https://skills.sh/mukul975/anthropic-cybersecurity-skills/configuring-oauth2-authorization-flow
---

# configuring-oauth2-authorization-flow

skills/mukul975/anthropic-cybersecurity-skills/configuring-oauth2-authorization-flow
configuring-oauth2-authorization-flow
Installation
$ npx skills add https://github.com/mukul975/anthropic-cybersecurity-skills --skill configuring-oauth2-authorization-flow
SKILL.md
Configuring OAuth 2.0 Authorization Flow
Overview

Configure secure OAuth 2.0 authorization flows including Authorization Code with PKCE, Client Credentials, and Device Authorization Grant. This skill covers flow selection, PKCE implementation, token lifecycle management, scope design, and alignment with OAuth 2.1 security requirements.

When to Use
When deploying or configuring configuring oauth2 authorization flow capabilities in your environment
When establishing security controls aligned to compliance requirements
When building or improving security architecture for this domain
When conducting security assessments that require this implementation
Prerequisites
Familiarity with identity access management concepts and tools
Access to a test or lab environment for safe execution
Python 3.8+ with required dependencies installed
Appropriate authorization for any testing activities
Objectives
Implement Authorization Code flow with PKCE for public and confidential clients
Configure Client Credentials flow for machine-to-machine communication
Design least-privilege scope hierarchies
Implement secure token storage, refresh, and revocation
Apply OAuth 2.1 best practices and RFC 9700 security recommendations
Validate token integrity and prevent common OAuth attacks
Key Concepts
OAuth 2.0 Grant Types
Authorization Code + PKCE: Recommended for all client types (web, mobile, SPA). PKCE is mandatory in OAuth 2.1.
Client Credentials: Machine-to-machine authentication without user context.
Device Authorization Grant (RFC 8628): For input-constrained devices (smart TVs, CLI tools).
Refresh Token: Long-lived token to obtain new access tokens without re-authentication.
PKCE (Proof Key for Code Exchange)

PKCE (RFC 7636) prevents authorization code interception attacks:

Client generates random code_verifier (43-128 characters, unreserved URI chars)
Client computes code_challenge = BASE64URL(SHA256(code_verifier))
Authorization request includes code_challenge and code_challenge_method=S256
Token request includes original code_verifier
Server validates SHA256(code_verifier) matches stored code_challenge
Token Types
Access Token: Short-lived (5-60 min), bearer or DPoP-bound
Refresh Token: Long-lived, single-use with rotation
ID Token (OIDC): JWT containing user identity claims
Workflow
Step 1: Authorization Code Flow with PKCE
Generate cryptographically random code_verifier (min 43 chars)
Compute code_challenge using S256 method
Redirect user to authorization endpoint with parameters:
response_type=code
client_id, redirect_uri, scope, state
code_challenge, code_challenge_method=S256
User authenticates and consents
Authorization server redirects with authorization code
Exchange code + code_verifier for tokens at token endpoint
Validate state parameter matches original value
Step 2: Scope Design
Define granular scopes: read:users, write:orders, admin:settings
Follow least-privilege: request minimum scopes needed
Implement scope validation on resource server
Document scope hierarchy and consent requirements
Step 3: Token Security
Store tokens securely (httpOnly cookies for web, keychain for mobile)
Implement token refresh with rotation (one-time-use refresh tokens)
Set appropriate expiration: access tokens 5-15 min, refresh tokens 8-24 hrs
Enable DPoP (Demonstration of Proof-of-Possession) for sender-constrained tokens
Implement token revocation endpoint
Step 4: Client Credentials Flow
Register service client with client_id and client_secret
Request token: POST /oauth/token with grant_type=client_credentials
Include scope for required permissions
Store client_secret securely (vault, env vars, not code)
Implement certificate-based client authentication for higher assurance
Step 5: Security Hardening
Enforce PKCE for all authorization code flows
Use exact redirect URI matching (no wildcards)
Implement CSRF protection with state parameter
Enable refresh token rotation and revocation on reuse detection
Apply RFC 9700 security best practices
Block implicit grant and ROPC (removed in OAuth 2.1)
Security Controls
Control	NIST 800-53	Description
Access Control	AC-3	Token-based access enforcement
Authentication	IA-5	Client credential management
Session Management	SC-23	Token lifecycle management
Audit	AU-3	Log all token issuance and revocation
Cryptographic Protection	SC-13	PKCE and token signing
Common Pitfalls
Using implicit grant (removed in OAuth 2.1) instead of authorization code + PKCE
Storing tokens in localStorage (XSS vulnerable) instead of httpOnly cookies
Not validating state parameter enabling CSRF attacks
Using wildcard redirect URIs allowing open redirect exploitation
Not implementing refresh token rotation allowing token theft persistence
Verification
 Authorization Code + PKCE flow completes successfully
 PKCE code_challenge validated at token endpoint
 State parameter prevents CSRF
 Access tokens expire within configured lifetime
 Refresh token rotation issues new refresh token each use
 Token revocation invalidates both access and refresh tokens
 Client Credentials flow works for service-to-service calls
 Scopes correctly enforced at resource server
Weekly Installs
26
Repository
mukul975/anthro…y-skills
GitHub Stars
5.9K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn