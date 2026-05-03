---
title: design-system-creation
url: https://skills.sh/aj-geddes/useful-ai-prompts/design-system-creation
---

# design-system-creation

skills/aj-geddes/useful-ai-prompts/design-system-creation
design-system-creation
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill design-system-creation
SKILL.md
Design System Creation
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

A design system is a structured set of components, guidelines, and principles that ensure consistency, accelerate development, and improve product quality.

When to Use
Multiple product interfaces or teams
Scaling design consistency
Reducing redundant component development
Improving design-to-dev handoff
Creating shared language across teams
Building reusable components
Documenting design standards
Quick Start

Minimal working example:

Design System Structure:

Foundation Layer:
  Typography:
    - Typefaces (Roboto, Inter)
    - Font sizes (scale: 12, 14, 16, 20, 28, 36, 48)
    - Font weights (Regular, Medium, Bold)
    - Line heights and letter spacing

Colors:
  - Primary brand color (#2196F3)
  - Secondary colors
  - Neutral palette (grays)
  - Semantic colors (success, error, warning)
  - Dark mode variants

Spacing:
  - Base unit: 4px
  - Scale: 4, 8, 12, 16, 24, 32, 48, 64px
  - Apply consistently across UI

Shadows & Elevation:
  - Elevation 0 (flat)
  - Elevation 1, 2, 4, 8, 16 (increasing depth)
  - Used for modals, cards, overlays
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Design System Components	Design System Components
Component Documentation	Component Documentation
Design System Governance	Design System Governance
Design System Documentation	Design System Documentation
Best Practices
✅ DO
Start with essential components
Document every component thoroughly
Include code examples
Test components across browsers
Include accessibility guidance
Version the design system
Have clear governance
Communicate updates proactively
Gather feedback from users
Maintain incrementally
❌ DON'T
Create too many components initially
Skip documentation
Ignore accessibility
Make breaking changes without migration path
Allow inconsistent implementations
Ignore user feedback
Let design system stagnate
Create components without proven need
Make components too prescriptive
Ignore performance impact
Weekly Installs
342
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass