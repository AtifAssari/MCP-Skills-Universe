---
title: refine-dev
url: https://skills.sh/itechmeat/llm-code/refine-dev
---

# refine-dev

skills/itechmeat/llm-code/refine-dev
refine-dev
Installation
$ npx skills add https://github.com/itechmeat/llm-code --skill refine-dev
SKILL.md
Refine.dev Framework

Refine is a headless React framework for building enterprise CRUD applications. It provides data fetching, routing, authentication, and access control out of the box while remaining UI-agnostic.

Core Concepts

Refine is built around these key abstractions:

Data Provider — adapter for your backend (REST, GraphQL, etc.)
Resources — entities in your app (e.g., posts, users, products)
Hooks — useList, useOne, useCreate, useUpdate, useDelete, useForm, useTable
Auth Provider — handles login, logout, permissions
Router Provider — integrates with React Router, etc.
Quick Start (Vite)

Scaffold: npm create refine-app@latest (select Vite, Mantine, REST API). For manual setup, install @refinedev/core @refinedev/mantine @refinedev/react-router and Mantine packages.

Minimal App Structure
// src/App.tsx
import { Refine } from "@refinedev/core";
import { MantineProvider } from "@mantine/core";
import routerProvider from "@refinedev/react-router";
import dataProvider from "@refinedev/simple-rest";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <MantineProvider>
        <Refine
          dataProvider={dataProvider("https://api.example.com")}
          routerProvider={routerProvider}
          resources={[
            {
              name: "posts",
              list: "/posts",
              create: "/posts/create",
              edit: "/posts/edit/:id",
              show: "/posts/show/:id",
            },
          ]}
        >
          <Routes>{/* Your routes here */}</Routes>
        </Refine>
      </MantineProvider>
    </BrowserRouter>
  );
}

Critical Prohibitions
Do NOT mix multiple UI libraries (pick Mantine and stick with it)
Do NOT bypass data provider — always use Refine hooks for data operations
Do NOT hardcode API URLs — use data provider configuration
Do NOT skip resource definition — all CRUD entities must be declared in resources
Do NOT ignore TypeScript types — Refine is fully typed, leverage it
Steps for New Feature
Define the resource in <Refine resources={[...]}>
Create page components (List, Create, Edit, Show)
Set up routes matching resource paths
Use appropriate hooks (useTable for lists, useForm for create/edit)
Configure auth provider if authentication is needed
Definition of Done
 Resource defined in Refine configuration
 All CRUD pages implemented with proper hooks
 Routes match resource configuration
 TypeScript types for resource data defined
 Error handling in place
 Loading states handled
Release Note (5.0.12)
useList and useTable now preserve custom fields returned by getList, which matters when your data provider returns extra aggregate or pagination metadata alongside the row list.
References (Detailed Guides)
Core
data-providers.md — Data provider interface, available providers, custom implementation
resources.md — Resource definition and configuration
routing.md — React Router integration and route patterns
Hooks
hooks.md — All hooks: useList, useOne, useCreate, useUpdate, useDelete, useForm, useTable, useSelect
Security & Auth
auth.md — Auth provider, access control, RBAC/ABAC, Casbin/CASL integration
UI & Components
mantine-ui.md — Mantine components integration
inferencer.md — Auto-generate CRUD pages from API schema
Utilities & Features
notifications.md — Notification provider and useNotification hook
i18n.md — Internationalization with i18nProvider
realtime.md — LiveProvider for websocket/realtime subscriptions
Links
Documentation
Releases
GitHub
npm
Weekly Installs
98
Repository
itechmeat/llm-code
GitHub Stars
15
First Seen
Jan 29, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn