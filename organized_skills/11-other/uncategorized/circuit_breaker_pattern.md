---
rating: ⭐⭐
title: circuit-breaker-pattern
url: https://skills.sh/aj-geddes/useful-ai-prompts/circuit-breaker-pattern
---

# circuit-breaker-pattern

skills/aj-geddes/useful-ai-prompts/circuit-breaker-pattern
circuit-breaker-pattern
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill circuit-breaker-pattern
SKILL.md
Circuit Breaker Pattern
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement circuit breaker patterns to prevent cascading failures and provide graceful degradation when dependencies fail.

When to Use
External API calls
Microservices communication
Database connections
Third-party service integrations
Preventing cascading failures
Implementing fallback mechanisms
Rate limiting protection
Timeout handling
Quick Start

Minimal working example:

enum CircuitState {
  CLOSED = "CLOSED",
  OPEN = "OPEN",
  HALF_OPEN = "HALF_OPEN",
}

interface CircuitBreakerConfig {
  failureThreshold: number;
  successThreshold: number;
  timeout: number;
  resetTimeout: number;
}

interface CircuitBreakerStats {
  failures: number;
  successes: number;
  consecutiveFailures: number;
  consecutiveSuccesses: number;
  lastFailureTime?: number;
}

class CircuitBreaker {
  private state: CircuitState = CircuitState.CLOSED;
  private stats: CircuitBreakerStats = {
    failures: 0,
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
TypeScript Circuit Breaker	TypeScript Circuit Breaker
Circuit Breaker with Monitoring	Circuit Breaker with Monitoring
Opossum-Style Circuit Breaker (Node.js)	Opossum-Style Circuit Breaker (Node.js)
Python Circuit Breaker	Python Circuit Breaker
Resilience4j-Style (Java)	Resilience4j-Style (Java)
Best Practices
✅ DO
Use appropriate thresholds for your use case
Implement fallback mechanisms
Monitor circuit breaker states
Set reasonable timeouts
Use exponential backoff
Log state transitions
Alert on frequent trips
Test circuit breaker behavior
Use per-dependency breakers
Implement health checks
❌ DON'T
Use same breaker for all dependencies
Set unrealistic thresholds
Skip fallback implementation
Ignore open circuit breakers
Use overly aggressive reset timeouts
Forget to monitor
Weekly Installs
292
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