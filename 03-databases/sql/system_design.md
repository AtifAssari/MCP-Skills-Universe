---
title: system design
url: https://skills.sh/danhvb/my-ba-skills/system-design
---

# system design

skills/danhvb/my-ba-skills/System Design
System Design
Installation
$ npx skills add https://github.com/danhvb/my-ba-skills --skill 'System Design'
SKILL.md
System Design Skill
Purpose

Enable the Solution Architect Agent to design the high-level structure of software systems, selecting appropriate patterns, technologies, and integration strategies.

Architectural Patterns
1. Monolithic
Use Case: Small startup, simple domain, fast initial dev.
Pros: Simple deployment, easy debugging.
Cons: Scalability limits, tight coupling.
2. Microservices
Use Case: Complex enterprise, distinct domains, independent scaling.
Pros: Tech stack agnostic per service, scalable.
Cons: Distributed complexity, network latency, data consistency.
3. Event-Driven
Use Case: Real-time interactions, high decoupling.
Components: Producers, Consumers, Event Bus (Kafka, RabbitMQ).
4. Serverless
Use Case: Event-triggered, variable load.
Pros: Pay-per-use, no infra management.
Key Design Decisions (The "ilities")
Scalability: Vertical (bigger machine) vs. Horizontal (more machines).
Availability: Redundancy, failover strategies. Load balancers.
Reliability: Circuit breakers, retries, eventual consistency.
Maintainability: Clean code, documentation, monitoring.
Security: Authentication (OAuth), Authorization (RBAC), Encryption.
API Design Strategy
REST: Standard resource-based.
GraphQL: Flexible data querying.
gRPC: High performance inter-service comms.
Database Selection
Relational (SQL): Structured data, ACID transactions (PostgreSQL, MySQL).
NoSQL (Document): Flexible schema, rapid iteration (MongoDB).
NoSQL (Key-Value): Caching, heavy read/write (Redis, DynamoDB).
Time-Series: IoT, financial data (InfluxDB).
Documenting Architecture
C4 Model: Context, Container, Component, Code.
ADR (Architecture Decision Records): Documenting WHY a decision was made.
Deliverables
High-Level Design (HLD) Document.
Low-Level Design (LLD) Document.
Database Schema (ERD).
API Specifications (Swagger/OpenAPI).
Weekly Installs
–
Repository
danhvb/my-ba-skills
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass