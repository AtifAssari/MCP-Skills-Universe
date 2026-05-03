---
title: webhook-integration
url: https://skills.sh/aj-geddes/useful-ai-prompts/webhook-integration
---

# webhook-integration

skills/aj-geddes/useful-ai-prompts/webhook-integration
webhook-integration
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill webhook-integration
SKILL.md
Webhook Integration
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Implement robust webhook systems for event-driven architectures, enabling real-time communication between services and third-party integrations.

When to Use
Third-party service integrations (Stripe, GitHub, Shopify)
Event notification systems
Real-time data synchronization
Automated workflow triggers
Payment processing callbacks
CI/CD pipeline notifications
User activity tracking
Microservices communication
Quick Start

Minimal working example:

import crypto from "crypto";
import axios from "axios";

interface WebhookEvent {
  id: string;
  type: string;
  timestamp: number;
  data: any;
}

interface WebhookEndpoint {
  url: string;
  secret: string;
  events: string[];
  active: boolean;
}

interface DeliveryAttempt {
  attemptNumber: number;
  timestamp: number;
  statusCode?: number;
  error?: string;
  duration: number;
}

// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Webhook Sender (TypeScript)	Webhook Sender (TypeScript)
Webhook Receiver (Express)	Webhook Receiver (Express)
Webhook Queue with Bull	Webhook Queue with Bull
Webhook Testing Utilities	Webhook Testing Utilities
Best Practices
✅ DO
Use HMAC signatures for verification
Implement idempotency with event IDs
Return 200 OK quickly, process asynchronously
Implement exponential backoff for retries
Include timestamp to prevent replay attacks
Use queue systems for reliable delivery
Log all delivery attempts
Provide webhook testing tools
Document webhook payload schemas
Implement webhook management UI
Allow filtering by event types
Support webhook versioning
❌ DON'T
Send sensitive data in webhooks
Skip signature verification
Block responses with heavy processing
Retry indefinitely
Expose internal error details
Send webhooks to localhost (in production)
Forget timeout handling
Skip rate limiting
Weekly Installs
275
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn