---
title: security-audit-logging
url: https://skills.sh/aj-geddes/useful-ai-prompts/security-audit-logging
---

# security-audit-logging

skills/aj-geddes/useful-ai-prompts/security-audit-logging
security-audit-logging
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill security-audit-logging
SKILL.md
Security Audit Logging
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive audit logging for security events, user actions, and system changes with structured logging, retention policies, and SIEM integration.

When to Use
Compliance requirements (SOC 2, HIPAA, PCI-DSS)
Security monitoring
Forensic investigations
User activity tracking
System change auditing
Breach detection
Quick Start

Minimal working example:

// audit-logger.js
const winston = require("winston");
const { ElasticsearchTransport } = require("winston-elasticsearch");

class AuditLogger {
  constructor() {
    this.logger = winston.createLogger({
      level: "info",
      format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.json(),
      ),
      transports: [
        // File transport
        new winston.transports.File({
          filename: "logs/audit.log",
          maxsize: 10485760, // 10MB
          maxFiles: 30,
          tailable: true,
        }),

        // Elasticsearch transport for SIEM
        new ElasticsearchTransport({
          level: "info",
          clientOpts: {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Node.js Audit Logger	Node.js Audit Logger
Python Audit Logging System	Python Audit Logging System
Java Audit Logging	Java Audit Logging
Best Practices
✅ DO
Log all security events
Use structured logging
Include timestamps (UTC)
Log user context
Implement log retention
Encrypt sensitive logs
Monitor log integrity
Send to SIEM
Include request IDs
❌ DON'T
Log passwords/secrets
Log sensitive PII unnecessarily
Skip failed attempts
Allow log tampering
Store logs insecurely
Ignore log analysis
Weekly Installs
337
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