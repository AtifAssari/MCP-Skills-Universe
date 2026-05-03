---
title: error-handling
url: https://skills.sh/srstomp/pokayokay/error-handling
---

# error-handling

skills/srstomp/pokayokay/error-handling
error-handling
Installation
$ npx skills add https://github.com/srstomp/pokayokay --skill error-handling
SKILL.md
Error Handling

Design resilient applications through intentional error handling strategies. Errors are data, not just exceptions — design them intentionally.

Quick Decision Guide
Situation	Pattern	Reference
Typed error categories	Custom error classes	error-patterns.md
Explicit handling (no throws)	Result/Either type	error-patterns.md
React component crash	Error boundary	react-errors.md
API error response	Structured API errors	api-errors.md
Network calls that fail	Retry with backoff	recovery-patterns.md
Unreliable downstream service	Circuit breaker	recovery-patterns.md
Key Principles
Debuggable: Rich context, stack traces, correlation IDs
Recoverable: Retry logic, fallbacks, circuit breakers
User-friendly: Clear messages, recovery guidance, no leaked internals
Consistent: Same error shape across all API endpoints
Quick Start Checklist
Define base AppError class with code and context
Create domain-specific error subclasses
Implement consistent API error response shape
Add error boundaries at app, route, and component levels
Set up error tracking (Sentry) with scrubbing
References
Reference	Description
error-patterns.md	Custom errors, Result types, error hierarchies
react-errors.md	Error boundaries, Suspense, React error handling
api-errors.md	HTTP errors, response shapes, status codes
recovery-patterns.md	Retry, circuit breaker, fallbacks, degradation
overview.md	Error types, Result pattern, user messages, tracking, anti-patterns
anti-rationalization.md	Iron Law, common rationalizations, red flag STOP list for error handling discipline
tdd-patterns.md	Test-first patterns for error paths, retry logic, boundaries
review-checklist.md	Error handling review checklist (classes, messages, recovery, tracking)
Weekly Installs
21
Repository
srstomp/pokayokay
GitHub Stars
6
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass