---
title: secrets-rotation
url: https://skills.sh/aj-geddes/useful-ai-prompts/secrets-rotation
---

# secrets-rotation

skills/aj-geddes/useful-ai-prompts/secrets-rotation
secrets-rotation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill secrets-rotation
SKILL.md
Secrets Rotation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement automated secrets rotation strategy for credentials, API keys, certificates, and encryption keys with zero-downtime deployment and comprehensive audit logging.

When to Use
API key management
Database credentials
TLS/SSL certificates
Encryption key rotation
Compliance requirements
Security incident response
Service account management
Quick Start

Minimal working example:

// secrets-manager.js
const AWS = require("aws-sdk");
const crypto = require("crypto");

class SecretsManager {
  constructor() {
    this.secretsManager = new AWS.SecretsManager({
      region: process.env.AWS_REGION,
    });

    this.rotationSchedule = new Map();
  }

  /**
   * Generate new secret value
   */
  generateSecret(type = "api_key", length = 32) {
    switch (type) {
      case "api_key":
        return crypto.randomBytes(length).toString("hex");

      case "password":
        // Generate strong password
        const chars =
          "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Node.js Secrets Manager with Rotation	Node.js Secrets Manager with Rotation
Python Secrets Rotation with Vault	Python Secrets Rotation with Vault
Kubernetes Secrets Rotation	Kubernetes Secrets Rotation
Best Practices
✅ DO
Automate rotation
Use grace periods
Verify new secrets
Maintain rotation audit trail
Implement rollback procedures
Monitor rotation failures
Use managed services (AWS Secrets Manager)
Test rotation procedures
❌ DON'T
Hardcode secrets
Share secrets
Skip verification
Rotate without grace period
Ignore rotation failures
Store secrets in version control
Weekly Installs
267
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