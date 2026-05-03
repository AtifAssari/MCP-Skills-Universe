---
title: trigger-tasks
url: https://skills.sh/triggerdotdev/skills/trigger-tasks
---

# trigger-tasks

skills/triggerdotdev/skills/trigger-tasks
trigger-tasks
Installation
$ npx skills add https://github.com/triggerdotdev/skills --skill trigger-tasks
Summary

Durable background tasks with automatic retries, queuing, scheduling, and observability for AI agents and workflows.

Create tasks with built-in retry logic, exponential backoff, and error handling; supports schema validation with Zod for type-safe payloads
Trigger tasks from backend code or within other tasks, with options for fire-and-forget, wait-for-result, or batch processing up to 1,000 items
Manage concurrency and queuing per-task or per-tenant, debounce rapid triggers, and enforce idempotency to prevent duplicate work
Schedule recurring tasks with cron expressions and timezone support, or create dynamic multi-tenant schedules on demand
Track progress and metadata in real-time, tag runs for filtering, and scale compute with machine presets from micro to large-2x configurations
SKILL.md
Trigger.dev Tasks

Build durable background tasks that run reliably with automatic retries, queuing, and observability.

When to Use
Creating background jobs or async workflows
Building AI agents that need long-running execution
Processing webhooks, emails, or file uploads
Scheduling recurring tasks (cron)
Any work that shouldn't block your main application
Critical Rules
Always use @trigger.dev/sdk — never use deprecated client.defineJob
Check result.ok before accessing result.output from triggerAndWait()
Never use Promise.all with triggerAndWait() or wait.* calls
Export tasks from files in your trigger/ directory
Basic Task
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

Schema Task (Validated Input)
import { schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";

export const validatedTask = schemaTask({
  id: "validated-task",
  schema: z.object({
    name: z.string(),
    email: z.string().email(),
  }),
  run: async (payload) => {
    // payload is typed and validated
    return { message: `Hello ${payload.name}` };
  },
});

Triggering Tasks
From Backend Code
import { tasks } from "@trigger.dev/sdk";
import type { processData } from "./trigger/tasks";

// Single trigger (fire and forget)
const handle = await tasks.trigger<typeof processData>("process-data", {
  userId: "123",
  data: [{ id: 1 }],
});

// Batch trigger (up to 1,000 items, 3MB per payload)
const batchHandle = await tasks.batchTrigger<typeof processData>("process-data", [
  { payload: { userId: "123", data: [] } },
  { payload: { userId: "456", data: [] } },
]);

From Inside Tasks
export const parentTask = task({
  id: "parent-task",
  run: async (payload) => {
    // Fire and forget
    const handle = await childTask.trigger({ data: "value" });

    // Wait for result - returns Result object, NOT direct output
    const result = await childTask.triggerAndWait({ data: "value" });
    if (result.ok) {
      console.log("Output:", result.output);
    } else {
      console.error("Failed:", result.error);
    }

    // Quick unwrap (throws on error)
    const output = await childTask.triggerAndWait({ data: "value" }).unwrap();

    // Batch with wait
    const results = await childTask.batchTriggerAndWait([
      { payload: { data: "item1" } },
      { payload: { data: "item2" } },
    ]);
  },
});

Waits
import { task, wait } from "@trigger.dev/sdk";

export const taskWithWaits = task({
  id: "task-with-waits",
  run: async (payload) => {
    await wait.for({ seconds: 30 });
    await wait.for({ minutes: 5 });
    await wait.until({ date: new Date("2024-12-25") });

    // Wait for external approval
    await wait.forToken({
      token: "user-approval-token",
      timeoutInSeconds: 3600,
    });
  },
});


Waits > 5 seconds are checkpointed and don't count toward compute.

Concurrency & Queues
import { task, queue } from "@trigger.dev/sdk";

// Shared queue
const emailQueue = queue({
  name: "email-processing",
  concurrencyLimit: 5,
});

// Task-level concurrency
export const oneAtATime = task({
  id: "sequential-task",
  queue: { concurrencyLimit: 1 },
  run: async (payload) => {
    // Only one instance runs at a time
  },
});

// Use shared queue
export const emailTask = task({
  id: "send-email",
  queue: emailQueue,
  run: async (payload) => {},
});

// Per-tenant concurrency (at trigger time)
await childTask.trigger(payload, {
  queue: {
    name: `user-${userId}`,
    concurrencyLimit: 2,
  },
});

Debouncing

Consolidate rapid triggers into a single execution:

await myTask.trigger(
  { userId: "123" },
  {
    debounce: {
      key: "user-123-update",
      delay: "5s",
      mode: "trailing", // Use latest payload (default: "leading")
    },
  }
);

Idempotency
import { task, idempotencyKeys } from "@trigger.dev/sdk";

export const paymentTask = task({
  id: "process-payment",
  run: async (payload: { orderId: string }) => {
    const key = await idempotencyKeys.create(`payment-${payload.orderId}`);

    await chargeCustomer.trigger(payload, {
      idempotencyKey: key,
      idempotencyKeyTTL: "24h",
    });
  },
});

Error Handling & Retries
import { task, retry, AbortTaskRunError } from "@trigger.dev/sdk";

export const resilientTask = task({
  id: "resilient-task",
  retry: {
    maxAttempts: 10,
    factor: 1.8,
    minTimeoutInMs: 500,
    maxTimeoutInMs: 30_000,
  },
  catchError: async ({ error, ctx }) => {
    if (error.code === "FATAL_ERROR") {
      throw new AbortTaskRunError("Cannot retry");
    }
    return { retryAt: new Date(Date.now() + 60000) };
  },
  run: async (payload) => {
    // Retry specific operations
    const result = await retry.onThrow(
      async () => unstableApiCall(payload),
      { maxAttempts: 3 }
    );

    // HTTP retries with conditions
    const response = await retry.fetch("https://api.example.com", {
      retry: {
        maxAttempts: 5,
        condition: (res, err) => res?.status === 429 || res?.status >= 500,
      },
    });
  },
});

Scheduled Tasks (Cron)
import { schedules } from "@trigger.dev/sdk";

// Declarative schedule
export const dailyTask = schedules.task({
  id: "daily-cleanup",
  cron: "0 0 * * *", // Midnight UTC
  run: async (payload) => {
    // payload.timestamp - scheduled time
    // payload.timezone - IANA timezone
    // payload.scheduleId - schedule identifier
  },
});

// With timezone
export const tokyoTask = schedules.task({
  id: "tokyo-morning",
  cron: { pattern: "0 9 * * *", timezone: "Asia/Tokyo" },
  run: async () => {},
});

// Dynamic/multi-tenant schedules
await schedules.create({
  task: "reminder-task",
  cron: "0 8 * * *",
  timezone: "America/New_York",
  externalId: userId,
  deduplicationKey: `${userId}-daily`,
});

Metadata & Progress
import { task, metadata } from "@trigger.dev/sdk";

export const batchProcessor = task({
  id: "batch-processor",
  run: async (payload: { items: any[] }) => {
    metadata.set("progress", 0).set("total", payload.items.length);

    for (let i = 0; i < payload.items.length; i++) {
      await processItem(payload.items[i]);
      metadata.set("progress", ((i + 1) / payload.items.length) * 100);
    }

    metadata.set("status", "completed");
  },
});

Tags
import { task, tags } from "@trigger.dev/sdk";

export const processUser = task({
  id: "process-user",
  run: async (payload: { userId: string }) => {
    await tags.add(`user_${payload.userId}`);
  },
});

// Trigger with tags
await processUser.trigger(
  { userId: "123" },
  { tags: ["priority", "user_123"] }
);

Machine Presets
export const heavyTask = task({
  id: "heavy-computation",
  machine: { preset: "large-2x" }, // 8 vCPU, 16 GB RAM
  maxDuration: 1800, // 30 minutes
  run: async (payload) => {},
});

Preset	vCPU	RAM
micro	0.25	0.25 GB
small-1x	0.5	0.5 GB (default)
small-2x	1	1 GB
medium-1x	1	2 GB
medium-2x	2	4 GB
large-1x	4	8 GB
large-2x	8	16 GB
Best Practices
Make tasks idempotent — safe to retry without side effects
Use queues to prevent overwhelming external services
Configure appropriate retries with exponential backoff
Track progress with metadata for long-running tasks
Use debouncing for user activity and webhook bursts
Match machine size to computational requirements

See references/ for detailed documentation on each feature.

Weekly Installs
1.4K
Repository
triggerdotdev/skills
GitHub Stars
25
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass