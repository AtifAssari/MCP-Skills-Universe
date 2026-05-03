---
title: swift-best-practices
url: https://skills.sh/secondsky/claude-skills/swift-best-practices
---

# swift-best-practices

skills/secondsky/claude-skills/swift-best-practices
swift-best-practices
Installation
$ npx skills add https://github.com/secondsky/claude-skills --skill swift-best-practices
SKILL.md
Swift Best Practices Skill
Overview

Apply modern Swift development best practices focusing on Swift 6+ features, concurrency safety, API design principles, and code quality guidelines for iOS and macOS projects targeting macOS 15.7+.

When to Use This Skill

Use this skill when:

Writing new Swift code for iOS or macOS applications
Reviewing Swift code for correctness, safety, and style
Implementing Swift concurrency features (async/await, actors, MainActor)
Designing Swift APIs and public interfaces
Migrating code from Swift 5 to Swift 6
Addressing concurrency warnings, data race issues, or compiler errors related to Sendable/isolation
Working with modern Swift language features introduced in Swift 6 and 6.2
SwiftLens MCP Integration (Claude Code)

This skill complements SwiftLens MCP server for semantic-level Swift code analysis.

What SwiftLens Provides:

15 tools for semantic Swift analysis using Apple's SourceKit-LSP
Symbol lookup, cross-file references, type information
Safe code modification and refactoring
Compiler-grade understanding of Swift code structure

What This Skill Provides:

Swift 6+ design patterns and best practices
Concurrency strategies (async/await, actors, MainActor)
API design guidelines and naming conventions
Migration guidance (Swift 5 → Swift 6)

Setup for Claude Code CLI:

Create .claude/mcps/swiftlens.json in your Swift project:

{
  "mcpServers": {
    "swiftlens": {
      "description": "SwiftLens MCP provides semantic Swift analysis via SourceKit-LSP",
      "command": "uvx",
      "args": ["swiftlens"]
    }
  }
}


⚠️ Note: This is Claude Code configuration (not Claude Desktop). See references/swiftlens-mcp-claude-code.md for complete setup guide, all 15 tools, index building, and usage examples.

Workflow: SwiftLens provides runtime analysis (what the code is doing), this skill provides design expertise (what the code should be doing).

Core Guidelines
Fundamental Principles
Clarity at point of use is paramount - evaluate designs by examining use cases, not just declarations
Clarity over brevity - compact code comes from the type system, not minimal characters
Write documentation for every public declaration - if you can't describe functionality simply, the API may be poorly designed
Name by role, not type - var greeting = "Hello" not var string = "Hello"
Favour elegance through simplicity - avoid over-engineering unless complexity genuinely warrants it
Swift 6 Concurrency Model

Swift 6 enables complete concurrency checking by default with region-based isolation (SE-0414). The compiler now proves code safety, eliminating many false positives whilst catching real concurrency issues at compile time.

Critical understanding:

Async ≠ background - async functions can suspend but don't automatically run on background threads
Actors protect mutable shared state through automatic synchronisation
@MainActor ensures UI-related code executes on the main thread
Global actor-isolated types are automatically Sendable
Essential Patterns
Async/Await
// Parallel execution with async let
func fetchData() async -> (String, Int) {
    async let stringData = fetchString()
    async let intData = fetchInt()
    return await (stringData, intData)
}

// Always check cancellation in long-running operations
func process(_ items: [Item]) async throws -> [Result] {
    var results: [Result] = []
    for item in items {
        try Task.checkCancellation()
        results.append(await process(item))
    }
    return results
}

MainActor for UI Code
// Apply at type level for consistent isolation
@MainActor
class ContentViewModel: ObservableObject {
    @Published var images: [UIImage] = []

    func fetchData() async throws {
        self.images = try await fetchImages()
    }
}

// Avoid MainActor.run when direct await works
await doMainActorStuff()  // Good
await MainActor.run { doMainActorStuff() }  // Unnecessary

Actor Isolation
actor DataCache {
    private var cache: [String: Data] = [:]

    func store(_ data: Data, forKey key: String) {
        cache[key] = data  // No await needed inside actor
    }

    nonisolated func cacheType() -> String {
        return "DataCache"  // No await needed - doesn't access isolated state
    }
}

Common Pitfalls to Avoid
Don't mark functions as async unnecessarily - async calling convention has overhead
Never use DispatchSemaphore with async/await - risk of deadlock
Don't create stateless actors - use non-isolated async functions instead
Avoid split isolation - don't mix isolation domains within one type
Check task cancellation - long operations must check Task.checkCancellation()
Don't assume async means background - explicitly move work to background if needed
Avoid excessive context switching - group operations within same isolation domain
API Design Quick Reference
Naming Conventions
Types/protocols: UpperCamelCase
Everything else: lowerCamelCase
Protocols describing capabilities: -able, -ible, -ing suffixes (Equatable, ProgressReporting)
Factory methods: Begin with make (x.makeIterator())
Mutating pairs: imperative vs past participle (x.sort() / x.sorted())
Method Naming by Side Effects
No side effects: Noun phrases (x.distance(to: y))
With side effects: Imperative verbs (x.append(y), x.sort())
Argument Labels
Omit when arguments can't be distinguished: min(number1, number2)
Value-preserving conversions omit first label: Int64(someUInt32)
Prepositional phrases label at preposition: x.removeBoxes(havingLength: 12)
Label all other arguments
Swift 6 Breaking Changes
Must Explicitly Mark Types with @MainActor (SE-0401)

Property wrappers no longer infer actor isolation automatically.

@MainActor
struct LogInView: View {
    @StateObject private var model = ViewModel()
}

Global Variables Must Be Concurrency-Safe (SE-0412)
static let config = Config()  // Constant - OK
@MainActor static var state = State()  // Actor-isolated - OK
nonisolated(unsafe) var cache = [String: Data]()  // Unsafe - use with caution

Other Changes
@UIApplicationMain/@NSApplicationMain deprecated (use @main)
any required for existential types
Import visibility requires explicit access control
API Availability Patterns
// Basic availability
@available(macOS 15, iOS 18, *)
func modernAPI() { }

// Deprecation with message
@available(*, deprecated, message: "Use newMethod() instead")
func oldMethod() { }

// Renaming with auto-fix
@available(*, unavailable, renamed: "newMethod")
func oldMethod() { }

// Runtime checking
if #available(iOS 18, *) {
    // iOS 18+ code
}

// Inverted checking (Swift 5.6+)
if #unavailable(iOS 18, *) {
    // iOS 17 and lower
}


Key differences:

deprecated - Warning, allows usage
obsoleted - Error from specific version
unavailable - Error, completely prevents usage
How to Use This Skill
When Writing Code
Apply naming conventions following role-based, clarity-first principles
Use appropriate isolation (@MainActor for UI, actors for mutable state)
Implement async/await patterns correctly with proper cancellation handling
Follow Swift 6 concurrency model - trust compiler's flow analysis
Document public APIs with clear, concise summaries
When Reviewing Code
Check for concurrency safety violations
Verify proper actor isolation and Sendable conformance
Ensure async functions handle cancellation appropriately
Validate API naming follows Swift guidelines
Confirm availability annotations are correct for target platforms
Code Quality Standards
Minimise comments - code should be self-documenting where possible
Avoid over-engineering and unnecessary abstractions
Use meaningful variable names based on role, not type
Follow established project architecture and patterns
Prefer count(where:) over filter().count
Use InlineArray for fixed-size, performance-critical data
Trust compiler's concurrency flow analysis - avoid unnecessary Sendable conformances
Resources
references/

Detailed reference material to load when in-depth information is needed:

swiftlens-mcp-claude-code.md - SwiftLens MCP server setup for Claude Code CLI, 15 semantic analysis tools, index building, usage examples, and integration workflows
api-design.md - Complete API design conventions, documentation standards, parameter guidelines, and naming patterns
concurrency.md - Detailed async/await patterns, actor best practices, common pitfalls, performance considerations, and thread safety patterns
swift6-features.md - New language features in Swift 6/6.2, breaking changes, migration strategies, and modern patterns
availability-patterns.md - Comprehensive @available attribute usage, deprecation strategies, and platform version management

Load these references when detailed information is needed beyond the core guidelines provided above.

Platform Requirements
Swift 6.0+ compiler for Swift 6 features
Swift 6.2+ for InlineArray and enhanced concurrency features
macOS 15.7+ with appropriate SDK
iOS 18+ for latest platform features
Use #available for runtime platform detection
Use @available for API availability marking
Weekly Installs
180
Repository
secondsky/claude-skills
GitHub Stars
129
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass