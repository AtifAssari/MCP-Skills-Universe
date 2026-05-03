---
rating: ⭐⭐⭐
title: documents
url: https://skills.sh/danielmiessler/personal_ai_infrastructure/documents
---

# documents

skills/danielmiessler/personal_ai_infrastructure/Documents
Documents
Installation
$ npx skills add https://github.com/danielmiessler/personal_ai_infrastructure --skill Documents
SKILL.md
Customization

Before executing, check for user customizations at: ~/.claude/PAI/USER/SKILLCUSTOMIZATIONS/Documents/

If this directory exists, load and apply any PREFERENCES.md, configurations, or resources found there. These override default behavior. If the directory does not exist, proceed with skill defaults.

🚨 MANDATORY: Voice Notification (REQUIRED BEFORE ANY ACTION)

You MUST send this notification BEFORE doing anything else when this skill is invoked.

Send voice notification:

curl -s -X POST http://localhost:8888/notify \
  -H "Content-Type: application/json" \
  -d '{"message": "Running the WORKFLOWNAME workflow in the Documents skill to ACTION"}' \
  > /dev/null 2>&1 &


Output text notification:

Running the **WorkflowName** workflow in the **Documents** skill to ACTION...


This is not optional. Execute this curl command immediately upon skill invocation.

Documents Skill
🎯 Load Full PAI Context

Before starting any task with this skill, load complete PAI context:

read ~/.claude/PAI/SKILL.md

When to Activate This Skill
Word Documents (DOCX)
User wants to create, edit, or analyze Word documents
User mentions "tracked changes", "redlining", "document review"
User needs to convert documents to other formats
User wants to work with document structure, comments, or formatting
PDF Files
User wants to create, merge, split, or manipulate PDFs
User mentions "extract text from PDF", "PDF tables", "fill PDF form"
User needs to convert PDFs to/from other formats
User wants to add watermarks, passwords, or extract images
PowerPoint Presentations (PPTX)
User wants to create or edit presentations
User mentions "slides", "presentation template", "speaker notes"
User needs to convert presentations to other formats
User wants to work with slide layouts or design elements
Excel Spreadsheets (XLSX)
User wants to create or edit spreadsheets
User mentions "formulas", "financial model", "data analysis"
User needs to work with Excel tables, charts, or pivot tables
User wants to convert spreadsheets to/from other formats
Workflow Routing
Request Pattern	Route To
Consulting report, McKinsey report, assessment report, professional PDF	Workflows/ConsultingReport.md
Large PDF, process big PDF, Gemini PDF	Workflows/ProcessLargePdfGemini3.md
Word document, DOCX, create docx, edit docx, tracked changes, redlining	Docx/SKILL.md
PDF, create PDF, merge PDF, split PDF, extract text from PDF, fill form	Pdf/SKILL.md
Presentation, PPTX, slides, PowerPoint, speaker notes	Pptx/SKILL.md
Spreadsheet, XLSX, Excel, formulas, financial model, data analysis	Xlsx/SKILL.md
Document Type Details

This skill organizes document processing across 4 document types plus specialized workflows:

Consulting Reports (HTML + Playwright PDF)

Reference Documentation:

Workflows/ConsultingReport.md - Complete consulting report generation workflow

Routing Logic:

"Create consulting report", "generate report PDF" → ConsultingReport workflow
"Build assessment report", "strategic assessment" → ConsultingReport workflow
"McKinsey-style report", "professional report PDF" → ConsultingReport workflow

Pipeline: Report Artifacts → Structured HTML → Playwright PDF

Key Capabilities:

Parse report directories with mixed content (markdown, TypeScript data, images)
Professional CSS typography (Georgia serif body, Inter sans headings)
Color-coded callout boxes (red/amber/green) and severity badges
Auto-generated linked Table of Contents
Cover page with classification marking
Headers/footers with CONFIDENTIAL and page numbers
Image compression pipeline (PNG → JPEG, max 1200px)
A4 format with Playwright for pixel-perfect PDF output

Reference Implementation: Quorum Cyber assessment at /path/to/reference/generate-pdf.mjs

Word Documents (DOCX)

Reference Documentation:

docx/SKILL.md - Complete DOCX processing guide
docx/docx-js.md - Creating new documents with JavaScript
docx/ooxml.md - Editing existing documents with OOXML

Routing Logic:

"Create Word document", "new docx" → Create workflow (docx-js)
"Edit Word document", "tracked changes", "redlining" → Edit workflow (OOXML)
"Read Word document", "extract text from docx" → Read workflow (pandoc)
"Document review", "track changes" → Redlining workflow

Supporting Resources:

Scripts: ~/.claude/skills/Utilities/Documents/Docx/Scripts/
OOXML tools: ~/.claude/skills/Utilities/Documents/Docx/ooxml/
License: ~/.claude/skills/Utilities/Documents/Docx/LICENSE.txt

Key Capabilities:

Create professional documents with docx-js
Edit with tracked changes (redlining workflow)
Extract text/comments with pandoc
Convert to images for visual inspection
Work with raw OOXML for advanced features
PDF Processing

Reference Documentation:

pdf/SKILL.md - Complete PDF processing guide
pdf/forms.md - Filling PDF forms
pdf/reference.md - Advanced features and troubleshooting

Routing Logic:

"Create PDF" → Creation workflow (reportlab)
"Merge PDFs", "split PDF" → Manipulation workflow (pypdf)
"Extract text from PDF" → Extraction workflow (pdfplumber)
"Fill PDF form" → Forms workflow (pdf-lib or pypdf)
"Extract tables from PDF" → Table extraction (pdfplumber + pandas)

Supporting Resources:

Scripts: ~/.claude/skills/Utilities/Documents/Pdf/Scripts/
License: ~/.claude/skills/Utilities/Documents/Pdf/LICENSE.txt

Key Capabilities:

Create PDFs with reportlab
Extract text/tables with pdfplumber
Merge/split with pypdf or qpdf
Fill forms programmatically
Add watermarks and password protection
Extract images from PDFs
PowerPoint Presentations (PPTX)

Reference Documentation:

pptx/SKILL.md - Complete PPTX processing guide
pptx/html2pptx.md - Creating presentations from HTML
pptx/ooxml.md - Editing existing presentations

Routing Logic:

"Create presentation", "new slides" → Creation workflow (html2pptx)
"Edit presentation", "modify slides" → Edit workflow (OOXML)
"Use presentation template" → Template workflow
"Extract slide text" → Read workflow (markitdown)
"Create thumbnail grid" → Thumbnail workflow

Supporting Resources:

Scripts: ~/.claude/skills/Utilities/Documents/Pptx/Scripts/
OOXML tools: ~/.claude/skills/Utilities/Documents/Pptx/ooxml/
License: ~/.claude/skills/Utilities/Documents/Pptx/LICENSE.txt

Key Capabilities:

Create presentations with html2pptx (HTML → PPTX)
Professional design with color palettes and layouts
Edit with OOXML for advanced features
Work with templates (rearrange, inventory, replace)
Generate thumbnail grids for visual analysis
Convert to images for inspection
Excel Spreadsheets (XLSX)

Reference Documentation:

xlsx/SKILL.md - Complete XLSX processing guide
xlsx/recalc.py - Formula recalculation script

Routing Logic:

"Create spreadsheet", "new Excel file" → Creation workflow (openpyxl)
"Edit spreadsheet", "modify Excel" → Edit workflow (openpyxl)
"Analyze data", "read Excel" → Analysis workflow (pandas)
"Financial model", "formulas" → Financial modeling workflow
"Recalculate formulas" → Recalculation workflow (recalc.py)

Supporting Resources:

Recalc script: ~/.claude/skills/Utilities/Documents/Xlsx/recalc.py
License: ~/.claude/skills/Utilities/Documents/Xlsx/LICENSE.txt

Key Capabilities:

Create spreadsheets with formulas (openpyxl)
Data analysis with pandas
Financial modeling with color coding standards
Formula recalculation with LibreOffice
Error detection and validation
Preserve formatting and formulas when editing
📋 Document Processing Principles
DOCX Best Practices
Tracked Changes - Use redlining workflow for professional document review
Minimal Edits - Only mark text that actually changes, preserve original RSIDs
Batch Changes - Group related edits (3-10 changes) for efficient processing
Verification - Always convert to markdown to verify changes applied correctly
PDF Best Practices
Library Selection - pypdf for basic ops, pdfplumber for text/tables, reportlab for creation
OCR for Scanned - Use pytesseract + pdf2image for scanned documents
Form Filling - Follow forms.md for programmatic form completion
Command Line - Use qpdf/pdftotext for simple operations
PPTX Best Practices
Design First - Analyze content and choose appropriate colors/layouts before coding
Web-Safe Fonts - Only use web-safe fonts (Arial, Helvetica, Times, etc.)
Visual Verification - Always generate thumbnails to inspect layout issues
Template Analysis - Create inventory before using templates to understand structure
XLSX Best Practices
Use Formulas - ALWAYS use Excel formulas, NEVER hardcode calculated values
Zero Errors - Deliver with zero formula errors (#REF!, #DIV/0!, etc.)
Recalculate - Run recalc.py after creating/editing to update formula values
Financial Standards - Follow color coding (blue inputs, black formulas, green links)
Examples

Example 1: Create proposal with tracked changes

User: "Create a consulting proposal doc with redlining"
→ Routes to DOCX workflows
→ Creates document with docx-js
→ Enables tracked changes for review workflow
→ Outputs professional .docx with revision marks


Example 2: Fill a PDF form programmatically

User: "Fill out this NDA PDF with my info"
→ Routes to PDF workflows
→ Reads form fields from PDF
→ Fills fields programmatically with pdf-lib
→ Outputs completed, flattened PDF


Example 3: Build financial model spreadsheet

User: "Create a revenue projection spreadsheet"
→ Routes to XLSX workflows
→ Creates workbook with openpyxl
→ Adds formulas (never hardcoded values)
→ Runs recalc.py to update calculations


Example 4: Generate professional consulting report PDF

User: "Create a consulting report from the assessment data"
→ Routes to ConsultingReport workflow
→ Parses report directory for data files, markdown, diagrams
→ Compresses images (PNG→JPEG, max 1200px)
→ Generates styled HTML with professional typography
→ Converts to PDF via Playwright with headers/footers
→ Outputs McKinsey-quality A4 PDF with TOC, diagrams, color boxes

🔗 Integration with Other Skills
Feeds Into:
writing skill - Creating documents for blog posts and newsletters
business skill - Creating consulting proposals and financial models
research skill - Extracting data from research documents
Uses:
media skill - Creating images for document illustrations
development skill - Building document processing automation
system skill - Command-line tools and scripting
🎯 Key Principles
Document Creation
Quality First - Professional formatting and structure from the start
Template Reuse - Leverage existing templates when available
Validation - Always verify output (visual inspection, error checking)
Automation - Use scripts for repetitive tasks
Document Editing
Preserve Intent - Maintain original formatting and structure
Track Changes - Use proper workflows for document review
Batch Processing - Group related operations for efficiency
Error Prevention - Validate before finalizing
Document Analysis
Right Tool - Choose appropriate library/tool for the task
Data Integrity - Preserve original data when extracting/converting
Format Awareness - Understand document structure (OOXML, PDF structure, etc.)
Performance - Use efficient methods for large documents
📚 Full Reference Documentation

Word Documents (DOCX):

Main Guide: ~/.claude/skills/Utilities/Documents/Docx/SKILL.md
Creation Reference: ~/.claude/skills/Utilities/Documents/Docx/docx-js.md
Editing Reference: ~/.claude/skills/Utilities/Documents/Docx/ooxml.md

PDF Processing:

Main Guide: ~/.claude/skills/Utilities/Documents/Pdf/SKILL.md
Forms Guide: ~/.claude/skills/Utilities/Documents/Pdf/forms.md
Advanced Reference: ~/.claude/skills/Utilities/Documents/Pdf/reference.md

PowerPoint Presentations (PPTX):

Main Guide: ~/.claude/skills/Utilities/Documents/Pptx/SKILL.md
Creation Reference: ~/.claude/skills/Utilities/Documents/Pptx/html2pptx.md
Editing Reference: ~/.claude/skills/Utilities/Documents/Pptx/ooxml.md

Excel Spreadsheets (XLSX):

Main Guide: ~/.claude/skills/Utilities/Documents/Xlsx/SKILL.md
Recalc Script: ~/.claude/skills/Utilities/Documents/Xlsx/recalc.py
Summary

The documents skill provides comprehensive document processing:

DOCX - Create, edit, analyze Word documents with tracked changes support
PDF - Create, manipulate, extract from PDFs with form filling capabilities
PPTX - Create, edit presentations with professional design and templates
XLSX - Create, edit spreadsheets with formulas and financial modeling

Reference-based organization - Each document type has complete guides and tooling

Routing is automatic - Analyzes user intent and activates appropriate document type workflow

Professional quality - Standards and best practices for production-ready documents

Weekly Installs
110
Repository
danielmiessler/…tructure
GitHub Stars
11.9K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail