---
rating: ⭐⭐⭐
title: grafana-plugin-scaffolding
url: https://skills.sh/nodnarbnitram/claude-code-extensions/grafana-plugin-scaffolding
---

# grafana-plugin-scaffolding

skills/nodnarbnitram/claude-code-extensions/grafana-plugin-scaffolding
grafana-plugin-scaffolding
Installation
$ npx skills add https://github.com/nodnarbnitram/claude-code-extensions --skill grafana-plugin-scaffolding
SKILL.md
Grafana Plugin Scaffolding Skill

Automate Grafana plugin project creation using the official @grafana/create-plugin scaffolder. This skill handles project scaffolding, development environment setup, and initial configuration for all plugin types.

Supported Grafana Version: v12.x+ only

Instructions
Step 1: Verify Prerequisites

Before scaffolding, verify these tools are installed:

# Check Node.js (v18+ required)
node --version

# Check npm
npm --version

# Check Docker (optional, for local development)
docker --version


If prerequisites are missing, guide the user to install them:

Node.js: https://nodejs.org/
Docker Desktop: https://www.docker.com/products/docker-desktop/
Step 2: Scaffold the Plugin

Use the official @grafana/create-plugin tool:

# Interactive scaffolding (recommended)
npx @grafana/create-plugin@latest

# The tool will prompt for:
# - Plugin type (panel, datasource, app, scenesapp)
# - Organization name (e.g., "myorg")
# - Plugin name (e.g., "my-panel")
# - Include backend? (y/n)

Step 3: Navigate and Install Dependencies
# Navigate to the new plugin directory
cd <orgName>-<pluginName>-<pluginType>

# Install frontend dependencies
npm install

# Install backend dependencies (if backend plugin)
go mod tidy

Step 4: Start Development Environment

Option A: Docker with Hot-Reload (Recommended)

The scaffolder generates a docker-compose.yaml. For enhanced development with file watching, use the template from templates/docker-compose.yaml which includes Docker Compose develop features.

# Start Grafana with file watching (Docker Compose v2.22.0+)
docker compose watch

# Or standard start without watching
docker compose up -d

# Access Grafana at http://localhost:3000
# Login: admin / admin


With docker compose watch:

Frontend changes in dist/ sync automatically (no restart)
Backend binary changes (gpx_*) trigger container restart
No manual rebuild-restart cycle needed

Option B: Manual

# Build and watch frontend
npm run dev

# Build backend (if applicable)
mage -v

# Configure Grafana to load unsigned plugins
# Add to grafana.ini: plugins.allow_loading_unsigned_plugins = <plugin-id>

Step 5: Verify Plugin Installation
Open http://localhost:3000
Navigate to Administration > Plugins
Search for your plugin name
Verify it appears and can be added to dashboards
Plugin Type Workflows
Panel Plugin
npx @grafana/create-plugin@latest
# Select: panel
# Enter: organization name
# Enter: plugin name
# Backend: No (panels don't need backend)


Post-scaffolding:

Edit src/components/SimplePanel.tsx for visualization logic
Edit src/types.ts for panel options interface
Edit src/module.ts for option configuration
Data Source Plugin (Frontend Only)
npx @grafana/create-plugin@latest
# Select: datasource
# Enter: organization name
# Enter: plugin name
# Backend: No


Post-scaffolding:

Edit src/datasource.ts for query logic
Edit src/ConfigEditor.tsx for connection settings
Edit src/QueryEditor.tsx for query builder UI
Data Source Plugin (With Backend)
npx @grafana/create-plugin@latest
# Select: datasource
# Enter: organization name
# Enter: plugin name
# Backend: Yes


Post-scaffolding:

Edit pkg/plugin/datasource.go for Go query logic
Implement QueryData and CheckHealth methods
Build backend: mage -v
App Plugin
npx @grafana/create-plugin@latest
# Select: app
# Enter: organization name
# Enter: plugin name
# Backend: Optional


Post-scaffolding:

Edit src/pages/ for app pages
Update plugin.json includes for navigation
Add new pages as React components
Development Commands
# Frontend development (watch mode)
npm run dev

# Frontend production build
npm run build

# Backend build (Go plugins)
mage -v

# Run unit tests
npm test

# Run E2E tests (requires Grafana running)
npx playwright test

# Lint code
npm run lint

# Type check
npm run typecheck

E2E Testing

The @grafana/create-plugin scaffolder includes E2E testing setup with @grafana/plugin-e2e and Playwright.

# Install Playwright browsers
npx playwright install --with-deps chromium

# Start Grafana
docker compose up -d

# Run E2E tests
npx playwright test

# Run with UI mode (debugging)
npx playwright test --ui


See references/e2e-testing.md for comprehensive testing patterns, fixtures, and CI/CD setup.

Best Practices
Start Simple: Begin with minimal functionality, then iterate
Use Docker: Consistent environment across team members
Test Early: Run tests frequently during development
Type Safety: Leverage TypeScript for all frontend code
SDK Updates: Keep @grafana/data, @grafana/ui, @grafana/runtime versions aligned
Common Issues
Plugin Not Appearing
Check plugin.json has correct id field
Verify Docker volume mounts correctly
Ensure npm run dev completed without errors
Backend Plugin Errors
Run mage -v to rebuild Go code
Check plugin_start_linux_* or gpx_* binaries exist in dist/
Verify plugin.json has "backend": true
Development Server Issues
Clear browser cache
Restart Docker: docker compose down && docker compose up -d
Check Grafana logs: docker compose logs grafana
Delegation

For complex architectural decisions, plugin design patterns, or troubleshooting, delegate to the grafana-plugin-expert agent which has access to current SDK documentation via Context7.

Weekly Installs
51
Repository
nodnarbnitram/c…tensions
GitHub Stars
8
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass