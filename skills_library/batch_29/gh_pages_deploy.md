---
title: gh-pages-deploy
url: https://skills.sh/aviz85/claude-skills-library/gh-pages-deploy
---

# gh-pages-deploy

skills/aviz85/claude-skills-library/gh-pages-deploy
gh-pages-deploy
Installation
$ npx skills add https://github.com/aviz85/claude-skills-library --skill gh-pages-deploy
SKILL.md
GitHub Pages Deployment

Deploy static frontend websites to GitHub Pages using the GitHub CLI.

Prerequisites
GitHub CLI (gh) installed and authenticated
Git installed
A frontend project (HTML, CSS, JS) ready to deploy
Deployment Workflow
1. Initialize Git Repository (if needed)
git init
git add .
git commit -m "Initial commit"

2. Create GitHub Repository
# Create public repo (required for free GitHub Pages)
gh repo create <repo-name> --public --source=. --push

3. Enable GitHub Pages
# Enable GitHub Pages from main branch root
gh api repos/{owner}/{repo}/pages -X POST -f build_type=legacy -f source='{"branch":"main","path":"/"}'


Or for docs folder:

gh api repos/{owner}/{repo}/pages -X POST -f build_type=legacy -f source='{"branch":"main","path":"/docs"}'

4. Check Deployment Status
# Get pages info
gh api repos/{owner}/{repo}/pages

# View deployment status
gh api repos/{owner}/{repo}/pages/builds/latest

5. Set Homepage URL in Repo Settings

Always do this — sets the live URL in the GitHub repo's About panel (top-right on the repo page):

OWNER=$(gh api user --jq '.login')
PAGES_URL=$(gh api repos/$OWNER/$REPO_NAME/pages --jq '.html_url')
gh api --method PATCH repos/$OWNER/$REPO_NAME --field homepage="$PAGES_URL" --jq '.homepage'

6. Get Site URL

The site will be available at: https://<username>.github.io/<repo-name>/

Auto-deploy is active: every push to main triggers a rebuild. No GitHub Actions needed for legacy build.

Quick Deploy Script

For a complete deployment in one flow:

# Variables
REPO_NAME="my-site"

# Initialize and commit
git init
git add .
git commit -m "Initial commit"

# Create repo and push
gh repo create $REPO_NAME --public --source=. --push

# Enable pages
sleep 2
OWNER=$(gh api user --jq '.login')
gh api repos/$OWNER/$REPO_NAME/pages -X POST -f build_type=legacy -f source='{"branch":"main","path":"/"}'

# Set homepage URL in repo About panel
PAGES_URL="https://$OWNER.github.io/$REPO_NAME/"
gh api --method PATCH repos/$OWNER/$REPO_NAME --field homepage="$PAGES_URL" --jq '.homepage'

echo "✓ Site live at: $PAGES_URL"

Troubleshooting
Pages not enabled: Ensure repo is public or you have GitHub Pro
404 error: Wait 1-2 minutes for deployment, check if index.html exists at root
Build failed: Check GitHub Actions tab for errors
Updating the Site

After making changes:

git add .
git commit -m "Update site"
git push


GitHub Pages will automatically rebuild.

Weekly Installs
236
Repository
aviz85/claude-s…-library
GitHub Stars
27
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass