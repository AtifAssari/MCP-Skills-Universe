---
rating: ⭐⭐
title: vueuse-math-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/vueuse-math-skilld
---

# vueuse-math-skilld

skills/harlan-zw/vue-ecosystem-skills/vueuse-math-skilld
vueuse-math-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill vueuse-math-skilld
SKILL.md
vueuse/vueuse @vueuse/math@14.2.1

Tags: alpha: 14.0.0-alpha.3, beta: 14.0.0-beta.1, latest: 14.2.1

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

DEPRECATED: and, or, not — v14 deprecated in favor of original names logicAnd, logicOr, logicNot source

BREAKING: Requires Vue 3.5+ — v14 moved to Vue 3.5 as minimum version, enabling native useTemplateRef and MaybeRefOrGetter source

BREAKING: ESM-only — v13 dropped CommonJS (CJS) support entirely source

NEW: useAverage — reactively calculate average from an array or variadic arguments

NEW: useSum — reactively calculate sum from an array or variadic arguments

NEW: createProjection — create a reusable numeric projector between two numeric domains

NEW: createGenericProjection — create a projector with a custom mapping function for arbitrary types

NEW: usePrecision — options now include math property for rounding strategy (floor, ceil, round)

NEW: useClamp — returns ComputedRef instead of Ref when input is a getter or readonly ref

NEW: useMath — provides reactive access to any standard Math method via key name

NEW: logicAnd, logicOr, logicNot — variadic reactive boolean logic supporting multiple refs

NEW: useMax, useMin — support both array and variadic arguments for reactive comparison

NEW: useAbs, useCeil, useFloor, useRound, useTrunc — dedicated reactive wrappers for common Math methods

NEW: useProjection — reactive numeric projection from one domain to another

Also changed: tsdown build system v14 · WatchSource<T> types v14 · MaybeRefOrGetter native v12.8

Best Practices
Use useClamp with a mutable ref to create a self-validating state. When a mutable ref is passed, it returns a writable computed that automatically clamps any value assigned to it source
// Preferred: prevents invalid state assignment
const value = useClamp(shallowRef(0), 0, 10)
value.value = 15 // state remains 10


Pass reactive arrays for domains in useProjection to handle dynamic scaling. This is preferred for UI elements like zoomable charts or responsive sliders where the input/output boundaries change over time source

Define reusable mappers with createProjection outside component logic. This ensures consistent scaling across different parts of the application and reduces the overhead of redefining domains source

Leverage rest arguments in aggregation composables for ad-hoc calculations. useSum, useAverage, useMax, and useMin accept multiple refs directly, avoiding the need to create intermediate array refs

// Preferred: cleaner syntax for fixed sets of refs
const total = useSum(refA, refB, refC)


Prefer usePrecision over toFixed for numeric operations. usePrecision returns a number, which prevents type-coercion bugs and allows further mathematical operations without re-parsing strings source

Use explicit rounding modes in usePrecision for specific UI requirements. Pass the math option ('floor' | 'ceil' | 'round') to control how fractional values are handled in paginators or progress bars source

Combine logicAnd or logicOr with @vueuse/core's whenever for cleaner side effects. This pattern is more readable than complex manual computed properties when triggering actions based on multiple reactive flags source

Employ createGenericProjection for non-linear domain mapping. Provide a custom projector function to handle logarithmic scales or custom eased transitions between numeric domains source

Use useMath to reactively derive values from standard Math methods. It automatically wraps multiple arguments and ensures the result updates whenever any input dependency changes source

Use logicNot for reactive boolean inversion in templates. It expresses intent more clearly than !ref.value or manual computed wrappers when defining visibility or disabled states

Weekly Installs
71
Repository
harlan-zw/vue-e…m-skills
GitHub Stars
158
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass