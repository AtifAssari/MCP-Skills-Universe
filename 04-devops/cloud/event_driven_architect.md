---
title: event-driven-architect
url: https://skills.sh/404kidwiz/claude-supercode-skills/event-driven-architect
---

# event-driven-architect

skills/404kidwiz/claude-supercode-skills/event-driven-architect
event-driven-architect
Installation
$ npx skills add https://github.com/404kidwiz/claude-supercode-skills --skill event-driven-architect
SKILL.md
Event-Driven Architect
Purpose

Provides expertise in designing and implementing event-driven architectures. Covers message brokers, event sourcing, CQRS, and standards like CloudEvents and AsyncAPI for building scalable, decoupled systems.

When to Use
Designing event-driven architectures
Implementing message queues and brokers
Building event sourcing systems
Implementing CQRS patterns
Creating AsyncAPI specifications
Designing event mesh topologies
Building asynchronous microservices
Quick Start

Invoke this skill when:

Designing event-driven architectures
Implementing message queues and brokers
Building event sourcing systems
Implementing CQRS patterns
Creating AsyncAPI specifications

Do NOT invoke when:

Building synchronous REST APIs (use api-designer)
Setting up Kafka infrastructure (use data-engineer)
Building workflow orchestration (use workflow-orchestrator)
Designing GraphQL APIs (use graphql-architect)
Decision Framework
Message Broker Selection:
├── High throughput, streaming → Kafka
├── Flexible routing → RabbitMQ
├── Cloud-native, serverless → EventBridge, Pub/Sub
├── Simple queuing → SQS, Redis Streams
└── Enterprise integration → Azure Service Bus

Pattern Selection:
├── Audit/replay needed → Event Sourcing
├── Read/write separation → CQRS
├── Simple async → Pub/Sub
├── Guaranteed delivery → Transactional outbox
└── Complex routing → Message router

Core Workflows
1. Event-Driven System Design
Identify domain events
Define event schemas (CloudEvents)
Choose message broker
Design topic/queue structure
Define consumer groups
Plan dead letter handling
Document with AsyncAPI
2. Event Sourcing Implementation
Define aggregate boundaries
Design event types
Implement event store
Build projection handlers
Create read models
Handle schema evolution
Plan snapshot strategy
3. AsyncAPI Specification
Define servers and protocols
Describe channels (topics/queues)
Define message schemas
Document operations (pub/sub)
Add security schemes
Generate documentation
Enable code generation
Best Practices
Use CloudEvents format for interoperability
Design idempotent consumers
Implement dead letter queues
Version event schemas carefully
Monitor consumer lag
Plan for at-least-once delivery
Anti-Patterns
Anti-Pattern	Problem	Correct Approach
Synchronous over async	Defeats purpose	Use proper patterns
No idempotency	Duplicate processing	Design idempotent handlers
Ignoring order	Data consistency issues	Partition by key if needed
Huge events	Network overhead	Small events, fetch details
No schema evolution	Breaking changes	Versioning strategy
Weekly Installs
154
Repository
404kidwiz/claud…e-skills
GitHub Stars
76
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass