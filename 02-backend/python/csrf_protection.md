---
rating: ⭐⭐
title: csrf-protection
url: https://skills.sh/aj-geddes/useful-ai-prompts/csrf-protection
---

# csrf-protection

skills/aj-geddes/useful-ai-prompts/csrf-protection
csrf-protection
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill csrf-protection
SKILL.md
CSRF Protection
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive Cross-Site Request Forgery protection using synchronizer tokens, double-submit cookies, SameSite cookie attributes, and custom headers.

When to Use
Form submissions
State-changing operations
Authentication systems
Payment processing
Account management
Any POST/PUT/DELETE requests
Quick Start

Minimal working example:

// csrf-protection.js
const crypto = require("crypto");
const csrf = require("csurf");

class CSRFProtection {
  constructor() {
    this.tokens = new Map();
    this.tokenExpiry = 3600000; // 1 hour
  }

  /**
   * Generate CSRF token
   */
  generateToken() {
    return crypto.randomBytes(32).toString("hex");
  }

  /**
   * Create token for session
   */
  createToken(sessionId) {
    const token = this.generateToken();
    const expiry = Date.now() + this.tokenExpiry;

    this.tokens.set(sessionId, {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Node.js/Express CSRF Protection	Node.js/Express CSRF Protection
Double Submit Cookie Pattern	Double Submit Cookie Pattern
Python Flask CSRF Protection	Python Flask CSRF Protection
Frontend CSRF Implementation	Frontend CSRF Implementation
Origin and Referer Validation	Origin and Referer Validation
Best Practices
✅ DO
Use CSRF tokens for all state-changing operations
Set SameSite=Strict on cookies
Validate Origin/Referer headers
Use secure, random tokens
Implement token expiration
Use HTTPS only
Include tokens in AJAX requests
Test CSRF protection
❌ DON'T
Skip CSRF for authenticated requests
Use GET for state changes
Trust Origin header alone
Reuse tokens
Store tokens in localStorage
Allow credentials in CORS without validation
Weekly Installs
280
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