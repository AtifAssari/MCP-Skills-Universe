---
title: tuzi-url-to-markdown
url: https://skills.sh/tuziapi/tuzi-skills/tuzi-url-to-markdown
---

# tuzi-url-to-markdown

skills/tuziapi/tuzi-skills/tuzi-url-to-markdown
tuzi-url-to-markdown
Installation
$ npx skills add https://github.com/tuziapi/tuzi-skills --skill tuzi-url-to-markdown
SKILL.md
URL to Markdown

Fetches any URL via Chrome CDP and converts HTML to clean markdown.

Script Directory

Important: All scripts are located in the scripts/ subdirectory of this skill.

Agent Execution Instructions:

Determine this SKILL.md file's directory path as SKILL_DIR
Script path = ${SKILL_DIR}/scripts/<script-name>.ts
Replace all ${SKILL_DIR} in this document with the actual path

Script Reference:

Script	Purpose
scripts/main.ts	CLI entry point for URL fetching
Preferences (EXTEND.md)

Use Bash to check EXTEND.md existence (priority order):

# Check project-level first
test -f .tuzi-skills/tuzi-url-to-markdown/EXTEND.md && echo "project"

# Then user-level (cross-platform: $HOME works on macOS/Linux/WSL)
test -f "$HOME/.tuzi-skills/tuzi-url-to-markdown/EXTEND.md" && echo "user"


┌────────────────────────────────────────────────────────┬───────────────────┐ │ Path │ Location │ ├────────────────────────────────────────────────────────┼───────────────────┤ │ .tuzi-skills/tuzi-url-to-markdown/EXTEND.md │ Project directory │ ├────────────────────────────────────────────────────────┼───────────────────┤ │ $HOME/.tuzi-skills/tuzi-url-to-markdown/EXTEND.md │ User home │ └────────────────────────────────────────────────────────┴───────────────────┘

┌───────────┬───────────────────────────────────────────────────────────────────────────┐ │ Result │ Action │ ├───────────┼───────────────────────────────────────────────────────────────────────────┤ │ Found │ Read, parse, apply settings │ ├───────────┼───────────────────────────────────────────────────────────────────────────┤ │ Not found │ MUST run first-time setup (see below) — do NOT silently create defaults │ └───────────┴───────────────────────────────────────────────────────────────────────────┘

EXTEND.md Supports: Download media by default | Default output directory | Default capture mode | Timeout settings

First-Time Setup (BLOCKING)

CRITICAL: When EXTEND.md is not found, you MUST use AskUserQuestion to ask the user for their preferences before creating EXTEND.md. NEVER create EXTEND.md with defaults without asking. This is a BLOCKING operation — do NOT proceed with any conversion until setup is complete.

Use AskUserQuestion with ALL questions in ONE call:

Question 1 — header: "Media", question: "How to handle images and videos in pages?"

"Ask each time (Recommended)" — After saving markdown, ask whether to download media
"Always download" — Always download media to local imgs/ and videos/ directories
"Never download" — Keep original remote URLs in markdown

Question 2 — header: "Output", question: "Default output directory?"

"url-to-markdown (Recommended)" — Save to ./url-to-markdown/{domain}/{slug}.md
(User may choose "Other" to type a custom path)

Question 3 — header: "Save", question: "Where to save preferences?"

"User (Recommended)" — ~/.tuzi-skills/ (all projects)
"Project" — .tuzi-skills/ (this project only)

After user answers, create EXTEND.md at the chosen location, confirm "Preferences saved to [path]", then continue.

Full reference: references/config/first-time-setup.md

Supported Keys
Key	Default	Values	Description
download_media	ask	ask / 1 / 0	ask = prompt each time, 1 = always download, 0 = never
default_output_dir	empty	path or empty	Default output directory (empty = ./url-to-markdown/)

Value priority:

CLI arguments (--download-media, -o)
EXTEND.md
Skill defaults
Features
Chrome CDP for full JavaScript rendering
Two capture modes: auto or wait-for-user
Clean markdown output with metadata
Handles login-required pages via wait mode
Download images and videos to local directories
Usage
# Auto mode (default) - capture when page loads
npx -y bun ${SKILL_DIR}/scripts/main.ts <url>

# Wait mode - wait for user signal before capture
npx -y bun ${SKILL_DIR}/scripts/main.ts <url> --wait

# Save to specific file
npx -y bun ${SKILL_DIR}/scripts/main.ts <url> -o output.md

# Download images and videos to local directories
npx -y bun ${SKILL_DIR}/scripts/main.ts <url> --download-media

Options
Option	Description
<url>	URL to fetch
-o <path>	Output file path (default: auto-generated)
--wait	Wait for user signal before capturing
--timeout <ms>	Page load timeout (default: 30000)
--download-media	Download image/video assets to local imgs/ and videos/, and rewrite markdown links to local relative paths
Capture Modes
Mode	Behavior	Use When
Auto (default)	Capture on network idle	Public pages, static content
Wait (--wait)	User signals when ready	Login-required, lazy loading, paywalls

Wait mode workflow:

Run with --wait → script outputs "Press Enter when ready"
Ask user to confirm page is ready
Send newline to stdin to trigger capture
Output Format

YAML front matter with url, title, description, author, published, captured_at fields, followed by converted markdown content.

Output Directory
url-to-markdown/<domain>/<slug>.md

<slug>: From page title or URL path (kebab-case, 2-6 words)
Conflict resolution: Append timestamp <slug>-YYYYMMDD-HHMMSS.md

When --download-media is enabled:

Images are saved to imgs/ next to the markdown file
Videos are saved to videos/ next to the markdown file
Markdown media links are rewritten to local relative paths
Media Download Workflow

Based on download_media setting in EXTEND.md:

Setting	Behavior
1 (always)	Run script with --download-media flag
0 (never)	Run script without --download-media flag
ask (default)	Follow the ask-each-time flow below
Ask-Each-Time Flow
Run script without --download-media → markdown saved
Check saved markdown for remote media URLs (https:// in image/video links)
If no remote media found → done, no prompt needed
If remote media found → use AskUserQuestion:
header: "Media", question: "Download N images/videos to local files?"
"Yes" — Download to local directories
"No" — Keep remote URLs
If user confirms → run script again with --download-media (overwrites markdown with localized links)
Environment Variables
Variable	Description
URL_CHROME_PATH	Custom Chrome executable path
URL_DATA_DIR	Custom data directory
URL_CHROME_PROFILE_DIR	Custom Chrome profile directory

Troubleshooting: Chrome not found → set URL_CHROME_PATH. Timeout → increase --timeout. Complex pages → try --wait mode.

Extension Support

Custom configurations via EXTEND.md. See Preferences section for paths and supported options.

Weekly Installs
121
Repository
tuziapi/tuzi-skills
GitHub Stars
33
First Seen
Mar 5, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn