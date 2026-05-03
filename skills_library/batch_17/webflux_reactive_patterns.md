---
title: webflux-reactive-patterns
url: https://skills.sh/jheisonmb/skills/webflux-reactive-patterns
---

# webflux-reactive-patterns

skills/jheisonmb/skills/webflux-reactive-patterns
webflux-reactive-patterns
Installation
$ npx skills add https://github.com/jheisonmb/skills --skill webflux-reactive-patterns
SKILL.md
WebFlux Reactive Patterns

This skill provides comprehensive guidance for writing idiomatic, production-ready reactive code with Spring WebFlux in Java. It enforces pure reactive programming patterns and eliminates common anti-patterns that break reactive streams.

When to Use This Skill

Activate this skill when:

Developing or refactoring Spring WebFlux applications
Working with Mono and Flux reactive types
Implementing reactive REST APIs or microservices
Converting imperative code to reactive patterns
Reviewing reactive code for anti-patterns
Handling asynchronous operations in Java
Core Principles
1. Analysis Before Implementation

Before writing any code, analyze existing code, define an implementation plan, ask clarifying questions, and make explicit design decisions. See references/BEFORE_CODING.md for the complete workflow.

2. Pure Reactive Flow

Never use imperative constructs (if, throw, nested operations). Replace with reactive operators (filter, flatMap, switchIfEmpty, Mono.error()). All errors must be lazy using Mono.defer(). See references/REACTIVE_PATTERNS.md for detailed patterns.

3. No Literals

Never use string or number literals in code. Use constants for all values and enums for error messages. This ensures maintainability and type safety.

4. Helper Methods

Extract complex operations into single-responsibility helper methods. Main methods should read as high-level reactive flows. Includes builders, validations, and collection searches.

5. Parallel Operations

Use Mono.zip() for independent parallel validations. Use Flux.merge() for independent parallel operations. Never serialize what can run in parallel.

6. Clean Imports and Types

Always use short imported names, never fully qualified class names. Organize imports: Java standard library → external libraries → project classes. Let the compiler infer types when obvious.

Quick Reference

Common Anti-Patterns to Avoid:

❌ if (condition) { ... } else { ... } → ✅ Use filter(), switchIfEmpty()
❌ throw new Exception() → ✅ Use Mono.defer(() -> Mono.error())
❌ .then(Mono.just(x)) mid-flow → ✅ Breaks fail-fast, restructure flow
❌ Nested flatMap chains → ✅ Extract to helper methods
❌ Mono<Void> mid-flow → ✅ Only at final return
❌ String literals → ✅ Use constants or enums

Essential Patterns:

// Lazy error handling (mandatory pattern)
return Optional.ofNullable(data)
    .filter(d -> !d.isEmpty())
    .map(Mono::just)
    .orElse(Mono.defer(() -> Mono.error(BusinessType.EMPTY_DATA.build())));

// Repository with fallback
return repository.findById(id)
    .switchIfEmpty(Mono.defer(() -> Mono.error(BusinessType.NOT_FOUND.build(id))));

// Parallel validations
return Mono.zip(
    validateField1(data),
    validateField2(data),
    validateField3(data)
).then(Mono.just(data));

Detailed Documentation

For comprehensive guidance, refer to these resources:

references/BEFORE_CODING.md - Pre-implementation analysis workflow and planning checklist
references/REACTIVE_PATTERNS.md - Complete reactive patterns, anti-patterns, and transformations
references/BEST_PRACTICES.md - Code style, imports, constants, and organizational rules
references/TROUBLESHOOTING.md - Common issues, debugging techniques, and solutions
assets/reactive-service-example.java - Working example demonstrating all key patterns
Operator Selection Guide

Use this decision tree to select the right operator:

Is the operation synchronous (no I/O, no async calls)?

Yes → Use map()
No → Continue

Does it return Mono/Flux?

Yes → Use flatMap()
No → Use map()

Need to filter elements?

Use filter() + switchIfEmpty()

Need to handle empty streams?

Use switchIfEmpty()

Need to run operations in parallel?

Independent Monos → Mono.zip()
Independent Fluxes → Flux.merge()

Need to aggregate Flux to collection?

Use collect() or collectList()

Need lazy evaluation (especially errors)?

Use Mono.defer()
Quick Reference
map() - Synchronous transformations (1:1)
flatMap() - Asynchronous operations returning Mono/Flux (1:1)
filter() - Conditional filtering based on predicates
switchIfEmpty() - Fallback when stream is empty
zip() - Combine multiple independent Monos in parallel
merge() - Combine multiple Fluxes, emitting as they arrive
collect() - Aggregate Flux elements into collections
defer() - Lazy evaluation (critical for error handling)
Error Handling Philosophy

All errors must be lazy to maintain reactive semantics. Never use throw directly in reactive chains. Always wrap errors in Mono.defer() to ensure they're only evaluated when subscribed.

Why lazy errors matter:

Preserves fail-fast behavior in reactive chains
Allows proper error propagation through operators
Enables retry and fallback strategies
Maintains backpressure semantics
Quick Troubleshooting

For common reactive programming issues and solutions, refer to the Troubleshooting Guide.

If you need to extend this skill with additional patterns or examples, please maintain the workflow-based organization and ensure all code examples are minimal and focused on demonstrating specific patterns.

Weekly Installs
17
Repository
jheisonmb/skills
GitHub Stars
4
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass