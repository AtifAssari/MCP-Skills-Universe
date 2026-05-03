---
title: domain-embedded
url: https://skills.sh/zhanghandong/rust-skills/domain-embedded
---

# domain-embedded

skills/zhanghandong/rust-skills/domain-embedded
domain-embedded
Installation
$ npx skills add https://github.com/zhanghandong/rust-skills --skill domain-embedded
Summary

Embedded and no_std Rust development constraints, patterns, and critical safety rules for microcontroller firmware.

Enforces no dynamic allocation (heap-free design using heapless collections), no_std compilation, and static memory buffers for deterministic resource usage on resource-constrained devices
Covers interrupt safety through critical sections and Mutex<RefCell> patterns to prevent race conditions when shared state is accessed from ISRs
Provides hardware ownership patterns (singleton peripherals, HAL-based access) to prevent conflicting peripheral access and unsafe register manipulation
Includes framework guidance for RTIC (priority-based), Embassy (async), and bare-metal approaches, plus key crates (cortex-m-rt, heapless, embedded-hal, defmt, probe-run)
Documents common mistakes (Vec instead of heapless::Vec, missing critical sections, blocking in ISRs) with fixes tied to design patterns
SKILL.md
Contains Shell Commands

This skill contains shell command directives (!`command`) that may execute system commands. Review carefully before installing.

Project Context (Auto-Injected)

Target configuration: !cat .cargo/config.toml 2>/dev/null || echo "No .cargo/config.toml found"

Embedded Domain

Layer 3: Domain Constraints

Domain Constraints → Design Implications
Domain Rule	Design Constraint	Rust Implication
No heap	Stack allocation	heapless, no Box/Vec
No std	Core only	#![no_std]
Real-time	Predictable timing	No dynamic alloc
Resource limited	Minimal memory	Static buffers
Hardware safety	Safe peripheral access	HAL + ownership
Interrupt safe	No blocking in ISR	Atomic, critical sections
Critical Constraints
No Dynamic Allocation
RULE: Cannot use heap (no allocator)
WHY: Deterministic memory, no OOM
RUST: heapless::Vec<T, N>, arrays

Interrupt Safety
RULE: Shared state must be interrupt-safe
WHY: ISR can preempt at any time
RUST: Mutex<RefCell<T>> + critical section

Hardware Ownership
RULE: Peripherals must have clear ownership
WHY: Prevent conflicting access
RUST: HAL takes ownership, singletons

Trace Down ↓

From constraints to design (Layer 2):

"Need no_std compatible data structures"
    ↓ m02-resource: heapless collections
    ↓ Static sizing: heapless::Vec<T, N>

"Need interrupt-safe state"
    ↓ m03-mutability: Mutex<RefCell<Option<T>>>
    ↓ m07-concurrency: Critical sections

"Need peripheral ownership"
    ↓ m01-ownership: Singleton pattern
    ↓ m12-lifecycle: RAII for hardware

Layer Stack
Layer	Examples	Purpose
PAC	stm32f4, esp32c3	Register access
HAL	stm32f4xx-hal	Hardware abstraction
Framework	RTIC, Embassy	Concurrency
Traits	embedded-hal	Portable drivers
Framework Comparison
Framework	Style	Best For
RTIC	Priority-based	Interrupt-driven apps
Embassy	Async	Complex state machines
Bare metal	Manual	Simple apps
Key Crates
Purpose	Crate
Runtime (ARM)	cortex-m-rt
Panic handler	panic-halt, panic-probe
Collections	heapless
HAL traits	embedded-hal
Logging	defmt
Flash/debug	probe-run
Design Patterns
Pattern	Purpose	Implementation
no_std setup	Bare metal	#![no_std] + #![no_main]
Entry point	Startup	#[entry] or embassy
Static state	ISR access	Mutex<RefCell<Option<T>>>
Fixed buffers	No heap	heapless::Vec<T, N>
Code Pattern: Static Peripheral
#![no_std]
#![no_main]

use cortex_m::interrupt::{self, Mutex};
use core::cell::RefCell;

static LED: Mutex<RefCell<Option<Led>>> = Mutex::new(RefCell::new(None));

#[entry]
fn main() -> ! {
    let dp = pac::Peripherals::take().unwrap();
    let led = Led::new(dp.GPIOA);

    interrupt::free(|cs| {
        LED.borrow(cs).replace(Some(led));
    });

    loop {
        interrupt::free(|cs| {
            if let Some(led) = LED.borrow(cs).borrow_mut().as_mut() {
                led.toggle();
            }
        });
    }
}

Common Mistakes
Mistake	Domain Violation	Fix
Using Vec	Heap allocation	heapless::Vec
No critical section	Race with ISR	Mutex + interrupt::free
Blocking in ISR	Missed interrupts	Defer to main loop
Unsafe peripheral	Hardware conflict	HAL ownership
Trace to Layer 1
Constraint	Layer 2 Pattern	Layer 1 Implementation
No heap	Static collections	heapless::Vec<T, N>
ISR safety	Critical sections	Mutex<RefCell>
Hardware ownership	Singleton	take().unwrap()
no_std	Core-only	#![no_std], #![no_main]
Related Skills
When	See
Static memory	m02-resource
Interior mutability	m03-mutability
Interrupt patterns	m07-concurrency
Unsafe for hardware	unsafe-checker
Weekly Installs
518
Repository
zhanghandong/rust-skills
GitHub Stars
1.1K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass