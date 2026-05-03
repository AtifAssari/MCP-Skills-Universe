---
rating: ⭐⭐
title: umbraco-kinds
url: https://skills.sh/umbraco/umbraco-cms-backoffice-skills/umbraco-kinds
---

# umbraco-kinds

skills/umbraco/umbraco-cms-backoffice-skills/umbraco-kinds
umbraco-kinds
Installation
$ npx skills add https://github.com/umbraco/umbraco-cms-backoffice-skills --skill umbraco-kinds
SKILL.md
Umbraco Kinds
What is it?

A Kind is a preset configuration that extensions inherit for consistency. It reduces redundancy by defining default properties that multiple extensions can share. Kinds ensure standardized structures across extensions and simplify definitions by providing predefined properties that extensions automatically inherit.

Documentation

Always fetch the latest docs before implementing:

Main docs: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-types/kind
Foundation: https://docs.umbraco.com/umbraco-cms/customizing/foundation
Extension Registry: https://docs.umbraco.com/umbraco-cms/customizing/extending-overview/extension-registry
Workflow
Fetch docs - Use WebFetch on the URLs above
Ask questions - What extension type? What default properties to share?
Generate files - Create kind manifest + consuming extensions based on latest docs
Explain - Show what was created and how to test
Minimal Examples
Registering a Kind
import type { UmbExtensionManifestKind } from '@umbraco-cms/backoffice/extension-api';

export const customButtonKind: UmbExtensionManifestKind = {
  type: 'kind',
  alias: 'My.Kind.HeaderAppButton',
  matchType: 'headerApp',
  matchKind: 'button',
  manifest: {
    elementName: 'umb-header-app-button',
  },
};

Using a Kind in an Extension
const manifest = {
  type: 'headerApp',
  kind: 'button',  // Uses the 'button' kind
  name: 'My Header App',
  alias: 'My.HeaderApp',
  meta: {
    label: 'My App',
    icon: 'icon-heart',
    href: '/my-app',
  },
};

Kind with Default Meta Properties
export const cardKind: UmbExtensionManifestKind = {
  type: 'kind',
  alias: 'My.Kind.DashboardCard',
  matchType: 'dashboard',
  matchKind: 'card',
  manifest: {
    elementName: 'my-dashboard-card',
    meta: {
      // Default meta properties
      size: 'medium',
      color: 'default',
    },
  },
};

// Extension inherits defaults, can override
const dashboard = {
  type: 'dashboard',
  kind: 'card',
  alias: 'My.Dashboard',
  name: 'My Dashboard',
  meta: {
    label: 'Stats',
    pathname: 'stats',
    // size and color inherited from kind
  },
};


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