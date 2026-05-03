---
title: schema0-mobile
url: https://skills.sh/schema0/skills/schema0-mobile
---

# schema0-mobile

skills/schema0/skills/schema0-mobile
schema0-mobile
Installation
$ npx skills add https://github.com/schema0/skills --skill schema0-mobile
SKILL.md
Mobile Platform

React Native / Expo app at apps/mobile/. Skip this if apps/mobile/ does not exist.

Overview

Mobile apps use a single Cloudflare Worker (apps/mobile/worker.ts) that handles both static assets and API. API routes are mounted at /rpc via Hono + RPCHandler using the same routers from packages/api/.

Key Differences from Web
Uses @tanstack/react-query directly (NOT TanStack DB / useLiveQuery)
Data fetching: useQuery(orpc.{entity}.selectAll.queryOptions())
Auth via @schema0/auth-mobile + WorkOS (NOT @template/auth)
API calls go to deployed backend at EXPO_PUBLIC_WEB_URL/rpc
Environment variables use EXPO_PUBLIC_* prefix
Navigation via Expo Router (file-based)
Required Env Vars

Validated in _layout.tsx:

EXPO_PUBLIC_WORKOS_CLIENT_ID
EXPO_PUBLIC_ORGANIZATION_ID
EXPO_PUBLIC_WEB_URL
EXPO_PUBLIC_API_HOSTNAME
EXPO_PUBLIC_APP_ID
Deploying
schema0 sandbox deploy --platform mobile

References
references/patterns.md -- ORPC client setup, data fetching with useQuery, navigation, web vs mobile comparison table
Weekly Installs
17
Repository
schema0/skills
First Seen
9 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass