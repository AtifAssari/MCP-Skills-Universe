---
title: markitdown
url: https://skills.sh/0xdarkmatter/claude-mods/markitdown
---

# markitdown

skills/0xdarkmatter/claude-mods/markitdown
markitdown
Installation
$ npx skills add https://github.com/0xdarkmatter/claude-mods --skill markitdown
SKILL.md
markitdown - Document to Markdown

Convert local documents to clean Markdown. One tool for PDF, Word, Excel, PowerPoint, images, and more.

When to Use markitdown
Use Case	Recommendation
Local files (PDF, Word, Excel)	✅ Use markitdown - unique capability
Web pages	❌ Use Jina (r.jina.ai/) - 5x faster
Blocked/anti-bot sites	❌ Use Firecrawl
OCR on images	✅ Use markitdown
Audio transcription	✅ Use markitdown
Basic Usage
# Local files (primary use case)
markitdown document.pdf
markitdown report.docx
markitdown data.xlsx
markitdown slides.pptx
markitdown screenshot.png    # OCR

# URLs (works, but Jina is faster)
markitdown https://example.com

# Save output
markitdown document.pdf > document.md

Supported Formats
Format	Extensions	Notes
PDF	.pdf	Text extraction, tables
Word	.docx	Formatting preserved
Excel	.xlsx	Tables to markdown
PowerPoint	.pptx	Slides as sections
Images	.jpg, .png	OCR text extraction
HTML	.html	Clean conversion
Audio	.mp3, .wav	Speech-to-text
Text	.txt, .csv, .json, .xml	Pass-through/structure
URLs	https://...	Works but slower than Jina
Benchmarked Performance (URLs)
Tool	Avg Speed	Success Rate
Jina	0.5s	10/10
markitdown	2.5s	9/10
Firecrawl	4.5s	10/10

Verdict: For URLs, use Jina. For local files, markitdown is the only option.

Examples
# PDF to markdown (primary use case)
markitdown report.pdf > report.md

# Excel spreadsheet
markitdown financials.xlsx

# Image with text (OCR)
markitdown screenshot.png

# PowerPoint deck
markitdown presentation.pptx > slides.md

# Audio transcription
markitdown meeting.mp3 > transcript.md

Comparison with Alternatives
Task	markitdown	Alternative
PDF text	markitdown file.pdf	PyMuPDF, pdfplumber
Word docs	markitdown file.docx	python-docx
Excel	markitdown file.xlsx	pandas, openpyxl
OCR	markitdown image.png	Tesseract
Web pages	Use Jina instead	r.jina.ai/URL (5x faster)

markitdown's advantage: One CLI for all local document formats. No code needed.

Weekly Installs
25
Repository
0xdarkmatter/claude-mods
GitHub Stars
17
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn