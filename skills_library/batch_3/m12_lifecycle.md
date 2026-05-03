---
title: m12-lifecycle
url: https://skills.sh/zhanghandong/rust-skills/m12-lifecycle
---

# m12-lifecycle

skills/zhanghandong/rust-skills/m12-lifecycle
m12-lifecycle
Installation
$ npx skills add https://github.com/zhanghandong/rust-skills --skill m12-lifecycle
Summary

Design resource creation, cleanup, and scope using RAII, lazy initialization, and pooling patterns.

Covers five lifecycle patterns: RAII with Drop trait, lazy initialization via OnceLock/LazyLock, connection pooling with r2d2/deadpool, guard-based scoped access, and transaction scope boundaries
Includes decision framework for resource cost, scope determination, and error handling during cleanup
Provides pattern templates for RAII guards and lazy singletons, plus common errors and anti-patterns to avoid
Traces connections to ownership models (Layer 1) and domain constraints (Layer 3) for integrated design
SKILL.md
Resource Lifecycle

Layer 2: Design Choices

Core Question

When should this resource be created, used, and cleaned up?

Before implementing lifecycle:

What's the resource's scope?
Who owns the cleanup responsibility?
What happens on error?
Lifecycle Pattern → Implementation
Pattern	When	Implementation
RAII	Auto cleanup	Drop trait
Lazy init	Deferred creation	OnceLock, LazyLock
Pool	Reuse expensive resources	r2d2, deadpool
Guard	Scoped access	MutexGuard pattern
Scope	Transaction boundary	Custom struct + Drop
Thinking Prompt

Before designing lifecycle:

What's the resource cost?

Cheap → create per use
Expensive → pool or cache
Global → lazy singleton

What's the scope?

Function-local → stack allocation
Request-scoped → passed or extracted
Application-wide → static or Arc

What about errors?

Cleanup must happen → Drop
Cleanup is optional → explicit close
Cleanup can fail → Result from close
Trace Up ↑

To domain constraints (Layer 3):

"How should I manage database connections?"
    ↑ Ask: What's the connection cost?
    ↑ Check: domain-* (latency requirements)
    ↑ Check: Infrastructure (connection limits)

Question	Trace To	Ask
Connection pooling	domain-*	What's acceptable latency?
Resource limits	domain-*	What are infra constraints?
Transaction scope	domain-*	What must be atomic?
Trace Down ↓

To implementation (Layer 1):

"Need automatic cleanup"
    ↓ m02-resource: Implement Drop
    ↓ m01-ownership: Clear owner for cleanup

"Need lazy initialization"
    ↓ m03-mutability: OnceLock for thread-safe
    ↓ m07-concurrency: LazyLock for sync

"Need connection pool"
    ↓ m07-concurrency: Thread-safe pool
    ↓ m02-resource: Arc for sharing

Quick Reference
Pattern	Type	Use Case
RAII	Drop trait	Auto cleanup on scope exit
Lazy Init	OnceLock, LazyLock	Deferred initialization
Pool	r2d2, deadpool	Connection reuse
Guard	MutexGuard	Scoped lock release
Scope	Custom struct	Transaction boundaries
Lifecycle Events
Event	Rust Mechanism
Creation	new(), Default
Lazy Init	OnceLock::get_or_init
Usage	&self, &mut self
Cleanup	Drop::drop()
Pattern Templates
RAII Guard
struct FileGuard {
    path: PathBuf,
    _handle: File,
}

impl Drop for FileGuard {
    fn drop(&mut self) {
        // Cleanup: remove temp file
        let _ = std::fs::remove_file(&self.path);
    }
}

Lazy Singleton
use std::sync::OnceLock;

static CONFIG: OnceLock<Config> = OnceLock::new();

fn get_config() -> &'static Config {
    CONFIG.get_or_init(|| {
        Config::load().expect("config required")
    })
}

Common Errors
Error	Cause	Fix
Resource leak	Forgot Drop	Implement Drop or RAII wrapper
Double free	Manual memory	Let Rust handle
Use after drop	Dangling reference	Check lifetimes
E0509 move out of Drop	Moving owned field	Option::take()
Pool exhaustion	Not returned	Ensure Drop returns
Anti-Patterns
Anti-Pattern	Why Bad	Better
Manual cleanup	Easy to forget	RAII/Drop
lazy_static!	External dep	std::sync::OnceLock
Global mutable state	Thread unsafety	OnceLock or proper sync
Forget to close	Resource leak	Drop impl
Related Skills
When	See
Smart pointers	m02-resource
Thread-safe init	m07-concurrency
Domain scopes	m09-domain
Error in cleanup	m06-error-handling
Weekly Installs
659
Repository
zhanghandong/rust-skills
GitHub Stars
1.1K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass