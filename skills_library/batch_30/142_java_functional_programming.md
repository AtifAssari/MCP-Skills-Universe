---
title: 142-java-functional-programming
url: https://skills.sh/jabrena/cursor-rules-java/142-java-functional-programming
---

# 142-java-functional-programming

skills/jabrena/cursor-rules-java/142-java-functional-programming
142-java-functional-programming
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 142-java-functional-programming
SKILL.md
Java Functional Programming rules

Identify and apply functional programming principles in Java to improve immutability, expressiveness, and maintainability.

What is covered in this Skill?

Immutable objects and Records (JEP 395)
Pure functions free of side effects
Functional interfaces: Function, Predicate, Consumer, Supplier, custom @FunctionalInterface
Lambda expressions and method references
Stream API: filter/map/reduce pipelines, parallel streams, toUnmodifiable* collectors
Optional idiomatic usage: map/flatMap/filter/orElse* over isPresent()+get()
Function composition: andThen/compose
Higher-order functions: memoization, currying, partial application
Pattern Matching for instanceof and switch (Java 21)
Sealed classes and interfaces (Java 17) for exhaustive domain hierarchies
Switch Expressions (Java 14), Stream Gatherers (JEP 461)
Effect-boundary separation: side effects at edges, pure core logic
Immutable collections: List.of(), Collectors.toUnmodifiableList()

Scope: The reference is organized by examples (good/bad code patterns) for each core area. Apply recommendations based on applicable examples.

Constraints

Before applying any functional programming changes, ensure the project compiles. If compilation fails, stop immediately — do not proceed until the project compiles successfully. Verify that maven-compiler-plugin source/target supports the Java features being used.

MANDATORY: Run ./mvnw compile or mvn compile before applying any changes
SAFETY: If compilation fails, stop immediately — do not proceed until the project compiles successfully
VERIFY: Verify maven-compiler-plugin source/target supports the Java features being used
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed good/bad examples, constraints, and safeguards for each functional programming pattern
EDGE CASE: If request scope is ambiguous, stop and ask a clarifying question before applying changes
EDGE CASE: If required inputs, files, or tooling are missing, report what is missing and ask whether to proceed with setup guidance
When to use this skill
Improve the code with Functional Programming
Apply Functional Programming
Refactor the code with Functional Programming
Workflow
Compile project before functional refactoring

Run ./mvnw compile or mvn compile and stop immediately if compilation fails.

Confirm Java feature compatibility

Verify maven-compiler-plugin source/target supports the functional features planned for adoption.

Read functional-programming reference and assess code

Read references/142-java-functional-programming.md and identify opportunities for immutability, pure functions, and functional composition.

Apply functional programming improvements

Implement selected functional refactorings while keeping side effects at boundaries.

Verify with full build

Run ./mvnw clean verify or mvn clean verify after applying improvements.

Reference

For detailed guidance, examples, and constraints, see references/142-java-functional-programming.md.

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