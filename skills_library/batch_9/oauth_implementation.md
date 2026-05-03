---
title: oauth-implementation
url: https://skills.sh/aj-geddes/useful-ai-prompts/oauth-implementation
---

# oauth-implementation

skills/aj-geddes/useful-ai-prompts/oauth-implementation
oauth-implementation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill oauth-implementation
SKILL.md
OAuth Implementation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement industry-standard OAuth 2.0 and OpenID Connect authentication flows with JWT tokens, refresh tokens, and secure session management.

When to Use
User authentication systems
Third-party API integration
Single Sign-On (SSO) implementation
Mobile app authentication
Microservices security
Social login integration
Quick Start

Minimal working example:

// oauth-server.js - Complete OAuth 2.0 implementation
const express = require("express");
const jwt = require("jsonwebtoken");
const crypto = require("crypto");
const bcrypt = require("bcrypt");

class OAuthServer {
  constructor() {
    this.app = express();
    this.clients = new Map();
    this.authorizationCodes = new Map();
    this.refreshTokens = new Map();
    this.accessTokens = new Map();

    // JWT signing keys
    this.privateKey = process.env.JWT_PRIVATE_KEY;
    this.publicKey = process.env.JWT_PUBLIC_KEY;

    this.setupRoutes();
  }

  // Register OAuth client
  registerClient(clientId, clientSecret, redirectUris) {
    this.clients.set(clientId, {
      clientSecret: bcrypt.hashSync(clientSecret, 10),
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Node.js OAuth 2.0 Server	Node.js OAuth 2.0 Server
Python OpenID Connect Implementation	Python OpenID Connect Implementation
Java Spring Security OAuth	Java Spring Security OAuth
Best Practices
✅ DO
Use PKCE for public clients
Implement token rotation
Store tokens securely
Use HTTPS everywhere
Validate redirect URIs
Implement rate limiting
Use short-lived access tokens
Log authentication events
❌ DON'T
Store tokens in localStorage
Use implicit flow
Skip state parameter
Expose client secrets
Allow open redirects
Use weak signing keys
Weekly Installs
354
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass