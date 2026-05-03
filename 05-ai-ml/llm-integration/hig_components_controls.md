---
title: hig-components-controls
url: https://skills.sh/raintree-technology/apple-hig-skills/hig-components-controls
---

# hig-components-controls

skills/raintree-technology/apple-hig-skills/hig-components-controls
hig-components-controls
Installation
$ npx skills add https://github.com/raintree-technology/apple-hig-skills --skill hig-components-controls
SKILL.md
Apple HIG: Selection and Input Controls

Check for .claude/apple-design-context.md before asking questions. Use existing context and only ask for information not already covered.

Key Principles

Clear current state. Users must always see what is selected. Toggles show on/off, segmented controls highlight the active segment, pickers display the current selection.

Prefer standard system controls. Built-in controls provide consistency and accessibility. Custom controls introduce a learning curve and may break assistive features.

Toggles for binary states. On or off. In Settings-style screens, changes take effect immediately. In modal forms, changes commit on confirmation.

Segmented controls for mutually exclusive options. 2-5 items, roughly equal importance, short labels.

Sliders for continuous values. When precise numeric input is not critical. Provide min/max labels or icons for range endpoints.

Pickers for long option lists. Too many options for a segmented control. Works well for dates, times, structured data.

Steppers for small, precise adjustments. Increment/decrement in fixed steps. Display current value next to the stepper with reasonable min/max bounds.

Text fields for short, single-line input. Text views for multi-line. Configure keyboard type to match expected input (email, URL, number).

Combo boxes: text input + selection list. macOS. Type a value or choose from a predefined list when custom values are valid.

Token fields: discrete values as visual tokens. macOS. For email recipients, tags, or collections of discrete items.

Gauges and rating indicators display values. Gauges show a value within a range. Rating indicators show ratings (often stars). Display-only; use interactive variants for input.

Reference Index
Reference	Topic	Key content
controls.md	General controls	States, affordance, system controls
toggles.md	Toggles	On/off, immediate effect
segmented-controls.md	Segmented controls	2-5 options, equal weight
sliders.md	Sliders	Continuous range, min/max labels
steppers.md	Steppers	Fixed steps, bounded values
pickers.md	Pickers	Dates, times, long option sets
combo-boxes.md	Combo boxes	macOS, type or select, custom values
text-fields.md	Text fields	Short input, keyboard types, validation
text-views.md	Text views	Multi-line, comments, descriptions
labels.md	Labels	Placement, VoiceOver support
token-fields.md	Token fields	macOS, chips, tags, recipients
virtual-keyboards.md	Virtual keyboards	Email, URL, number keyboard types
rating-indicators.md	Rating indicators	Star ratings, display-only
gauges.md	Gauges	Level indicators, range display
Output Format
Control recommendation with rationale and why alternatives are less suitable.
State management -- how the control communicates current state and whether changes apply immediately or on confirmation.
Validation approach -- when to show errors and how to communicate rules.
Accessibility -- labels, traits, hints for VoiceOver.
Questions to Ask
What type of data? (Boolean, choice from fixed set, numeric, free-form text?)
How many options?
Which platforms? (Combo boxes and token fields are macOS-only)
Settings screen or inline form?
Related Skills
hig-components-menus -- Buttons and pop-up buttons complementing selection controls
hig-components-dialogs -- Sheets and popovers containing forms
hig-components-search -- Search fields sharing text input patterns
hig-inputs -- Keyboard, pointer, gesture interactions with controls
hig-foundations -- Typography, color, layout for control styling

Built by Raintree Technology · More developer tools

Weekly Installs
151
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