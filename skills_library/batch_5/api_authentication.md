---
title: api-authentication
url: https://skills.sh/aj-geddes/useful-ai-prompts/api-authentication
---

# api-authentication

skills/aj-geddes/useful-ai-prompts/api-authentication
api-authentication
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill api-authentication
SKILL.md
API Authentication
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive authentication strategies for APIs including JWT tokens, OAuth 2.0, API keys, and session management with proper security practices.

When to Use
Securing API endpoints
Implementing user login/logout flows
Managing access tokens and refresh tokens
Integrating OAuth 2.0 providers
Protecting sensitive data
Implementing API key authentication
Quick Start

Minimal working example:

// Node.js JWT Implementation
const express = require('express');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');

const app = express();
const SECRET_KEY = process.env.JWT_SECRET || 'your-secret-key';
const REFRESH_SECRET = process.env.REFRESH_SECRET || 'your-refresh-secret';

// User login endpoint
app.post('/api/auth/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    // Find user in database
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    // Verify password
    const isValid = await bcrypt.compare(password, user.password);
    if (!isValid) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
JWT Authentication	JWT Authentication
OAuth 2.0 Implementation	OAuth 2.0 Implementation
API Key Authentication	API Key Authentication
Python Authentication Implementation	Python Authentication Implementation
Best Practices
✅ DO
Use HTTPS for all authentication
Store tokens securely (HttpOnly cookies)
Implement token refresh mechanism
Set appropriate token expiration times
Hash and salt passwords
Use strong secret keys
Validate tokens on every request
Implement rate limiting on auth endpoints
Log authentication attempts
Rotate secrets regularly
❌ DON'T
Store passwords in plain text
Send tokens in URL parameters
Use weak secret keys
Store sensitive data in JWT payload
Ignore token expiration
Disable HTTPS in production
Log sensitive tokens
Reuse API keys across services
Store credentials in code
Weekly Installs
338
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