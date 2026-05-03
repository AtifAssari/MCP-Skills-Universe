---
title: swift-concurrency-6-2
url: https://skills.sh/affaan-m/everything-claude-code/swift-concurrency-6-2
---

# swift-concurrency-6-2

skills/affaan-m/everything-claude-code/swift-concurrency-6-2
swift-concurrency-6-2
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill swift-concurrency-6-2
Summary

Single-threaded by default with explicit background offloading via @concurrent and isolated protocol conformances.

Async functions stay on the calling actor by default, eliminating implicit background offloading that caused data-race errors in Swift 6.1 and earlier
Isolated conformances allow MainActor types to safely conform to non-isolated protocols without unsafe workarounds
@concurrent attribute explicitly offloads CPU-intensive work to background threads; requires nonisolated type and await at call sites
MainActor default inference mode (opt-in for app targets) reduces boilerplate annotations for predominantly single-threaded code
Requires Xcode 26 build settings (SE-0466 and SE-0461) for full Approachable Concurrency support; enables incremental migration from Swift 5.x and 6.0/6.1
SKILL.md
Swift 6.2 Approachable Concurrency

Patterns for adopting Swift 6.2's concurrency model where code runs single-threaded by default and concurrency is introduced explicitly. Eliminates common data-race errors without sacrificing performance.

When to Activate
Migrating Swift 5.x or 6.0/6.1 projects to Swift 6.2
Resolving data-race safety compiler errors
Designing MainActor-based app architecture
Offloading CPU-intensive work to background threads
Implementing protocol conformances on MainActor-isolated types
Enabling Approachable Concurrency build settings in Xcode 26
Core Problem: Implicit Background Offloading

In Swift 6.1 and earlier, async functions could be implicitly offloaded to background threads, causing data-race errors even in seemingly safe code:

// Swift 6.1: ERROR
@MainActor
final class StickerModel {
    let photoProcessor = PhotoProcessor()

    func extractSticker(_ item: PhotosPickerItem) async throws -> Sticker? {
        guard let data = try await item.loadTransferable(type: Data.self) else { return nil }

        // Error: Sending 'self.photoProcessor' risks causing data races
        return await photoProcessor.extractSticker(data: data, with: item.itemIdentifier)
    }
}


Swift 6.2 fixes this: async functions stay on the calling actor by default.

// Swift 6.2: OK — async stays on MainActor, no data race
@MainActor
final class StickerModel {
    let photoProcessor = PhotoProcessor()

    func extractSticker(_ item: PhotosPickerItem) async throws -> Sticker? {
        guard let data = try await item.loadTransferable(type: Data.self) else { return nil }
        return await photoProcessor.extractSticker(data: data, with: item.itemIdentifier)
    }
}

Core Pattern — Isolated Conformances

MainActor types can now conform to non-isolated protocols safely:

protocol Exportable {
    func export()
}

// Swift 6.1: ERROR — crosses into main actor-isolated code
// Swift 6.2: OK with isolated conformance
extension StickerModel: @MainActor Exportable {
    func export() {
        photoProcessor.exportAsPNG()
    }
}


The compiler ensures the conformance is only used on the main actor:

// OK — ImageExporter is also @MainActor
@MainActor
struct ImageExporter {
    var items: [any Exportable]

    mutating func add(_ item: StickerModel) {
        items.append(item)  // Safe: same actor isolation
    }
}

// ERROR — nonisolated context can't use MainActor conformance
nonisolated struct ImageExporter {
    var items: [any Exportable]

    mutating func add(_ item: StickerModel) {
        items.append(item)  // Error: Main actor-isolated conformance cannot be used here
    }
}

Core Pattern — Global and Static Variables

Protect global/static state with MainActor:

// Swift 6.1: ERROR — non-Sendable type may have shared mutable state
final class StickerLibrary {
    static let shared: StickerLibrary = .init()  // Error
}

// Fix: Annotate with @MainActor
@MainActor
final class StickerLibrary {
    static let shared: StickerLibrary = .init()  // OK
}

MainActor Default Inference Mode

Swift 6.2 introduces a mode where MainActor is inferred by default — no manual annotations needed:

// With MainActor default inference enabled:
final class StickerLibrary {
    static let shared: StickerLibrary = .init()  // Implicitly @MainActor
}

final class StickerModel {
    let photoProcessor: PhotoProcessor
    var selection: [PhotosPickerItem]  // Implicitly @MainActor
}

extension StickerModel: Exportable {  // Implicitly @MainActor conformance
    func export() {
        photoProcessor.exportAsPNG()
    }
}


This mode is opt-in and recommended for apps, scripts, and other executable targets.

Core Pattern — @concurrent for Background Work

When you need actual parallelism, explicitly offload with @concurrent:

Important: This example requires Approachable Concurrency build settings — SE-0466 (MainActor default isolation) and SE-0461 (NonisolatedNonsendingByDefault). With these enabled, extractSticker stays on the caller's actor, making mutable state access safe. Without these settings, this code has a data race — the compiler will flag it.

nonisolated final class PhotoProcessor {
    private var cachedStickers: [String: Sticker] = [:]

    func extractSticker(data: Data, with id: String) async -> Sticker {
        if let sticker = cachedStickers[id] {
            return sticker
        }

        let sticker = await Self.extractSubject(from: data)
        cachedStickers[id] = sticker
        return sticker
    }

    // Offload expensive work to concurrent thread pool
    @concurrent
    static func extractSubject(from data: Data) async -> Sticker { /* ... */ }
}

// Callers must await
let processor = PhotoProcessor()
processedPhotos[item.id] = await processor.extractSticker(data: data, with: item.id)


To use @concurrent:

Mark the containing type as nonisolated
Add @concurrent to the function
Add async if not already asynchronous
Add await at call sites
Key Design Decisions
Decision	Rationale
Single-threaded by default	Most natural code is data-race free; concurrency is opt-in
Async stays on calling actor	Eliminates implicit offloading that caused data-race errors
Isolated conformances	MainActor types can conform to protocols without unsafe workarounds
@concurrent explicit opt-in	Background execution is a deliberate performance choice, not accidental
MainActor default inference	Reduces boilerplate @MainActor annotations for app targets
Opt-in adoption	Non-breaking migration path — enable features incrementally
Migration Steps
Enable in Xcode: Swift Compiler > Concurrency section in Build Settings
Enable in SPM: Use SwiftSettings API in package manifest
Use migration tooling: Automatic code changes via swift.org/migration
Start with MainActor defaults: Enable inference mode for app targets
Add @concurrent where needed: Profile first, then offload hot paths
Test thoroughly: Data-race issues become compile-time errors
Best Practices
Start on MainActor — write single-threaded code first, optimize later
Use @concurrent only for CPU-intensive work — image processing, compression, complex computation
Enable MainActor inference mode for app targets that are mostly single-threaded
Profile before offloading — use Instruments to find actual bottlenecks
Protect globals with MainActor — global/static mutable state needs actor isolation
Use isolated conformances instead of nonisolated workarounds or @Sendable wrappers
Migrate incrementally — enable features one at a time in build settings
Anti-Patterns to Avoid
Applying @concurrent to every async function (most don't need background execution)
Using nonisolated to suppress compiler errors without understanding isolation
Keeping legacy DispatchQueue patterns when actors provide the same safety
Skipping model.availability checks in concurrency-related Foundation Models code
Fighting the compiler — if it reports a data race, the code has a real concurrency issue
Assuming all async code runs in the background (Swift 6.2 default: stays on calling actor)
When to Use
All new Swift 6.2+ projects (Approachable Concurrency is the recommended default)
Migrating existing apps from Swift 5.x or 6.0/6.1 concurrency
Resolving data-race safety compiler errors during Xcode 26 adoption
Building MainActor-centric app architectures (most UI apps)
Performance optimization — offloading specific heavy computations to background
Weekly Installs
2.8K
Repository
affaan-m/everyt…ude-code
GitHub Stars
171.6K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass