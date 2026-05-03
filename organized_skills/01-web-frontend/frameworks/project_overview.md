---
rating: ⭐⭐⭐
title: project-overview
url: https://skills.sh/lobehub/lobehub/project-overview
---

# project-overview

skills/lobehub/lobehub/project-overview
project-overview
Installation
$ npx skills add https://github.com/lobehub/lobehub --skill project-overview
Summary

Complete project architecture guide for LobeHub, an open-source AI Agent Workspace built on Next.js and React.

Monorepo structure with @lobechat/ namespace packages covering agent runtime, model providers, database, tools, and platform-specific bridges (Electron, web, mobile)
Tech stack includes Next.js 16, React 19, TypeScript, Zustand for state, tRPC for type-safe APIs, Neon PostgreSQL with Drizzle ORM, and antd-style for CSS-in-JS
Three deployment targets: web (desktop/mobile), Electron desktop app, and React Native mobile (coming soon)
Data flow: React UI → Zustand stores → client services → tRPC routers → server services → Drizzle models → PostgreSQL; SPA routing via react-router-dom inside Next.js
SKILL.md
LobeHub Project Overview
Project Description

Open-source, modern-design AI Agent Workspace: LobeHub (previously LobeChat).

Supported platforms:

Web desktop/mobile
Desktop (Electron)
Mobile app (React Native) - coming soon

Logo emoji: 🤯

Complete Tech Stack
Category	Technology
Framework	Next.js 16 + React 19
Routing	SPA inside Next.js with react-router-dom
Language	TypeScript
UI Components	@lobehub/ui, antd
CSS-in-JS	antd-style
Icons	lucide-react, @ant-design/icons
i18n	react-i18next
State	zustand
URL Params	nuqs
Data Fetching	SWR
React Hooks	aHooks
Date/Time	dayjs
Utilities	es-toolkit
API	TRPC (type-safe)
Database	Neon PostgreSQL + Drizzle ORM
Testing	Vitest
Complete Project Structure

Monorepo using @lobechat/ namespace for workspace packages.

lobehub/
├── apps/
│   └── desktop/                 # Electron desktop app
├── docs/
│   ├── changelog/
│   ├── development/
│   ├── self-hosting/
│   └── usage/
├── locales/
│   ├── en-US/
│   └── zh-CN/
├── packages/
│   ├── agent-runtime/           # Agent runtime
│   ├── builtin-agents/
│   ├── builtin-tool-*/          # Builtin tool packages
│   ├── business/                # Cloud-only business logic
│   │   ├── config/
│   │   ├── const/
│   │   └── model-runtime/
│   ├── config/
│   ├── const/
│   ├── context-engine/
│   ├── conversation-flow/
│   ├── database/
│   │   └── src/
│   │       ├── models/
│   │       ├── schemas/
│   │       └── repositories/
│   ├── desktop-bridge/
│   ├── edge-config/
│   ├── editor-runtime/
│   ├── electron-client-ipc/
│   ├── electron-server-ipc/
│   ├── fetch-sse/
│   ├── file-loaders/
│   ├── memory-user-memory/
│   ├── model-bank/
│   ├── model-runtime/
│   │   └── src/
│   │       ├── core/
│   │       └── providers/
│   ├── observability-otel/
│   ├── prompts/
│   ├── python-interpreter/
│   ├── ssrf-safe-fetch/
│   ├── types/
│   ├── utils/
│   └── web-crawler/
├── src/
│   ├── app/
│   │   ├── (backend)/
│   │   │   ├── api/
│   │   │   ├── f/
│   │   │   ├── market/
│   │   │   ├── middleware/
│   │   │   ├── oidc/
│   │   │   ├── trpc/
│   │   │   └── webapi/
│   │   ├── spa/                  # SPA HTML template service
│   │   └── [variants]/
│   │       └── (auth)/           # Auth pages (SSR required)
│   ├── routes/                  # SPA page components (Vite)
│   │   ├── (main)/
│   │   ├── (mobile)/
│   │   ├── (desktop)/
│   │   ├── onboarding/
│   │   └── share/
│   ├── spa/                     # SPA entry points and router config
│   │   ├── entry.web.tsx
│   │   ├── entry.mobile.tsx
│   │   ├── entry.desktop.tsx
│   │   └── router/
│   ├── business/                # Cloud-only (client/server)
│   │   ├── client/
│   │   ├── locales/
│   │   └── server/
│   ├── components/
│   ├── config/
│   ├── const/
│   ├── envs/
│   ├── features/
│   ├── helpers/
│   ├── hooks/
│   ├── layout/
│   │   ├── AuthProvider/
│   │   └── GlobalProvider/
│   ├── libs/
│   │   ├── better-auth/
│   │   ├── oidc-provider/
│   │   └── trpc/
│   ├── locales/
│   │   └── default/
│   ├── server/
│   │   ├── featureFlags/
│   │   ├── globalConfig/
│   │   ├── modules/
│   │   ├── routers/
│   │   │   ├── async/
│   │   │   ├── lambda/
│   │   │   ├── mobile/
│   │   │   └── tools/
│   │   └── services/
│   ├── services/
│   ├── store/
│   │   ├── agent/
│   │   ├── chat/
│   │   └── user/
│   ├── styles/
│   ├── tools/
│   ├── types/
│   └── utils/
└── e2e/                         # E2E tests (Cucumber + Playwright)

Architecture Map
Layer	Location
UI Components	src/components, src/features
SPA Pages	src/routes/
React Router	src/spa/router/
Global Providers	src/layout
Zustand Stores	src/store
Client Services	src/services/
REST API	src/app/(backend)/webapi
tRPC Routers	src/server/routers/{async|lambda|mobile|tools}
Server Services	src/server/services (can access DB)
Server Modules	src/server/modules (no DB access)
Feature Flags	src/server/featureFlags
Global Config	src/server/globalConfig
DB Schema	packages/database/src/schemas
DB Model	packages/database/src/models
DB Repository	packages/database/src/repositories
Third-party	src/libs (analytics, oidc, etc.)
Builtin Tools	src/tools, packages/builtin-tool-*
Cloud-only	src/business/*, packages/business/*
Data Flow
React UI → Store Actions → Client Service → TRPC Lambda → Server Services → DB Model → PostgreSQL

Weekly Installs
936
Repository
lobehub/lobehub
GitHub Stars
75.9K
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass