---
title: migrate-to-rstest
url: https://skills.sh/rstackjs/agent-skills/migrate-to-rstest
---

# migrate-to-rstest

skills/rstackjs/agent-skills/migrate-to-rstest
migrate-to-rstest
Installation
$ npx skills add https://github.com/rstackjs/agent-skills --skill migrate-to-rstest
SKILL.md
Migrate to Rstest
Goal

Migrate Jest- or Vitest-based tests and configuration to Rstest with minimal behavior changes.

Migration principles (must follow)
Smallest-change-first: prefer the smallest viable change that restores test pass.
Config before code: prefer fixing in config/tooling/mocks before touching test logic.
Do not change user source behavior: avoid modifying production/business source files unless user explicitly requests it.
Avoid bulk test rewrites: do not refactor entire test suites when a local compatibility patch can solve it.
Preserve test intent: keep assertions and scenario coverage unchanged unless clearly broken by framework differences.
Two-phase legacy-runner lifecycle (per migrated scope): (a) While the scope being migrated is not green on Rstest, keep every Jest/Vitest dep + config/setup/workspace file untouched — they are your rollback path. (b) Once that scope is green, delete its scope-local legacy config/setup files in the same commit. Drop the shared legacy devDeps (jest, vitest, adapters, environments) only when no other scope still relies on them — in a partial / mixed-mode monorepo migration that means the final scope, not the first. Leaving files behind "for reference" creates two source-of-truth configs. Framework-specific file enumeration: see the deltas reference.
Literal API substitution, no shims: rewrite every vi. / jest. / vitest. call site — no global aliasing, no local rebinding, no aliased imports. Full forbidden-form list and reasoning in references/global-api-migration.md.
Replace on call sites, not strings: match only identifiers preceding (; after every batch edit, grep describe\(|it\(|test\( to confirm no test name string was mutated. Regex template and rationale in references/global-api-migration.md.
Coverage thresholds are not negotiable: never lower coverage.thresholds (lines/functions/branches/statements) to make a migrated suite pass. If thresholds fail under Rstest, investigate coverage.include / exclude / provider wiring before touching the numbers.
Workflow
Detect current test framework (references/detect-test-framework.md)
Dependency install gate (blocker check, see references/dependency-install-gate.md)
Open the framework-specific deltas file and the official migration guide it points to. Prefer the .md URL form when fetching — Rstest pages provide Markdown variants that are more AI-friendly.
Jest: references/jest-migration-deltas.md
Vitest: references/vitest-migration-deltas.md
Global API replacement rules: references/global-api-migration.md
Apply the mapping from the official guide + the skill-side enforcement rules from the deltas file
Check type errors
Run tests and fix deltas
Apply cleanup phase of principle 6 once the migrated scope is green (delete scope-local legacy config/setup in the same commit; drop shared legacy devDeps only when no other scope still relies on them; framework-specific file list is in the deltas file)
Summarize changes
Detect current test framework

See references/detect-test-framework.md for detection signals and the mixed-mode scope policy.

Dependency install gate (blocker check)

Before large-scale edits, verify dependencies can be installed and test runner binaries are available. Detailed checks, blocked-mode output format, and ni policy are in references/dependency-install-gate.md.

Patch scope policy (strict)
Preferred change order
CLI/script/config migration (package.json, rstest.config.ts, include/exclude, test environment).
Test setup adapter migration (for example @testing-library/jest-dom/vitest to matcher-based setup in Rstest).
Mock compatibility adjustments (target module path, { mock: true }, importActual).
Narrow per-test setup fixes (single-file, single-suite level).
Path resolution compatibility fixes (import.meta.url vs __dirname) in test/setup helpers.
As a last resort, test body changes.
Never modify runtime source logic by default.
Red lines

Principles 6–9 above are themselves red lines — the bullets below cover the scope / intent red lines not captured there:

Do not rewrite many tests in one sweep without first proving config-level fixes are insufficient.
Do not alter business/runtime behavior to satisfy tests.
Do not change assertion semantics just to make tests pass.
Do not broaden migration to unrelated packages in a monorepo.
Escalation rule for large edits

If a fix would require either:

editing many test files, or
changing user source files,

stop and provide:

why minimal fixes failed,
proposed large-change options,
expected impact/risk per option,
recommended option.
Run tests and fix deltas
Run the test suite and fix failures iteratively.
Fix configuration and resolver errors first, then address mocks/timers/snapshots, and touch test logic last.
If mocks fail for re-exported modules under Rspack, first check whether the project is pinned to rstest < 0.9.3 (fixed in 0.9.3 — upgrade before debugging mock behavior further).
Summarize changes
Provide a concise change summary and list files touched.
Call out any remaining manual steps or TODOs.
Weekly Installs
135
Repository
rstackjs/agent-skills
GitHub Stars
65
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn