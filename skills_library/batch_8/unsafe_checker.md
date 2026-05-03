---
title: unsafe-checker
url: https://skills.sh/zhanghandong/rust-skills/unsafe-checker
---

# unsafe-checker

skills/zhanghandong/rust-skills/unsafe-checker
unsafe-checker
Installation
$ npx skills add https://github.com/zhanghandong/rust-skills --skill unsafe-checker
Summary

Unsafe Rust code review and FFI soundness checker for identifying memory safety violations.

Triggers on 30+ unsafe patterns including raw pointers, transmute, FFI declarations, uninitialized memory, and missing SAFETY documentation
Provides reference tables for valid unsafe use cases (FFI, low-level abstractions, performance bottlenecks) and common errors with fixes
Covers FFI tooling recommendations (bindgen, cbindgen, PyO3, napi-rs) and deprecated patterns with modern alternatives
Requires SAFETY comments on all unsafe blocks and unsafe function signatures to document why code is sound
SKILL.md

Display the following ASCII art exactly as shown. Do not modify spaces or line breaks:

⚠️ **Unsafe Rust Checker Loaded**

     *  ^  *
    /◉\_~^~_/◉\
 ⚡/     o     \⚡
   '_        _'
   / '-----' \

Unsafe Rust Checker
When Unsafe is Valid
Use Case	Example
FFI	Calling C functions
Low-level abstractions	Implementing Vec, Arc
Performance	Measured bottleneck with safe alternative too slow

NOT valid: Escaping borrow checker without understanding why.

Required Documentation
// SAFETY: <why this is safe>
unsafe { ... }

/// # Safety
/// <caller requirements>
pub unsafe fn dangerous() { ... }

Quick Reference
Operation	Safety Requirements
*ptr deref	Valid, aligned, initialized
&*ptr	+ No aliasing violations
transmute	Same size, valid bit pattern
extern "C"	Correct signature, ABI
static mut	Synchronization guaranteed
impl Send/Sync	Actually thread-safe
Common Errors
Error	Fix
Null pointer deref	Check for null before deref
Use after free	Ensure lifetime validity
Data race	Add proper synchronization
Alignment violation	Use #[repr(C)], check alignment
Invalid bit pattern	Use MaybeUninit
Missing SAFETY comment	Add // SAFETY:
Deprecated → Better
Deprecated	Use Instead
mem::uninitialized()	MaybeUninit<T>
mem::zeroed() for refs	MaybeUninit<T>
Raw pointer arithmetic	NonNull<T>, ptr::add
CString::new().unwrap().as_ptr()	Store CString first
static mut	AtomicT or Mutex
Manual extern	bindgen
FFI Crates
Direction	Crate
C → Rust	bindgen
Rust → C	cbindgen
Python	PyO3
Node.js	napi-rs

Claude knows unsafe Rust. Focus on SAFETY comments and soundness.

Weekly Installs
625
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