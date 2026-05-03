---
title: log-analysis
url: https://skills.sh/aj-geddes/useful-ai-prompts/log-analysis
---

# log-analysis

skills/aj-geddes/useful-ai-prompts/log-analysis
log-analysis
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill log-analysis
SKILL.md
Log Analysis
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Logs are critical for debugging and monitoring. Effective log analysis quickly identifies issues and enables root cause analysis.

When to Use
Troubleshooting errors
Performance investigation
Security incident analysis
Auditing user actions
Monitoring application health
Quick Start

Minimal working example:

// Good: Structured logs (machine-readable)
logger.info({
  level: 'INFO',
  timestamp: '2024-01-15T10:30:00Z',
  service: 'auth-service',
  user_id: '12345',
  action: 'user_login',
  status: 'success',
  duration_ms: 150,
  ip_address: '192.168.1.1'
});

// Bad: Unstructured logs (hard to parse)
console.log('User 12345 logged in successfully in 150ms from 192.168.1.1');

// JSON Format (Elasticsearch friendly)
{
  "@timestamp": "2024-01-15T10:30:00Z",
  "level": "ERROR",
  "service": "api-gateway",
  "trace_id": "abc123",
  "message": "Database connection failed",
  "error": {
    "type": "ConnectionError",
    "code": "ECONNREFUSED"
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Structured Logging	Structured Logging
Log Levels & Patterns	Log Levels & Patterns
Log Analysis Tools	Log Analysis Tools
Common Log Analysis Queries	Common Log Analysis Queries
Best Practices
✅ DO
Follow established patterns and conventions
Write clean, maintainable code
Add appropriate documentation
Test thoroughly before deploying
❌ DON'T
Skip testing or validation
Ignore error handling
Hard-code configuration values
Weekly Installs
352
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