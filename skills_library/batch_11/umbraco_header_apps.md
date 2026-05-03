---
title: umbraco-header-apps
url: https://skills.sh/umbraco/umbraco-cms-backoffice-skills/umbraco-header-apps
---

# umbraco-header-apps

skills/umbraco/umbraco-cms-backoffice-skills/umbraco-header-apps
umbraco-header-apps
Installation
$ npx skills add https://github.com/umbraco/umbraco-cms-backoffice-skills --skill umbraco-header-apps
SKILL.md
Umbraco Header Apps
What is it?

Header apps are single-purpose extensions that appear in Umbraco's top navigation bar, positioned next to the user profile avatar and global search. They provide globally accessible functionality to the Backoffice, such as quick links to documentation, tools, or custom interactive features. Header apps can be simple links or custom interactive components that open modals or perform actions.

Documentation

Always fetch the latest docs before implementing:

Main docs: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/header-apps
Foundation: https://docs.umbraco.com/umbraco-cms/customizing/foundation
Extension Registry: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-registry
Related Foundation Skills

If you need to explain these foundational concepts when implementing header apps, reference these skills:

Umbraco Element: When implementing interactive header apps, explaining UmbHeaderAppButtonElement, or custom elements

Reference skill: umbraco-umbraco-element

Context API: When implementing context access, modals, notifications, or services from header apps

Reference skill: umbraco-context-api

Controllers: When implementing controllers, action handlers, click handlers, or header app behavior

Reference skill: umbraco-controllers
Workflow
Fetch docs - Use WebFetch on the URLs above
Ask questions - What will it do? Simple link or interactive? What icon/label?
Generate files - Create manifest + element (if interactive) based on latest docs
Explain - Show what was created and how to test
Minimal Examples
Simple Link Header App (umbraco-package.json)
{
  "type": "headerApp",
  "alias": "My.HeaderApp",
  "name": "My Header App",
  "kind": "button",
  "meta": {
    "label": "Documentation",
    "icon": "icon-help",
    "href": "https://docs.umbraco.com/"
  }
}

Interactive Header App Manifest (manifest.ts)
export const manifests = [
  {
    type: "headerApp",
    alias: "My.Interactive.HeaderApp",
    name: "My Interactive Header App",
    element: () => import('./header-app.element.js'),
    meta: {
      label: "Tools",
      icon: "icon-tools"
    }
  }
];

Interactive Header App Element (header-app.element.ts)
import { html, customElement } from '@umbraco-cms/backoffice/external/lit';
import { UmbHeaderAppButtonElement } from '@umbraco-cms/backoffice/header-app';

@customElement('my-header-app')
export class MyHeaderAppElement extends UmbHeaderAppButtonElement {

  #onClick() {
    // Handle click - open modal, navigate, etc.
    console.log('Header app clicked!');
  }

  render() {
    return html`
      <uui-button
        @click="${this.#onClick}"
        label="${this.manifest?.meta?.label}"
        compact
      >
        <uui-icon name="${this.manifest?.meta?.icon}"></uui-icon>
      </uui-button>
    `;
  }
}

export default MyHeaderAppElement;

Common Use Cases
Quick Links: External documentation, help resources, or admin tools
Global Actions: Search, notifications, or system-wide operations
Custom Tools: Integration with external services or custom functionality

That's it! Always fetch fresh docs, keep examples minimal, generate complete working code.

Weekly Installs
139
Repository
umbraco/umbraco…e-skills
GitHub Stars
23
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass