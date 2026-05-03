---
title: qstash-js
url: https://skills.sh/upstash/qstash-js/qstash-js
---

# qstash-js

skills/upstash/qstash-js/qstash-js
qstash-js
Installation
$ npx skills add https://github.com/upstash/qstash-js --skill qstash-js
SKILL.md
QStash JavaScript SDK

QStash is an HTTP-based messaging and scheduling solution for serverless and edge runtimes. This skill helps you use the QStash JS SDK effectively.

When to use this skill

Use this skill when:

Publishing HTTP messages to endpoints or URL groups
Creating scheduled or delayed message delivery
Managing FIFO queues with configurable parallelism
Verifying incoming webhook signatures from QStash
Implementing callbacks, DLQ handling, or message deduplication
Quick Start
Installing the SDK
npm install @upstash/qstash

Basic Publishing
import { Client } from "@upstash/qstash";

const client = new Client({
  token: process.env.QSTASH_TOKEN!,
});

const result = await client.publishJSON({
  url: "https://my-api.example.com/webhook",
  body: { event: "user.created", userId: "123" },
});

Core Concepts

For fundamental QStash operations, see:

Publishing Messages
Schedules
Queues and Flow Control
URL Groups

For verifying incoming messages:

Receiver Verification - Core signature verification with the Receiver class
Platform-Specific Verifiers:
Next.js - App Router, Pages Router, and Edge Runtime

For advanced features:

Callbacks
Dead Letter Queue (DLQ)
Message Deduplication
Region migration & multi-region support
If needed, multi-region env variable setup verification script. Can be run without arguments
Platform Support

QStash JS SDK works across various platforms:

Next.js (App Router and Pages Router)
Cloudflare Workers
Deno
Node.js (v18+)
Vercel Edge Runtime
SvelteKit, Nuxt, SolidJS, and other frameworks

Note on Workflow SDK: For building complex durable workflows that chain multiple QStash messages together, consider using the separate QStash Workflow SDK (@upstash/workflow). The Workflow SDK empowers you to orchestrate multi-step processes with automatic state management, retries, and fault tolerance. This Skills file focuses on the core QStash messaging SDK.

Best Practices
Always verify incoming QStash messages using the Receiver class
Use environment variables for tokens and signing keys
Set appropriate retry counts and timeouts for your use case
Use queues for ordered processing with controlled parallelism
Implement DLQ handling for failed message recovery
Weekly Installs
58
Repository
upstash/qstash-js
GitHub Stars
266
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn