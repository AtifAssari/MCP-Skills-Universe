---
rating: ⭐⭐
title: microservices-patterns
url: https://skills.sh/nickcrew/claude-ctx-plugin/microservices-patterns
---

# microservices-patterns

skills/nickcrew/claude-ctx-plugin/microservices-patterns
microservices-patterns
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill microservices-patterns
SKILL.md
Microservices Architecture Patterns

Expert guidance for designing, implementing, and operating microservices architectures.

When to Use This Skill
Breaking down monolithic applications into services
Designing distributed systems from scratch
Implementing service communication patterns (sync/async)
Managing data consistency across services
Building resilient distributed systems
Defining service boundaries and API contracts
Core Principles
Single Responsibility - Each service has one reason to change
Independent Deployability - No coordination required for deployments
Decentralized Data - Each service owns its data exclusively
Design for Failure - Embrace failures, build resilience
Automate Everything - Deployment, scaling, and recovery
Quick Reference

Load detailed patterns on-demand:

Task	Load Reference
Define service boundaries and decompose monoliths	skills/microservices-patterns/references/service-decomposition.md
Implement service communication (sync/async)	skills/microservices-patterns/references/communication-patterns.md
Manage data consistency and transactions	skills/microservices-patterns/references/data-management.md
Build resilient systems (circuit breakers, retries)	skills/microservices-patterns/references/resilience-patterns.md
Add observability (tracing, logging, metrics)	skills/microservices-patterns/references/observability.md
Plan deployments and migrations	skills/microservices-patterns/references/deployment-migration.md
Workflow
1. Understand Requirements
Map business capabilities and domains
Assess scalability/resilience needs
Identify team boundaries
2. Define Service Boundaries

Load references/service-decomposition.md for:

Business capability decomposition
DDD bounded contexts
Service boundary validation
3. Design Communication

Load references/communication-patterns.md for:

Synchronous: API Gateway, REST, gRPC
Asynchronous: Message Queue, Pub/Sub, Event Sourcing
4. Manage Data

Load references/data-management.md for:

Database per service pattern
Saga distributed transactions
CQRS read/write optimization
5. Build Resilience

Load references/resilience-patterns.md for:

Circuit breakers
Retry with exponential backoff
Bulkhead isolation
Rate limiting and timeouts
6. Add Observability

Load references/observability.md for:

Distributed tracing
Centralized logging
Metrics and monitoring
7. Plan Deployment

Load references/deployment-migration.md for:

Blue-Green, Canary, Rolling deployments
Strangler Fig migration pattern
Common Mistakes
Distributed Monolith - Tightly coupled, must deploy together
Shared Database - Multiple services accessing same database
Chatty APIs - Excessive synchronous service calls
Missing Circuit Breakers - No cascading failure protection
No Observability - Deploying without tracing/logging/metrics
Ignoring Network Failures - Assuming reliable network
No API Versioning - Breaking changes without versioning

Fixes: Load relevant reference files for detailed solutions.

Resources
Books: "Building Microservices" (Newman), "Microservices Patterns" (Richardson)
Sites: microservices.io, martinfowler.com/microservices
Tools: Kubernetes, Istio, Kafka, Kong, Jaeger, Prometheus
Weekly Installs
41
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass