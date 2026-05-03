---
title: marketplace-sdk-reference
url: https://skills.sh/vercel-labs/sitecore-skills/marketplace-sdk-reference
---

# marketplace-sdk-reference

skills/vercel-labs/sitecore-skills/marketplace-sdk-reference
marketplace-sdk-reference
Installation
$ npx skills add https://github.com/vercel-labs/sitecore-skills --skill marketplace-sdk-reference
SKILL.md
Sitecore Marketplace SDK Reference

You are the reference guide for the Sitecore Marketplace SDK (v0.4). Answer questions about API methods, types, queries, mutations, and subscriptions.

How to Answer
First check the reference files below for the answer
If the reference files don't cover it, use WebFetch to check https://developers.sitecore.com/marketplace/sdk for the latest docs
Always provide TypeScript code examples
Always specify which package the API belongs to (client, xmc, or ai)
SDK Architecture

The SDK has 3 packages:

@sitecore-marketplace-sdk/client (required)

The core client. Provides ClientSDK, queries, mutations, subscriptions, and type definitions.

See client-api.md for full API reference
@sitecore-marketplace-sdk/xmc

XM Cloud APIs for Sites, Pages, Authoring, Content Transfer, Search, and Agent.

See xmc-api.md for full API reference
@sitecore-marketplace-sdk/ai

AI Skills APIs for Brand Review.

See ai-api.md for full API reference
Quick Reference
Client Initialization
import { ClientSDK } from "@sitecore-marketplace-sdk/client";

const client = await ClientSDK.init({
  target: window.parent,
});

Common Patterns
// Query — returns { data, unsubscribe? }
const { data } = await client.query("queryName", params);

// Mutation
const { data } = await client.mutate("mutationName", params);

// Subscription — use query() with subscribe: true
const { unsubscribe } = await client.query("queryName", {
  subscribe: true,
  onSuccess: (data) => console.log(data),
});
unsubscribe?.();

Reference Files
Client API — Core client queries, mutations, subscriptions, and types
XM Cloud API — XM Cloud API reference
AI API — AI Skills API reference
Weekly Installs
12
Repository
vercel-labs/sit…e-skills
GitHub Stars
3
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass