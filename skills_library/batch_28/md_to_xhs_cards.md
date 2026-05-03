---
title: md-to-xhs-cards
url: https://skills.sh/erafat/skills/md-to-xhs-cards
---

# md-to-xhs-cards

skills/erafat/skills/md-to-xhs-cards
md-to-xhs-cards
Installation
$ npx skills add https://github.com/erafat/skills --skill md-to-xhs-cards
SKILL.md
Markdown To Xiaohongshu Cards
Overview

Convert markdown content into a multi-image card set suitable for Xiaohongshu posting. Keep source ordering and formatting cues (headings, paragraphs, lists, quotes, code, dividers, images) without rewriting the content.

Quick Start
Resolve the markdown file path from the user request.
Run:
scripts/run_md_to_xhs_cards.sh /absolute/or/relative/path/to/file.md

Return output folder and generated card paths.

Default output folder: <markdown-dir>/<markdown-stem>-xhs-cards

Workflow
Validate input:
Confirm markdown file exists.
Confirm referenced images are local files when possible (![...](...) or Obsidian ![[...]]).
Execute deterministic rendering:
Run scripts/run_md_to_xhs_cards.sh.
Use --width and --height to match required aspect ratio.
Use --background, --text-color, and related flags for style adjustment.
Use --author (and optionally --title / --subtitle) for a dedicated cover card.
Verify output:
Ensure at least one NN-card.png exists.
Check manifest.json for count and filenames.
If images are missing, report placeholders and list unresolved image paths.
Optional publish to Xiaohongshu:
Add --publish-xhs to publish immediately after rendering.
Use --publish-title / --publish-desc overrides when needed.
For safe validation, run once with --publish-dry-run.
Report clearly:
Provide absolute output directory.
Provide absolute paths for all generated cards.
Call out any missing/remote image limitations.
Quality Rules
Keep direct conversion behavior: do not rewrite the article content unless user asks.
Keep markdown block order stable.
Preserve image placement where possible (markdown and Obsidian image embeds).
Prefer 3:4 cards for Xiaohongshu (1080x1440 or 1242x1660).
Common Commands

Default:

scripts/run_md_to_xhs_cards.sh content/post.md


Set explicit output directory:

scripts/run_md_to_xhs_cards.sh content/post.md --output-dir exports/xhs-cards


Use larger Xiaohongshu canvas:

scripts/run_md_to_xhs_cards.sh content/post.md --width 1242 --height 1660


Style tuning:

scripts/run_md_to_xhs_cards.sh content/post.md \
  --background "#f3f3f3" \
  --text-color "#141414" \
  --muted-color "#6f6f6f" \
  --line-height-scale 1.80


Render + publish in one command:

scripts/run_md_to_xhs_cards.sh content/post.md \
  --publish-xhs \
  --publish-title "医生的病历写给谁看" \
  --publish-desc "关于病历、医疗决策，与医生的身份危机"


Dry-run publish validation:

scripts/run_md_to_xhs_cards.sh content/post.md \
  --publish-xhs \
  --publish-dry-run

User Option Packs

Soft reading style:

scripts/run_md_to_xhs_cards.sh content/post.md \
  --background "#faf9f6" \
  --quote-bg "#f4f2eb" \
  --quote-border "#e8e3d7" \
  --quote-accent "#7a756a"


Cover + ending signature:

scripts/run_md_to_xhs_cards.sh content/post.md \
  --author "鹿不角" \
  --signature-text "-- 鹿不角"


Keep author on cover too:

scripts/run_md_to_xhs_cards.sh content/post.md \
  --author "鹿医生" \
  --cover-author


Cover with author:

scripts/run_md_to_xhs_cards.sh content/post.md --author "鹿医生"


Last-page signature (without cover author):

scripts/run_md_to_xhs_cards.sh content/post.md \
  --author "鹿不角" \
  --signature-text "-- 鹿不角"

Dependencies
scripts/run_md_to_xhs_cards.sh auto-selects a Python interpreter with Pillow.
If none found, install:
python3 -m pip install pillow

Optional publishing uses scripts/publish_xhs.py:
Local mode: python3 -m pip install xhs
API mode (--publish-api-mode): python3 -m pip install requests
Cookie lookup supports:
--publish-cookie
XHS_COOKIE environment variable
.env in current directory / skill directory
References
Rendering details and defaults: references/render-spec.md
Claude Compatibility

Use the same command workflow in Claude Code. This skill is CLI-driven and does not depend on Codex-only interaction primitives.

Weekly Installs
16
Repository
erafat/skills
GitHub Stars
12
First Seen
Feb 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketFail
SnykPass