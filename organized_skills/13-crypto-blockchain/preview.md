---
rating: ⭐⭐⭐
title: preview
url: https://skills.sh/anton-abyzov/specweave/preview
---

# preview

skills/anton-abyzov/specweave/preview
preview
Installation
$ npx skills add https://github.com/anton-abyzov/specweave --skill preview
SKILL.md
Documentation View Skill

Expert in launching and managing Docusaurus documentation server for SpecWeave projects.

What I Do

I help you view your SpecWeave living documentation with Docusaurus:

Key Features
Zero-config setup - Works in any SpecWeave project automatically
Internal & Public docs - Internal on port 3015, public on port 3016
Cached installation - Docusaurus cached in .specweave/cache/docs-site/ (gitignored)
Hot reload - Edit markdown, see changes instantly
Mermaid diagrams - Architecture diagrams render beautifully
Auto sidebar - Generated from folder structure
Bypasses private registries - Uses public npm to avoid Azure DevOps/corporate issues
How It Works

First run (~30 seconds):

Creates Docusaurus in .specweave/cache/docs-site/ (internal) or .specweave/cache/docs-site-public/ (public)
Installs dependencies from public npm registry
Configures to read from .specweave/docs/internal/ or .specweave/docs/public/

Subsequent runs (instant):

Uses cached installation
Starts server immediately
Available Commands
View Internal Documentation (Default)
/sw-docs:view


What it does:

Checks if .specweave/docs/internal/ exists
Runs pre-flight validation (auto-fixes common issues)
Sets up Docusaurus in cache (if first run)
Starts dev server on http://localhost:3015
Enables hot reload
View Public Documentation
/sw-docs:view --public


What it does:

Checks if .specweave/docs/public/ exists
Runs pre-flight validation (auto-fixes common issues)
Sets up Docusaurus in cache (if first run)
Starts dev server on http://localhost:3016
Enables hot reload
Build Static Site
/sw-docs:build


What it does:

Builds production-ready static site
Outputs to .specweave/cache/docs-site/build/
Ready for deployment to any static host
When to Use This Skill
Activate for:
"View my documentation"
"Preview my docs"
"Show me my docs in a browser"
"Launch Docusaurus"
"View my living documentation"
"Start docs server"
"I want to see my internal docs"
"View public docs"
Workflow
User: "I want to preview my docs"
You: "I'll launch the documentation view server."
     [Run: /sw-docs:view]

User: "Show me my public documentation"
You: "I'll launch the public documentation server."
     [Run: /sw-docs:view --public]

Port Reference
Docs Type	Port	Path
Internal (default)	3015	.specweave/docs/internal/
Public	3016	.specweave/docs/public/
Troubleshooting
Port 3015 or 3016 already in use
# For internal docs
lsof -i :3015 && kill -9 $(lsof -t -i :3015)

# For public docs
lsof -i :3016 && kill -9 $(lsof -t -i :3016)

Reinstall from scratch
# For internal docs
rm -rf .specweave/cache/docs-site
# Then run /sw-docs:view again

# For public docs
rm -rf .specweave/cache/docs-site-public
# Then run /sw-docs:view --public again

npm registry issues

The setup explicitly uses --registry=https://registry.npmjs.org to bypass private/corporate registry configurations.

See Also
/sw-docs:build - Build static site for deployment
/sw-docs:organize - Organize large folders with themed indexes
/sw-docs:health - Documentation health report
/sw-docs:validate - Validate documentation before viewing
Weekly Installs
18
Repository
anton-abyzov/specweave
GitHub Stars
134
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubWarn