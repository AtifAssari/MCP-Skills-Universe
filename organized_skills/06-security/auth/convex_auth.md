---
rating: ⭐⭐
title: convex-auth
url: https://skills.sh/igorwarzocha/opencode-workflows/convex-auth
---

# convex-auth

skills/igorwarzocha/opencode-workflows/convex-auth
convex-auth
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill convex-auth
SKILL.md
Auth Operations
In functions: ctx.auth.getUserIdentity() returns tokenIdentifier, subject, issuer plus provider claims.
Custom JWT auth MAY expose claims at identity["properties.email"] style paths.
User storage patterns:
Client mutation to store user from JWT, or webhook from provider to upsert users.
Index lookups SHOULD use by_token / byExternalId.
Webhooks: You MUST implement via HTTP actions and verify signatures with provider SDK; signing secrets MUST be stored in env vars.
Convex Auth (Beta) Specifics
Supported Methods:
Magic Links & OTPs: Email-based links or codes.
OAuth: GitHub, Google, Apple, etc.
Passwords: Supports reset flows and optional email verification.
Components: Does not provide UI components; You MUST build them in React using library hooks.
Next.js: SSR/Middleware support is experimental/beta.
Server Function Patterns
You MUST read identity via ctx.auth.getUserIdentity().
You MUST enforce row-level authorization in every public function.
You SHOULD NOT expose sensitive logic via public functions; prefer internal ones.
Service-to-service Access
If no user JWT is available, You SHOULD use a shared secret pattern.
You MUST store secrets in deployment env vars; MUST NOT hardcode.
Client Guidance
You MUST follow provider quickstarts; MUST NOT invent flows.
You SHOULD NOT rely on auth data in client-only code without server verification.
Weekly Installs
59
Repository
igorwarzocha/op…orkflows
GitHub Stars
111
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass