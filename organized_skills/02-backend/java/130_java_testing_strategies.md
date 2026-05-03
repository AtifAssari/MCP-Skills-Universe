---
rating: ⭐⭐
title: 130-java-testing-strategies
url: https://skills.sh/jabrena/cursor-rules-java/130-java-testing-strategies
---

# 130-java-testing-strategies

skills/jabrena/cursor-rules-java/130-java-testing-strategies
130-java-testing-strategies
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 130-java-testing-strategies
SKILL.md
Java testing strategies

Apply proven testing strategies (RIGHT-BICEP, A-TRIP, CORRECT) to design and verify Java unit tests.

What is covered in this Skill?

RIGHT-BICEP: Key questions to guide test creation — Right results, Boundary conditions, Inverse relationships, Cross-checks, Error conditions, Performance
A-TRIP: Characteristics of good tests — Automatic, Thorough, Repeatable, Independent, Professional
CORRECT: Boundary condition verification — Conformance, Ordering, Range, Reference, Existence, Cardinality, Time
Constraints

Before applying any test strategy changes, ensure the project compiles. If compilation fails, stop immediately — do not proceed until resolved. After applying improvements, run full verification.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
SAFETY: If compilation fails, stop immediately and do not proceed — compilation failure is a blocking condition
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed examples, good/bad patterns, and constraints
EDGE CASE: If the user goal is ambiguous, stop and ask a clarifying question before editing files or running project-wide commands
EDGE CASE: If required context, files, credentials, or tools are missing, report the blocker explicitly and ask whether to proceed with setup or fallback guidance
EDGE CASE: If requested changes conflict with project constraints or safety boundaries, explain the conflict and ask for user confirmation on the preferred trade-off
When to use this skill
Review Java code for testing strategies
Apply RIGHT-BICEP testing strategies in Java code
Apply A-TRIP testing strategies in Java code
Apply CORRECT boundary condition verification in Java code
Workflow
Compile project before test-strategy changes

Run ./mvnw compile or mvn compile and stop immediately if compilation fails.

Read testing-strategies reference

Read references/130-java-testing-strategies.md and map current tests to RIGHT-BICEP, A-TRIP, and CORRECT gaps.

Apply strategy-driven test improvements

Improve or add tests to cover missing boundaries, quality characteristics, and verification depth.

Verify with full build

Run ./mvnw clean verify or mvn clean verify after applying improvements.

Reference

For detailed guidance, examples, and constraints, see references/130-java-testing-strategies.md.

Weekly Installs
60
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass