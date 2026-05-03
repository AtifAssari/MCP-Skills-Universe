---
title: document-converter-suite
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/document-converter-suite
---

# document-converter-suite

skills/dkyazzentwatwa/chatgpt-skills/document-converter-suite
document-converter-suite
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill document-converter-suite
SKILL.md
Document Converter Suite

Run best-effort extraction and rebuild workflows across common document formats. Preserve clean structure, not pixel-perfect layout.

Use This For
Converting between pdf, docx, pptx, xlsx, txt, csv, md, and html
Pulling tables or spreadsheet-style grids into editable outputs
Running utility PDF operations such as merge, split, rotate, watermark, or page extraction
Filling simple document or form-style templates
Workflow
Confirm the source format, target format, and whether editability or fidelity matters more.
Use scripts/convert.py for single documents and scripts/batch_convert.py for folders.
Use the bundled utility scripts when the user needs a focused PDF or table task:
scripts/pdf_toolkit.py
scripts/table_extractor.py
scripts/form_filler.py
Say explicitly when the output is best-effort and likely to lose layout, images, OCR text, or advanced formatting.
Guardrails
Do not promise visual fidelity.
Treat scanned PDFs as OCR problems, not conversion problems.
Raise safety caps gradually on large sheets or documents instead of processing everything blindly.
References
references/conversion_matrix.md for supported paths.
references/limitations.md for failure modes and tradeoffs.
Weekly Installs
289
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass