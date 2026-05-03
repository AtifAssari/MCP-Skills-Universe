---
rating: ⭐⭐
title: litestar-channels
url: https://skills.sh/alti3/litestar-skills/litestar-channels
---

# litestar-channels

skills/alti3/litestar-skills/litestar-channels
litestar-channels
Installation
$ npx skills add https://github.com/alti3/litestar-skills --skill litestar-channels
SKILL.md
Channels
Execution Workflow
Choose the backend and durability model first: in-memory, Redis Pub/Sub, Redis Streams, or Postgres-backed variants.
Define channel names or intentionally allow arbitrary channels.
Publish events from domain boundaries through the injected channels plugin.
Manage subscriber lifecycle explicitly with start_subscription(), subscribe(), unsubscribe(), and cleanup.
Decide whether history and backpressure need configuration before traffic arrives.
Integrate with websocket handlers directly or generate websocket route handlers through the plugin.
Core Rules
Treat ChannelsPlugin as the central routing and fanout component.
Keep event payloads compact, versionable, and transport-agnostic.
Use the injected channels dependency instead of importing global plugin instances inside handlers.
Choose the backend based on inter-process needs, latency, and history requirements.
Configure backpressure intentionally when slow subscribers are possible.
Prefer run_in_background() over manual iter_events() loops when concurrent websocket receive work is required.
Keep history replay bounded so subscribers do not drown in backlog immediately after connecting.
Decision Guide
Use MemoryChannelsBackend for local development, tests, and single-process deployments.
Use RedisChannelsPubSubBackend when low-latency fanout matters more than history.
Use RedisChannelsStreamBackend when history replay is required.
Use generated websocket route handlers when each channel maps cleanly to a websocket subscription endpoint.
Use manual websocket integration when authentication, multiplexing, or bidirectional behavior is more custom.
Reference Files

Read only the sections you need:

For plugin configuration, publishing, subscription management, subscriber iteration, history replay, and direct websocket integration, read references/plugin-and-subscriber-patterns.md.
For backend selection, backpressure strategy, and generated websocket route handlers, read references/backends-and-routing.md.
Recommended Defaults
Define known channels up front unless arbitrary channel creation is part of the product.
Publish from application services or domain events, not ad hoc transport code.
Keep subscriber callbacks small and idempotent where retries or duplicate delivery are possible.
Use bounded history and backlog settings when subscriber speed can vary materially.
Reach for websocket integration only after the core event-stream model is sound.
Anti-Patterns
Using channels when a single websocket connection with no fanout requirements would do.
Publishing transport-specific payloads that make backend or consumer reuse hard.
Ignoring backpressure in systems with bursty or slow consumers.
Iterating iter_events() beside a websocket receive loop without understanding disconnect risks.
Turning on arbitrary channels without a naming, authorization, or lifecycle strategy.
Validation Checklist
Confirm backend choice matches latency, durability, and history needs.
Confirm channel names and authorization expectations are explicit.
Confirm publish paths work through the injected plugin.
Confirm subscriber lifecycle is cleaned up on disconnect and shutdown.
Confirm history replay and backlog settings cannot overwhelm new subscribers.
Confirm websocket integration handles disconnects without hanging.
Confirm generated websocket route handlers match the intended channel topology.
Cross-Skill Handoffs
Use litestar-websockets for client-facing websocket contract design and handler selection.
Use litestar-testing for subscriber, history, and websocket-fanout test coverage.
Use litestar-metrics and litestar-logging for throughput, lag, and delivery observability.
Use litestar-dependency-injection when publishers or subscriber callbacks need injected services.
Litestar References
https://docs.litestar.dev/latest/usage/channels.html
https://docs.litestar.dev/latest/reference/channels/plugin.html
https://docs.litestar.dev/latest/reference/channels/subscriber.html
Weekly Installs
15
Repository
alti3/litestar-skills
GitHub Stars
5
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass