---
rating: ⭐⭐
title: 121-java-object-oriented-design
url: https://skills.sh/jabrena/cursor-rules-java/121-java-object-oriented-design
---

# 121-java-object-oriented-design

skills/jabrena/cursor-rules-java/121-java-object-oriented-design
121-java-object-oriented-design
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 121-java-object-oriented-design
SKILL.md
Java Object-Oriented Design Guidelines

Review and improve Java code using comprehensive object-oriented design guidelines and refactoring practices.

What is covered in this Skill?

Fundamental design principles (SOLID, DRY, YAGNI)
Class and interface design: composition over inheritance, immutability, accessibility minimization, accessor methods
Core OOP concepts: encapsulation, inheritance, polymorphism
Object creation patterns: static factory methods, Builder, Singleton, dependency injection, avoiding unnecessary objects
OOD code smells: God Class, Feature Envy, Inappropriate Intimacy, Refused Bequest, Shotgun Surgery, Data Clumps
Method design: parameter validation, defensive copies, careful signatures, empty collections over nulls, Optional usage
Exception handling: checked vs. runtime exceptions, standard exceptions, failure-capture messages, no silent ignoring

Scope: The reference is organized by examples (good/bad code patterns) for each core area. Apply recommendations based on applicable examples.

Constraints

Before applying any OOD changes, ensure the project compiles. If compilation fails, stop immediately — do not proceed until resolved. After applying improvements, run full verification.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
SAFETY: If compilation fails, stop immediately and do not proceed — compilation failure is a blocking condition
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed examples, good/bad patterns, and constraints
EDGE CASE: If request scope is ambiguous, stop and ask a clarifying question before applying changes
EDGE CASE: If required inputs, files, or tooling are missing, report what is missing and ask whether to proceed with setup guidance
When to use this skill
Review Java code for object-oriented design
Refactor Java code for object-oriented design
Improve Java code for object-oriented design
Fix OOP concept misuse in Java code
Identify and resolve code smells in Java code
Improve object creation patterns in Java code
Improve method design in Java code
Improve exception handling in Java code
Workflow
Compile project before OOD changes

Run ./mvnw compile or mvn compile and stop immediately if compilation fails.

Read OOD reference and assess code

Read references/121-java-object-oriented-design.md and identify applicable SOLID/OOP/code-smell improvements.

Apply focused refactorings

Implement the selected object-oriented design improvements while preserving behavior.

Verify with full build

Run ./mvnw clean verify or mvn clean verify after applying improvements.

Reference

For detailed guidance, examples, and constraints, see references/121-java-object-oriented-design.md.

Weekly Installs
86
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