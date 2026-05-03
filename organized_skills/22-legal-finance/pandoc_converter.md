---
rating: ⭐⭐⭐
title: pandoc-converter
url: https://skills.sh/jrajasekera/claude-skills/pandoc-converter
---

# pandoc-converter

skills/jrajasekera/claude-skills/pandoc-converter
pandoc-converter
Installation
$ npx skills add https://github.com/jrajasekera/claude-skills --skill pandoc-converter
SKILL.md
Pandoc Converter

Convert documents between common formats using Pandoc.

Quick Start
# Basic conversion (format auto-detected from extensions)
python scripts/convert.py input.md output.docx

# Specify output format only
python scripts/convert.py document.md --to html

# Check if Pandoc is installed
python scripts/convert.py --check

# List supported formats
python scripts/convert.py --formats

Supported Formats

Document formats (read/write): markdown, html, docx, latex, epub, rtf, pptx, pdf
Data formats (read only): csv, tsv, xlsx
Markdown variants: gfm (GitHub), commonmark

For detailed compatibility, see references/format-compatibility.md.

Common Conversions
From	To	Command
Markdown	Word	python scripts/convert.py doc.md doc.docx
Markdown	PDF	python scripts/convert.py doc.md doc.pdf
Markdown	HTML	python scripts/convert.py doc.md doc.html
Word	Markdown	python scripts/convert.py doc.docx doc.md
CSV	HTML table	python scripts/convert.py data.csv data.html
LaTeX	PDF	python scripts/convert.py paper.tex paper.pdf
Options
Option	Description
--from <fmt>	Override input format detection
--to <fmt>	Specify output format (if no output file)
--standalone	Include document headers/footers
--toc	Add table of contents
--pdf-engine <eng>	PDF engine: pdflatex, xelatex, lualatex

Additional Pandoc options pass through directly.

Workflow
Check installation: Run python scripts/convert.py --check
If not installed: Follow the installation instructions provided
Convert: Run the conversion with input and output files
Present result: Provide the converted file to the user
Installation (if needed)

The script provides installation guidance, but here's a summary:

# macOS
brew install pandoc

# Ubuntu/Debian  
sudo apt-get install pandoc

# For PDF output, also install LaTeX:
# macOS: brew install --cask mactex-no-gui
# Ubuntu: sudo apt-get install texlive-xetex

Limitations
CSV/TSV/XLSX: Input only (converts to tables in other formats)
PDF output: Requires LaTeX installation
PPTX: Text extraction works; complex layouts may simplify
Complex formatting: Some features may not transfer between formats
Weekly Installs
45
Repository
jrajasekera/cla…e-skills
GitHub Stars
1
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass