---
title: translate-pdf
url: https://skills.sh/morphet81/cheat-sheets/translate-pdf
---

# translate-pdf

skills/morphet81/cheat-sheets/translate-pdf
translate-pdf
Installation
$ npx skills add https://github.com/morphet81/cheat-sheets --skill translate-pdf
SKILL.md

Translate a PDF document end-to-end: extract structured Markdown from the source PDF, translate the content, and build a new PDF in the target language.

Usage:

/translate-pdf ./report.pdf French English — Translate a French PDF to English
/translate-pdf /path/to/manual.pdf English Spanish — Translate an English PDF to Spanish
/translate-pdf invoice.pdf German French — Translate a German PDF to French

Instructions:

Parse positional arguments:

$1 = path to the source PDF file
$2 = the language the PDF is currently written in
$3 = the language to translate into
If any of $1, $2, or $3 is missing, display the following and STOP:
## Missing Arguments

Usage: /translate-pdf <path-to-pdf> <source-language> <target-language>

Examples:
  /translate-pdf ./report.pdf French English
  /translate-pdf /path/to/manual.pdf English Spanish
  /translate-pdf invoice.pdf German French


Validate the PDF file exists:

Resolve the path and verify the file exists and has a .pdf extension
If the file does not exist, display the error and STOP:
File not found: "<path>"
Please provide a valid path to a PDF file.


Check Python dependencies:

The skill relies on a Python script located at skills/translate-pdf/translate_pdf.py (relative to this repo). The script requires:

pymupdf — PDF text extraction
markdown — Markdown to HTML conversion
weasyprint — HTML to PDF rendering (also requires system libraries: cairo, pango, gdk-pixbuf)

a) Check if the dependencies are installed: Run python3 -c "import fitz; import markdown; from weasyprint import HTML; print('OK')" via the Bash tool.

b) If the check fails, use AskUserQuestion to ask the developer:

The following Python packages are required but not all are installed:

pymupdf (PDF extraction)
markdown (Markdown → HTML)
weasyprint (HTML → PDF, also needs system libs: cairo, pango, gdk-pixbuf)

Would you like me to install them now?

Provide two options:

Yes — install with pip → Run pip install pymupdf markdown weasyprint
No — I'll handle it myself → Display manual installation instructions and STOP:
## Manual Installation

Install the Python packages:
  pip install pymupdf markdown weasyprint

weasyprint also requires system libraries. Install them for your OS:

macOS (Homebrew):
  brew install cairo pango gdk-pixbuf libffi

Ubuntu/Debian:
  sudo apt install libcairo2-dev libpango1.0-dev libgdk-pixbuf2.0-dev libffi-dev

Then re-run the skill.


Step 1 — Extract PDF to Markdown:

Determine the output directory — use the same directory as the source PDF.

Run the extraction script:

python3 <repo-root>/skills/translate-pdf/translate_pdf.py extract "<pdf-path>" -o "<output-dir>/<filename>_source.md"


Where <filename> is the PDF filename without extension.

After extraction, read the generated Markdown file to verify it looks reasonable. If the Markdown is mostly empty or garbled (e.g., the PDF is scanned/image-based), warn the developer:

The PDF appears to be image-based or has very little extractable text. The translation may be incomplete or inaccurate. Consider using an OCR tool first.

Step 1b — Verify table preservation:

The extraction script automatically detects tables in the PDF using PyMuPDF's find_tables() and converts them to Markdown table syntax. After extraction, you must verify that tables are correctly preserved:

a) Read the source PDF using the Read tool to visually identify all tables in the document. Note the number of tables and their approximate content (headers, row counts).

b) Read the extracted Markdown file and locate all Markdown tables (lines starting with |). For each table, verify:

The table has a header row, a separator row (| --- | --- |), and the correct number of data rows
Cell content is present and not empty where the original PDF had data
Multi-column structure is preserved (correct number of | delimiters per row)

c) Compare counts: If the number of Markdown tables does not match the number of tables you identified in the source PDF, some tables were likely not detected. For each missing table:

Identify the page and location of the missing table in the PDF
Manually reconstruct the table in Markdown format by reading the relevant text from the extracted Markdown (the content may appear as plain text paragraphs)
Insert the reconstructed Markdown table at the correct position in the file, replacing the plain-text paragraph(s) that contained the table data

d) Fix malformed tables: If any Markdown table has inconsistent column counts, missing separators, or garbled content, fix it by referencing the source PDF. Ensure every table row has the same number of columns.

After verification and any fixes, save the updated Markdown file.

Step 2 — Translate the Markdown:

Read the extracted Markdown file (<filename>_source.md).

Translate all text content from <source-language> to <target-language>, following these rules:

Preserve all Markdown formatting — headings, bold, italic, lists, tables, code blocks, links, image references
Preserve all Markdown tables exactly — keep the same number of rows, columns, header rows, and separator rows. Translate cell content but never alter table structure (do not add, remove, or merge columns/rows)
Preserve page comment markers (<!-- page N -->) and horizontal rules (---) that act as page separators
Do NOT translate: code snippets, URLs, file paths, proper nouns that are universally recognized (brand names, product names), or technical identifiers
Translate naturally — produce fluent, natural-sounding text in the target language, not word-for-word translation
Preserve document structure — the translated Markdown should have the same number of sections, paragraphs, tables, and structural elements as the source

Write the translated content to <output-dir>/<filename>_<target-language>.md (e.g., report_English.md).

Step 3 — Build the translated PDF:

Run the build script:

python3 <repo-root>/skills/translate-pdf/translate_pdf.py build "<output-dir>/<filename>_<target-language>.md" -o "<output-dir>/<filename>_<target-language>.pdf"


Verify the output PDF was created successfully.

Report results:

Display a summary:

## Translation Complete

**Source:** <pdf-path> (<source-language>)
**Target language:** <target-language>

### Generated Files
- Source Markdown: `<filename>_source.md`
- Translated Markdown: `<filename>_<target-language>.md`
- Translated PDF: `<filename>_<target-language>.pdf`

All files saved in: `<output-directory>/`


Handle edge cases:

If the PDF is password-protected, display an error and STOP
If the PDF has no extractable text at all, warn the developer and STOP
If the build step fails due to missing system libraries (weasyprint dependency), display the platform-specific installation instructions from step 3
If the source and target languages are the same, warn the developer and ask for confirmation before proceeding
Weekly Installs
67
Repository
morphet81/cheat-sheets
First Seen
2 days ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass