---
rating: ⭐⭐
title: app-builder
url: https://skills.sh/davila7/claude-code-templates/app-builder
---

# app-builder

skills/davila7/claude-code-templates/app-builder
app-builder
Originally fromsickn33/antigravity-awesome-skills
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill app-builder
SKILL.md
App Builder - Application Building Orchestrator

Analyzes user's requests, determines tech stack, plans structure, and coordinates agents.

🎯 Selective Reading Rule

Read ONLY files relevant to the request! Check the content map, find what you need.

File	Description	When to Read
project-detection.md	Keyword matrix, project type detection	Starting new project
tech-stack.md	2025 default stack, alternatives	Choosing technologies
agent-coordination.md	Agent pipeline, execution order	Coordinating multi-agent work
scaffolding.md	Directory structure, core files	Creating project structure
feature-building.md	Feature analysis, error handling	Adding features to existing project
templates/SKILL.md	Project templates	Scaffolding new project
📦 Templates (13)

Quick-start scaffolding for new projects. Read the matching template only!

Template	Tech Stack	When to Use
nextjs-fullstack	Next.js + Prisma	Full-stack web app
nextjs-saas	Next.js + Stripe	SaaS product
nextjs-static	Next.js + Framer	Landing page
nuxt-app	Nuxt 3 + Pinia	Vue full-stack app
express-api	Express + JWT	REST API
python-fastapi	FastAPI	Python API
react-native-app	Expo + Zustand	Mobile app
flutter-app	Flutter + Riverpod	Cross-platform mobile
electron-desktop	Electron + React	Desktop app
chrome-extension	Chrome MV3	Browser extension
cli-tool	Node.js + Commander	CLI app
monorepo-turborepo	Turborepo + pnpm	Monorepo
🔗 Related Agents
Agent	Role
project-planner	Task breakdown, dependency graph
frontend-specialist	UI components, pages
backend-specialist	API, business logic
database-architect	Schema, migrations
devops-engineer	Deployment, preview
Usage Example
User: "Make an Instagram clone with photo sharing and likes"

App Builder Process:
1. Project type: Social Media App
2. Tech stack: Next.js + Prisma + Cloudinary + Clerk
3. Create plan:
   ├─ Database schema (users, posts, likes, follows)
   ├─ API routes (12 endpoints)
   ├─ Pages (feed, profile, upload)
   └─ Components (PostCard, Feed, LikeButton)
4. Coordinate agents
5. Report progress
6. Start preview

Weekly Installs
362
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn