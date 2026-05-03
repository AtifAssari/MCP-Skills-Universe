---
title: ocr-document-processor
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/ocr-document-processor
---

# ocr-document-processor

skills/dkyazzentwatwa/chatgpt-skills/ocr-document-processor
ocr-document-processor
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill ocr-document-processor
Summary

Extract text from images and scanned PDFs with support for 100+ languages, table detection, and multiple output formats.

Handles PNG, JPEG, TIFF, BMP images and multi-page PDFs with per-page or full-document extraction
Supports 100+ languages with auto-detection, language-specific packs, and multi-language document processing
Exports to plain text, Markdown, JSON, HTML, and searchable PDFs with confidence scoring and bounding box data
Includes intelligent preprocessing (deskew, denoise, contrast enhancement, shadow removal) for low-quality scans and specialized parsers for receipts and business cards
Batch processing for directories, configurable page segmentation modes, and per-word confidence assessment for quality validation
SKILL.md
OCR Document Processor

Handle OCR-heavy inputs where text must be recovered from images or scanned pages.

Use This For
OCR on images and scanned PDFs
Searchable PDF export
Structured extraction to text, markdown, JSON, or HTML
Table extraction from scanned material
Receipt parsing and business card parsing
Workflow
Decide whether plain OCR, structured extraction, or document-specific parsing is needed.
Preprocess noisy inputs before extraction when skew, blur, or shadows are present.
Use scripts/ocr_processor.py for core OCR tasks.
Use the focused helpers when the input is specialized:
scripts/business_card_scanner.py
scripts/receipt_scanner.py
Return confidence caveats when the source is low quality, rotated, handwritten, or multilingual.
Guardrails
Prefer explicit language selection when accuracy matters.
Do not claim fields are exact when OCR confidence is weak.
Route non-scanned digital PDFs to document-converter-suite instead of OCR by default.
Weekly Installs
3.7K
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass