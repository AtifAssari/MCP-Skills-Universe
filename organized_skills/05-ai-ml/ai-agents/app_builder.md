---
rating: ⭐⭐
title: app-builder
url: https://skills.sh/sickn33/antigravity-awesome-skills/app-builder
---

# app-builder

skills/sickn33/antigravity-awesome-skills/app-builder
app-builder
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill app-builder
Summary

Full-stack application orchestrator that analyzes requests, selects tech stacks, and coordinates multi-agent development.

Detects project type from natural language and recommends appropriate technology stack from 13 pre-built templates covering web apps, APIs, mobile, desktop, and CLI tools
Coordinates execution across specialized agents: project planner, frontend specialist, backend specialist, database architect, and DevOps engineer
Provides selective reading guidance through a content map to avoid unnecessary context loading during multi-agent workflows
Handles project scaffolding, feature planning, and error recovery across full-stack development pipelines
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

When to Use

This skill is applicable to execute the workflow or actions described in the overview.

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
656
Repository
sickn33/antigra…e-skills
GitHub Stars
36.0K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass