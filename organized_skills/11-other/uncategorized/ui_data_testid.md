---
rating: ⭐⭐
title: ui-data-testid
url: https://skills.sh/dtyq/magic/ui-data-testid
---

# ui-data-testid

skills/dtyq/magic/ui-data-testid
ui-data-testid
Installation
$ npx skills add https://github.com/dtyq/magic --skill ui-data-testid
SKILL.md
UI Data-testid
Overview

Add predictable data-testid attributes to UI code as part of implementation, not as a later patch. Keep selectors stable across i18n text changes and visual refactors. Follow project testing rules in .cursor/rules:

preserve existing data-testid during refactor/migration
use data-testid-first query strategy in project tests
Workflow
Determine the scope prefix from feature/module context (for example: user-menus, organization-switch, settings-profile).
Add data-testid to the component root container.
Add data-testid to all primary interactive nodes:
button/link triggers
input/select/checkbox/radio controls
tabs/menu items/submenu triggers
modal/drawer open and confirm actions
For config-driven UI (for example menu.items), add "data-testid" in config and forward it to the real clickable DOM node in renderer/wrapper components.
For repeated list rows/items, prefer one shared id queried with getAllByTestId; if uniqueness is required, append a stable business key (never array index when order can change).
Keep existing ids unchanged unless user explicitly asks to rename; never remove existing ids in migration tasks.
For interaction changes, add or update Vitest/RTL tests in colocated __tests__ where feasible.
Naming Rules
Use lowercase kebab-case only.
Use semantic format: <scope>-<entity>-<action>.
Keep IDs text-agnostic (do not depend on i18n labels).
Avoid dynamic/random values (Date.now, UUID, translated text).
Do not embed secrets, emails, phone numbers, or tokens.
Use stable suffixes when applicable: trigger, content, button, input, option, item, row, loading, empty, error.
Minimum Coverage Checklist

For every newly created UI component, include at least:

one root container test id
one primary CTA test id
test ids for each secondary action button
test ids for each form field group/control
test ids for menu item triggers when menus are present
preserved historical data-testid in touched files
loading/empty/error test ids for async UIs
Query Priority

When writing or updating tests:

prefer getByTestId for stable selectors in this project
use getByRole, getByLabelText, getByText as complementary assertions
avoid container.querySelector(...) selectors for user-facing behavior tests

This keeps alignment with .cursor/rules/testing-guide.mdc.

Scenario Playbook

Apply these patterns for stable and accurate element targeting:

Forms
add ids for form container, inputs, submit/cancel buttons, and validation errors
Lists and tables
add list container id and row container id
use stable business key for row id suffix when uniqueness is required
query child actions with within(row) scope
Menus and dropdowns
add ids for trigger, popup content, and each actionable menu item
if menu is config-driven, forward item-level data-testid to rendered node
Modal and drawer
add ids for open trigger, modal content, primary action, and close/cancel action
Async states
add ids for loading, empty, and error states
Stability Rules
Never generate ids from array index if order may change.
Never generate ids from random values or timestamps.
Keep singleton ids unique on a page.
For repeated components, keep shared child ids and scope with within(...).
Patterns
Component markup
<div data-testid="user-menus-organization-info">
  <button type="button" data-testid="user-menus-upgrade-button" />
  <button type="button" data-testid="user-menus-recharge-button" />
</div>

Config + renderer forwarding
const items = [
  { key: "logout", label: t("logout"), "data-testid": "user-menus-logout" },
]

<ItemComponent data-testid={menuItem["data-testid"]}>{menuItem.label}</ItemComponent>

Done Criteria

Complete only when all new interactive nodes in touched UI files have stable data-testid values and any wrapper layer correctly forwards them to rendered DOM elements. Confirm no existing data-testid was removed unintentionally in migration/refactor diffs.

Weekly Installs
16
Repository
dtyq/magic
GitHub Stars
4.8K
First Seen
Mar 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass