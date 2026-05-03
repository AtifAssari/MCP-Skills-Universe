---
title: api-rate-limiting
url: https://skills.sh/aj-geddes/useful-ai-prompts/api-rate-limiting
---

# api-rate-limiting

skills/aj-geddes/useful-ai-prompts/api-rate-limiting
api-rate-limiting
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill api-rate-limiting
SKILL.md
API Rate Limiting
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Protect APIs from abuse and manage traffic using various rate limiting algorithms with per-user, per-IP, and per-endpoint strategies.

When to Use
Protecting APIs from brute force attacks
Managing traffic spikes
Implementing tiered service plans
Preventing DoS attacks
Fairness in resource allocation
Enforcing quotas and usage limits
Quick Start

Minimal working example:

// Token Bucket Rate Limiter
class TokenBucket {
  constructor(capacity, refillRate) {
    this.capacity = capacity;
    this.tokens = capacity;
    this.refillRate = refillRate; // tokens per second
    this.lastRefillTime = Date.now();
  }

  refill() {
    const now = Date.now();
    const timePassed = (now - this.lastRefillTime) / 1000;
    const tokensToAdd = timePassed * this.refillRate;

    this.tokens = Math.min(this.capacity, this.tokens + tokensToAdd);
    this.lastRefillTime = now;
  }

  consume(tokens = 1) {
    this.refill();

    if (this.tokens >= tokens) {
      this.tokens -= tokens;
      return true;
    }
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Token Bucket Algorithm	Token Bucket Algorithm
Sliding Window Algorithm	Sliding Window Algorithm
Redis-Based Rate Limiting	Redis-Based Rate Limiting
Tiered Rate Limiting	Tiered Rate Limiting
Python Rate Limiting (Flask)	Python Rate Limiting (Flask)
Response Headers	Response Headers
Best Practices
✅ DO
Include rate limit headers in responses
Use Redis for distributed rate limiting
Implement tiered limits for different user plans
Set appropriate window sizes and limits
Monitor rate limit metrics
Provide clear retry guidance
Document rate limits in API docs
Test under high load
❌ DON'T
Use in-memory storage in production
Set limits too restrictively
Forget to include Retry-After header
Ignore distributed scenarios
Make rate limits public (security)
Use simple counters for distributed systems
Forget cleanup of old data
Weekly Installs
374
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