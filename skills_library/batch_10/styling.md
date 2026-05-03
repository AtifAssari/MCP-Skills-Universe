---
title: styling
url: https://skills.sh/ui5/webcomponents/styling
---

# styling

skills/ui5/webcomponents/styling
styling
Installation
$ npx skills add https://github.com/ui5/webcomponents --skill styling
SKILL.md
Styling UI5 Web Components

UI5 Web Components use Shadow DOM for encapsulation. Styles are isolated — external CSS won't leak in, but customization requires specific techniques. There are five approaches, ordered from most recommended to least.

1. Styles on Tag Level

Some components (Title, Label, Tag, Button, Input, and others) are designed so that styles set directly on the custom element take effect.

ui5-input {
  width: 150px;
  color: yellow;
  background: purple;
}


This works for simpler components. For complex components with deep DOM structures, tag-level styling has no effect on internal elements.

Best practice: Always use tag-level styling for sizing properties (margin, padding, width, height) to avoid design inconsistencies.

2. CSS Shadow Parts

For complex components, specific internal elements are exposed as CSS shadow parts.

ui5-card-header::part(status) {
  color: red;
}


Important: Available shadow parts are listed in each component's API reference under the "Overview" section. Only documented parts are stable — do not rely on undocumented internal structure.

3. CSS Custom States

Components can expose custom states via the CSS custom state pseudo-class, allowing you to style based on internal component conditions.

ui5-toolbar-item:state(overflowed) {
  flex-direction: column;
}


Important: Available custom states are listed in each component's API reference under the "Overview" section.

4. Overriding CSS Variables

UI5 Web Components use SAP CSS variables (--sap*) for theming. You can override these on a per-component or per-scope basis.

ui5-button {
  --sapButton_TextColor: purple;
}


All global SAP CSS variables are defined in @sap-theming/theming-base-content. Overriding them changes the appearance of any component that uses them.

Best practice: For broad theme changes, prefer using the UI Theme Designer to ensure consistency. Use direct CSS variable overrides only for targeted, scoped customizations.

5. Custom CSS via addCustomCSS (Last Resort)

If none of the above work, custom CSS can be injected directly into a component's shadow DOM using the addCustomCSS API. It targets internal DOM structure that may change between versions. Only use it when CSS variables, tag-level styles, and shadow parts cannot achieve the desired result.

Before writing custom CSS:

Find the component's template and existing styles in node_modules
Optionally, inspect the component's shadow DOM in DevTools to understand the internal structure
Target the minimal set of selectors needed

Custom CSS must be registered before any instances of the component are created:

import { addCustomCSS } from "@ui5/webcomponents-base/dist/Theming.js";

addCustomCSS("ui5-select", `
  .ui5-select-root {
    background-color: red;
  }
`);


The first argument is the component's tag name, the second is a CSS string that gets injected into every instance's shadow DOM.

What NOT to Do
Don't pierce shadow DOM with deprecated >>> or /deep/ selectors — they don't work.
Don't rely on internal DOM structure — it can change between versions. Only use documented shadow parts.
Don't use !important on SAP variables — scope your overrides instead.
Don't override raw colors when a SAP CSS variable exists — use the variable to maintain theme consistency.
Quick Decision Guide
Goal	Technique
Change width, margin, padding	Tag-level styles
Restyle a specific internal element	::part(name)
Style based on component state	:state(name)
Change colors/fonts globally	Override --sap* CSS variables
Full theme customization	UI Theme Designer
Override internal shadow DOM styles	addCustomCSS (last resort)
Weekly Installs
61
Repository
ui5/webcomponents
GitHub Stars
1.7K
First Seen
Mar 15, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass