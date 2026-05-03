---
title: cyrus-setup-gitlab
url: https://skills.sh/ceedaragents/cyrus/cyrus-setup-gitlab
---

# cyrus-setup-gitlab

skills/ceedaragents/cyrus/cyrus-setup-gitlab
cyrus-setup-gitlab
Installation
$ npx skills add https://github.com/ceedaragents/cyrus --skill cyrus-setup-gitlab
SKILL.md

CRITICAL: Never use Read, Edit, or Write tools on ~/.cyrus/.env or any file inside ~/.cyrus/. Use only Bash commands (grep, printf >>, etc.) to interact with env files — secrets must never be read into the conversation context.

Setup GitLab

Configures GitLab CLI and git so Cyrus can create branches, commits, and merge requests.

Step 1: Check Existing Configuration

Check if glab is already authenticated:

glab auth status 2>&1


If authenticated, check git config:

git config --global user.name
git config --global user.email


If both glab auth and git config are set, inform the user:

GitLab is already configured. Skipping this step.

Skip to completion.

Step 2: Authenticate GitLab CLI

If glab is not authenticated:

glab auth login


This opens an interactive browser flow. Let the user complete it.

For self-hosted GitLab instances, the user can specify the hostname:

glab auth login --hostname gitlab.example.com


After completion, verify:

glab auth status

Step 3: Configure Git Identity

If git user name or email are not set, ask the user for their preferred values:

What name should appear on commits made by Cyrus? (e.g., your name, or "Cyrus Bot")

What email should appear on commits? (e.g., your email, or a noreply address)

Then set them:

git config --global user.name "<name>"
git config --global user.email "<email>"

Step 4: Verify
glab auth status
git config --global user.name
git config --global user.email

Completion

✓ GitLab CLI authenticated ✓ Git identity configured: <name> <email>

Weekly Installs
66
Repository
ceedaragents/cyrus
GitHub Stars
564
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass