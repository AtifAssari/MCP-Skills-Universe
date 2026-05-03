---
title: clean-ddd-hexagonal
url: https://skills.sh/ccheney/robust-skills/clean-ddd-hexagonal
---

# clean-ddd-hexagonal

skills/ccheney/robust-skills/clean-ddd-hexagonal
clean-ddd-hexagonal
Installation
$ npx skills add https://github.com/ccheney/robust-skills --skill clean-ddd-hexagonal
Summary

Language-agnostic backend architecture combining DDD, Clean Architecture, and Hexagonal patterns.

Enforces strict dependency rules (inward only) with clear layer separation: domain (core logic), application (use cases), and infrastructure (adapters)
Provides tactical DDD patterns including entities, value objects, aggregates, domain events, repositories, and domain services with concrete decision trees for placement
Includes anti-pattern warnings (anemic models, god aggregates, leaking infrastructure, premature CQRS) and implementation sequencing from domain discovery through adapter implementation
Covers aggregate boundary design, repository-per-aggregate strategy, eventual consistency via domain events, and transaction management across service boundaries
Language-agnostic guidance applicable to Go, Rust, Python, TypeScript, Java, and C# with reference documentation on layers, bounded contexts, CQRS, event sourcing, and testing strategies
SKILL.md
Clean Architecture + DDD + Hexagonal

Backend architecture combining DDD tactical patterns, Clean Architecture dependency rules, and Hexagonal ports/adapters for maintainable, testable systems.

When to Use (and When NOT to)
Use When	Skip When
Complex business domain with many rules	Simple CRUD, few business rules
Long-lived system (years of maintenance)	Prototype, MVP, throwaway code
Team of 5+ developers	Solo developer or small team (1-2)
Multiple entry points (API, CLI, events)	Single entry point, simple API
Need to swap infrastructure (DB, broker)	Fixed infrastructure, unlikely to change
High test coverage required	Quick scripts, internal tools

Start simple. Evolve complexity only when needed. Most systems don't need full CQRS or Event Sourcing.

CRITICAL: The Dependency Rule

Dependencies point inward only. Outer layers depend on inner layers, never the reverse.

Infrastructure → Application → Domain
   (adapters)     (use cases)    (core)


Violations to catch:

Domain importing database/HTTP libraries
Controllers calling repositories directly (bypassing use cases)
Entities depending on application services

Design validation: "Create your application to work without either a UI or a database" — Alistair Cockburn. If you can run your domain logic from tests with no infrastructure, your boundaries are correct.

Quick Decision Trees
"Where does this code go?"
Where does it go?
├─ Pure business logic, no I/O           → domain/
├─ Orchestrates domain + has side effects → application/
├─ Talks to external systems              → infrastructure/
├─ Defines HOW to interact (interface)    → port (domain or application)
└─ Implements a port                      → adapter (infrastructure)

"Is this an Entity or Value Object?"
Entity or Value Object?
├─ Has unique identity that persists → Entity
├─ Defined only by its attributes    → Value Object
├─ "Is this THE same thing?"         → Entity (identity comparison)
└─ "Does this have the same value?"  → Value Object (structural equality)

"Should this be its own Aggregate?"
Aggregate boundaries?
├─ Must be consistent together in a transaction → Same aggregate
├─ Can be eventually consistent                 → Separate aggregates
├─ Referenced by ID only                        → Separate aggregates
└─ >10 entities in aggregate                    → Split it


Rule: One aggregate per transaction. Cross-aggregate consistency via domain events (eventual consistency).

Directory Structure
src/
├── domain/                    # Core business logic (NO external dependencies)
│   ├── {aggregate}/
│   │   ├── entity              # Aggregate root + child entities
│   │   ├── value_objects       # Immutable value types
│   │   ├── events              # Domain events
│   │   ├── repository          # Repository interface (DRIVEN PORT)
│   │   └── services            # Domain services (stateless logic)
│   └── shared/
│       └── errors              # Domain errors
├── application/               # Use cases / Application services
│   ├── {use-case}/
│   │   ├── command             # Command/Query DTOs
│   │   ├── handler             # Use case implementation
│   │   └── port                # Driver port interface
│   └── shared/
│       └── unit_of_work        # Transaction abstraction
├── infrastructure/            # Adapters (external concerns)
│   ├── persistence/           # Database adapters
│   ├── messaging/             # Message broker adapters
│   ├── http/                  # REST/GraphQL adapters (DRIVER)
│   └── config/
│       └── di                  # Dependency injection / composition root
└── main                        # Bootstrap / entry point

DDD Building Blocks
Pattern	Purpose	Layer	Key Rule
Entity	Identity + behavior	Domain	Equality by ID
Value Object	Immutable data	Domain	Equality by value, no setters
Aggregate	Consistency boundary	Domain	Only root is referenced externally
Domain Event	Record of change	Domain	Past tense naming (OrderPlaced)
Repository	Persistence abstraction	Domain (port)	Per aggregate, not per table
Domain Service	Stateless logic	Domain	When logic doesn't fit an entity
Application Service	Orchestration	Application	Coordinates domain + infra
Anti-Patterns (CRITICAL)
Anti-Pattern	Problem	Fix
Anemic Domain Model	Entities are data bags, logic in services	Move behavior INTO entities
Repository per Entity	Breaks aggregate boundaries	One repository per AGGREGATE
Leaking Infrastructure	Domain imports DB/HTTP libs	Domain has ZERO external deps
God Aggregate	Too many entities, slow transactions	Split into smaller aggregates
Skipping Ports	Controllers → Repositories directly	Always go through application layer
CRUD Thinking	Modeling data, not behavior	Model business operations
Premature CQRS	Adding complexity before needed	Start with simple read/write, evolve
Cross-Aggregate TX	Multiple aggregates in one transaction	Use domain events for consistency
Implementation Order
Discover the Domain — Event Storming, conversations with domain experts
Model the Domain — Entities, value objects, aggregates (no infra)
Define Ports — Repository interfaces, external service interfaces
Implement Use Cases — Application services coordinating domain
Add Adapters last — HTTP, database, messaging implementations

DDD is collaborative. Modeling sessions with domain experts are as important as the code patterns.

Reference Documentation
File	Purpose
references/LAYERS.md	Complete layer specifications
references/DDD-STRATEGIC.md	Bounded contexts, context mapping
references/DDD-TACTICAL.md	Entities, value objects, aggregates (pseudocode)
references/HEXAGONAL.md	Ports, adapters, naming
references/CQRS-EVENTS.md	Command/query separation, events
references/TESTING.md	Unit, integration, architecture tests
references/CHEATSHEET.md	Quick decision guide
Sources
Primary Sources
The Clean Architecture — Robert C. Martin (2012)
Hexagonal Architecture — Alistair Cockburn (2005)
Domain-Driven Design: The Blue Book — Eric Evans (2003)
Implementing Domain-Driven Design — Vaughn Vernon (2013)
Pattern References
CQRS — Martin Fowler
Event Sourcing — Martin Fowler
Repository Pattern — Martin Fowler (PoEAA)
Unit of Work — Martin Fowler (PoEAA)
Bounded Context — Martin Fowler
Transactional Outbox — microservices.io
Effective Aggregate Design — Vaughn Vernon
Implementation Guides
Microsoft: DDD + CQRS Microservices
Domain Events — Udi Dahan
Weekly Installs
2.4K
Repository
ccheney/robust-skills
GitHub Stars
39
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass