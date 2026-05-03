---
rating: ⭐⭐
title: design-taste
url: https://skills.sh/customware-ai/skills/design-taste
---

# design-taste

skills/customware-ai/skills/design-taste
design-taste
Installation
$ npx skills add https://github.com/customware-ai/skills --skill design-taste
SKILL.md
Design Taste Skill
What this skill is

This skill is the visual quality bar shared across every build. It's read alongside frontend-design (which handles mechanics — template contract, brand theming, BrandMark) and any vertical skill (which handles workflow structure — CPQ stages, Trades sections, CRM entities). design-taste encodes the taste layer: how to lay things out so they feel balanced, how to pick a coherent visual language, how to build components with restraint, and how to avoid the patterns that make AI builds look generic.

The reason most one-shot AI output looks mediocre is not that the agent is incapable of any individual decision. It's that the agent makes decisions component-by-component in isolation, and each "reasonable" decision drifts slightly from the last. Twelve reasonable-but-uncoordinated decisions produce visual chaos. This skill replaces that pattern with a coordinated system: declare the visual language upfront, then implement every component as a consumer of that language.

Read this skill on every build. Apply it whether the build is a CPQ for an industrial customer, a CRM for a professional services firm, a Trades app for a contractor, or a YOLO consumer SPA with no vertical at all. The taste layer is universal.

A. Foundations — what good design feels like

These principles describe the qualities the build should have. They're abstract on their own; the system, patterns, and recipes that follow are how each principle gets implemented.

1. Visual balance

Most app screens are NOT centered hero pages. Content aligns left, scans top-to-bottom, with the focal element occupying the upper third or upper-left of the main content area. Asymmetric balance — a heavy element offset by a lighter cluster of supporting elements — reads as more sophisticated than centered symmetry, which is reserved for empty states, error pages, and onboarding.

A balanced layout has:

One focal point per screen. The primary score, the day's plan, the active document, the highlighted record. One — not three.
Supporting elements that orbit, don't compete. Secondary information sits to the side or below at lower visual weight (smaller, lighter, less color).
Negative space as a design element. Empty space isn't unfilled — it's part of what makes the focal point feel focal.
2. Hierarchy

Hierarchy is how the user knows what to look at first, second, third. It's built from four levers — size, weight, color, spacing — and the rule is to use ONE, occasionally two, never four at once.

Size hierarchy: primary number 32px, title 20px, supporting label 14px, metadata 12px. Four sizes total. A fifth means you're trying to differentiate something that doesn't deserve differentiation.
Weight hierarchy: semibold (600) for primary numbers and headings, medium (500) for titles and emphasized labels, regular (400) for body. Three weights, used systematically.
Color hierarchy: foreground (primary text), muted (secondary), subtle (tertiary). Three text colors. The brand color is reserved for action, not for hierarchy.
Spacing hierarchy: larger gaps (32-40px) separate major sections; medium gaps (16-24px) separate cards within a section; small gaps (8-12px) separate elements within a card.

When two elements need to feel different in importance, change ONE lever — usually size or weight. Don't change all four. Visual noise comes from over-differentiation.

3. Restraint

Restraint is the signature of premium design. AI defaults toward the opposite — using brand colors everywhere, adding gradients, layering shadows, multiplying decorative elements. Each individually feels like "more polish"; together they feel like a discount template.

The single most important restraint rule: the brand or accent color appears in roughly 8-10% of pixels — no more. Primary buttons, the active state border, the score badge fill, maybe one or two focal accents. Body text is foreground. Icons are foreground or muted. Most surfaces are neutral.

Other restraint rules:

No more than one primary action per screen. Two if absolutely necessary, with one clearly subordinate.
No more than one focal card per screen. Other cards are supporting context.
No more than 2-3 colors in any chart. Multi-colored bars and lines are noise.
No more than 4 type sizes total in the entire app. Hard ceiling.
No drop shadows for elevation. Use 1px borders. Shadows immediately read as bargain-template.

Restraint produces calm. Calm is what makes the user trust the app.

4. Rhythm

Rhythm is the consistent spacing and sizing pattern that makes the app feel like one designer made it. It comes from using a defined scale — radius scale, spacing scale, type scale — and never improvising values.

8px grid for spacing. All spacing values are multiples of 4 (4, 8, 12, 16, 20, 24, 32, 40). Invisible to the user but felt in the regularity of the layout.
Generous default. When in doubt about whether a gap should be 12px or 16px, choose 16px. AI defaults to dense layouts; override the default. Premium aesthetics breathe.
Consistent radius by hierarchy. Cards use one radius, chips use another, badges use another. Same hierarchy = same radius. Don't mix.
Aligned baselines. Text in the same row aligns vertically. Headings align with the icons next to them. Card content has consistent padding all around.

Rhythm is invisible when present and obvious when absent. It's what separates "looks fine" from "feels right."

B. System — how to encode visual language

The principles in Section A describe what the build should feel like. This section describes the mechanics.

Core mandate: token-first, then archetype, then components

Every build follows this order:

Pick or derive an archetype based on the app's purpose, customer, and feeling
Declare the complete token set in app.css — colors, typography, radius, borders, elevation, spacing
Build every component as a consumer of those tokens — no hardcoded hex values, no improvised type sizes, no ad-hoc radii

This single ordering eliminates 60% of AI design failures. It physically prevents the agent from inventing a fourth radius or a sixth type size mid-build. The constraint produces coherence; the coherence produces taste.

Picking the archetype

An archetype is a complete preset for the visual language — a palette flavor, a typography pairing, a radius scale, an elevation style. All archetypes share the same structural shape (8 token categories); they differ only in values.

Selection rules:

DOMAIN.md has brand colors → use the brand colors for the palette layer; pick the archetype whose structural feel matches the customer (industrial CPQ → Enterprise; wellness clinic → Wellness; creative agency CRM → Creator). The brand colors override the archetype's palette; everything else (typography, radius, elevation) comes from the archetype.
No DOMAIN.md and no clear emotional cue → use Neutral / Default. It's the safe choice and works for any app.
No DOMAIN.md but a clear cue from the task → match the archetype to the cue. "Build me a habit tracker" → Wellness. "Build me an expense tracker" → Finance & Trust. "Build me a journal" → Creator & Social.
Multiple cues → pick the most dominant. Don't blend archetypes.

Do not invent a new archetype mid-build. Pick one, declare its tokens, build against them.

For full archetype catalog and the encoded token sets (Neutral / Default + Wellness & Health in v0.1, others pending validation), see references/archetypes.md. Read this reference at the moment of writing the token block to app.css.

C. Patterns — how to lay things out

These are universal layout patterns that work across verticals and archetypes. The vertical skill (if present) defines what content goes in each region; this skill defines how the regions are arranged and how content within them is composed.

Layout patterns

Focal layout (most common for primary screens). Sidebar + main content area with focal card on top + row stack below + supporting right panel. Used for CRM home, CPQ project list, Trades job list, consumer SPA home.

Detail layout (for viewing/editing a single record). Header (back nav + title + primary actions) + tab nav + body (form or detail data) + optional right panel for related items. Used for the document view in CPQ, the project detail in Trades, the contact/deal detail in CRM.

List/index layout (for browsing many records). Title + primary action above; search + filter chips below; row stack as the body. Optional right panel for advanced filters or a preview of the selected row.

Form layout. Single column by default. Two-column field layouts only when fields are conceptually paired (first/last name, start/end date). Primary save action goes at the bottom-right; cancel is to its left.

Mobile-first responsiveness

Three-column layouts collapse to single-column under 768px. The right panel either disappears, becomes a tab, or becomes a section below the main content. The sidebar becomes a drawer triggered by a menu button.

For consumer SPAs likely used primarily on phones, build for mobile first and let the desktop layout grow from it. For business apps used primarily on desktops, build for desktop first and let mobile collapse cleanly.

State patterns — every interactive element has all four states

Default. Resting appearance. What the user sees on first paint.

Hover. Subtle change signaling interactivity — slight background tint, slight border darken. Never a dramatic visual jump. Cursor changes to pointer.

Active / pressed. Slightly more pronounced than hover; signals the click is registering.

Disabled. Reduced opacity (60-70%), no hover effect, no cursor change. The user should immediately understand "this is here but currently unavailable."

Beyond these four interactive states, every list, every form, every async action has these UI states:

Empty. Never leave a list view blank. Empty state has: optional muted illustration, title ("No projects yet"), description ("Create your first project to get started"), and a primary action button when applicable.

Loading. Skeletons matching the actual content shape, not generic spinners. A row skeleton is a tinted rectangle the size of a row. Spinners are reserved for short async actions (button submit) and even then a loading state on the button itself is better.

Error. Constructive, never dead-end. Title ("Couldn't load projects"), description ("Check your connection and try again"), action ("Retry"). Never a raw error message.

Success. After a destructive or significant action, confirm via a toast at the bottom-right that auto-dismisses after 3-4 seconds. For inline actions (toggling a checkbox), the visible state change IS the confirmation — no toast needed.

Microinteractions

Microinteractions are small UI responses that make the app feel alive. Universal subtleties:

Hover transitions: 150-200ms ease-out on background, border, color changes
Focus indicators: visible focus ring on keyboard nav (2px outline in --primary with 2px offset)
Optimistic UI: update immediately, roll back if the action fails
Button press feedback: subtle scale or color shift on press
Animated state transitions: 150ms cross-fade or slide between sections
Toast entry animation: slide in from bottom-right over 200ms

If a transition is noticeable as a transition, it's too long. Aim for "I didn't notice it but the app felt good."

D. Component recipes

Components consume the active token set. Same recipe across all archetypes; different tokens; different visual results; always coherent.

For exact specs of all component recipes (Primary Button, Secondary Button, Tertiary Button, Chip Active/Inactive, Status Badge, Row Default/Hover/Selected, Card, Toggle, Form Input, Section Header, Empty State, Toast, Loading Skeleton — 16 recipes total), see references/components.md.

Read this reference whenever building any UI component. Each recipe specifies background, text, typography, radius, padding, height, hover, disabled, and transition specs — implementable directly without design decisions.

E. Anti-patterns

These are the failures that show up in 90% of one-shot AI builds. Naming them explicitly is the most effective preventive measure.

The full list of 18 anti-patterns — covering brand-color overuse, drop shadows, mixed radii, fifth type sizes, invented status colors, colored-text-on-tinted-backgrounds, dense layouts, gradients, decorative gray icons, internal dividers, centered-everything layouts, loading spinners, unexplained disabled buttons, uniform field widths, modal overuse, toast overuse, decorative emojis, regular-weight page titles — lives in references/anti-patterns.md.

Read this reference before starting the build (to internalize what to avoid) AND before completion (to scan the build for violations).

F. Build order

The agent MUST follow this order. Do not start building components before the token block is complete in app.css.

Pick the archetype. Read references/archetypes.md. Match to the task description, DOMAIN.md (if present), and customer feeling. Note the choice in a code comment at the top of app.css: /* design-taste archetype: Wellness & Health */
Write the complete token block to app.css. All 8 token categories (surfaces, palette, status, text, typography, radius, borders, elevation, spacing) declared as CSS variables under :root. No exceptions.
Set light mode in BOTH places. app.css AND the JavaScript ThemeProvider default. Failure to do this means the app ships in dark mode regardless of tokens. Most-skipped step in the entire pipeline.
Build the layout shell. Sidebar (if applicable), header, main content area. Use --surface-stage for the page background, --surface-navigation for the sidebar. NO hardcoded colors — every value comes from a token.
Build the focal element on the primary screen. The focal card, score, dashboard centerpiece — whichever is the screen's anchor. Use --surface-focal (white), generous padding, display-size primary text.
Build supporting elements. Row stacks, secondary cards, section headers, sidebar navigation items. Open references/components.md and follow each recipe exactly.
Build interactive states. Every interactive element has hover, active, selected, disabled. Every form has loading, error, success.
Build empty/loading/error/success states. Every list view has an empty state. Every async action has a loading and error state. Every significant action confirms.
Add microinteractions. Hover transitions, focus indicators, optimistic UI, button press feedback, toast animations.
Anti-pattern scan. Open references/anti-patterns.md. Scan the build against each item. Fix any violations.
Side-by-side check (iterative builds only). When the prototype already exists and this is a follow-up build, compare the new screen to the closest existing peer screen using playwright-interactive-sandbox. Match radius, typography, spacing, badge style, button shape. The existing app's visual language overrides this skill's defaults — match the existing.
G. Verification

Before completion, run through this checklist:

Token block complete. All 8 token categories declared in app.css. No hardcoded hex values anywhere except inside the token block.
Archetype consistent. Every component pulls from the declared tokens. No off-archetype values.
Light mode in both places. app.css AND ThemeProvider default. App ships in light mode.
Hierarchy clear. Each screen has one focal point. Supporting elements are visually subordinate.
Restraint visible. Brand color used in <10% of pixels. No more than one primary action per screen. No drop shadows.
Rhythm consistent. All spacing on the 4/8 scale. Same hierarchy = same radius. Aligned baselines.
All four states present for every interactive element (default/hover/active/disabled) and every async surface (default/loading/empty/error).
Anti-pattern scan clean. All 18 anti-patterns checked (references/anti-patterns.md). No violations.
Side-by-side check passed (iterative builds). New screen visually matches existing peer screen.
H. v0.1 scope and validation plan

This is v0.1. Validated on zero builds.

Encoded in v0.1:

2 archetypes (Neutral / Default + Wellness & Health) — see references/archetypes.md
16 component recipes — see references/components.md
18 anti-patterns — see references/anti-patterns.md
4 layout patterns + 4 interactive states + 4 async UI states + 6 microinteraction guidelines

Pending in future versions:

8 additional archetypes (Productivity, Finance, Creator, Lifestyle, Education, Utility, Reading, Enterprise)
Edge components (date picker, multi-step wizards, complex modals, data tables, calendars, kanban boards)
Animation specifics for transitions beyond microinteractions
Detailed responsive breakpoint behavior
Dark mode (deferred — get light mode reliable first)

Validation plan:

Run a YOLO build with this v0.1 ("build me a habit tracker") using the Wellness archetype. Compare to the vision-board reference.
Run an existing-vertical build (e.g., re-run an HB Material Handling CPQ build) using the Default archetype with brand colors from DOMAIN.md overriding the palette. Compare against current quality.
Identify gaps in both runs. Update to v0.2.
Encode a third archetype only after both validation builds reliably hit their respective quality targets.

Do not generalize this skill across all 10 archetypes until the encoded ones produce reliable output.

How this fits the skill stack
Skill	Reads when	What it provides
frontend-design	Always	Template contract, BrandMark, brand theming mechanics, must-not-skip rules
design-taste	Always	Visual quality bar — foundations, archetypes, recipes, anti-patterns, polish
cpq-builder	When task is CPQ-shaped	CPQ-specific section structure, quote document, RBAC patterns
trades-builder	When task is trades-shaped	Trades-specific section structure, job summary, payment flow
crm-builder	When task is CRM-shaped	Entity model, pipeline view, list/detail patterns
erp-builder	When task is ERP-shaped	Inventory model, purchase order flow

Every build reads frontend-design + design-taste. Verticals are additive. For YOLO consumer SPAs, no vertical is read — design-taste carries most of the visual decisions.

Weekly Installs
9
Repository
customware-ai/skills
GitHub Stars
1
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass