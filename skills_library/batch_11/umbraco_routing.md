---
title: umbraco-routing
url: https://skills.sh/umbraco/umbraco-cms-backoffice-skills/umbraco-routing
---

# umbraco-routing

skills/umbraco/umbraco-cms-backoffice-skills/umbraco-routing
umbraco-routing
Installation
$ npx skills add https://github.com/umbraco/umbraco-cms-backoffice-skills --skill umbraco-routing
SKILL.md
Umbraco Routing
What is it?

Routing in Umbraco's backoffice enables navigation between sections, dashboards, and workspaces using pathname-based URLs. Sections serve as primary organizational dividers with entry points via section views, dashboards, or custom elements. Custom routing can be built using umb-router-slot with route definitions that support parameters and redirects.

Documentation

Always fetch the latest docs before implementing:

Main docs: https://docs.umbraco.com/umbraco-cms/customizing/foundation/routes
Sections: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/sections/section
Dashboards: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/dashboard
Foundation: https://docs.umbraco.com/umbraco-cms/customizing/foundation
Reference Example

The Umbraco source includes a working example:

Location: /Umbraco-CMS/src/Umbraco.Web.UI.Client/examples/modal-routed/

This example demonstrates routed modals with URL-based navigation and deep-linking support. Study this for complex routing patterns.

Workflow
Fetch docs - Use WebFetch on the URLs above
Ask questions - Custom routes? Section navigation? Parameters needed?
Generate code - Implement routing based on latest docs
Explain - Show what was created and how navigation works
Minimal Examples
Section with Pathname
{
  "type": "section",
  "alias": "My.Section",
  "name": "My Section",
  "meta": {
    "label": "My Section",
    "pathname": "my-section"
  }
}


URL: /section/my-section

Dashboard with Pathname
{
  "type": "dashboard",
  "alias": "My.Dashboard",
  "name": "My Dashboard",
  "meta": {
    "label": "Welcome",
    "pathname": "welcome-dashboard"
  },
  "conditions": [
    {
      "alias": "Umb.Condition.SectionAlias",
      "match": "Umb.Section.Content"
    }
  ]
}


URL: /section/content/dashboard/welcome-dashboard

Custom Router with Routes
import { html, customElement, state } from '@umbraco-cms/backoffice/external/lit';
import { UmbLitElement } from '@umbraco-cms/backoffice/lit-element';
import type { UmbRoute } from '@umbraco-cms/backoffice/router';

@customElement('my-routed-element')
export class MyRoutedElement extends UmbLitElement {
  @state()
  private _routes: UmbRoute[] = [
    {
      path: 'person/:personId',
      component: () => import('./person.element.js'),
      setup: (_component, info) => {
        console.log('personId:', info.match.params.personId);
      },
    },
    {
      path: 'people',
      component: () => import('./people.element.js'),
    },
    {
      path: '',
      redirectTo: 'people',
    },
  ];

  render() {
    return html`
      <umb-router-slot .routes=${this._routes}></umb-router-slot>
    `;
  }
}

Route with Parameters
{
  path: 'edit/:id',
  component: () => import('./edit.element.js'),
  setup: (component, info) => {
    const id = info.match.params.id;
    component.itemId = id;
  },
}

Route with Redirect
{
  path: '',
  redirectTo: 'overview',
}

Multiple Routes Example
@state()
private _routes: UmbRoute[] = [
  {
    path: 'overview',
    component: () => import('./overview.element.js'),
  },
  {
    path: 'settings',
    component: () => import('./settings.element.js'),
  },
  {
    path: 'item/:id',
    component: () => import('./item-detail.element.js'),
    setup: (component, info) => {
      component.itemId = info.match.params.id;
    },
  },
  {
    path: '',
    redirectTo: 'overview',
  },
];

Navigation Links
render() {
  return html`
    <nav>
      <a href="/section/my-section/overview">Overview</a>
      <a href="/section/my-section/settings">Settings</a>
      <a href="/section/my-section/item/123">Item 123</a>
    </nav>
    <umb-router-slot .routes=${this._routes}></umb-router-slot>
  `;
}

Section View with Pathname
{
  "type": "sectionView",
  "alias": "My.SectionView",
  "name": "My Section View",
  "element": "/App_Plugins/MyExtension/section-view.js",
  "meta": {
    "label": "Organization",
    "pathname": "organization",
    "icon": "icon-users"
  },
  "conditions": [
    {
      "alias": "Umb.Condition.SectionAlias",
      "match": "My.Section"
    }
  ]
}


URL: /section/my-section/organization

Nested Routes
// Parent element
@state()
private _routes: UmbRoute[] = [
  {
    path: 'admin',
    component: () => import('./admin-layout.element.js'),
  },
  {
    path: 'users',
    component: () => import('./users-layout.element.js'),
  },
];

// Admin layout element can have its own nested routes
@state()
private _adminRoutes: UmbRoute[] = [
  {
    path: 'dashboard',
    component: () => import('./admin-dashboard.element.js'),
  },
  {
    path: 'settings',
    component: () => import('./admin-settings.element.js'),
  },
];

Route Setup Function
{
  path: 'edit/:documentId',
  component: () => import('./document-editor.element.js'),
  setup: (component, info) => {
    // Access route parameters
    const documentId = info.match.params.documentId;

    // Pass to component
    component.documentId = documentId;

    // Can also access query params, etc.
    console.log('Route info:', info);
  },
}

Key Concepts

pathname: URL segment for sections/dashboards/views

umb-router-slot: Component that renders matched route

UmbRoute: Route definition with path, component, setup

Route Order: First match wins - order matters!

Parameters: Use :paramName in path (e.g., item/:id)

Redirects: Use redirectTo to redirect to another path

setup Function: Called when route matches, receives component and route info

URL Structure:

Section: /section/my-section
Dashboard: /section/content/dashboard/welcome
Section View: /section/my-section/organization
Custom: /section/my-section/people/person/123

Entry Points:

Section Views (with tabs/icons)
Dashboards (with tabs/icons)
Workspaces (entity editing)
Custom Elements (full control)

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
Gen Agent Trust HubPass
SocketPass
SnykPass