---
rating: ⭐⭐
title: modern-swift
url: https://skills.sh/johnrogers/claude-swift-engineering/modern-swift
---

# modern-swift

skills/johnrogers/claude-swift-engineering/modern-swift
modern-swift
Installation
$ npx skills add https://github.com/johnrogers/claude-swift-engineering --skill modern-swift
SKILL.md
Modern Swift (6.2+)

Swift 6.2 introduces strict compile-time concurrency checking with async/await, actors, and Sendable constraints that prevent data races at compile time instead of runtime. This is the foundation of safe concurrent Swift.

Overview

Modern Swift replaces older concurrency patterns (completion handlers, DispatchQueue, locks) with compiler-enforced safety. The core principle: if it compiles with strict concurrency enabled, it cannot have data races.

Quick Reference
Need	Use	NOT
Async operation	async/await	Completion handlers
Main thread work	@MainActor	DispatchQueue.main
Shared mutable state	actor	Locks, serial queues
Parallel tasks	TaskGroup	DispatchGroup
Thread safety	Sendable	@unchecked everywhere
Core Workflow

When writing async Swift code:

Mark async functions with async, call with await
Apply @MainActor to view models and UI-updating code
Use actor instead of locks for shared mutable state
Check Task.isCancelled or call Task.checkCancellation() in loops
Enable strict concurrency in Package.swift for compile-time safety
Reference Loading Guide

ALWAYS load reference files if there is even a small chance the content may be required. It's better to have the context than to miss a pattern or make a mistake.

Reference	Load When
Concurrency Essentials	Writing async code, converting completion handlers, using await
Swift 6 Concurrency	Using @concurrent, nonisolated(unsafe), or actor patterns
Task Groups	Running multiple async operations in parallel
Task Cancellation	Implementing long-running or cancellable operations
Strict Concurrency	Enabling Swift 6 strict mode or fixing Sendable errors
Macros	Using or understanding Swift macros like @Observable
Modern Attributes	Migrating legacy code or using @preconcurrency, @backDeployed
Migration Patterns	Modernizing delegate patterns or UIKit views
Common Mistakes

@unchecked Sendable as a quick fix — Using @unchecked Sendable to silence compiler errors means you've opted out of safety. If the error persists after @unchecked, your code has a potential data race. Fix the underlying issue instead.

Missing await at call sites — Forgetting await when calling async functions is a compiler error, but checking Task.isCancelled in a loop without calling Task.checkCancellation() silently ignores cancellation.

Capturing self in async blocks without weak — Holding a strong reference to self in a long-running async task prevents deinit. Always use [weak self] in closures or use .task which auto-manages the lifecycle.

Not checking task cancellation — Long-running operations should regularly check Task.isCancelled or call Task.checkCancellation(), otherwise cancellation signals are ignored.

Forgetting @MainActor on UI code and test suites — Main test struct and view models that update @Published properties need @MainActor. Forgetting it silently allows cross-thread mutations. Apply @MainActor to: view models, view structs, main test structs, and any type that touches UI.

Actor re-entrancy surprises — await inside an actor method can release the lock temporarily. Another task may modify actor state. Design actor methods assuming state can change between await points.

Weekly Installs
105
Repository
johnrogers/clau…ineering
GitHub Stars
201
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass