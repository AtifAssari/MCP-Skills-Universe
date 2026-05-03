---
title: bkend-auth
url: https://skills.sh/popup-studio-ai/bkit-claude-code/bkend-auth
---

# bkend-auth

skills/popup-studio-ai/bkit-claude-code/bkend-auth
bkend-auth
Installation
$ npx skills add https://github.com/popup-studio-ai/bkit-claude-code --skill bkend-auth
SKILL.md
bkend.ai Authentication & Security Guide
Auth Methods
Method	Description
Email + Password	Email/password signup and login
Social (Google)	OAuth 2.0 social login
Social (GitHub)	OAuth 2.0 social login
Magic Link	Email link login (no password)
JWT Token Structure
Access Token: 1 hour validity
Refresh Token: 7 days validity
Auto-refresh: POST /v1/auth/refresh
Password Policy

8+ characters, uppercase + lowercase + numbers + special characters

MCP Auth Workflow

bkend MCP does NOT have dedicated auth tools. Use this workflow:

Search docs: search_docs with query "email signup" or "social login"
Get examples: search_docs with query "auth code examples"
Generate code: AI generates REST API code based on search results
Searchable Auth Docs
Doc ID	Content
3_howto_implement_auth	Signup, login, token management guide
6_code_examples_auth	Email, social, magic link code examples
Key Pattern
User: "Add social login"
  → search_docs(query: "social login implementation")
  → Returns auth guide with REST API patterns
  → AI generates social login code

REST Auth API (Core Endpoints)

For the complete endpoint list, use search_docs or check Live Reference.

Method	Endpoint	Description
POST	/v1/auth/email/signup	Sign up
POST	/v1/auth/email/signin	Sign in
GET	/v1/auth/me	Current user
POST	/v1/auth/refresh	Refresh token
POST	/v1/auth/signout	Sign out
GET/POST	/v1/auth/:provider/callback	Social login callback
POST	/v1/auth/password/reset/request	Password reset
POST	/v1/auth/password/reset/confirm	Confirm reset
POST	/v1/auth/password/change	Change password
GET	/v1/auth/sessions	List sessions
DELETE	/v1/auth/sessions/:sessionId	Remove session
DELETE	/v1/auth/withdraw	Delete account

Additional endpoints (MFA, invitations, user management): use search_docs or Live Reference.

RBAC (Role-Based Access Control)
Group	Description	Scope
admin	Full CRUD	All data
user	Authenticated user	Full read, own write
self	Owner only	createdBy-based
guest	Unauthenticated	Read only (usually)
RLS (Row Level Security)
Per-table row-level access control
4-level policies: admin/user/self/guest
Auto-filtering based on createdBy field
Session Management
Per-device session tracking
GET /v1/auth/sessions - List sessions
DELETE /v1/auth/sessions/:sessionId - Remove session
Official Documentation (Live Reference)

For the latest authentication documentation, use WebFetch:

Auth Overview: https://raw.githubusercontent.com/popup-studio-ai/bkend-docs/main/en/authentication/01-overview.md
MCP Auth Guide: https://raw.githubusercontent.com/popup-studio-ai/bkend-docs/main/en/mcp/06-auth-tools.md
Security: https://raw.githubusercontent.com/popup-studio-ai/bkend-docs/main/en/security/01-overview.md
Full TOC: https://raw.githubusercontent.com/popup-studio-ai/bkend-docs/main/SUMMARY.md
Weekly Installs
34
Repository
popup-studio-ai…ude-code
GitHub Stars
523
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn