---
rating: ⭐⭐
title: hig-components-dialogs
url: https://skills.sh/raintree-technology/apple-hig-skills/hig-components-dialogs
---

# hig-components-dialogs

skills/raintree-technology/apple-hig-skills/hig-components-dialogs
hig-components-dialogs
Installation
$ npx skills add https://github.com/raintree-technology/apple-hig-skills --skill hig-components-dialogs
SKILL.md
Apple HIG: Presentation Components

Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

Key Principles

Alerts: sparingly, for critical situations. Errors needing attention, destructive action confirmations, or information requiring acknowledgment. They interrupt flow and demand a response.

Sheets: focused tasks that maintain context. Slides in from the edge (or attaches to a window on macOS). Use for creating items, editing settings, multi-step forms.

Popovers: non-modal on iPad and Mac. Appear next to the trigger element, dismissed by tapping outside. For additional information, options, or controls without taking over the screen.

Action sheets: choosing among actions. Present when picking from multiple actions, especially if one is destructive. iPhone: slide up from bottom. iPad: appear as popovers.

Minimize interruptions. Before reaching for a modal, consider inline presentation or making the action undoable instead.

Concise, actionable alert text. Short descriptive title. Brief message body if needed. Button labels should be specific verbs ("Delete", "Save"), not "OK".

Mark destructive actions clearly. Destructive button style (red text). Place destructive buttons where users are less likely to tap reflexively.

Provide a cancel option for alerts and action sheets with multiple actions. On action sheets, cancel appears at the bottom, separated.

Digit entry: focused and accessible. Appropriately sized input fields, automatic advancement between digits, support for paste and autofill.

Adapt presentation to platform. The same interaction may use different components on iPhone, iPad, Mac, and visionOS.

Reference Index
Reference	Topic	Key content
alerts.md	Alerts	Button ordering, title/message text, confirmation, destructive actions
action-sheets.md	Action sheets	Multiple actions, cancel option, destructive handling
popovers.md	Popovers	Non-modal, dismiss on tap outside, iPad/Mac
sheets.md	Sheets	Modal task, context preservation
digit-entry-views.md	Digit entry	PIN input, autofill, auto-advance
Output Format
Recommended presentation type with rationale and why alternatives are less suitable.
Content guidelines -- title, message, button labels per Apple's tone and brevity rules.
Dismiss behavior -- how the user dismisses and what happens (save, discard, cancel).
Alternatives -- when the scenario might not need a modal at all (inline feedback, undo, progressive disclosure).
Questions to Ask
What information or action does the presentation need?
Blocking or non-blocking?
Which platforms?
How often does this appear?
Related Skills
hig-components-menus -- Buttons and toolbar items triggering presentations
hig-components-controls -- Input controls within sheets and popovers
hig-components-search -- Search and navigation within presented views
hig-patterns -- Modality, interruptions, user flow management
hig-foundations -- Color, typography, layout for presentation components

Built by Raintree Technology · More developer tools

Weekly Installs
153
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