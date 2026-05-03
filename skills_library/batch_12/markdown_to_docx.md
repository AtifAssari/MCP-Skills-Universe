---
title: markdown-to-docx
url: https://skills.sh/vace/markdown-docx/markdown-to-docx
---

# markdown-to-docx

skills/vace/markdown-docx/markdown-to-docx
markdown-to-docx
Installation
$ npx skills add https://github.com/vace/markdown-docx --skill markdown-to-docx
SKILL.md
Markdown to DOCX Converter
Overview

Convert Markdown files to Microsoft Word DOCX format using the markdown-docx npm package. Supports single file and batch conversions with automatic output file naming.

Quick Start

Single file conversion:

python scripts/convert_md_to_docx.py -i document.md


This creates document.docx in the same directory.

Batch conversion:

python scripts/convert_md_to_docx.py -i file1.md file2.md file3.md


Each file is converted to DOCX in its original location.

Custom output location:

python scripts/convert_md_to_docx.py -i document.md -o output/mydoc.docx


Batch to specific directory:

python scripts/convert_md_to_docx.py -i *.md -o output_docs/

Workflow

When a user requests markdown to DOCX conversion:

Identify input files - Confirm which markdown file(s) to convert
Determine output naming - Use auto-naming unless user specifies custom names
Run conversion - Execute the script with appropriate parameters
Report results - Inform user of success and output file location(s)
Common Use Cases
Convert a single markdown file

User: "Convert README.md to DOCX"

python scripts/convert_md_to_docx.py -i README.md

Convert all markdown files in current directory

User: "Convert all my markdown files to Word documents"

python scripts/convert_md_to_docx.py -i *.md

Convert with custom output name

User: "Convert notes.md to report.docx"

python scripts/convert_md_to_docx.py -i notes.md -o report.docx

Convert documentation set to a folder

User: "Convert all docs to DOCX and put them in the exports folder"

python scripts/convert_md_to_docx.py -i docs/*.md -o exports/

Script Details

Location: scripts/convert_md_to_docx.py

Features:

Validates input files exist and are markdown format
Auto-generates output filenames (input.md → input.docx)
Supports custom output paths for single files
Supports output directory for batch conversions
Creates output directories if they don't exist
Provides clear success/failure feedback
Returns proper exit codes for automation

Requirements:

Python 3+
Node.js and npm (for npx)
markdown-docx npm package (automatically fetched via npx)
Error Handling

The script handles common errors:

Input file not found - Reports missing file path
Invalid file type - Ensures input is .md or .markdown
npx not available - Checks for Node.js/npm installation
Conversion failure - Captures and reports markdown-docx errors
Tips
Auto-naming is preferred - The script automatically names output files, reducing friction
Batch operations - When converting multiple files, the script shows a summary of successes and failures
Path handling - Both absolute and relative paths work for input and output
Glob patterns - Shell glob patterns (*.md) can be used for batch operations
Weekly Installs
81
Repository
vace/markdown-docx
GitHub Stars
299
First Seen
Feb 3, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass