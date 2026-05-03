---
rating: ⭐⭐
title: hig-components-menus
url: https://skills.sh/raintree-technology/apple-hig-skills/hig-components-menus
---

# hig-components-menus

skills/raintree-technology/apple-hig-skills/hig-components-menus
hig-components-menus
Installation
$ npx skills add https://github.com/raintree-technology/apple-hig-skills --skill hig-components-menus
SKILL.md
Apple HIG: Menus and Buttons

Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

Key Principles

Menus should be contextual and predictable. Standard items in standard locations. Follow platform conventions for ordering and grouping.

Use standard button styles. System-defined styles communicate affordance and maintain visual consistency. Prefer them over custom designs.

Toolbars for frequent actions. Most commonly used commands in the toolbar. Rarely used actions belong in menus.

Menu bar is the primary command interface on macOS. Every command reachable from the menu bar. Toolbars and context menus supplement, not replace.

Context menus for secondary actions. Right-click or long-press, relevant to the item under the pointer. Never put a command only in a context menu.

Pop-up buttons for mutually exclusive choices. Select exactly one option from a set.

Pull-down buttons for action lists. No current selection; they offer a set of commands.

Action buttons consolidate related actions behind a single icon in toolbars or title bars.

Disclosure controls for progressive disclosure. Show or hide additional content.

Dock menus: short and focused on the most useful actions when the app is running.

Reference Index
Reference	Topic	Key content
menus.md	General menu design	Item ordering, grouping, shortcuts
context-menus.md	Context menus	Right-click, long press, secondary actions
dock-menus.md	Dock menus	macOS app-level actions, running state
edit-menus.md	Edit menus	Undo, copy, paste, standard items
the-menu-bar.md	Menu bar	macOS primary command interface, structure
toolbars.md	Toolbars	Frequent actions, customization, placement
buttons.md	Buttons	System styles, sizing, affordance
action-button.md	Action button	Grouped secondary actions, toolbar use
pop-up-buttons.md	Pop-up buttons	Mutually exclusive choice selection
pull-down-buttons.md	Pull-down buttons	Action lists, no current selection
disclosure-controls.md	Disclosure controls	Progressive disclosure, show/hide
Output Format
Component recommendation -- which menu or button type and why.
Visual hierarchy -- placement, sizing, grouping within the interface.
Platform-specific behavior across iOS, iPadOS, macOS, visionOS.
Keyboard shortcuts (macOS) -- standard and custom shortcuts for menu items and toolbar actions.
Questions to Ask
Which platforms?
Primary or secondary action?
How many actions need to be available?
macOS menu bar app?
Related Skills
hig-components-search -- Search fields, page controls alongside toolbars and menus
hig-components-controls -- Toggles, pickers, segmented controls complementing buttons
hig-components-dialogs -- Alerts, sheets, popovers triggered by menu items or buttons
hig-inputs -- Keyboard shortcuts and pointer interactions with menus and toolbars

Built by Raintree Technology · More developer tools

Weekly Installs
156
Repository
raintree-techno…g-skills
GitHub Stars
45
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass