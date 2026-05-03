---
title: symfony:functional-tests
url: https://skills.sh/makfly/superpowers-symfony/symfony:functional-tests
---

# symfony:functional-tests

skills/makfly/superpowers-symfony/symfony:functional-tests
symfony:functional-tests
Installation
$ npx skills add https://github.com/makfly/superpowers-symfony --skill symfony:functional-tests
SKILL.md
Functional Tests (Symfony)
Use when
Building regression-safe behavior with TDD/functional/e2e tests.
Converting bug reports into executable failing tests.
Default workflow
Write failing test for target behavior and one boundary case.
Implement minimal code to pass.
Refactor while preserving green suite.
Broaden coverage for invalid/unauthorized/not-found paths.
Guardrails
Prefer deterministic fixtures/builders.
Assert observable behavior, not internal implementation.
Keep tests isolated and stable in CI.
Progressive disclosure
Use this file for execution posture and risk controls.
Open references when deep implementation details are needed.
Output contract
RED/GREEN/REFACTOR trace.
Test files changed and executed commands.
Coverage and confidence notes.
References
reference.md
docs/complexity-tiers.md
Weekly Installs
253
Repository
makfly/superpow…-symfony
GitHub Stars
128
First Seen
Jan 23, 2026