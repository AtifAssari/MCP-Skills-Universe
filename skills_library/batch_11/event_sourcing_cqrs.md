---
title: event-sourcing-cqrs
url: https://skills.sh/claude-dev-suite/claude-dev-suite/event-sourcing-cqrs
---

# event-sourcing-cqrs

skills/claude-dev-suite/claude-dev-suite/event-sourcing-cqrs
event-sourcing-cqrs
Installation
$ npx skills add https://github.com/claude-dev-suite/claude-dev-suite --skill event-sourcing-cqrs
SKILL.md
Event Sourcing & CQRS
Core Concepts
Command ──▶ Command Handler ──▶ Aggregate ──▶ Events ──▶ Event Store
                                                           │
                                                    ┌──────┘
                                                    ▼
                                              Projections ──▶ Read Models ──▶ Queries

Event Sourcing (TypeScript)
Event Store
interface DomainEvent {
  eventId: string;
  aggregateId: string;
  type: string;
  data: unknown;
  version: number;
  timestamp: Date;
}

class EventStore {
  async append(aggregateId: string, events: DomainEvent[], expectedVersion: number): Promise<void> {
    // Optimistic concurrency: check current version matches expected
    const current = await this.getCurrentVersion(aggregateId);
    if (current !== expectedVersion) throw new ConcurrencyError(aggregateId);

    await db.events.createMany({
      data: events.map((e, i) => ({ ...e, version: expectedVersion + i + 1 })),
    });
  }

  async getEvents(aggregateId: string): Promise<DomainEvent[]> {
    return db.events.findMany({
      where: { aggregateId },
      orderBy: { version: 'asc' },
    });
  }
}

Event-Sourced Aggregate
class OrderAggregate {
  private id!: string;
  private status!: string;
  private items: OrderItem[] = [];
  private version = 0;
  private uncommittedEvents: DomainEvent[] = [];

  static fromHistory(events: DomainEvent[]): OrderAggregate {
    const aggregate = new OrderAggregate();
    events.forEach((e) => aggregate.apply(e, false));
    return aggregate;
  }

  createOrder(id: string, items: OrderItem[]) {
    this.apply({ type: 'OrderCreated', data: { id, items } }, true);
  }

  confirmOrder() {
    if (this.status !== 'pending') throw new DomainError('Cannot confirm');
    this.apply({ type: 'OrderConfirmed', data: { id: this.id } }, true);
  }

  private apply(event: Partial<DomainEvent>, isNew: boolean) {
    switch (event.type) {
      case 'OrderCreated':
        this.id = event.data.id;
        this.items = event.data.items;
        this.status = 'pending';
        break;
      case 'OrderConfirmed':
        this.status = 'confirmed';
        break;
    }
    this.version++;
    if (isNew) this.uncommittedEvents.push(event as DomainEvent);
  }
}

CQRS
Command Side
class ConfirmOrderHandler {
  constructor(private eventStore: EventStore) {}

  async handle(cmd: ConfirmOrderCommand): Promise<void> {
    const events = await this.eventStore.getEvents(cmd.orderId);
    const aggregate = OrderAggregate.fromHistory(events);

    aggregate.confirmOrder();

    await this.eventStore.append(
      cmd.orderId,
      aggregate.uncommittedEvents,
      aggregate.version - aggregate.uncommittedEvents.length,
    );
  }
}

Query Side (Projection)
class OrderProjection {
  async handle(event: DomainEvent): Promise<void> {
    switch (event.type) {
      case 'OrderCreated':
        await readDb.orders.create({
          data: { id: event.data.id, status: 'pending', total: calcTotal(event.data.items) },
        });
        break;
      case 'OrderConfirmed':
        await readDb.orders.update({
          where: { id: event.aggregateId },
          data: { status: 'confirmed', confirmedAt: event.timestamp },
        });
        break;
    }
  }
}

Snapshots (for long event streams)
async function loadAggregate(id: string): Promise<OrderAggregate> {
  const snapshot = await snapshotStore.getLatest(id);
  const events = await eventStore.getEvents(id, snapshot?.version ?? 0);

  const aggregate = snapshot
    ? OrderAggregate.fromSnapshot(snapshot)
    : new OrderAggregate();

  events.forEach((e) => aggregate.apply(e, false));
  return aggregate;
}

Anti-Patterns
Anti-Pattern	Fix
Querying event store for reads	Build read models via projections
No optimistic concurrency	Check expected version on append
Deleting events	Events are immutable; use compensating events
Projections coupled to write model	Projections consume events independently
No snapshots for long streams	Snapshot every N events (e.g., 100)
Production Checklist
 Event store with optimistic concurrency
 Projections for each read model
 Snapshots for aggregates with many events
 Idempotent projection handlers
 Event versioning strategy (upcasting)
 Monitoring: projection lag, event throughput
Weekly Installs
27
Repository
claude-dev-suit…ev-suite
GitHub Stars
12
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass