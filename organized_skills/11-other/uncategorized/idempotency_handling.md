---
rating: ⭐⭐
title: idempotency-handling
url: https://skills.sh/aj-geddes/useful-ai-prompts/idempotency-handling
---

# idempotency-handling

skills/aj-geddes/useful-ai-prompts/idempotency-handling
idempotency-handling
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill idempotency-handling
SKILL.md
Idempotency Handling
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement idempotency to ensure operations produce the same result regardless of how many times they're executed.

When to Use
Payment processing
API endpoints with retries
Webhooks and callbacks
Message queue consumers
Distributed transactions
Bank transfers
Order creation
Email sending
Resource creation
Quick Start

Minimal working example:

import express from "express";
import Redis from "ioredis";
import crypto from "crypto";

interface IdempotentRequest {
  key: string;
  status: "processing" | "completed" | "failed";
  response?: any;
  error?: string;
  createdAt: number;
  completedAt?: number;
}

class IdempotencyService {
  private redis: Redis;
  private ttl = 86400; // 24 hours

  constructor(redisUrl: string) {
    this.redis = new Redis(redisUrl);
  }

  async getRequest(key: string): Promise<IdempotentRequest | null> {
    const data = await this.redis.get(`idempotency:${key}`);
    return data ? JSON.parse(data) : null;
  }
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Express Idempotency Middleware	Express Idempotency Middleware
Database-Based Idempotency	Database-Based Idempotency
Stripe-Style Idempotency	Stripe-Style Idempotency
Message Queue Idempotency	Message Queue Idempotency
Best Practices
✅ DO
Require idempotency keys for mutations
Store request and response together
Set appropriate TTL for idempotency records
Validate request body matches stored request
Handle concurrent requests gracefully
Return same response for duplicate requests
Clean up old idempotency records
Use database constraints for atomicity
❌ DON'T
Apply idempotency to GET requests
Store idempotency data forever
Skip validation of request body
Use non-unique idempotency keys
Process same request concurrently
Change response for duplicate requests
Weekly Installs
274
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