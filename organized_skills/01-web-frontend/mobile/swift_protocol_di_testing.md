---
rating: ⭐⭐⭐
title: swift-protocol-di-testing
url: https://skills.sh/affaan-m/everything-claude-code/swift-protocol-di-testing
---

# swift-protocol-di-testing

skills/affaan-m/everything-claude-code/swift-protocol-di-testing
swift-protocol-di-testing
Installation
$ npx skills add https://github.com/affaan-m/everything-claude-code --skill swift-protocol-di-testing
Summary

Protocol-based dependency injection for testable Swift code with focused abstractions and Swift Testing.

Define small, single-responsibility protocols for each external concern (file system, network, APIs) and provide default production implementations
Create mock implementations with configurable error properties to test failure paths deterministically without real I/O
Inject dependencies via default parameters so production code uses real implementations automatically while tests override with mocks
Ensure Sendable conformance on protocols and mocks for safe use across actor boundaries in Swift concurrency
SKILL.md
Swift Protocol-Based Dependency Injection for Testing

Patterns for making Swift code testable by abstracting external dependencies (file system, network, iCloud) behind small, focused protocols. Enables deterministic tests without I/O.

When to Activate
Writing Swift code that accesses file system, network, or external APIs
Need to test error handling paths without triggering real failures
Building modules that work across environments (app, test, SwiftUI preview)
Designing testable architecture with Swift concurrency (actors, Sendable)
Core Pattern
1. Define Small, Focused Protocols

Each protocol handles exactly one external concern.

// File system access
public protocol FileSystemProviding: Sendable {
    func containerURL(for purpose: Purpose) -> URL?
}

// File read/write operations
public protocol FileAccessorProviding: Sendable {
    func read(from url: URL) throws -> Data
    func write(_ data: Data, to url: URL) throws
    func fileExists(at url: URL) -> Bool
}

// Bookmark storage (e.g., for sandboxed apps)
public protocol BookmarkStorageProviding: Sendable {
    func saveBookmark(_ data: Data, for key: String) throws
    func loadBookmark(for key: String) throws -> Data?
}

2. Create Default (Production) Implementations
public struct DefaultFileSystemProvider: FileSystemProviding {
    public init() {}

    public func containerURL(for purpose: Purpose) -> URL? {
        FileManager.default.url(forUbiquityContainerIdentifier: nil)
    }
}

public struct DefaultFileAccessor: FileAccessorProviding {
    public init() {}

    public func read(from url: URL) throws -> Data {
        try Data(contentsOf: url)
    }

    public func write(_ data: Data, to url: URL) throws {
        try data.write(to: url, options: .atomic)
    }

    public func fileExists(at url: URL) -> Bool {
        FileManager.default.fileExists(atPath: url.path)
    }
}

3. Create Mock Implementations for Testing
public final class MockFileAccessor: FileAccessorProviding, @unchecked Sendable {
    public var files: [URL: Data] = [:]
    public var readError: Error?
    public var writeError: Error?

    public init() {}

    public func read(from url: URL) throws -> Data {
        if let error = readError { throw error }
        guard let data = files[url] else {
            throw CocoaError(.fileReadNoSuchFile)
        }
        return data
    }

    public func write(_ data: Data, to url: URL) throws {
        if let error = writeError { throw error }
        files[url] = data
    }

    public func fileExists(at url: URL) -> Bool {
        files[url] != nil
    }
}

4. Inject Dependencies with Default Parameters

Production code uses defaults; tests inject mocks.

public actor SyncManager {
    private let fileSystem: FileSystemProviding
    private let fileAccessor: FileAccessorProviding

    public init(
        fileSystem: FileSystemProviding = DefaultFileSystemProvider(),
        fileAccessor: FileAccessorProviding = DefaultFileAccessor()
    ) {
        self.fileSystem = fileSystem
        self.fileAccessor = fileAccessor
    }

    public func sync() async throws {
        guard let containerURL = fileSystem.containerURL(for: .sync) else {
            throw SyncError.containerNotAvailable
        }
        let data = try fileAccessor.read(
            from: containerURL.appendingPathComponent("data.json")
        )
        // Process data...
    }
}

5. Write Tests with Swift Testing
import Testing

@Test("Sync manager handles missing container")
func testMissingContainer() async {
    let mockFileSystem = MockFileSystemProvider(containerURL: nil)
    let manager = SyncManager(fileSystem: mockFileSystem)

    await #expect(throws: SyncError.containerNotAvailable) {
        try await manager.sync()
    }
}

@Test("Sync manager reads data correctly")
func testReadData() async throws {
    let mockFileAccessor = MockFileAccessor()
    mockFileAccessor.files[testURL] = testData

    let manager = SyncManager(fileAccessor: mockFileAccessor)
    let result = try await manager.loadData()

    #expect(result == expectedData)
}

@Test("Sync manager handles read errors gracefully")
func testReadError() async {
    let mockFileAccessor = MockFileAccessor()
    mockFileAccessor.readError = CocoaError(.fileReadCorruptFile)

    let manager = SyncManager(fileAccessor: mockFileAccessor)

    await #expect(throws: SyncError.self) {
        try await manager.sync()
    }
}

Best Practices
Single Responsibility: Each protocol should handle one concern — don't create "god protocols" with many methods
Sendable conformance: Required when protocols are used across actor boundaries
Default parameters: Let production code use real implementations by default; only tests need to specify mocks
Error simulation: Design mocks with configurable error properties for testing failure paths
Only mock boundaries: Mock external dependencies (file system, network, APIs), not internal types
Anti-Patterns to Avoid
Creating a single large protocol that covers all external access
Mocking internal types that have no external dependencies
Using #if DEBUG conditionals instead of proper dependency injection
Forgetting Sendable conformance when used with actors
Over-engineering: if a type has no external dependencies, it doesn't need a protocol
When to Use
Any Swift code that touches file system, network, or external APIs
Testing error handling paths that are hard to trigger in real environments
Building modules that need to work in app, test, and SwiftUI preview contexts
Apps using Swift concurrency (actors, structured concurrency) that need testable architecture
Weekly Installs
2.9K
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