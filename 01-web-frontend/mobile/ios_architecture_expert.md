---
rating: ⭐⭐
title: ios-architecture-expert
url: https://skills.sh/swiftyjourney/ios-architecture-expert-skill/ios-architecture-expert
---

# ios-architecture-expert

skills/swiftyjourney/ios-architecture-expert-skill/ios-architecture-expert
ios-architecture-expert
Installation
$ npx skills add https://github.com/swiftyjourney/ios-architecture-expert-skill --skill ios-architecture-expert
SKILL.md
iOS Architecture Expert — Essential Developer Methodology
Agent Behavior Contract

When this skill is active, follow these rules strictly:

Feature modules have zero UIKit/SwiftUI imports — only Foundation. Domain models, use cases, presenters, and API/cache logic never depend on a UI framework.
Define protocol boundaries at every layer transition — FeedStore, HTTPClient, ResourceView, FeedCache, etc. Concrete types live behind protocols.
Domain models are value types — struct, Hashable, Sendable. No classes for models.
Presentation logic is framework-agnostic — presenters output view models (structs). No UIImage, UIColor, or SwiftUI types in the presentation layer.
All dependency wiring happens in the Composition Root — the app target (or a dedicated CompositionRoot module). Feature modules never create their own dependencies.
Tests drive the design — one test class per use case, named by behavior (CacheFeedUseCaseTests, not LocalFeedLoaderTests). Use makeSUT() factory in every test class.
Use SPM multi-target packages for module separation — EssentialFeed (Foundation), EssentialFeediOS (UIKit), EssentialApp (composition).
Prefer async/await over closures/Combine for async operations. Use Task.immediate for synchronous-first execution in adapters.
Use Swift Testing (@Test, #expect) for new tests. Follow patterns in the swift-testing-expert skill when available.
Mark shared mutable state with @MainActor — presenters, adapters, view controllers, and composition code run on the main actor.
Architecture Diagnostic Table
Symptom	First check	Smallest safe fix	Deep dive
Feature module imports UIKit/SwiftUI	Dependency graph	Move type to correct layer	references/architecture-layers.md
Retain cycle between presenter and view	Proxy wiring	Add WeakRefVirtualProxy	references/adapters-and-proxies.md
CoreData crashes on launch	Fallback strategy	Add InMemoryFeedStore fallback	references/composition-root.md
Duplicate network requests on refresh	isLoading guard	Use LoadResourcePresentationAdapter	references/adapters-and-proxies.md
Test requires real infrastructure	Protocol boundary	Extract protocol at boundary	references/testing-strategy.md
Sendable warning at composition boundary	Closure annotations	Add @Sendable + @MainActor	references/concurrency-at-boundaries.md
Pagination won't load next page	loadMore closure	Verify recursive composition in FeedViewAdapter	references/composition-root.md
Cache validation doesn't run	Task.immediate usage	Use fire-and-forget with Task.immediate	references/concurrency-at-boundaries.md
Architecture Layers
Layer	Responsibility
Feature	Domain models (struct, Sendable) and abstract use-case protocols. Zero framework imports beyond Foundation.
API	Endpoint enums, static mappers with private Decodable types, HTTPClient protocol.
Cache	Store protocols, local models (decoupled from domain), use-case orchestrators, cache policy objects.
Presentation	Generic LoadResourcePresenter<Resource, View>, view model structs, localized error strings.
UI (UIKit)	View controllers, cells, DiffableDataSource, CellController type-erasure. Conforms to presenter view protocols.
UI (SwiftUI)	@Observable view models, View composition, environment-based DI. Same presenter patterns, different binding.
Composition	Composer static factories, PresentationAdapter, WeakRefVirtualProxy, FeedViewAdapter. App-target only.

Full code examples: architecture-layers.md

Key Patterns Quick Reference
Pattern	Purpose
LoadResourcePresenter<Resource, View>	Reusable loading/error/success state machine with generic mapper
WeakRefVirtualProxy<T>	Break retain cycles in presenter->view binding via conditional conformance
LoadResourcePresentationAdapter	Generic async loader bridging use cases to presenters with cancellation
FeedViewAdapter	Maps domain models to CellController array, composes recursive loadMore
Paginated<Item>	Recursive pagination with optional loadMore closure (Sendable)
Composition Root / FeedService	@MainActor orchestrator with lazy init, Scheduler, and fallback strategy
Scheduler protocol	Abstract store execution context for CoreData/InMemory polymorphism
InMemoryFeedStore	@MainActor fallback store — production fallback + acceptance test double
LoaderSpy<Param, Resource>	Generic async test spy using AsyncThrowingStream for UI integration tests
Specification Pattern	Protocol-driven shared test specs across store implementations
UI Composer (static factory)	Wire presenter->adapter->view chain per feature (FeedUIComposer.feedComposedWith)
Static Mapper	Pure function for data transformation — FeedItemsMapper.map(_:from:)
Cache Policy	Business rule encapsulation for cache validation — FeedCachePolicy.validate(_:against:)
CellController	Type-erased cell composition — wraps UITableViewDataSource + Delegate + Prefetching
Feature Decision Tree

Starting a new feature? Follow this path:

Define the domain model -> struct in Feature layer, Hashable, Sendable
Add concurrency annotations -> @MainActor on view protocols, Sendable on models
Need remote data? -> Endpoint enum + static mapper in API layer
Need persistence? -> Store protocol + local model + cache policy in Cache layer
Need to display it? -> LoadResourcePresenter + view model struct in Presentation layer
UIKit or SwiftUI? -> Build view layer, conform to ResourceView protocols
Wire it up -> Composer + adapter + proxy in Composition Root
Verify concurrency -> Build with SWIFT_STRICT_CONCURRENCY = complete, run Thread Sanitizer

Step-by-step guide: feature-implementation-workflow.md

Guardrails
Do not create concrete types inside feature modules — all instantiation belongs in the Composition Root
Do not use singletons — lazy var in FeedService achieves deferred init without global state
Do not add @MainActor to domain types or store protocols — only presentation, adapters, and composition
Do not use @unchecked Sendable — redesign the type as a value type or use @MainActor
Do not embed cache policy logic inside the loader — keep it as a separate type
Do not put navigation logic in view controllers — use closure callbacks wired in the Composition Root
Defer non-architectural concurrency questions to the swift-concurrency skill
Verification Checklist

When implementing or reviewing architecture:

Build with SWIFT_STRICT_CONCURRENCY = complete — zero warnings
No UIKit/SwiftUI imports in Feature/API/Cache modules
All protocol boundaries have corresponding test doubles
makeSUT() exists in every test class
CoreData store has InMemoryFeedStore fallback in Composition Root
Run Thread Sanitizer (-enableThreadSanitizer YES) — zero data races
WeakRefVirtualProxy wraps all view references in UIKit composition (or @Observable in SwiftUI)
Pagination loadMore is nil for the last page
Reference Router

Open the smallest reference that matches the question:

Architecture & Layers
architecture-layers.md — layer boundaries, domain models, protocols
spm-project-structure.md — module layout, Package.swift, CI
Composition & Wiring
composition-root.md — FeedService, Scheduler, fallback, dependency creation
adapters-and-proxies.md — adapter, proxy, view adapter, pagination wiring
Concurrency in Architecture
concurrency-at-boundaries.md — Scheduler, @Sendable, Task.immediate, cancellation
Testing
testing-strategy.md — unit, spec, integration, snapshot, acceptance
Workflow
feature-implementation-workflow.md — step-by-step feature building
Navigation index
references/_index.md
Weekly Installs
10
Repository
swiftyjourney/i…rt-skill
GitHub Stars
2
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass