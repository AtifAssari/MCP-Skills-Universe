---
rating: ⭐⭐
title: iii-node-sdk
url: https://skills.sh/iii-hq/skills/iii-node-sdk
---

# iii-node-sdk

skills/iii-hq/skills/iii-node-sdk
iii-node-sdk
Installation
$ npx skills add https://github.com/iii-hq/skills --skill iii-node-sdk
SKILL.md
Node.js SDK

The TypeScript/JavaScript SDK for connecting workers to the iii engine.

Documentation

Full API reference: https://iii.dev/docs/api-reference/sdk-node

Install

npm install iii-sdk

Key Exports
Export	Purpose
registerWorker(url, { workerName })	Connect to the engine and return the client
registerFunction({ id }, handler)	Register an async function handler
registerTrigger({ type, function_id, config })	Bind a trigger to a function
trigger({ function_id, payload, action? })	Invoke a function
TriggerAction.Void()	Fire-and-forget invocation mode
TriggerAction.Enqueue({ queue })	Durable async invocation mode
Logger	Structured logging
withSpan, getTracer, getMeter	OpenTelemetry instrumentation
createChannel()	Binary streaming between workers
createStream(name, adapter)	Custom stream implementation
registerTriggerType(id, handler)	Custom trigger type registration
Pattern Boundaries
For usage patterns and working examples, see iii-functions-and-triggers
For HTTP endpoint patterns, see iii-http-endpoints
For Python SDK, see iii-python-sdk
For Rust SDK, see iii-rust-sdk
Weekly Installs
121
Repository
iii-hq/skills
GitHub Stars
6
First Seen
Mar 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass