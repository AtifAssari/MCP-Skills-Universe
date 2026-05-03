---
title: firecrawl-build-onboarding
url: https://skills.sh/firecrawl/skills/firecrawl-build-onboarding
---

# firecrawl-build-onboarding

skills/firecrawl/skills/firecrawl-build-onboarding
firecrawl-build-onboarding
Installation
$ npx skills add https://github.com/firecrawl/skills --skill firecrawl-build-onboarding
SKILL.md
Firecrawl Build Onboarding

Use this skill for the application-integration path from Firecrawl's onboarding flow.

Install

If you haven't installed yet, one command sets up both the CLI tools (for live web work) and the build skills (for app integration):

npx -y firecrawl-cli@latest init --all --browser


This installs the Firecrawl CLI, the CLI skills, and these build skills together. It also opens browser auth so the human can sign in or create an account. No separate npx skills add step is needed.

Use This When
a project needs FIRECRAWL_API_KEY
the user wants Firecrawl wired into .env
you are adding Firecrawl to an app for the first time
you need to choose the first SDK or REST path

If the human still needs to sign up, sign in, or authorize access in the browser, use the auth flow reference in this skill.

Quick Start

If the user already has an API key, place it in .env:

FIRECRAWL_API_KEY=fc-...


If the project is self-hosted, also set:

FIRECRAWL_API_URL=https://your-firecrawl-instance.example.com


Then decide which integration path applies:

Fresh project -> choose the target stack, install the SDK, add the first Firecrawl call, and run a smoke test
Existing project -> inspect the repo first, then integrate Firecrawl where the project already handles third-party APIs and env vars
What Do You Need?
Task	Reference
Run the browser auth flow and save FIRECRAWL_API_KEY	references/auth-flow.md
Install the right SDK	references/sdk-installation.md
Put credentials into .env or project config	references/project-setup.md
Choose the right endpoint after setup	firecrawl-build
Need live web tooling during this task	The CLI skills are already installed from the same command
Start implementation from a known URL	firecrawl-build-scrape
Start implementation from a query	firecrawl-build-search
Docs (Source of Truth)

Read the source-of-truth page for your project language for SDK usage, schemas, and examples:

Node / TypeScript: docs.firecrawl.dev/agent-source-of-truth/node
Python: docs.firecrawl.dev/agent-source-of-truth/python
Rust: docs.firecrawl.dev/agent-source-of-truth/rust
Java: docs.firecrawl.dev/agent-source-of-truth/java
Elixir: docs.firecrawl.dev/agent-source-of-truth/elixir
cURL / REST: docs.firecrawl.dev/agent-source-of-truth/curl
After Setup

Once the key is present:

decide whether this is a fresh project or an existing codebase
ask what Firecrawl should do in the product
pick the narrowest endpoint that matches that behavior
read the source-of-truth page for the project language before writing code
add the SDK or REST call in code
run a smoke test that proves one real Firecrawl request succeeds
use the endpoint-specific skills in this repo for implementation guidance
if you also need live web tooling during the current task, the CLI skills are already installed — use firecrawl/cli
Weekly Installs
16.5K
Repository
firecrawl/skills
GitHub Stars
4
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass