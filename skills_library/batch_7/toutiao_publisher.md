---
title: toutiao-publisher
url: https://skills.sh/guanyang/super-publisher/toutiao-publisher
---

# toutiao-publisher

skills/guanyang/super-publisher/toutiao-publisher
toutiao-publisher
Installation
$ npx skills add https://github.com/guanyang/super-publisher --skill toutiao-publisher
Summary

Publish articles to Toutiao with persistent login and browser-based publishing.

One-time QR code login with automatic session persistence; subsequent publishes use saved credentials without re-authentication
Interactive publishing mode opens authenticated browser directly to the publish page, or fully automated mode via command-line arguments (title, content file, cover image)
Automatic title optimization to meet Toutiao's 2–30 character requirement; truncates or pads as needed
Session management commands to check authentication status or clear stored credentials
Uses patchright with stealth features for bot detection avoidance
SKILL.md
Toutiao Publisher Skill

Manage Toutiao (Today's Headlines) account, maintain persistent login session, and publish articles.

When to Use This Skill

Trigger when user:

Asks to publish to Toutiao/Today's Headlines
Wants to manage Toutiao login
Mentions "toutiao" or "头条号"
Core Workflow
Step 1: Authentication (One-Time Setup)

The skill requires a one-time login. The session is persisted for subsequent uses.

# Browser will open for manual login (scan QR code)
python scripts/run.py auth_manager.py setup


Instructions:

Run the setup command.
A browser window will open loading the Toutiao login page.
Log in manually (e.g., scan QR code).
Once logged in (redirected to dashboard), the script will save the session and close.
Step 2: Publish Article
# Opens browser with authenticated session at publish page
python scripts/run.py publisher.py


Instructions:

Run the publisher command.
Browser opens directly to the "Publish Article" page.
Write and publish the article manually.
Press Ctrl+C in the terminal when done.

Note: Toutiao requires titles to be 2-30 characters. This tool automatically optimizes titles to fit this constraint (truncating if >30, padding if <2).

Advanced Usage (Automated)

You can fully automate the publishing process by providing arguments:

# Publish with title, content file, and cover image
python scripts/run.py publisher.py --title "AI Trends 2025" --content "article.md" --cover "assets/cover.jpg" --headless

Management
# Check authentication status
python scripts/run.py auth_manager.py status

# Clear authentication data (logout)
python scripts/run.py auth_manager.py clear

Technical Details
Persistent Auth: Uses patchright to launch a persistent browser context. Cookies and storage state are saved to data/browser_state/state.json.
Anti-Detection: Uses patchright's stealth features to avoid bot detection.
Environment: Automatically manages a virtual environment (.venv) with required dependencies.
Script Reference
scripts/auth_manager.py: Handles login, session validation, and state persistence.
scripts/publisher.py: Launches authenticated browser for publishing.
scripts/run.py: Wrapper ensuring execution in the correct virtual environment.
Weekly Installs
733
Repository
guanyang/super-publisher
GitHub Stars
17
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn