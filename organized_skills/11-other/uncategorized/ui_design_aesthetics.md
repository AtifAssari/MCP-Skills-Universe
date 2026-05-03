---
rating: ⭐⭐
title: ui-design-aesthetics
url: https://skills.sh/nickcrew/claude-ctx-plugin/ui-design-aesthetics
---

# ui-design-aesthetics

skills/nickcrew/claude-ctx-plugin/ui-design-aesthetics
ui-design-aesthetics
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill ui-design-aesthetics
SKILL.md
UI Design & Aesthetics

Expert guidance for designing and implementing beautiful, high-performance user interfaces. This skill enforces distinctive aesthetics while ensuring technical excellence through progressive disclosure and dynamic loading.

Core Capabilities
Aesthetic Direction: avoiding "AI slop" by enforcing distinctive typography, color, and depth.
Performance Architecture: ensuring UI components load dynamically to minimize initial payload.
Progressive Disclosure: designing interfaces that reveal complexity only when needed.
API Contract Validation: ensuring frontend components align with backend data structures.
Usage

Use this skill when:

Designing a new feature or application from scratch.
Refactoring an existing UI to be more modern and performant.
Implementing complex dashboards or data-heavy interfaces.
Quick Reference
Topic	Reference
Aesthetic Rules (Typography, Color, Motion)	skills/ui-design-aesthetics/references/aesthetics.md
Progressive Disclosure & Dynamic Loading	skills/ui-design-aesthetics/references/progressive-disclosure.md
API Contract Validation	skills/ui-design-aesthetics/references/api-contracts.md
Design Workflow
Analyze & Select Aesthetic: Choose a cohesive theme (Swiss, Neo-Brutalism, etc.) and reject generic defaults.
Architect for Performance: Identify heavy components for lazy loading (React.lazy, dynamic imports).
Design Interaction: Plan staggered reveals and interaction-based loading.
Validate Data: Define TypeScript interfaces or Zod schemas for API responses.
Implement: Write the code using utility classes (Tailwind) and enforcing the design system.
Performance Requirements
Initial Payload: Critical path CSS/JS only.
Dynamic Loading: Secondary components MUST load on interaction or visibility (IntersectionObserver).
Latency: Design optimistic UI states for interactions > 100ms.
Weekly Installs
106
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass