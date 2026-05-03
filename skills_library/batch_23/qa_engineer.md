---
title: qa-engineer
url: https://skills.sh/anyproto/anytype-ts/qa-engineer
---

# qa-engineer

skills/anyproto/anytype-ts/qa-engineer
qa-engineer
Installation
$ npx skills add https://github.com/anyproto/anytype-ts --skill qa-engineer
SKILL.md
QA Engineer Skill

Analyze recent code changes in anytype-ts, map them to testable user-facing behavior, and generate Playwright E2E tests in the ../anytype-desktop-suite repository.

When to Use

Activate this skill when:

After implementing a new feature or modifying existing functionality
After editor/component changes that affect user interactions
The user explicitly asks to add tests for recent changes
After completing a task referenced in CLAUDE.md's "QA Engineer" section
Principles
Change-driven — Only test what actually changed, don't generate tests for untouched code
User-facing — Focus on observable behavior, not implementation details
Compatible — Follow the existing test patterns in anytype-desktop-suite exactly
Minimal — One test file per feature area, don't over-test
Translation-aware — Always use translation keys, never hardcoded UI text
Process
Phase 1: Analyze Changes
Identify what changed — Run git diff against the base branch (or recent commits) to see modified files
Classify changes — Determine which changes are user-facing vs internal refactoring
Map to features — Connect code changes to testable user flows:
Component changes → UI interactions to verify
Store changes → State transitions to test
Menu/popup changes → Open/close/interact flows
Editor changes → Block creation, editing, selection
API changes → Data flow and error handling

Skip internal-only changes (type refactors, utility extractions, pure style changes) that have no user-facing impact.

Phase 2: Research Existing Coverage
Check existing tests — Search ../anytype-desktop-suite/tests/ for tests that already cover the changed feature area
Check existing page objects — Search ../anytype-desktop-suite/src/pages/ for page objects that interact with affected components
Check test plans — Search ../anytype-desktop-suite/specs/ for existing plans covering the area
Identify gaps — Determine what's not yet covered
Phase 3: Create Test Plan

Write a test plan in ../anytype-desktop-suite/specs/ following this format:

# Feature Area — Test Plan

**Source changes:** List of changed files in anytype-ts
**Date:** YYYY-MM-DD

## Prerequisites
- Seed: `tests/seed.spec.ts` (creates account, opens vault)
- Any additional setup needed

### 1. Test Group Name
**Seed:** `tests/seed.spec.ts`

#### 1.1 Scenario Name
**Steps:**
1. Step description
2. Step description
**Expected:** What should happen

#### 1.2 Another Scenario
...

Phase 4: Generate Test Files

Create test files in ../anytype-desktop-suite/tests/ following these strict conventions:

File Structure
// spec: specs/plan-name.md
// seed: tests/seed.spec.ts

import { test, expect } from '../../src/fixtures';
import { restartGrpcServer } from '../../src/helpers/test-server';
// Import relevant page objects
import { SidebarPage } from '../../src/pages/main/sidebar.page';

test.describe('Feature Area', () => {
  test.describe.configure({ mode: 'serial' });

  test.beforeAll(async () => {
    await restartGrpcServer();
  });

  test('should do the expected behavior', async ({ page, translations }) => {
    const sidebar = new SidebarPage(page, translations);
    await sidebar.waitForReady();

    // Step: Description of what we're doing
    await page.getByText(translations.someTranslationKey).click();

    // Verify: Expected outcome
    await expect(page.locator('#some-element')).toBeVisible();
  });
});

Rules
Translations — Always use translations.keyName for UI text. Look up keys in ../anytype-ts/dist/lib/json/lang/en-US.json or ../anytype-ts/src/json/text.json
Page Objects — Use existing page objects from ../anytype-desktop-suite/src/pages/. Create new ones only if needed
Waits — Use await expect(locator).toBeVisible() or waitFor({ state: 'visible' }). Never use setTimeout, networkidle, or fixed delays
Selectors — Prefer role-based > test ID > text > CSS selectors
Isolation — Each test file restarts gRPC server in beforeAll. Tests in a file can share state with serial mode
Naming — File names are kebab-case matching the feature: feature-name.spec.ts
Directory — Place in a subdirectory matching the feature area: tests/editor/, tests/blocks/, etc.
Phase 5: Create Page Objects (if needed)

If the changed feature needs new page interactions not covered by existing page objects, create a new page object:

import { BasePage } from '../base.page';

export class FeaturePage extends BasePage {
  // Locators
  get someButton() {
    return this.page.locator('#some-button');
  }

  get someText() {
    return this.page.getByText(this.t('translationKey'));
  }

  // Actions
  async waitForReady() {
    await this.someButton.waitFor({ state: 'visible' });
  }

  async doSomething() {
    await this.someButton.click();
    await expect(this.someText).toBeVisible();
  }
}


Page objects go in ../anytype-desktop-suite/src/pages/ in the appropriate subdirectory.

Phase 6: Output Summary

After generating tests, provide a summary:

## QA Engineer Summary

### Changes Analyzed
- file1.tsx — description of change
- file2.tsx — description of change

### Tests Generated
- `tests/feature/scenario-name.spec.ts` — what it tests
- `specs/feature-plan.md` — test plan

### New Page Objects
- `src/pages/main/feature.page.ts` — (if created)

### Coverage Notes
- What's covered by new tests
- What's NOT covered and why (e.g., requires manual testing, backend-only change)

### Run Tests
```bash
cd ../anytype-desktop-suite && npm test -- tests/feature/scenario-name.spec.ts


## Finding Translation Keys

To map UI text to translation keys:

1. Search `../anytype-ts/src/json/text.json` for the English text
2. The key is the JSON property name (e.g., `"authSelectSignup": "Create new vault"` → use `translations.authSelectSignup`)
3. For dynamic text with parameters, check how the component calls `translate()` with substitution params

## Finding Selectors

To find stable selectors for elements:

1. Search the component source in `../anytype-ts/src/ts/component/` for `id=`, `data-`, `className`
2. Check for block IDs: blocks typically have `#block-{id}` selectors
3. Check for menu IDs: menus use `#menu{Type}` pattern
4. Check for popup IDs: popups use `#popup{Type}` pattern
5. The sidebar uses `#sidebarPage{Section}` pattern

## Test Areas Mapping

| anytype-ts Area | Test Directory | Page Objects |
|---|---|---|
| `component/block/text.tsx` | `tests/editor/` | `pages/main/editor.page.ts` |
| `component/block/dataview.tsx` | `tests/dataview/` | `pages/main/dataview.page.ts` |
| `component/menu/` | `tests/menus/` | (inline or new page object) |
| `component/popup/` | `tests/popups/` | `pages/components/modal.component.ts` |
| `component/sidebar/` | `tests/sidebar/` | `pages/main/sidebar.page.ts` |
| `component/widget/` | `tests/widgets/` | `pages/main/widget.page.ts` |
| `component/page/main/graph.tsx` | `tests/graph/` | (new page object) |
| `component/page/auth/` | `tests/auth/` | `pages/auth/*.page.ts` |
| `store/` | (test via UI) | (use existing page objects) |

## What NOT to Test

- Pure TypeScript type changes
- Internal utility refactors with no UI impact
- CSS-only changes (unless they affect element visibility/layout)
- Backend (anytype-heart) changes — those have their own tests
- Build/config changes

Weekly Installs
53
Repository
anyproto/anytype-ts
GitHub Stars
7.5K
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass