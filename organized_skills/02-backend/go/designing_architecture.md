---
rating: ⭐⭐⭐
title: designing-architecture
url: https://skills.sh/cloudai-x/claude-workflow-v2/designing-architecture
---

# designing-architecture

skills/cloudai-x/claude-workflow-v2/designing-architecture
designing-architecture
Installation
$ npx skills add https://github.com/cloudai-x/claude-workflow-v2 --skill designing-architecture
SKILL.md
Designing Architecture
When to Load
Trigger: System design, module structure, new project scaffolding, choosing architecture patterns
Skip: Simple bug fixes or minor code changes that don't affect architecture
Architecture Decision Workflow

Copy this checklist and track progress:

Architecture Design Progress:
- [ ] Step 1: Understand requirements and constraints
- [ ] Step 2: Assess project size and team capabilities
- [ ] Step 3: Select architecture pattern
- [ ] Step 4: Define directory structure
- [ ] Step 5: Document trade-offs and decision
- [ ] Step 6: Validate against decision framework

Pattern Selection Guide
By Project Size
Size	Recommended Pattern
Small (<10K LOC)	Simple MVC/Layered
Medium (10K-100K)	Clean Architecture
Large (>100K)	Modular Monolith or Microservices
By Team Size
Team	Recommended
1-3 devs	Monolith with clear modules
4-10 devs	Modular Monolith
10+ devs	Microservices (if justified)
Common Patterns
1. Layered Architecture
┌─────────────────────────────┐
│       Presentation          │  ← UI, API Controllers
├─────────────────────────────┤
│       Application           │  ← Use Cases, Services
├─────────────────────────────┤
│         Domain              │  ← Business Logic, Entities
├─────────────────────────────┤
│      Infrastructure         │  ← Database, External APIs
└─────────────────────────────┘


Use when: Simple CRUD apps, small teams, quick prototypes

2. Clean Architecture
┌─────────────────────────────────────┐
│            Frameworks & Drivers      │
│  ┌─────────────────────────────┐    │
│  │     Interface Adapters       │    │
│  │  ┌─────────────────────┐    │    │
│  │  │   Application       │    │    │
│  │  │  ┌─────────────┐    │    │    │
│  │  │  │   Domain    │    │    │    │
│  │  │  └─────────────┘    │    │    │
│  │  └─────────────────────┘    │    │
│  └─────────────────────────────┘    │
└─────────────────────────────────────┘


Use when: Complex business logic, long-lived projects, testability is key

3. Hexagonal (Ports & Adapters)
        ┌──────────┐
        │ HTTP API │
        └────┬─────┘
             │ Port
    ┌────────▼────────┐
    │                 │
    │   Application   │
    │     Core        │
    │                 │
    └────────┬────────┘
             │ Port
        ┌────▼─────┐
        │ Database │
        └──────────┘


Use when: Need to swap external dependencies, multiple entry points

4. Event-Driven Architecture
Producer → Event Bus → Consumer
              │
              ├─→ Consumer
              │
              └─→ Consumer


Use when: Loose coupling needed, async processing, scalability

5. CQRS (Command Query Responsibility Segregation)
┌─────────────┐      ┌─────────────┐
│  Commands   │      │   Queries   │
│  (Write)    │      │   (Read)    │
└──────┬──────┘      └──────┬──────┘
       │                    │
       ▼                    ▼
  Write Model          Read Model
       │                    │
       └────────┬───────────┘
                ▼
           Event Store


Use when: Different read/write scaling, complex domains, event sourcing

Directory Structure Patterns
Feature-Based (Recommended for medium+)
src/
├── features/
│   ├── users/
│   │   ├── api/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── types/
│   └── orders/
│       ├── api/
│       ├── components/
│       └── ...
├── shared/
│   ├── components/
│   ├── hooks/
│   └── utils/
└── app/
    └── ...

Layer-Based (Simple apps)
src/
├── controllers/
├── services/
├── models/
├── repositories/
└── utils/

Decision Framework

When making architectural decisions, evaluate against these criteria:

Simplicity - Start simple, evolve when needed
Team Skills - Match architecture to team capabilities
Requirements - Let business needs drive decisions
Scalability - Consider growth trajectory
Maintainability - Optimize for change
Trade-off Analysis Template

Use this template to document architectural decisions:

## Decision: [What we're deciding]

### Context

[Why this decision is needed now]

### Options Considered

1. Option A: [Description]
2. Option B: [Description]

### Trade-offs

| Criteria         | Option A | Option B |
| ---------------- | -------- | -------- |
| Complexity       | Low      | High     |
| Scalability      | Medium   | High     |
| Team familiarity | High     | Low      |

### Decision

We chose [Option] because [reasoning].

### Consequences

- [What this enables]
- [What this constrains]

Validation Checklist

After selecting an architecture, validate against:

Architecture Validation:
- [ ] Matches project size and complexity
- [ ] Aligns with team skills and experience
- [ ] Supports current requirements
- [ ] Allows for anticipated growth
- [ ] Dependencies flow inward (core has no external deps)
- [ ] Clear boundaries between modules/layers
- [ ] Testing strategy is feasible
- [ ] Trade-offs are documented


If validation fails, reconsider the pattern selection or adjust the implementation approach.

Weekly Installs
116
Repository
cloudai-x/claud…kflow-v2
GitHub Stars
1.4K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass