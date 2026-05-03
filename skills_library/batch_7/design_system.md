---
title: design-system
url: https://skills.sh/anthropics/knowledge-work-plugins/design-system
---

# design-system

skills/anthropics/knowledge-work-plugins/design-system
design-system
Installation
$ npx skills add https://github.com/anthropics/knowledge-work-plugins --skill design-system
SKILL.md
/design-system

If you see unfamiliar placeholders or need to check which tools are connected, see CONNECTORS.md.

Manage your design system — audit for consistency, document components, or design new patterns.

Usage
/design-system audit                    # Full system audit
/design-system document [component]     # Document a component
/design-system extend [pattern]         # Design a new component or pattern

Components of a Design System
Design Tokens

Atomic values that define the visual language:

Colors (brand, semantic, neutral)
Typography (scale, weights, line heights)
Spacing (scale, component padding)
Borders (radius, width)
Shadows (elevation levels)
Motion (durations, easings)
Components

Reusable UI elements with defined:

Variants (primary, secondary, ghost)
States (default, hover, active, disabled, loading, error)
Sizes (sm, md, lg)
Behavior (interactions, animations)
Accessibility (ARIA, keyboard)
Patterns

Common UI solutions combining components:

Forms (input groups, validation, submission)
Navigation (sidebar, tabs, breadcrumbs)
Data display (tables, cards, lists)
Feedback (toasts, modals, inline messages)
Principles
Consistency over creativity — The system exists so teams don't reinvent the wheel
Flexibility within constraints — Components should be composable, not rigid
Document everything — If it's not documented, it doesn't exist
Version and migrate — Breaking changes need migration paths
Output — Audit
## Design System Audit

### Summary
**Components reviewed:** [X] | **Issues found:** [X] | **Score:** [X/100]

### Naming Consistency
| Issue | Components | Recommendation |
|-------|------------|----------------|
| [Inconsistent naming] | [List] | [Standard to adopt] |

### Token Coverage
| Category | Defined | Hardcoded Values Found |
|----------|---------|----------------------|
| Colors | [X] | [X] instances of hardcoded hex |
| Spacing | [X] | [X] instances of arbitrary values |
| Typography | [X] | [X] instances of custom fonts/sizes |

### Component Completeness
| Component | States | Variants | Docs | Score |
|-----------|--------|----------|------|-------|
| Button | ✅ | ✅ | ⚠️ | 8/10 |
| Input | ✅ | ⚠️ | ❌ | 5/10 |

### Priority Actions
1. [Most impactful improvement]
2. [Second priority]
3. [Third priority]

Output — Document
## Component: [Name]

### Description
[What this component is and when to use it]

### Variants
| Variant | Use When |
|---------|----------|
| [Primary] | [Main actions] |
| [Secondary] | [Supporting actions] |

### Props / Properties
| Property | Type | Default | Description |
|----------|------|---------|-------------|
| [prop] | [type] | [default] | [description] |

### States
| State | Visual | Behavior |
|-------|--------|----------|
| Default | [description] | — |
| Hover | [description] | [interaction] |
| Active | [description] | [interaction] |
| Disabled | [description] | Non-interactive |
| Loading | [description] | [animation] |

### Accessibility
- **Role**: [ARIA role]
- **Keyboard**: [Tab, Enter, Escape behavior]
- **Screen reader**: [Announced as...]

### Do's and Don'ts
| ✅ Do | ❌ Don't |
|------|---------|
| [Best practice] | [Anti-pattern] |

### Code Example
[Framework-appropriate code snippet]

Output — Extend
## New Component: [Name]

### Problem
[What user need or gap this component addresses]

### Existing Patterns
| Related Component | Similarity | Why It's Not Enough |
|-------------------|-----------|---------------------|
| [Component] | [What's shared] | [What's missing] |

### Proposed Design

#### API / Props
| Property | Type | Default | Description |
|----------|------|---------|-------------|
| [prop] | [type] | [default] | [description] |

#### Variants
| Variant | Use When | Visual |
|---------|----------|--------|
| [Variant] | [Scenario] | [Description] |

#### States
| State | Behavior | Notes |
|-------|----------|-------|
| Default | [Description] | — |
| Hover | [Description] | [Interaction] |
| Disabled | [Description] | Non-interactive |
| Loading | [Description] | [Animation] |

#### Tokens Used
- Colors: [Which tokens]
- Spacing: [Which tokens]
- Typography: [Which tokens]

### Accessibility
- **Role**: [ARIA role]
- **Keyboard**: [Expected interactions]
- **Screen reader**: [Announced as...]

### Open Questions
- [Decision that needs design review]
- [Edge case to resolve]

If Connectors Available

If ~~design tool is connected:

Audit components directly in Figma — check naming, variants, and token usage
Pull component properties and layer structure for documentation

If ~~knowledge base is connected:

Search for existing component documentation and usage guidelines
Publish updated documentation to your wiki
Tips
Start with an audit — Know where you are before deciding where to go.
Document as you build — It's easier to document a component while designing it.
Prioritize coverage over perfection — 80% of components documented beats 100% of 10 components.
Weekly Installs
1.1K
Repository
anthropics/know…-plugins
GitHub Stars
11.7K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass