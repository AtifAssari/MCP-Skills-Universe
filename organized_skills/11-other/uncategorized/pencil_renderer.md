---
rating: ⭐⭐
title: pencil-renderer
url: https://skills.sh/phrazzld/claude-config/pencil-renderer
---

# pencil-renderer

skills/phrazzld/claude-config/pencil-renderer
pencil-renderer
Installation
$ npx skills add https://github.com/phrazzld/claude-config --skill pencil-renderer
SKILL.md
Pencil Renderer

Translate aesthetic DNA codes into Pencil .pen frames via MCP.

Interface

Input:

DNA code: [layout, color, typography, motion, density, background]
Component type: hero | card | form | nav | footer | section | button | input
Optional: Name, dimensions, parent frame ID

Output:

Frame ID in .pen file
Screenshot of rendered frame
Workflow
1. Ensure Document Ready
// Check if editor open
mcp__pencil__get_editor_state({ include_schema: false })

// If no editor, open or create
mcp__pencil__open_document({ filePathOrTemplate: "new" })

2. Get Style Foundation
// Get available style guide tags
mcp__pencil__get_style_guide_tags()

// Get style guide matching DNA mood
// Map DNA to relevant tags:
// - dark color → ["dark-mode", "moody"]
// - light color → ["light", "clean"]
// - spacious density → ["airy", "whitespace"]
// etc.
mcp__pencil__get_style_guide({ tags: [mapped_tags] })

3. Translate DNA to Pencil Properties

Reference: references/dna-to-pencil.md

DNA axis → Pencil property mapping is deterministic. Example: centered layout → alignItems: "center", symmetric padding

4. Execute Design Operations

Reference: references/batch-design-patterns.md

mcp__pencil__batch_design({
  filePath: "<path>.pen",
  operations: `
    frame=I(document, {type: "frame", name: "Hero-Brutalist", ...properties})
    heading=I(frame, {type: "text", content: "Headline", ...typography})
    // ... additional operations
  `
})

5. Capture Result
// Screenshot for visual verification
mcp__pencil__get_screenshot({ nodeId: "frameId" })

6. Return
Frame ID: [id]
DNA: [layout, color, typography, motion, density, background]


Plus screenshot image.

Component Templates
Type	Structure
hero	Container + headline + subhead + CTA buttons
card	Container + image area + content + actions
form	Container + labels + inputs + submit
nav	Container + logo + links + actions
footer	Container + columns + links + legal
section	Container + heading + content grid
button	Frame + text + icon slot
input	Frame + label + field + validation
DNA Translation Quick Reference
DNA Axis	Key Pencil Properties
Layout: centered	alignItems: "center", equal padding
Layout: asymmetric	Offset positions, varied gaps
Layout: bento	Grid with varied spans
Color: dark	Dark fill, light foreground
Color: gradient	fill: {type: "linear", stops: [...]}
Typography: display-heavy	Large heading sizes, high contrast
Typography: minimal	Restrained scale, single family
Density: spacious	gap: 24-48, generous padding
Density: compact	gap: 8-16, tight padding
Background: solid	Single fill color
Background: textured	G() for patterns/images
Constraints
Single concern: Render DNA → frame. No interview, no iteration.
Pencil MCP required: Fails fast if unavailable
Deterministic mapping: Same DNA always produces same structure
Composable: Called by orchestrators, not users directly
References
references/dna-to-pencil.md — Complete axis mapping
references/batch-design-patterns.md — Common operation sequences
aesthetic-system/references/dna-codes.md — DNA axis definitions
Integration

Called by:

design-exploration orchestrator (when Pencil backend available)

Composes:

aesthetic-system (for DNA interpretation)
Weekly Installs
112
Repository
phrazzld/claude-config
GitHub Stars
8
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass