---
title: security-headers-configuration
url: https://skills.sh/aj-geddes/useful-ai-prompts/security-headers-configuration
---

# security-headers-configuration

skills/aj-geddes/useful-ai-prompts/security-headers-configuration
security-headers-configuration
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill security-headers-configuration
SKILL.md
Security Headers Configuration
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive HTTP security headers to protect web applications from XSS, clickjacking, MIME sniffing, and other browser-based attacks.

When to Use
New web application deployment
Security audit remediation
Compliance requirements
Browser security hardening
API security
Static site protection
Quick Start

Minimal working example:

// security-headers.js
const helmet = require("helmet");

function configureSecurityHeaders(app) {
  // Comprehensive Helmet configuration
  app.use(
    helmet({
      // Content Security Policy
      contentSecurityPolicy: {
        directives: {
          defaultSrc: ["'self'"],
          scriptSrc: [
            "'self'",
            "'unsafe-inline'", // Remove in production
            "https://cdn.example.com",
            "https://www.google-analytics.com",
          ],
          styleSrc: [
            "'self'",
            "'unsafe-inline'",
            "https://fonts.googleapis.com",
          ],
          fontSrc: ["'self'", "https://fonts.gstatic.com"],
          imgSrc: ["'self'", "data:", "https:", "blob:"],
          connectSrc: ["'self'", "https://api.example.com"],
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Node.js/Express Security Headers	Node.js/Express Security Headers
Nginx Security Headers Configuration	Nginx Security Headers Configuration
Python Flask Security Headers	Python Flask Security Headers
Apache .htaccess Configuration	Apache .htaccess Configuration
Security Headers Testing Script	Security Headers Testing Script
Best Practices
✅ DO
Use HTTPS everywhere
Implement strict CSP
Enable HSTS with preload
Block framing with X-Frame-Options
Prevent MIME sniffing
Report CSP violations
Test headers regularly
Use security scanners
❌ DON'T
Allow unsafe-inline in CSP
Skip HSTS on subdomains
Ignore CSP violations
Use overly permissive policies
Forget to test changes
Weekly Installs
306
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn