---
title: tenzir-design-system
url: https://skills.sh/tenzir/skills/tenzir-design-system
---

# tenzir-design-system

skills/tenzir/skills/tenzir-design-system
tenzir-design-system
Installation
$ npx skills add https://github.com/tenzir/skills --skill tenzir-design-system
SKILL.md
Tenzir Design System

Use the shared Tenzir design system when implementing frontend UI.

Start Here
Identify whether the task needs design tokens, a standard component, or a logo asset.
Load only the reference files needed for the current component or styling problem.
Prefer design tokens and existing component patterns over bespoke styling.
Design Tokens

Load these references as needed:

typography
colors
spacing
shadows
border radius

Use the --tnz- CSS custom-property prefix for design-system tokens.

Component References

Load the relevant reference before implementing the component:

buttons
dropdown
hyperlinks
segmented control
input field
search input
checkbox
radio button
toggle switch
tag
badge
tab bar
toast
Assets

Official logo files live in assets/logos/:

logo.svg
logo-white.svg
logomark.svg
logomark-white.svg

Use these assets for Tenzir products and integrations that should follow the official brand system.

Weekly Installs
29
Repository
tenzir/skills
GitHub Stars
1
First Seen
Mar 11, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass