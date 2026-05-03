---
title: email-html-mjml
url: https://skills.sh/framix-team/skill-email-html-mjml/email-html-mjml
---

# email-html-mjml

skills/framix-team/skill-email-html-mjml/email-html-mjml
email-html-mjml
Installation
$ npx skills add https://github.com/framix-team/skill-email-html-mjml --skill email-html-mjml
SKILL.md
email-html-mjml — Responsive Email Developer

Generate valid, cross-client MJML 4.x templates and compile them to production-ready HTML. The primary goal is compatibility: Outlook (2013–365), Gmail (web/app), Apple Mail, and major mobile clients. Every output must be compilable with --config.validationLevel=strict and survive Gmail's 102KB clip limit.

Workflow
Gather requirements — Infer email type, brand colors, and content from the user's message and conversation context. Ask only for what is genuinely missing and blocking progress (e.g., no colors provided and the layout has branded sections). Never front-load a questionnaire.
Plan layout — Decide and announce the structure before writing code (single-column, 2-col grid, hero + content, etc.)
Load component references — Read the relevant file(s) from the Component Index below before writing any MJML
Generate MJML — Write complete, valid MJML starting from <mjml> with a full <mj-head>
Compile — Follow compilation.md. Run npx mjml with --config.minify=true
Deliver both files — Always output .mjml source AND compiled .html
9 Engineering Rules
Structural Integrity — All visual content MUST be in <mj-column> inside <mj-section>. Sections cannot be nested.
Responsive Defaults — Assume 600px width. Use <mj-group> to prevent mobile stacking for side-by-side elements (social bars, logo rows).
Outlook Compatibility — Use <mj-font> for web fonts (prevents Times New Roman fallback). Always provide a fallback stack (Arial, sans-serif). For <mj-section> background images, always set both background-size and a fallback background-color.
Gmail Optimization — Use inline="inline" on <mj-style> for custom CSS. Prefer component attributes (color, font-size) over CSS classes for critical styles.
Dark Mode — Include dark mode support when explicitly requested or when the email has a light background that would cause harsh forced-inversion. See the Dark Mode Pattern below.
Accessibility — Every <mj-image> MUST have alt. Always set <mj-title> (populates aria-label). Maintain WCAG 2.1 AA 4.5:1 contrast. For heading roles, use mj-html-attributes — direct role/aria-level attributes on mj-text are illegal under strict validation (see Accessibility Checklist below).
Styling Efficiency — Use <mj-attributes> with <mj-all>, component defaults, and <mj-class> to eliminate repetitive inline styles.
Hero Sections — Use <mj-hero> for full-bleed hero banners; it falls back to a regular section in unsupported clients. Avoid <mj-accordion> and <mj-carousel> — client support is too poor to be useful.
Templating Support — Wrap dynamic tags (Handlebars/Liquid) in <mj-raw> to protect them from the MJML parser.
Critical Gotchas

Outlook:

Background images: VML only generated for <mj-section> and <mj-hero> — nowhere else
Background positioning: keyword values only (top, center, bottom) — pixel values ignored
Always pair background-repeat="no-repeat" with explicit background-size
Font fallback: <mj-font> hides @font-face from Outlook via MSO conditional comments

Gmail:

Use component attributes for critical layout — CSS classes may be stripped
102KB clip: always compile with --config.minify=true

iOS / Android stacking:

Always compile with --config.minify=true — removes whitespace between inline-block columns
Whitespace between tags causes stacking even inside <mj-group>

Vertical-align bug:

If any column in a section sets vertical-align, ALL columns in that section must explicitly set it

JavaScript:

JS is completely blocked in all email clients (Gmail, Outlook, Apple Mail, iOS Mail). No onclick, no clipboard API, no interactivity of any kind. Interactive-looking elements (copy buttons, toggles) are purely decorative.
Dark Mode Pattern
<mj-head>
  <mj-raw>
    <meta name="color-scheme" content="light dark">
    <meta name="supported-color-schemes" content="light dark">
  </mj-raw>

  <!-- Light logo visible by default; dark logo hidden -->
  <mj-style inline="inline">
    .dark-logo { display: none !important; }
  </mj-style>

  <!-- Dark mode overrides -->
  <mj-style>
    @media (prefers-color-scheme: dark) {
      .light-logo { display: none !important; }
      .dark-logo  { display: block !important; }
    }
  </mj-style>
</mj-head>


Safe neutrals: #121212 (not #000000) and #F1F1F1 (not #FFFFFF) — prevents jarring forced inversions.

Accessibility Checklist
<mj-title> is set (screen reader email label + aria-label)
lang attribute on root <mjml> tag
alt on every <mj-image> and <mj-social-element>
Heading role set via mj-html-attributes (NOT as a direct attribute on mj-text):
<!-- In mj-head -->
<mj-html-attributes>
  <mj-selector path=".email-heading div">
    <mj-html-attribute name="role">heading</mj-html-attribute>
    <mj-html-attribute name="aria-level">1</mj-html-attribute>
  </mj-selector>
</mj-html-attributes>
<!-- On the component -->
<mj-text css-class="email-heading" ...>Heading text</mj-text>

4.5:1 contrast ratio on all text/background pairs
No text baked into images — always use live <mj-text> blocks
Component Index

Before writing any MJML, read the component file(s) for the components you'll use.

Group	Components	Load when	File
Head	mj-attributes, mj-font, mj-style, mj-preview, mj-breakpoint, mj-html-attributes	Setting up head, global styles	components/head.md
Layout	mj-body, mj-section, mj-column, mj-group, mj-wrapper	Building structure / grid	components/layout.md
Content	mj-text, mj-image, mj-button, mj-divider, mj-spacer, mj-table	Adding content blocks	components/content.md
Interactive	mj-accordion, mj-carousel, mj-social, mj-navbar	Interactive or social elements	components/interactive.md
Advanced	mj-hero, mj-raw, mj-include	Hero banners, template tags, partials	components/advanced.md

General reference (hierarchy, ending tags, validation, width math, Gmail clip): mjml-reference.md

Compilation

Read compilation.md for the full workflow. Key command:

npx mjml template.mjml -o dist/template.html --config.minify=true --config.validationLevel=strict


Hard rules:

Never npm install -g mjml
Always use npx or ./node_modules/.bin/mjml
If mjml not in package.json, suggest npm install -D mjml
Examples

assets/examples/basic-layout.mjml — MJML docs basic layout example. Covers 6-section structure: company header, image hero + button, intro text, 2-column image+text, 3-column icons, social row. Intentionally bare-bones (no mj-head, no dark mode, placeholder copy) — reflects the MJML docs style. Use as a structural reference for layout patterns only, not as a production template.

Output

Always deliver:

<name>.mjml — complete MJML source (editable, version-controllable)
<name>.html — compiled output (production-ready, send via ESP)

Name files after the email type: welcome.mjml, promo-sale.mjml, order-confirmation.mjml

Weekly Installs
226
Repository
framix-team/ski…tml-mjml
GitHub Stars
32
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass