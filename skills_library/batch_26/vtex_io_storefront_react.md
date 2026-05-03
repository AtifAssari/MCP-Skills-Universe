---
title: vtex-io-storefront-react
url: https://skills.sh/vtex/skills/vtex-io-storefront-react
---

# vtex-io-storefront-react

skills/vtex/skills/vtex-io-storefront-react
vtex-io-storefront-react
Installation
$ npx skills add https://github.com/vtex/skills --skill vtex-io-storefront-react
SKILL.md
Storefront React Components
When this skill applies

Use this skill when building shopper-facing React components under the react builder for storefront experiences.

Creating product or category UI widgets
Building custom banners, forms, and shopper-facing layout pieces
Using storefront hooks or context providers
Styling components with css-handles

Do not use this skill for:

admin pages
block registration and render-runtime contracts
service runtime or backend route design
GraphQL schema design
Decision rules
Treat storefront components as browser-facing UI and keep them safe for shopper contexts.
Prefer keeping storefront components presentational and props-driven, and move complex data fetching or business logic to hooks or container components.
Use vtex.css-handles instead of hardcoded global class names.
Prefer receiving data through props or documented storefront hooks and contexts such as useProduct, useRuntime, or useOrderForm instead of calling VTEX APIs directly from the browser or using app keys in storefront code.
Keep components resilient to loading, empty, and unavailable product or search context.
For shopper-facing copy, use message IDs and helpers from the messages infrastructure, as described in vtex-io-messages-and-i18n, instead of string literals.
Treat storefront components as part of the storefront accessibility surface: use semantic HTML elements such as button or a instead of clickable divs, and ensure important content has appropriate labels or alternative text.
When accessing browser globals such as window or document, guard against server-side execution, for example by using useEffect or checking typeof window !== 'undefined'.
Hard constraints
Constraint: Storefront styling must use css-handles

Storefront components MUST expose styling through css-handles, not arbitrary hardcoded class names.

Why this matters

css-handles are the customization contract for storefront components. Hardcoded or hidden class names make themes harder to extend safely.

Detection

If a storefront component uses arbitrary global class names without css-handles, STOP and expose styling through handles first.

Correct

const CSS_HANDLES = ['container', 'title'] as const


Wrong

return <div className="my-random-block-root">...</div>

Constraint: Storefront components must remain browser-safe

Storefront React code MUST not depend on Node-only APIs or server-only assumptions.

Why this matters

These components run in the shopper-facing frontend. Server-only dependencies break rendering and create runtime failures in the browser.

Detection

If a component uses Node-only modules, filesystem access, or server runtime assumptions, STOP and redesign it for the browser.

Correct

return <span>{label}</span>


Wrong

import fs from 'fs'

Constraint: Shopper-facing strings must be localizable

Visible storefront strings MUST use the app i18n pattern instead of hardcoded text.

Why this matters

Storefront UIs run across locales and stores. Hardcoded strings make the component less reusable and less consistent with VTEX IO localization.

Detection

If shopper-visible copy is hardcoded in JSX, STOP and move it to the i18n mechanism.

Correct

<FormattedMessage id="storefront.cta" />


Wrong

<span>Buy now</span>

Preferred pattern

Keep storefront components small, props-driven, css-handle-based, and safe for shopper contexts.

Minimal css-handles pattern:

import { useCssHandles } from 'vtex.css-handles'

const CSS_HANDLES = ['container', 'title'] as const

export function MyComponent() {
  const { handles } = useCssHandles(CSS_HANDLES)

  return (
    <div className={handles.container}>
      <h2 className={handles.title}>...</h2>
    </div>
  )
}

Common failure modes
Hardcoding class names instead of using css-handles.
Using browser-unsafe dependencies.
Hardcoding shopper-visible strings.
Fetching data in ad hoc ways instead of using VTEX storefront patterns.
Putting complex business logic or heavy data fetching directly inside presentational components instead of using hooks or containers.
Using non-semantic clickable elements such as div or span with onClick where a button or a element should be used.
Review checklist
 Is this component truly shopper-facing?
 Are styles exposed through css-handles?
 Is the component safe for browser execution?
 Are visible strings localized?
 Is the data flow appropriate for a storefront component?
Related skills
vtex-io-render-runtime-and-blocks - Use when the main question is block registration and Store Framework wiring
vtex-io-messages-and-i18n - Use when the main question is how shopper-facing strings should be translated and organized
Reference
Store Framework - Storefront app context, data, and hooks
CSS Handles - Styling contract for VTEX IO storefront components
Weekly Installs
171
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