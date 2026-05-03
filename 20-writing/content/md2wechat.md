---
title: md2wechat
url: https://skills.sh/lingengyuan/my-skills/md2wechat
---

# md2wechat

skills/lingengyuan/my-skills/md2wechat
md2wechat
Installation
$ npx skills add https://github.com/lingengyuan/my-skills --skill md2wechat
SKILL.md
MD to WeChat Skill (AI Only)

Convert Markdown to WeChat Official Account HTML with inline CSS (AI mode) and optionally upload to the draft box.

Quick Commands
# Render AI-style HTML (theme) from Markdown
python scripts/md_ai_render.py --md article.md --theme autumn-warm --out article.html

# Then publish
python scripts/wechat_publish.py --md article.md --html article.html --draft --cover cover.jpg

Workflow
Read the Markdown file and note title, images, and structure.
Pick AI theme (see references/themes.md).
Render themed HTML and save it to file.
If user wants one-click publish, upload images and create draft with the tool.
Render HTML
python scripts/md_ai_render.py --md article.md --theme autumn-warm --out article.html

Draft Upload (One-Click Publish)
python scripts/wechat_publish.py --md article.md --html article.html --draft --cover cover.jpg


Use the first image as cover if the user does not provide one.

Fetch WeChat-Sanitized HTML
python scripts/wechat_publish.py --md article.md --html article.html --draft --cover cover.jpg --fetch-draft article.wechat.html

Images
Local/remote images are uploaded to WeChat by the tool during publish.
For AI-generated images, insert ![alt](__generate:prompt__) in Markdown or ask in natural language.
For details, read references/image-syntax.md.
Standalone Image

AI image generation is handled by Claude; no separate tool call.

Configuration (Env File)

Assume the user has an env file (e.g. .env) configured with:

WECHAT_APPID
WECHAT_SECRET

Optional:

IMAGE_API_KEY (AI images)
IMAGE_API_BASE

The publish tool loads .env by default; override with --env. It also accepts AppID/AppSecret in the env file. Draft title defaults to the Markdown filename (without .md). Override with --title.

Examples
Example 1: Basic Conversion

Input (article.md):

# Hello World

This is a simple article.

- Item 1
- Item 2


Command:

python scripts/md_ai_render.py --md article.md --theme autumn-warm --out article.html


Output (article.html): WeChat-compatible HTML with inline CSS and autumn-warm theme styling.

Example 2: Publish to Draft

Input: article.md + article.html + cover.jpg

Command:

python scripts/wechat_publish.py --md article.md --html article.html --draft --cover cover.jpg


Output:

{"success": true, "image_count": 2, "draft_media_id": "xxx"}

References
references/themes.md (AI themes and prompts)
references/html-guide.md (WeChat HTML rules)
references/image-syntax.md (image syntax)
references/wechat-api.md (draft upload behavior)
Weekly Installs
9
Repository
lingengyuan/my-skills
GitHub Stars
8
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass