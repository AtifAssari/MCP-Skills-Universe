---
title: vercel-python-services
url: https://skills.sh/vercel-labs/py-ai/vercel-python-services
---

# vercel-python-services

skills/vercel-labs/py-ai/vercel-python-services
vercel-python-services
Installation
$ npx skills add https://github.com/vercel-labs/py-ai --skill vercel-python-services
SKILL.md
Python Services with Vercel

Build multi-service projects using Vercel's experimentalServices API with a Python backend and (optional) JavaScript frontend.

Setup
Create the project files (see references for the minimal working example). Choose frameworks for each service according to user's requests.
Define backend routes without the /api prefix (e.g. @app.get("/health")). Vercel strips the prefix before forwarding to the backend.
Validate services in vercel.json have entrypoint and routePrefix, but no extra unknown fields, otherwise that will cause preview to crash

Only vercel.json lives at the root. Each service manages its own dependencies independently.

Usage
Use vercel dev -L from the project root to run all services as one application. The CLI will handle each individual service's routing and dev server and put the application on port 3000.
Frontend calls /api/... — Vercel routes these to the backend, which sees only the path after the prefix. No localhost URLs, no proxy needed.
Weekly Installs
28
Repository
vercel-labs/py-ai
GitHub Stars
40
First Seen
Mar 4, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass