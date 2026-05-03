---
title: code-quality
url: https://skills.sh/tursodatabase/turso/code-quality
---

# code-quality

skills/tursodatabase/turso/code-quality
code-quality
Installation
$ npx skills add https://github.com/tursodatabase/turso --skill code-quality
Summary

Production-grade code standards emphasizing correctness, crash-safety, and Rust idioms over convenience.

Prioritizes data integrity: crash on invalid state rather than corrupt data; assert invariants aggressively; handle all errors explicitly
Rust-specific patterns: make illegal states unrepresentable, use exhaustive pattern matching and enums over strings, minimize allocations
Comments document why, not what; avoid temporal markers, AI conversation references, and code-repeating explanations
Rejects over-engineering: implement only requested changes, skip error handling for impossible scenarios, avoid premature abstractions
Index mutations require careful ordering verification against SQLite to prevent inconsistencies
SKILL.md
Code Quality Guide
Core Principle

Production database. Correctness paramount. Crash > corrupt.

Correctness Rules
No workarounds or quick hacks. Handle all errors, check invariants
Assert often. Never silently fail or swallow edge cases
Crash on invalid state if it risks data integrity. Don't continue in undefined state
Consider edge cases. On long enough timeline, all possible bugs will happen
Rust Patterns
Make illegal states unrepresentable
Exhaustive pattern matching
Prefer enums over strings/sentinels
Minimize heap allocations
Write CPU-friendly code (microsecond = long time)
If-Statements

Wrong:

if condition {
    // happy path
} else {
    // "shouldn't happen" - silently ignored
}


Right:

// If only one branch should ever be hit:
assert!(condition, "invariant violated: ...");
// OR
return Err(LimboError::InternalError("unexpected state".into()));
// OR
unreachable!("impossible state: ...");


Use if-statements only when both branches are expected paths.

Comments

Do:

Document WHY, not what
Document functions, structs, enums, variants
Focus on why something is necessary

Don't:

Comments that repeat code
References to AI conversations ("This test should trigger the bug")
Temporal markers ("added", "existing code", "Phase 1")
Avoid Over-Engineering
Only changes directly requested or clearly necessary
Don't add features beyond what's asked
Don't add docstrings/comments to unchanged code
Don't add error handling for impossible scenarios
Don't create abstractions for one-time operations
Three similar lines > premature abstraction
Index Mutations

When code involves index inserts, deletes, or conflict resolution, double-check the ordering against SQLite. Wrong ordering causes index inconsistencies. and easy to miss.

Ensure understanding of IO model
Async IO model
Cleanup
Delete unused code completely
No backwards-compat hacks (renamed _vars, re-exports, // removed comments)
Weekly Installs
948
Repository
tursodatabase/turso
GitHub Stars
18.4K
First Seen
Jan 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass