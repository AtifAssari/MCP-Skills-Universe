---
title: replicate-webhooks
url: https://skills.sh/hookdeck/webhook-skills/replicate-webhooks
---

# replicate-webhooks

skills/hookdeck/webhook-skills/replicate-webhooks
replicate-webhooks
Installation
$ npx skills add https://github.com/hookdeck/webhook-skills --skill replicate-webhooks
SKILL.md
Replicate Webhooks
When to Use This Skill
Setting up Replicate webhook handlers
Debugging signature verification failures
Understanding Replicate event types and payloads
Handling prediction lifecycle events (start, output, logs, completed)
Essential Code (USE THIS)
Express Webhook Handler
const express = require('express');
const crypto = require('crypto');

const app = express();

// CRITICAL: Use express.raw() for webhook endpoint - Replicate needs raw body
app.post('/webhooks/replicate',
  express.raw({ type: 'application/json' }),
  async (req, res) => {
    // Get webhook headers
    const webhookId = req.headers['webhook-id'];
    const webhookTimestamp = req.headers['webhook-timestamp'];
    const webhookSignature = req.headers['webhook-signature'];

    // Verify we have required headers
    if (!webhookId || !webhookTimestamp || !webhookSignature) {
      return res.status(400).json({ error: 'Missing required webhook headers' });
    }

    // Manual signature verification (recommended approach)
    const secret = process.env.REPLICATE_WEBHOOK_SECRET; // whsec_xxxxx from Replicate
    const signedContent = `${webhookId}.${webhookTimestamp}.${req.body}`;

    try {
      // Extract base64 secret after 'whsec_' prefix
      const secretBytes = Buffer.from(secret.split('_')[1], 'base64');
      const expectedSignature = crypto
        .createHmac('sha256', secretBytes)
        .update(signedContent)
        .digest('base64');

      // Replicate can send multiple signatures, check each one
      const signatures = webhookSignature.split(' ').map(sig => {
        const parts = sig.split(',');
        return parts.length > 1 ? parts[1] : sig;
      });

      const isValid = signatures.some(sig => {
        try {
          return crypto.timingSafeEqual(
            Buffer.from(sig),
            Buffer.from(expectedSignature)
          );
        } catch {
          return false; // Different lengths = invalid
        }
      });

      if (!isValid) {
        return res.status(400).json({ error: 'Invalid signature' });
      }

      // Check timestamp to prevent replay attacks (5-minute window)
      const timestamp = parseInt(webhookTimestamp, 10);
      const currentTime = Math.floor(Date.now() / 1000);
      if (currentTime - timestamp > 300) {
        return res.status(400).json({ error: 'Timestamp too old' });
      }
    } catch (err) {
      console.error('Signature verification error:', err);
      return res.status(400).json({ error: 'Invalid signature' });
    }

    // Parse the verified webhook body
    const prediction = JSON.parse(req.body.toString());

    // Handle the prediction based on its status
    console.log('Prediction webhook received:', {
      id: prediction.id,
      status: prediction.status,
      version: prediction.version
    });

    switch (prediction.status) {
      case 'starting':
        console.log('Prediction starting:', prediction.id);
        break;
      case 'processing':
        console.log('Prediction processing:', prediction.id);
        if (prediction.logs) {
          console.log('Logs:', prediction.logs);
        }
        break;
      case 'succeeded':
        console.log('Prediction completed successfully:', prediction.id);
        console.log('Output:', prediction.output);
        break;
      case 'failed':
        console.log('Prediction failed:', prediction.id);
        console.log('Error:', prediction.error);
        break;
      case 'canceled':
        console.log('Prediction canceled:', prediction.id);
        break;
      default:
        console.log('Unknown status:', prediction.status);
    }

    res.status(200).json({ received: true });
  }
);

Common Prediction Statuses
Status	Description	Common Use Cases
starting	Prediction is initializing	Show loading state in UI
processing	Model is running	Display progress, show logs if available
succeeded	Prediction completed successfully	Process final output, update UI
failed	Prediction encountered an error	Show error message to user
canceled	Prediction was canceled	Clean up resources, notify user
Environment Variables
# Your webhook signing secret from Replicate
REPLICATE_WEBHOOK_SECRET=whsec_your_secret_here

Local Development

For local webhook testing, install the Hookdeck CLI:

# Install via npm
npm install -g hookdeck-cli

# Or via Homebrew
brew install hookdeck/hookdeck/hookdeck


Then start the tunnel:

hookdeck listen 3000 --path /webhooks/replicate


No account required. Provides local tunnel + web UI for inspecting requests.

Reference Materials
What are Replicate webhooks — Event types and payload structure
Setting up webhooks — Dashboard configuration and signing secret
Signature verification — Verification algorithm and common issues
Resources for Implementation
Framework Examples
Express implementation — Node.js with Express
Next.js implementation — React framework with API routes
FastAPI implementation — Python async framework
Documentation
Official Replicate webhook docs
Webhook setup guide
Webhook verification guide
Recommended: webhook-handler-patterns

Enhance your webhook implementation with these patterns:

Handler sequence
Idempotency
Error handling
Retry logic
Related Skills
stripe-webhooks - Stripe payment webhooks
github-webhooks - GitHub repository events
shopify-webhooks - Shopify store events
clerk-webhooks - Clerk authentication events
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