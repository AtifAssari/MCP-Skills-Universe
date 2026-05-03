---
title: backend-design
url: https://skills.sh/dauquangthanh/hanoi-rainbow/backend-design
---

# backend-design

skills/dauquangthanh/hanoi-rainbow/backend-design
backend-design
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill backend-design
SKILL.md
Backend Design
Workflow

Follow this systematic design process:

Requirements Analysis

Gather functional requirements (features, operations)
Define non-functional requirements (performance, scalability, availability)
Identify constraints (budget, timeline, technology, compliance)

Architecture Selection

Choose architecture pattern (monolith, microservices, serverless)
Select technology stack based on requirements
Define service boundaries and responsibilities

API Design

Design RESTful endpoints with proper resource modeling
Define request/response schemas and contracts
Plan versioning strategy and documentation
See api-design-guide.md for REST/GraphQL/gRPC patterns

Database Design

Model entities and relationships
Design schema with normalization
Plan indexing and partitioning strategies
See database-design.md for relational and NoSQL patterns

Security Design

Design authentication flow (OAuth 2.0, JWT)
Plan authorization model (RBAC, ABAC)
Define data encryption and protection strategy

Scalability & Performance

Design caching strategy (Redis, CDN)
Plan load balancing and auto-scaling
Define asynchronous processing with message queues

Documentation

Create API specifications (OpenAPI/Swagger)
Document architecture decisions with Mermaid diagrams
Provide implementation guidelines and roadmap
Output Structure

Present your backend design with these sections:

System Overview - High-level architecture, components, technology stack
API Specification - Endpoints, schemas, authentication, OpenAPI docs
Database Design - ERD, schema, indexes, migration plan
Architecture Decisions - Service decomposition, communication patterns, consistency model
Security Implementation - Authentication/authorization flows, encryption
Scalability Plan - Load balancing, caching, database scaling, auto-scaling
Deployment Architecture - Containers, infrastructure, CI/CD, monitoring
Implementation Roadmap - Phases, milestones, dependencies, risks
Core Principles
API-first approach - Design and document APIs before implementation
Security by design - Build authentication, authorization, and encryption from the start
Design for scalability - Plan for growth with caching, load balancing, and horizontal scaling
Plan for failure - Include error handling, retries, circuit breakers, and graceful degradation
Document thoroughly - Create clear API specs, Mermaid architecture diagrams, and implementation guides
Reference Files

Load additional resources based on specific needs:

Detailed Design Process: See backend-design-process.md for comprehensive step-by-step workflow with examples for API design, database modeling, authentication flows, and microservices patterns

API Design Guide: See api-design-guide.md when designing RESTful APIs, GraphQL schemas, or gRPC services - includes resource modeling, status codes, versioning strategies, and documentation

Database Design: See database-design.md for detailed guidance on relational and NoSQL database design, normalization, indexing, partitioning, and replication strategies

Best Practices: See best-practices.md for API design, database optimization, security hardening, performance tuning, and reliability patterns

Common Patterns: See common-patterns.md for code examples of repository pattern, service layer, dependency injection, and other architectural patterns

Example Projects: See examples.md for complete architecture examples including e-commerce systems, real-time chat applications, and microservices implementations

Weekly Installs
53
Repository
dauquangthanh/h…-rainbow
GitHub Stars
10
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass