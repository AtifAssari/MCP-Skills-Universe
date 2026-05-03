---
title: all-in-one-ui-ux-design
url: https://skills.sh/luisjppm/skills/all-in-one-ui-ux-design
---

# all-in-one-ui-ux-design

skills/luisjppm/skills/all-in-one-ui-ux-design
all-in-one-ui-ux-design
Installation
$ npx skills add https://github.com/luisjppm/skills --skill all-in-one-ui-ux-design
SKILL.md
All-in-One UI/UX Design

Use this skill as the default end-to-end UI/UX system. Keep this file focused on workflow. Load reference files only when needed.

Goal: deliver memorable interfaces that are production-ready, accessible, and maintainable.

Start Here

Collect the minimum context before generating or reviewing code:

Product context: product type, audience, tone, and brand constraints.
Scope: full page/app, component set, redesign, or UI audit.
Platform and stack: web/mobile + framework/library choices.
Required states: loading, empty, error, success, disabled, and edge cases.
Delivery target: prototype, production code, audit findings, or design system spec.

If details are missing, ask 1-3 focused questions. If the user prefers speed, proceed with explicit assumptions.

Mode Selection

Pick the mode that matches intent:

build: design and implement new UI.
redesign: keep functionality, replace visual and interaction layer.
audit: review existing UI and return actionable findings.
design-system: define tokens, type scale, and component primitives before coding.
flow: design multi-screen journeys (onboarding, checkout, settings, dashboards).

For mixed requests, run design-system -> build -> audit in sequence.

Default Recommendations

Use these defaults unless the user asks otherwise:

Stack selection: Use the stack already present in the codebase. If no stack is present and the task is web, default to html-tailwind. If no stack is present and the task is mobile, use platform-native patterns.
Audit depth: Use full checklist audit by default. Use quick audit only when the user explicitly asks for speed over depth.
Creativity: Do not rely on rigid templates as the primary output. Use a bespoke direction per project, with reusable principles instead of cloned layouts. Use assets/primitives/ as composable scaffolding, not final visual identity.
Reference Loading Map

Load only what the task needs:

File	Load when
references/creative-direction.md	Choosing style direction, typography personality, palette mood, layout composition, and visual differentiation
references/system-build-playbook.md	Building implementation plans, selecting stacks, applying UX priority rules, and using final delivery checklists
references/web-interface-guidelines.md	Auditing UI code for accessibility, interaction, performance, copy quality, and anti-pattern detection
Asset Kit

Use these optional assets when implementation speed is needed without sacrificing originality:

Asset	Use for
assets/primitives/tokens.css	Typography, color, spacing, radius, elevation, and semantic token scaffold
assets/primitives/motion.css	Motion tokens, entry effects, and reduced-motion-safe behavior
assets/primitives/layout.css	Responsive layout primitives (container, stack, cluster, grid, section, surface)
assets/primitives/component-states.css	Accessible default states for buttons, fields, and cards
assets/blueprints/semantic-shell.html	Minimal semantic page skeleton for rapid prototyping

Asset rules:

Copy only what is needed.
Retheme tokens before final delivery.
Recompose layouts per project; never ship blueprint defaults unchanged.
Core Principles
Commit to a clear aesthetic direction. Do not produce generic template-looking UI.
Keep style and interaction consistent across the entire surface.
Prioritize accessibility and usability before decorative polish.
Use motion intentionally; communicate state changes, do not add noise.
Build for responsive behavior and real content from the first pass.
Favor readable, maintainable code and tokenized styling over ad hoc values.
Non-Negotiable Quality Bar

Apply these rules in every mode:

Typography must feel intentional. Avoid default stacks and repetitive safe choices.
Color must be cohesive. Use design tokens or CSS variables for primary, secondary, accent, and semantic states.
Interactive elements must expose visible hover and keyboard focus states.
Touch targets must be at least 44x44px on touch interfaces.
Respect reduced-motion preference and avoid expensive animation properties.
Provide complete state coverage: normal, hover, focus, active, disabled, loading, empty, error, success.
Prevent layout shifts and clipping with explicit media sizing and robust text overflow handling.
Avoid anti-patterns listed in references/web-interface-guidelines.md.
Anti-Generic Design Checks (Required)

Before final delivery, fail the output if any of these remain:

Default-looking typography choices with no clear intent.
Generic gradient-heavy or template-first visual direction with weak brand fit.
Boilerplate page composition that could belong to any product with minimal changes.
Decorative motion that does not communicate hierarchy, feedback, or state.
No memorable differentiator in type, layout, interaction, or visual texture.
End-to-End Workflow
1. Understand and Frame
Translate request into problem statement and success criteria.
Extract constraints: brand, compliance, performance, deadlines.
Define deliverables and acceptance criteria before coding.
2. Choose a Design Direction
Pick one primary visual direction and one secondary supporting influence.
Define mood words, contrast level, texture strategy, and motion character.
Lock direction with a concise design brief before component implementation.

Use references/creative-direction.md for direction options and anti-generic guardrails.

3. Define the Design System

Create a compact spec:

Color tokens: background, surface, text, muted, border, primary, accent, danger, success.
Typography system: display/headline/body/caption styles and line-height rules.
Spacing and radius scales.
Elevation/shadow system and border treatments.
Motion tokens: durations, easing, and reduced-motion fallbacks.
Component primitives: button, input, select, card, modal, tooltip, toast, table.

Use references/system-build-playbook.md for rule priority and stack-specific guidance.

4. Build Layout and Interaction Architecture
Draft responsive structure first (mobile-first breakpoints unless specified otherwise).
Define hierarchy, grouping, and scanning paths.
Assign interaction patterns: navigation, filtering, validation, feedback.
Plan edge states early to avoid late-stage regressions.
5. Implement by Stack
Respect user-selected stack. If unspecified, apply the defaults from the Default Recommendations section above.
Keep implementation style-consistent with the design system.
Use semantic HTML and accessible component APIs.
Prefer composable primitives and reusable tokens over one-off classes.
If using the Asset Kit, customize tokens, composition, and interaction details before delivery.
6. Audit Before Delivery

Run self-review against references/web-interface-guidelines.md:

Accessibility and semantic correctness.
Focus/keyboard and touch quality.
Responsive behavior and overflow handling.
Motion/performance and hydration safety.
Copy clarity and interaction labels.
Audit Mode Output Contract

When request intent is review/audit/check:

Findings first, ordered by severity.
Group by file with file:line locations.
Keep each finding terse and actionable.
Mention pass status only when file has no issues.
Include residual risks or missing test coverage.

Default behavior:

Run strict/full audit against the complete guideline set.
Switch to quick audit only when user asks for lightweight review.

Format:

## path/to/file.tsx

path/to/file.tsx:42 - issue summary
path/to/file.tsx:77 - issue summary

## path/to/another.tsx

pass

Build Mode Output Contract

When request intent is implementation:

Provide final code or patch.
Summarize design direction in 2-4 bullets.
Confirm key accessibility and responsive decisions.
List known tradeoffs and follow-up improvements.
Rapid Prompt Pattern

Use this structure internally when requirements are vague:

"Who is this interface for and what is the core action?"
"What emotional tone should the UI convey?"
"What stack or platform constraints apply?"
"What quality constraints are mandatory (a11y, perf, brand, localization)?"

If user does not answer, continue with assumptions and state them clearly.

Completion Checklist

Before final delivery, confirm:

Visual direction is distinctive and coherent.
All critical interactions have hover/focus/active/disabled states.
Accessibility checks pass for labels, semantics, focus, and contrast.
Mobile and desktop layouts are verified.
Performance-sensitive behavior (images, animations, lists) is handled.
Copy and error states are specific and user-actionable.
Weekly Installs
50
Repository
luisjppm/skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass