---
title: docx-processing-openai
url: https://skills.sh/lawvable/awesome-legal-skills/docx-processing-openai
---

# docx-processing-openai

skills/lawvable/awesome-legal-skills/docx-processing-openai
docx-processing-openai
Installation
$ npx skills add https://github.com/lawvable/awesome-legal-skills --skill docx-processing-openai
SKILL.md
DOCX Skill
When to use
Read or review DOCX content where layout matters (tables, diagrams, pagination).
Create or edit DOCX files with professional formatting.
Validate visual layout before delivery.
Workflow
Prefer visual review (layout, tables, diagrams).
If soffice and pdftoppm are available, convert DOCX -> PDF -> PNGs.
Or use scripts/render_docx.py (requires pdf2image and Poppler).
If these tools are missing, install them or ask the user to review rendered pages locally.
Use python-docx for edits and structured creation (headings, styles, tables, lists).
After each meaningful change, re-render and inspect the pages.
If visual review is not possible, extract text with python-docx as a fallback and call out layout risk.
Keep intermediate outputs organized and clean up after final approval.
Temp and output conventions
Use tmp/docs/ for intermediate files; delete when done.
Write final artifacts under output/doc/ when working in this repo.
Keep filenames stable and descriptive.
Dependencies (install if missing)

Prefer uv for dependency management.

Python packages:

uv pip install python-docx pdf2image


If uv is unavailable:

python3 -m pip install python-docx pdf2image


System tools (for rendering):

# macOS (Homebrew)
brew install libreoffice poppler

# Ubuntu/Debian
sudo apt-get install -y libreoffice poppler-utils


If installation isn't possible in this environment, tell the user which dependency is missing and how to install it locally.

Environment

No required environment variables.

Rendering commands

DOCX -> PDF:

soffice -env:UserInstallation=file:///tmp/lo_profile_$$ --headless --convert-to pdf --outdir $OUTDIR $INPUT_DOCX


PDF -> PNGs:

pdftoppm -png $OUTDIR/$BASENAME.pdf $OUTDIR/$BASENAME


Bundled helper:

python3 scripts/render_docx.py /path/to/file.docx --output_dir /tmp/docx_pages

Quality expectations
Deliver a client-ready document: consistent typography, spacing, margins, and clear hierarchy.
Avoid formatting defects: clipped/overlapping text, broken tables, unreadable characters, or default-template styling.
Charts, tables, and visuals must be legible in rendered pages with correct alignment.
Use ASCII hyphens only. Avoid U+2011 (non-breaking hyphen) and other Unicode dashes.
Citations and references must be human-readable; never leave tool tokens or placeholder strings.
Final checks
Re-render and inspect every page at 100% zoom before final delivery.
Fix any spacing, alignment, or pagination issues and repeat the render loop.
Confirm there are no leftovers (temp files, duplicate renders) unless the user asks to keep them.
Weekly Installs
40
Repository
lawvable/awesom…l-skills
GitHub Stars
308
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass