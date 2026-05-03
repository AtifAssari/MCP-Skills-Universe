---
title: webflow-code-component:deploy-guide
url: https://skills.sh/webflow/webflow-skills/webflow-code-component:deploy-guide
---

# webflow-code-component:deploy-guide

skills/webflow/webflow-skills/webflow-code-component:deploy-guide
webflow-code-component:deploy-guide
Installation
$ npx skills add https://github.com/webflow/webflow-skills --skill webflow-code-component:deploy-guide
SKILL.md
Deploy Guide

Guide users through deploying their code component library to Webflow.

When to Use This Skill

Use when:

User is ready to deploy components to Webflow
User asks how to share, publish, or deploy their library
First-time deployment to a workspace
Step-by-step deployment walkthrough needed

Do NOT use when:

Deployment failed (use troubleshoot-deploy instead)
Just validating before deploy (use pre-deploy-check instead)
Setting up local development (use local-dev-setup instead)

Note: The CLI command is webflow library share. This skill uses "deploy" as the user-facing term.

Instructions
Phase 1: Pre-Flight Checks

Verify project is ready:

Check webflow.json configuration
Ensure all dependencies installed
Run pre-deploy-check skill checks

Check authentication status:

Look for existing .env with API token
Verify WEBFLOW_WORKSPACE_API_TOKEN if set
Prepare for authentication if needed

Confirm deployment target:

Which workspace?
New library or update existing?
Phase 2: Authentication
Guide authentication:
Interactive: Follow CLI prompts
CI/CD: Use --api-token flag
Show how to get workspace API token if needed
Phase 3: Deployment
Execute deployment:
Run npx webflow library share
Monitor for errors
Capture output
Phase 4: Verification

Verify deployment:

Check Webflow Designer for components
Test component functionality
Confirm all components appear

Provide next steps:

How to use components in Designer
How to update in future
Common post-deploy tasks
If deployment fails, use troubleshoot-deploy to diagnose and fix issues
Deployment Workflow
Standard Deployment
📦 Deploying Code Components

Step 1: Pre-flight checks
├── webflow.json ✅
├── Dependencies ✅
└── Build test ✅

Step 2: Authentication
├── Checking for existing auth...
└── Found valid token ✅

Step 3: Deploying
├── Bundling components...
├── Uploading to workspace...
└── Processing...

Step 4: Verification
├── Library registered ✅
└── 4 components available ✅

🎉 Deployment Complete!

CI/CD Deployment
# Set environment variable
export WEBFLOW_WORKSPACE_API_TOKEN=your-token-here

# Deploy without prompts
npx webflow library share --no-input

Examples

User prompt:

Deploy my components to Webflow


Response:

🚀 Deploy Guide: Code Components

Let me guide you through deploying your component library.

---

## Step 1: Pre-Flight Checks

Running validation...

✅ webflow.json configured
✅ Dependencies installed
✅ Build succeeds
✅ Bundle size: 2.3MB (under 50MB limit)

All checks passed! Ready to deploy.

---

## Step 2: Authentication

**Option A: Interactive (Recommended for first time)**

Run the deploy command:
```bash
npx webflow library share


This will:

Open your browser for Webflow login
Ask you to authorize the app
Save credentials to .env

Option B: API Token (For CI/CD or returning users)

Get your Workspace API Token:

Go to Webflow Dashboard
Navigate to your Workspace Settings
Find "Apps & Integrations" → "Manage"
Under "Workspace API Access", click "Generate API Token"
Copy the token

Run with token:

npx webflow library share --api-token YOUR_TOKEN_HERE


Or set environment variable:

export WEBFLOW_WORKSPACE_API_TOKEN=YOUR_TOKEN_HERE
npx webflow library share

Step 3: Deploy

Ready to deploy? Run:

npx webflow library share


Expected output:

✓ Bundling components...
✓ Authenticating...
✓ Uploading library...
✓ Processing...

Library "My Component Library" successfully shared!

Components:
- Button
- Card
- Accordion
- Modal

View in Designer: Open any site in your workspace

Step 4: Verify in Designer

After deployment:

Open Webflow Designer for any site in your workspace
Open Add Panel (A key or + button)
Find "Components" section
Look for your library under custom components
Drag a component onto the canvas to test
Step 5: Next Steps

✅ Your components are live!

To update components later:

# Make your changes, then re-deploy
npx webflow library share


Important notes:

Updates replace the entire library (no partial updates)
Existing component instances will update automatically
Don't rename .webflow.tsx files (breaks instances)

💡 Tips:

Add .env to .gitignore to protect your token
Use --verbose flag for debugging issues
Run npx webflow library log to see recent deploy logs

---

**Example: First-Time Setup**



🚀 Deploy Guide: First-Time Setup

I see this is your first deployment. Let me walk you through the full setup.

Step 1: Get Workspace API Token

You'll need a Workspace API token to deploy:

Open Webflow Dashboard Go to webflow.com and log in

Navigate to Workspace Settings Click your workspace name → Settings

Find API Access Go to "Apps & Integrations" → "Manage"

Generate Token Under "Workspace API Access":

Click "Generate API Token"
Copy the token (you won't see it again!)

Save Token Add to your .env file:

WEBFLOW_WORKSPACE_API_TOKEN=your-token-here


⚠️ Add .env to .gitignore:

echo ".env" >> .gitignore

Step 2: Deploy

Now run:

npx webflow library share


The CLI will:

Read your token from .env
Bundle your components
Upload to your workspace
Step 3: Verify

After successful deploy:

Open Webflow Designer
Press 'A' to open Add panel
Find your components in the Components section
Drag onto canvas to test

🎉 First deployment complete!

Future deployments are simpler:

# Just run this after making changes
npx webflow library share


---

**Example: CI/CD Setup**



🚀 Deploy Guide: CI/CD Setup

Setting up automated deployments for your pipeline.

GitHub Actions Example

Create .github/workflows/deploy.yml:

name: Deploy to Webflow

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Deploy to Webflow
        env:
          WEBFLOW_WORKSPACE_API_TOKEN: ${{ secrets.WEBFLOW_WORKSPACE_API_TOKEN }}
        run: npx webflow library share --no-input

Add Secret to GitHub
Go to your repo → Settings → Secrets and variables → Actions
Click "New repository secret"
Name: WEBFLOW_WORKSPACE_API_TOKEN
Value: Your workspace API token
Click "Add secret"
Key Flags for CI/CD
npx webflow library share --no-input

--no-input: Disables interactive prompts
Uses WEBFLOW_WORKSPACE_API_TOKEN env var automatically
Optional: Add TypeScript Check
- name: Type check
  run: npx tsc --noEmit


✅ CI/CD configured!

Now every push to main will automatically deploy your components.


## Validation

After deployment, verify success with these checks:

| Check | How to Verify |
|-------|---------------|
| Deploy completed | `npx webflow library share` exited without errors |
| Components visible | Open Designer Add panel → find your library |
| Import logs clean | `npx webflow library log` shows successful import |
| Bundle size OK | Output shows bundle under 50MB |
| Props work | Drag component onto canvas, verify props in right panel |

## Guidelines

### Terminology

The CLI command is `webflow library share`. This skill uses "deploy" as the user-facing term for consistency with common developer vocabulary. See the [CLI reference](../../references/CODE_COMPONENTS_REFERENCE.md) (Section 12) for full command documentation.

### Authentication Methods

| Method | Use Case | Command |
|--------|----------|---------|
| Interactive | First time, local dev | `npx webflow library share` |
| Environment variable | CI/CD, automation | Set `WEBFLOW_WORKSPACE_API_TOKEN` |
| CLI flag | One-off with different token | `--api-token TOKEN` |

### Pre-Deploy Checklist

Before every deployment:

- [ ] `npm install` is up to date
- [ ] Build succeeds locally
- [ ] Bundle under 50MB
- [ ] All component tests pass
- [ ] No SSR-breaking code (or ssr: false set)
- [ ] Props have default values where supported (not available for Link, Image, Slot, ID)

### Common Deploy Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| "Authentication failed" | Invalid/expired token | Regenerate workspace token |
| "Bundle too large" | Over 50MB | Optimize dependencies |
| "Library not found" | Wrong workspace | Check token workspace |
| "Build failed" | Code errors | Fix compilation errors |

### CLI Flags Reference

All flags for `npx webflow library share`:

| Flag | Description | Default |
|------|-------------|---------|
| `--manifest` | Path to `webflow.json` file | Scans current directory |
| `--api-token` | Workspace API token | Uses `WEBFLOW_WORKSPACE_API_TOKEN` from `.env` |
| `--no-input` | Skip interactive prompts (for CI/CD) | No |
| `--verbose` | Display more debugging information | No |
| `--dev` | Bundle in development mode (no minification) | No |

### Rollback & Versioning

- Each `library share` replaces the **entire** library — there are no partial updates
- There is **no built-in rollback** — use git to revert changes and re-deploy
- **Never rename `.webflow.tsx` files** — renaming creates a new component and removes the old one, breaking all existing instances in projects

### Debugging Commands

```bash
# Check recent deploy logs
npx webflow library log

# Verbose deploy output (detailed errors)
npx webflow library share --verbose

# Local bundle verification (catches build errors before deploying)
npx webflow library bundle --public-path http://localhost:4000/

CI/CD Deployment

The GitHub Actions example above applies to any CI system. The key elements are:

# Generic CI pattern:
npm ci                                        # Install dependencies
npx webflow library share --no-input          # Deploy without prompts
# Requires WEBFLOW_WORKSPACE_API_TOKEN env var

Post-Deploy Verification

Always verify after deployment:

Check Designer: Components appear in Add panel
Test drag-and-drop: Component renders on canvas
Test props: Props editable in right panel
Test preview: Component works in preview mode
Test publish: Component works on published site
Weekly Installs
220
Repository
webflow/webflow-skills
GitHub Stars
64
First Seen
Mar 11, 2026