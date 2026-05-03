---
title: incremental-tdd
url: https://skills.sh/kambleakash0/agent-skills/incremental-tdd
---

# incremental-tdd

skills/kambleakash0/agent-skills/incremental-tdd
incremental-tdd
Installation
$ npx skills add https://github.com/kambleakash0/agent-skills --skill incremental-tdd
SKILL.md
Test-Driven Development (Red-Green-Refactor)

This skill forces you to work in tight TDD loops: one failing test, one implementation, then refactor. It prefers vertical slices and deep modules so tests stay honest, stable, and focused on real behavior instead of implementation details.

This skill comes with extra documents you can reference for philosophy and examples:

deep-modules.md – why deep modules make AI‑driven TDD easier and safer.
refactoring.md – patterns for safe refactors.
interface-design.md – how to design interfaces for TDD.
mocking.md – how and when to mock without lying to yourself.
tests.md – how and when to mock without lying to yourself.

When you need guidance on design or refactoring, open and read these files instead of guessing.

When to Use

Use this skill when the user:

Wants to build a feature or fix a bug using TDD.
Mentions “red‑green‑refactor”, “test‑first”, or “write the tests first”.
Wants honest integration or module‑level tests that drive design rather than brittle unit tests.
Is running longer “Ralph” loops or autonomous agents and wants higher‑quality changes.

If the requirements are unclear, suggest using /grill-me and /spec-writer first, then come back here for execution.

Overall Workflow

You can compress steps when context is obvious, but keep the red → green → refactor discipline.

Clarify behavior and interfaces

Confirm what behavior should exist from the outside: which inputs, outputs, and observable effects matter.
Identify or design the interfaces you’ll use to expose that behavior (public functions, handlers, endpoints, etc.).
Prefer deep modules: fewer, larger modules with thin, stable interfaces on top.
If needed, open deep-modules.md and adjust your interface design to match that philosophy.

Choose the next vertical slice

From the PRD or problem description, pick a thin vertical slice: a single behavior that exercises a real path through the system.
Avoid purely horizontal slices like “set up the DB table” or “write all the UI” in isolation.
Confirm with the user (or with comments) what this slice should prove when finished.

Red: write one failing test

Write one test that expresses the desired behavior of the slice using the chosen interface.
Keep the test as close as possible to “how a real caller would use this”, even when testing at module level.
Prefer real collaborators or thin fakes over heavy mocking. When in doubt, consult mocking.md.
Run the test and confirm it fails for the expected reason.

Green: write the minimal implementation

Open the relevant production files and write the simplest implementation that makes the test pass.
Do not over‑generalize, add unused parameters, or implement future behavior that isn’t tested yet.
Re‑run the tests and make sure the new test passes and the suite remains green.

Refactor: improve design safely

With tests green, look for duplication, awkward interfaces, or leaky abstractions.
Apply small refactors while running tests frequently to ensure behavior stays the same.
Use deep-modules.md and refactoring.md as guides for better boundaries and deeper modules.
Stop once the design is “good enough” for now; you can refactor again after future slices.

Repeat the loop

Pick the next slice or behavior, then repeat Red → Green → Refactor.
Each cycle should be small enough that you can understand and reverse it if it goes wrong.
As you go, keep tests focused on behavior and avoid coupling them to incidental implementation details.
Behavior and Rules
Always respect the loop. Never write large chunks of production code without a failing test first.
One test at a time. Do not generate dozens of tests at once. Add tests incrementally as behavior demands.
Prefer higher‑level tests. Where reasonable, prefer integration or module‑level tests that exercise real flows.
Guard against dishonest tests. Avoid tests that would pass even if the real behavior were broken; check for obvious false positives.
Be willing to change your own code. Treat previously written code as disposable if a better design emerges; rely on tests for safety.
Use the attached docs. When you’re unsure about module shape, refactoring, or mocking, open the linked markdown files instead of hallucinating patterns.
Example Flow

User: “Implement weekly admin summary emails using TDD. I already have the PRD and issues.”

You (high level):

Skim the PRD and issues, identify the first vertical slice (e.g., “compute weekly metrics for a single team”).
Design or confirm the module interface responsible for computing metrics; check deep-modules.md for guidance.
Write a single failing test for “given last week’s events, compute the summary object for team X”.
Implement the minimal code to make that test pass, then refactor the module while keeping tests green.
Repeat for additional behaviors (multiple teams, filters, performance constraints, error handling), always via red‑green‑refactor.
Weekly Installs
12
Repository
kambleakash0/ag…t-skills
GitHub Stars
6
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass