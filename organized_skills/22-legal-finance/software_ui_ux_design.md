---
rating: ⭐⭐
title: software-ui-ux-design
url: https://skills.sh/vasilyu1983/ai-agents-public/software-ui-ux-design
---

# software-ui-ux-design

skills/vasilyu1983/ai-agents-public/software-ui-ux-design
software-ui-ux-design
Installation
$ npx skills add https://github.com/vasilyu1983/ai-agents-public --skill software-ui-ux-design
SKILL.md
Software UI/UX Design

Design intuitive, accessible, user-centered interfaces.

Baselines (Mar 2026):

Accessibility: WCAG 2.2 Level AA — W3C
Performance: Core Web Vitals (LCP ≤2.5s, INP ≤200ms, CLS ≤0.1) — web.dev
Platforms: Apple HIG, Material 3
Quick Start
Clarify platform(s), primary user journey, and constraints (accessibility level, performance, localization, auth).
Choose track: audit an existing UI (heuristics + state matrix + WCAG) or design a new UI (IA + flows + UI spec).
Produce artifacts: recommendations, acceptance criteria, and a handoff spec (components, states, copy, tokens).
Decision Tree
Design challenge:
    ├─ What to build? → Use software-ux-research first
    ├─ Improving existing UI?
    │   ├─ Usability issues → Heuristic review
    │   ├─ Accessibility gaps → WCAG 2.2 audit
    │   ├─ Inconsistency → Design system alignment
    │   └─ Conversion issues → CRO audit
    ├─ Building new UI?
    │   └─ references/ui-generation-workflows.md
    ├─ Non-technical users / simplification?
    │   └─ references/simplification-patterns.md
    ├─ Specific demographics?
    │   └─ references/demographic-inclusive-design.md
    └─ Platform constraints?
        ├─ Web → semantics + focus + reflow
        ├─ iOS → system nav + Dynamic Type
        └─ Android → Material + edge-to-edge

Interaction Checklist
Goal	Do	Avoid
Clarity	One primary action per view	Competing CTAs
Affordances	Native controls, strong signifiers	Clickable divs, hover-only
Feedback	Immediate visual response	Silent taps
Error prevention	Constrain inputs, show examples	Submit-then-fail
Error recovery	Specific message + next step	"Something went wrong"
Consistency	Reuse patterns and terms	Same term, different meanings
State Matrix
State	Treatment	When
Loading	Placeholder matching layout	Data fetching
Empty	Message + CTA	Zero items
Error	Alert + retry action	Request fails
Offline	Banner + cached indicator	No network
Degraded	Warning + limited functionality	Partial failure
Platform Constraints
Web
Semantic HTML first (no "div soup")
ARIA only when needed
Manage focus on SPA navigation
Reflow at 320 CSS px (WCAG 1.4.10)
Target size ≥24px (WCAG 2.5.8)
iOS
System navigation (tab bar, nav bar)
Dynamic Type support
Dark mode + system materials
Handle Safe Areas
Android
Material 3 components
Dynamic Color (Material You)
Edge-to-edge content
Handle predictive back
WCAG 2.2 Key Changes
Requirement	Implementation
Focus not obscured	Keep focus visible with sticky UI
Focus appearance	Clear visible indicator
Dragging movements	Non-drag alternatives
Target size	≥24×24 CSS px
Redundant entry	Don't re-request known info
Accessible auth	Avoid cognitive tests
Reduced Motion
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

Design Tokens
{
  "color": {
    "primary": {
      "$value": "#0066cc",
      "$type": "color"
    }
  },
  "spacing": {
    "sm": {
      "$value": "8px",
      "$type": "dimension"
    }
  }
}

Layer	Examples	Purpose
Primitive	blue-500, 16px	Raw values
Semantic	color-primary	Intent-based
Component	button-bg	Component-specific
Resources
Resource	Purpose
references/implementation-research-workflow.md	Research before building
references/design-systems.md	Design system patterns
references/component-library-comparison.md	shadcn, MUI, Radix
references/nielsen-heuristics.md	Heuristic evaluation
references/wcag-accessibility.md	WCAG compliance
references/demographic-inclusive-design.md	Age-specific UX
references/neurodiversity-design.md	ADHD, autism, dyslexia
references/ui-generation-workflows.md	UI from scratch
references/ai-design-tools-2025.md	Figma AI, v0
references/cro-framework.md	Conversion optimization
references/mobile-ux-patterns.md	Mobile UX: thumb zone, navigation, gestures, platform patterns
references/form-design-patterns.md	Form UX: layout, validation, multi-step, accessibility
references/dark-mode-theming.md	Dark mode & multi-theme: tokens, CSS, platform implementation
references/ai-automation-ux.md	AI/automation UX: chatbots, agents, progressive disclosure
references/cultural-design-patterns.md	Cross-cultural design: RTL, CJK, color semiotics, locale UX
references/frontend-aesthetics-2025.md	Visual design trends 2025: glassmorphism, variable fonts, 3D
references/simplification-patterns.md	Interface simplification for non-technical users, digital literacy spectrum
references/modern-ux-patterns-2025.md	Modern UX patterns: command palettes, skeleton states, dark mode, 2026 trends
references/data-visualization-ux.md	Data viz: chart selection, dashboards, accessible charts
references/typography-systems.md	Type scales, font pairing, variable fonts, design tokens
references/performance-ux-vitals.md	Core Web Vitals UX, perceived performance, loading patterns
references/prototype-to-production.md	Prototype-to-production alignment, dashboard QA, design-to-ship checks
references/operational-playbook.md	Decision frameworks
Templates
Template	Purpose
assets/design-brief.md	Design brief
assets/ux-review-checklist.md	UX review
assets/ui-generation/full-ui-spec.md	UI spec
assets/audits/cro-audit-template.md	CRO audit
assets/accessibility/template-wcag-testing.md	WCAG testing
assets/audits/simplification-audit-template.md	Simplification audit
assets/design-systems/template-design-system.md	Design system setup
assets/component-libraries/template-shadcn-ui.md	shadcn/ui integration
assets/component-libraries/template-mui-material-ui.md	MUI / Material UI
assets/interaction-patterns/template-micro-interactions.md	Micro-interactions
Pattern Inspiration
Mobbin — 300k+ screenshots
Page Flows — User flow recordings
Refero Design — Web design references
Related Skills
Skill	Purpose
software-ux-research	Research (use first)
software-frontend	Implementation
software-mobile	Mobile patterns
product-management	Product strategy
Fact-Checking
Use web search/web fetch to verify current external facts, versions, pricing, deadlines, regulations, or platform behavior before final answers.
Prefer primary sources; report source links and dates for volatile information.
If web access is unavailable, state the limitation and mark guidance as unverified.
Weekly Installs
371
Repository
vasilyu1983/ai-…s-public
GitHub Stars
59
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass