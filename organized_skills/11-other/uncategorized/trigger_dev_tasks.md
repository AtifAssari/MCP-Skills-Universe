---
rating: ⭐⭐
title: trigger-dev-tasks
url: https://skills.sh/triggerdotdev/trigger.dev/trigger-dev-tasks
---

# trigger-dev-tasks

skills/triggerdotdev/trigger.dev/trigger-dev-tasks
trigger-dev-tasks
Installation
$ npx skills add https://github.com/triggerdotdev/trigger.dev --skill trigger-dev-tasks
SKILL.md
Trigger.dev Task Expert

You are an expert Trigger.dev developer specializing in building production-grade background job systems. Tasks deployed to Trigger.dev run in Node.js 21+ and use the @trigger.dev/sdk package.

Critical Rules
Always use @trigger.dev/sdk - Never use @trigger.dev/sdk/v3 or deprecated client.defineJob pattern
Never use node-fetch - Use the built-in fetch function
Export all tasks - Every task must be exported, including subtasks
Never wrap wait/trigger calls in Promise.all - triggerAndWait, batchTriggerAndWait, and wait.* calls cannot be wrapped in Promise.all or Promise.allSettled
Basic Task Pattern
import { task } from "@trigger.dev/sdk";

export const processData = task({
  id: "process-data",
  retry: {
    maxAttempts: 10,
    factor: 1.8,
    minTimeoutInMs: 500,
    maxTimeoutInMs: 30_000,
  },
  run: async (payload: { userId: string; data: any[] }) => {
    console.log(`Processing ${payload.data.length} items`);
    return { processed: payload.data.length };
  },
});

Schema Task (with validation)
import { schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";

export const validatedTask = schemaTask({
  id: "validated-task",
  schema: z.object({
    name: z.string(),
    email: z.string().email(),
  }),
  run: async (payload) => {
    // Payload is automatically validated and typed
    return { message: `Hello ${payload.name}` };
  },
});

Triggering Tasks
From Backend Code (type-only import to prevent dependency leakage)
import { tasks } from "@trigger.dev/sdk";
import type { processData } from "./trigger/tasks";

const handle = await tasks.trigger<typeof processData>("process-data", {
  userId: "123",
  data: [{ id: 1 }],
});

From Inside Tasks
export const parentTask = task({
  id: "parent-task",
  run: async (payload) => {
    // Trigger and wait - returns Result object, NOT direct output
    const result = await childTask.triggerAndWait({ data: "value" });
    if (result.ok) {
      console.log("Output:", result.output);
    } else {
      console.error("Failed:", result.error);
    }

    // Or unwrap directly (throws on error)
    const output = await childTask.triggerAndWait({ data: "value" }).unwrap();
  },
});

Idempotency (Critical for Retries)

Always use idempotency keys when triggering tasks from inside other tasks:

import { idempotencyKeys } from "@trigger.dev/sdk";

export const paymentTask = task({
  id: "process-payment",
  run: async (payload: { orderId: string }) => {
    // Scoped to current run - survives retries
    const key = await idempotencyKeys.create(`payment-${payload.orderId}`);

    await chargeCustomer.trigger(payload, {
      idempotencyKey: key,
      idempotencyKeyTTL: "24h",
    });
  },
});

Trigger Options
await myTask.trigger(payload, {
  delay: "1h",           // Delay execution
  ttl: "10m",            // Cancel if not started within TTL
  idempotencyKey: key,
  queue: "my-queue",
  machine: "large-1x",   // micro, small-1x, small-2x, medium-1x, medium-2x, large-1x, large-2x
  maxAttempts: 3,
  tags: ["user_123"],    // Max 10 tags
  debounce: {            // Consolidate rapid triggers
    key: "unique-key",
    delay: "5s",
    mode: "trailing",    // "leading" (default) or "trailing"
  },
});

Debouncing

Consolidate multiple triggers into a single execution:

// Rapid triggers with same key = single execution
await myTask.trigger({ userId: "123" }, {
  debounce: {
    key: "user-123-update",
    delay: "5s",
  },
});

// Trailing mode: use payload from LAST trigger
await myTask.trigger({ data: "latest" }, {
  debounce: {
    key: "my-key",
    delay: "10s",
    mode: "trailing",
  },
});


Use cases: user activity updates, webhook deduplication, search indexing, notification batching.

Batch Triggering

Up to 1,000 items per batch, 3MB per payload:

const results = await myTask.batchTriggerAndWait([
  { payload: { userId: "1" } },
  { payload: { userId: "2" } },
]);

for (const result of results) {
  if (result.ok) console.log(result.output);
}

Machine Presets
Preset	vCPU	Memory
micro	0.25	0.25GB
small-1x	0.5	0.5GB
small-2x	1	1GB
medium-1x	1	2GB
medium-2x	2	4GB
large-1x	4	8GB
large-2x	8	16GB
Design Principles
Break complex workflows into subtasks that can be independently retried and made idempotent
Don't over-complicate - Sometimes Promise.allSettled inside a single task is better than many subtasks (each task has dedicated process and is charged by millisecond)
Always configure retries - Set appropriate maxAttempts based on the operation
Use idempotency keys - Especially for payment/critical operations
Group related subtasks - Keep subtasks only used by one parent in the same file, don't export them
Use logger - Log at key execution points with logger.info(), logger.error(), etc.
Reference Documentation

For detailed documentation on specific topics, read these files:

basic-tasks.md - Task basics, triggering, waits
advanced-tasks.md - Tags, queues, concurrency, metadata, error handling
scheduled-tasks.md - Cron schedules, declarative and imperative
realtime.md - Real-time subscriptions, streams, React hooks
config.md - trigger.config.ts, build extensions (Prisma, Playwright, FFmpeg, etc.)
Weekly Installs
175
Repository
triggerdotdev/t…gger.dev
GitHub Stars
14.7K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn