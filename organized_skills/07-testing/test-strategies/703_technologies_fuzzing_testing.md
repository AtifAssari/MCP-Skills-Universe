---
rating: ⭐⭐
title: 703-technologies-fuzzing-testing
url: https://skills.sh/jabrena/cursor-rules-java/703-technologies-fuzzing-testing
---

# 703-technologies-fuzzing-testing

skills/jabrena/cursor-rules-java/703-technologies-fuzzing-testing
703-technologies-fuzzing-testing
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 703-technologies-fuzzing-testing
SKILL.md
Java fuzz testing with CATS

Design and implement contract-driven fuzz testing for Java APIs using CATS to uncover edge cases and input-validation defects early.

What is covered in this Skill?

CATS setup and baseline command usage for OpenAPI-driven fuzzing
Negative testing strategy for invalid payloads, missing fields, wrong types, and malformed values
Boundary testing for size, range, format, and enum constraints
CI integration patterns with actionable logs and reproducible failures
Local execution workflow for contributors before opening pull requests
Reporting and triage practices for fuzzing findings

Scope: Focus on HTTP API fuzzing and contract validation with CATS. Use this skill to define practical, repeatable checks in both local and CI workflows.

Constraints

Before applying any fuzz testing changes, ensure the project compiles. If compilation fails, stop immediately. After implementation, regenerate skills and run verification.

MANDATORY: Run ./mvnw compile or mvn compile before applying any change
SAFETY: If compilation fails, stop immediately and do not proceed
MANDATORY: Regenerate skills with ./mvnw clean install -pl skills-generator after editing skill XML
VERIFY: Run ./mvnw clean verify or mvn clean verify after applying improvements
BEFORE APPLYING: Read the reference for detailed examples, good/bad patterns, and constraints
EDGE CASE: If request scope is ambiguous, stop and ask a clarifying question before applying changes
EDGE CASE: If required inputs, files, or tooling are missing, report what is missing and ask whether to proceed with setup guidance
When to use this skill
Add fuzz testing to a Java project
Use CATS for API negative testing
Review CI quality gates for API contract robustness
Improve boundary and malformed input test coverage
Workflow
Read reference and assess project context

Read references/703-technologies-fuzzing-testing.md and inspect current API/context artifacts before proposing changes.

Gather scope and decide target improvements

Identify requested outcomes, constraints, and the minimum safe set of changes to apply.

Apply technology-aligned changes

Implement or refactor artifacts following the reference patterns and project conventions.

Run verification and report results

Execute appropriate checks and summarize what changed, what was verified, and any follow-up actions.

Reference

For detailed guidance, examples, and constraints, see references/703-technologies-fuzzing-testing.md.

Weekly Installs
28
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass