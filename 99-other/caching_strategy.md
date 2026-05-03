---
rating: ⭐⭐
title: caching-strategy
url: https://skills.sh/aj-geddes/useful-ai-prompts/caching-strategy
---

# caching-strategy

skills/aj-geddes/useful-ai-prompts/caching-strategy
caching-strategy
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill caching-strategy
SKILL.md
Caching Strategy
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement effective caching strategies to improve application performance, reduce latency, and decrease load on backend systems.

When to Use
Reducing database query load
Improving API response times
Handling high traffic loads
Caching expensive computations
Storing session data
CDN integration for static assets
Implementing distributed caching
Rate limiting and throttling
Quick Start

Minimal working example:

import Redis from "ioredis";

interface CacheOptions {
  ttl?: number; // Time to live in seconds
  prefix?: string;
}

class CacheService {
  private redis: Redis;
  private defaultTTL = 3600; // 1 hour

  constructor(redisUrl: string) {
    this.redis = new Redis(redisUrl, {
      retryStrategy: (times) => {
        const delay = Math.min(times * 50, 2000);
        return delay;
      },
      maxRetriesPerRequest: 3,
    });

    this.redis.on("connect", () => {
      console.log("Redis connected");
    });

    this.redis.on("error", (error) => {
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Redis Cache Implementation (Node.js)	Redis Cache Implementation (Node.js)
Cache Decorator (Python)	Cache Decorator (Python)
Multi-Level Cache	Multi-Level Cache
Cache Invalidation Strategies	Cache Invalidation Strategies
HTTP Caching Headers	HTTP Caching Headers
Best Practices
✅ DO
Set appropriate TTL values
Implement cache warming for critical data
Use cache-aside pattern for reads
Monitor cache hit rates
Implement graceful degradation on cache failure
Use compression for large cached values
Namespace cache keys properly
Implement cache stampede prevention
Use consistent hashing for distributed caching
Monitor cache memory usage
❌ DON'T
Cache everything indiscriminately
Use caching as a fix for poor database design
Store sensitive data without encryption
Forget to handle cache misses
Set TTL too long for frequently changing data
Ignore cache invalidation strategies
Cache without monitoring
Store large objects without consideration
Weekly Installs
346
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