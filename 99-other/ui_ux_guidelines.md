---
title: ui-ux-guidelines
url: https://skills.sh/jgamaraalv/ts-dev-kit/ui-ux-guidelines
---

# ui-ux-guidelines

skills/jgamaraalv/ts-dev-kit/ui-ux-guidelines
ui-ux-guidelines
Installation
$ npx skills add https://github.com/jgamaraalv/ts-dev-kit --skill ui-ux-guidelines
SKILL.md
Web Interface Guidelines

Dispatch hub for UI/UX rules. Load the relevant reference file for full details.

Rule Categories by Priority
Priority	Category	Impact	Reference File
1	Accessibility	CRITICAL	accessibility-and-interaction
2	Touch & Interaction	CRITICAL	accessibility-and-interaction
3	Performance	HIGH	layout-typography-animation
4	Layout & Responsive	HIGH	layout-typography-animation
5	Typography & Color	MEDIUM	layout-typography-animation
6	Animation	MEDIUM	layout-typography-animation
7	Forms	HIGH	forms-content-checklist
8	Content & Navigation	MEDIUM	forms-content-checklist
9	Charts & Data	LOW	layout-typography-animation
Workflows

<phase_1_review_ui>

Review UI code
Read the target file(s).
Load the relevant reference file(s) from references/ based on what the code contains.
Check each applicable rule. Report violations in the output format below. </phase_1_review_ui>

<phase_2_build_component>

Build new component
Load references/accessibility-and-interaction.md -- all components must meet CRITICAL rules.
Load additional references based on component type:
Form component -> references/forms-content-checklist.md
Layout/visual component -> references/layout-typography-animation.md
Follow rules during implementation. </phase_2_build_component>

<phase_3_pre_delivery>

Pre-delivery checklist
Load references/forms-content-checklist.md for the full checklist.
Load references/accessibility-and-interaction.md for the interaction checklist.
Walk through every checkbox before shipping. </phase_3_pre_delivery>

<anti_patterns>

Anti-patterns (flag these)
user-scalable=no or maximum-scale=1 -- disables zoom
onPaste with preventDefault -- blocks paste
transition: all -- list properties explicitly
outline-none without :focus-visible replacement
<div>/<span> with click handlers -- use <button> or <a>
<img> without width and height (causes CLS)
Inline onClick navigation without <a> (breaks Cmd+click)
Large .map() without virtualization (>50 items)
Hardcoded date/number formats -- use Intl.*
Icon-only buttons without aria-label

</anti_patterns>

Code Review Output Format

Group findings by file. Use file:line format (VS Code clickable). Be terse -- state issue and location. Skip explanation unless fix is non-obvious.

See template.md for the expected output format.

Reference Files

Load these as needed during reviews and implementation:

Accessibility & Interaction -- Focus, ARIA, keyboard, touch targets, cursors, drag UX
Layout, Typography & Animation -- Performance, responsive, fonts, color, motion, charts
Forms, Content & Checklist -- Forms, content handling, navigation, dark mode, locale, hydration, pre-delivery checklist
Weekly Installs
25
Repository
jgamaraalv/ts-dev-kit
GitHub Stars
14
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass