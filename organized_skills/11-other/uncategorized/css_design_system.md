---
rating: ⭐⭐⭐
title: css-design-system
url: https://skills.sh/ujon/skills/css-design-system
---

# css-design-system

skills/ujon/skills/css-design-system
css-design-system
Installation
$ npx skills add https://github.com/ujon/skills --skill css-design-system
SKILL.md
CSS Styleguide

Write a CSS design-token styleguide for any web project by assembling ready-to-copy blocks from references/. No build script — you write the files directly with the Write tool.

First action — blocking gate

Before reading the tree, reading references, or writing any file, ask the user which of the seven design systems to use. See Workflow §1 for the exact list and wording. The skill is not allowed to proceed past this gate without either (a) an explicit system name in the user's message, or (b) the user's reply to this question. "Just do it" / silent defaulting to minimal is a bug, not a shortcut.

What gets produced
<output>/
├── index.css              single import entry point — pulls in everything below, in order
├── primitives/            variable layer only (no classes)
│   ├── palette.css        every color token the system exposes
│   ├── size.css           every dimension token (spacing, radius, button heights, transition, shape scales, icon size)
│   ├── typography.css     every type token (families, semantic scale, type roles)
│   ├── motion.css         OPTIONAL — easings, durations, animation timing (beyond --transition)
│   ├── effects.css        OPTIONAL — shadows, elevation, glow, gradients used as visual effects
│   └── index.css          aggregator — imports the files above
├── theme.css              variable layer — semantic mapping (light + dark), incl. overlay/icon semantic colors
├── components/            class layer — plain class names, always written
│   ├── typography.css     .text-* OR role classes (per-system, mutually exclusive)
│   ├── color.css          .bg-* / .text-* / .border-* wrappers for every semantic role (system-agnostic)
│   ├── button.css
│   ├── form.css           field + label + help + input + textarea + select + choice + switch
│   ├── badge.css
│   ├── avatar.css
│   ├── card.css
│   ├── alert.css
│   ├── progress.css
│   ├── tabs.css
│   ├── table.css
│   ├── link.css
│   ├── effects.css        OPTIONAL — .glow / .sweep / .glow-sweep + @keyframes, for systems that ship visual-effect classes
│   └── index.css          aggregator
└── styleguide.html        self-contained preview — CSS inlined via <style> (preview only)


Architectural rules:

Variables are internal to this bundle; consumers interact via classes only. All CSS custom properties live under primitives/ and theme.css. Everything a consumer applies is a class from components/.
One concern per file. Each primitives/*.css owns a single semantic category: colors / dimensions / type / motion / visual effects. There is no extras.css catch-all — if a token doesn't fit an existing file, it gets its own concern-named file.
Size.css holds every dimension token the system exposes — the semantic invariants and any system-specific extensions (e.g., Maximal's --space-scale-*, Material's --md-shape-*, --icon-size, --icon-stroke).
Typography.css holds every type token — semantic --font-* plus every --typography-<role>-*.
Motion.css is for motion tokens beyond --transition — MD3 durations / easings, sweep timing, etc. Omit the file if the system has no additional motion tokens.
Effects.css is for visual-effect values — elevation, box-shadow compositions, glow, sweep gradients. Omit if the system has none.
Theme.css absorbs semantic overlay/icon colors — --overlay-dim, --icon-color-*, etc. These are semantic role mappings, not raw primitives.
Components/effects.css holds effect classes (.glow, .sweep, .glow-sweep) and their @keyframes — colocated with the classes that use them. Only written for systems that ship such effect classes.

Consumers only need to import the top-level index.css; every other file is pulled in by its @import chain.

Semantic tokens

Semantic token names are identical across all systems (--bg, --fg, --space-md, --font-lg, --radius-md, etc.). Only the values differ. System-specific tokens go in the appropriate concern-named primitive file (motion.css, effects.css, etc.) and never collide with the semantic layer.

Basic components

The components/ directory ships twelve per-component stylesheets with plain class names that read only variables from the primitives + theme layer, plus an optional thirteenth (effects.css) for systems that define visual-effect classes. Pick just the ones you need via @import — or import components/index.css for everything.

File	Classes	Purpose
typography.css	.text-xs … .text-2xl (Minimal) or role classes such as .display-large / .headline-medium / .body1 (Material, Carbon, Fluent, Maximal)	Per-system typography utilities (mutually exclusive — a system ships one vocabulary or the other, never both)
color.css	.bg-*, .text-*, .border-* wrapping every non-default semantic role (subtle / muted / elevated / accent / accent-muted / highlight / highlight-muted / danger / success / warning). Default roles (--bg / --fg / --border) apply automatically without a class.	System-agnostic color utilities — lets consumers tint any element using semantic role tokens without reading var(--*) directly
button.css	.btn + .primary / .secondary / .ghost / .danger / .disabled / .sm / .lg	Call-to-action buttons
form.css	.field / .label / .input / .textarea / .select / .help / .choice / .switch	Inputs + choice + toggle, with focus, error, disabled states
badge.css	.badge + solid / soft / outline / danger / success / warning	Labels + status chips
avatar.css	.avatar + .accent / .lg	User avatars
card.css	.card	Grouped content surface
alert.css	.alert + info / success / warning / danger	Inline banners
progress.css	.progress + .progress-fill	Linear progress
tabs.css	.tabs + .tab + .active	Tab bar
table.css	.table	Data tables
link.css	.link	Inline hyperlinks
effects.css (optional)	.glow (+ .strong / .highlight / .danger), .sweep, .glow-sweep + @keyframes effect-sweep + @media (prefers-reduced-motion)	Visual effect classes — only present when the system ships them (e.g. expressive Maximal variants with --glow-* / --sweep-* in primitives/effects.css)

All classes swap correctly when the theme toggles and when the active design system is regenerated. If one of the plain names clashes with an existing class in the consumer's codebase, rename it with a single global search-and-replace before importing.

When to trigger

User phrases:

"make / generate a styleguide", "give me a style guide"
"CSS design tokens", "CSS variables for my theme", "set up theme tokens"
"typography scale", "color palette", "spacing scale", "radius tokens"
"apply Material / Carbon / Fluent / Maximal / Minimal to this project"
"compare design systems", "preview how X looks"
"refresh / regenerate / reset the tokens / the theme"
Any request that ends in writing CSS custom properties for a design system, even in scratch projects

Do not trigger for: editing one component's CSS, fixing a single style rule, or framework-specific build-config work.

Workflow
1. Ask which design system to use — BLOCKING

This step is a hard gate. Do not read references, do not call the Write tool, do not plan files until the system is chosen. Ask the user with this exact shape (or equivalent) and then STOP and wait for their reply:

Which design system would you like? Pick one:

minimal — Monochrome + accents, system font. Clean, quiet baseline.
material — Google MD3. Roboto, tonal palette, shape + elevation scales, full type roles.
carbon — IBM Carbon v11. Plex Sans, sharp, 16-step gray, high-contrast enterprise.
fluent — Microsoft Fluent 2. Segoe UI Variable, Communication Blue, two-layer elevation, 14 type-ramp roles.
maximal — Expressive — vivid purple brand, 27 type roles, 18-step spacing, shadow-heavy.

The only two cases where you may skip the question:

The user named one of the five system keys verbatim (case-insensitive) in their triggering message: minimal / material / carbon / fluent / maximal, or a clearly equivalent proper name ("Material Design", "MD3", "IBM Carbon", "Fluent 2", "Fluent UI"). Use that system.
You are regenerating an existing <output>/ and the top-level index.css header comment already records the chosen system. Reuse it unless the user asked to switch.

Vibe descriptions are NOT system names — still ask. Examples that look like hints but are not: "modern / clean / playful / enterprise / AI vibe / dark-mode / brutalist / pastel / minimal look / corporate / consumer / dev-tool". Present the list and let the user choose. You may add a one-sentence suggestion next to the question (e.g., "AI vibe coding often pairs with maximal for expressive chrome or fluent for crisp Microsoft-style UI — your call.") but the choice is still theirs.

If the user replies with "whatever / default / any / no preference" to the question above: pick minimal, tell them that's what you're using, and offer to switch — do not treat this as authorization to skip the question on the next first-time invocation.

Once the system is chosen, also infer or ask (these rarely warrant a follow-up — infer when possible):

Output directory? Default: styleguide-preview relative to the current working directory.
Preview? On by default. Skip preview files only if the user says things like "tokens only", "no preview", "skip preview", "no html", or "just the CSS".
2. Read only what you need
Always: references/<system>.md — contains one code block per file to write.
If preview is on: references/preview.md — shared HTML + CSS template + component examples.
Only if the user is comparing systems or picking between them: references/design-systems.md.

Do not read references for systems you aren't generating.

3. Write the token files and components.css (always)

Copy blocks verbatim from references/<system>.md:

Source block in reference	Write to
## primitives/palette.css	<output>/primitives/palette.css
## primitives/size.css	<output>/primitives/size.css
## primitives/typography.css	<output>/primitives/typography.css
## primitives/motion.css (if present)	<output>/primitives/motion.css
## primitives/effects.css (if present)	<output>/primitives/effects.css
## theme.css	<output>/theme.css
## components/typography.css	<output>/components/typography.css
## components/effects.css (if present)	<output>/components/effects.css

From references/preview.md:

Source block	Write to
## components/color.css	<output>/components/color.css
## components/button.css	<output>/components/button.css
## components/form.css	<output>/components/form.css
## components/badge.css	<output>/components/badge.css
## components/avatar.css	<output>/components/avatar.css
## components/card.css	<output>/components/card.css
## components/alert.css	<output>/components/alert.css
## components/progress.css	<output>/components/progress.css
## components/tabs.css	<output>/components/tabs.css
## components/table.css	<output>/components/table.css
## components/link.css	<output>/components/link.css
## components/index.css	<output>/components/index.css

Always also write <output>/primitives/index.css. Base template:

@import './palette.css';
@import './size.css';
@import './typography.css';
@import './motion.css';
@import './effects.css';


Include the motion.css / effects.css lines only for systems that define those files. For reference:

motion.css: Material (MD3 motion timings), Fluent (Fluent 2 durations + easing curves), plus any system with additional motion tokens.
effects.css: Material (MD3 elevation), Fluent (two-layer Fluent shadows, light + dark), Maximal (elevation).

Minimal and Carbon have neither — their primitives/index.css is three lines.

Similarly, <output>/components/index.css imports effects.css only for systems that ship one (today: Maximal if the user opts in to glow/sweep-style effects; the stock references don't ship a components/effects.css).

Don't invent values. If something looks wrong in the reference, fix the reference first and then regenerate.

If the user asks for tokens or effects that don't exist in any reference (custom additions like --glow-*, --sweep-*, project-specific brand tokens, gradient tokens, animation keyframes, etc.) — do NOT silently invent them. Instead, after the base system is chosen, ask:

"[Those tokens] aren't in the <system> reference. Two options: (a) One-off — add them to <output>/ for this project only, dropping them into the concern-appropriate file (primitives/effects.css for shadows/glows/gradients, primitives/motion.css for timing, components/effects.css for classes like .glow). They'll be lost the next time you regenerate. (b) Permanent — add them to references/<system>.md first so they survive regeneration. I can do either — which do you want?"

Wait for the answer. Never write unreferenced tokens on your own judgment. When creating new token groups, use concern-named files rather than a catch-all.

The components/ directory is written even when the user asks to skip the preview — components are part of "what the skill produces". Typography is per-system, so it comes from references/<system>.md; the other ten class files are system-agnostic and come from references/preview.md.

Finally, always write the top-level <output>/index.css — the single import entry point consumers use. Template:

/*
 * Design system: {{SYSTEM_NAME}}
 * Generated by the css-design-system skill. Do not edit tokens here — edit
 * the per-layer files instead and this file will keep working.
 *
 * How to use
 *   1. Import this one file from your app stylesheet:
 *        @import 'styleguide-preview/index.css';
 *      — or link it from HTML:
 *        <link rel="stylesheet" href="styleguide-preview/index.css">
 *   2. Theme defaults to light. Toggle dark mode with:
 *        <html data-theme="dark">
 *      Remove the attribute (or set "light") to return to the default.
 *   3. Style your markup with the classes from components/* (e.g. .btn,
 *      .input, .heading-lg). Do not reference --* variables from consumer
 *      code — treat them as internal.
 *
 * Layers (imported in this order — later layers depend on earlier ones):
 *   primitives (variables)
 *     → theme (semantic variables, light + dark)
 *       → components (classes)
 */

@import './primitives/index.css';
@import './theme.css';
@import './components/index.css';


Replace {{SYSTEM_NAME}} with the chosen system's display name (from ## Preview metadata → name in the system reference). Every system uses the same three-line import order — optional files like primitives/motion.css, primitives/effects.css, and components/effects.css are chained through primitives/index.css / components/index.css, so the top-level file never references them directly.

4. Write the preview (on by default)

If the user didn't ask to skip it, write a single self-contained <output>/styleguide.html. No separate styleguide.css file — all CSS lives in a <style> block inside the HTML so the preview opens directly from the filesystem with no link resolution.

Use the ## HTML template from references/preview.md. Replace the {{BUNDLED_CSS}} placeholder with the following blocks concatenated in this exact order:

## Reset from references/preview.md
## primitives/palette.css from references/<system>.md
## primitives/size.css from references/<system>.md
## primitives/typography.css from references/<system>.md
## primitives/motion.css from references/<system>.md (only if present)
## primitives/effects.css from references/<system>.md (only if present)
## theme.css from references/<system>.md
## Base from references/preview.md
## components/typography.css from references/<system>.md
## components/color.css from references/preview.md
Remaining ten system-agnostic ## components/*.css blocks from references/preview.md (button, form, badge, avatar, card, alert, progress, tabs, table, link — skip index.css since it's @import-only and those imports won't resolve inline)
## components/effects.css from references/<system>.md (only if present)
## Preview chrome CSS from references/preview.md

Then substitute the remaining placeholders per:

Placeholder	Source
{{SYSTEM_NAME}}	## Preview metadata → name, in the system reference
{{SYSTEM_DESCRIPTION}}	## Preview metadata → description
{{FONT_FAMILY_ROWS}}	Two fixed rows — one sample each for --font-sans and --font-mono. Pattern in preview.md.
{{TYPOGRAPHY_ROWS}}	Mutually exclusive: Minimal (the only system with type_roles: none) emits six rows — one per --font-xs … --font-2xl. Every other system emits one row per role listed in its Preview metadata. Never both. Patterns in preview.md.
{{SEMANTIC_SWATCHES}}	Exhaustive — one swatch per key in the light theme.css :root block.
{{PRIMITIVE_SWATCHES}}	Exhaustive — one swatch per every --* variable in primitives/palette.css (every ramp step + every accent), in source order. No skipping.
{{SPACING_ROWS}}	Exhaustive — one row per spacing token declared anywhere in primitives/size.css. Includes --space-* and any system-specific extensions like --space-scale-*.
{{RADIUS_BOXES}}	Exhaustive — one box per corner-radius / shape token declared in primitives/size.css (--radius-*, plus any --md-shape-* or similar if present).
{{BUTTON_SIZE_ROWS}}	Three value rows for --btn-sm/md/lg. Pattern in preview.md.
{{MOTION_ROW}}	One row with the --transition value and a hover demo.
{{MOTION_SECTION}}	Full section block listing every token in primitives/motion.css (easings + durations) with a hover demo per easing. Empty string if the system has no primitives/motion.css.
{{EFFECTS_SECTION}}	Full section block visualizing every token in primitives/effects.css — shadows as elevated boxes, glows as glowing boxes, gradients/sweeps rendered live. Empty string if the system has no primitives/effects.css. Subsumes the old {{ELEVATION_SECTION}}.
{{COMPONENTS_BLOCK}}	Verbatim from ## Components HTML in preview.md.

Completeness test: after substitution, every --* variable declared anywhere in primitives/* + theme.css must be visible somewhere in the preview. The [data-var] spans are refreshed by the theme-toggle script, so variable values stay live when the user switches light ↔ dark.

5. If existing files would be overwritten

Check whether <output>/ has content. If it does and the user hasn't said "overwrite", ask before proceeding. Never clobber silently.

6. Report

After writing, tell the user:

The file paths written.
The chosen system.
Whether preview was included.
How to open the preview (open <output>/styleguide.html on macOS, or equivalent).
Invariants across systems

Every system's bundle is required to declare the following minimum set of semantic token names. Systems are free to add more tokens in the same files — the invariant is the names must exist, not that these are the only names. These are implementation details; classes in components/ read them, consumers don't touch them directly.

From theme.css: --bg, --bg-subtle, --bg-muted, --bg-elevated, --fg, --fg-muted, --fg-subtle, --border, --border-strong, --accent, --accent-muted, --highlight, --highlight-muted, --danger, --success, --warning. (Plus any semantic role mappings the system adds — e.g. --overlay-dim, --icon-color-*.)

From primitives/typography.css: --font-sans, --font-mono, --font-xs … --font-2xl. (Plus any --typography-<role>-* tokens the system adds.)

From primitives/size.css: --space-xs … --space-xl, --radius-sm/md/lg, --btn-sm/md/lg, --transition. (Plus any --space-scale-*, --md-shape-*, icon sizing, etc.)

Where does a new token belong?
Token flavor	File
Raw color (ramp step, brand accent, named hue)	primitives/palette.css
Any length / duration / numeric scale (spacing, radius, sizing, default transition)	primitives/size.css
Font family / size / weight / line / letter / role	primitives/typography.css
Motion token beyond --transition (easing curve, named duration)	primitives/motion.css
Shadow, elevation, glow, gradient used as visual effect	primitives/effects.css
Semantic color role mapping (--overlay-dim, --icon-color-main, …)	theme.css
Effect class (.glow, .sweep, .glow-sweep) + its @keyframes	components/effects.css

There is no extras.css and no catch-all. If a new token doesn't fit an existing file, create a new concern-named primitive file (primitives/<concern>.css) rather than reaching for a generic bucket.

Adding a new system

If the user wants a system not in the list (Fluent, Ant Design, Atlassian, Tailwind defaults, custom house style…):

Add references/<new-system>.md using the section structure: primitives/palette.css / primitives/size.css / primitives/typography.css / primitives/motion.css (optional) / primitives/effects.css (optional) / theme.css / components/typography.css / components/effects.css (optional) / Preview metadata / Source.
Pull values from the upstream spec; note the source URL.
Classify each token using the table above. Omit the optional files entirely when not used.
In components/typography.css, emit one class per type role (or .text-xs...text-2xl if the system has no roles). Classes must read only from variables defined in this system's primitives + theme.
Run the same workflow against the new reference.

Keep the minimum semantic token names intact — everything else is free to vary per system.

References
references/design-systems.md — selection guide and invariants.
references/preview.md — shared reset + base + preview CSS + HTML template + 10 system-agnostic components.
references/<system>.md × 5 — per-system CSS blocks including components/typography.css. Currently: minimal.md, material.md, carbon.md, fluent.md, maximal.md.
What this skill does not do
No automatic project integration. The output sits in the directory you pass. Wiring is one line: @import '<output>/index.css'; from a root stylesheet (or a <link> tag in HTML). The top-level index.css chains primitives → theme → components for you.
No script runner. Generation is manual — open references, write files. Keeps the skill light and transparent.
No namespace guarantee. components/ uses plain class names (.btn, .input, .card, …). If any clash with your codebase, rename via global search-and-replace before importing.
Utility classes are limited to color and typography. components/color.css ships .bg-* / .text-* / .border-* for every semantic role because tinting is universal. components/typography.css ships per-system type utilities. Spacing and radius stay internal — no .p-md / .rounded-md layer. If you need a custom surface with specific padding / radius, build it in your own CSS, composed from the component classes.
Weekly Installs
9
Repository
ujon/skills
GitHub Stars
1
First Seen
7 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass