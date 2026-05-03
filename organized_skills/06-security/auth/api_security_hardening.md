---
rating: ⭐⭐
title: api-security-hardening
url: https://skills.sh/aj-geddes/useful-ai-prompts/api-security-hardening
---

# api-security-hardening

skills/aj-geddes/useful-ai-prompts/api-security-hardening
api-security-hardening
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill api-security-hardening
Summary

Comprehensive security middleware for REST APIs covering authentication, rate limiting, input validation, and attack prevention.

Implements multiple security layers: helmet for HTTP headers, rate limiting, CORS configuration, input sanitization, and XSS/HPP protection
Supports Node.js/Express and Python FastAPI with reference implementations for each framework
Includes JWT-based authentication, input validation with sanitization, and security event logging
Provides best practices guidance covering HTTPS enforcement, error handling, API versioning, and common vulnerability prevention
SKILL.md
API Security Hardening
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive API security measures including authentication, authorization, rate limiting, input validation, and attack prevention to protect against common vulnerabilities.

When to Use
New API development
Security audit remediation
Production API hardening
Compliance requirements
High-traffic API protection
Public API exposure
Quick Start

Minimal working example:

// secure-api.js - Comprehensive API security
const express = require("express");
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");
const mongoSanitize = require("express-mongo-sanitize");
const xss = require("xss-clean");
const hpp = require("hpp");
const cors = require("cors");
const jwt = require("jsonwebtoken");
const validator = require("validator");

class SecureAPIServer {
  constructor() {
    this.app = express();
    this.setupSecurityMiddleware();
    this.setupRoutes();
  }

  setupSecurityMiddleware() {
    // 1. Helmet - Set security headers
    this.app.use(
      helmet({
        contentSecurityPolicy: {
          directives: {
            defaultSrc: ["'self'"],
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Node.js/Express API Security	Node.js/Express API Security
Python FastAPI Security	Python FastAPI Security
API Gateway Security Configuration	API Gateway Security Configuration
Best Practices
✅ DO
Use HTTPS everywhere
Implement rate limiting
Validate all inputs
Use security headers
Log security events
Implement CORS properly
Use strong authentication
Version your APIs
❌ DON'T
Expose stack traces
Return detailed errors
Trust user input
Use HTTP for APIs
Skip input validation
Ignore rate limiting
Weekly Installs
516
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