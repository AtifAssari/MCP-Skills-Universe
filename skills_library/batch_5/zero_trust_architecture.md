---
title: zero-trust-architecture
url: https://skills.sh/aj-geddes/useful-ai-prompts/zero-trust-architecture
---

# zero-trust-architecture

skills/aj-geddes/useful-ai-prompts/zero-trust-architecture
zero-trust-architecture
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill zero-trust-architecture
SKILL.md
Zero Trust Architecture
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive Zero Trust security architecture based on "never trust, always verify" principle with identity-centric security, microsegmentation, and continuous verification.

When to Use
Cloud-native applications
Microservices architecture
Remote workforce security
API security
Multi-cloud deployments
Legacy modernization
Compliance requirements
Quick Start

Minimal working example:

// zero-trust-gateway.js
const jwt = require("jsonwebtoken");
const axios = require("axios");

class ZeroTrustGateway {
  constructor() {
    this.identityProvider = process.env.IDENTITY_PROVIDER_URL;
    this.deviceRegistry = new Map();
    this.sessionContext = new Map();
  }

  /**
   * Verify identity - Who are you?
   */
  async verifyIdentity(token) {
    try {
      // Verify JWT token
      const decoded = jwt.verify(token, process.env.JWT_PUBLIC_KEY, {
        algorithms: ["RS256"],
      });

      // Check token hasn't been revoked
      const revoked = await this.checkTokenRevocation(decoded.jti);
      if (revoked) {
        throw new Error("Token has been revoked");
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Zero Trust Gateway	Zero Trust Gateway
Service Mesh - Microsegmentation	Service Mesh - Microsegmentation
Python Zero Trust Policy Engine	Python Zero Trust Policy Engine
Best Practices
✅ DO
Verify every request
Implement MFA everywhere
Use microsegmentation
Monitor continuously
Encrypt all communications
Implement least privilege
Log all access
Regular audits
❌ DON'T
Trust network location
Use implicit trust
Skip device verification
Allow lateral movement
Use static credentials
Weekly Installs
278
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