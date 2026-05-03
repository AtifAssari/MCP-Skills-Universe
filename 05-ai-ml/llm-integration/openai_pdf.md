---
title: openai-pdf
url: https://skills.sh/trailofbits/skills-curated/openai-pdf
---

# openai-pdf

skills/trailofbits/skills-curated/openai-pdf
openai-pdf
Installation
$ npx skills add https://github.com/trailofbits/skills-curated --skill openai-pdf
SKILL.md
PDF Skill
When to use
Read or review PDF content where layout and visuals matter.
Create PDFs programmatically with reliable formatting.
Validate final rendering before delivery.
Workflow
Prefer visual review: render PDF pages to PNGs and inspect them.
Use pdftoppm if available.
If unavailable, install Poppler or ask the user to review the output locally.
Use reportlab to generate PDFs when creating new documents.
Use pdfplumber (or pypdf) for text extraction and quick checks; do not rely on it for layout fidelity.
After each meaningful update, re-render pages and verify alignment, spacing, and legibility.
Temp and output conventions
Use tmp/pdfs/ for intermediate files; delete when done.
Write final artifacts under output/pdf/ when working in this repo.
Keep filenames stable and descriptive.
Dependencies (install if missing)

Prefer uv for dependency management.

Python packages:

uv pip install reportlab pdfplumber pypdf


If uv is unavailable:

python3 -m pip install reportlab pdfplumber pypdf


System tools (for rendering):

# macOS (Homebrew)
brew install poppler

# Ubuntu/Debian
sudo apt-get install -y poppler-utils


If installation isn't possible in this environment, tell the user which dependency is missing and how to install it locally.

Environment

No required environment variables.

Rendering command
pdftoppm -png $INPUT_PDF $OUTPUT_PREFIX

Quality expectations
Maintain polished visual design: consistent typography, spacing, margins, and section hierarchy.
Avoid rendering issues: clipped text, overlapping elements, broken tables, black squares, or unreadable glyphs.
Charts, tables, and images must be sharp, aligned, and clearly labeled.
Use ASCII hyphens only. Avoid U+2011 (non-breaking hyphen) and other Unicode dashes.
Citations and references must be human-readable; never leave tool tokens or placeholder strings.
Final checks
Do not deliver until the latest PNG inspection shows zero visual or formatting defects.
Confirm headers/footers, page numbering, and section transitions look polished.
Keep intermediate files organized or remove them after final approval.
When NOT to Use
Weekly Installs
31
Repository
trailofbits/ski…-curated
GitHub Stars
381
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass