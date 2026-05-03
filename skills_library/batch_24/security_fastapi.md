---
title: security-fastapi
url: https://skills.sh/igorwarzocha/opencode-workflows/security-fastapi
---

# security-fastapi

skills/igorwarzocha/opencode-workflows/security-fastapi
security-fastapi
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill security-fastapi
SKILL.md

Security audit patterns for FastAPI applications covering authentication dependencies, CORS configuration, and middleware security.

Core Risks to Check
Missing Auth on Routes

FastAPI expects authentication/authorization via dependencies on routes or routers. If no Depends()/Security() usage exists, review every route for unintended public access.

from fastapi import Depends, Security

@app.get("/private")
async def private_route(user=Depends(get_current_user)):
    return {"ok": True}

@app.get("/scoped")
async def scoped_route(user=Security(get_current_user, scopes=["items"])):
    return {"ok": True}

API Key Schemes

If using API keys, SHOULD prefer header-based schemes (APIKeyHeader) and validate the key server-side.

from fastapi import Depends, FastAPI
from fastapi.security import APIKeyHeader

api_key = APIKeyHeader(name="x-api-key")

@app.get("/items")
async def read_items(key: str = Depends(api_key)):
    return {"key": key}

CORS: Avoid Wildcards with Credentials

Using allow_origins=["*"] excludes credentialed requests (cookies/Authorization). For authenticated browser clients, MUST explicitly list allowed origins.

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://app.example.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Host Header and HTTPS Enforcement

SHOULD use Starlette middleware to prevent host-header attacks and enforce HTTPS in production.

from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"])
app.add_middleware(HTTPSRedirectMiddleware)

Quick Audit Commands
# Detect FastAPI usage
rg -n "fastapi" pyproject.toml requirements*.txt

# Find routes
rg -n "@app\.(get|post|put|patch|delete)" . -g "*.py"

# Check for auth dependencies
rg -n "Depends\(|Security\(" . -g "*.py"

# CORS config and wildcards
rg -n "CORSMiddleware|allow_origins|allow_credentials" . -g "*.py"

# TrustedHost/HTTPS middleware
rg -n "TrustedHostMiddleware|HTTPSRedirectMiddleware" . -g "*.py"

Hardening Checklist
 All sensitive routes require Depends() or Security() auth dependencies
 API key schemes use headers (APIKeyHeader), not query params
 allow_origins is explicit when allow_credentials=True
 TrustedHostMiddleware configured for production domains
 HTTPSRedirectMiddleware enabled in production (or enforced by proxy)
Scripts
scripts/scan.sh - First-pass FastAPI security scan
Weekly Installs
57
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