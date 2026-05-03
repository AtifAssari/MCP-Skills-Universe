---
title: rust
url: https://skills.sh/petekp/claude-code-setup/rust
---

# rust

skills/petekp/claude-code-setup/rust
rust
Installation
$ npx skills add https://github.com/petekp/claude-code-setup --skill rust
SKILL.md
Rust Engineering Guide

Patterns for building reliable Rust systems that handle file-backed data, external process integration, and cross-language boundaries.

Core Philosophy

Conservative by Default: Inputs from files, subprocesses, and external systems are untrusted.

Prefer false negatives over false positives
Same input → same output (deterministic)
Never panic on user machines due to bad input

Canonical Model Ownership: When Rust is the source of truth, maintain separate representations:

Layer	Purpose	Characteristics
Internal domain	Business logic	Expressive enums, rich types
FFI DTOs	Cross-language boundary	Flat, stable, String-heavy
File format	Persistence	Versioned, round-trippable
External input	Validation boundary	Strictly validated, never trusted

Safe Rust Only: None of these patterns require unsafe. Use ecosystem crates for safe abstractions.

Reference Guides

Load the relevant reference when working in that domain:

Domain	Reference	When to Load
Data Modeling	references/data-modeling.md	Serde patterns, UniFFI, strong types, versioned schemas
File I/O	references/file-io.md	Atomic writes, concurrency control, file watching
Process Integration	references/process-integration.md	PID verification, subprocess handling, timestamps
Text & Parsing	references/text-and-parsing.md	UTF-8 safety, path normalization, state machines
Testing	references/testing.md	Round-trip tests, fuzz testing, Clippy lints
Error Handling
Library vs Application Errors

Libraries (public API): Use thiserror with granular error types per operation:

// File operations have their own error type
#[derive(thiserror::Error, Debug)]
pub enum ReadError {
    #[error("failed to read {path}")]
    Io { path: PathBuf, #[source] source: std::io::Error },

    #[error("parse error at line {line}: {message}")]
    Parse { line: usize, message: String },
}

// Subprocess operations have their own error type
#[derive(thiserror::Error, Debug)]
pub enum SubprocessError {
    #[error("failed to spawn process")]
    Spawn(#[source] std::io::Error),

    #[error("process exited with {code:?}: {stderr}")]
    NonZeroExit { code: Option<i32>, stderr: String },

    #[error("output not valid UTF-8")]
    InvalidUtf8(#[source] std::str::Utf8Error),

    #[error("timed out after {0:?}")]
    Timeout(std::time::Duration),
}


Applications (internal/binary): Use anyhow for context-rich errors:

use anyhow::{Context, Result};

fn load_config(path: &Path) -> Result<Config> {
    let content = std::fs::read_to_string(path)
        .with_context(|| format!("failed to read config from {}", path.display()))?;
    // ...
}

Graceful Degradation

Errors degrade functionality, not crash. But log when being lenient:

match parse_metadata(&line) {
    Ok(meta) => entries.push(meta),
    Err(e) => {
        tracing::warn!("skipping malformed entry at line {}: {}", line_num, e);
        // Continue processing other entries
    }
}

Quick Reference
Do
Use std::sync::LazyLock for static regex (Rust 1.80+)
Hold locks across entire read-modify-write cycles
Add #[serde(deny_unknown_fields)] for strict external input
Truncate strings with .chars() or graphemes, not byte slicing
Write files atomically with sync_all() before rename
Verify PID identity with process start time
Use saturating_sub for time arithmetic
Run cargo clippy -- -D warnings and cargo fmt before commit
Don't
Use #[from] without adding context (loses which file failed)
Create monolithic error enums spanning unrelated operations
Silently ignore errors without logging
Slice strings with &s[..N] (panics on char boundaries)
Assume directory iteration order is stable
Trust subprocess output without validation
Use unsafe (not needed for these patterns)
Bugs This Guide Prevents
Bug	Pattern	Reference
PID reuse "ghost sessions"	Store + verify process start time	process-integration.md
Timestamp unit mismatch (sec vs ms)	Normalize on read	process-integration.md
UTF-8 panic on truncation	Use .chars().take(n)	text-and-parsing.md
Lost updates under concurrency	Lock spans full read-modify-write	file-io.md
Corrupt file on power loss	sync_all() before rename	file-io.md
Silent metadata corruption	Anchor updates to heading lines	text-and-parsing.md
Old data breaks new code	#[serde(default)] + alias	data-modeling.md
Change Checklist

When modifying these systems, verify:

Schema / Serde

 New fields use Option + #[serde(default)]
 Old field names supported via alias (read) or rename (write)
 External input uses #[serde(deny_unknown_fields)]

Concurrency

 Mutex held across entire read-modify-write cycle
 Shared state uses Mutex<T>, not thread_local!
 File locking documents platform caveats if used

Robustness

 No panics on file I/O or parse errors
 Errors logged before being ignored
 Subprocesses have timeouts

Quality

 cargo clippy -- -D warnings passes
 cargo fmt --check passes
 No unsafe blocks (unless justified and audited)
Weekly Installs
18
Repository
petekp/claude-code-setup
GitHub Stars
35
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass