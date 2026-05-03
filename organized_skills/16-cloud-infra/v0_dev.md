---
title: v0-dev
url: https://skills.sh/vercel-labs/vercel-plugin/v0-dev
---

# v0-dev

skills/vercel-labs/vercel-plugin/v0-dev
v0-dev
Installation
$ npx skills add https://github.com/vercel-labs/vercel-plugin --skill v0-dev
SKILL.md
v0 by Vercel

You are an expert in v0 (v0.app) — Vercel's AI-powered development agent that generates production-ready code from natural language descriptions.

Overview

v0 transforms prompts into working React/Next.js code. It supports 6M+ developers and 80K+ active teams globally. v0 operates as a universal coding agent with research, planning, debugging, and iteration capabilities.

Core Capabilities
Natural language → code: Describe what you want, get production React components
Visual input: Upload Figma designs, screenshots, or sketches → code
Multi-framework: Outputs React, Vue, Svelte, HTML, Markdown
Agentic intelligence: Research, plan, debug, iterate autonomously
shadcn/ui + Tailwind CSS: Default styling system
Full IDE: Built-in VS Code editor, terminal, and git panel in the web UI
CLI Usage
Component Integration CLI (v0 package)

Install and pull v0-generated components into your Next.js project:

# Initialize v0 in an existing Next.js project (one-time setup)
npx v0@latest init

# Add a specific v0-generated component by ID
npx v0@latest add <component-id>

# With pnpm
pnpm dlx v0@latest init
pnpm dlx v0@latest add <component-id>


v0 init installs required dependencies (@radix-ui/react-icons, clsx, lucide-react) and creates a components.json config file.

"Add to Codebase" (Web UI → Local)

From the v0.dev web interface, click the "Add to Codebase" button (terminal icon) to generate a command:

npx shadcn@latest add "https://v0.dev/chat/b/<project_id>?token=<token>"


Run this in your project root to pull the entire generated project into your codebase.

Typical Workflow
# 1. Scaffold a Next.js app
npx create-next-app@latest --typescript --tailwind --eslint

# 2. Initialize v0 integration
npx v0@latest init

# 3. Generate a component on v0.dev, get its ID
# 4. Add the component locally
npx v0@latest add a1B2c3d4

# 5. Import and use in your app

Project Scaffolding CLI
# Create a new project from v0 templates
npx create-v0-sdk-app@latest my-v0-app

# Use the v0-clone template (full v0.dev replica with auth, DB, streaming)
npx create-v0-sdk-app@latest --template v0-clone

v0 SDK (Programmatic API)
Installation
npm install v0-sdk

Authentication
import { v0 } from 'v0-sdk'
// Automatically reads from process.env.V0_API_KEY

// Or create a custom client:
import { createClient } from 'v0-sdk'
const v0 = createClient({ apiKey: process.env.CUSTOM_V0_KEY })


Get your API key at: https://v0.app/chat/settings/keys

Create a Chat and Generate Code
import { v0 } from 'v0-sdk'

const chat = await v0.chats.create({
  message: 'Create a responsive navbar with dark mode toggle using Tailwind',
  system: 'You are an expert React developer',
})

console.log(`Open in browser: ${chat.webUrl}`)

Full Project Workflow (Create → Chat → Deploy)
import { v0 } from 'v0-sdk'

// Create a project
const project = await v0.projects.create({ name: 'My App' })

// Initialize a chat with existing code
const chat = await v0.chats.init({
  type: 'files',
  files: [{ name: 'App.tsx', content: existingCode }],
  projectId: project.id,
})

// Send follow-up instructions
await v0.chats.sendMessage({
  chatId: chat.id,
  message: 'Add a sidebar with navigation links and a user avatar',
})

// Deploy when ready
const deployment = await v0.deployments.create({
  projectId: project.id,
  chatId: chat.id,
  versionId: chat.latestVersion.id,
})

console.log(`Live at: ${deployment.url}`)

Download Generated Code
// Download files from a specific chat version
const files = await v0.chats.downloadVersion({
  chatId: chat.id,
  versionId: chat.latestVersion.id,
})

SDK Method Reference

Chats:

v0.chats.create(params) — Create a new chat
v0.chats.sendMessage(params) — Send a message to an existing chat
v0.chats.getById(params) — Retrieve a specific chat
v0.chats.update(params) — Update chat properties
v0.chats.findVersions(params) — List all versions of a chat
v0.chats.getVersion(params) — Retrieve a specific version
v0.chats.updateVersion(params) — Update files within a version
v0.chats.downloadVersion(params) — Download files for a version
v0.chats.resume(params) — Resume processing of a message

Projects:

v0.projects.create(params) — Create a new project
v0.projects.getById(params) — Retrieve a project
v0.projects.update(params) — Update a project
v0.projects.find() — List all projects
v0.projects.assign(params) — Assign a chat to a project
v0.projects.getByChatId(params) — Get project by chat ID
v0.projects.createEnvVars(params) — Create env vars for a project

Deployments:

v0.deployments.create(params) — Create deployment from a chat version
v0.deployments.getById(params) — Get deployment details
v0.deployments.delete(params) — Delete a deployment
v0.deployments.find(params) — List deployments
v0.deployments.findLogs(params) — Get deployment logs
REST API

Base URL: https://api.v0.dev/v1 Auth: Authorization: Bearer <V0_API_KEY>

Method	Endpoint	Description
GET	/v1/projects	List projects
POST	/v1/projects	Create project
GET	/v1/projects/:id	Get project
PUT	/v1/projects/:id	Update project
DELETE	/v1/projects/:id	Delete project
POST	/v1/chats	Create/initialize chat
GET	/v1/chats/:id/messages	Get messages
POST	/v1/chats/:id/messages	Send message
POST	/v1/deployments	Create deployment
Rate Limits
API Requests: 10,000/day
Chat Messages: 1,000/day
Deployments: 100/day
File Uploads: 1 GB/day
Projects per account: 100
Available Models
v0-1.5-md — Everyday tasks and UI generation
v0-1.5-lg — Advanced reasoning
v0-1.0-md — Legacy model
AI SDK Integration
Using v0 as an AI Provider
npm i @ai-sdk/vercel

import { vercel } from '@ai-sdk/vercel'
import { generateText } from 'ai'

const { text } = await generateText({
  model: vercel('v0-1.5-md'),
  prompt: 'Create a login form with email and password fields',
})

v0 AI Tools (Agent Integration)

Use v0's full capabilities as tools within an AI SDK agent:

npm install @v0-sdk/ai-tools ai

import { generateText } from 'ai'
import { openai } from '@ai-sdk/openai'
import { v0Tools } from '@v0-sdk/ai-tools'

const result = await generateText({
  model: openai('gpt-5.2'),
  prompt: 'Create a new React dashboard project with charts and a data table',
  tools: v0Tools({ apiKey: process.env.V0_API_KEY }),
})


For granular control, import specific tool sets:

import { createChatTools, createProjectTools, createDeploymentTools } from '@v0-sdk/ai-tools'


The v0Tools export includes 20+ tools: createChat, sendMessage, getChat, updateChat, deleteChat, favoriteChat, forkChat, listChats, createProject, getProject, updateProject, listProjects, assignChatToProject, createEnvironmentVariables, createDeployment, getDeployment, deleteDeployment, listDeployments, getDeploymentLogs.

MCP Server

Connect v0 to any MCP-compatible IDE (Cursor, Claude Desktop, etc.):

{
  "mcpServers": {
    "v0": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.v0.dev",
        "--header",
        "Authorization: Bearer ${V0_API_KEY}"
      ]
    }
  }
}


Exposes 4 tools: create chat, get chat info, find chats, send messages.

GitHub Integration
Setup
In the v0 chat sidebar → Git section → click Connect
Select GitHub account/org scope and repository name
Click Create Repository — links chat to a new private GitHub repo
A Vercel deployment is automatically created
Branch Behavior (Automatic)
Every chat creates a new branch (e.g., v0/main-e7bad8e4)
Every prompt that changes code automatically commits and pushes
You never work directly on main
PR Workflow
Click the Publish button (shows PR icon when GitHub-connected)
Select Open PR — creates PR from v0/main-abc123 → main
Review in the GitHub modal or on GitHub.com
Merge the PR → closes the chat permanently
Every PR gets a Preview Deployment; merging triggers Production Deployment
Importing Existing Repos
In v0 prompt bar → click + → "Import from GitHub"
v0 reads your existing codebase and env vars from Vercel
Iterate with prompts; all changes committed to a new branch
Prompt Engineering Tips
1. Be Specific About Design
Weak:  "Build a dashboard"
Strong: "Build a support ticket dashboard. Mobile-first, light theme, high
        contrast. Color code: red for urgent, yellow for medium, green for low.
        Show agent status badges. Maximum 2 columns on mobile."

2. Specify Your Tech Stack
"Build a real-time chat app using: Next.js 16 with App Router,
Socket.io for messaging, Vercel Postgres for storage,
NextAuth.js for authentication."

3. Define User Roles
"Create a team collaboration tool with admin, manager, and member
roles, task assignment, progress tracking, and file sharing."

4. Queue Multiple Prompts

You can queue up to 10 prompts while v0 is still generating:

"Create the base layout with navigation"
"Add authentication with NextAuth"
"Connect the database and add CRUD operations"
"Add a settings page with dark mode toggle"
5. Specify Error and Empty States
"Add comprehensive error handling for network failures, invalid
input, and empty states with helpful recovery suggestions."

6. Use Visual Selection for Precision

Click a specific element in the preview before typing to target exactly what you want to change. Eliminates ambiguity for multi-instance components.

7. Use Design Mode vs Prompts
Prompts: Structural changes, adding features, wiring up logic
Design Mode (click element → adjust): Colors, spacing, typography tweaks
8. v0's Default Output Stack

When no framework is specified, v0 generates:

React with JSX + TypeScript
Tailwind CSS
shadcn/ui components
Lucide React icons
Complete, copy-paste-ready code (never partial stubs)
Design Normalization for v0 Output

v0 is strongest when you specify both structure and aesthetic direction. For Vercel-stack projects, include guidance like: use shadcn/ui primitives, use Geist fonts, default to dark mode, use zinc/neutral tokens, avoid generic card grids. After importing v0 code, normalize it: replace ad-hoc controls with shadcn components, collapse repeated card grids into stronger patterns, align typography to Geist, remove mixed radii and decorative effects.

Integration Patterns
Pattern 1: Generate Components, Import Locally

Best for adding individual UI components to an existing app.

npx v0@latest init
npx v0@latest add <component-id>


Then import the component:

import { DataTable } from '@/components/data-table'

export default function DashboardPage() {
  return <DataTable data={rows} columns={columns} />
}

Pattern 2: GitHub Round-Trip

Best for iterating on a full feature branch with non-engineers.

Import repo into v0 from GitHub
Non-engineer iterates via prompts
v0 auto-commits each change to a feature branch
Engineer reviews the PR, merges
Pattern 3: SDK Automation

Best for CI/CD pipelines or programmatic component generation.

import { v0 } from 'v0-sdk'

// Generate a component from a design spec
const chat = await v0.chats.create({
  message: `Create a pricing table component with these tiers:
    - Free: 0/mo, 1 project, community support
    - Pro: $20/mo, unlimited projects, priority support
    - Enterprise: Custom, SLA, dedicated support`,
})

// Wait for generation, then download
const files = await v0.chats.downloadVersion({
  chatId: chat.id,
  versionId: chat.latestVersion.id,
})

Pattern 4: v0 as AI Agent Tool

Best for autonomous agents that need to generate and deploy UI.

import { Agent } from 'ai'
import { v0Tools } from '@v0-sdk/ai-tools'

const agent = new Agent({
  model: openai('gpt-5.2'),
  tools: {
    ...v0Tools({ apiKey: process.env.V0_API_KEY }),
    // ... other tools
  },
  system: 'You are a full-stack developer. Use v0 to generate UI components.',
})

const { text } = await agent.generateText({
  prompt: 'Create a dashboard for our analytics data and deploy it',
})

Built-in Integrations

v0 has native support for these services in its sandbox:

Databases: Neon (PostgreSQL), Supabase, Upstash Redis, Vercel Blob
AI: OpenAI, Anthropic, Groq, Grok, fal, Deep Infra (via Vercel AI Gateway)
Payments: Stripe
External APIs: Twilio, and others via the "Vars" panel
Limitations
Best for UI components and layouts (~20% of a full application)
Backend, database, auth, and AI integration require separate implementation or explicit prompting
Generated code may need manual fixes for complex business logic
Enterprise-level scalability needs additional architecture review
shadcn/ui is the primary component library; other libraries require explicit prompting
Official Documentation
v0 App
v0 Documentation
v0 API Overview
v0 AI Tools
v0 MCP Server
v0 GitHub Integration
API Keys
GitHub: v0 SDK
Weekly Installs
53
Repository
vercel-labs/ver…l-plugin
GitHub Stars
156
First Seen
Mar 7, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn