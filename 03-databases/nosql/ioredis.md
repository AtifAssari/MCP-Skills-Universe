---
rating: ⭐⭐
title: ioredis
url: https://skills.sh/jgamaraalv/ts-dev-kit/ioredis
---

# ioredis

skills/jgamaraalv/ts-dev-kit/ioredis
ioredis
Installation
$ npx skills add https://github.com/jgamaraalv/ts-dev-kit --skill ioredis
SKILL.md
ioredis v5 — Node.js Redis Client

ioredis v5.x. Requires Node.js >= 12, Redis >= 2.6.12. 100% TypeScript.

<quick_reference>

Critical: Import Style
// CORRECT — named import (required for NodeNext / moduleResolution: "nodenext")
import { Redis } from "ioredis";

// For Cluster:
import { Redis, Cluster } from "ioredis";

Quick Reference
Operation	Code
Connect	new Redis() or new Redis(6379, "host") or new Redis("redis://...")
Get/Set	await redis.set("key", "val") / await redis.get("key")
Pipeline	await redis.pipeline().set("a","1").get("a").exec()
Transaction	await redis.multi().set("a","1").get("a").exec()
Pub/Sub	sub.subscribe("ch") / sub.on("message", cb) / pub.publish("ch", msg)
Lua script	redis.defineCommand("name", { numberOfKeys: 1, lua: "..." })
Scan	redis.scanStream({ match: "prefix:*", count: 100 })
Graceful close	await redis.quit()
Force close	redis.disconnect()

</quick_reference>

Common Gotchas
Named import: Always import { Redis } from "ioredis" with NodeNext resolution
Pub/Sub isolation: A subscribed client cannot run other commands — use separate instances
maxRetriesPerRequest: Default is 20. Set to null for infinite retries (required by BullMQ)
Pipeline errors: pipeline.exec() never rejects — errors are in each result's [0] position
showFriendlyErrorStack: Performance cost — never enable in production
Cluster pipelines: All keys in a pipeline must hash to slots served by the same node
enableAutoPipelining: 35-50% throughput improvement, safe to enable globally
When to Load References
Need	Reference file
Connection setup, RedisOptions, TLS, retryStrategy, lifecycle	references/connection-options.md
Core API: pipelines, transactions, Pub/Sub, Lua scripting, scanning, events	references/core-api.md
Streams, auto-pipelining, transformers, binary data, error handling, debugging	references/advanced-patterns.md
Redis Cluster setup, ClusterOptions, Sentinel config, failover	references/cluster-sentinel.md
Weekly Installs
32
Repository
jgamaraalv/ts-dev-kit
GitHub Stars
14
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass