---
rating: ⭐⭐
title: code-discipline
url: https://skills.sh/mwillbanks/agent-skills/code-discipline
---

# code-discipline

skills/mwillbanks/agent-skills/code-discipline
code-discipline
Installation
$ npx skills add https://github.com/mwillbanks/agent-skills --skill code-discipline
SKILL.md
Code Discipline

Use this skill whenever a task involves adding or modifying logic and there is risk of helper sprawl, unnecessary wrappers, duplicate utilities, duplicate constants, or abstraction bloat.

This is an anti-laziness skill. It prevents agents from "solving" tasks by inventing new files, helpers, and indirection when existing primitives already solve the problem.

Default assumption:

The user wants maintainable code with minimal abstraction surface area.
The user does not want renamed duplicates of existing behavior.
New helpers, wrappers, constants modules, and style-only indirection are disallowed unless justified by clear architectural value.
When to Use

Invoke this skill for:

feature implementation that introduces new logic
refactors that add utility or service layers
UI changes where component-local helpers may proliferate
frontend work where constants, tokens, or styled files may be needlessly split apart
bug fixes that tempt quick wrapper-based patches
code review focused on maintainability and reuse discipline

Use together with agent-execution-mode and repo-standards-enforcement for production implementation work.

Core Enforcement Policy
Non-Negotiable
Do not create a helper if the logic is trivial and used once.
Do not create a wrapper that only forwards calls.
Do not create renamed duplicates of existing utilities.
Do not add service, hook, or adapter layers that add indirection without policy.
Do not reimplement platform or standard library behavior.
Do not duplicate utility logic across packages.
Do not extract one-off constants into a module just to reduce line count.
Do not create a constants, helpers, utils, or shared file unless ownership and reuse are real.
Do not split styles into separate files when the styles are local and the split adds no ownership value.
Required Posture
prefer platform primitives first
prefer framework-native capabilities second
prefer existing internal utilities third
prefer existing repository dependencies fourth
create new abstraction only as a last resort with explicit rationale
Mandatory Evaluation Order

Before adding any helper, hook, service, wrapper, adapter, formatter, parser, transformer, constant module, token, or utility, evaluate in this exact order:

language or runtime primitives
standard library APIs
framework-native features
existing repository utilities
existing installed dependencies
new abstraction with justification

Skipping this order is non-compliant behavior.

New Abstraction Admission Gate

A new abstraction, helper, constant module, or shared style boundary is allowed only if at least one is true:

it enforces domain invariants or policy
it encapsulates non-trivial repeated logic across multiple call sites
it isolates an infrastructure boundary
it provides correctness, validation, or security guarantees
it improves testability of genuinely complex behavior
it creates a shared source of truth for a value that must stay synchronized across multiple consumers

A new abstraction is rejected if it only:

renames existing behavior
forwards calls one-to-one
wraps a single primitive or single library call
exists for style preference only
hides a one-off literal that is clearer inline
Smell Rules

Treat these as automatic scrutiny triggers:

names starting with normalize, format, parse, transform, sanitize, safe, to
names starting with build, make, create, get, set, use, or manage when they only wrap a single operation
services that only proxy repository or SDK methods
hooks that only call another hook and return the same shape
helpers used once in a single file
utility modules that only contain one-line wrappers
constants modules with a single consumer
style files that only move declarations without changing ownership or reuse

Smells are not always wrong, but they require explicit defense.

Component Logic Rules
Keep simple display and one-off transformations inline.
Extract only when complexity or reuse justifies extraction.
Do not grow component files into local utility libraries.
Move reusable logic to the correct shared layer, not the nearest file.
Keep one-off constants inline unless they are part of a shared contract or repeated across files.
Keep component-local styled declarations local unless repeated styling proves the need for a shared primitive.
Constant Placement Rules
Keep one-off literals near their use when that improves readability.
Promote a constant only when it carries shared meaning, is reused, or is part of a public or cross-file contract.
Do not create a module just to host a single constant.
Do not move a literal into const X = ... if the new name adds no meaning.
Put shared design tokens in the theme or design-system layer, not in page-local files.
Put shared UI constants in the owning domain or shared layer, not in a convenience bucket.
File and Style Organization Rules
Keep helpers, constants, and styles in the narrowest correct owner.
Prefer colocated component styles for component-local concerns.
Prefer shared style primitives only when multiple components truly share them.
Avoid generic catch-all folders that exist only to hide structure.
Avoid re-export barrels that add no boundary or reuse value.
Keep styled file names descriptive of ownership, not generic (Button.styles.ts is clearer than styles.ts).
Split a styled file only when the split makes ownership, reuse, or maintenance clearer.
Do not create a separate file for a tiny style fragment that is used once.
Monorepo and Workspace Rules
do not duplicate helpers across packages
promote shared logic to the correct shared package when reuse exists
respect architecture boundaries when sharing utilities
do not bypass boundaries through convenience imports
Review and Refactor Enforcement

When active in review/refactor mode, agents must:

flag unnecessary helpers and wrappers
remove trivial abstractions where safe
consolidate duplicate utilities
replace handwritten logic with platform/library primitives where appropriate
explain each removal or consolidation with maintainability rationale
Definition of Done

This skill is satisfied only when all are true:

no newly introduced trivial helper/wrapper layers remain
no duplicate utility logic remains in changed scope
no one-off constants were extracted without a shared-meaning reason
new abstractions (if any) are justified by the admission gate
platform/framework/internal utilities were preferred over reinvention
changed scope is simpler or equal in surface area, not more bloated
Output Contract

When responding after this skill is used, report:

what abstraction/helper candidates were considered
what existing primitive/utility was reused
what abstractions were rejected and why
what consolidations/removals were performed
any new abstraction added and which admission-gate condition allowed it
where constants and styles were kept inline instead of being extracted
References

Use the reference guides for strict implementation details:

references/helper-functions.md
references/abstraction-patterns.md
references/library-preference.md
references/component-logic.md
references/constants-and-organization.md
Weekly Installs
29
Repository
mwillbanks/agent-skills
GitHub Stars
1
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass