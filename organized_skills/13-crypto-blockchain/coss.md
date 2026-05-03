---
rating: ⭐⭐
title: coss
url: https://skills.sh/cosscom/coss/coss
---

# coss

skills/cosscom/coss/coss
coss
Installation
$ npx skills add https://github.com/cosscom/coss --skill coss
SKILL.md
coss ui

coss ui is a component library built on Base UI with a shadcn-like developer experience plus a large particle catalog.

What this skill is for

Use this skill to:

pick the right coss primitive(s) for a UI task
write correct coss usage code (imports, composition, props)
avoid common migration mistakes from shadcn/Radix assumptions
reference particle examples to produce practical, production-like patterns
Source of truth
coss components docs: apps/ui/content/docs/components/*.mdx
https://github.com/cosscom/coss/tree/main/apps/ui/content/docs/components
coss particle examples: apps/ui/registry/default/particles/p-*.tsx
https://github.com/cosscom/coss/tree/main/apps/ui/registry/default/particles
coss particles catalog: https://coss.com/ui/particles
docs map for agents: https://coss.com/ui/llms.txt
Out of scope
Maintaining coss monorepo internals/build pipelines.
Editing registry internals unless explicitly requested.
Principles for agent output
Use existing primitives and particles first before inventing custom markup.
Prefer composition over custom behavior reimplementation.
Follow coss naming and APIs from docs exactly.
Keep examples accessible and production-realistic.
Prefer concise code that mirrors coss docs/particles conventions.
Assume Tailwind CSS v4 conventions in coss examples and setup guidance.
Critical usage rules

Always apply before returning coss code:

Do not invent coss APIs. Verify against component docs first.
For trigger-based primitives (Dialog, Menu, Select, Popover, Tooltip), follow each primitive's documented trigger/content hierarchy and composition API; do not mix patterns across components.
Preserve accessibility labels and error semantics.
Consult primitive-specific guides for component invariants and edge cases.
For manual install guidance, include all required dependencies and local component files referenced by imports.
Prefer styled coss exports first; use *Primitive exports only when custom composition/styling requires it.

Rule references (read on demand when the task touches these areas):

./references/rules/styling.md — Tailwind tokens, icon conventions, data-slot selectors
./references/rules/forms.md — Field composition, validation, input patterns
./references/rules/composition.md — Trigger/popup hierarchies, grouped controls
./references/rules/migration.md — shadcn/Radix to coss/Base UI migration patterns
./references/portal-props.md — optional portalProps on composed popups and toast providers (keepMounted, container, which surfaces support it)
Component discovery

All 53 primitives have dedicated reference guides at ./references/primitives/<name>.md. To find the right one for a task, consult the component registry index:

./references/component-registry.md
Usage workflow
Identify user intent (single primitive, composed flow, form flow, overlay flow, feedback flow).
Consult references/component-registry.md to identify candidate primitives.
Select primitives from coss docs first; avoid custom fallback unless needed.
Check at least one particle example for practical composition patterns. Particle files live at apps/ui/registry/default/particles/p-<name>-<N>.tsx (e.g. p-dialog-1.tsx).
Write minimal code using documented imports/props.
Self-check accessibility and composition invariants.
Installation reference

See ./references/cli.md for full install/discovery workflow.

Quick CLI pattern:

npx shadcn@latest add @coss/<component>


Quick manual pattern:

install dependencies listed in the component docs page
copy required component file(s)
update imports to match the target app alias setup
Primitive Guidance

Every primitive has a reference guide at ./references/primitives/<name>.md with imports, minimal patterns, inline code examples, pitfalls, and particle references. Use the component registry to find the right file.

High-risk primitives (read these guides first -- they have the most composition gotchas):

./references/primitives/dialog.md — modal overlays, form-in-dialog, responsive dialog/drawer
./references/primitives/menu.md — dropdown actions, checkbox/radio items, submenus
./references/primitives/select.md — items-first pattern, multiple, object values, groups
./references/primitives/form.md — Field composition, validation, submission
./references/primitives/input-group.md — addons, DOM order invariant, textarea layouts
./references/primitives/toast.md — toastManager (not Sonner), anchored toasts, providers
Output Checklist

Before returning code:

imports and props match coss docs
composition structure is valid for selected primitive(s)
accessibility and explicit control types (button, input, etc.) are present
migration-sensitive flows are verified (type/lint, keyboard/a11y behavior, and SSR-sensitive primitives like Select/Command)
Weekly Installs
881
Repository
cosscom/coss
GitHub Stars
9.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn