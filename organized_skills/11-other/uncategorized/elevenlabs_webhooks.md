---
rating: ⭐⭐⭐
title: elevenlabs-webhooks
url: https://skills.sh/hookdeck/webhook-skills/elevenlabs-webhooks
---

# elevenlabs-webhooks

skills/hookdeck/webhook-skills/elevenlabs-webhooks
elevenlabs-webhooks
Installation
$ npx skills add https://github.com/hookdeck/webhook-skills --skill elevenlabs-webhooks
SKILL.md
ElevenLabs Webhooks
When to Use This Skill
Setting up ElevenLabs webhook handlers
Debugging signature verification failures
Understanding ElevenLabs event types and payloads
Processing call transcription events
Handling voice removal notifications
Essential Code
Signature Verification (SDK — Recommended)

ElevenLabs recommends using the official @elevenlabs/elevenlabs-js SDK for webhook verification and event construction. See Verify the webhook secret and construct the webhook payload.

// Express.js / Node example
const { ElevenLabsClient } = require('@elevenlabs/elevenlabs-js');

const elevenlabs = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY || 'webhook-only'
});

// In your webhook handler: get raw body and signature header, then:
const event = await elevenlabs.webhooks.constructEvent(rawBody, signatureHeader, process.env.ELEVENLABS_WEBHOOK_SECRET);
// event is the parsed payload; SDK throws on invalid signature

// Next.js example
import { ElevenLabsClient } from '@elevenlabs/elevenlabs-js';

const elevenlabs = new ElevenLabsClient({
  apiKey: process.env.ELEVENLABS_API_KEY || 'webhook-only'
});

export async function POST(request: NextRequest) {
  const rawBody = await request.text();
  const signatureHeader = request.headers.get('ElevenLabs-Signature');
  try {
    const event = await elevenlabs.webhooks.constructEvent(
      rawBody,
      signatureHeader,
      process.env.ELEVENLABS_WEBHOOK_SECRET
    );
    // Handle event.type, event.data...
    return new NextResponse('OK', { status: 200 });
  } catch (error) {
    return NextResponse.json({ error: (error as Error).message }, { status: 401 });
  }
}

Python SDK Verification (FastAPI)
import os
from fastapi import FastAPI, Request, HTTPException
from elevenlabs import ElevenLabs
from elevenlabs.errors import BadRequestError

app = FastAPI()
elevenlabs = ElevenLabs(api_key=os.environ.get("ELEVENLABS_API_KEY") or "webhook-only")

@app.post("/webhooks/elevenlabs")
async def elevenlabs_webhook(request: Request):
    raw_body = await request.body()
    sig = request.headers.get("ElevenLabs-Signature") or request.headers.get("elevenlabs-signature")
    
    if not sig:
        raise HTTPException(status_code=400, detail="Missing signature header")
    
    try:
        event = elevenlabs.webhooks.construct_event(
            raw_body.decode("utf-8"),
            sig,
            os.environ["ELEVENLABS_WEBHOOK_SECRET"]
        )
        # Handle event["type"], event["data"]...
        return {"status": "ok"}
    except BadRequestError as e:
        raise HTTPException(status_code=401, detail="Invalid signature")


The SDK (Node/TypeScript and Python) verifies the signature, validates the timestamp (30-minute tolerance), and returns the parsed event. On failure it throws; return 401 and the error message.

Common Event Types
Event	Triggered When	Common Use Cases
post_call_transcription	Call analysis completed	Process call insights, save transcripts
voice_removal_notice	Notice that voice will be removed	Notify users, backup voice data
voice_removal_notice_withdrawn	Voice removal notice cancelled	Update user notifications
voice_removed	Voice has been removed	Clean up voice data, update UI
Environment Variables
ELEVENLABS_WEBHOOK_SECRET=your_webhook_secret_here

Local Development

For local webhook testing, install Hookdeck CLI:

# Install via npm (recommended)
npm install -g hookdeck-cli

# Or via Homebrew
brew install hookdeck/hookdeck/hookdeck


Then start the tunnel:

hookdeck listen 3000 --path /webhooks/elevenlabs


No account required. Provides local tunnel + web UI for inspecting requests.

Resources
Overview - What ElevenLabs webhooks are, common event types
Setup - Configure webhooks in ElevenLabs dashboard, get signing secret
Verification - Signature verification details and gotchas
Express Example - Complete Express.js implementation
Next.js Example - Next.js App Router implementation
FastAPI Example - Python FastAPI implementation
Recommended: webhook-handler-patterns

We recommend installing the webhook-handler-patterns skill alongside this one for handler sequence, idempotency, error handling, and retry logic. Key references (open on GitHub):

Handler sequence — Verify first, parse second, handle idempotently third
Idempotency — Prevent duplicate processing
Error handling — Return codes, logging, dead letter queues
Retry logic — Provider retry schedules, backoff patterns
Related Skills
stripe-webhooks - Stripe payment webhook handling
shopify-webhooks - Shopify e-commerce webhook handling
github-webhooks - GitHub repository webhook handling
resend-webhooks - Resend email webhook handling
chargebee-webhooks - Chargebee billing webhook handling
clerk-webhooks - Clerk auth webhook handling
openai-webhooks - OpenAI webhook handling
paddle-webhooks - Paddle billing webhook handling
webhook-handler-patterns - Handler sequence, idempotency, error handling, retry logic
hookdeck-event-gateway - Webhook infrastructure that replaces your queue — guaranteed delivery, automatic retries, replay, rate limiting, and observability for your webhook handlers
Official ElevenLabs SDK Skills

For making API calls TO ElevenLabs (text-to-speech, transcription, agents), see the official ElevenLabs Skills. This skill handles the opposite direction: receiving webhooks FROM ElevenLabs.

SDK Warning: Always use @elevenlabs/elevenlabs-js for JavaScript. Do not use npm install elevenlabs (that's an outdated v1.x package).

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
SnykWarn