---
title: cursor-webhooks
url: https://skills.sh/hookdeck/webhook-skills/cursor-webhooks
---

# cursor-webhooks

skills/hookdeck/webhook-skills/cursor-webhooks
cursor-webhooks
Installation
$ npx skills add https://github.com/hookdeck/webhook-skills --skill cursor-webhooks
SKILL.md
Cursor Webhooks
When to Use This Skill
Setting up Cursor Cloud Agent webhook handlers
Debugging signature verification failures
Understanding Cursor webhook event types and payloads
Handling Cloud Agent status change events (ERROR, FINISHED)
Essential Code (USE THIS)
Cursor Signature Verification (JavaScript)
const crypto = require('crypto');

function verifyCursorWebhook(rawBody, signatureHeader, secret) {
  if (!signatureHeader || !secret) return false;

  // Cursor sends: sha256=xxxx
  const [algorithm, signature] = signatureHeader.split('=');
  if (algorithm !== 'sha256') return false;

  const expected = crypto
    .createHmac('sha256', secret)
    .update(rawBody)
    .digest('hex');

  try {
    return crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(expected));
  } catch {
    return false;
  }
}

Express Webhook Handler
const express = require('express');
const app = express();

// CRITICAL: Use express.raw() - Cursor requires raw body for signature verification
app.post('/webhooks/cursor',
  express.raw({ type: 'application/json' }),
  (req, res) => {
    const signature = req.headers['x-webhook-signature'];
    const webhookId = req.headers['x-webhook-id'];
    const event = req.headers['x-webhook-event'];

    // Verify signature
    if (!verifyCursorWebhook(req.body, signature, process.env.CURSOR_WEBHOOK_SECRET)) {
      console.error('Cursor signature verification failed');
      return res.status(401).send('Invalid signature');
    }

    // Parse payload after verification
    const payload = JSON.parse(req.body.toString());

    console.log(`Received ${event} (id: ${webhookId})`);

    // Handle status changes
    if (event === 'statusChange') {
      console.log(`Agent ${payload.id} status: ${payload.status}`);

      if (payload.status === 'FINISHED') {
        console.log(`Summary: ${payload.summary}`);
      } else if (payload.status === 'ERROR') {
        console.error(`Agent error for ${payload.id}`);
      }
    }

    res.json({ received: true });
  }
);

Python Signature Verification (FastAPI)
import hmac
import hashlib
from fastapi import Request, HTTPException

def verify_cursor_webhook(body: bytes, signature_header: str, secret: str) -> bool:
    if not signature_header or not secret:
        return False

    # Cursor sends: sha256=xxxx
    parts = signature_header.split('=')
    if len(parts) != 2 or parts[0] != 'sha256':
        return False

    signature = parts[1]
    expected = hmac.new(
        secret.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    # Timing-safe comparison
    return hmac.compare_digest(signature, expected)

Common Event Types
Event Type	Description	Common Use Cases
statusChange	Agent status changed	Monitor agent completion, handle errors
Event Payload Structure
{
  "event": "statusChange",
  "timestamp": "2024-01-01T12:00:00.000Z",
  "id": "agent_123456",
  "status": "FINISHED",  // or "ERROR"
  "source": {
    "repository": "https://github.com/user/repo",
    "ref": "main"
  },
  "target": {
    "url": "https://github.com/user/repo/pull/123",
    "branchName": "feature-branch",
    "prUrl": "https://github.com/user/repo/pull/123"
  },
  "summary": "Updated 3 files and fixed linting errors"
}

Environment Variables
# Your Cursor webhook signing secret
CURSOR_WEBHOOK_SECRET=your_webhook_secret_here

Local Development

For local webhook testing, install Hookdeck CLI:

# Install via npm
npm install -g hookdeck-cli

# Or via Homebrew
brew install hookdeck/hookdeck/hookdeck


Then start the tunnel:

hookdeck listen 3000 --path /webhooks/cursor


No account required. Provides local tunnel + web UI for inspecting requests.

Resources
overview.md - What Cursor webhooks are, event types
setup.md - Configure webhooks in Cursor dashboard
verification.md - Signature verification details and gotchas
examples/ - Runnable examples per framework
Recommended: webhook-handler-patterns

For production-ready webhook handling, also use the webhook-handler-patterns skill:

Handler sequence
Idempotency
Error handling
Retry logic
Related Skills
stripe-webhooks - Stripe webhook handling
github-webhooks - GitHub webhook handling
shopify-webhooks - Shopify webhook handling
openai-webhooks - OpenAI webhook handling
webhook-handler-patterns - Idempotency, error handling, retry logic
hookdeck-event-gateway - Webhook infrastructure that replaces your queue — guaranteed delivery, automatic retries, replay, rate limiting, and observability for your webhook handlers
Weekly Installs
65
Repository
hookdeck/webhook-skills
GitHub Stars
69
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass