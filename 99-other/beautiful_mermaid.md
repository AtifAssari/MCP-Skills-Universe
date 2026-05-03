---
title: beautiful-mermaid
url: https://skills.sh/alexmikhalev/beautiful-mermaid/beautiful-mermaid
---

# beautiful-mermaid

skills/alexmikhalev/beautiful-mermaid/beautiful-mermaid
beautiful-mermaid
Installation
$ npx skills add https://github.com/alexmikhalev/beautiful-mermaid --skill beautiful-mermaid
SKILL.md
Beautiful Mermaid Diagram Rendering

Render Mermaid diagrams as SVG (for UIs) or ASCII/Unicode (for terminals and markdown).

Quick Start
1. Install Dependencies
npm install beautiful-mermaid


Or run the setup script:

bash scripts/setup.sh

2. Render SVG
import { renderMermaid } from 'beautiful-mermaid'

const svg = await renderMermaid(`
  graph LR
    A[Start] --> B{Decision}
    B -->|Yes| C[Action]
    B -->|No| D[End]
`)

3. Render ASCII
import { renderMermaidAscii } from 'beautiful-mermaid'

const ascii = renderMermaidAscii(`graph LR; A --> B --> C`)
// Output:
// +---+     +---+     +---+
// | A |---->| B |---->| C |
// +---+     +---+     +---+

Core API
renderMermaid(text, options?): Promise<string>

Returns SVG string. Options:

Option	Type	Default	Description
bg	string	"#FFFFFF"	Background color
fg	string	"#27272A"	Foreground color
font	string	"Inter"	Font family
transparent	boolean	false	Transparent background
line	string	auto	Edge/connector color
accent	string	auto	Arrow heads, highlights
muted	string	auto	Secondary text, labels
surface	string	auto	Node fill tint
border	string	auto	Node stroke
renderMermaidAscii(text, options?): string

Returns ASCII/Unicode string. Synchronous. Options:

Option	Type	Default	Description
useAscii	boolean	false	Use ASCII chars instead of Unicode
paddingX	number	5	Horizontal node spacing
paddingY	number	5	Vertical node spacing
boxBorderPadding	number	1	Inner box padding
Theming
Mono Mode (Two Colors)

Provide only bg and fg. All other colors are derived automatically:

const svg = await renderMermaid(diagram, {
  bg: '#1a1b26',
  fg: '#a9b1d6'
})

Built-in Themes
import { renderMermaid, THEMES } from 'beautiful-mermaid'

const svg = await renderMermaid(diagram, THEMES['tokyo-night'])


Available themes: zinc-light, zinc-dark, tokyo-night, tokyo-night-storm, tokyo-night-light, catppuccin-mocha, catppuccin-latte, nord, nord-light, dracula, github-light, github-dark, solarized-light, solarized-dark, one-dark.

Shiki Theme Integration
import { getSingletonHighlighter } from 'shiki'
import { renderMermaid, fromShikiTheme } from 'beautiful-mermaid'

const highlighter = await getSingletonHighlighter({
  themes: ['vitesse-dark']
})
const colors = fromShikiTheme(highlighter.getTheme('vitesse-dark'))
const svg = await renderMermaid(diagram, colors)


See themes.md for complete theming reference.

Supported Diagrams
Type	Syntax	Example
Flowchart	graph TD/LR/BT/RL	graph LR; A --> B
State	stateDiagram-v2	stateDiagram-v2\n[*] --> Active
Sequence	sequenceDiagram	sequenceDiagram\nAlice->>Bob: Hello
Class	classDiagram	`classDiagram\nAnimal <
ER	erDiagram	`erDiagram\nCUSTOMER
Common Patterns
Save SVG to File
import { renderMermaid, THEMES } from 'beautiful-mermaid'
import { writeFile } from 'fs/promises'

const svg = await renderMermaid(diagram, THEMES['github-dark'])
await writeFile('diagram.svg', svg)

Generate ASCII for Markdown
import { renderMermaidAscii } from 'beautiful-mermaid'

const ascii = renderMermaidAscii(diagram, { useAscii: true })
const markdown = `## Architecture\n\n\`\`\`\n${ascii}\n\`\`\``

Live Theme Switching (Browser)

SVG output uses CSS custom properties. Switch themes without re-rendering:

svgElement.style.setProperty('--bg', '#282a36')
svgElement.style.setProperty('--fg', '#f8f8f2')

Reference Files
File	Contents
themes.md	Complete theming guide, color derivation, custom themes
ascii-rendering.md	ASCII mode options, Unicode vs ASCII, formatting
Troubleshooting

"Cannot find module 'beautiful-mermaid'": Run npm install beautiful-mermaid

Empty SVG output: Verify Mermaid syntax is valid. Test at mermaid.live first.

Fonts not rendering: Ensure the font is available. Use web-safe fonts or embed font CSS.

Weekly Installs
23
Repository
alexmikhalev/be…-mermaid
GitHub Stars
1
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass