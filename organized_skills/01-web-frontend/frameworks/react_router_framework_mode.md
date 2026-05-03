---
rating: ⭐⭐
title: react-router-framework-mode
url: https://skills.sh/remix-run/agent-skills/react-router-framework-mode
---

# react-router-framework-mode

skills/remix-run/agent-skills/react-router-framework-mode
react-router-framework-mode
Installation
$ npx skills add https://github.com/remix-run/agent-skills --skill react-router-framework-mode
Summary

Full-stack React development with file-based routing, server/client rendering, data loading, and type-safe route modules.

Supports file-based routing with nested routes, dynamic segments, and multiple rendering strategies (SSR, SPA, pre-rendering)
Handles data loading via loader/clientLoader and mutations via action/clientAction with built-in form handling and optimistic UI
Includes 10+ reference guides covering routing, data loading, actions, navigation, error boundaries, authentication, and type safety
Requires React Router 7.0.0+; middleware features need 7.9.0+ with v8_middleware flag
SKILL.md
React Router Framework Mode

Framework mode is React Router's full-stack development experience with file-based routing, server-side, client-side, and static rendering strategies, data loading and mutations, and type-safe route module API.

When to Apply
Configuring new routes (app/routes.ts)
Loading data with loader or clientLoader
Handling mutations with action or clientAction
Navigating with <Link>, <NavLink>, <Form>, redirect, and useNavigate
Implementing pending/loading UI states
Configuring SSR, SPA mode, or pre-rendering (react-router.config.ts)
Implementing authentication
References

Load the relevant reference for detailed guidance on the specific API/concept:

Reference	Use When
references/routing.md	Configuring routes, nested routes, dynamic segments
references/route-modules.md	Understanding all route module exports
references/special-files.md	Customizing root.tsx, adding global nav/footer, fonts
references/data-loading.md	Loading data with loaders, streaming, caching
references/actions.md	Handling forms, mutations, validation
references/navigation.md	Links, programmatic navigation, redirects
references/pending-ui.md	Loading states, optimistic UI
references/error-handling.md	Error boundaries, error reporting
references/rendering-strategies.md	SSR vs SPA vs pre-rendering configuration
references/middleware.md	Adding middleware (requires v7.9.0+)
references/sessions.md	Cookie sessions, authentication, protected routes
references/type-safety.md	Auto-generated route types, type imports, type safety
Version Compatibility

Some features require specific React Router versions. Always verify before implementing:

npm list react-router

Feature	Minimum Version	Notes
Middleware	7.9.0+	Requires v8_middleware flag
Core framework features	7.0.0+	loaders, actions, Form, etc.
Critical Patterns

These are the most important patterns to follow. Load the relevant reference for full details.

Forms & Mutations

Search forms - use <Form method="get">, NOT onSubmit with setSearchParams:

// ✅ Correct
<Form method="get">
  <input name="q" />
</Form>

// ❌ Wrong - don't manually handle search params
<form onSubmit={(e) => { e.preventDefault(); setSearchParams(...) }}>


Inline mutations - use useFetcher, NOT <Form> (which causes page navigation):

const fetcher = useFetcher();
const optimistic = fetcher.formData?.get("favorite") === "true" ?? isFavorite;

<fetcher.Form method="post" action={`/favorites/${id}`}>
  <button>{optimistic ? "★" : "☆"}</button>
</fetcher.Form>;


See references/actions.md for complete patterns.

Layouts

Global UI belongs in root.tsx - don't create separate layout files for nav/footer:

// app/root.tsx - add navigation, footer, providers here
export default function App() {
  return (
    <div>
      <nav>...</nav>
      <Outlet />
      <footer>...</footer>
    </div>
  );
}


Use nested routes for section-specific layouts. See references/routing.md.

Route Module Exports

meta uses loaderData, not deprecated data:

// ✅ Correct
export function meta({ loaderData }: Route.MetaArgs) { ... }

// ❌ Wrong - `data` is deprecated
export function meta({ data }: Route.MetaArgs) { ... }


See references/route-modules.md for all exports.

Further Documentation

If anything related to React Router is not covered in these references, you can search the official documentation:

https://reactrouter.com/docs

Weekly Installs
1.9K
Repository
remix-run/agent-skills
GitHub Stars
125
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass