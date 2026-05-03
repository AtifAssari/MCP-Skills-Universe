---
rating: ⭐⭐
title: react-router-v7
url: https://skills.sh/existential-birds/beagle/react-router-v7
---

# react-router-v7

skills/existential-birds/beagle/react-router-v7
react-router-v7
Installation
$ npx skills add https://github.com/existential-birds/beagle --skill react-router-v7
SKILL.md
React Router v7 Best Practices
Quick Reference

Router Setup (Data Mode):

import { createBrowserRouter, RouterProvider } from "react-router";

const router = createBrowserRouter([
  {
    path: "/",
    Component: Root,
    ErrorBoundary: RootErrorBoundary,
    loader: rootLoader,
    children: [
      { index: true, Component: Home },
      { path: "products/:productId", Component: Product, loader: productLoader },
    ],
  },
]);

ReactDOM.createRoot(root).render(<RouterProvider router={router} />);


Framework Mode (Vite plugin):

// routes.ts
import { index, route } from "@react-router/dev/routes";

export default [
  index("./home.tsx"),
  route("products/:pid", "./product.tsx"),
];

Route Configuration
Nested Routes with Outlets
createBrowserRouter([
  {
    path: "/dashboard",
    Component: Dashboard,
    children: [
      { index: true, Component: DashboardHome },
      { path: "settings", Component: Settings },
    ],
  },
]);

function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <Outlet /> {/* Renders child routes */}
    </div>
  );
}

Dynamic Segments and Splats
{ path: "teams/:teamId" }           // params.teamId
{ path: ":lang?/categories" }       // Optional segment
{ path: "files/*" }                 // Splat: params["*"]

Key Decision Points
Form vs Fetcher

Use <Form>: Creating/deleting with URL change, adding to history Use useFetcher: Inline updates, list operations, popovers - no URL change

Loader vs useEffect

Use loader: Data before render, server-side fetch, automatic revalidation Use useEffect: Client-only data, user-interaction dependent, subscriptions

Additional Documentation
Data Loading: See references/loaders.md for loader patterns, parallel loading, search params
Mutations: See references/actions.md for actions, Form, fetchers, validation
Navigation: See references/navigation.md for Link, NavLink, programmatic nav
Advanced: See references/advanced.md for error boundaries, protected routes, lazy loading
Mode Comparison
Feature	Framework Mode	Data Mode	Declarative Mode
Setup	Vite plugin	createBrowserRouter	<BrowserRouter>
Type Safety	Auto-generated types	Manual	Manual
SSR Support	Built-in	Manual	Limited
Use Case	Full-stack apps	SPAs with control	Simple/legacy
Weekly Installs
348
Repository
existential-birds/beagle
GitHub Stars
56
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass