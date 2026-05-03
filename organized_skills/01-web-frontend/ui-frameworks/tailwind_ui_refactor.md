---
rating: ⭐⭐
title: tailwind-ui-refactor
url: https://skills.sh/pproenca/dot-skills/tailwind-ui-refactor
---

# tailwind-ui-refactor

skills/pproenca/dot-skills/tailwind-ui-refactor
tailwind-ui-refactor
Installation
$ npx skills add https://github.com/pproenca/dot-skills --skill tailwind-ui-refactor
SKILL.md
Refactoring UI Tailwind CSS Best Practices

Comprehensive UI refactoring guide based on Refactoring UI by Adam Wathan & Steve Schoger, implemented with Tailwind CSS utility classes. Contains 52 rules across 9 categories, prioritized by design impact to guide automated refactoring and code generation. Uses Tailwind CSS v4 syntax (v3 notes provided where syntax differs).

Important: Think first, style second. Before applying any visual rule, understand the UI's purpose, identify what matters to the user, and remove unnecessary elements. The Design Intent category (priority 1) must be considered before any styling changes. A simpler component with fewer elements always beats a decorated component with unnecessary markup.

When to Apply

Reference these guidelines when:

Refactoring existing Tailwind CSS components
Writing new UI with Tailwind utility classes
Reviewing code for visual hierarchy and spacing issues
Improving design quality without a designer
Fixing accessibility contrast problems
Rule Categories by Priority
Priority	Category	Impact	Prefix
1	Design Intent	CRITICAL	intent-
2	Visual Hierarchy	CRITICAL	hier-
3	Layout & Spacing	CRITICAL	space-
4	Typography	HIGH	type-
5	Color Systems	HIGH	color-
6	Depth & Shadows	MEDIUM	depth-
7	Borders & Separation	MEDIUM	sep-
8	Images & Content	LOW-MEDIUM	img-
9	Polish & Details	LOW	polish-
Quick Reference
1. Design Intent (CRITICAL)
intent-audit-before-styling - Audit what each element communicates before changing any CSS
intent-remove-before-decorating - Remove unnecessary elements before styling what remains
intent-reduce-cognitive-load - Reduce choices per screen — fewer options beat prettier options
intent-progressive-disclosure - Hide secondary information behind interactions
intent-content-drives-layout - Let real content determine layout — not the other way around
intent-simplify-over-decorate - Prefer removing a wrapper over adding 5 utility classes to it
intent-match-context-fidelity - Match design polish to context — admin vs consumer vs product
intent-match-existing-patterns - Audit sibling component patterns before restyling
2. Visual Hierarchy (CRITICAL)
hier-size-weight-color - Use size, weight, and color for hierarchy — not just size
hier-deemphasize-secondary - De-emphasize secondary content instead of emphasizing primary
hier-button-hierarchy - Style buttons by visual hierarchy, not semantic importance
hier-label-value-pairs - Combine labels and values into natural language
hier-semantic-vs-visual - Separate visual hierarchy from document hierarchy
hier-icon-sizing - Size icons relative to adjacent text, not to fill space
hier-color-hierarchy-on-dark - Use opacity or muted colors for hierarchy on colored backgrounds
3. Layout & Spacing (CRITICAL)
space-start-generous - Start with too much whitespace, then remove
space-systematic-scale - Use a constrained spacing scale, not arbitrary values
space-relationship-proximity - Use spacing to show relationships between elements
space-dont-fill-screen - Constrain content width — avoid filling the whole screen
space-grids-not-required - Use fixed widths when grids are not needed
space-relative-sizing-fails - Avoid raw viewport units without clamping
space-mobile-first - Design mobile-first at ~400px, then expand
4. Typography (HIGH)
type-line-length - Keep line length between 45-75 characters
type-line-height-inverse - Line height and font size are inversely proportional
type-font-weight-variety - Choose fonts with at least 5 weight variations
type-no-center-long-text - Left-align body content — avoid centering long-form text
type-letter-spacing - Tighten letter spacing for headlines, loosen for uppercase
type-align-numbers-right - Align numbers right in tables for easy comparison
5. Color Systems (HIGH)
color-define-palette-upfront - Define a complete color palette upfront — don't pick colors ad-hoc
color-grayscale-first - Design in grayscale first, add color last
color-accessible-contrast - Ensure 4.5:1 contrast ratio for body text
color-dark-gray-not-black - Use dark gray instead of pure black for text
color-saturated-grays - Add subtle saturation to grays for warmth or coolness
color-light-backgrounds-dark-text - Use light-colored backgrounds with dark text for badges
6. Depth & Shadows (MEDIUM)
depth-shadow-scale - Define a fixed shadow scale — small to extra large
depth-shadow-vertical-offset - Use vertical offset for natural-looking shadows
depth-interactive-elevation - Use shadow changes to communicate interactivity
depth-light-closer-dark-recedes - Lighter colors feel closer, darker colors recede
depth-overlap-layers - Overlap elements to create visual layers
7. Borders & Separation (MEDIUM)
sep-fewer-borders - Use fewer borders — replace with spacing, shadows, or background color
sep-background-color-separation - Use background color differences to separate sections
sep-table-spacing-not-lines - Use spacing instead of lines in simple tables
sep-card-radio-buttons - Upgrade radio buttons to selectable cards for key choices
8. Images & Content (LOW-MEDIUM)
img-control-user-content - Control user-uploaded image size and aspect ratio
img-text-overlay - Add overlays or reduce contrast for text over images
img-dont-scale-up-icons - Avoid scaling up icons designed for small sizes
img-empty-states - Design meaningful empty states with clear CTAs
9. Polish & Details (LOW)
polish-accent-borders - Add accent borders to highlight important elements
polish-custom-bullets - Replace default bullets with icons or checkmarks
polish-border-radius-personality - Match border radius to brand personality
polish-gradient-close-hues - Use gradients with hues within 30 degrees of each other
polish-inner-shadow-images - Add inner shadow to prevent image background bleed
Scope & Limitations

This skill covers layout, hierarchy, spacing, color, and polish based on Refactoring UI principles. It does NOT cover:

Font selection & pairing — choosing distinctive typefaces, avoiding generic AI defaults (Inter, Arial, system-ui), or pairing display + body fonts
Animation & motion — meaningful transitions, micro-interactions, page load sequences, or scroll-triggered reveals
Creative direction — establishing an aesthetic vision, choosing a tone (minimal, maximalist, brutalist, etc.), or differentiating from generic "AI slop" aesthetics
Spatial composition — asymmetric layouts, grid-breaking elements, or unconventional visual flow

For these concerns, pair this skill with a design-thinking or frontend-design skill that covers creative direction and aesthetic execution.

How to Use

Read individual reference files for detailed explanations and code examples:

Section definitions - Category structure and impact levels
Rule template - Template for adding new rules
Reference Files
File	Description
references/_sections.md	Category definitions and ordering
assets/templates/_template.md	Template for new rules
metadata.json	Version and reference information
Weekly Installs
232
Repository
pproenca/dot-skills
GitHub Stars
132
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass