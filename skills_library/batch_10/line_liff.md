---
title: line-liff
url: https://skills.sh/abgne/line-dev/line-liff
---

# line-liff

skills/abgne/line-dev/line-liff
line-liff
Installation
$ npx skills add https://github.com/abgne/line-dev --skill line-liff
SKILL.md
LINE LIFF (Front-end Framework)

Do not answer LIFF questions from memory — LINE updates APIs frequently and training data is unreliable. Always consult the references below.

Reference for building, reviewing, and debugging LIFF web apps inside LINE.

Workflow
Build
Read references/guidelines.md (registration, endpoint URL rules, environment compatibility)
Load the relevant reference for the feature being implemented
For architecture or design choices, consult references/experts.md for directional guidance
Write code following specs and constraints from references
Review / Debug
Read references/guidelines.md (URL constraints, authentication flow, API availability)
Load relevant references for the code being reviewed
Cross-check code against specs (endpoint URL rules, scope requirements, environment limitations, init order)
For design pattern concerns, consult references/experts.md
Report violations with reference to specific constraints
Environment Variables
LIFF_ID=LIFF app ID (from LINE Developers Console)
LINE_LOGIN_CHANNEL_ID=LINE Login Channel ID (for server-side JWT verification)
LINE_LOGIN_CHANNEL_SECRET=Channel secret (server-side only)
CHANNEL_ACCESS_TOKEN=Channel access token (for LIFF Server API — manage LIFF apps programmatically)

SDK

Install via CDN or npm. For tree-shaking (reduce ~34% bundle size), use pluggable SDK.

SDK installation, CDN/npm setup, pluggable SDK → references/api.md § Pluggable SDK

Initialization
liff.init({ liffId: 'YOUR_LIFF_ID', withLoginOnExternalBrowser: true })
  .then(() => { /* use LIFF APIs */ })
  .catch(err => console.error(err.code, err.message));

Must be called before all LIFF APIs (except pre-init methods)
withLoginOnExternalBrowser: true — auto-trigger login in external browser
liff.ready — Promise that resolves when init completes
Getting Started
Create a LINE Login channel in LINE Developers Console
Add a LIFF app and set the Endpoint URL (HTTPS required)
Integrate SDK, call liff.init()
Or scaffold with npx @line/create-liff-app (React/Vue/Svelte/Next.js/Nuxt/vanilla)
API Reference

Complete API reference (methods, parameters, scopes, availability matrix) → references/api.md

View Sizes
Type	Coverage
Full	100% screen
Tall	~75%
Compact	~50%
Key Constraints
Endpoint URL: liff.init() only works at or below the registered Endpoint URL
URL handling: modify URLs only after liff.init() resolves
Universal Links: use https://liff.line.me/{liffId} as primary entry point
Token security: send raw ID Token to server for verification, never expose decoded token → see server-auth.md
Login behavior differs: auto in LIFF browser, manual in external browser
Deprecated APIs: liff.scanCode() → use scanCodeV2(); liff.getLanguage() → use getAppLanguage(); liff.permanentLink.createUrl() → use createUrlBy() (may be removed in v3)
Reference Index
File	Topic
references/api.md	LIFF v2 API complete reference, pluggable SDK modules, error codes
references/guidelines.md	Registration, endpoint URL rules, authentication flow, UI/UX, environment compatibility
references/navigation.md	LIFF URLs, liff.state, permanent links, LIFF-to-LIFF transitions, browser minimization
references/plugins.md	LIFF plugin development, hooks system, official plugins (Inspector, Mock)
references/server-api.md	LIFF Server API (v1) — programmatic LIFF app CRUD (create, update, list, delete)
references/server-auth.md	Server-side ID Token (JWT) verification
references/cli.md	LIFF CLI — local HTTPS dev server, app CRUD, Inspector debugging, ngrok
references/experts.md	LIFF domain experts for architecture guidance
SDK & Tools
npm: @line/liff
Pluggable SDK: @line/liff/core + individual modules
Official plugins: @line/liff-inspector | @line/liff-mock
LIFF CLI: CLI tool (create, serve, deploy, HTTPS dev server)
Create LIFF App: npx @line/create-liff-app — scaffolding (React/Vue/Svelte/Next.js/Nuxt/vanilla, JS/TS)
LIFF Playground: liff-playground.netlify.app — online API testing
Starter app: line/line-liff-v2-starter (vanilla/Next.js/Nuxt)
Weekly Installs
37
Repository
abgne/line-dev
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass