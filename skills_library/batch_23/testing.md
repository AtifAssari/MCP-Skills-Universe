---
title: testing
url: https://skills.sh/epicenterhq/epicenter/testing
---

# testing

skills/epicenterhq/epicenter/testing
testing
Installation
$ npx skills add https://github.com/epicenterhq/epicenter --skill testing
SKILL.md
Test File Conventions
When to Apply This Skill

Use this pattern when you need to:

Write or refactor *.test.ts files in this codebase.
Structure tests with setup() functions instead of mutable beforeEach setup.
Split large test files into focused behavior/type/scenario files.
Enforce behavior-based test naming and clear failure intent.
Add or review negative type tests using @ts-expect-error.
References

Load these on demand based on what you're working on:

If working with negative type tests (@ts-expect-error, bun:test type strategy, no as any), read references/type-testing.md
If working with test setup architecture (setup() patterns, composable setup, beforeEach avoidance, shared schemas), read references/setup-pattern.md
If working with test organization structure (flat tests, describe() boundaries, helper-over-nesting), read references/test-structure.md

External reading:

Kent C. Dodds, "Avoid Nesting When You're Testing" — setup functions over beforeEach, flat tests
Kent C. Dodds, "AHA Testing" — avoid hasty abstractions in tests
Kent C. Dodds, Testing JavaScript — Test Object Factory Pattern
Matt Pocock, "How to test your types" — vitest expectTypeOf for type testing
Matt Pocock, shoehorn — partial mocks for test ergonomics

Related Skills: See services-layer for the service patterns being tested. See typescript for type testing conventions.

File-Level Doc Comments

Every .test.ts file MUST start with a JSDoc block explaining what is being tested and the key behaviors verified. This serves as documentation for the module's contract.

Structure
/**
 * [Module Name] Tests
 *
 * [1-3 sentences explaining what this file tests and why these tests matter.]
 *
 * Key behaviors:
 * - [Behavior 1]
 * - [Behavior 2]
 * - [Behavior 3]
 *
 * See also:
 * - `related-file.test.ts` for [related aspect]
 */

Good Example
/**
 * Cell-Level LWW CRDT Sync Tests
 *
 * Verifies cell-level LWW conflict resolution where each field
 * has its own timestamp. Unlike row-level LWW, concurrent edits to
 * DIFFERENT fields merge independently.
 *
 * Key behaviors:
 * - Concurrent edits to SAME field: latest timestamp wins
 * - Concurrent edits to DIFFERENT fields: BOTH preserved (merge)
 * - Delete removes all cells for a row
 */

Bad Example (Too Minimal)
// Tests for create-tables

Section Headers

For long test files (100+ lines), use comment headers to separate logical sections:

// ============================================================================
// MESSAGE_SYNC Tests
// ============================================================================

Multi-Aspect Test File Splitting

When a module has distinct behavioral aspects, split into focused test files rather than one monolithic file:

Pattern	Use Case
{module}.test.ts	Core CRUD behavior, happy paths, edge cases
{module}.types.test.ts	Type inference verification, negative type tests
{module}.{scenario}.test.ts	Specific scenarios (CRDT sync, offline, integration)
When to Split
File exceeds ~500 lines
Tests cover genuinely distinct concerns (CRUD vs sync vs types)
Different setup requirements per concern
When NOT to Split
Splitting would create files with fewer than 3 tests
All tests share the same setup and concern
Test Naming

Test descriptions MUST be behavior assertions, not vague descriptions. The name should tell you what broke when the test fails.

Rules
State what happens, not "should work" or "handles correctly"
Include the condition when testing edge cases
No filler words: "should", "correctly", "properly" add nothing
Good Names
test('upsert stores row and get retrieves it', () => { ... });
test('filter returns only published posts', () => { ... });
test('concurrent edits to different fields: both preserved', () => { ... });
test('delete vs update race: update wins (rightmost entry)', () => { ... });
test('observer fires once per transaction, not per operation', () => { ... });
test('get() throws for undefined tables with helpful message', () => { ... });

Bad Names
test('should work correctly', () => { ... });         // What works? What's correct?
test('should handle batch operations', () => { ... }); // Handle how?
test('basic test', () => { ... });                     // Says nothing
test('should create and retrieve rows correctly', () => { ... }); // Vague "correctly"

Pattern: {action} {outcome} [condition]
"upsert stores row and get retrieves it"
 ^^^^^^ ^^^^^^^^^^   ^^^ ^^^^^^^^^^^^^
 action  outcome    action  outcome

"observer fires once per transaction, not per operation"
 ^^^^^^^^ ^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 subject   outcome              condition

"get() returns not_found for non-existent rows"
 ^^^^^ ^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^
 action     outcome            condition

Weekly Installs
43
Repository
epicenterhq/epicenter
GitHub Stars
4.5K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass