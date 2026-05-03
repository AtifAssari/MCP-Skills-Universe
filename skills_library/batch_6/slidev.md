---
title: slidev
url: https://skills.sh/slidevjs/slidev/slidev
---

# slidev

skills/slidevjs/slidev/slidev
slidev
Originally fromantfu/skills
Installation
$ npx skills add https://github.com/slidevjs/slidev --skill slidev
Summary

Web-based slidedecks for developers with Markdown, Vue components, live code editing, and interactive animations.

Supports syntax-highlighted code with line-by-line animations, Monaco editor integration, and runnable code blocks
Includes 15+ built-in layouts (cover, two-cols, image, iframe, quote, section) and diagram support (Mermaid, PlantUML, LaTeX)
Export to PDF, PPTX, PNG, or deploy as a static SPA; includes presenter mode with recording, timer, and remote control
Built-in drawing mode, click-based animations (v-click), rough markers, and draggable elements for interactive presentations
SKILL.md
Slidev - Presentation Slides for Developers

Web-based slides maker built on Vite, Vue, and Markdown.

When to Use
Technical presentations or slidedecks with live code examples
Syntax-highlighted code snippets with animations
Interactive demos (Monaco editor, runnable code)
Mathematical equations (LaTeX) or diagrams (Mermaid, PlantUML)
Record presentations with presenter notes
Export to PDF, PPTX, or host as SPA
Code walkthroughs for developer talks or workshops
Quick Start
pnpm create slidev    # Create project
pnpm run dev          # Start dev server (opens http://localhost:3030)
pnpm run build        # Build static SPA
pnpm run export       # Export to PDF (requires playwright-chromium)


Verify: After pnpm run dev, confirm slides load at http://localhost:3030. After pnpm run export, check the output PDF exists in the project root.

Basic Syntax
---
theme: default
title: My Presentation
---

# First Slide

Content here

---

# Second Slide

More content

<!--
Presenter notes go here
-->

--- separates slides
First frontmatter = headmatter (deck config)
HTML comments = presenter notes
Core References
Topic	Description	Reference
Markdown Syntax	Slide separators, frontmatter, notes, code blocks	core-syntax
Animations	v-click, v-clicks, motion, transitions	core-animations
Headmatter	Deck-wide configuration options	core-headmatter
Frontmatter	Per-slide configuration options	core-frontmatter
CLI Commands	Dev, build, export, theme commands	core-cli
Components	Built-in Vue components	core-components
Layouts	Built-in slide layouts	core-layouts
Exporting	PDF, PPTX, PNG export options	core-exporting
Hosting	Build and deploy to various platforms	core-hosting
Global Context	$nav, $slidev, composables API	core-global-context
Feature Reference
Code & Editor
Feature	Usage	Reference
Line highlighting	```ts {2,3}	code-line-highlighting
Click-based highlighting	```ts {1|2-3|all}	code-line-highlighting
Line numbers	lineNumbers: true or {lines:true}	code-line-numbers
Scrollable code	{maxHeight:'100px'}	code-max-height
Code tabs	::code-group (requires comark: true)	code-groups
Monaco editor	```ts {monaco}	editor-monaco
Run code	```ts {monaco-run}	editor-monaco-run
Edit files	<<< ./file.ts {monaco-write}	editor-monaco-write
Code animations	````md magic-move	code-magic-move
TypeScript types	```ts twoslash	code-twoslash
Import code	<<< @/snippets/file.js	code-import-snippet
Diagrams & Math
Feature	Usage	Reference
Mermaid diagrams	```mermaid	diagram-mermaid
PlantUML diagrams	```plantuml	diagram-plantuml
LaTeX math	$inline$ or $$block$$	diagram-latex
Layout & Styling
Feature	Usage	Reference
Canvas size	canvasWidth, aspectRatio	layout-canvas-size
Zoom slide	zoom: 0.8	layout-zoom
Scale elements	<Transform :scale="0.5">	layout-transform
Layout slots	::right::, ::default::	layout-slots
Scoped CSS	<style> in slide	style-scoped
Global layers	global-top.vue, global-bottom.vue	layout-global-layers
Draggable elements	v-drag, <v-drag>	layout-draggable
Icons	<mdi-icon-name />	style-icons
Animation & Interaction
Feature	Usage	Reference
Click animations	v-click, <v-clicks>	core-animations
Rough markers	v-mark.underline, v-mark.circle	animation-rough-marker
Drawing mode	Press C or config drawings:	animation-drawing
Direction styles	forward:delay-300	style-direction
Note highlighting	[click] in notes	animation-click-marker
Syntax Extensions
Feature	Usage	Reference
Comark syntax	comark: true + {style="color:red"}	syntax-comark
Block frontmatter	```yaml instead of ---	syntax-block-frontmatter
Import slides	src: ./other.md	syntax-importing-slides
Merge frontmatter	Main entry wins	syntax-frontmatter-merging
Presenter & Recording
Feature	Usage	Reference
Recording	Press G for camera	presenter-recording
Timer	duration: 30min, timer: countdown	presenter-timer
Remote control	slidev --remote	presenter-remote
Ruby text	notesAutoRuby:	presenter-notes-ruby
Export & Build
Feature	Usage	Reference
Export options	slidev export	core-exporting
Build & deploy	slidev build	core-hosting
Build with PDF	download: true	build-pdf
Cache images	Automatic for remote URLs	build-remote-assets
OG image	seoMeta.ogImage or og-image.png	build-og-image
SEO tags	seoMeta:	build-seo-meta

Export prerequisite: pnpm add -D playwright-chromium is required for PDF/PPTX/PNG export. If export fails with a browser error, install this dependency first.

Editor & Tools
Feature	Usage	Reference
Side editor	Click edit icon	editor-side
VS Code extension	Install antfu.slidev	editor-vscode
Prettier	prettier-plugin-slidev	editor-prettier
Eject theme	slidev theme eject	tool-eject-theme
Lifecycle & API
Feature	Usage	Reference
Slide hooks	onSlideEnter(), onSlideLeave()	api-slide-hooks
Navigation API	$nav, useNav()	core-global-context
Common Layouts
Layout	Purpose
cover	Title/cover slide
center	Centered content
default	Standard slide
two-cols	Two columns (use ::right::)
two-cols-header	Header + two columns
image / image-left / image-right	Image layouts
iframe / iframe-left / iframe-right	Embed URLs
quote	Quotation
section	Section divider
fact / statement	Data/statement display
intro / end	Intro/end slides
Resources
Documentation: https://sli.dev
Theme Gallery: https://sli.dev/resources/theme-gallery
Showcases: https://sli.dev/resources/showcases
Weekly Installs
4.8K
Repository
slidevjs/slidev
GitHub Stars
46.2K
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn