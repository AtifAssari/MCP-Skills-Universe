---
title: formkit-core-skilld
url: https://skills.sh/harlan-zw/vue-ecosystem-skills/formkit-core-skilld
---

# formkit-core-skilld

skills/harlan-zw/vue-ecosystem-skills/formkit-core-skilld
formkit-core-skilld
Installation
$ npx skills add https://github.com/harlan-zw/vue-ecosystem-skills --skill formkit-core-skilld
SKILL.md
formkit/formkit @formkit/core@2.0.0

Tags: perf: 1.0.0-beta.13-c578106, latest: 2.0.0, dev: 2.0.0-dev.c6ae298

References: Docs

API Changes

This section documents version-specific API changes — prioritize recent major/minor releases.

NEW: useFormKitContext() — v1.6.0, access parent context with optional effect callback source

NEW: useFormKitContextById() — v1.6.0, access any context by its explicit id source

NEW: useFormKitNodeById() — v1.6.0, access any node by its explicit id source

NEW: stopWatch() — v1.6.0, de-registers receipts from the watchRegistry function source

NEW: library prop — v1.6.0, adds additional components to the input schema for sections-schema source

NEW: createInput — v1.5.0, third argument sectionsSchema allows extending default sections source

NEW: didMount / mounted — v1.5.0, context property and node event to detect DOM mounting source

NEW: changeLocale() — v1.5.0, globally change locale for all forms across multiple APIs source

NEW: date_after_node — v1.7.0, compare date against another field; also date_before_node source

NEW: passing state — v1.6.3, context.state.passing indicates if input satisfies validation rules source

NEW: minAutoHeight — v1.7.0, prop for auto-height textarea addon to respect CSS min-height source

BREAKING: @formkit/vue — v1.6.0, Vue is now a peer dependency to avoid multiple instance issues source

DEPRECATED: Genesis CSS theme — v1.5.0, marked as legacy; use Tailwind themes instead source

NEW: mergeStrategy (experimental) — v1.6.1, syncs two nodes of same name in same parent (experimental) source

Also changed: getNode<T>() generic v1.6.0 · Boolean props shorthand v1.5.0 · summaryHeader i18n v1.7.0 · node.children reactivity v1.5.0 · FormKitTypeDefinition inference v1.6.0 · themes peer deps removed v1.7.1

Best Practices

Read resolved configuration and prop data from node.props rather than node.config — explicit props and parent configurations are automatically merged into the props object source

Synchronize multiple inputs with the same name at the same level using the mergeStrategy config option — prevents value conflicts when identical names are required by template structure source

Use node.input(value) instead of direct assignment to node.value — ensures the tree's state is tracked and triggers the asynchronous settlement process source

Await node.settled before programmatically reading form values or submitting — guarantees all asynchronous input commits and side effects are complete source

Append .deep to event names in node.on() to capture events bubbling from descendants — allows parent nodes or plugins to respond to subtree lifecycle changes source

Leverage node.ledger to create reactive, tree-wide counters for messages — efficiently sums message states (like errors or visibility) across complex form structures source

Traverse the node tree using node.at() with special tokens like $root, $parent, and $self — provides a robust way to access relative nodes without hardcoding absolute paths source

Opt out of defaultConfig in production to enable tree-shaking for unused rules, inputs, and locales — significantly reduces bundle size by manually registering only required features source

Register middleware via node.hook within plugins to intercept core operations — enables reusable logic for transforming props, values, or error messages across multiple forms source

Always remove event listeners using the "receipt" returned by node.on() via node.off(receipt) — prevents memory leaks and redundant execution in long-lived or dynamic form contexts source

Weekly Installs
57
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