---
title: pdf-word-reader-zh
url: https://skills.sh/20041002liu-cloud/pdf-word-reader-zh/pdf-word-reader-zh
---

# pdf-word-reader-zh

skills/20041002liu-cloud/pdf-word-reader-zh/pdf-word-reader-zh
pdf-word-reader-zh
Installation
$ npx skills add https://github.com/20041002liu-cloud/pdf-word-reader-zh --skill pdf-word-reader-zh
SKILL.md
PDF Word Reader ZH
Purpose

Turn a document path into three analysis artifacts:

structured extraction
chunked evidence index
understanding report scaffold

Use this skill when output quality requires traceable evidence, not only a short summary.

Input Support
.pdf
.docx
.pptx (convert to PDF first)

For .doc, convert to .docx before using this skill.

One-Command Execution
python scripts/prepare_document_context.py "<input-file>" --output-dir "output/document-understanding"

Decision Flow
Detect input type by extension.
If .pptx, convert to PDF:
Prefer soffice when available.
Fallback to Microsoft PowerPoint COM on Windows.
Extract content:
PDF: page text + table extraction; use OCR fallback for low-text pages.
DOCX: paragraphs + table extraction.
Normalize and chunk long text into stable chunk IDs (C001, C002, ...).
Generate understanding scaffold with evidence index.
Output Contract

Write the following files to output directory:

01_extracted.json
02_chunks.json
03_understanding_report.md
01_extracted.json

Must include:

source_file
file_type
full_text
structure fields (pages or paragraphs/tables)
warnings and runtime metadata when available
02_chunks.json

Must include:

chunk_count
chunks[] with fields:
chunk_id
char_count
estimated_tokens
text
03_understanding_report.md

Must include:

document profile
key lines
chunk evidence index
deliverable template for final analysis
Recommended Parameters
--disable-ocr: disable OCR fallback
--max-pages N: quick verification on first N pages
--fail-on-empty: stop when no text extracted
Error Handling Rules

If conversion/extraction fails:

Return a concrete cause (missing dependency, unsupported format, conversion error).
Provide exact next action (install command or format conversion step).
Do not fabricate extracted content.

If extracted text is low quality:

Keep warnings in output metadata.
Continue chunking with available text.
Explicitly mark uncertainty in report.
Dependency Baseline

Install Python deps:

python -m pip install -r requirements.txt


Recommended system tools:

tesseract + chi_sim
pdftoppm (Poppler)
soffice (LibreOffice), or Microsoft PowerPoint (Windows)
Final Analysis Rules

When producing final conclusions from output artifacts:

Read all chunks before writing conclusions.
Cite chunk IDs for key claims, e.g. [C003][C011].
Separate facts from assumptions.
List missing evidence and unresolved questions.
Keep numeric claims exactly aligned with extracted text.
Minimal Working Examples

PDF:

python scripts/prepare_document_context.py "./report.pdf" --output-dir "./out"


DOCX:

python scripts/prepare_document_context.py "./report.docx" --output-dir "./out"


PPTX:

python scripts/prepare_document_context.py "./slides.pptx" --output-dir "./out"

Weekly Installs
29
Repository
20041002liu-clo…eader-zh
GitHub Stars
3
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail