---
rating: ⭐⭐
title: outpost
url: https://skills.sh/hookdeck/webhook-skills/outpost
---

# outpost

skills/hookdeck/webhook-skills/outpost
outpost
Installation
$ npx skills add https://github.com/hookdeck/webhook-skills --skill outpost
SKILL.md
Hookdeck Outpost

Outpost is open-source infrastructure for delivering events to user-preferred destinations: Webhooks (HTTP), SQS, RabbitMQ, Pub/Sub, EventBridge, Kafka, and more. Apache 2.0 licensed, available as managed by Hookdeck or self-hosted.

When to Use Outpost
You're building a SaaS or API platform and need to send webhooks to your users
You need multi-destination support beyond HTTP webhooks (SQS, RabbitMQ, Pub/Sub, EventBridge, Kafka)
You want self-hostable webhook delivery infrastructure
You need multi-tenant support with per-user observability
You want to offer your customers reliable, retryable event delivery
Quick Start
Managed (Hookdeck)

The fastest way to get started — Hookdeck hosts and operates Outpost for you:

Sign up at hookdeck.com
See the Send Webhooks quickstart
Self-Hosted

Run Outpost on your own infrastructure:

See the Outpost documentation
Clone from GitHub
Supported Destinations
Destination	Protocol
Webhooks	HTTP/HTTPS
Amazon SQS	AWS SQS
RabbitMQ	AMQP
Google Pub/Sub	gRPC
Amazon EventBridge	AWS EventBridge
Apache Kafka	Kafka protocol
Full Product Skills

For detailed Outpost skills:

npx skills add hookdeck/agent-skills --skill outpost


See hookdeck/agent-skills for the complete Outpost skill, the Outpost documentation, and the GitHub repo.

Resources
Outpost Documentation
GitHub Repository
Hookdeck Send Webhooks Guide
Related Skills
hookdeck-event-gateway - For receiving and ingesting webhooks (the inbound counterpart)
hookdeck-event-gateway-webhooks - Verify Hookdeck signatures on forwarded webhooks
webhook-handler-patterns - Handler sequence, idempotency, error handling, retry logic
Weekly Installs
60
Repository
hookdeck/webhook-skills
GitHub Stars
69
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass