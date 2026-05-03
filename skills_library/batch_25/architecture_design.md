---
title: architecture-design
url: https://skills.sh/dauquangthanh/hanoi-rainbow/architecture-design
---

# architecture-design

skills/dauquangthanh/hanoi-rainbow/architecture-design
architecture-design
Installation
$ npx skills add https://github.com/dauquangthanh/hanoi-rainbow --skill architecture-design
SKILL.md
Architecture Design
Overview

This skill enables you to design comprehensive software solution architectures including system components, technology stacks, integration patterns, scalability strategies, and deployment models.

Core Capabilities

When activated, this skill provides:

Requirements Analysis & Architecture Planning

Analyze functional and non-functional requirements
Identify architectural drivers (scalability, security, performance)
Define system boundaries and constraints
Establish architecture goals and success criteria

System Architecture Design

Design layered/tiered architectures
Create microservices and domain-driven designs
Design event-driven and message-based systems
Plan serverless and cloud-native architectures
Design monolithic, modular monolithic, or distributed systems

Technology Stack Selection

Evaluate and justify programming languages and frameworks
Select databases with rationale (SQL, NoSQL, time-series, graph)
Choose middleware and integration platforms (message queues, API gateways)
Select infrastructure and cloud platforms (assess vendor lock-in)
Recommend CI/CD and DevOps tools
Document technology decisions in ADRs with alternatives considered
Assess team skills and training needs for new technologies

Architecture Patterns & Best Practices

Apply design patterns (MVC, MVVM, Clean Architecture, Hexagonal)
Implement integration patterns (REST, GraphQL, gRPC, message queues)
Design for scalability (horizontal/vertical, caching, CDN)
Implement security patterns (OAuth, JWT, zero-trust)
Apply resilience patterns (circuit breakers, retries, bulkheads)

Documentation & Deliverables

Create C4 model diagrams in Mermaid format (Context, Container, Component, Code)
Generate Mermaid diagrams (class, sequence, deployment)
Produce architecture decision records (ADRs)
Write technical specifications and API contracts
Create implementation roadmaps and migration plans
Architecture Design Workflow

Follow this systematic process:

Step 1: Discovery & Requirements

Gather Requirements

Functional requirements (features, use cases)
Non-functional requirements (performance, scalability, security)
Business constraints (budget, timeline, compliance)
Technical constraints (existing systems, team skills)

Analyze Architecture Drivers

Performance: latency, throughput targets
Scalability: user growth, data volume projections
Availability: uptime SLA, disaster recovery needs
Security: authentication, authorization, compliance requirements
Maintainability: testability, modularity goals

Define System Context

Identify stakeholders and their needs
Map external systems and dependencies
Define system boundaries
Identify integration points
Step 2: Architecture Design
Choose Architecture Style

Select based on requirements and constraints:

Monolithic

Use for: Simple applications, MVPs, small teams, tight deadlines
Benefits: Simple deployment, strong consistency, no network overhead
Trade-offs: Scaling limitations, technology lock-in

Modular Monolithic

Use for: Medium complexity, clear domain boundaries
Benefits: Better organization, some isolation, shared infrastructure
Trade-offs: Still single deployment, limited independent scaling

Microservices

Use for: Large scale, multiple teams, different tech stacks
Benefits: Independent scaling/deployment, technology flexibility
Trade-offs: Distributed complexity, network overhead, eventual consistency

Serverless

Use for: Event-driven, variable load, rapid development
Benefits: Auto-scaling, pay-per-use, no infrastructure management
Trade-offs: Cold starts, vendor lock-in, debugging complexity

Event-Driven

Use for: Real-time processing, loose coupling, high throughput
Benefits: Scalability, flexibility, asynchronous processing
Trade-offs: Complexity, eventual consistency, debugging challenges
Design System Components

Define key layers and components:

┌─────────────────────────────────┐
│   Presentation Layer            │  UI, Controllers, APIs
├─────────────────────────────────┤
│   Application Layer             │  Use Cases, Orchestration
├─────────────────────────────────┤
│   Domain Layer                  │  Business Logic, Entities
├─────────────────────────────────┤
│   Data Layer                    │  Databases, Caches
├─────────────────────────────────┤
│   Infrastructure Layer          │  External APIs, Services
└─────────────────────────────────┘


Define Data Architecture

Design data models and schemas
Choose database types (relational, document, graph, time-series)
Plan data partitioning and sharding strategies
Design caching layers (Redis, Memcached)
Define data flows and ETL processes

Design Integration Points

API design (REST, GraphQL, gRPC)
Message queues (Kafka, RabbitMQ, SQS)
Event streaming architectures
Authentication and authorization flows
Rate limiting and throttling strategies
Step 3: Document Architecture
Create Architecture Diagrams

Use C4 model in Mermaid format for comprehensive documentation:

Context: System in environment with users and external systems (use Mermaid C4Context)
Container: High-level technology choices and communication (use Mermaid C4Container)
Component: Internal structure of containers (use Mermaid C4Component)
Code: Class diagrams for complex components (use Mermaid classDiagram)

All diagrams should use Mermaid syntax for easy versioning and rendering in markdown.

Write Architecture Decision Records (ADRs)

Document all significant decisions using structured ADRs:

# ADR-001: [Decision Title]

## Status
Proposed | Accepted | Deprecated | Superseded

## Context
[Problem and constraints requiring decision]

## Decision
[Chosen solution and approach]

## Consequences
[Benefits and trade-offs]


Full ADR Template: See adr-template.md for complete structure with examples

Produce Technical Specifications
System overview and objectives
Component descriptions and responsibilities
API contracts and interfaces
Data models and schemas
Security and compliance measures
Deployment and operations guidelines
Step 4: Validate & Review

Quality Attributes Assessment

Performance: Response time, throughput
Scalability: Horizontal/vertical scaling capabilities
Availability: Fault tolerance, disaster recovery
Security: Authentication, authorization, encryption
Maintainability: Code organization, testability
Cost: Infrastructure and operational expenses

Design Validation Checklist

Ensure architecture is review-ready:

 All functional and non-functional requirements addressed
 Architecture style justified with trade-offs documented
 Scalability strategy defined (horizontal/vertical, capacity planning)
 Security measures implemented (authentication, authorization, encryption)
 Data architecture validated (storage, consistency, replication)
 Integration patterns specified (sync/async, APIs, events)
 Monitoring and observability planned (metrics, logs, traces, alerts)
 Disaster recovery and backup strategy documented (RPO/RTO)
 Cost estimates provided (infrastructure, operations, scaling)
 Architecture Decision Records (ADRs) created for major decisions
Reference Files

Load reference files based on specific needs:

Architecture Design Process: See architecture-design-process.md when:

Need detailed step-by-step guidance for complex architectures
Working through each phase systematically
Require comprehensive checklists and considerations

Architecture Patterns: See architecture-patterns.md when:

Need detailed pattern descriptions with benefits and trade-offs
Comparing multiple architecture styles
Looking for specific pattern implementations and examples

Technology Stack Guide: See technology-stack-guide.md when:

Evaluating specific technologies or frameworks
Need recommendations for databases, languages, or cloud platforms
Comparing technology options for specific requirements

Best Practices: See best-practices.md when:

Need design principles and guidelines
Looking for API design standards
Require security or operational best practices

Design Considerations: See design-considerations.md when:

Evaluating quality attributes (performance, scalability, security)
Need guidance on specific architectural concerns
Planning for observability, resilience, or cost optimization

Common Anti-Patterns: See common-anti-patterns-to-avoid.md when:

Reviewing existing architectures for issues
Validating design decisions
Need examples of what NOT to do

Migration Patterns: See migration-patterns.md when:

Modernizing legacy applications
Planning migration strategies
Need patterns for phased migrations or strangler fig approaches

Examples: See examples.md when:

Need complete architecture examples for common scenarios
Looking for real-world reference implementations
Want to see how patterns are applied in practice

Resources and References: See resources-and-references.md when:

Need external documentation links
Looking for additional learning resources
Require specifications or standards references
Output Format

Produce clear, comprehensive architecture documentation:

Architecture Overview

System purpose and scope
Key architecture decisions and rationale
High-level component diagram

Detailed Design

Component descriptions and responsibilities
Data models and schemas
API specifications
Integration patterns

Diagrams (All in Mermaid format)

C4 Context diagram (Mermaid C4Context)
C4 Container diagram (Mermaid C4Container)
Sequence diagrams for key flows (Mermaid sequenceDiagram)
Deployment diagram (Mermaid flowchart or C4Deployment)

Implementation Roadmap

Phase breakdown with milestones
Dependencies and sequencing
Resource requirements
Risk mitigation strategies

Architecture Decision Records

Document all significant decisions
Include context, alternatives, and trade-offs
Weekly Installs
21
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