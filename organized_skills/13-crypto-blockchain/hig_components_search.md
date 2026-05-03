---
rating: ⭐⭐
title: hig-components-search
url: https://skills.sh/raintree-technology/apple-hig-skills/hig-components-search
---

# hig-components-search

skills/raintree-technology/apple-hig-skills/hig-components-search
hig-components-search
Installation
$ npx skills add https://github.com/raintree-technology/apple-hig-skills --skill hig-components-search
SKILL.md
Apple HIG: Navigation Components

Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

Key Principles

Search: discoverable with instant feedback. Place search fields where users expect them (top of list, toolbar/navigation bar). Show results as the user types.

Page controls: position in a flat page sequence. For discrete, equally weighted pages (onboarding, photo gallery). Show current page and total count.

Path controls: file hierarchy navigation. macOS path controls display location within a directory structure and allow jumping to any ancestor.

Search scopes narrow large result sets. Provide scope buttons so users can filter without complex queries.

Clear empty states for search. Helpful message suggesting corrections or alternatives, not a blank screen.

Page controls are not for hierarchical navigation. Flat, linear sequences only. Use navigation controllers, tab bars, or sidebars for hierarchy.

Keep path controls concise. Show meaningful segments only. Users can click any segment to navigate directly.

Support keyboard for search. Command-F and system search shortcuts should activate search.

Reference Index
Reference	Topic	Key content
search-fields.md	Search fields	Scopes, tokens, instant results, placement
page-controls.md	Page controls	Dot indicators, flat page sequences
path-controls.md	Path controls	Breadcrumbs, ancestor navigation
Output Format
Component recommendation -- search field, page control, or path control, and why.
Behavior specification -- interaction model (search-as-you-type, swipe for pages, click-to-navigate for paths).
Platform differences across iOS, iPadOS, macOS, visionOS.
Questions to Ask
What type of content is being searched or navigated?
Which platforms?
How large is the dataset?
Is search the primary interaction?
Related Skills
hig-components-menus -- Toolbars and menu bars hosting search and navigation controls
hig-components-controls -- Text fields, pickers, segmented controls in search interfaces
hig-components-dialogs -- Popovers and sheets for expanded search or filtering
hig-patterns -- Navigation patterns and information architecture
hig-foundations -- Typography and layout for navigation components

Built by Raintree Technology · More developer tools

Weekly Installs
152
Repository
raintree-techno…g-skills
GitHub Stars
45
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass