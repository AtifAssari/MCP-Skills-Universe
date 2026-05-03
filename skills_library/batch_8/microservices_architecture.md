---
title: microservices-architecture
url: https://skills.sh/aj-geddes/useful-ai-prompts/microservices-architecture
---

# microservices-architecture

skills/aj-geddes/useful-ai-prompts/microservices-architecture
microservices-architecture
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill microservices-architecture
SKILL.md
Microservices Architecture
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Comprehensive guide to designing, implementing, and maintaining microservices architectures. Covers service decomposition, communication patterns, data management, deployment strategies, and observability for distributed systems.

When to Use
Designing new microservices architectures
Decomposing monolithic applications
Implementing service-to-service communication
Setting up API gateways and service mesh
Implementing service discovery
Managing distributed transactions
Designing inter-service data consistency
Scaling independent services
Quick Start

Minimal working example:

Bounded Contexts:
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│  Order Service  │  │  User Service   │  │ Payment Service │
│                 │  │                 │  │                 │
│ - Create Order  │  │ - User Profile  │  │ - Process Pay   │
│ - Order Status  │  │ - Auth          │  │ - Refund        │
│ - Order History │  │ - Preferences   │  │ - Transactions  │
└─────────────────┘  └─────────────────┘  └─────────────────┘

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Service Boundary Design	Service Boundary Design
Communication Patterns	Communication Patterns
API Gateway Pattern	API Gateway Pattern
Service Discovery	Service Discovery
Data Consistency Patterns	Data Consistency Patterns
Service Mesh (Istio)	Service Mesh (Istio)
Best Practices
✅ DO
Design services around business capabilities
Use asynchronous communication where possible
Implement circuit breakers for resilience
Use API gateway for cross-cutting concerns
Implement distributed tracing
Use service mesh for service-to-service communication
Design for failure (chaos engineering)
Implement health checks for all services
Use correlation IDs for request tracking
Version your APIs
Implement proper monitoring and alerting
Use event-driven architecture for loose coupling
Implement idempotent operations
Use database per service pattern
❌ DON'T
Share databases between services
Create overly granular services (nanoservices)
Use distributed transactions (two-phase commit)
Ignore network latency and failures
Share domain models between services
Deploy all services as one unit
Hardcode service URLs
Forget to implement authentication/authorization
Use synchronous calls for long-running operations
Ignore backward compatibility
Skip monitoring and logging
Create circular dependencies between services
Weekly Installs
315
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass