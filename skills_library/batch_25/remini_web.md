---
title: remini-web
url: https://skills.sh/baphomet480/claude-skills/remini-web
---

# remini-web

skills/baphomet480/claude-skills/remini-web
remini-web
Installation
$ npx skills add https://github.com/baphomet480/claude-skills --skill remini-web
SKILL.md
Remini Web

Use Remini Web with a human-in-the-loop browser automation flow that keeps account login and verification manual.

Quick Start
Run script help first:
python3 scripts/remini_apply.py --help

Install prerequisites if needed:
python3 -m pip install playwright
python3 -m playwright install chromium

Run a standard enhancement:
python3 scripts/remini_apply.py /path/to/photo.jpg


The script opens Chromium, reuses a local browser profile, attempts upload/start actions, and waits for the Remini download.

Core Workflow
Confirm the input is a local image (.jpg, .jpeg, .png, .webp, .heic, .heif).
Launch scripts/remini_apply.py with a persistent profile.
Log in manually in the browser if needed.
Let the script try auto-upload and auto-start.
Complete actions manually in-browser if UI labels differ.
Click Download in Remini and let the script capture/save the output.
Common Commands
# Standard run (visible browser)
python3 scripts/remini_apply.py ./input/portrait.jpg

# Save to explicit output path
python3 scripts/remini_apply.py ./input/portrait.jpg --output ./output/portrait-remini.png

# Disable action click automation if the UI text changed
python3 scripts/remini_apply.py ./input/portrait.jpg --no-auto-start

# Add a custom action label for one-off UI variants
python3 scripts/remini_apply.py ./input/portrait.jpg --action-label "Create"

# Batch from a shell loop (one process per image)
for img in ./batch/*.{jpg,jpeg,png}; do
  python3 scripts/remini_apply.py "$img" --downloads-dir ./output/downloads
done

Operational Rules
Keep login, MFA, and checkout actions manual.
Do not store passwords or one-time codes in files.
Prefer --no-auto-start when Remini changes button text or flow.
Increase --timeout for long-running jobs.
Load troubleshooting notes from references/workflow.md when upload/download capture fails.
Resources
scripts/remini_apply.py: Interactive Playwright helper for Remini Web.
references/workflow.md: UI matching strategy and troubleshooting.
Weekly Installs
12
Repository
baphomet480/cla…e-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn