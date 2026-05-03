---
title: vueuse-motion-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/vueuse-motion-skilld
---

# vueuse-motion-skilld

skills/harlan-zw/vue-ecosystem-skills/vueuse-motion-skilld
vueuse-motion-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill vueuse-motion-skilld
SKILL.md
vueuse/motion @vueuse/motion@3.0.3

Tags: beta: 2.0.0-beta.29, latest: 3.0.3

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

BREAKING: ESM-only — @vueuse/motion v3.0.0 dropped CommonJS (CJS) support, the package is now ESM-only source

NEW: VueUse v13 support — updated dependencies to support the latest VueUse features in v3.0.0 source

NEW: <Motion> component — declarative component for animations, offering better SSR and MDC support since v2.2.0 source

NEW: <MotionGroup> component — renderless component introduced in v2.2.0 to apply motion configurations to all child elements source

NEW: duration and delay shorthand props — support for setting transition timing directly on elements/components since v2.2.0 source

BREAKING: Drop Vue 2 support — v2.0.0 and above exclusively support Vue 3 source

NEW: Full SSR support — significantly improved server-side rendering compatibility for both components and directives in v2.0.0 source

NEW: kebab-case directive support — v-motion-initial and other directive variants now support kebab-case since v2.1.0 source

NEW: useMotionFeatures export — this composable is now exported for manual feature registration since v2.2.6 source

NEW: useMotion dynamic keys — support for dynamic variant keys when calling .apply() and other methods since v2.1.0 source

NEW: reactive-style and reactive-transform — specialized composables for direct style and transform manipulation since v2.0.0 source

NEW: MotionPlugin types — enhanced TypeScript definitions for the main Vue plugin in v2.2.5 source

BREAKING: onComplete triggers — fixed in v2.2.0 to trigger after each property animation completes instead of only once source

NEW: unref directive bindings — directives now unref initial bindings, supporting refs within objects since v2.0.0 source

Also changed: visibilityOnce variant new v2.0.0 · useSpring documentation update v2.2.0 · preset mutation fix v2.2.0 · useMotions dynamic keys v2.1.0 · useMotionVariants internal updates v2.0.0

Best Practices
Avoid deconstructing useMotions() at the top level of setup because properties are registered after the script execution; access them via the returned object within methods or hooks to ensure reactivity source
// Preferred
const motions = useMotions()
const play = () => motions.myElement?.variant.value = 'play'

// Avoid
const { myElement } = useMotions()


Use camelCase for visibility variants in Nuxt 3 templates (e.g., visibleOnce) rather than kebab-case (visible-once) to ensure proper directive resolution and avoid warnings source

Prefer the <Motion> component over the v-motion directive for projects requiring robust SSR, as it handles initial state style injection more reliably for SEO and UX source

Define custom directives in the MotionPlugin configuration to create reusable animation presets that can be applied consistently via v-motion-[name] across the application source

Use <MotionGroup> to apply a single animation configuration or preset to multiple child elements, significantly reducing template boilerplate and improving maintainability source

Map the leave helper from the motion instance to the Vue <transition> element's @leave event to perform manual and synchronized exit animations on elements source

const { leave } = useMotion(target, { leave: { opacity: 0 } })

// In template
// <transition @leave="(el, done) => leave(done)">


Always specify an initial variant containing all properties that will be animated to prevent unexpected layout shifts and ensure smooth transitions from a known base state source

Utilize useSpring with useMotionProperties for high-performance, frame-rate independent animations that require physical continuity, such as for interactive gestures source

In Nuxt applications, use runtimeConfig.public.motion.directives to define global custom directives, ensuring they are properly initialized during both client and server rendering source

Pass a reactive reference as the target to useMotion to allow the motion instance to automatically track and apply the current variant to new elements as they are updated source

Weekly Installs
86
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