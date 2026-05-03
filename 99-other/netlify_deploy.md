---
rating: ⭐⭐⭐
title: netlify-deploy
url: https://skills.sh/openai/skills/netlify-deploy
---

# netlify-deploy

skills/openai/skills/netlify-deploy
netlify-deploy
Installation
$ npx skills add https://github.com/openai/skills --skill netlify-deploy
Summary

Deploy web projects to Netlify with automatic authentication, site linking, and framework detection.

Handles full deployment workflow: authentication verification, site linking or creation, dependency installation, and preview or production deploys
Supports both browser-based OAuth and API token authentication; guides users through login if needed
Automatically detects project configuration from netlify.toml or prompts for build command and publish directory based on framework
Includes error handling for common issues (authentication failures, missing site links, build errors) and escalated network access for sandbox environments
SKILL.md
Netlify Deployment Skill

Deploy web projects to Netlify using the Netlify CLI with intelligent detection of project configuration and deployment context.

Overview

This skill automates Netlify deployments by:

Verifying Netlify CLI authentication
Detecting project configuration and framework
Linking to existing sites or creating new ones
Deploying to production or preview environments
Prerequisites
Netlify CLI: Installed via npx (no global install required)
Authentication: Netlify account with active login session
Project: Valid web project in current directory
When sandboxing blocks the deployment network calls, rerun with sandbox_permissions=require_escalated.
The deployment might take a few minutes. Use appropriate timeout values.
Authentication Pattern

The skill uses the pre-authenticated Netlify CLI approach:

Check authentication status with npx netlify status
If not authenticated, guide user through npx netlify login
Fail gracefully if authentication cannot be established

Authentication uses either:

Browser-based OAuth (primary): netlify login opens browser for authentication
API Key (alternative): Set NETLIFY_AUTH_TOKEN environment variable
Workflow
1. Verify Netlify CLI Authentication

Check if the user is logged into Netlify:

npx netlify status


Expected output patterns:

✅ Authenticated: Shows logged-in user email and site link status
❌ Not authenticated: "Not logged into any site" or authentication error

If not authenticated, guide the user:

npx netlify login


This opens a browser window for OAuth authentication. Wait for user to complete login, then verify with netlify status again.

Alternative: API Key authentication

If browser authentication isn't available, users can set:

export NETLIFY_AUTH_TOKEN=your_token_here


Tokens can be generated at: https://app.netlify.com/user/applications#personal-access-tokens

2. Detect Site Link Status

From netlify status output, determine:

Linked: Site already connected to Netlify (shows site name/URL)
Not linked: Need to link or create site
3. Link to Existing Site or Create New

If already linked → Skip to step 4

If not linked, attempt to link by Git remote:

# Check if project is Git-based
git remote show origin

# If Git-based, extract remote URL
# Format: https://github.com/username/repo or git@github.com:username/repo.git

# Try to link by Git remote
npx netlify link --git-remote-url <REMOTE_URL>


If link fails (site doesn't exist on Netlify):

# Create new site interactively
npx netlify init


This guides user through:

Choosing team/account
Setting site name
Configuring build settings
Creating netlify.toml if needed
4. Verify Dependencies

Before deploying, ensure project dependencies are installed:

# For npm projects
npm install

# For other package managers, detect and use appropriate command
# yarn install, pnpm install, etc.

5. Deploy to Netlify

Choose deployment type based on context:

Preview/Draft Deploy (default for existing sites):

npx netlify deploy


This creates a deploy preview with a unique URL for testing.

Production Deploy (for new sites or explicit production deployments):

npx netlify deploy --prod


This deploys to the live production URL.

Deployment process:

CLI detects build settings (from netlify.toml or prompts user)
Builds the project locally
Uploads built assets to Netlify
Returns deployment URL
6. Report Results

After deployment, report to user:

Deploy URL: Unique URL for this deployment
Site URL: Production URL (if production deploy)
Deploy logs: Link to Netlify dashboard for logs
Next steps: Suggest netlify open to view site or dashboard
Handling netlify.toml

If a netlify.toml file exists, the CLI uses it automatically. If not, the CLI will prompt for:

Build command: e.g., npm run build, next build
Publish directory: e.g., dist, build, .next

Common framework defaults:

Next.js: build command npm run build, publish .next
React (Vite): build command npm run build, publish dist
Static HTML: no build command, publish current directory

The skill should detect framework from package.json if possible and suggest appropriate settings.

Example Full Workflow
# 1. Check authentication
npx netlify status

# If not authenticated:
npx netlify login

# 2. Link site (if needed)
# Try Git-based linking first
git remote show origin
npx netlify link --git-remote-url https://github.com/user/repo

# If no site exists, create new one:
npx netlify init

# 3. Install dependencies
npm install

# 4. Deploy (preview for testing)
npx netlify deploy

# 5. Deploy to production (when ready)
npx netlify deploy --prod

Error Handling

Common issues and solutions:

"Not logged in" → Run npx netlify login

"No site linked" → Run npx netlify link or npx netlify init

"Build failed" → Check build command and publish directory in netlify.toml or CLI prompts → Verify dependencies are installed → Review build logs for specific errors

"Publish directory not found" → Verify build command ran successfully → Check publish directory path is correct

Troubleshooting
Escalated Network Access

If deployment fails due to network issues (timeouts, DNS errors, connection resets), rerun the deploy with escalated permissions (use sandbox_permissions=require_escalated). The deploy requires escalated network access when sandbox networking blocks outbound requests.

Example guidance to the user:

The deploy needs escalated network access to deploy to Netlify. I can rerun the command with escalated permissions—want me to proceed?

Environment Variables

For secrets and configuration:

Never commit secrets to Git
Set in Netlify dashboard: Site Settings → Environment Variables
Access in builds via process.env.VARIABLE_NAME
Tips
Use netlify deploy (no --prod) first to test before production
Run netlify open to view site in Netlify dashboard
Run netlify logs to view function logs (if using Netlify Functions)
Use netlify dev for local development with Netlify Functions
Reference
Netlify CLI Docs: https://docs.netlify.com/cli/get-started/
netlify.toml Reference: https://docs.netlify.com/configure-builds/file-based-configuration/
Bundled References (Load As Needed)
CLI commands
Deployment patterns
netlify.toml guide
Weekly Installs
1.0K
Repository
openai/skills
GitHub Stars
18.0K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass