---
rating: ⭐⭐
title: logging-best-practices
url: https://skills.sh/aj-geddes/useful-ai-prompts/logging-best-practices
---

# logging-best-practices

skills/aj-geddes/useful-ai-prompts/logging-best-practices
logging-best-practices
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill logging-best-practices
SKILL.md
Logging Best Practices
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Comprehensive guide to implementing structured, secure, and performant logging across applications. Covers log levels, structured logging formats, contextual information, PII protection, and centralized logging systems.

When to Use
Setting up application logging infrastructure
Implementing structured logging
Configuring log levels for different environments
Managing sensitive data in logs
Setting up centralized logging
Implementing distributed tracing
Debugging production issues
Compliance with logging regulations
Quick Start

Minimal working example:

// logger.ts
enum LogLevel {
  DEBUG = 0, // Detailed information for debugging
  INFO = 1, // General informational messages
  WARN = 2, // Warning messages, potentially harmful
  ERROR = 3, // Error messages, application can continue
  FATAL = 4, // Critical errors, application must stop
}

class Logger {
  constructor(private minLevel: LogLevel = LogLevel.INFO) {}

  debug(message: string, context?: object) {
    if (this.minLevel <= LogLevel.DEBUG) {
      this.log(LogLevel.DEBUG, message, context);
    }
  }

  info(message: string, context?: object) {
    if (this.minLevel <= LogLevel.INFO) {
      this.log(LogLevel.INFO, message, context);
    }
  }

  warn(message: string, context?: object) {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Log Levels	Log Levels
Structured Logging (JSON)	Structured Logging (JSON)
Contextual Logging	Contextual Logging
PII and Sensitive Data Handling	PII and Sensitive Data Handling
Performance Logging	Performance Logging
Centralized Logging	Centralized Logging
Distributed Tracing	Distributed Tracing
Log Sampling (High-Volume Services)	Log Sampling (High-Volume Services)
Best Practices
✅ DO
Use structured logging (JSON) in production
Include correlation/request IDs in all logs
Log at appropriate levels (don't overuse DEBUG)
Redact sensitive data (PII, passwords, tokens)
Include context (userId, requestId, etc.)
Log errors with full stack traces
Use centralized logging in distributed systems
Set up log rotation to manage disk space
Monitor log volume and costs
Use async logging for performance
Include timestamps in ISO 8601 format
Log business events (user actions, transactions)
Set up alerts for error patterns
❌ DON'T
Log passwords, tokens, or sensitive data
Use console.log in production
Log at DEBUG level in production by default
Log inside tight loops (use sampling)
Include PII without anonymization
Ignore log rotation (disk will fill up)
Use synchronous logging in hot paths
Log to multiple transports without need
Forget to include error stack traces
Log binary data or large objects
Use string concatenation (use structured fields)
Log every single request in high-volume APIs
Weekly Installs
400
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