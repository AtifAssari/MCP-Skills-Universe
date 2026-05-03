---
title: diagram
url: https://skills.sh/spm1001/claude-suite/diagram
---

# diagram

skills/spm1001/claude-suite/diagram
diagram
Installation
$ npx skills add https://github.com/spm1001/claude-suite --skill diagram
SKILL.md
Diagramming

Create conceptual charts and diagrams as SVG, render to PNG, self-critique, iterate, and show user.

When to Use
Conceptual diagrams (Venn, flow, architecture)
Data charts (line, bar, area)
Visual explanations for slides or documents
When NOT to Use
Hero images or photorealistic content (use picture skill)
Simple text formatting (markdown suffices)
Screenshots or screen mockups (different tools)
Workflow
1. Understand the Content

User typically provides:

Structure — "boxes connected by arrows", "Venn with overlap"
Content — the actual text/data to include
Purpose — the message or insight

Clarify these before drawing. The structure is theirs, the execution is yours.

2. Apply Brand (if applicable)

If a brand skill exists (e.g., itv-brand), read its specs for:

Color palette
Typography
Visual principles

If no brand specified, use sensible defaults:

Clear hierarchy (see Contrast below)
Vary the palette. Don't default to dark backgrounds every time. Light, warm, pastel, earthy, muted — all valid. Match the tone of the content: playful topic → bright colours; corporate → clean whites with accent colours; technical → cool greys. Dark backgrounds are one option, not the default.
3. Create SVG

Canvas: 1280×720 (16:9) default. Brand skill may override.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" width="1280" height="720">
  <rect x="0" y="0" width="1280" height="720" fill="#BACKGROUND"/>
  <!-- Content -->
</svg>


For human-editable SVGs: Structure multi-line text as siblings in one transform group:

<g transform="translate(250, 175)">
  <text x="0" y="0" text-anchor="middle">Line One</text>
  <text x="0" y="28" text-anchor="middle">Line Two</text>
</g>


This keeps lines together as one selectable object in editors like Inkscape. (Note: Affinity breaks this apart on import — see references/svg-interop.md.)

CRITICAL: Never create separate unlinked <text> elements for lines that belong together semantically. If "New stories / to tell" is one label, it's one group — always. Ungrouped lines become editing nightmares.

4. Render to PNG

Prerequisite: brew install librsvg — required for arrow markers and full SVG rendering fidelity.

rsvg-convert -w 1280 -h 720 input.svg -o /tmp/chart.png


sips is faster but silently drops SVG markers (arrows, arrowheads). Only use sips for diagrams with no markers. If rsvg-convert is not installed, warn the user before rendering — arrows will be missing.

5. Self-Critique (CRAP + Composition)

Read the PNG and critique against CRAP principles before showing user:

Proximity — Are related items grouped?

Labels adjacent to what they describe (not 300px away in a separate column)
Annotations should be close enough that the eye doesn't have to hunt
More space between groups than within groups
White space organized, not scattered — no large empty area in one place and cramped in another
Minimum gap between unrelated elements: ~22px (0.3" equivalent). Closer than that looks like collision unless deliberately grouped

Alignment — Do elements connect visually?

Every element aligns with something else
One dominant alignment system
If annotations are in a column, align them to ONE x-coordinate (ragged = amateur)
Strong invisible lines across the canvas
Cross-canvas alignment creates unity even between unrelated elements

Repetition — Is styling consistent?

Similar elements styled identically
Limited color palette, reused systematically
Clear visual rhythm
Consolidate font sizes to 3-4 levels maximum

Contrast — Is hierarchy clear?

Title largest, then highlighted element, then content
Primary data stands out from secondary
No "wimpy" differences — all contrasts are bold. If two elements are different hierarchy levels, the size difference should be at least 2x (e.g., 36px title vs 18px body, not 20px vs 16px)
Check contrast at smaller sizes — problems emerge
Text on dark backgrounds: #e2e8f0 minimum. WCAG 4.5:1 contrast ratio as hard floor

Composition Check — After CRAP, step back and ask:

Is the composition centered on the canvas? (Calculate, don't eyeball)
Is whitespace balanced left/right, top/bottom? (Check both axes — horizontally centered but top-heavy still looks wrong)
Are there orphan elements with no visual relationship to anything?
Canvas edge margin: keep content away from the outer ~10% on all sides. Content touching edges looks unfinished.

Centering calculation:

left_edge = leftmost content x-coordinate
right_edge = rightmost content x-coordinate
content_center = (left_edge + right_edge) / 2
offset = canvas_center - content_center
# Shift everything by offset


See references/design-principles.md for detailed interventions.

6. Reduced Size Check

View the PNG at 50-75% size (or squint). Problems that hide at full size emerge:

Centering issues become obvious
Competing elements reveal themselves
Hierarchy flattens — is the important thing still prominent?
Low contrast text disappears

If something looks wrong small, it IS wrong.

7. Fix and Re-render

If issues found, fix and render again. One fix often creates another problem — repositioning to fix an overlap can create a new gap; resizing text can break alignment. Run at least two critique cycles before declaring done.

Common fixes:

Centering off → calculate offset, shift all elements
Annotations too far → move closer, or put inside elements
Orphan element → add connector line or align to something
Low contrast → boost to #e2e8f0 minimum for text on dark backgrounds
Text touching shape edges → inset text 10-15px from borders on all sides
Too dense → split content across multiple visuals rather than shrinking text
8. Completeness Check

Before showing user, ask: what's missing from the domain? You're visualising someone's mental model — have you captured all the key elements they'd expect to see? If the diagram is about "data partnerships" and you only listed two when there are three, the user will notice. This isn't about design; it's about content accuracy.

9. Show User
open -a "Google Chrome" /tmp/chart.png


Or copy to Desktop if user needs the file.

Design Principles
Hierarchy

Title > Highlighted element > Content. Three levels maximum. The title is largest. The key insight (e.g., Venn intersection) is second. Everything else supports these. The difference between levels should be obvious — 2x size minimum between title and body text.

Containment

In Venn diagrams, intersection text should be visually contained within the overlap shape. Each piece of content should be unambiguously inside its region.

Territory Clarity

No straddling, no ambiguity about "which side does this belong to?" Content occupies clear territory.

Labels Don't Touch Lines

Circle labels, box labels — keep clear space from edges. Position labels at "clock positions" (10 o'clock, 2 o'clock) rather than centered above. Text inside shapes (cards, banners, rounded rectangles) should be inset 10-15px from borders on all sides — text touching shape edges looks cramped and accidental.

Fill the Space
Chart area should use ~80% of canvas (with ~10% margin from edges)
"Fill" means centered and balanced, not just "big enough"
If there's empty space at bottom, elements are undersized or poorly positioned
Scale elements uniformly to fill — never stretch text (aspect ratio is sacred)
Prefer splitting content across multiple visuals over shrinking everything to fit one. A diagram with 12 cramped boxes is a document, not a visual — 3-4 key elements per canvas is the sweet spot
Scatter, Don't Stack

When placing multiple detail items within a region (e.g., items inside a Venn circle), scatter them organically to fill the territory. Don't default to neat vertical stacks or bullet-list layouts — that's document thinking, not visual thinking. Let items breathe and occupy the space naturally. Stacking looks rigid; scattering looks designed.

Display Text Capitalisation

Labels and titles get consistent Title Case capitalisation.

Label Specificity

Review labels for specificity before finalising. Bare nouns often need modification to land:

"Naming" → "Consistent Naming"
"SME-friendly" → "SME-friendly tools"
"Models" → "Better predictive models"

Ask: would someone unfamiliar with the context understand what this means? If not, add the adjective.

Chesterton's Fence

Before removing any element, ask: "What job is this doing?"

Axis labels frame conceptual space (X vs Y dimensions)
Annotations provide meaning, not just labels ("This ad led to this click" ≠ "Last-click")
Width indicators reinforce messages the visual implies
Key/legend panels group meta-information
Don't mistake "explanation" for "noise"
Respect the Metaphor

Visual metaphors have rules. Breaking them breaks comprehension:

Ladder: rungs go INSIDE the rails, not wider than them
Venn: content belongs unambiguously in one region
Flow: arrows point in direction of flow
Tree: children below parents

If your visual breaks the metaphor's rules, the viewer's mental model breaks.

Less Is More (Especially Overlaps)

Not every region needs a label. In Venn diagrams, if an overlap's meaning is self-evident from the surrounding content, leave it empty. Labelling everything creates noise. The unlabelled center can be more powerful than a forced "synergy" label. Ask: does this label add meaning, or am I labelling because I feel I should?

No Orphan Elements

Everything needs a visual relationship to something else:

If a callout box floats alone, connect it (line, alignment, proximity)
Elements without relationships look like mistakes
Even "independent" items should align with something
No Emoji as Icons

Never use emoji or Unicode symbols as visual elements. They render inconsistently across platforms, browsers, and export formats. Use proper SVG shapes — a circle with a checkmark path, not ✅. A triangle with an exclamation mark, not ⚠️.

Key/Legend Placement

Hierarchy of preferences:

Best: No key needed — visual is self-explanatory
Acceptable: Contained key panel — all meta-info grouped in one area
Worst: Scattered meta-info — bits floating in different corners

If you need a key, contain it. If you're adding labels to explain what colors mean, the colors might not be working.

Key Specs
Element	Size	Notes
Title	36-40px	Largest, top hierarchy
Highlighted text	24-28px	Second hierarchy
Labels	20-24px	Circle/region labels
Content text	18-20px	Inside regions
Strokes	3-4px	Circle outlines, connectors
Composing with Brand Skills

When a brand skill exists:

Read its brand-guide.md for colors, fonts, specs
Apply those specs to your SVG
Brand skill may specify different canvas size

Example: For ITV-branded charts, also invoke the itv-styling skill.

Anti-Patterns
Pattern	Problem	Fix
Skip self-critique	Quality issues persist	Always render and check before showing user
Low contrast text	Illegible on projection	White/near-white on dark, WCAG 4.5:1 minimum, test at 50% zoom
Crowded layouts	Visual overload	3-4 key elements per visual, split rather than shrink
Wimpy size differences	Hierarchy invisible	2x minimum between levels (36px title / 18px body)
Text touching shape edges	Looks cramped	10-15px inset on all sides
Single fix, no re-check	New problems introduced	Two critique cycles minimum
Same dark background every time	Monotonous, mismatched tone	Vary palette to match content
Emoji as icons	Inconsistent rendering	Use SVG shapes
Skip brand check	Inconsistent styling	Load brand skill first when brand applies
References
references/design-principles.md — Full CRAP framework with SVG-specific interventions
references/slide-design-principles.md — Slide-specific thresholds (spacing, density, layout vocabulary). Load when output is for presentations. Universal rules (marked U) apply to all diagrams.
references/svg-interop.md — SVG editor compatibility notes
references/svg-recipes.md — Code snippets for common elements
Weekly Installs
32
Repository
spm1001/claude-suite
GitHub Stars
1
First Seen
Jan 31, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass