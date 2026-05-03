---
rating: ⭐⭐⭐
title: architecture-design
url: https://skills.sh/swiftyjourney/architecture-design-skill/architecture-design
---

# architecture-design

skills/swiftyjourney/architecture-design-skill/architecture-design
architecture-design
Installation
$ npx skills add https://github.com/swiftyjourney/architecture-design-skill --skill architecture-design
SKILL.md
Architecture & Design Principles Skill

Transform codebases into maintainable, testable, and scalable architectures using Clean Architecture principles, SOLID design patterns, and industry best practices from the Essential Developer methodology.

Overview

This skill guides you through a structured 5-step process to:

Analyze Requirements → Identify components, responsibilities, and boundaries
Apply SOLID Principles → Design with SRP, OCP, LSP, ISP, DIP
Define Clean Architecture → Establish layers, boundaries, and dependency rules
Design Testing Strategy → Plan unit tests, integration tests, and test boundaries
Document Decisions → Create Architecture Decision Records (ADRs)
Core Philosophy

"Good architecture is a byproduct of good team processes and communication"

This skill follows these principles:

Framework Independence - Business logic doesn't depend on frameworks
Testability - Architecture enables easy testing
UI Independence - UI can change without affecting business rules
Database Independence - Business rules don't know about the database
External Agency Independence - Business rules don't depend on external services
The 5-Step Process
Step 1: Analyze Requirements

Objective: Identify components, responsibilities, and architectural boundaries

Actions:

Break down feature into distinct responsibilities
Identify core business logic vs infrastructure concerns
Recognize cross-cutting concerns (logging, analytics, caching)
Map data flow through the system
Identify potential architectural boundaries

Key Questions to Ask:

What is the core business logic?
What are the external dependencies (network, database, UI)?
What needs to be testable in isolation?
What components might change independently?
What are the inputs and outputs of each component?

Output: Component diagram with clear responsibilities

Reference: See references/modular_design.md for component identification patterns

Step 2: Apply SOLID Principles

Objective: Design components following SOLID principles

S - Single Responsibility Principle (SRP)

Each class/module has one reason to change. Separate business logic from infrastructure.

❌ A class that loads data AND presents it
✅ Separate UseCase for business logic; separate Presenter for view logic
O - Open/Closed Principle (OCP)

Open for extension via protocols/interfaces, closed for modification:

// Open for extension via protocol (Swift example — same idea in any language)
protocol ItemLoader {
    func load() async throws -> [Item]
}

// Closed for modification — implementations extend behavior
final class RemoteItemLoader: ItemLoader { ... }
final class CachedItemLoader: ItemLoader { ... }
final class FallbackItemLoader: ItemLoader { ... }

L - Liskov Substitution Principle (LSP)

Subtypes must be substitutable for base types. Contracts must be honored by all implementations.

I - Interface Segregation Principle (ISP)

Clients shouldn't depend on interfaces they don't use. Create focused, specific protocols.

❌ protocol DataStore { func save(_:); func load(); func delete(); func migrate(); func backup() }
✅ protocol ItemReader { func retrieve() throws -> [Item]? } + separate ItemCache
D - Dependency Inversion Principle (DIP)

High-level modules depend on abstractions, not concretions.

class ItemListViewController {
    private let loader: ItemLoader  // depends on abstraction, not concrete type
    init(loader: ItemLoader) { self.loader = loader }
}


Output: SOLID-compliant component design

Reference: See references/solid_principles.md for detailed patterns and anti-patterns

Step 3: Define Clean Architecture

Objective: Establish clear architectural layers with proper dependency flow

The Clean Architecture Layers:

┌─────────────────────────────────────────┐
│          Presentation Layer             │
│    (UI, ViewModels, Presenters)        │
└─────────────────┬───────────────────────┘
                  │ depends on
┌─────────────────▼───────────────────────┐
│         Domain/Business Layer           │
│      (Use Cases, Entities, Rules)      │
└─────────────────┬───────────────────────┘
                  │ depends on
┌─────────────────▼───────────────────────┐
│         Infrastructure Layer            │
│   (Network, Database, Framework Code)  │
└─────────────────────────────────────────┘


Dependency Rule: Source code dependencies point inward only

Key Patterns:

Use Cases — contain business rules, orchestrate data flow, independent of UI and frameworks
Boundaries (Protocols) — define contracts between layers, enable testability
Adapters — convert data between layers, implement boundary protocols
Composition Root — wire dependencies together, configure the object graph

Output: Layered architecture with clear boundaries

Reference: See references/clean_architecture.md for detailed layer definitions; examples/generic/layered_architecture.md for a language-agnostic example; examples/swift/ for Swift/iOS real implementations

Step 4: Design Testing Strategy

Objective: Plan comprehensive testing at all architectural layers

Testing Pyramid:

        ┌──────────┐
        │    UI    │ Few - End to End
        ├──────────┤
        │Integration│ Some - Integration
        ├──────────┤
        │   Unit   │ Many - Fast & Isolated
        └──────────┘


Testing Boundaries:

Domain Layer (Unit Tests) — test use cases in isolation, mock all dependencies
Infrastructure Layer (Integration Tests) — test adapters with real dependencies
Presentation Layer (Unit Tests) — test presenters/view models, mock use cases

Test Double Vocabulary:

Stubs: Provide canned answers
Spies: Record calls for verification
Mocks: Verify behavior expectations
Fakes: Working implementations for testing

Testing Strategies:

Test behavior, not implementation details
Use native async test primitives; avoid manual callback synchronization when the language supports await
Factory helper pattern: create the system under test (SUT) and its dependencies together in a makeSUT() helper to keep individual test methods clean
Arrange, Act, Assert structure; extract helpers for clarity

Output: Comprehensive testing strategy document

Reference: See references/testing_strategies.md for patterns and best practices

Step 5: Document Decisions

Objective: Create clear architectural documentation and decision records

ADR Format:

# ADR-NNN: <Decision Title>
## Status: Accepted | Superseded | Deprecated
## Context: Why this decision was needed
## Decision: What was decided
## Consequences: Positive and negative outcomes
## Alternatives Considered: What was rejected and why


See examples/generic/ for a complete ADR example.

Documentation Requirements:

Architecture Overview — system context diagram, component diagram, layer relationships
Component Documentation — purpose, dependencies, usage examples
Design Patterns Used — which patterns and why, trade-offs
Testing Strategy — what gets tested and how

Output: Complete architectural documentation

Reference: See references/ for detailed documentation patterns

Best Practices
DO ✅
Separate business logic from infrastructure
Depend on abstractions, not concretions
Make dependencies explicit through initializer injection
Write tests for all business logic
Use async IO protocols at network/network boundaries; synchronous protocols for in-process storage
Isolate presentation types to the main/UI thread using the language's concurrency primitives
Design for testability from the start
DON'T ❌
Let business logic depend on frameworks
Use singletons for dependency management
Mix presentation and business logic
Create god classes with multiple responsibilities
Use manual callback/completion-handler patterns where the language's native async/await is available
Dispatch to the UI thread manually — use structured concurrency instead

Swift/iOS: Use async throws at network boundaries, sync throws at cache boundaries, @MainActor for presentation types, and Sendable for value types crossing actor boundaries. See the Swift Concurrency section below.

Common Architectural Patterns
Clean Architecture (Recommended) — clear separation of concerns, dependency rule: inward only
Hexagonal Architecture (Ports & Adapters) — business logic at the center, ports define boundaries
MVVM — separation of UI and logic, testable view models
MVC — traditional separation, controller as composition root

Reference: See examples/generic/layered_architecture.md for a language-agnostic layered example; examples/swift/ for MVVM+Coordinator, Composition Root, and Two-Layer View in Swift/iOS

Language-Specific Guidance
Swift/iOS
Use async throws protocols for network boundaries
Use sync throws for cache/store boundaries; bridge to async via Scheduler protocol
Apply @MainActor to presentation types (ResourceView, LoadResourcePresenter)
Mark domain value types Sendable (e.g. FeedImage: Hashable, Sendable)
Use LoadResourcePresenter<Resource, View> generic presenter — one type for all features
Use WeakRefVirtualProxy<T> to break retain cycles without per-type boilerplate
Apply Composition Root pattern in SceneDelegate; extract infrastructure into @MainActor service objects (see examples/swift/composition_root.md)

Reference: See examples/swift/ for Swift-specific patterns

Generic/Agnostic
Apply SOLID principles universally
Use interfaces/traits/protocols depending on language
Adapt patterns to language features
Maintain Clean Architecture layers

Reference: See examples/generic/ for language-agnostic examples

Swift Concurrency (Swift/iOS only)

The concepts in this section — async IO boundaries, main-thread isolation, value-type thread safety, generic presenter, memory-safe proxies — apply universally. The syntax and APIs below are Swift-specific. For the detailed implementations, see references/concurrency_patterns.md.

Async Protocol Boundaries

Network protocols use async throws; store protocols use sync throws:

// Network boundary — async because IO is inherently async
public protocol HTTPClient {
    func get(from url: URL) async throws -> (Data, HTTPURLResponse)
}

// Cache/store boundary — sync because the store runs on its own queue (bridged via Scheduler)
// Apply this pattern to any persistent store: CoreData, SQLite, in-memory, Realm, etc.
public protocol ItemStore {
    func delete() throws
    func insert(_ items: [LocalItem], timestamp: Date) throws
    func retrieve() throws -> CachedItems?
}
// Essential Feed uses FeedStore with identical structure for FeedImage caching

@MainActor Isolation

Presentation layer types are @MainActor — no manual thread dispatching:

@MainActor public protocol ResourceView {
    associatedtype ResourceViewModel
    func display(_ viewModel: ResourceViewModel)
}

@MainActor public final class LoadResourcePresenter<Resource, View: ResourceView> {
    public typealias Mapper = (Resource) throws -> View.ResourceViewModel
    public init(resourceView: View, loadingView: ResourceLoadingView,
                errorView: ResourceErrorView, mapper: @escaping Mapper)
    public init(resourceView: View, loadingView: ResourceLoadingView,
                errorView: ResourceErrorView) where Resource == View.ResourceViewModel
    public func didStartLoading()
    public func didFinishLoading(with resource: Resource)
    public func didFinishLoading(with error: Error)
}

Sendable Value Types

Domain entities crossing actor boundaries must be Sendable. All stored properties must themselves be Sendable; the compiler verifies this:

// Generic pattern — apply to any domain entity
public struct Item: Hashable, Sendable {
    public let id: UUID
    public let title: String
    // String, UUID, URL are all Sendable — compiler is satisfied
}

// Concrete example from Essential Feed:
// public struct FeedImage: Hashable, Sendable { ... }

WeakRefVirtualProxy

Prevents retain cycles via a single generic type with conditional conformances:

final class WeakRefVirtualProxy<T: AnyObject> {
    private weak var object: T?
    init(_ object: T) { self.object = object }
}

extension WeakRefVirtualProxy: ResourceErrorView where T: ResourceErrorView {
    func display(_ viewModel: ResourceErrorViewModel) { object?.display(viewModel) }
}

extension WeakRefVirtualProxy: ResourceLoadingView where T: ResourceLoadingView {
    func display(_ viewModel: ResourceLoadingViewModel) { object?.display(viewModel) }
}

Scheduler Protocol

Bridges sync FeedStore into async contexts without making the store async:

protocol Scheduler {
    @MainActor
    func schedule<T>(_ action: @escaping @Sendable () throws -> T) async rethrows -> T
}


Reference: See references/concurrency_patterns.md for full implementations and migration guide

Integration with Requirements Engineering
Start with requirements → Use Cases → BDD scenarios
Apply this skill → Architecture → Component design
Implement → Following architectural patterns
Test → Using defined testing strategy
References

Inside references/:

clean_architecture.md - Clean Architecture layers and rules
solid_principles.md - Detailed SOLID explanations with examples
design_patterns.md - Common patterns (Adapter, Decorator, Composite, Null Object, etc.)
null_object_pattern.md - Null Object Pattern with testing examples
command_query_separation.md - CQS principle for cache design
dependency_management.md - DI patterns and strategies
testing_strategies.md - Testing patterns and best practices
modular_design.md - Module organization and boundaries
concurrency_patterns.md - Swift Concurrency: async/await, @MainActor, Sendable, Scheduler

Inside examples/:

swift/ - Real implementations from Essential Feed (Swift 6)
generic/ - Language-agnostic examples
Output Format

When applying this skill, provide:

Component Analysis - Identified components and responsibilities
SOLID Review - Applied principles with rationale
Architecture Diagram - Layers and dependencies (Mermaid)
Testing Strategy - Test structure and coverage plan
ADRs - Key decisions documented
Implementation Guide - Step-by-step refactoring or implementation plan
Credits

Based on the Essential Developer's proven architecture methodology:

Essential Feed Case Study
Essential Developer Resources
Version History
2.1.0 - Generalized for multi-project use: domain-neutral SOLID examples, separated Swift-specific guidance, added scope labels, created generic ADR template and updated generic architecture example
2.0.0 - Swift 6 migration: async/await, @MainActor, Sendable, LoadResourcePresenter, Scheduler, WeakRefVirtualProxy
1.0.0 - Initial release with 5-step process
Weekly Installs
64
Repository
swiftyjourney/a…gn-skill
GitHub Stars
1
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass