---
title: vtex-io-messages-and-i18n
url: https://skills.sh/vtex/skills/vtex-io-messages-and-i18n
---

# vtex-io-messages-and-i18n

skills/vtex/skills/vtex-io-messages-and-i18n
vtex-io-messages-and-i18n
Installation
$ npx skills add https://github.com/vtex/skills --skill vtex-io-messages-and-i18n
SKILL.md
Messages & Internationalization
When this skill applies

Use this skill when a VTEX IO app needs translated copy instead of hardcoded strings.

Adding localized UI text to storefront or Admin apps
Creating or updating /messages/*.json translation files
Defining message keys in context.json
Reviewing React, Admin, or backend code that currently hardcodes user-facing copy
Integrating app-specific translations with vtex.messages

Do not use this skill for:

general UI layout or component composition
authorization, policies, or auth tokens
service runtime sizing
choosing between HTTP, GraphQL, and event-driven APIs
Decision rules
Use the messages builder and translation files for user-facing copy instead of hardcoding labels, button text, or UI messages in source code.
Keep translation keys stable, explicit, and scoped to the app domain instead of generic keys such as title or button. The exact format may vary, but keys should remain specific, descriptive, and clearly owned by the app.
Prefix message IDs according to their UI surface or domain, for example store/... for storefront messages and admin/... for Admin or Site Editor messages, so keys stay organized and do not collide across contexts.
Define message keys in /messages/context.json so VTEX IO can discover and manage the app’s translation surface. Keep it as a flat map of messageId -> description and include the keys the app actually uses.
Keep translated message payloads small and app-focused. Do not turn the messages system into a general content store.
In React or Admin UIs, prefer message IDs and localization helpers over literal copy in JSX.
In backend or GraphQL flows, translate only when the app boundary truly needs localized text; otherwise return stable machine-oriented data and let the caller localize the presentation.
Use app-level overrides of vtex.messages only when the app truly needs to customize translation behavior or message resolution beyond normal app-local message files.
Hard constraints
Constraint: User-facing strings must come from the messages infrastructure

User-facing strings MUST come from the messages infrastructure instead of being hardcoded in components, handlers, or resolvers.

Why this matters

Hardcoded copy breaks localization, makes message review harder, and creates inconsistent behavior across storefront, Admin, and backend flows.

Detection

If you see labels, buttons, headings, alerts, or other user-facing text embedded directly in JSX or backend response formatting for a localized app, STOP and move that copy to message files.

Correct

<FormattedMessage id="admin/my-app.save" />


Wrong

<button>Save</button>

Constraint: Message keys must be declared and organized explicitly

Message keys MUST be app-scoped and represented in the app’s message configuration instead of being invented ad hoc in code.

Why this matters

Unstructured keys become hard to maintain, collide across app areas, and make message ownership unclear.

Detection

If code introduces new message IDs with no corresponding translation files or context.json entry, STOP and add the message contract explicitly.

Correct

{
  "admin/my-app.save": "Save"
}


Wrong

{
  "save": "Save"
}

Constraint: The messages system must not be used as a general content or configuration store

Translation files MUST contain localized copy, not operational configuration, secrets, or large content payloads.

Why this matters

The messages infrastructure is designed for translated strings. Using it for other data creates maintenance confusion and mixes localization concerns with configuration or content storage.

Detection

If message files contain API URLs, credentials, business rules, or long structured content blobs, STOP and move that data to app settings, configuration apps, or a content-specific mechanism.

Correct

{
  "store/my-app.emptyState.title": "No records found"
}


Wrong

{
  "apiBaseUrl": "https://partner.example.com",
  "featureFlags": {
    "betaMode": true
  }
}

Preferred pattern

Recommended file layout:

.
├── messages/
│   ├── context.json
│   ├── en.json
│   └── pt.json
└── react/
    └── components/
        └── SaveButton.tsx


Minimal messages setup:

// messages/context.json
{
  "admin/my-app.save": "Label for the save action in the admin settings page"
}

// messages/en.json
{
  "admin/my-app.save": "Save",
  "store/my-app.emptyState.title": "No records found"
}

// messages/pt.json
{
  "admin/my-app.save": "Salvar"
}

import { FormattedMessage } from 'react-intl'

export function SaveButton() {
  return <FormattedMessage id="admin/my-app.save" />
}


Backend or GraphQL translation pattern:

scalar IOMessage

type ProductLabel {
  id: ID
  label: IOMessage
}

type Query {
  productLabel(id: ID!): ProductLabel
}

export const resolvers = {
  Query: {
    productLabel: async (_: unknown, { id }: { id: string }) => {
      return {
        id,
        label: {
          content: 'store/my-app.product-label',
          description: 'Label for product badge',
          from: 'en-US',
        },
      }
    },
  },
}


Keep a complete en.json as the default fallback, even when the app’s main audience uses another locale, so the messages system has a stable base for resolution and auto-translation behavior.

Use translated IDs in code, keep translation files explicit, and centralize user-facing copy in the messages system instead of scattering literals through the app.

Common failure modes
Hardcoding user-facing strings in JSX, resolvers, or handler responses.
Adding new message IDs in code without updating context.json or the message files.
Using generic or collision-prone keys such as title, save, or button.
Storing configuration values or non-localized business payloads in message files.
Treating vtex.messages overrides as the default path instead of app-local message management.
Review checklist
 Are user-facing strings sourced from the messages infrastructure instead of hardcoded in code?
 Are message keys explicit, app-scoped, and declared consistently?
 Does context.json reflect the translation surface used by the app?
 Are message files limited to localized copy rather than configuration or operational data?
 Is any customization of vtex.messages truly necessary for this app?
Related skills
vtex-io-storefront-react - Use when the main question is storefront component structure and shopper-facing UI behavior
vtex-io-admin-react - Use when the main question is Admin UI structure and operational interaction patterns
vtex-io-graphql-api - Use when the main question is GraphQL schema and resolver design rather than translation infrastructure
Reference
Messages - VTEX messages app and runtime translation behavior
Overwriting the Messages app - How app-specific overrides of vtex.messages work
Weekly Installs
160
Repository
vtex/skills
GitHub Stars
25
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass