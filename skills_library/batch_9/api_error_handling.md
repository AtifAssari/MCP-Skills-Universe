---
title: api-error-handling
url: https://skills.sh/aj-geddes/useful-ai-prompts/api-error-handling
---

# api-error-handling

skills/aj-geddes/useful-ai-prompts/api-error-handling
api-error-handling
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill api-error-handling
SKILL.md
API Error Handling
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Build robust error handling systems with standardized error responses, detailed logging, error categorization, and user-friendly error messages. This skill covers the full lifecycle from throwing typed errors through logging, monitoring, and client-facing response formatting.

When to Use
Handling API errors consistently across endpoints
Debugging production issues with request tracing
Implementing error recovery strategies (retry, circuit breaker)
Monitoring and alerting on error rates
Providing meaningful, actionable error messages to clients
Validating request inputs before processing
Tracking error patterns over time
Quick Start

Minimal standardized error response format:

{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Input validation failed",
    "statusCode": 422,
    "requestId": "req_abc123xyz789",
    "timestamp": "2025-01-15T10:30:00Z",
    "details": [
      { "field": "email", "message": "Invalid email format", "code": "INVALID_EMAIL" }
    ]
  }
}


Custom error class (Node.js):

class ApiError extends Error {
  constructor(code, message, statusCode = null, details = null) {
    super(message);
    this.code = code;
    this.statusCode = statusCode || ERROR_CODES[code]?.status || 500;
    this.details = details;
    this.timestamp = new Date().toISOString();
  }
}

// Usage
throw new ApiError("NOT_FOUND", "User not found", 404);
throw new ApiError("VALIDATION_ERROR", "Missing fields", 422, fieldErrors);

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Error Codes & Response Format	Complete ERROR_CODES map, response formatter, global middleware (Node.js + Python)
Retry Strategies & Circuit Breaker	Exponential backoff, jitter, circuit breaker pattern
Monitoring & Tracking	Sentry integration, error rate metrics, /metrics/errors endpoint
Validation Patterns	Input validation, schema guards, detecting bad responses before errors occur
Best Practices
✅ DO
Use a consistent error response format across all endpoints
Include requestId and traceId in every error for observability
Log 5xx errors at ERROR level; log 4xx at WARN level
Provide actionable error messages — tell the client what to fix
Use standard HTTP status codes (4xx client errors, 5xx server errors)
Implement retry with exponential backoff for transient failures
Use circuit breakers to prevent cascade failures
Validate inputs early and return all field errors at once
Monitor error rates and alert on anomalous spikes
❌ DON'T
Expose stack traces or internal implementation details to clients
Return HTTP 200 for error responses
Silently swallow errors
Log sensitive data (passwords, tokens, PII)
Use vague messages like "Something went wrong"
Mix error handling logic with business logic
Retry non-idempotent operations or client errors (4xx)
Return different error shapes from different endpoints
Weekly Installs
311
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