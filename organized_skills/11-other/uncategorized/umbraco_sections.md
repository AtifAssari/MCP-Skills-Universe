---
rating: ⭐⭐
title: umbraco-sections
url: https://skills.sh/umbraco/umbraco-cms-backoffice-skills/umbraco-sections
---

# umbraco-sections

skills/umbraco/umbraco-cms-backoffice-skills/umbraco-sections
umbraco-sections
Installation
$ npx skills add https://github.com/umbraco/umbraco-cms-backoffice-skills --skill umbraco-sections
SKILL.md
Umbraco Sections
What is it?

Sections are top-level navigation items in the Umbraco backoffice that appear alongside default options like Content, Media, and Settings. They serve as a home for custom content and functionality, providing a blank canvas that can be extended with dashboards, sidebars, and section views. Sections require permission configuration for user groups to access them.

Documentation

Always fetch the latest docs before implementing:

Main docs: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/sections/section
Section Views: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/sections/section-view
Section Sidebar: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/sections/section-sidebar
Dashboard: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/dashboard
Foundation: https://docs.umbraco.com/umbraco-cms/customizing/foundation
Extension Registry: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-registry
Reference Example

The Umbraco source includes a working example:

Location: /Umbraco-CMS/src/Umbraco.Web.UI.Client/examples/section-sidebar-menu-expansion/

This example demonstrates section sidebar menu expansion patterns. Study this for sidebar customization.

Related Foundation Skills

If you need to explain these foundational concepts when implementing sections, reference these skills:

Context API: When implementing section contexts or explaining how section extensions communicate

Reference skill: umbraco-context-api

Conditions: When implementing permissions, user group access, visibility controls, or section restrictions

Reference skill: umbraco-conditions

Routing: When implementing pathnames, navigation patterns, URLs, or section routing

Reference skill: umbraco-routing
Workflow
Fetch docs - Use WebFetch on the URLs above
Ask questions - What will the section contain? Dashboards? Trees? Sidebar needed?
Generate files - Create manifest for section + related extensions based on latest docs
Explain - Show what was created and how to configure permissions
Minimal Examples
Basic Section (umbraco-package.json)
{
  "type": "section",
  "alias": "My.Section",
  "name": "My Section",
  "meta": {
    "label": "My Section",
    "pathname": "my-section"
  }
}

Section with Icon (manifest.ts)
export const manifests = [
  {
    type: "section",
    alias: "My.CustomSection",
    name: "Custom Section",
    meta: {
      label: "Custom",
      pathname: "custom-section"
    },
    conditions: [
      {
        alias: "Umb.Condition.SectionUserPermission",
        match: "My.CustomSection"
      }
    ]
  }
];

Section with Dashboard (manifest.ts)
export const manifests = [
  {
    type: "section",
    alias: "My.Section",
    name: "My Section",
    meta: {
      label: "My Section",
      pathname: "my-section"
    }
  },
  {
    type: "dashboard",
    alias: "My.Section.Dashboard",
    name: "My Section Dashboard",
    element: () => import('./dashboard.element.js'),
    meta: {
      label: "Welcome",
      pathname: "welcome"
    },
    conditions: [
      {
        alias: "Umb.Condition.SectionAlias",
        match: "My.Section"
      }
    ]
  }
];

Section with Sidebar (manifest.ts)
export const manifests = [
  {
    type: "section",
    alias: "My.Section",
    name: "My Section",
    meta: {
      label: "My Section",
      pathname: "my-section"
    }
  },
  {
    type: "sectionSidebarApp",
    alias: "My.Section.Sidebar",
    name: "My Section Sidebar",
    element: () => import('./sidebar.element.js'),
    conditions: [
      {
        alias: "Umb.Condition.SectionAlias",
        match: "My.Section"
      }
    ]
  }
];

Key Properties
type: Always "section"
alias: Unique identifier for the section
name: Display name in backoffice
meta.label: Label shown in navigation
meta.pathname: URL route for the section
element: Optional custom element (not recommended - use dashboards instead)
conditions: Control visibility and access
Granting Permissions

To enable a custom section for users:

Navigate to Users section in Umbraco backoffice
Select User Groups menu item
Choose the user group to configure
Click the Choose button under Sections
Select your custom section
Save changes
Built-in Sections
Umb.Section.Content - Content management
Umb.Section.Media - Media library
Umb.Section.Settings - System settings
Umb.Section.Packages - Package management
Umb.Section.Users - User management
Umb.Section.Members - Member management

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
SnykPass