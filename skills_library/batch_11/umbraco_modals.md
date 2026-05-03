---
title: umbraco-modals
url: https://skills.sh/umbraco/umbraco-cms-backoffice-skills/umbraco-modals
---

# umbraco-modals

skills/umbraco/umbraco-cms-backoffice-skills/umbraco-modals
umbraco-modals
Installation
$ npx skills add https://github.com/umbraco/umbraco-cms-backoffice-skills --skill umbraco-modals
SKILL.md
Umbraco Modals
What is it?

A modal is a popup layer that darkens the surroundings and comes with a focus lock. The modal extension type is used to configure and present dialogs and sidebars within the Umbraco backoffice. Modals can be opened via routes (for deep-linking) or at runtime using the Modal Manager Context, and they use a token-based system for type-safe communication.

Documentation

Always fetch the latest docs before implementing:

Main docs: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/modals
Custom Modals: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/modals/custom-modals
Route Registration: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/modals/route-registration
Foundation: https://docs.umbraco.com/umbraco-cms/customizing/foundation
Extension Registry: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-registry
Reference Examples

The Umbraco source includes working examples:

Custom Modal Location: /Umbraco-CMS/src/Umbraco.Web.UI.Client/examples/custom-modal/

This example demonstrates a basic custom modal with token, element, and manifest.

Routed Modal Location: /Umbraco-CMS/src/Umbraco.Web.UI.Client/examples/modal-routed/

This example demonstrates modals that can be opened via URL routing for deep-linking support.

Related Foundation Skills

If you need to explain these foundational concepts when implementing modals, reference these skills:

Context API: When implementing modal manager context, consumeContext patterns, or explaining how to open modals

Reference skill: umbraco-context-api

Umbraco Element: When implementing modal elements, explaining UmbLitElement, or creating modal components

Reference skill: umbraco-umbraco-element

State Management: When implementing modal data flow, modal values, or state management between modal and caller

Reference skill: umbraco-state-management
Workflow
Fetch docs - Use WebFetch on the URLs above
Ask questions - What will the modal do? Dialog or sidebar? What data in/out? Deep-link needed?
Generate files - Create modal token + element + manifest based on latest docs
Explain - Show what was created and how to open the modal
Minimal Examples
Modal Token (modal-token.ts)
import { UmbModalToken } from '@umbraco-cms/backoffice/modal';

export interface MyModalData {
  title: string;
}

export interface MyModalValue {
  confirmed: boolean;
}

export const MY_MODAL_TOKEN = new UmbModalToken<MyModalData, MyModalValue>(
  'My.Modal',
  {
    modal: {
      type: 'sidebar',
      size: 'small',
    },
  }
);

Modal Element (modal.element.ts)
import { html, customElement } from '@umbraco-cms/backoffice/external/lit';
import { UmbLitElement } from '@umbraco-cms/backoffice/lit-element';
import { UmbModalExtensionElement } from '@umbraco-cms/backoffice/modal';

@customElement('my-modal')
export class MyModalElement extends UmbLitElement
  implements UmbModalExtensionElement<MyModalData, MyModalValue> {

  modalContext: any;

  #handleSubmit() {
    this.modalContext.updateValue({ confirmed: true });
    this.modalContext.submit();
  }

  render() {
    return html`
      <umb-body-layout headline="${this.modalContext?.data?.title}">
        <uui-box>
          <p>Modal content here</p>
          <uui-button @click="${this.#handleSubmit}">
            Confirm
          </uui-button>
        </uui-box>
      </umb-body-layout>
    `;
  }
}

export default MyModalElement;

Manifest (manifest.ts)
export const manifests = [
  {
    type: 'modal',
    alias: 'My.Modal',
    name: 'My Modal',
    element: () => import('./modal.element.js'),
  },
];

Opening the Modal
import { UMB_MODAL_MANAGER_CONTEXT } from '@umbraco-cms/backoffice/modal';
import { MY_MODAL_TOKEN } from './modal-token.js';

// In your element:
constructor() {
  super();
  this.consumeContext(UMB_MODAL_MANAGER_CONTEXT, (context) => {
    this._modalManager = context;
  });
}

async openModal() {
  const result = await this._modalManager?.open(this, MY_MODAL_TOKEN, {
    data: { title: 'My Modal' }
  });

  if (result?.confirmed) {
    console.log('User confirmed!');
  }
}

Modal Types
Dialog: Centered on screen
Sidebar: Slides in from the right

That's it! Always fetch fresh docs, keep examples minimal, generate complete working code.

Weekly Installs
138
Repository
umbraco/umbraco…e-skills
GitHub Stars
23
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn