---
rating: ⭐⭐⭐
title: brand-system
url: https://skills.sh/hungv47/marketing-skills/brand-system
---

# brand-system

skills/hungv47/marketing-skills/brand-system
brand-system
Installation
$ npx skills add https://github.com/hungv47/marketing-skills --skill brand-system
SKILL.md
⚠ v6 Breaking Change

Output moved from .agents/design/brand-system.md → brand/BRAND.md + brand/DESIGN.md.

Downstream consumers to update:

product-skills/user-flow — consumes design/brand-system.md → update to brand/DESIGN.md
product-skills/technical-writer — consumes .agents/design/brand-system.md → update to brand/BRAND.md (voice/terminology) and brand/DESIGN.md (tokens)
Root README.md artifact table → update path

Duration scale change: Timings shifted from (100, 200, 300, 500)ms to (75, 150, 250, 400, 600)ms with a new --duration-emphasis tier. Brands built on v5 will have different motion timing.

Quick Brand (Route A) produces brand/BRAND.md only. DESIGN.md and ASSETS.md require the full Route B pipeline.

v6.2 Additions
voice-agent: Lexicon Rules block — machine-readable forbidden_vocabulary, preferred_phrases, casing, and emoji_policy. Lints downstream copywriting / content-create / cold-outreach output.
visual-agent: Font Loading & Licensing table — every font has source, license, free/paid status, and <link>/@font-face block. Fonts with unclear licenses are flagged [NEEDS LICENSING].
visual-agent: Iconography source library + substitution + forbidden icons — name the source library (Lucide / Tabler / etc.) with CDN/npm link, the fallback library when a glyph is missing, and a YAML list of forbidden glyphs (e.g., never 🔥).
AI-slop self-check — visual-agent and component-token-agent now self-check against references/ai-slop-detection.md before returning, instead of leaving every catch to the critic.
Step 9 broadened to "Visual Renderings (optional)" — Paper MCP (existing) + Claude Design (claude.ai/design handoff) + None. Spec stays canonical; rendering is derivative.
Anti-pattern: don't round-trip Claude Design exports into brand/ — exports are presentation artifacts, not source of truth.
Tightened example-design.md disclaimer — added a paper/solid anti-glass excerpt for Surface & Material to prevent over-anchoring on glassmorphism.
OKLCH/hex round-trip fix — oklch(0.65 0.15 180) / #2cbaa0 → oklch(0.7 0.11 180) / #3eb8a4 in the worked example and visual-agent example.
v6.1 Addition — ASSETS.md

Route B now produces a third artifact: brand/ASSETS.md. A production inventory projected deterministically from BRAND.md brand mark + DESIGN.md specs + declared platforms. Every row is a checkbox with a spec reference and a target file path under brand/. Always-on auto-scan: every brand-system run (fresh or re-run) walks the brand/ tree and flips [ ] → [x] for any row whose target file exists. Human-set [~] (in progress) and [!] (blocked) markers are preserved across runs. No new agent; implemented as an orchestrator post-merge step (Step 8.5).

Brand Identity & Design System — Orchestrator

Design — Step 1 of 2. Coordinates specialized agents to transform product artifacts into a complete brand narrative and AI-readable design system.

Core Question: "Does every visual decision trace back to who we are?"

Critical Gates — Read First
Do NOT choose colors or fonts before strategy. Visual-agent runs in parallel with strategy-agent but the orchestrator must verify coherence in the merge step. Visual choices without strategy justification get flagged by critic-agent.
Do NOT dispatch Layer 2 before Layer 1 completes. Token-architect-agent needs visual-agent output. Component-token-agent needs token-architect-agent output. The chain is strict.
Do NOT skip the critic's cross-element coherence check. Radius must map to archetype. Typography must match personality. Color must align with brand emotion. The critic checks the matrix that no individual agent can see.
Stale upstream data (>30 days) produces generic archetypes. Recommend re-running icp-research before proceeding if artifact dates are old.
BRAND.md is prose, DESIGN.md is specification. BRAND.md reads like a brand book — narrative, story, voice. DESIGN.md reads like an API reference — tables, formulas, exact values. Never mix the registers.
Inputs Required
Product description or PRD (what the product does, who it serves)
Target audience profile (demographics, psychographics, context of use)
Competitive context (who else serves this audience, how they're positioned)
Output — Three Files (Route B) / One File (Route A)

The skill produces up to three complementary files, each serving a different audience:

BRAND.md — Brand Narrative & Voice

Audience: Founders, marketers, copywriters, designers making brand decisions. Register: Prose. Reads like a brand book — narrative, story, voice examples. Contains: Origin story, naming, purpose/mission/vision, values, positioning, archetype, personality traits, emotional journey, voice chart, tone spectrum, messaging architecture, brand mark, product-specific brand sections, digital touchpoints.

DESIGN.md — AI-Readable Design System

Audience: AI coding agents, frontend engineers, design system consumers. Register: Specification. Tables, formulas, exact values. An AI agent should be able to read this file and produce on-brand UI without any other context. Contains: Visual atmosphere, complete color palettes per theme, typography rules, component stylings, layout principles, shadows & elevation, iconography, imagery direction, motion & animation, accessibility, do's and don'ts.

ASSETS.md — Production Inventory (Route B only)

Audience: Designers, art directors, asset producers, project managers tracking what to ship. Register: Checklist. Every row is a GFM checkbox with a spec reference and a target file path under brand/. Contains: Universal assets (logo variants, fonts, tokens) + social & sharing + favicon/web metadata + imagery/illustration + one per-declared-platform block. Auto-scanned on every run — [x] if the target file exists, [ ] if not. [~] in-progress and [!] blocked markers are human-owned and preserved across runs. Projected deterministically from BRAND.md + DESIGN.md + declared platforms — contains no new research, only production tracking.

Output location: brand/BRAND.md, brand/DESIGN.md, and brand/ASSETS.md in the project directory. Optionally, visual renderings via Paper MCP artboards (brand/artboards/) or a Claude Design handoff message pointing the user to claude.ai/design for interactive prototypes — see Step 9.

Agent-to-File Routing
Agent Output	→ BRAND.md	→ DESIGN.md	→ ASSETS.md
Strategy Agent	Origin story, naming, purpose/mission/vision, values, positioning, competitive landscape, product-specific sections, digital touchpoints (universal + per-declared-platform surfaces)	—	—
Personality Agent	Archetype, personality traits, emotional journey map	—	—
Voice Agent	Voice attributes (Do/Don't), tone range (3 contexts), tagline	—	—
Visual Agent	Brand mark / logo system	Visual atmosphere, color system, per-theme palettes, typography, imagery, iconography (including per-declared-platform icon specs: sizes, safe zones, state variants), surface & material language, shadow system, z-index, do's and don'ts	—
Token Architect Agent	—	Primitive scales, semantic token map, spacing, radius	—
Component Token Agent	—	Component specs, product-specific components, motion tokens, named animations	—
Accessibility Agent	—	Contrast audit, touch targets, focus states, dark mode, color independence, motion safety	—
Orchestrator (Step 8.5)	—	—	Projects brand mark + DESIGN.md Platform Icon Specs + declared platforms into a checkable inventory. Deterministic — no new agent.
Quality Gate

Before delivering, the critic agent verifies both files:

BRAND.md checks:

 Origin story and naming have cultural/etymological depth — not just "we named it X"
 Values have real tradeoffs (not generic "innovation, quality, integrity")
 Voice attributes have Do/Don't examples using real brand contexts (not hypothetical)
 Tone range covers 3 key contexts with clear shift across the range
 Tagline scored with V/F/U (minimum 6/9), passes competitor swap test
 Lexicon Rules block present: forbidden_vocabulary (5-15 entries, each a term + reason pair), preferred_phrases (5-12 brand-native strings), casing, emoji_policy — all values concrete, not "TBD". Reasons live in YAML keys, not comments.
 No copywriting scope creep (no boilerplate, pillars, elevator pitch, tagline variants)
 Emotional journey is touchpoint-level with design/interaction triggers (not copy triggers)
 Brand mark described with enough detail to commission or generate
 Digital touchpoints scoped to visual expression (not verbal)
 Route B — Platform coverage: Universal Surfaces table filled + one Digital Touchpoints subsection per declared platform; every surface within each subsection has a brand-expression entry (not blank, not "TBD"). Zero undeclared platforms appear.
 Route A — Platform coverage: Digital Touchpoints contains only the Platforms declared at intake line plus deferral note. Per-platform tables are ABSENT (not empty, not TBD — absent).
 Register separation: Digital Touchpoints surface rows describe brand expression (mood, motion cue, color role, density), never geometry (pixel sizes, masks, safe zones, framework APIs). Geometry lives in DESIGN.md Platform Icon Specifications only.
 Prose quality: reads like a brand book, not fill-in-the-blank templates

DESIGN.md checks:

 AI-readable header summarizes key decisions (archetype, metaphor, fonts, primary color)
 Font Loading & Licensing table present: every font has source, license, status, load method. Any unclear-license font is flagged [NEEDS LICENSING]
 Iconography source library named with CDN/npm link, substitution fallback library named, Forbidden Icons YAML emitted (3-8 entries with reasons, or empty list with explanation)
 Complete color palette tables for every theme (not just primary + neutrals)
 All semantic tokens have values for every theme
 Every token pair meets WCAG AA contrast (4.5:1 normal text, 3:1 large/UI)
 Background/foreground convention used consistently (bg-primary text-primary-foreground)
 One global --radius value — archetype-justified
 Surface/material language documented with CSS formulas
 Shadow system with multiple elevation levels
 Named animations with physics values (spring stiffness, damping, mass)
 Platform Icon Specifications: one subsection per declared platform with sizes, safe-area rules, state variants (dark/tinted/themed/monochrome as applicable), and derivative size list. Zero undeclared platforms appear.
 Do's and Don'ts section with concrete rules

ASSETS.md checks (Route B only):

 One section per declared platform; zero undeclared platforms
 Every row has a spec reference (BRAND.md / DESIGN.md / platform-surfaces.md) and a concrete, fully-substituted target path under brand/ (no unfilled {host} / {count} / {token} placeholders remain in any emitted path)
 No invented assets — every row traces to an upstream spec
 No duplicated spec (pixel sizes, safe zones) — ASSETS.md cites, it does not re-define
 Legend present; Summary counts present; ## Orphaned block handled (present if platforms dropped, absent otherwise)
 Prior [~] and [!] markers preserved from previous run (verify by diff if re-run)

Cross-file coherence:

 Cross-element coherence: radius maps to archetype, type personality matches archetype, color emotion aligns with brand personality, imagery direction reflects the archetype's visual world
 Voice tone in BRAND.md matches the visual atmosphere described in DESIGN.md
 ASSETS.md platform blocks exactly match BRAND.md Digital Touchpoints platforms and DESIGN.md Platform Icon Specifications platforms (same set, same order)
 AI slop check: run references/ai-slop-detection.md — 0-1 clean, 2-3 review, 4+ regeneration

Reference quality bar: Compare output against the annotated quality guides in references/example-brand.md and references/example-design.md. Every section should match the "good" pattern and avoid the "bad" pattern described in those guides. Use the overall quality tests in example-design.md (copy-paste test, blind build test, competitor swap test, implementation gap test) as final validation.

Chain Position

Previous: icp-research (product context) | Next: imc-plan, copywriting, content-create

Re-run triggers: After major product pivots, when entering new markets, after significant audience shifts, or annually for brand refresh.

Related skills (non-chain): icp-research (audience data for brand strategy), content-create (consumes voice guidelines), humanize (uses voice adjectives)

Skill Deference
Need audience research first? Run icp-research (from marketing-skills) — brand strategy without audience research produces generic archetypes.
Need user flows after brand? Run user-flow next — it consumes design tokens and component context.
Need marketing copy? Run content-create or copywriting — they consume voice guidelines.
Agent Manifest
Agent	Layer	File	Routes to	Focus
Strategy Agent	1 (parallel)	agents/strategy-agent.md	BRAND.md	Purpose, mission, vision, values, positioning, competitive landscape, brand narrative (origin/naming), product-specific sections, digital touchpoints
Personality Agent	1 (parallel)	agents/personality-agent.md	BRAND.md	Jungian archetype (70/30 blend), personality traits, touchpoint-level emotional journey
Voice Agent	1 (parallel)	agents/voice-agent.md	BRAND.md	Voice attributes (Do/Don't), tone range (3 key contexts), primary tagline with V/F/U score
Visual Agent	1 (parallel)	agents/visual-agent.md	Both	Logo → BRAND.md. Visual atmosphere, color system, per-theme palettes, typography, imagery, surface & material language, shadow system, z-index, do's and don'ts → DESIGN.md
Token Architect Agent	2 (sequential)	agents/token-architect-agent.md	DESIGN.md	3-layer W3C token system, semantic map, radius-to-archetype, per-theme token tables
Component Token Agent	2 (sequential)	agents/component-token-agent.md	DESIGN.md	Button 6 variants, input specs, card specs, product-specific components, named animations with physics values, motion tokens
Accessibility Agent	2 (sequential)	agents/accessibility-agent.md	DESIGN.md	WCAG AA contrast, touch targets, dark mode audit, focus states
Critic Agent	2 (final)	agents/critic-agent.md	Both	Cross-element coherence, BRAND.md narrative quality, DESIGN.md AI-readability, PASS/FAIL
Shared References (read by multiple agents)
references/assets-inventory.md — Per-platform asset templates, emission rules, and auto-scan protocol (read by orchestrator only, Step 8.5)
references/brand-archetypes.md — 12 Jungian archetypes with visual/verbal mappings
references/brand-voice.md — Voice frameworks, tone dimensions, messaging architecture
references/visual-identity.md — Logo systems, imagery, iconography, graphic elements
references/color-emotion.md — Color psychology, OKLCH values, audience palettes
references/typography-psychology.md — Font personality mappings and pairing rules
references/token-architecture.md — Three-layer token system, semantic token map
references/token-templates.md — Primitive scales, radius-archetype mapping, mapping example
references/component-tokens.md — Component token map, button/input/card specs, motion tokens
references/component-patterns.md — Extended UI component patterns with token consumption maps
references/implementation-rules.md — Accessibility baseline, dark mode rules, brand applications
references/platform-surfaces.md — Per-platform brand-expression surfaces + icon specifications (strategy-agent reads the Brand expression tables, visual-agent reads the Icon specifications blocks)
references/artboard-generation.md — Paper MCP artboard specs and workflow
references/paper-artboard-templates.md — Paper MCP HTML/CSS templates
references/ai-slop-detection.md — AI-generated design anti-patterns checklist
Quality-Bar Reference Examples
references/example-brand.md — Annotated quality guide: good vs bad excerpts for every BRAND.md section
references/example-design.md — Annotated quality guide: good vs bad excerpts for every DESIGN.md section
Routing Logic
Mode Selection

Ask: "Full brand system or quick brand for MVP?"

Route A: Quick Brand (MVP)

When: MVP, early-stage, need to ship fast with basic brand foundations.

1. Pre-dispatch: Gather context (Step 0)
2. LAYER 1 — Dispatch IN PARALLEL:
   - strategy-agent (purpose, values, positioning)
   - visual-agent (color + typography only — logo deferred)
3. Dispatch: critic-agent (coherence check — strategy-to-visual only)
4. If FAIL → re-dispatch named agent(s) with feedback (max 2 cycles)
5. Deliver Quick Brand artifact


Quick Brand scope: Purpose/mission/vision, core values, positioning, primary color + neutrals, display + body font, basic type hierarchy. Target platforms are still captured at intake and recorded in BRAND.md as a one-line declaration ("Ships on: iOS, macOS, Web") so Route B can pick them up later. Defers: archetype analysis, voice/tone system, messaging architecture, full visual identity, token architecture, component tokens, accessibility audit, dark mode, Visual Renderings (Step 9), per-platform Digital Touchpoints surfaces, per-platform icon specifications.

Quick Brand output includes a note: "Run full brand-system when ready to build the design system."

Route B: Full Brand System

When: Established product, full rebrand, comprehensive guidelines needed.

Step 0    Pre-dispatch: Gather context
Step 1    LAYER 1 — Dispatch IN PARALLEL:
          - strategy-agent
          - personality-agent
          - voice-agent
          - visual-agent
Step 2    MERGE: Assemble Layer 1 outputs into brand identity sections
Step 3    LAYER 2 — Dispatch SEQUENTIALLY:
          - token-architect-agent (receives visual-agent + personality-agent output)
          - component-token-agent (receives token-architect-agent output)
          - accessibility-agent (receives token-architect + component-token outputs)
Step 4    Dispatch: critic-agent (receives BRAND.md + DESIGN.md)
Step 5    If FAIL → re-dispatch named agent(s) with feedback (max 2 cycles)
Step 8.5  ASSETS.md projection — deterministic, no new agent, always-on auto-scan
Step 9    Visual Renderings (optional) — Paper MCP / Claude Design / none
Step 10   Deliver artifacts (BRAND.md + DESIGN.md + ASSETS.md)


Why the jump from Step 5 to Step 8.5: the label 8.5 is a section header, not a sequence index. It was chosen so ASSETS.md projection could slot after the critic gate but before the pre-existing Step 9 (Visual Renderings) without renumbering downstream references. Steps 6, 7, and 8 are intentionally absent — the legacy flow used the names "Critic Gate", "re-dispatch", "deliver" without numeric step labels, so no content maps to those slots. Reading order is: 0 → 1 → 2 → 3 → 4 → 5 → 8.5 → 9 → 10.

Step 0: Pre-Dispatch Context Gathering
Product Context Check

Check for research/product-context.md and research/icp-research.md. If date fields are older than 30 days, warn the user and recommend re-running upstream skills. Tip: /navigate status (from meta-skills) gives a single-pass freshness report across all upstream artifacts.

Required Inputs — Interview If Missing

Product description or PRD

Target audience profile

Competitive context

Target platforms — which surfaces the brand ships on. Multi-select. Ask explicitly; do not assume "a web app." Canonical set:

Web (marketing site, in-product web UI, PWA)
iOS / iPadOS
Android
macOS (native AppKit/SwiftUI, or cross-platform shell like Electron/Tauri — ask which)
Windows (native WinUI/Win32, or cross-platform shell)
Linux desktop (GTK/Qt, or shell)
watchOS / Wear OS
tvOS
CarPlay / Android Auto
Browser extension (Chrome / Firefox / Safari / Edge — ask which)
CLI / terminal
Email (as a first-class brand channel — transactional + newsletter)
Embedded app (Slack / Notion / Discord / Microsoft Teams / Linear / GitHub — ask which host)

Disambiguate common vagueness: "mobile app" → iOS, Android, or both? "desktop app" → native or Electron? "web app" → marketing site + product, or just one? If the user names a cross-platform shell (Electron, Tauri, Flutter, RN, Capacitor), still enumerate the host OSes — each OS gets its own surface set.

Strongly Recommended
Existing brand assets (logos, colors, fonts, past guidelines)
Founder/team values and origin story
Key differentiators
Helpful
Admired brands (aspirational and anti-aspirational)
Market positioning intent (premium, accessible, disruptive, trusted)
Optional Artifacts
Artifact	Source	Benefit
research/product-context.md	icp-research (from hungv47/research-skills)	Product positioning, audience, and voice adjectives — grounds brand strategy in audience research
research/icp-research.md	icp-research (from hungv47/research-skills)	Audience personas, pain profiles, and VoC quotes — brand strategy without audience research produces generic archetypes

Strongly recommended: Run icp-research (from research-skills) first if audience research hasn't been done.

Context to Pass to All Agents
Product: description, audience, competitive landscape
Existing assets: any logos, colors, fonts, guidelines to preserve or evolve
Positioning intent: premium, accessible, disruptive, trusted
Upstream artifacts: excerpts from product-context.md and icp-research.md if available
Target platforms: declared platform list from intake — strategy-agent renders a Digital Touchpoints subsection per declared platform; visual-agent renders per-platform icon specs. Undeclared platforms MUST NOT appear in output. If the user declared "iOS + web" only, do not pad the artifact with Android/Windows sections.

Missing product details are not guessable — interview for them.

Dispatch Protocol
How to spawn a sub-agent
Read the agent instruction file — include its FULL content in the Agent prompt
Append the context (product, audience, competitive landscape, existing assets) after the instructions
Resolve file paths to absolute: replace relative paths with absolute paths rooted at this skill's directory
Pass upstream artifacts by content: the orchestrator reads .agents/ files FIRST, then includes relevant excerpts in context. Sub-agents should NOT read artifact files directly.
If feedback exists (from critic FAIL), append with header "## Critic Feedback — Address Every Point"
Conventions
Source citation: When stating facts about brand psychology, color theory, or archetype effectiveness, cite the source. If from a web search, include the URL. If a fact cannot be attributed, flag it as [UNVERIFIED].
Context loaded: When producing the artifact, include which upstream artifacts were read and their versions/dates in the artifact body. This creates an audit trail for downstream skills.
Single-agent fallback

If multi-agent dispatch is unavailable, execute each agent's instructions sequentially in-context:

Layer 1: define strategy, select archetype, write voice chart, design visual identity
Layer 2: build token architecture, map component tokens, audit accessibility
Final: evaluate with critic rubric, check cross-element coherence
Layer 1: Parallel Foundation

Spawn IN PARALLEL:

Agent	Instruction File	Pass These Inputs	Reference Files
Strategy Agent	agents/strategy-agent.md	brief (product + audience + competitors + declared platforms)	references/platform-surfaces.md (Route B only)
Personality Agent	agents/personality-agent.md	brief (product + audience)	references/brand-archetypes.md
Voice Agent	agents/voice-agent.md	brief (product + audience)	references/brand-voice.md
Visual Agent	agents/visual-agent.md	brief (product + audience + existing assets + declared platforms)	references/color-emotion.md, references/typography-psychology.md, references/visual-identity.md, references/platform-surfaces.md

Wait for all to complete. Their outputs feed the merge step and Layer 2.

Merge Step — Brand File Assembly (BRAND.md + DESIGN.md)

Before assembling, read references/artifact-templates.md for the complete section structure, field specifications, and ordering for both files. ASSETS.md is assembled separately in Step 8.5 after the critic gate passes — it does not merge in this step.

After Layer 1 completes, assemble outputs into two separate files simultaneously:

BRAND.md Assembly (from Layer 1)
Section	Owner Agent	Notes
The Origin Story	Strategy Agent	Narrative prose, not bullet points
The Name	Strategy Agent	Etymology, meaning, cultural context
Purpose, Mission & Vision	Strategy Agent	—
Core Values	Strategy Agent	"X over Y" format with real tradeoffs
Brand Positioning	Strategy Agent	Positioning statement, value prop, what we are/aren't
Brand Archetype	Personality Agent	70/30 blend with "in action" section
Personality Traits	Personality Agent	"Trait, but not extreme" table
Emotional Journey Map	Personality Agent	Touchpoint-by-touchpoint, not before/during/after
Brand Voice DNA	Voice Agent	Voice attributes (Do/Don't) + tone range (3 contexts) + tagline
The Brand Mark	Visual Agent (logo section)	Visual description, variations, color combos, rules
[Product-Specific Sections]	Strategy Agent	Differentiators, pricing as brand, parent brand relationship
Digital Touchpoints	Strategy Agent	How brand expresses at each surface
DESIGN.md Assembly (starts from Layer 1, completed by Layer 2)
Section	Owner Agent	Notes
AI-Readable Header	Orchestrator synthesis	Archetype, visual metaphor, fonts, primary color
1. Visual Theme & Atmosphere	Visual Agent	Mood, density, metaphor — prose introduction
2. Color Palette & Roles	Visual Agent + Token Architect	Primary colors, semantic, per-theme palettes, neutrals, distribution rules
3. Typography Rules	Visual Agent	Font stack, type scale, typography rules
4. Component Stylings	Component Token Agent	Product-specific core components + standard components
5. Layout Principles	Token Architect Agent	Spacing scale, border radius
6. Shadows & Elevation	Visual Agent + Component Token	Shadow scale, z-index scale
7. Iconography	Visual Agent	System icons, product-specific icons, Platform Icon Specifications (per declared platform)
8. Imagery & Visual Direction	Visual Agent	Photography, brand devices
9. Motion & Animation	Component Token Agent	Principles, duration scale, easing, named animations, motion safety
10. Accessibility	Accessibility Agent	Contrast, focus, touch targets, color independence
11. Do's and Don'ts	Visual Agent	Concrete rules synthesized from all decisions

Coherence check before Layer 2: Verify that the archetype selected by personality-agent aligns with the visual choices made by visual-agent. If they contradict (e.g., Caregiver archetype with sharp/aggressive typography), resolve before dispatching Layer 2.

Layer 2: Sequential Chain

Dispatch ONE AT A TIME, IN ORDER:

Step	Agent	Instruction File	Receives
1	Token Architect Agent	agents/token-architect-agent.md	Visual-agent output (colors, fonts, complete theme palettes) + personality-agent output (archetype for radius)
2	Component Token Agent	agents/component-token-agent.md	Token-architect-agent output (semantic token map)
3	Accessibility Agent	agents/accessibility-agent.md	Token-architect + component-token outputs
4	Critic Agent	agents/critic-agent.md	Complete assembled brand system (both BRAND.md and DESIGN.md)

Palette ownership rule: Visual-agent is authoritative for color choices and theme palette values. Token-architect-agent systematizes those values into the three-layer architecture (primitive → semantic → component) and adds any missing infrastructure tokens (--popover, --popover-foreground). If values conflict, visual-agent wins.

Accessibility hand-back: Accessibility-agent runs after shadow tokens are set, but if its audit demands changes to upstream values (a shadow color that fails contrast against the surface it sits on, a primary lightness that fails 3:1 against --primary-foreground), it does NOT edit the upstream table directly. Instead, it reports the failing pair to the critic, which fails the gate and re-dispatches the upstream owner — visual-agent for shadows / colors, token-architect-agent for semantic values, component-token-agent for component-level overrides. Accessibility-agent owns the audit, not the fix.

Critic Gate
PASS: Proceed to ASSETS.md projection (Step 8.5), then optional Visual Renderings (Step 9 — Paper MCP / Claude Design / none).
FAIL: Re-dispatch named agent(s) with critic feedback. Max 2 rewrite cycles. After 2 failures, deliver with critic annotations and flag to user.
Step 8.5: ASSETS.md Projection (Route B only, always-on)

No sub-agent. Deterministic orchestrator step executed after the critic passes and before Visual Renderings (Step 9).

Read references/assets-inventory.md for the full emission rules, per-platform templates, and file template. Summary of the procedure:

Load prior state (if any): Read existing brand/ASSETS.md. Extract rows with status [~] (in progress) or [!] (blocked) — preserve verbatim. Note any platforms present in the old file that are no longer in the declared list — those rows go to ## Orphaned on emit.
Project fresh inventory: Using BRAND.md brand mark section, DESIGN.md §2/§3/§7/§8/§9, and the declared-platforms list, emit rows in this order — Universal → Social & Sharing → Favicon & Web Metadata (if Web declared) → Imagery & Illustration (if DESIGN.md §8 declares direction) → one per-platform block in declared order. Every row has: name, spec ref, target path, status. Expand every {placeholder} before proceeding: for each declared embedded host, emit one full row set with {host} substituted; for imagery rows, substitute {count} from DESIGN.md §8. No row may reach substep 3 with an unfilled placeholder in its target path.
Auto-scan for [x]: For file-typed rows, Bash: test -e <path> → [x] if true, [ ] if false. For directory-typed rows (path ends in /), require at least one non-.gitkeep file: test -d <path> && [ -n "$(ls -A <path> 2>/dev/null | grep -v '^\.gitkeep$')" ] → [x] if true, [ ] if false. This prevents scaffolded-empty-directory false-completion.
Merge human markers: Overlay preserved [~] and [!] rows from step 1 (matched by name) onto the fresh inventory. Human markers override auto-computed status.
Compute summary: Total / Done / In progress / Blocked / Not started counts.
Write brand/ASSETS.md with frontmatter (declared platforms, last scan ISO timestamp, BRAND.md version, DESIGN.md version), legend, sections, summary, and ## Orphaned block if any.
Re-run versioning: ASSETS.md is a living file — always updated in place. Dropped-platform rows move to ## Orphaned (they are NOT removed), which preserves tracking state continuously. Only version (rename to ASSETS.v[N].md) when the user explicitly requests a fresh inventory, e.g., after a major product pivot. The Orphaned block mechanism, not versioning, is the primary handler for "platform dropped between runs."

Quality gate for this step (orchestrator self-check before writing the file):

Every row has both a spec ref and a target path.
Platform block set in ASSETS.md === declared platforms === BRAND.md Digital Touchpoints platforms === DESIGN.md Platform Icon Specifications platforms.
No human-set [~] or [!] markers from the prior file were overwritten.
No invented rows (every row traces to references/assets-inventory.md templates).

Scope: Route B only. Route A (Quick Brand) does not produce ASSETS.md — the platform list is captured but no inventory is emitted until the full pipeline runs.

Step 9: Visual Renderings (optional)

The spec — BRAND.md / DESIGN.md / ASSETS.md — is the canonical artifact. Renderings are derivative presentations of that spec, not source of truth. Three renderer paths, all optional:

9a. Paper MCP — programmatic artboards

If Paper MCP tools are available, render the brand as 5 presentation artboards. Reference references/artboard-generation.md for complete specs, workflow, and prerequisites.

After generating artboards, run the AI slop detection checklist (references/ai-slop-detection.md). Artboards are the highest-risk output for AI default patterns.

Artboards: Color Palette | Typography System | Spacing & Tokens | UI Style Principles | Logo System

Save to brand/artboards/.

9b. Claude Design — interactive prototypes (claude.ai/design)

Claude Design is an Anthropic Labs UI product available at claude.ai/design (Pro / Max / Team / Enterprise tiers). It produces designs, prototypes, slides, and one-pagers in collaboration with the user inside Claude. The product accepts text prompts, document/image uploads, and codebase context for design-system grounding.

This skill does not dispatch to Claude Design — there is no API or MCP. It hands off, by giving the user precise instructions for what to share and how to scope the session:

Pre-flight check before instructing the user:

brand/DESIGN.md exists and contains complete theme palette tables for every theme.
brand/BRAND.md Brand Mark section describes the logo at commission-grade detail.
At least one of brand/logo/logo-full.svg or a placeholder logo asset exists.
brand/font/ contains either downloaded woff2s or a link comment for each declared font.

If any pre-flight check fails, say so — do not send the user to Claude Design with an incomplete spec.

Handoff message to user (if checks pass):

Your brand spec is ready for Claude Design. Open claude.ai/design (requires Pro / Max / Team / Enterprise) and start a session by sharing your brand/ folder — at minimum paste DESIGN.md (so the design system tokens, theme palettes, and component specs ground the session) and BRAND.md (so voice and brand mark ground any copy or logo placement). ASSETS.md is useful for telling Claude Design which production assets already exist vs. still need to be made. Outputs (prototypes, slides, one-pagers, HTML/PPTX/Canva exports) are presentation artifacts — keep them in a separate location, not inside brand/. To update the brand source, re-run brand-system; share the updated spec with Claude Design in the next session.

9c. None

If neither renderer is available or wanted, skip — the spec stands alone. Downstream skills (user-flow, content-create) consume DESIGN.md directly without rendering.

Artifact Templates

Save to brand/BRAND.md, brand/DESIGN.md, and brand/ASSETS.md in the project directory. Create the brand/ directory if it doesn't exist. Also create brand/logo/, brand/font/, brand/inspiration/, brand/social/, brand/favicon/, brand/tokens/, brand/imagery/, and brand/platforms/ subdirectories with .gitkeep files for future assets.

On re-run: rename existing BRAND.md / DESIGN.md to BRAND.v[N].md / DESIGN.v[N].md and create new with incremented version. ASSETS.md is always updated in place — it's a living inventory. Dropped-platform rows move to the ## Orphaned block (preserved, not deleted). Version ASSETS.md (ASSETS.v[N].md) only when the user explicitly requests a fresh inventory.

Full templates: See references/artifact-templates.md for the complete BRAND.md and DESIGN.md templates with all sections and field specifications.

Template summary:

BRAND.md (11 sections): Origin Story → Name → Purpose/Mission/Vision → Core Values ("X over Y" format) → Brand Positioning → Brand Archetype (Primary 70% + Secondary 30%) → Personality Traits → Emotional Journey Map → Brand Voice DNA (attributes + tone range + tagline with V/F/U scoring) → Brand Mark (logo system) → Digital Touchpoints.

DESIGN.md (11 sections): Visual Theme & Atmosphere → Color Palette & Roles (OKLCH, themes, neutral scale, 60/30/10) → Typography Rules (font stack, type scale) → Component Stylings (core component + cards + buttons + inputs) → Layout Principles (spacing, radius) → Shadows & Elevation (z-index) → Iconography → Imagery & Visual Direction → Motion & Animation (duration, easing, spring physics) → Accessibility (contrast, focus, touch targets) → Do's and Don'ts.

ASSETS.md (5 fixed sections + one subsection per declared platform): Universal → Social & Sharing → Favicon & Web Metadata (if Web declared) → Imagery & Illustration (if DESIGN.md §8 declares direction) → Platforms (one subsection per declared platform, in declared order) → Summary → Orphaned (only if platforms dropped between runs). Full template and per-platform row sets in references/assets-inventory.md.

Quality-bar examples: references/example-brand.md and references/example-design.md show the complete output at the expected quality level.

Worked Example (Condensed) — Route B: Full Brand System

Input: FinLit — a personal finance app for young professionals (22-30), positioned against intimidating banking apps.

Step 0: Pre-Dispatch

Product: personal finance app. Audience: young professionals 22-30. Competitors: traditional banking apps (Mint, bank mobile apps). Platforms declared: iOS, Web (marketing site + PWA), Email.

Layer 1: Parallel Foundation

All 4 agents dispatched in parallel:

Strategy agent returns: Origin story ("born from a founder's shame spiral at 24"), name ("FinLit — financial literacy, shortened to feel casual"), purpose "make finance empowering, not shameful." Positioning: "the only finance app that feels like a supportive friend." Values: transparency over comfort, simplicity over completeness, progress over perfection. Digital touchpoints mapped across 6 surfaces. Product-specific: "Streak System as brand expression" section.
Personality agent returns: Caregiver (70%) + Explorer (30%). Traits: encouraging but not patronizing, clear but not dumbed-down, warm but not saccharine. Emotional journey: 8-touchpoint map (first encounter → app store → onboarding → first budget → daily check → missed goal → annual review → telling a friend).
Voice agent returns: Voice DNA with 3 attributes (straight-talking, encouraging, honest) with real-context Do/Don't examples. Tone range across 3 contexts (marketing: inviting + confident, product UI: minimal + clear, errors: calm + honest). Tagline: "Money, minus the shame." V:3 F:2 U:3 = 8/9.
Visual agent returns: For BRAND.md: Logo system (4 variations, color combos, rules). For DESIGN.md: Visual atmosphere ("warm kitchen table, not bank lobby"). Primary warm teal oklch(0.7 0.11 180) / #3eb8a4. Complete light + dark theme palettes (18 tokens each). Neutral base: Stone. Display: Plus Jakarta Sans. Body: Inter. Shadow system (5 levels). Surface material: soft matte (no glass). Imagery: real people, natural light, warm tones. Do's and Don'ts (12 items each).
Merge — Brand File Assembly (BRAND.md + DESIGN.md)

BRAND.md assembled from strategy (origin/name/purpose/values/positioning/touchpoints) + personality (archetype/traits/journey) + voice (voice DNA/tone range/tagline) + visual (logo only). DESIGN.md started from visual (atmosphere/colors/typography/shadows/imagery/do's-don'ts). AI-readable header generated.

Coherence check: Caregiver archetype aligns with warm teal (trust + growth), humanist-leaning typography (approachable), 0.5rem radius (soft). PASS — proceed to Layer 2.

Layer 2: Sequential Chain

All outputs go to DESIGN.md:

Token architect returns: Stone 50-950 neutral scale, teal 50-950 primary scale, --radius: 0.5rem, 19 semantic tokens with light + dark values. Spacing scale.
Component token returns: 6 button variants mapped to semantic tokens, input specs with blur validation, card specs. Product-specific: "Budget Card" component with progress ring. Named animations: progress-fill (spring, stiffness 180), goal-celebrate (confetti, 600ms). Motion tokens (75-500ms).
Accessibility returns: All token pairs pass 4.5:1. Dark mode surface hierarchy (stone.950 → stone.900 → stone.800). Primary shifts to teal.400 in dark mode. Touch targets ≥44px.
Critic returns: PASS on both files. BRAND.md narrative quality strong, emotional journey touchpoint-level. DESIGN.md AI-readable, all themes complete. Cross-element coherence verified. AI slop score: 1 item (clean).
Step 8.5: ASSETS.md Projection

Orchestrator projects declared platforms (iOS, Web, Email) against references/assets-inventory.md templates. Emits 18 Universal rows + 13 Social & Sharing + 8 Favicon/Web + 8 Imagery + 13 iOS + 7 Web-platform + 7 Email-platform = 74 rows. Auto-scans brand/ — logo-full.svg exists → [x]; all others [ ] (fresh run). Writes brand/ASSETS.md with legend, sections, summary (Done: 1 / 74), no orphaned block (first run). On re-run, Done count rises as the designer drops files into brand/ subdirs.

Deliver

brand/BRAND.md, brand/DESIGN.md, and brand/ASSETS.md saved.

Worked Example (Condensed) — Route A: Quick Brand

Input: TaskFlow — a new project management tool, pre-MVP, needs basic brand to start building.

Step 0: Pre-Dispatch

Product: project management tool. Audience: small team leads. Platforms declared: Web, macOS (Electron). Quick Brand selected — platforms captured as one line in BRAND.md; per-platform surfaces and icon specs deferred to Route B.

Layer 1: Parallel (reduced)
Strategy agent returns: Purpose, values (clarity over complexity, speed over ceremony), positioning. Origin story deferred.
Visual agent returns: Primary blue oklch(0.623 0.214 259) / #3b82f6. Neutral: Slate. Display: Inter. Body: Inter.
Critic (reduced)

Checks strategy-to-visual coherence only. PASS.

Deliver

Quick Brand artifact saved as single brand/BRAND.md with note: "Run full brand-system when ready to produce DESIGN.md."

Quick Brand produces BRAND.md only. DESIGN.md requires the full Route B pipeline (token architect, component tokens, accessibility audit).

Anti-Patterns

Aesthetics without strategy — Picking colors or fonts because they "look nice" without tracing back to archetype and positioning. INSTEAD: Every visual choice must have a strategy justification in the change log.

Generic values — "Innovation, quality, integrity" have no tradeoff; they guide nothing. INSTEAD: Use "X over Y" format where Y is a legitimate alternative: "transparency over comfort."

Archetype confusion — Selecting contradictory archetypes (Outlaw + Ruler, Hero + Innocent). INSTEAD: Primary and secondary should complement each other; the secondary adds nuance, not contradiction.

Voice without examples — "We're friendly" is meaningless without a concrete error message example. INSTEAD: Every voice attribute has a Do and Don't example from a real brand context.

Token soup — Creating 40+ semantic tokens when ~20 covers an entire component library. INSTEAD: Keep the semantic layer tight. If you're inventing --subtle-muted-foreground-alt, the system is too granular.

Skipping semantic layer — Components referencing primitives (oklch(0.546...)) instead of semantic tokens (var(--primary)). INSTEAD: Always reference semantic tokens. The three-layer chain is Primitive -> Semantic -> Component.

Mismatched bg/fg pairs — bg-primary text-primary is wrong; use bg-primary text-primary-foreground. INSTEAD: Every semantic color role is a pair. Base = background. -foreground = text on that surface.

Dark mode as inversion — Simply swapping black/white produces unusable surfaces. INSTEAD: Deliberate surface hierarchy (background -> card -> popover), reduced saturation, shifted primary lightness.

Dispatching all agents for Quick Brand — Route A exists for MVPs. INSTEAD: Quick Brand uses only strategy + visual + critic. No archetype analysis, no tokens, no components.

Inventing ASSETS.md rows — Adding checklist rows for assets not traceable to BRAND.md / DESIGN.md / platform-surfaces.md. INSTEAD: every row cites its spec. If you can't point to the spec, the asset doesn't belong in the inventory.

Overwriting human [~] or [!] markers in ASSETS.md — The auto-scan only flips [ ] ↔ [x] based on file existence. In-progress and blocked markers are human-owned. INSTEAD: preserve them verbatim across re-runs; merge after the fresh projection.

Silently dropping ASSETS.md rows when a platform is un-declared — Erases tracking state the user may have been maintaining. INSTEAD: move the dropped-platform rows to ## Orphaned (platform no longer declared) on emit, so the user can review before losing status.

Round-tripping Claude Design exports into brand/ — Claude Design produces interactive prototypes, slides, one-pagers, and HTML/PPTX/Canva exports. These are derivative presentation artifacts, not source of truth. Saving them into BRAND.md / DESIGN.md / ASSETS.md corrupts the spec. INSTEAD: Claude Design exports go to a separate location (e.g., presentations/, or a Claude Design folder/Canva account). To update the spec, re-run brand-system; Claude Design will re-render from the updated source on the next visit.

Agent Files
Sub-Agent Instructions (agents/)
agents/strategy-agent.md — Purpose, mission, vision, values, positioning
agents/personality-agent.md — Jungian archetype blend, personality traits, emotional journey
agents/voice-agent.md — Voice chart, tone spectrum, messaging architecture
agents/visual-agent.md — Logo, color system, typography, imagery
agents/token-architect-agent.md — 3-layer W3C token system, semantic map
agents/component-token-agent.md — Button variants, input/card specs, motion tokens
agents/accessibility-agent.md — WCAG AA, dark mode, touch targets, focus states
agents/critic-agent.md — Cross-element coherence, PASS/FAIL
Shared References (references/)
references/assets-inventory.md — ASSETS.md per-platform templates, emission rules, auto-scan protocol (orchestrator Step 8.5)
references/brand-archetypes.md — 12 Jungian archetypes with visual and verbal mappings
references/brand-voice.md — Voice frameworks, tone dimensions, messaging architecture
references/visual-identity.md — Logo systems, imagery direction, iconography, graphic elements
references/token-architecture.md — Three-layer token system, semantic token map, neutral presets
references/token-templates.md — Primitive scales, semantic token map, radius-archetype mapping, mapping example
references/component-tokens.md — Component token map, button/input/card specs, motion tokens
references/implementation-rules.md — Accessibility baseline, dark mode rules, brand applications
references/platform-surfaces.md — Per-platform brand-expression surfaces + icon specifications (single source of truth for both strategy-agent and visual-agent)
references/artboard-generation.md — Paper MCP artboard specs and workflow
references/typography-psychology.md — Font personality mappings and pairing rules
references/color-emotion.md — Color psychology, OKLCH values, audience palettes
references/component-patterns.md — Extended UI component patterns with token consumption maps
references/paper-artboard-templates.md — Paper MCP HTML/CSS templates
references/ai-slop-detection.md — AI-generated design anti-patterns checklist
references/artifact-templates.md — Complete BRAND.md and DESIGN.md output templates with all sections and field specifications
Quality-Bar Reference Examples (references/)
references/example-brand.md — Worked example: Conquistador BRAND.md (narrative brand book at quality bar)
references/example-design.md — Worked example: Conquistador DESIGN.md (AI-readable design system at quality bar)
Weekly Installs
17
Repository
hungv47/marketing-skills
GitHub Stars
1
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass