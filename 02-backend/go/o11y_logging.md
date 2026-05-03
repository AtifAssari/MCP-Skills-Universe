---
title: o11y-logging
url: https://skills.sh/joelhooks/joelclaw/o11y-logging
---

# o11y-logging

skills/joelhooks/joelclaw/o11y-logging
o11y-logging
Installation
$ npx skills add https://github.com/joelhooks/joelclaw --skill o11y-logging
SKILL.md
JoelClaw Observability + Logging

Prevent silent failure by default. Observability is not optional polish: it is part of done.

Non-Negotiable Rules
Use the canonical event contract only.
packages/system-bus/src/observability/otel-event.ts
packages/system-bus/src/observability/emit.ts
packages/system-bus/src/observability/store.ts
Worker/Inngest code emits through emitOtelEvent or emitMeasuredOtelEvent.
Gateway code emits through emitGatewayOtel.
Internal ingestion goes through POST /observability/emit (packages/system-bus/src/serve.ts), not ad-hoc writes.
Never treat console.log as primary observability. Keep structured events as source of truth.
High-cardinality values go in metadata, not in facet fields (source, component, level, success).
Failures must set success: false with a meaningful error.
For warn/error/fatal, verify Convex mirror behavior (rolling window) in addition to Typesense write.
In Inngest durable functions, any "emit once" telemetry must live inside step.run(...) to avoid replay duplication after resume.
Event Conventions
source: subsystem (worker, gateway, webhook, memory, verification, etc.)
component: stable module/service name (check-system-health, redis-channel, observe)
action: stable dotted action (system.health.checked, events.immediate_telegram)
metadata: request IDs, deployment IDs, function IDs, session IDs, payload identifiers
duration_ms: include for timed operations

Use event-per-hop (wide event style): one context-rich event for each major boundary/operation, not scattered string logs.

Implementation Workflow
Identify the boundary being changed.
Inngest function, gateway channel, webhook route, API route, background job, sync step.
Add success and failure envelopes.
Start + completion for long tasks, or a single completion event for short tasks.
Include operational and business context in metadata.
Example: function id, event id, provider, queue depth, affected resource id.
Keep severity useful.
debug/info for normal activity, warn for degraded but recoverable, error/fatal for failures.
Run verification gates before finishing.

For full checklists and command recipes, read references/implementation-checklist.md.

Quick Patterns
Worker / Inngest timed operation
import { emitMeasuredOtelEvent } from "../../observability/emit";

await emitMeasuredOtelEvent(
  {
    level: "info",
    source: "worker",
    component: "content-sync",
    action: "content_sync.run",
    metadata: { trigger: event.name },
  },
  async () => {
    await runSync();
  }
);

Gateway emission
import { emitGatewayOtel } from "../observability";

await emitGatewayOtel({
  level: "error",
  component: "redis-channel",
  action: "events.immediate_telegram",
  success: false,
  error: "telegram_send_failed",
  metadata: { sessionId, queueDepth },
});

Definition of Done
Structured OTEL events added for the changed path.
No direct feature-level writes to Typesense/Convex for observability data.
Smoke probe passes (scripts/otel-smoke.sh).
joelclaw otel list and joelclaw otel stats show expected behavior.
New failure modes are queryable by source, component, and action.
Inngest Replay + Hang Triage

Use this when step code appears to run but runs remain RUNNING/CANCELLED with Finalization errors.

Inspect run trace first.
joelclaw run <run-id>


Look for errors.Finalization.stack containing Unable to reach SDK URL.

Confirm whether this is true network reachability or worker-side blocking.
joelclaw inngest status
joelclaw logs worker --lines 200
joelclaw logs errors --lines 200

Check for replay-noise in OTEL.

If an action that should emit once (for example manifest.archive.prereqs-passed) appears hundreds of times in one run window, move that emit into its own step.run.

joelclaw otel search "manifest.archive.prereqs-passed" --hours 1

Treat Unable to reach SDK URL as an ambiguous symptom.

It can indicate ingress problems, but in practice it can also happen when a function handler blocks on local IO/dependencies long enough that finalization cannot complete.

Helper Script

Use scripts/otel-smoke.sh for a fast end-to-end probe:

./skills/o11y-logging/scripts/otel-smoke.sh verification o11y-skill probe.emit

Key Files
packages/system-bus/src/observability/otel-event.ts
packages/system-bus/src/observability/emit.ts
packages/system-bus/src/observability/store.ts
packages/system-bus/src/serve.ts
packages/gateway/src/observability.ts
packages/system-bus/src/inngest/functions/check-system-health.ts
packages/cli/src/commands/otel.ts
apps/web/app/api/otel/route.ts
Weekly Installs
30
Repository
joelhooks/joelclaw
GitHub Stars
55
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass