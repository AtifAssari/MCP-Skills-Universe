---
title: zustand
url: https://skills.sh/pproenca/dot-skills/zustand
---

# zustand

skills/pproenca/dot-skills/zustand
zustand
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill zustand
SKILL.md
Community Zustand Best Practices

Comprehensive performance and architecture guide for Zustand state management in React applications. Contains 43 rules across 8 categories, prioritized by impact from critical (store architecture, selector optimization) to incremental (advanced patterns).

When to Apply

Reference these guidelines when:

Creating new Zustand stores
Optimizing re-render performance with selectors
Implementing persistence or middleware
Integrating Zustand with SSR/Next.js
Reviewing code for state management patterns
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Store Architecture	CRITICAL	store-
2	Selector Optimization	CRITICAL	select-
3	Re-render Prevention	HIGH	render-
4	State Updates	MEDIUM-HIGH	update-
5	Middleware Configuration	MEDIUM	mw-
6	SSR and Hydration	MEDIUM	ssr-
7	TypeScript Patterns	LOW-MEDIUM	ts-
8	Advanced Patterns	LOW	adv-
Quick Reference
1. Store Architecture (CRITICAL)
store-multiple-stores - Use multiple small stores instead of one monolithic store
store-separate-actions - Separate actions from state in dedicated namespace
store-event-naming - Name actions as events not setters
store-colocate-logic - Colocate actions with the state they modify
store-avoid-derived-state - Derive computed values instead of storing them
store-domain-boundaries - Organize stores by feature domain
2. Selector Optimization (CRITICAL)
select-always-use - Always use selectors never subscribe to entire store
select-atomic-picks - Use atomic selectors for single values
select-stable-returns - Ensure selectors return stable references
select-custom-hooks - Export custom hooks not raw store
select-auto-generate - Use auto-generated selectors for large stores
select-memoize-computed - Memoize expensive computed selectors
select-avoid-inline - Define selectors outside components
3. Re-render Prevention (HIGH)
render-use-shallow - Use useShallow for multi-property selections
render-equality-fn - Provide custom equality functions when needed
render-memo-children - Memo children affected by parent store updates
render-subscribe-external - Use subscribe for non-React consumers
render-avoid-object-returns - Avoid returning new objects from selectors
render-split-components - Split components to minimize subscription scope
4. State Updates (MEDIUM-HIGH)
update-functional-set - Use functional form when updating based on previous state
update-immutable - Never mutate state directly
update-shallow-merge - Understand set() shallow merge behavior
update-async-actions - Handle async actions with loading and error states
update-batch-updates - Batch related updates in single set call
5. Middleware Configuration (MEDIUM)
mw-devtools-actions - Name actions for DevTools debugging
mw-persist-partialize - Use partialize for selective persistence
mw-persist-migration - Version and migrate persisted state
mw-immer-nested - Use immer for deeply nested state updates
mw-combine-order - Apply middlewares in correct order
mw-slice-middleware - Apply middleware at combined store level
6. SSR and Hydration (MEDIUM)
ssr-skip-hydration - Use skipHydration in SSR contexts
ssr-manual-rehydrate - Manually rehydrate on client mount
ssr-hydration-hook - Use custom hook to prevent hydration mismatch
ssr-check-window - Guard browser APIs with typeof window check
7. TypeScript Patterns (LOW-MEDIUM)
ts-state-creator - Use StateCreator for slice typing
ts-middleware-inference - Preserve type inference with middleware
ts-separate-types - Separate state and actions interfaces
ts-generic-selectors - Type selectors for reusability
ts-bound-store - Type combined stores correctly
8. Advanced Patterns (LOW)
adv-context-stores - Combine Zustand with React Context for dependency injection
adv-transient-updates - Use subscribe for transient updates
adv-computed-getters - Implement computed state with getters
adv-third-party-integration - Integrate with React Query and SWR
How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
209
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass