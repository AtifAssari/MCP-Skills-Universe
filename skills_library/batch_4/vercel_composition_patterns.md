---
title: vercel-composition-patterns
url: https://skills.sh/supabase/supabase/vercel-composition-patterns
---

# vercel-composition-patterns

skills/supabase/supabase/vercel-composition-patterns
vercel-composition-patterns
Originally fromvercel-labs/agent-skills
Installation
$ npx skills add https://github.com/supabase/supabase --skill vercel-composition-patterns
SKILL.md
React Composition Patterns

Composition patterns for building flexible, maintainable React components. Avoid boolean prop proliferation by using compound components, lifting state, and composing internals. These patterns make codebases easier for both humans and AI agents to work with as they scale.

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
architecture-avoid-boolean-props - Don't add boolean props to customize behavior; use composition
architecture-compound-components - Structure complex components with shared context
2. State Management (MEDIUM)
state-decouple-implementation - Provider is the only place that knows how state is managed
state-context-interface - Define generic interface with state, actions, meta for dependency injection
state-lift-state - Move state into provider components for sibling access
3. Implementation Patterns (MEDIUM)
patterns-explicit-variants - Create explicit variant components instead of boolean modes
patterns-children-over-render-props - Use children for composition instead of renderX props
4. React 19 APIs (MEDIUM)

⚠️ React 19+ only. Supabase Studio currently uses React 18 — skip these patterns in Studio code.

react19-no-forwardref - Don't use forwardRef; use use() instead of useContext()
How to Use

Read individual rule files for detailed explanations and code examples:

rules/architecture-avoid-boolean-props.md
rules/state-context-interface.md


Each rule file contains:

Brief explanation of why it matters
Incorrect code example with explanation
Correct code example with explanation
Additional context and references
Full Compiled Document

For the complete guide with all rules expanded: AGENTS.md

Weekly Installs
464
Repository
supabase/supabase
GitHub Stars
101.8K
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass