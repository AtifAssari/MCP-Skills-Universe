---
title: pdf
url: https://skills.sh/openai/skills/pdf
---

# pdf

skills/openai/skills/pdf
pdf
Installation
$ npx skills add https://github.com/openai/skills --skill pdf
Summary

PDF reading, creation, and validation with visual rendering and programmatic generation.

Render PDF pages to PNG for visual inspection of layout, spacing, and typography before delivery using Poppler (pdftoppm)
Generate PDFs programmatically with reportlab for reliable formatting; extract text and metadata with pdfplumber or pypdf
Enforce quality standards: no clipped text, overlapping elements, broken tables, or rendering artifacts; ASCII hyphens only, human-readable citations
Use tmp/pdfs/ for intermediate files and output/pdf/ for final artifacts; re-render after each update to verify alignment and legibility
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
Weekly Installs
1.6K
Repository
openai/skills
GitHub Stars
18.0K
First Seen
Today
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn