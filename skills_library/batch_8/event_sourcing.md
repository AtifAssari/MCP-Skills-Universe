---
title: event-sourcing
url: https://skills.sh/aj-geddes/useful-ai-prompts/event-sourcing
---

# event-sourcing

skills/aj-geddes/useful-ai-prompts/event-sourcing
event-sourcing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill event-sourcing
SKILL.md
Event Sourcing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Store state changes as a sequence of events rather than the current state, enabling temporal queries, audit trails, and event replay.

When to Use
Audit trail requirements
Temporal queries (state at any point in time)
Event-driven microservices
CQRS implementations
Financial systems
Complex domain models
Debugging and analysis
Compliance and regulation
Quick Start

Minimal working example:

interface DomainEvent {
  id: string;
  aggregateId: string;
  aggregateType: string;
  eventType: string;
  data: any;
  metadata: {
    userId?: string;
    timestamp: number;
    version: number;
  };
}

interface Aggregate {
  id: string;
  version: number;
}

class EventStore {
  private events: DomainEvent[] = [];

  async appendEvents(
    aggregateId: string,
    expectedVersion: number,
    events: Omit<DomainEvent, "id" | "metadata">[],
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Event Store (TypeScript)	Event Store (TypeScript)
Projections (Read Models)	Projections (Read Models)
Event Store with PostgreSQL	Event Store with PostgreSQL
Snapshots for Performance	Snapshots for Performance
Best Practices
✅ DO
Store events immutably
Version your events
Use optimistic concurrency
Create snapshots for performance
Use projections for queries
Keep events small and focused
Include metadata (timestamp, user, etc.)
Handle event versioning/migration
❌ DON'T
Mutate past events
Store current state only
Skip concurrency checks
Query event store for reads
Make events too large
Forget about event schema evolution
Weekly Installs
431
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass