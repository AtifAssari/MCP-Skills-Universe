---
rating: ⭐⭐
title: application-logging
url: https://skills.sh/aj-geddes/useful-ai-prompts/application-logging
---

# application-logging

skills/aj-geddes/useful-ai-prompts/application-logging
application-logging
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill application-logging
SKILL.md
Application Logging
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement comprehensive structured logging with proper levels, context, and centralized aggregation for effective debugging and monitoring.

When to Use
Application debugging
Audit trail creation
Performance analysis
Compliance requirements
Centralized log aggregation
Quick Start

Minimal working example:

// logger.js
const winston = require("winston");

const logFormat = winston.format.combine(
  winston.format.timestamp({ format: "YYYY-MM-DD HH:mm:ss" }),
  winston.format.errors({ stack: true }),
  winston.format.json(),
);

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || "info",
  format: logFormat,
  defaultMeta: {
    service: "api-service",
    environment: process.env.NODE_ENV || "development",
  },
  transports: [
    new winston.transports.Console({
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple(),
      ),
    }),
    new winston.transports.File({
      filename: "logs/error.log",
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Node.js Structured Logging with Winston	Node.js Structured Logging with Winston
Express HTTP Request Logging	Express HTTP Request Logging
Python Structured Logging	Python Structured Logging
Flask Integration	Flask Integration
ELK Stack Setup	ELK Stack Setup
Logstash Configuration	Logstash Configuration
Best Practices
✅ DO
Use structured JSON logging
Include request IDs for tracing
Log at appropriate levels
Add context to error logs
Implement log rotation
Use timestamps consistently
Aggregate logs centrally
Filter sensitive data
❌ DON'T
Log passwords or secrets
Log at INFO for every operation
Use unstructured messages
Ignore log storage limits
Skip context information
Log to stdout in production
Create unbounded log files
Weekly Installs
323
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