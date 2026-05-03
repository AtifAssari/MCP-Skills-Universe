---
title: pdf
url: https://skills.sh/igorwarzocha/opencode-workflows/pdf
---

# pdf

skills/igorwarzocha/opencode-workflows/pdf
pdf
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill pdf
SKILL.md
🛠 High-Fidelity Creation

When generating polished reports:

Generate: Use Reportlab (programmatic) or Platypus (templated) as the primary engine.
Preview: Convert every page to PNG for inspection:
pdftoppm -png -r 150 document.pdf page
Inspect: Verify that charts, tables, and typography are sharp and well-aligned.
📋 Common Operations
1. Form Filling
Identify fillable fields using scripts/extract_form_field_info.py.
Reference: See references/forms.md for detailed instructions on filling PDF forms.
Populate fields programmatically and verify using the Render loop.
2. Manipulation (pypdf)
Merge: Use PdfWriter to combine multiple documents.
Split: Extract individual pages into new files.
Secure: Add passwords or watermarks using PdfWriter.encrypt().
Reference: See references/reference.md for advanced features and JS library alternatives.
3. Extraction (pdfplumber)
Extract text with layout preservation.
Extract complex tables directly into Pandas DataFrames for analysis.
💎 Quality Expectations
Legibility: Text must be readable at 100% zoom; avoid walls of dense text.
Polish: Maintain intentional visual design—consistent margins and color palettes.
Verification: Zero defects (black squares, clipped text) permitted in final output.
Weekly Installs
34
Repository
igorwarzocha/op…orkflows
GitHub Stars
111
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn