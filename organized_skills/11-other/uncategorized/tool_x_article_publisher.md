---
rating: ⭐⭐
title: tool-x-article-publisher
url: https://skills.sh/heyvhuang/ship-faster/tool-x-article-publisher
---

# tool-x-article-publisher

skills/heyvhuang/ship-faster/tool-x-article-publisher
tool-x-article-publisher
Installation
$ npx skills add https://github.com/heyvhuang/ship-faster --skill tool-x-article-publisher
SKILL.md
X Article Publisher

Publish Markdown content into X (Twitter) Articles as a draft, preserving formatting via rich text paste and deterministic image insertion.

Hard Rules (Safety)
Never auto-publish (draft only; user publishes manually).
User must be logged in before automation starts.
First image = cover image (if any).
Prerequisites
Browser automation available (Playwright MCP or equivalent)
X account can access Articles (Premium / Premium Plus)
macOS recommended (clipboard helper uses Cocoa)
Python 3.9+ with:
pip install Pillow pyobjc-framework-Cocoa
Inputs / Outputs (Recommended)

Inputs (paths only):

article_md_path: Markdown file to publish
Optional: run_dir for artifacts (otherwise use /tmp/)

Outputs (recommended artifacts):

/tmp/x_article.json (parsed structure)
/tmp/x_article.html (HTML body for paste)
Optional: run_dir/evidence/x-article-draft.md (what was done + links)
Bundled Scripts

Installed path (typical):

~/.claude/skills/tool-x-article-publisher/scripts/parse_markdown.py
~/.claude/skills/tool-x-article-publisher/scripts/copy_to_clipboard.py
Runbook (Step-by-step)

Follow: references/runbook.md

Weekly Installs
47
Repository
heyvhuang/ship-faster
GitHub Stars
338
First Seen
Feb 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass