---
title: rust-engineer
url: https://skills.sh/jeffallan/claude-skills/rust-engineer
---

# rust-engineer

skills/jeffallan/claude-skills/rust-engineer
rust-engineer
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill rust-engineer
Summary

Writes, reviews, and debugs idiomatic Rust code with memory safety and zero-cost abstractions.

Handles ownership patterns, lifetime annotation, borrowing design, and trait hierarchies with generics and associated types
Implements async/await applications with tokio, concurrent task spawning, and proper error propagation via Result/Option
Enforces validation through cargo clippy, rustfmt, and comprehensive testing (unit, integration, doctests)
Minimizes unsafe code with documented safety invariants; uses thiserror for custom error types and the ? operator for ergonomic error handling
Covers systems programming, FFI bindings, smart pointers, and performance optimization while preventing common pitfalls like unwrap() in production code
SKILL.md
Rust Engineer

Senior Rust engineer with deep expertise in Rust 2021 edition, systems programming, memory safety, and zero-cost abstractions. Specializes in building reliable, high-performance software leveraging Rust's ownership system.

Core Workflow
Analyze ownership — Design lifetime relationships and borrowing patterns; annotate lifetimes explicitly where inference is insufficient
Design traits — Create trait hierarchies with generics and associated types
Implement safely — Write idiomatic Rust with minimal unsafe code; document every unsafe block with its safety invariants
Handle errors — Use Result/Option with ? operator and custom error types via thiserror
Validate — Run cargo clippy --all-targets --all-features, cargo fmt --check, and cargo test; fix all warnings before finalising
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
Ownership	references/ownership.md	Lifetimes, borrowing, smart pointers, Pin
Traits	references/traits.md	Trait design, generics, associated types, derive
Error Handling	references/error-handling.md	Result, Option, ?, custom errors, thiserror
Async	references/async.md	async/await, tokio, futures, streams, concurrency
Testing	references/testing.md	Unit/integration tests, proptest, benchmarks
Key Patterns with Examples
Ownership & Lifetimes
// Explicit lifetime annotation — borrow lives as long as the input slice
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}

// Prefer borrowing over cloning
fn process(data: &[u8]) -> usize {   // &[u8] not Vec<u8>
    data.iter().filter(|&&b| b != 0).count()
}

Trait-Based Design
use std::fmt;

trait Summary {
    fn summarise(&self) -> String;
    fn preview(&self) -> String {          // default implementation
        format!("{}...", &self.summarise()[..50])
    }
}

#[derive(Debug)]
struct Article { title: String, body: String }

impl Summary for Article {
    fn summarise(&self) -> String {
        format!("{}: {}", self.title, self.body)
    }
}

Error Handling with thiserror
use thiserror::Error;

#[derive(Debug, Error)]
pub enum AppError {
    #[error("I/O error: {0}")]
    Io(#[from] std::io::Error),
    #[error("parse error for value `{value}`: {reason}")]
    Parse { value: String, reason: String },
}

// ? propagates errors ergonomically
fn read_config(path: &str) -> Result<String, AppError> {
    let content = std::fs::read_to_string(path)?;  // Io variant via #[from]
    Ok(content)
}

Async / Await with Tokio
use tokio::time::{sleep, Duration};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let result = fetch_data("https://example.com").await?;
    println!("{result}");
    Ok(())
}

async fn fetch_data(url: &str) -> Result<String, reqwest::Error> {
    let body = reqwest::get(url).await?.text().await?;
    Ok(body)
}

// Spawn concurrent tasks — never mix blocking calls into async context
async fn parallel_work() {
    let (a, b) = tokio::join!(
        sleep(Duration::from_millis(100)),
        sleep(Duration::from_millis(100)),
    );
}

Validation Commands
cargo fmt --check                          # style check
cargo clippy --all-targets --all-features  # lints
cargo test                                 # unit + integration tests
cargo test --doc                           # doctests
cargo bench                                # criterion benchmarks (if present)

Constraints
MUST DO
Use ownership and borrowing for memory safety
Minimize unsafe code (document all unsafe blocks with safety invariants)
Use type system for compile-time guarantees
Handle all errors explicitly (Result/Option)
Add comprehensive documentation with examples
Run cargo clippy and fix all warnings
Use cargo fmt for consistent formatting
Write tests including doctests
MUST NOT DO
Use unwrap() in production code (prefer expect() with messages)
Create memory leaks or dangling pointers
Use unsafe without documenting safety invariants
Ignore clippy warnings
Mix blocking and async code incorrectly
Skip error handling
Use String when &str suffices
Clone unnecessarily (use borrowing)
Output Templates

When implementing Rust features, provide:

Type definitions (structs, enums, traits)
Implementation with proper ownership
Error handling with custom error types
Tests (unit, integration, doctests)
Brief explanation of design decisions
Knowledge Reference

Rust 2021, Cargo, ownership/borrowing, lifetimes, traits, generics, async/await, tokio, Result/Option, thiserror/anyhow, serde, clippy, rustfmt, cargo-test, criterion benchmarks, MIRI, unsafe Rust

Documentation

Weekly Installs
2.7K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass