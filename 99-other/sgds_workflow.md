---
title: sgds-workflow
url: https://skills.sh/govtechsg/sgds-web-component/sgds-workflow
---

# sgds-workflow

skills/govtechsg/sgds-web-component/sgds-workflow
sgds-workflow
Installation
$ npx skills add https://github.com/govtechsg/sgds-web-component --skill sgds-workflow
SKILL.md
SGDS Skill Workflow

This skill maps out the available SGDS skills and the order to use them. Start here when unsure which skill applies, or to understand how skills fit together.

Are you starting a new app or working on an existing one?
New Application

Work through these stages in order. Within each stage, read the referenced skills as needed.

Stage 1 — Project Setup (always first)

→ Read sgds-getting-started

Covers: Inter font, CSS import order (themes/day.css → css/sgds.css → css/utility.css), component registration, and the two app layout templates (simple app vs sidebar app).

Complete all four steps in this skill before writing any component or page code.

Stage 2 — Build the UI (read concurrently as needed)

These skills are your day-to-day references while building. You will move between them frequently — read whichever is relevant to what you are building at any moment.

→ sgds-components — Every <sgds-*> web component (accordion through tooltip). Check here first before building anything with plain HTML. If an SGDS component exists for your need, use it.

→ sgds-utilities — All sgds: Tailwind utility classes: spacing, layout grid, typography, colors, borders, opacity. Use for layout, spacing, and styling between and around components.

→ Application Shell — Mandatory page chrome and layout templates (simple app and sidebar app) with sticky headers, sidebar column sizing, and container class reference. Read when sgds-getting-started Step 4 is not enough detail.

→ sgds-theming (optional) — Brand colour overrides, night/dark mode, and font customisation. Read this alongside the above when the app requires visual customisation beyond the default SGDS style. Skip if the default style is acceptable.

Stage 3 — Assemble Pages and Blocks (when building full pages or sections)

→ sgds-blocks — Reusable UI blocks for page sections and layouts. Includes: hero sections, CTAs, feature blocks, card grids, statistics displays, page headers, filters, forms, detail cards, application shell, and custom blocks. Start here when a user asks to build a landing page, dashboard, specific page section like "I need a call to action", or requests any page layout.

→ sgds-patterns — Typography and text patterns for consistent text styling: headings, display text, content headers, lists, and paragraphs. Use when styling content text, creating text hierarchies, or the user mentions "make a nice heading" or "style the page text".

→ sgds-templates — Ready-made full-page layouts: dashboard, login, form page, list page, settings. Start here when a user asks to build a complete page.

→ sgds-forms — Form submission, constraint validation, hasFeedback, setInvalid, and FormData. Read when any <form> with SGDS components is involved.

Stage 4 — Data Visualisation (if charts or dashboards are needed)

→ Read sgds-data-visualisation

Covers ECharts setup and applying the SGDS colour palette to charts. Only needed if the app includes charts, graphs, or data dashboards.

Existing Application

Do not re-read setup skills. Go directly to the skill that covers the current task.

Quick check — if utilities or components look broken, verify setup is complete before anything else:

themes/day.css → css/sgds.css → css/utility.css imported in that order in the main CSS file
utility.css is processed by Tailwind (not imported as a plain JS import)
import "@govtechsg/sgds-web-component" present in the JS entry point

If setup is confirmed correct, navigate using the table below.

Skill Map — What to Read for Each Task
What you need to do	Skill to read
Set up a new SGDS project from scratch	sgds-getting-started
Use any <sgds-*> component	sgds-components
Apply spacing, colors, typography, layout utilities	sgds-utilities
Structure the app shell (masthead, mainnav, footer, containers)	Application Shell
Change brand color, enable dark mode, change font	sgds-theming
Build page sections: hero, CTA, cards, feature, stats, filter, form, or custom blocks	sgds-blocks
Style text: headings, display text, lists, paragraphs	sgds-patterns
Build a full page (dashboard, login, list, form, settings)	sgds-templates
Add form validation, read FormData, use setInvalid	sgds-forms
Add charts, graphs, or data dashboards	sgds-data-visualisation
For AI Agents
When a user says "I'm building a new SGDS app" or "where do I start", always begin with sgds-getting-started (Stage 1) before reading any other skill.
During Stage 2, do not read all three skills upfront — read sgds-components when a component is needed and sgds-utilities when styling/layout is needed. They are references, not sequential reads.
sgds-theming is part of Stage 2 — read it concurrently with components and utilities when branding, dark mode, or font customisation is needed. Do not treat it as a separate sequential step.
sgds-blocks and sgds-patterns are concurrent Stage 3 skills — read them as needed based on user requests (blocks for page sections, patterns for text styling).
sgds-templates and sgds-blocks can be used independently or together — a user may need one, both, or neither depending on how far along they are.
sgds-forms is only needed when a <form> element is involved. Do not proactively read it for non-form UIs.
sgds-data-visualisation is only needed when charts or graphs are explicitly requested.
For existing apps, use the Skill Map table to navigate directly. Do not re-read sgds-getting-started unless there is a setup problem.
If a user's request does not clearly match any skill, read this workflow skill first to orient, then navigate to the appropriate skill.
Never use style attributes or inline CSS. All styling must be applied via class attributes using sgds: utility classes from sgds-utilities. Writing style="margin-top: 16px" when sgds:mt-4 exists is a violation.
Weekly Installs
49
Repository
govtechsg/sgds-…omponent
GitHub Stars
12
First Seen
Mar 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass