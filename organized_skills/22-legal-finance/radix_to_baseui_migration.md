---
rating: ⭐⭐
title: radix-to-baseui-migration
url: https://skills.sh/ghozysamudra/ai/radix-to-baseui-migration
---

# radix-to-baseui-migration

skills/ghozysamudra/ai/radix-to-baseui-migration
radix-to-baseui-migration
Installation
$ npx skills add https://github.com/ghozysamudra/ai --skill radix-to-baseui-migration
SKILL.md
Radix to Base UI Migration (shadcn)

Execute migration in four passes. Keep each pass small and compilable.

1) Remove Radix package surface and switch imports
Remove Radix primitive packages from dependencies.
Add Base UI package(s) used by the project.
Replace Radix imports with Base UI imports component-by-component.
Keep component names stable during this pass (use aliases if needed) to reduce diff size.

Use references/checklist.md for pass order and validation gates.

2) Replace asChild composition with Base UI render composition
Find trigger/content compositions that relied on asChild.
Replace asChild usage with Base UI render-based composition.
Preserve semantic HTML and avoid nested interactive elements.
Re-test keyboard and focus behavior for each migrated trigger.

Use references/migration-map.md for common asChild migration patterns.

3) Resolve type and API differences
Run type-check and build after each component family migration.
Replace Radix-flavored prop/type names with Base UI equivalents.
Treat TypeScript errors as the migration to-do list; fix from highest fan-out components first.
Check renamed slots/backdrop/overlay/content primitives and event prop naming differences.

Use references/migration-map.md to map common rename classes.

4) Migrate positioning to Positioner-based layout
For floating UI (dropdown, popover, tooltip, dialog-like overlays), introduce the Base UI Positioner pattern where required.
Move placement-related props from old content nodes to the new positioning layer.
Re-verify placement, collision handling, alignment, and animation origin.

Use references/migration-map.md for positioning conversion guidance.

Migration operating rules
Migrate one primitive family at a time (dropdown, popover, dialog, tooltip, select).
Keep visual styles unchanged during API migration; separate style refactors to a later PR.
Prefer docs and shadcn Base UI examples when uncertain; do not guess prop parity.
Keep builds green between families to avoid compounded regressions.
Completion criteria
No Radix primitive imports remain in source.
No migration-related TypeScript errors remain.
All floating components use valid Base UI positioning composition.
Keyboard/focus interactions pass for migrated components.
Existing UI snapshots or smoke tests pass.
Weekly Installs
26
Repository
ghozysamudra/ai
First Seen
Feb 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass