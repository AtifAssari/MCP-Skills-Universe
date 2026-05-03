---
title: durable-objects
url: https://skills.sh/site/developers.cloudflare.com/durable-objects
---

# durable-objects

skills/developers.cloudflare.com/durable-objects
durable-objects
$ npx skills add https://developers.cloudflare.com
SKILL.md
Durable Objects

Build stateful, coordinated applications on Cloudflare's edge using Durable Objects.

Retrieval Sources

Your knowledge of Durable Objects APIs and configuration may be outdated. Prefer retrieval over pre-training for any Durable Objects task.

Resource	URL
Docs	https://developers.cloudflare.com/durable-objects/
API Reference	https://developers.cloudflare.com/durable-objects/api/
Best Practices	https://developers.cloudflare.com/durable-objects/best-practices/
Examples	https://developers.cloudflare.com/durable-objects/examples/

Fetch the relevant doc page when implementing features.

When to Use
Creating new Durable Object classes for stateful coordination
Implementing RPC methods, alarms, or WebSocket handlers
Reviewing existing DO code for best practices
Configuring wrangler.jsonc/toml for DO bindings and migrations
Writing tests with @cloudflare/vitest-pool-workers
Designing sharding strategies and parent-child relationships
Reference Documentation
./references/rules.md - Core rules, storage, concurrency, RPC, alarms
./references/testing.md - Vitest setup, unit/integration tests, alarm testing
./references/workers.md - Workers handlers, types, wrangler config, observability

Search: blockConcurrencyWhile, idFromName, getByName, setAlarm, sql.exec

Core Principles
Use Durable Objects For
Need	Example
Coordination	Chat rooms, multiplayer games, collaborative docs
Strong consistency	Inventory, booking systems, turn-based games
Per-entity storage	Multi-tenant SaaS, per-user data
Persistent connections	WebSockets, real-time notifications
Scheduled work per entity	Subscription renewals, game timeouts
Do NOT Use For
Stateless request handling (use plain Workers)
Maximum global distribution needs
High fan-out independent requests
Quick Reference
Wrangler Configuration
// wrangler.jsonc
{
  "durable_objects": {
    "bindings": [{ "name": "MY_DO", "class_name": "MyDurableObject" }]
  },
  "migrations": [{ "tag": "v1", "new_sqlite_classes": ["MyDurableObject"] }]
}

Basic Durable Object Pattern
import { DurableObject } from "cloudflare:workers";

export interface Env {
  MY_DO: DurableObjectNamespace<MyDurableObject>;
}

export class MyDurableObject extends DurableObject<Env> {
  constructor(ctx: DurableObjectState, env: Env) {
    super(ctx, env);
    ctx.blockConcurrencyWhile(async () => {
      this.ctx.storage.sql.exec(`
        CREATE TABLE IF NOT EXISTS items (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          data TEXT NOT NULL
        )
      `);
    });
  }

  async addItem(data: string): Promise<number> {
    const result = this.ctx.storage.sql.exec<{ id: number }>(
      "INSERT INTO items (data) VALUES (?) RETURNING id",
      data
    );
    return result.one().id;
  }
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const stub = env.MY_DO.getByName("my-instance");
    const id = await stub.addItem("hello");
    return Response.json({ id });
  },
};

Critical Rules
Model around coordination atoms - One DO per chat room/game/user, not one global DO
Use getByName() for deterministic routing - Same input = same DO instance
Use SQLite storage - Configure new_sqlite_classes in migrations
Initialize in constructor - Use blockConcurrencyWhile() for schema setup only
Use RPC methods - Not fetch() handler (compatibility date >= 2024-04-03)
Persist first, cache second - Always write to storage before updating in-memory state
One alarm per DO - setAlarm() replaces any existing alarm
Anti-Patterns (NEVER)
Single global DO handling all requests (bottleneck)
Using blockConcurrencyWhile() on every request (kills throughput)
Storing critical state only in memory (lost on eviction/crash)
Using await between related storage writes (breaks atomicity)
Holding blockConcurrencyWhile() across fetch() or external I/O
Stub Creation
// Deterministic - preferred for most cases
const stub = env.MY_DO.getByName("room-123");

// From existing ID string
const id = env.MY_DO.idFromString(storedIdString);
const stub = env.MY_DO.get(id);

// New unique ID - store mapping externally
const id = env.MY_DO.newUniqueId();
const stub = env.MY_DO.get(id);

Storage Operations
// SQL (synchronous, recommended)
this.ctx.storage.sql.exec("INSERT INTO t (c) VALUES (?)", value);
const rows = this.ctx.storage.sql.exec<Row>("SELECT * FROM t").toArray();

// KV (async)
await this.ctx.storage.put("key", value);
const val = await this.ctx.storage.get<Type>("key");

Alarms
// Schedule (replaces existing)
await this.ctx.storage.setAlarm(Date.now() + 60_000);

// Handler
async alarm(): Promise<void> {
  // Process scheduled work
  // Optionally reschedule: await this.ctx.storage.setAlarm(...)
}

// Cancel
await this.ctx.storage.deleteAlarm();

Testing Quick Start
import { env } from "cloudflare:test";
import { describe, it, expect } from "vitest";

describe("MyDO", () => {
  it("should work", async () => {
    const stub = env.MY_DO.getByName("test");
    const result = await stub.addItem("test");
    expect(result).toBe(1);
  });
});

Weekly Installs
347
Source
developers.clou…lare.com
First Seen
Feb 28, 2026
Security Audits
SocketPass