---
title: wtf.steer-qa
url: https://skills.sh/xiduzo/wtf/wtf.steer-qa
---

# wtf.steer-qa

skills/xiduzo/wtf/wtf.steer-qa
wtf.steer-qa
Installation
$ npx skills add https://github.com/xiduzo/wtf --skill wtf.steer-qa
SKILL.md
Steer QA

Generate or refine docs/steering/QA.md — the QA standards document. This document is the canonical reference for test strategy, coverage requirements, test patterns, and the definition of done that every implementer and QA engineer must follow.

The shared steering-doc flow (exists-check → research → interview → draft → review → write → wiki sync → continue) lives in ../references/steering-doc-process.md. Follow that process with the skill-specific inputs below. Apply ../references/questioning-style.md for every user question.

Doc path: docs/steering/QA.md
Template: references/qa-template.md
Display name / wiki page: WTF-QA.md
Commit message: docs: add QA standards steering document
Step 2 — Research checklist

Use the Agent tool to extract QA facts directly. Do not ask the user for things that can be read:

Test framework: test runner config (vitest.config.ts, jest.config.js, pytest.ini, etc.)
Test scripts: package.json scripts for test, test:watch, test:coverage
Coverage config: coverage thresholds in test config files
Test file conventions: where tests live, naming patterns (.test.ts, .spec.ts, _test.go, etc.)
Existing test types: are there unit, integration, and e2e tests? What tools?
CI config: .github/workflows/ — what test gates run on PRs?
CLAUDE.md: extract any testing rules already defined there
Known flaky areas: skip, xit, @pytest.mark.skip usage or TODO comments in tests

Also check docs/steering/TECH.md if it exists — extract testing-related constraints already documented there.

Produce a concrete draft of Test Strategy, Test Patterns, and Commands from research alone.

Step 3 — Gap-topic list

Ask only about items research could not determine:

Coverage thresholds — "What is the minimum acceptable test coverage?" Pre-fill with thresholds found in test config or CLAUDE.md.
Definition of Done — "What must be true before any task can be merged?" Pre-fill with DoD items from CLAUDE.md or existing task templates.
Test environments — "What environments are available for testing? (local, staging, CI)" Pre-fill from CI config or README.
Known flaky areas — "Are there known areas that produce non-deterministic test failures?" Pre-fill with skipped tests or TODO comments found in step 2.
Mock strategy — "Are there project-specific exceptions to the 'only mock at boundaries' rule?" Pre-fill with mock patterns found in existing tests.
Step 4 — Writing rules
Coverage thresholds are stated as enforced minimums, not targets.
Test commands must be exact and match what CI actually runs.
Definition of Done items are written as checkboxes — concrete and binary.
Known Flaky Areas is honest, not aspirational — flag real issues.
Step 8 — Continue options
{label: "Create VISION.md", description: "Run wtf.steer-vision to document the product vision"}
{label: "Create TECH.md", description: "Run wtf.steer-tech to document the technical guidelines"}
{label: "Create DESIGN.md", description: "Run wtf.steer-design to document the design guidelines"}
{label: "Stop here", description: "Exit — no further action"}
Weekly Installs
33
Repository
xiduzo/wtf
GitHub Stars
3
First Seen
Apr 9, 2026