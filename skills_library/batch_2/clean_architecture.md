---
title: clean-architecture
url: https://skills.sh/pproenca/dot-skills/clean-architecture
---

# clean-architecture

skills/pproenca/dot-skills/clean-architecture
clean-architecture
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill clean-architecture
Summary

42 Clean Architecture rules organized by priority for designing maintainable, testable software systems.

Covers 8 rule categories from dependency direction and entity design (critical) through testing architecture (low-medium), each with specific guidance and code examples
Dependency rules enforce inward-pointing dependencies, interface ownership, and acyclic component graphs to prevent architectural decay
Entity and use case rules isolate business logic from frameworks, persistence, and presentation concerns through clear boundaries and explicit ports
Includes practical patterns like humble objects, anti-corruption layers, and partial boundaries for phased architectural improvements
SKILL.md
Clean Architecture Best Practices

Comprehensive guide to Clean Architecture principles for designing maintainable, testable software systems. Based on Robert C. Martin's "Clean Architecture: A Craftsman's Guide to Software Structure and Design." Contains 42 rules across 8 categories, prioritized by architectural impact.

When to Apply

Reference these guidelines when:

Designing new software systems or modules
Structuring dependencies between layers
Defining boundaries between business logic and infrastructure
Reviewing code for architectural violations
Refactoring coupled systems toward cleaner structure
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Dependency Direction	CRITICAL	dep-
2	Entity Design	CRITICAL	entity-
3	Use Case Isolation	HIGH	usecase-
4	Component Cohesion	HIGH	comp-
5	Boundary Definition	MEDIUM-HIGH	bound-
6	Interface Adapters	MEDIUM	adapt-
7	Framework Isolation	MEDIUM	frame-
8	Testing Architecture	LOW-MEDIUM	test-
Quick Reference
1. Dependency Direction (CRITICAL)
dep-inward-only - Source dependencies point inward only
dep-interface-ownership - Interfaces belong to clients not implementers
dep-no-framework-imports - Avoid framework imports in inner layers
dep-data-crossing-boundaries - Use simple data structures across boundaries
dep-acyclic-dependencies - Eliminate cyclic dependencies between components
dep-stable-abstractions - Depend on stable abstractions not volatile concretions
2. Entity Design (CRITICAL)
entity-pure-business-rules - Entities contain only enterprise business rules
entity-no-persistence-awareness - Entities must not know how they are persisted
entity-encapsulate-invariants - Encapsulate business invariants within entities
entity-value-objects - Use value objects for domain concepts
entity-rich-not-anemic - Build rich domain models not anemic data structures
3. Use Case Isolation (HIGH)
usecase-single-responsibility - Each use case has one reason to change
usecase-input-output-ports - Define input and output ports for use cases
usecase-orchestrates-not-implements - Use cases orchestrate entities not implement business rules
usecase-no-presentation-logic - Use cases must not contain presentation logic
usecase-explicit-dependencies - Declare all dependencies explicitly in constructor
usecase-transaction-boundary - Use case defines the transaction boundary
4. Component Cohesion (HIGH)
comp-screaming-architecture - Structure should scream the domain not the framework
comp-common-closure - Group classes that change together
comp-common-reuse - Avoid forcing clients to depend on unused code
comp-reuse-release-equivalence - Release components as cohesive units
comp-stable-dependencies - Depend in the direction of stability
5. Boundary Definition (MEDIUM-HIGH)
bound-humble-object - Use humble objects at architectural boundaries
bound-partial-boundaries - Use partial boundaries when full separation is premature
bound-boundary-cost-awareness - Weigh boundary cost against ignorance cost
bound-main-component - Treat main as a plugin to the application
bound-defer-decisions - Defer framework and database decisions
bound-service-internal-architecture - Services must have internal clean architecture
6. Interface Adapters (MEDIUM)
adapt-controller-thin - Keep controllers thin
adapt-presenter-formats - Presenters format data for the view
adapt-gateway-abstraction - Gateways hide external system details
adapt-mapper-translation - Use mappers to translate between layers
adapt-anti-corruption-layer - Build anti-corruption layers for external systems
7. Framework Isolation (MEDIUM)
frame-domain-purity - Domain layer has zero framework dependencies
frame-orm-in-infrastructure - Keep ORM usage in infrastructure layer
frame-web-in-infrastructure - Web framework concerns stay in interface layer
frame-di-container-edge - Dependency injection containers live at the edge
frame-logging-abstraction - Abstract logging behind domain interfaces
8. Testing Architecture (LOW-MEDIUM)
test-tests-are-architecture - Tests are part of the system architecture
test-testable-design - Design for testability from the start
test-layer-isolation - Test each layer in isolation
test-boundary-verification - Verify architectural boundaries with tests
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
1.4K
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass