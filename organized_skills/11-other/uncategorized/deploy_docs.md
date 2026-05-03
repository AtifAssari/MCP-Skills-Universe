---
rating: ⭐⭐⭐
title: deploy-docs
url: https://skills.sh/everyinc/compound-engineering-plugin/deploy-docs
---

# deploy-docs

skills/everyinc/compound-engineering-plugin/deploy-docs
deploy-docs
Installation
$ npx skills add https://github.com/everyinc/compound-engineering-plugin --skill deploy-docs
SKILL.md
Deploy Documentation Command

Validate the documentation site and prepare it for GitHub Pages deployment.

Step 1: Validate Documentation

Run these checks:

# Count components
echo "Agents: $(ls plugins/compound-engineering/agents/*.md | wc -l)"
echo "Skills: $(ls -d plugins/compound-engineering/skills/*/ 2>/dev/null | wc -l)"

# Validate JSON
cat .claude-plugin/marketplace.json | jq . > /dev/null && echo "✓ marketplace.json valid"
cat plugins/compound-engineering/.claude-plugin/plugin.json | jq . > /dev/null && echo "✓ plugin.json valid"

# Check all HTML files exist
for page in index agents commands skills mcp-servers changelog getting-started; do
  if [ -f "plugins/compound-engineering/docs/pages/${page}.html" ] || [ -f "plugins/compound-engineering/docs/${page}.html" ]; then
    echo "✓ ${page}.html exists"
  else
    echo "✗ ${page}.html MISSING"
  fi
done

Step 2: Check for Uncommitted Changes
git status --porcelain plugins/compound-engineering/docs/


If there are uncommitted changes, warn the user to commit first.

Step 3: Deployment Instructions

Since GitHub Pages deployment requires a workflow file with special permissions, provide these instructions:

First-time Setup
Create .github/workflows/deploy-docs.yml with the GitHub Pages workflow
Go to repository Settings > Pages
Set Source to "GitHub Actions"
Deploying

After merging to main, the docs will auto-deploy. Or:

Go to Actions tab
Select "Deploy Documentation to GitHub Pages"
Click "Run workflow"
Workflow File Content
name: Deploy Documentation to GitHub Pages

on:
  push:
    branches: [main]
    paths:
      - 'plugins/compound-engineering/docs/**'
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v4
      - uses: actions/upload-pages-artifact@v3
        with:
          path: 'plugins/compound-engineering/docs'
      - uses: actions/deploy-pages@v4

Step 4: Report Status

Provide a summary:

## Deployment Readiness

✓ All HTML pages present
✓ JSON files valid
✓ Component counts match

### Next Steps
- [ ] Commit any pending changes
- [ ] Push to main branch
- [ ] Verify GitHub Pages workflow exists
- [ ] Check deployment at https://everyinc.github.io/compound-engineering-plugin/

Weekly Installs
233
Repository
everyinc/compou…g-plugin
GitHub Stars
16.0K
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass