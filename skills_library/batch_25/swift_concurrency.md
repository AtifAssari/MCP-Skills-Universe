---
title: swift_concurrency
url: https://skills.sh/swiftzilla/skills/swift_concurrency
---

# swift_concurrency

skills/swiftzilla/skills/swift_concurrency
swift_concurrency
Installation
$ npx skills add https://github.com/swiftzilla/skills --skill swift_concurrency
SKILL.md
Swift Concurrency

This skill covers Swift's modern concurrency features from Swift 5.5 through Swift 6, including async/await, structured concurrency, actors, and Swift 6's strict data-race safety.

Overview

Swift's modern concurrency model provides a safer, more intuitive way to write asynchronous code. Swift 6 takes this further with compile-time data-race safety, turning potential concurrency bugs into compiler errors.

Available References
Swift 6 & Strict Concurrency
Swift 6 Strict Mode - Complete concurrency checking, data race prevention
Sendable Protocol - Sendable conformance, @Sendable closures, thread safety
Isolation & Actors - @MainActor, global actors, region-based isolation
Core Concurrency
Async/Await - Asynchronous functions, Task, TaskGroup, Actor basics
Swift 6 Highlights
Strict Concurrency by Default

Swift 6 enforces data-race safety at compile time:

// ❌ Compile-time error in Swift 6
var globalCounter = 0

func increment() {
    globalCounter += 1  // Error: concurrent access
}

// ✅ Safe with actor isolation
actor Counter {
    private var value = 0
    func increment() { value += 1 }
}

Sendable Protocol

Mark types safe to share across concurrency boundaries:

struct User: Sendable {
    let id: Int
    let name: String
}

@Sendable func process() async {
    // Captures must be Sendable
}

MainActor & Global Actors
@MainActor
class ViewModel: ObservableObject {
    @Published var items = [Item]()
}

@globalActor
actor DatabaseActor {
    static let shared = DatabaseActor()
    private init() {}
}

Quick Reference
Async/Await Basics
func fetchData() async throws -> Data {
    let (data, _) = try await URLSession.shared.data(from: url)
    return data
}

Swift 6 Migration Checklist
 Enable Swift 6 language mode
 Enable strict concurrency checking
 Wrap global mutable state in actors
 Add Sendable conformance to types
 Fix non-Sendable captures in @Sendable closures
 Isolate UI code with @MainActor
 Audit third-party dependencies
Running Async Code
// Fire-and-forget
Task {
    let result = await asyncOperation()
}

// With priority
Task(priority: .background) {
    await heavyComputation()
}

// With cancellation
let task = Task {
    try await longRunningOperation()
}
task.cancel()

Concurrent Operations
// Async let (parallel await)
async let task1 = fetchUser()
async let task2 = fetchSettings()
let (user, settings) = try await (task1, task2)

// TaskGroup
try await withThrowingTaskGroup(of: Item.self) { group in
    for id in ids {
        group.addTask { try await fetchItem(id: id) }
    }
    return try await group.reduce(into: []) { $0.append($1) }
}

Actor Thread Safety
actor BankAccount {
    private var balance: Double = 0
    
    func deposit(_ amount: Double) {
        balance += amount
    }
    
    func getBalance() -> Double {
        return balance
    }
}

let account = BankAccount()
await account.deposit(100)

Isolation Boundaries
// Crossing isolation boundaries
@MainActor
func updateUI() async {
    // On main thread
    let data = await fetchData()  // Switch to non-isolated
    label.text = data  // Back to main thread
}

// Region transfer
func process() async {
    let data = Data()  // Disconnected
    await save(data)   // Transfer to actor
    // ❌ Can't use data here anymore
}

Swift 6 vs Swift 5.x
Feature	Swift 5.x	Swift 6
Concurrency checking	Warnings	Errors
Data race safety	Runtime	Compile-time
Sendable enforcement	Opt-in	Required
Global variable safety	Warning	Error
Strict mode	Experimental	Default
Best Practices
Swift 6 Best Practices
Enable Swift 6 mode early - Start migration now
Use actors for shared state - Default to actors over locks
Design Sendable types - Make types Sendable from the start
Isolate UI with @MainActor - All UI code on main thread
Respect isolation regions - Don't use values after transfer
Leverage compile-time safety - Let compiler catch data races
Create domain actors - Custom global actors for heavy work
General Concurrency
Prefer async/await - Over completion handlers
Use structured concurrency - Clear task hierarchies
Handle cancellation - Check Task.isCancelled
Use value types - Immutable data is thread-safe
Avoid shared mutable state - Or protect with actors
Migration from Completion Handlers
// Before (Swift 5)
func fetchUser(completion: @escaping (Result<User, Error>) -> Void) {
    URLSession.shared.dataTask(with: url) { data, response, error in
        // Handle result
        completion(result)
    }.resume()
}

// After (Swift 6)
func fetchUser() async throws -> User {
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: data)
}

Common Swift 6 Errors
Error	Quick Fix
Concurrent access to global	Wrap in actor
Non-Sendable in @Sendable	Make type Sendable
Actor isolation violation	Add await or change isolation
Use after transfer	Use before transfer or copy value
Main actor isolation	Add @MainActor annotation
Resources
Swift Evolution: https://github.com/apple/swift-evolution
SE-0412: Strict concurrency for global variables
SE-0471: SerialExecutor isolation checking
SE-0430: Sending parameters
SE-0414: Region-based isolation
Apple Docs: https://developer.apple.com/documentation/swift/concurrency
SwiftZilla: https://swiftzilla.dev
For More Information

Each reference file contains detailed information, code examples, and best practices for specific topics. Visit https://swiftzilla.dev for comprehensive Swift concurrency documentation.

Weekly Installs
40
Repository
swiftzilla/skills
GitHub Stars
6
First Seen
Jan 28, 2026