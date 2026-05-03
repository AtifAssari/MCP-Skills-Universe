---
rating: ⭐⭐⭐
title: umbraco-menu-items
url: https://skills.sh/umbraco/umbraco-cms-backoffice-skills/umbraco-menu-items
---

# umbraco-menu-items

skills/umbraco/umbraco-cms-backoffice-skills/umbraco-menu-items
umbraco-menu-items
Installation
$ npx skills add https://github.com/umbraco/umbraco-cms-backoffice-skills --skill umbraco-menu-items
SKILL.md
Umbraco Menu Items
What is it?

Menu items are extension components that appear throughout the Umbraco backoffice in sidebars, button flyouts, and other locations. They work alongside Menu extensions to provide navigational and action-based functionality. Menu items come in different kinds (link, action, tree) and can use default components or custom elements.

Documentation

Always fetch the latest docs before implementing:

Main docs: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/menu-item
Menu: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/menu
Foundation: https://docs.umbraco.com/umbraco-cms/customizing/foundation
Extension Registry: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-registry
Reference Example

The Umbraco source includes a working example:

Location: /Umbraco-CMS/src/Umbraco.Web.UI.Client/examples/menu-item/

This example demonstrates custom menu items with different kinds. Study this for production patterns.

Related Foundation Skills

If you need to explain these foundational concepts when implementing menu items, reference these skills:

Umbraco Element: When implementing custom menu item elements, explaining UmbLitElement, or creating menu item components

Reference skill: umbraco-umbraco-element

Controllers: When implementing UmbMenuItemAction, action logic, execute methods, or menu item behavior

Reference skill: umbraco-controllers

Context API: When implementing context access or service consumption from menu item actions

Reference skill: umbraco-context-api
Workflow
Fetch docs - Use WebFetch on the URLs above
Ask questions - What kind? Which menu? Link, action, or tree? Custom element needed?
Generate files - Create manifest + element (if custom) based on latest docs
Explain - Show what was created and how to test
Minimal Examples
Link Menu Item (manifest.ts)
export const manifests = [
  {
    type: "menuItem",
    kind: "link",
    alias: "My.MenuItem.Link",
    name: "My Link Menu Item",
    weight: 100,
    meta: {
      label: "External Link",
      icon: "icon-link",
      menus: ["Umb.Menu.Help"],
      href: "https://example.com"
    }
  }
];

Action Menu Item (manifest.ts)
export const manifests = [
  {
    type: "menuItem",
    kind: "action",
    alias: "My.MenuItem.Action",
    name: "My Action Menu Item",
    api: () => import('./menu-item-action.js'),
    meta: {
      label: "Execute Action",
      icon: "icon-wand",
      menus: ["My.Menu"]
    }
  }
];

Action Implementation (menu-item-action.ts)
import { UmbMenuItemAction } from '@umbraco-cms/backoffice/menu';

export class MyMenuItemAction extends UmbMenuItemAction {
  async execute() {
    console.log('Menu item clicked!');
    // Perform custom logic here
  }
}

export default MyMenuItemAction;

Tree Menu Item (manifest.ts)
export const manifests = [
  {
    type: "menuItem",
    kind: "tree",
    alias: "My.MenuItem.Tree",
    name: "My Tree Menu Item",
    meta: {
      label: "Tree Structure",
      icon: "icon-folder",
      menus: ["Umb.Menu.Content"],
      treeAlias: "My.Tree"
    }
  }
];

Custom Element Menu Item (menu-item.element.ts)
import { html, customElement } from '@umbraco-cms/backoffice/external/lit';
import { UmbLitElement } from '@umbraco-cms/backoffice/lit-element';

@customElement('my-menu-item')
export class MyMenuItemElement extends UmbLitElement {

  #onClick() {
    // Custom logic
  }

  render() {
    return html`
      <uui-menu-item
        label="Custom Item"
        @click="${this.#onClick}"
      >
        <uui-icon name="icon-wand"></uui-icon>
      </uui-menu-item>
    `;
  }
}

export default MyMenuItemElement;

Menu Item Kinds
Link - Navigate to external URLs (href property)
Action - Execute custom logic on click (requires api implementation)
Tree - Display submenu from tree structure (treeAlias property)
Key Properties
type: Always "menuItem"
kind: Type of menu item ("link", "action", "tree")
alias: Unique identifier
meta.label: Display text
meta.icon: Icon identifier
meta.menus: Array of menu aliases to appear in
weight: Controls ordering (higher = later in list)
element: Path to custom element (optional)
api: Action implementation (for kind: "action")

That's it! Always fetch fresh docs, keep examples minimal, generate complete working code.

Weekly Installs
141
Repository
umbraco/umbraco…e-skills
GitHub Stars
23
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass