---
title: rate-limiting-implementation
url: https://skills.sh/aj-geddes/useful-ai-prompts/rate-limiting-implementation
---

# rate-limiting-implementation

skills/aj-geddes/useful-ai-prompts/rate-limiting-implementation
rate-limiting-implementation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill rate-limiting-implementation
SKILL.md
Rate Limiting Implementation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement rate limiting and throttling mechanisms to protect your services from abuse, ensure fair resource allocation, and maintain system stability under load.

When to Use
Protecting public APIs from abuse
Preventing DOS/DDOS attacks
Ensuring fair resource usage across users
Implementing API quotas and billing tiers
Managing system load and backpressure
Enforcing SLA limits
Controlling third-party API usage
Database connection management
Quick Start

Minimal working example:

interface TokenBucketConfig {
  capacity: number;
  refillRate: number; // tokens per second
  refillInterval: number; // milliseconds
}

class TokenBucket {
  private tokens: number;
  private lastRefill: number;
  private readonly capacity: number;
  private readonly refillRate: number;
  private readonly refillInterval: number;
  private refillTimer?: NodeJS.Timeout;

  constructor(config: TokenBucketConfig) {
    this.capacity = config.capacity;
    this.tokens = config.capacity;
    this.refillRate = config.refillRate;
    this.refillInterval = config.refillInterval;
    this.lastRefill = Date.now();

    this.startRefill();
  }

  private startRefill(): void {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Token Bucket Algorithm (TypeScript)	Token Bucket Algorithm (TypeScript)
Redis-Based Distributed Rate Limiter	Redis-Based Distributed Rate Limiter
Express Middleware	Express Middleware
Sliding Window Algorithm (Python)	Sliding Window Algorithm (Python)
Tiered Rate Limiting	Tiered Rate Limiting
Adaptive Rate Limiting	Adaptive Rate Limiting
Best Practices
✅ DO
Use distributed rate limiting for multi-server deployments
Implement multiple rate limit tiers (per second, minute, hour, day)
Return proper HTTP status codes (429 Too Many Requests)
Include Retry-After header in responses
Log rate limit violations for monitoring
Implement graceful degradation
Use Redis or similar for persistence
Consider cost-based rate limiting (expensive operations cost more)
Implement burst allowances for legitimate traffic spikes
Provide clear API documentation about limits
❌ DON'T
Store rate limit data in application memory for distributed systems
Use fixed window counters without considering edge cases
Forget to clean up expired data
Block all requests from an IP due to one bad actor
Set limits too restrictive for legitimate use
Ignore the impact of rate limiting on user experience
Fail closed (deny all) when rate limiter fails
Weekly Installs
309
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