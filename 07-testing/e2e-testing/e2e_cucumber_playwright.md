---
rating: ⭐⭐
title: e2e-cucumber-playwright
url: https://skills.sh/langgenius/dify/e2e-cucumber-playwright
---

# e2e-cucumber-playwright

skills/langgenius/dify/e2e-cucumber-playwright
e2e-cucumber-playwright
Installation
$ npx skills add https://github.com/langgenius/dify --skill e2e-cucumber-playwright
SKILL.md
Dify E2E Cucumber + Playwright

Use this skill for Dify's repository-level E2E suite in e2e/. Use e2e/AGENTS.md as the canonical guide for local architecture and conventions, then apply Playwright/Cucumber best practices only where they fit the current suite.

Scope
Use this skill for .feature files, Cucumber step definitions, DifyWorld, hooks, tags, and E2E review work under e2e/.
Do not use this skill for Vitest or React Testing Library work under web/; use frontend-testing instead.
Do not use this skill for backend test or API review tasks under api/.
Read Order
Read e2e/AGENTS.md first.
Read only the files directly involved in the task:
target .feature files under e2e/features/
related step files under e2e/features/step-definitions/
e2e/features/support/hooks.ts and e2e/features/support/world.ts when session lifecycle or shared state matters
e2e/scripts/run-cucumber.ts and e2e/cucumber.config.ts when tags or execution flow matter
Read references/playwright-best-practices.md only when locator, assertion, isolation, or waiting choices are involved.
Read references/cucumber-best-practices.md only when scenario wording, step granularity, tags, or expression design are involved.
Re-check official docs with Context7 before introducing a new Playwright or Cucumber pattern.
Local Rules
e2e/ uses Cucumber for scenarios and Playwright as the browser layer.
DifyWorld is the per-scenario context object. Type this as DifyWorld and use async function, not arrow functions.
Keep glue organized by capability under e2e/features/step-definitions/; use common/ only for broadly reusable steps.
Browser session behavior comes from features/support/hooks.ts:
default: authenticated session with shared storage state
@unauthenticated: clean browser context
@authenticated: readability/selective-run tag only unless implementation changes
@fresh: only for e2e:full* flows
Do not import Playwright Test runner patterns that bypass the current Cucumber + DifyWorld architecture unless the task is explicitly about changing that architecture.
Workflow
Rebuild local context.
Inspect the target feature area.
Reuse an existing step when wording and behavior already match.
Add a new step only for a genuinely new user action or assertion.
Keep edits close to the current capability folder unless the step is broadly reusable.
Write behavior-first scenarios.
Describe user-observable behavior, not DOM mechanics.
Keep each scenario focused on one workflow or outcome.
Keep scenarios independent and re-runnable.
Write step definitions in the local style.
Keep one step to one user-visible action or one assertion.
Prefer Cucumber Expressions such as {string} and {int}.
Scope locators to stable containers when the page has repeated elements.
Avoid page-object layers or extra helper abstractions unless repeated complexity clearly justifies them.
Use Playwright in the local style.
Prefer user-facing locators: getByRole, getByLabel, getByPlaceholder, getByText, then getByTestId for explicit contracts.
Use web-first expect(...) assertions.
Do not use waitForTimeout, manual polling, or raw visibility checks when a locator action or retrying assertion already expresses the behavior.
Validate narrowly.
Run the narrowest tagged scenario or flow that exercises the change.
Run pnpm -C e2e check.
Broaden verification only when the change affects hooks, tags, setup, or shared step semantics.
Review Checklist
Does the scenario describe behavior rather than implementation?
Does it fit the current session model, tags, and DifyWorld usage?
Should an existing step be reused instead of adding a new one?
Are locators user-facing and assertions web-first?
Does the change introduce hidden coupling across scenarios, tags, or instance state?
Does it document or implement behavior that differs from the real hooks or configuration?

Lead findings with correctness, flake risk, and architecture drift.

References
references/playwright-best-practices.md
references/cucumber-best-practices.md
Weekly Installs
17
Repository
langgenius/dify
GitHub Stars
139.9K
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass