---
title: baoyu-danger-x-to-markdown
url: https://skills.sh/jimliu/baoyu-skills/baoyu-danger-x-to-markdown
---

# baoyu-danger-x-to-markdown

skills/jimliu/baoyu-skills/baoyu-danger-x-to-markdown
baoyu-danger-x-to-markdown
Installation
$ npx skills add https://github.com/jimliu/baoyu-skills --skill baoyu-danger-x-to-markdown
Summary

Convert X tweets and articles to markdown with YAML front matter using reverse-engineered API.

Extracts tweets, threads, and X articles to markdown with metadata (author, URL, cover image, thread count)
Requires explicit user consent before first use; displays disclaimer about reverse-engineered API and potential account risks
Supports media download to local imgs/ and videos/ directories with automatic link rewriting, configurable per-conversion or via preferences
Authenticates via environment variables (X_AUTH_TOKEN, X_CT0) or Chrome login with cached cookies; includes --login flag to refresh credentials
SKILL.md
X to Markdown

Converts X content to markdown:

Tweets/threads → Markdown with YAML front matter
X Articles → Full content extraction
User Input Tools

When this skill prompts the user, follow this tool-selection rule (priority order):

Prefer built-in user-input tools exposed by the current agent runtime — e.g., AskUserQuestion, request_user_input, clarify, ask_user, or any equivalent.
Fallback: if no such tool exists, emit a numbered plain-text message and ask the user to reply with the chosen number/answer for each question.
Batching: if the tool supports multiple questions per call, combine all applicable questions into a single call; if only single-question, ask them one at a time in priority order.

Concrete AskUserQuestion references below are examples — substitute the local equivalent in other runtimes.

Script Directory

Scripts located in scripts/ subdirectory.

Path Resolution:

{baseDir} = this SKILL.md's directory
Script path = {baseDir}/scripts/main.ts
Resolve ${BUN_X} runtime: if bun installed → bun; if npx available → npx -y bun; else suggest installing bun
Consent Requirement

Before any conversion, check and obtain consent.

Consent Flow

Step 1: Check consent file

# macOS
cat ~/Library/Application\ Support/baoyu-skills/x-to-markdown/consent.json

# Linux
cat ~/.local/share/baoyu-skills/x-to-markdown/consent.json


Step 2: If accepted: true and disclaimerVersion: "1.0" → print warning and proceed:

Warning: Using reverse-engineered X API. Accepted on: <acceptedAt>


Step 3: If missing or version mismatch → display disclaimer:

DISCLAIMER

This tool uses a reverse-engineered X API, NOT official.

Risks:
- May break if X changes API
- No guarantees or support
- Possible account restrictions
- Use at your own risk

Accept terms and continue?


Use AskUserQuestion with options: "Yes, I accept" | "No, I decline"

Step 4: On accept → create consent file:

{
  "version": 1,
  "accepted": true,
  "acceptedAt": "<ISO timestamp>",
  "disclaimerVersion": "1.0"
}


Step 5: On decline → output "User declined. Exiting." and stop.

Preferences (EXTEND.md)

Check EXTEND.md in priority order — the first one found wins:

Priority	Path	Scope
1	.baoyu-skills/baoyu-danger-x-to-markdown/EXTEND.md	Project
2	${XDG_CONFIG_HOME:-$HOME/.config}/baoyu-skills/baoyu-danger-x-to-markdown/EXTEND.md	XDG
3	$HOME/.baoyu-skills/baoyu-danger-x-to-markdown/EXTEND.md	User home
Result	Action
Found	Read, parse, apply settings
Not found	MUST run first-time setup (see below) — do NOT silently create defaults

EXTEND.md supports: Download media by default, default output directory.

First-Time Setup (BLOCKING)

CRITICAL: When EXTEND.md is not found, you MUST use AskUserQuestion to ask the user for their preferences before creating EXTEND.md. NEVER create EXTEND.md with defaults without asking. This is a BLOCKING operation — do NOT proceed with any conversion until setup is complete.

Use AskUserQuestion with ALL questions in ONE call:

Question 1 — header: "Media", question: "How to handle images and videos in tweets?"

"Ask each time (Recommended)" — After saving markdown, ask whether to download media
"Always download" — Always download media to local imgs/ and videos/ directories
"Never download" — Keep original remote URLs in markdown

Question 2 — header: "Output", question: "Default output directory?"

"x-to-markdown (Recommended)" — Save to ./x-to-markdown/{username}/{tweet-id}.md
(User may choose "Other" to type a custom path)

Question 3 — header: "Save", question: "Where to save preferences?"

"User (Recommended)" — ~/.baoyu-skills/ (all projects)
"Project" — .baoyu-skills/ (this project only)

After user answers, create EXTEND.md at the chosen location, confirm "Preferences saved to [path]", then continue.

Full reference: references/config/first-time-setup.md

Supported Keys
Key	Default	Values	Description
download_media	ask	ask / 1 / 0	ask = prompt each time, 1 = always download, 0 = never
default_output_dir	empty	path or empty	Default output directory (empty = ./x-to-markdown/)

Value priority:

CLI arguments (--download-media, -o)
EXTEND.md
Skill defaults
Usage
${BUN_X} {baseDir}/scripts/main.ts <url>
${BUN_X} {baseDir}/scripts/main.ts <url> -o output.md
${BUN_X} {baseDir}/scripts/main.ts <url> --download-media
${BUN_X} {baseDir}/scripts/main.ts <url> --json

Options
Option	Description
<url>	Tweet or article URL
-o <path>	Output path
--json	JSON output
--download-media	Download image/video assets to local imgs/ and videos/, and rewrite markdown links to local relative paths
--login	Refresh cookies only
Supported URLs
https://x.com/<user>/status/<id>
https://twitter.com/<user>/status/<id>
https://x.com/i/article/<id>
Output
---
url: "https://x.com/user/status/123"
author: "Name (@user)"
tweetCount: 3
coverImage: "https://pbs.twimg.com/media/example.jpg"
---

Content...


File structure: x-to-markdown/{username}/{tweet-id}/{content-slug}.md

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
Authentication
Environment variables (preferred): X_AUTH_TOKEN, X_CT0
Chrome login (fallback): Auto-opens Chrome, caches cookies locally
Extension Support

Custom configurations via EXTEND.md. See Preferences section for paths and supported options.

Weekly Installs
16.9K
Repository
jimliu/baoyu-skills
GitHub Stars
16.9K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn