---
rating: ⭐⭐
title: superdesign
url: https://skills.sh/superdesigndev/superdesign-skill/superdesign
---

# superdesign

skills/superdesigndev/superdesign-skill/superdesign
superdesign
Installation
$ npx skills add https://github.com/superdesigndev/superdesign-skill --skill superdesign
Summary

Design agent for frontend UI/UX creation, iteration, and component extraction on an infinite canvas.

Analyzes your repo structure to build design context automatically, then generates and iterates design drafts with support for variations, themes, and multi-page flows
Core commands cover project setup, faithful UI reproduction, design iteration in branch mode, component extraction and updates, and design system configuration
Requires mandatory initialization of .superdesign/init/ with component, layout, route, theme, and page dependency files before any design task
CLI must be installed globally and authenticated via superdesign login before running any commands
SKILL.md

SuperDesign helps you (1) find design inspirations/styles and (2) generate/iterate design drafts on an infinite canvas.

Core scenarios (what this skill handles)
superdesign init — Analyze the repo and build UI context to .superdesign/init/
Help me design X (feature/page/flow)
Set design system
Help me improve design of X
Init: Repo Analysis

When .superdesign/init/ directory doesn't exist or is empty, you MUST automatically:

Create the .superdesign/init/ directory
Fetch the init prompt from the URL below
Follow the prompt instructions to analyze the repo and write context files
https://raw.githubusercontent.com/superdesigndev/superdesign-skill/main/skills/superdesign/INIT.md


Do NOT ask the user to do this manually — just do it.

Mandatory Init Files

If .superdesign/init/ exists, you MUST read ALL files in this directory FIRST before any design task:

components.md — shared UI primitives with full source code
layouts.md — shared layout components (nav, sidebar, header, footer)
routes.md — page/route mapping
theme.md — design tokens, CSS variables, Tailwind config
pages.md — page component dependency trees (which files each page needs)
extractable-components.md — components that can be extracted as reusable DraftComponents

When designing for an existing page: First check pages.md for the page's complete dependency tree. Every file in that tree MUST be passed as --context-file. Then also add globals.css, tailwind.config, and design-system.md.

Superdesign CLI (MUST run before any command)

IMPORTANT: Before running ANY superdesign command, you MUST ensure the CLI is installed and logged in.

Follow these steps in order — do NOT skip any step:

Check if CLI is already installed:

superdesign --version

If the command succeeds (prints a version), skip installation and go to step 2.
If the command fails (not found), install the CLI:
npm install -g @superdesign/cli@latest


Check login status by running any command (e.g. superdesign --help). If you see an auth/login error, run:

superdesign login


Wait for login to complete successfully before proceeding.

Only after login succeeds, run your intended superdesign commands.

Never assume the user is already logged in. Always verify login first.

How it works

MUST MANDATORY Fetch fresh guidelines below:

https://raw.githubusercontent.com/superdesigndev/superdesign-skill/main/skills/superdesign/SUPERDESIGN.md


Action accordingly based on instruction in the SUPERDESIGN.md

Weekly Installs
4.0K
Repository
superdesigndev/…gn-skill
GitHub Stars
293
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykFail