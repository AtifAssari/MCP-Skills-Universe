---
rating: ⭐⭐⭐
title: markdown-converter
url: https://skills.sh/intellectronica/agent-skills/markdown-converter
---

# markdown-converter

skills/intellectronica/agent-skills/markdown-converter
markdown-converter
Installation
$ npx skills add https://github.com/intellectronica/agent-skills --skill markdown-converter
Summary

Convert documents, spreadsheets, presentations, images, audio, and web content to Markdown for LLM processing.

Supports 15+ formats including PDF, Word, PowerPoint, Excel, HTML, CSV, JSON, XML, images with OCR, audio with transcription, ZIP archives, YouTube URLs, and EPub
Preserves document structure including headings, tables, lists, and links in the converted Markdown output
Optional Azure Document Intelligence integration (-d flag) for improved extraction on complex or scanned PDFs
Runs via uvx markitdown with no local installation required; accepts file paths, stdin input, or URL hints via -x and -m flags
SKILL.md
Markdown Converter

Convert files to Markdown using uvx markitdown — no installation required.

Basic Usage
# Convert to stdout
uvx markitdown input.pdf

# Save to file
uvx markitdown input.pdf -o output.md
uvx markitdown input.docx > output.md

# From stdin
cat input.pdf | uvx markitdown

Supported Formats
Documents: PDF, Word (.docx), PowerPoint (.pptx), Excel (.xlsx, .xls)
Web/Data: HTML, CSV, JSON, XML
Media: Images (EXIF + OCR), Audio (EXIF + transcription)
Other: ZIP (iterates contents), YouTube URLs, EPub
Options
-o OUTPUT      # Output file
-x EXTENSION   # Hint file extension (for stdin)
-m MIME_TYPE   # Hint MIME type
-c CHARSET     # Hint charset (e.g., UTF-8)
-d             # Use Azure Document Intelligence
-e ENDPOINT    # Document Intelligence endpoint
--use-plugins  # Enable 3rd-party plugins
--list-plugins # Show installed plugins

Examples
# Convert Word document
uvx markitdown report.docx -o report.md

# Convert Excel spreadsheet
uvx markitdown data.xlsx > data.md

# Convert PowerPoint presentation
uvx markitdown slides.pptx -o slides.md

# Convert with file type hint (for stdin)
cat document | uvx markitdown -x .pdf > output.md

# Use Azure Document Intelligence for better PDF extraction
uvx markitdown scan.pdf -d -e "https://your-resource.cognitiveservices.azure.com/"

Notes
Output preserves document structure: headings, tables, lists, links
First run caches dependencies; subsequent runs are faster
For complex PDFs with poor extraction, use -d with Azure Document Intelligence
Weekly Installs
1.1K
Repository
intellectronica…t-skills
GitHub Stars
254
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn