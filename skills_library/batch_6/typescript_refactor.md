---
title: typescript-refactor
url: https://skills.sh/pproenca/dot-skills/typescript-refactor
---

# typescript-refactor

skills/pproenca/dot-skills/typescript-refactor
typescript-refactor
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill typescript-refactor
SKILL.md
TypeScript Refactor Best Practices

Comprehensive TypeScript refactoring and modernization guide designed for AI agents and LLMs. Contains 43 rules across 8 categories, prioritized by impact to guide automated refactoring, code review, and code generation.

When to Apply

Reference these guidelines when:

Refactoring TypeScript code for type safety and maintainability
Designing type architectures (discriminated unions, branded types, generics)
Narrowing types to eliminate unsafe as casts
Adopting modern TypeScript 4.x-5.x features (satisfies, using, const type parameters)
Optimizing compiler performance in large codebases
Implementing type-safe error handling patterns
Reviewing code for TypeScript quirks and pitfalls
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Type Architecture	CRITICAL	arch-
2	Type Narrowing & Guards	CRITICAL	narrow-
3	Modern TypeScript	HIGH	modern-
4	Generic Patterns	HIGH	generic-
5	Compiler Performance	MEDIUM-HIGH	compile-
6	Error Safety	MEDIUM	error-
7	Runtime Patterns	MEDIUM	perf-
8	Quirks & Pitfalls	LOW-MEDIUM	quirk-
Quick Reference
1. Type Architecture (CRITICAL)
arch-discriminated-unions — Use discriminated unions over string enums for exhaustive pattern matching
arch-branded-types — Use branded types for domain identifiers to prevent value mix-ups
arch-satisfies-over-annotation — Use satisfies for config objects to preserve literal types
arch-interfaces-over-intersections — Extend interfaces instead of intersecting types for better error messages
arch-const-assertion — Use as const for immutable literal inference
arch-readonly-by-default — Default to readonly types for function parameters and return values
arch-avoid-partial-abuse — Avoid Partial<T> abuse for builder patterns
2. Type Narrowing & Guards (CRITICAL)
narrow-custom-type-guards — Write custom type guards instead of type assertions
narrow-assertion-functions — Use assertion functions for precondition checks
narrow-exhaustive-switch — Enforce exhaustive switch with never
narrow-in-operator — Narrow with the in operator for interface unions
narrow-eliminate-as-casts — Eliminate as casts with proper narrowing chains
narrow-typeof-chains — Use typeof narrowing before property access
3. Modern TypeScript (HIGH)
modern-using-keyword — Use the using keyword for resource cleanup
modern-const-type-parameters — Use const type parameters for literal inference
modern-template-literal-types — Use template literal types for string patterns
modern-noinfer-utility — Use NoInfer to control type parameter inference
modern-accessor-keyword — Use accessor for auto-generated getters and setters
modern-verbatim-module-syntax — Enable verbatimModuleSyntax for explicit import types
4. Generic Patterns (HIGH)
generic-infer-over-annotate — Let TypeScript infer instead of explicit annotation
generic-constrain-dont-overconstrain — Constrain generics minimally
generic-avoid-distributive-surprises — Control distributive conditional types
generic-mapped-type-utilities — Build custom mapped types for repeated transformations
generic-return-type-inference — Preserve return type inference in generic functions
5. Compiler Performance (MEDIUM-HIGH)
compile-explicit-return-types — Add explicit return types to exported functions
compile-avoid-deep-recursion — Avoid deeply recursive type definitions
compile-project-references — Use project references for monorepo builds
compile-base-types-over-unions — Use base types instead of large union types
6. Error Safety (MEDIUM)
error-result-type — Use Result types instead of thrown exceptions
error-exhaustive-error-handling — Use exhaustive checks for typed error variants
error-typed-catch — Type catch clause variables as unknown
error-never-for-unreachable — Use never to mark unreachable code paths
error-discriminated-error-unions — Model domain errors as discriminated unions
7. Runtime Patterns (MEDIUM)
perf-union-literals-over-enums — Use union literals instead of enums
perf-avoid-delete-operator — Avoid the delete operator on objects
perf-object-freeze-const — Use Object.freeze with as const for true immutability
perf-object-keys-narrowing — Avoid Object.keys type widening
perf-map-set-over-object — Use Map and Set over plain objects for dynamic collections
8. Quirks & Pitfalls (LOW-MEDIUM)
quirk-excess-property-checks — Understand excess property checks on object literals
quirk-empty-object-type — Avoid the {} type — it means non-nullish
quirk-type-widening-let — Prevent type widening with let declarations
quirk-variance-annotations — Use variance annotations for generic interfaces
quirk-structural-typing-escapes — Guard against structural typing escape hatches
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions — Category structure and impact levels
Rule template — Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
266
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass