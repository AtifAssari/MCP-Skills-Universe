---
title: reverse-engineer
url: https://skills.sh/pv-udpv/pplx-sdk/reverse-engineer
---

# reverse-engineer

skills/pv-udpv/pplx-sdk/reverse-engineer
reverse-engineer
Installation
$ npx skills add https://github.com/pv-udpv/pplx-sdk --skill reverse-engineer
SKILL.md
Reverse Engineering Perplexity AI APIs

Discover, document, and implement undocumented Perplexity AI endpoints for pplx-sdk.

When to use

Use this skill when:

Discovering new API endpoints from perplexity.ai browser traffic
Decoding request/response payloads from captured cURL commands
Mapping SSE event types from streaming endpoints
Extracting auth flows (cookies, tokens, session management)
Adding new endpoint support to the SDK
Instructions
Step 1: Capture Traffic
DevTools (F12) → Network → XHR/Fetch
1. Perform action on perplexity.ai
2. Right-click request → Copy as cURL
3. Paste cURL for analysis

Step 2: Decode Payload

Extract from the captured request:

URL path (e.g., /rest/sse/perplexity.ask)
Method (GET, POST, PUT, DELETE)
Auth (Bearer token from cookie pplx.session-id)
Request body (JSON payload with field names and types)
Response format (JSON, SSE stream, etc.)
Step 3: Document Schema

For each field in the payload:

Name, type, required/optional, default value
What it controls (e.g., mode: "concise" = shorter answers)
Discovered values (e.g., model_preference = "pplx-70b-chat" | "pplx-70b-deep")
Step 4: Map to SDK Architecture
Discovery	Target	Action
New endpoint	transport/	Add endpoint constant and method
Request fields	domain/models.py	Create Pydantic request model
Response fields	domain/models.py	Create Pydantic response model
SSE events	transport/sse.py	Add event type to parser
Auth variation	shared/auth.py	Add extraction method
Error codes	core/exceptions.py	Map to exception type
Step 5: Implement

Create the SDK implementation following the layered architecture:

Model in domain/models.py
Service in domain/<service>.py
Tests in tests/test_<service>.py
Known API Surface
Implemented
POST /rest/sse/perplexity.ask — Main query endpoint (SSE streaming)
Discovered (not yet implemented)
Thread management (/rest/threads/)
Collections (/rest/collections/)
User profile (/rest/user/)
File upload (/rest/upload)
Sharing (/rest/share/)
Anti-Detection Notes
Use realistic User-Agent headers matching Chrome/Safari
Include Referer: https://www.perplexity.ai/ and Origin headers
Consider TLS fingerprinting via curl_cffi with impersonate="chrome120"
Rate limit requests to avoid detection
Weekly Installs
18
Repository
pv-udpv/pplx-sdk
First Seen
Feb 8, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykFail