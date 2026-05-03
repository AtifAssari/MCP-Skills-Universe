---
rating: ⭐⭐⭐
title: github-auth
url: https://skills.sh/jackspace/claudeskillz/github-auth
---

# github-auth

skills/jackspace/claudeskillz/github-auth
github-auth
Installation
$ npx skills add https://github.com/jackspace/claudeskillz --skill github-auth
SKILL.md
GitHub Authentication

This skill provides secure access to GitHub credentials for API operations, repository management, and git commands.

Instructions

When helping with GitHub operations that require authentication:

Credential Location

Credentials are stored in the project root .env file

Cross-platform path examples:

Linux/macOS: ~/apps/your_claude_skills/.env or use relative path: ./.env
Windows: %USERPROFILE%\apps\your_claude_skills\.env or relative: .\.env

Load credentials:

# Linux/macOS:
source ./.env

# Windows PowerShell:
# Get-Content .\.env | ForEach-Object { if ($_ -match '^([^=]+)=(.*)$') { [Environment]::SetEnvironmentVariable($matches[1], $matches[2]) } }


Access in scripts:

# Linux/macOS:
GITHUB_USERNAME=$(grep GITHUB_USERNAME ./.env | cut -d= -f2)
GITHUB_PAT=$(grep GITHUB_PAT ./.env | cut -d= -f2)

# Windows PowerShell:
# $GITHUB_USERNAME = (Get-Content .\.env | Select-String "GITHUB_USERNAME").Line.Split("=")[1]
# $GITHUB_PAT = (Get-Content .\.env | Select-String "GITHUB_PAT").Line.Split("=")[1]

GitHub API Operations

Use the GitHub CLI (gh) for authenticated operations:

# Authenticate gh with stored PAT
echo "$GITHUB_PAT" | gh auth login --with-token

# Or use API directly with curl
curl -H "Authorization: token $GITHUB_PAT" https://api.github.com/user/repos

Git Operations with Authentication

⚠️ SECURITY WARNING: Embedding credentials in URLs is a security risk. Use SSH keys or git credential helper instead.

RECOMMENDED: Use SSH Keys

# Setup SSH key for GitHub (one-time setup)
ssh-keygen -t ed25519 -C "your_email@example.com"
cat ~/.ssh/id_ed25519.pub  # Add this to GitHub Settings > SSH Keys

# Clone with SSH (RECOMMENDED)
git clone git@github.com:owner/repo.git

# Add SSH remote
git remote add origin git@github.com:owner/repo.git


ALTERNATIVE: Use Git Credential Helper

# Configure git credential helper (stores credentials securely)
git config --global credential.helper store

# First time will prompt for credentials, then stores them securely
git clone https://github.com/owner/repo.git


NOT RECOMMENDED: Credentials in URL (only for automation/CI)

# WARNING: Credentials in URLs can leak in logs/history
# Only use in secure, automated environments
git clone https://$GITHUB_USERNAME:$GITHUB_PAT@github.com/owner/repo.git

Common GitHub Operations

Create Repository

gh repo create owner/repo --private --description "Description"


List Repositories

gh repo list


Create Pull Request

gh pr create --title "Title" --body "Description"


Manage Issues

gh issue create --title "Issue" --body "Description"
gh issue list


Release Management

gh release create v1.0.0 --title "Release 1.0.0" --notes "Release notes"

Security Best Practices

Never Echo or Display PAT

Never use echo $GITHUB_PAT or display the token
Use it directly in commands or pipe to stdin
Keep .env file permissions restricted (chmod 600)

Use gh CLI When Possible

Prefer gh commands over raw API calls
gh stores credentials securely
Better error handling and user-friendly output

Never Put Credentials in Git URLs

Credentials in URLs can leak in git history, logs, and error messages
Use SSH keys or git credential helper instead
Only use URL credentials in secure CI/CD environments

Verify .env is Gitignored

Always check .gitignore includes .env
Never commit credentials to git
Use .env.example for documentation

Rotate Tokens Regularly

GitHub PATs should be rotated periodically
Revoke old tokens after rotation
Update .env file with new token
Error Handling

If authentication fails:

Verify PAT is valid in .env file
Check PAT has required scopes (repo, workflow, etc.)
Verify PAT hasn't expired
Test with: gh auth status
Examples
Example 1: Create and Push to New Repo
# Load credentials (Linux/macOS):
source ./.env

# Load credentials (Windows PowerShell):
# Get-Content .\.env | ForEach-Object { if ($_ -match '^([^=]+)=(.*)$') { [Environment]::SetEnvironmentVariable($matches[1], $matches[2]) } }

# Create private repository
gh repo create yourusername/my-new-repo --private --description "My new project"

# Initialize local repo and push
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/my-new-repo.git
git push -u origin main

Example 2: Clone Private Repo (SSH - RECOMMENDED)
# Clone with SSH (most secure)
git clone git@github.com:yourusername/private-repo.git

Example 2b: Clone with Credential Helper
# First time setup (one-time)
git config --global credential.helper store

# Clone - will prompt for credentials first time, then cache
git clone https://github.com/yourusername/private-repo.git

Example 3: API Request
# Load credentials (Linux/macOS):
source ./.env

# Load credentials (Windows PowerShell):
# Get-Content .\.env | ForEach-Object { if ($_ -match '^([^=]+)=(.*)$') { [Environment]::SetEnvironmentVariable($matches[1], $matches[2]) } }

# List user's repositories (Linux/macOS):
curl -s -H "Authorization: token $GITHUB_PAT" \
  https://api.github.com/user/repos | jq -r '.[].full_name'

# Windows PowerShell:
# $headers = @{ Authorization = "token $env:GITHUB_PAT" }
# (Invoke-RestMethod -Uri "https://api.github.com/user/repos" -Headers $headers).full_name

Notes
GitHub CLI (gh) is the recommended method for GitHub operations
The PAT should have appropriate scopes based on operations needed
Credentials file is protected by .gitignore
For CI/CD, use GitHub Actions secrets instead of .env file
Consider using SSH keys for git operations as an alternative to HTTPS with PAT
Weekly Installs
37
Repository
jackspace/claudeskillz
GitHub Stars
14
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass