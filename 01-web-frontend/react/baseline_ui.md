---
rating: ⭐⭐
title: baseline-ui
url: https://skills.sh/ibelick/ui-skills/baseline-ui
---

# baseline-ui

skills/ibelick/ui-skills/baseline-ui
baseline-ui
Installation
$ npx skills add https://github.com/ibelick/ui-skills --skill baseline-ui
Summary

Enforces design and interaction constraints to prevent common UI anti-patterns in Tailwind CSS projects.

Validates animation durations (max 200ms for interactions), restricts animations to compositor properties only, and enforces prefers-reduced-motion respect
Requires accessible component primitives (Base UI, React Aria, Radix) for interactive elements and enforces keyboard behavior standards
Checks typography rules including text-balance for headings, tabular-nums for data, and prevents arbitrary letter-spacing modifications
Prevents layout anti-patterns like h-screen (use h-dvh instead), arbitrary z-index values, and animating layout properties
Reviews files against all constraints and outputs exact violations with code-level fixes
SKILL.md
Baseline UI

Enforces an opinionated UI baseline to prevent AI-generated interface slop.

How to use

/baseline-ui Apply these constraints to any UI work in this conversation.

/baseline-ui <file> Review the file against all constraints below and output:

violations (quote the exact line/snippet)
why it matters (1 short sentence)
a concrete fix (code-level suggestion)
Stack
MUST use Tailwind CSS defaults unless custom values already exist or are explicitly requested
MUST use motion/react (formerly framer-motion) when JavaScript animation is required
SHOULD use tw-animate-css for entrance and micro-animations in Tailwind CSS
MUST use cn utility (clsx + tailwind-merge) for class logic
Components
MUST use accessible component primitives for anything with keyboard or focus behavior (Base UI, React Aria, Radix)
MUST use the project’s existing component primitives first
NEVER mix primitive systems within the same interaction surface
SHOULD prefer Base UI for new primitives if compatible with the stack
MUST add an aria-label to icon-only buttons
NEVER rebuild keyboard or focus behavior by hand unless explicitly requested
Interaction
MUST use an AlertDialog for destructive or irreversible actions
SHOULD use structural skeletons for loading states
NEVER use h-screen, use h-dvh
MUST respect safe-area-inset for fixed elements
MUST show errors next to where the action happens
NEVER block paste in input or textarea elements
Animation
NEVER add animation unless it is explicitly requested
MUST animate only compositor props (transform, opacity)
NEVER animate layout properties (width, height, top, left, margin, padding)
SHOULD avoid animating paint properties (background, color) except for small, local UI (text, icons)
SHOULD use ease-out on entrance
NEVER exceed 200ms for interaction feedback
MUST pause looping animations when off-screen
SHOULD respect prefers-reduced-motion
NEVER introduce custom easing curves unless explicitly requested
SHOULD avoid animating large images or full-screen surfaces
Typography
MUST use text-balance for headings and text-pretty for body/paragraphs
MUST use tabular-nums for data
SHOULD use truncate or line-clamp for dense UI
NEVER modify letter-spacing (tracking-*) unless explicitly requested
Layout
MUST use a fixed z-index scale (no arbitrary z-*)
SHOULD use size-* for square elements instead of w-* + h-*
Performance
NEVER animate large blur() or backdrop-filter surfaces
NEVER apply will-change outside an active animation
NEVER use useEffect for anything that can be expressed as render logic
Design
NEVER use gradients unless explicitly requested
NEVER use purple or multicolor gradients
NEVER use glow effects as primary affordances
SHOULD use Tailwind CSS default shadow scale unless explicitly requested
MUST give empty states one clear next action
SHOULD limit accent color usage to one per view
SHOULD use existing theme or Tailwind CSS color tokens before introducing new ones
Weekly Installs
10.5K
Repository
ibelick/ui-skills
GitHub Stars
1.6K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass