---
title: composition-patterns
url: https://skills.sh/jgamaraalv/ts-dev-kit/composition-patterns
---

# composition-patterns

skills/jgamaraalv/ts-dev-kit/composition-patterns
composition-patterns
Installation
$ npx skills add https://github.com/jgamaraalv/ts-dev-kit --skill composition-patterns
SKILL.md
React Composition Patterns

Composition patterns for building flexible, maintainable React components. Avoid boolean prop proliferation by using compound components, lifting state, and composing internals. These patterns make codebases easier for both humans and AI agents to work with as they scale.

When NOT to Use

Skip these patterns when: fewer than 3 props, simple variants, or single-use components.

When to Apply

Reference these guidelines when:

Refactoring components with many boolean props
Building reusable component libraries
Designing flexible component APIs
Reviewing component architecture
Working with compound components or context providers
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Component Architecture	HIGH	architecture-
2	State Management	MEDIUM	state-
3	Implementation Patterns	MEDIUM	patterns-
4	React 19 APIs	MEDIUM	react19-
Quick Reference
1. Component Architecture (HIGH)
Avoid boolean props — Don't add boolean props like isThread, isEditing, isDMThread to customize behavior. Each boolean doubles possible states. Use composition instead — see references/architecture-avoid-boolean-props.md
Compound components — Structure complex components with shared context so each subcomponent accesses state via context, not props — see references/architecture-compound-components.md
2. State Management (MEDIUM)
Decouple implementation — Provider is the only place that knows how state is managed — see references/state-decouple-implementation.md
Context interface — Define generic interface with state, actions, meta for dependency injection — see references/state-context-interface.md
Lift state — Move state into provider components for sibling access — see references/state-lift-state.md
3. Implementation Patterns (MEDIUM)
Explicit variants — Create explicit variant components instead of boolean modes — see references/patterns-explicit-variants.md
Children over render props — Use children for composition instead of renderX props — see references/patterns-children-over-render-props.md
4. React 19 APIs (MEDIUM)

React 19+ only. Skip this section if using React 18 or earlier.

No forwardRef — Don't use forwardRef; pass ref as a regular prop. Use use() instead of useContext() — see references/react19-no-forwardref.md
Weekly Installs
22
Repository
jgamaraalv/ts-dev-kit
GitHub Stars
14
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass