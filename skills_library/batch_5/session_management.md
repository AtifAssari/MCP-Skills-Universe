---
title: session-management
url: https://skills.sh/aj-geddes/useful-ai-prompts/session-management
---

# session-management

skills/aj-geddes/useful-ai-prompts/session-management
session-management
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill session-management
SKILL.md
Session Management
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive session management systems with secure token handling, session persistence, token refresh mechanisms, proper logout procedures, and CSRF protection across different backend frameworks.

When to Use
Implementing user authentication systems
Managing session state and user context
Handling JWT token refresh cycles
Implementing logout functionality
Protecting against CSRF attacks
Managing session expiration and cleanup
Quick Start

Minimal working example:

# Python/Flask Example
from flask import current_app
from datetime import datetime, timedelta
import jwt
import os

class TokenManager:
    def __init__(self, secret_key=None):
        self.secret_key = secret_key or os.getenv('JWT_SECRET')
        self.algorithm = 'HS256'
        self.access_token_expires_hours = 1
        self.refresh_token_expires_days = 7

    def generate_tokens(self, user_id, email, role='user'):
        """Generate both access and refresh tokens"""
        now = datetime.utcnow()

        # Access token
        access_payload = {
            'user_id': user_id,
            'email': email,
            'role': role,
            'type': 'access',
            'iat': now,
            'exp': now + timedelta(hours=self.access_token_expires_hours)
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
JWT Token Generation and Validation	JWT Token Generation and Validation
Node.js/Express JWT Implementation	Node.js/Express JWT Implementation
Session Storage with Redis	Session Storage with Redis
CSRF Protection	CSRF Protection
Session Middleware Chain	Session Middleware Chain
Token Refresh Endpoint	Token Refresh Endpoint
Session Cleanup and Maintenance	Session Cleanup and Maintenance
Best Practices
✅ DO
Use HTTPS for all session transmission
Implement secure cookies (httpOnly, sameSite, secure flags)
Use JWT with proper expiration times
Implement token refresh mechanism
Store refresh tokens securely
Validate tokens on every request
Use strong secret keys
Implement session timeout
Log authentication events
Clear session data on logout
Use CSRF tokens for state-changing requests
❌ DON'T
Store sensitive data in tokens
Use short secret keys
Transmit tokens in URLs
Ignore token expiration
Reuse token secrets across environments
Store tokens in localStorage (use httpOnly cookies)
Implement session without HTTPS
Forget to validate token signatures
Expose session IDs in logs
Use predictable session IDs
Weekly Installs
284
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass