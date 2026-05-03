---
rating: ⭐⭐
title: 128-java-generics
url: https://skills.sh/jabrena/cursor-rules-java/128-java-generics
---

# 128-java-generics

skills/jabrena/cursor-rules-java/128-java-generics
128-java-generics
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 128-java-generics
SKILL.md
Java Generics Best Practices

Review and improve Java code using comprehensive generics best practices that enforce compile-time type safety and enable flexible, reusable APIs.

What is covered in this Skill?

Type safety: avoiding raw types, eliminating unsafe casts
Code reusability: generic methods and types for multiple type contexts
PECS wildcards: ? extends for producers, ? super for consumers
Diamond operator for type inference
Type erasure awareness: type tokens, factory patterns, array creation
Generic inheritance and variance: invariance, covariance, contravariance
@SafeVarargs for heap pollution prevention
Wildcard capture helpers, self-bounded generics (CRTP) for fluent builders
Proper wildcard API design: Comparator<? super T>, Function<? super T, ? extends R>
Arrays-vs-generics covariance pitfalls, serialization with TypeReference/TypeToken
Generic naming conventions (T, E, K/V, ?), typesafe heterogeneous containers
Integration with Records, sealed types, and pattern matching

Scope: The reference is organized by examples (good/bad code patterns) for each core area. Apply recommendations based on applicable examples.

Constraints

Before applying any generics changes, ensure the project compiles. If compilation fails, stop immediately — do not proceed until resolved. After applying improvements, run full verification.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
SAFETY: If compilation fails, stop immediately and do not proceed — compilation failure is a blocking condition
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed examples, good/bad patterns, and constraints
EDGE CASE: If request scope is ambiguous, stop and ask a clarifying question before applying changes
EDGE CASE: If required inputs, files, or tooling are missing, report what is missing and ask whether to proceed with setup guidance
When to use this skill
Improve the code with Generics
Apply Generics
Refactor the code with Generics
Workflow
Compile project before generics changes

Run ./mvnw compile or mvn compile and stop immediately if compilation fails.

Read generics reference and assess type safety

Read references/128-java-generics.md and identify raw types, unsafe casts, wildcard misuse, and API variance opportunities.

Apply generics refactorings

Implement selected generic type and API improvements while preserving behavior.

Verify with full build

Run ./mvnw clean verify or mvn clean verify after applying improvements.

Reference

For detailed guidance, examples, and constraints, see references/128-java-generics.md.

Weekly Installs
82
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
Mar 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass