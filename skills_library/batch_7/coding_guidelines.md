---
title: coding-guidelines
url: https://skills.sh/zhanghandong/rust-skills/coding-guidelines
---

# coding-guidelines

skills/zhanghandong/rust-skills/coding-guidelines
coding-guidelines
Installation
$ npx skills add https://github.com/zhanghandong/rust-skills --skill coding-guidelines
Summary

Rust naming, formatting, and best-practice guidelines covering 50 core rules.

Covers naming conventions (no get_ prefix, iterator patterns, conversion methods), data types (newtypes, slice patterns, pre-allocation), and string handling (prefer bytes for ASCII, use Cow<str> when appropriate)
Error handling guidance includes ? propagation over try!(), meaningful lifetime names, and lock ordering for concurrency safety
Includes deprecation mappings (e.g., lazy_static! to OnceLock, failure to thiserror) and quick reference for formatting, documentation, and linting standards
Designed as a reference for code review and style decisions in Rust projects
SKILL.md
Rust Coding Guidelines (50 Core Rules)
Naming (Rust-Specific)
Rule	Guideline
No get_ prefix	fn name() not fn get_name()
Iterator convention	iter() / iter_mut() / into_iter()
Conversion naming	as_ (cheap &), to_ (expensive), into_ (ownership)
Static var prefix	G_CONFIG for static, no prefix for const
Data Types
Rule	Guideline
Use newtypes	struct Email(String) for domain semantics
Prefer slice patterns	if let [first, .., last] = slice
Pre-allocate	Vec::with_capacity(), String::with_capacity()
Avoid Vec abuse	Use arrays for fixed sizes
Strings
Rule	Guideline
Prefer bytes	s.bytes() over s.chars() when ASCII
Use Cow<str>	When might modify borrowed data
Use format!	Over string concatenation with +
Avoid nested iteration	contains() on string is O(n*m)
Error Handling
Rule	Guideline
Use ? propagation	Not try!() macro
expect() over unwrap()	When value guaranteed
Assertions for invariants	assert! at function entry
Memory
Rule	Guideline
Meaningful lifetimes	'src, 'ctx not just 'a
try_borrow() for RefCell	Avoid panic
Shadowing for transformation	let x = x.parse()?
Concurrency
Rule	Guideline
Identify lock ordering	Prevent deadlocks
Atomics for primitives	Not Mutex for bool/usize
Choose memory order carefully	Relaxed/Acquire/Release/SeqCst
Async
Rule	Guideline
Sync for CPU-bound	Async is for I/O
Don't hold locks across await	Use scoped guards
Macros
Rule	Guideline
Avoid unless necessary	Prefer functions/generics
Follow Rust syntax	Macro input should look like Rust
Deprecated → Better
Deprecated	Better	Since
lazy_static!	std::sync::OnceLock	1.70
once_cell::Lazy	std::sync::LazyLock	1.80
std::sync::mpsc	crossbeam::channel	-
std::sync::Mutex	parking_lot::Mutex	-
failure/error-chain	thiserror/anyhow	-
try!()	? operator	2018
Quick Reference
Naming: snake_case (fn/var), CamelCase (type), SCREAMING_CASE (const)
Format: rustfmt (just use it)
Docs: /// for public items, //! for module docs
Lint: #![warn(clippy::all)]


Claude knows Rust conventions well. These are the non-obvious Rust-specific rules.

Weekly Installs
1.1K
Repository
zhanghandong/rust-skills
GitHub Stars
1.1K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass