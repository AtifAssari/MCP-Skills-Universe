---
rating: ⭐⭐⭐
title: sh_sci_fig
url: https://skills.sh/shzhao27208/aut_sci_write/sh_sci_fig
---

# sh_sci_fig

skills/shzhao27208/aut_sci_write/Sh_Sci_Fig
Sh_Sci_Fig
Installation
$ npx skills add https://github.com/shzhao27208/aut_sci_write --skill Sh_Sci_Fig
SKILL.md
Sh_Sci_Fig — Scientific Figure Extractor

Precisely extract figures and sub-figures from academic PDF papers.

Script Directory

Scripts in scripts/ subdirectory. Replace ${SKILL_DIR} with this SKILL.md's directory path.

Script	Purpose
scripts/extract_figure.py	Main CLI for figure extraction
Preferences (EXTEND.md)

Use Bash to check EXTEND.md existence (priority order):

# Check project-level first
test -f .baoyu-skills/Sh_Sci_Fig/EXTEND.md && echo "project"

# Then user-level (cross-platform: $HOME works on macOS/Linux/WSL)
test -f "$HOME/.baoyu-skills/Sh_Sci_Fig/EXTEND.md" && echo "user"


EXTEND.md Supports: Default DPI | Default output format | Tesseract path

Usage
python ${SKILL_DIR}/scripts/extract_figure.py <input.pdf> [options]

Options
Option	Short	Description	Default
<input>		PDF file path	Required
--figure	-f	Figure number (1, 2, 3...)	Required (except --list/--all)
--subfigure	-s	Sub-figure label (a, b, c...)	None (returns whole figure)
--output	-o	Output directory	Current directory
--dpi	-d	Output resolution	600
--list	-l	List all available figure numbers	false
--all		Extract all figures	false
--format		Output format	png
Examples
# Extract Figure 2, sub-figure c
python ${SKILL_DIR}/scripts/extract_figure.py paper.pdf -f 2 -s c

# Extract entire Figure 3
python ${SKILL_DIR}/scripts/extract_figure.py paper.pdf -f 3

# List all available figures in a PDF
python ${SKILL_DIR}/scripts/extract_figure.py paper.pdf --list

# Extract all figures
python ${SKILL_DIR}/scripts/extract_figure.py paper.pdf --all

# Custom output directory and DPI
python ${SKILL_DIR}/scripts/extract_figure.py paper.pdf -f 2 -s c -o ./output/ -d 300


Output:

Extracted: figure_2c.png (1920x1080, 600 DPI)

Error Handling
Scenario	Behavior
Figure number not found	Error + list all available figure numbers
OCR recognition failed	Return entire figure region
Sub-figure split failed	Return entire figure region
No sub-figure labels found	Return entire figure region
Tech Stack
Library	Role
pdfplumber	Text + coordinate extraction (locate "Figure X" labels)
PyMuPDF (fitz)	PDF → high-quality image rendering (600 DPI)
opencv-python	Boundary detection, contour analysis
Pillow	Final cropping, format conversion
pytesseract	OCR for sub-figure label recognition
Extension Support

Custom configurations via EXTEND.md. See Preferences section for paths and supported options.

Weekly Installs
12
Repository
shzhao27208/aut…ci_write
GitHub Stars
37
First Seen
Apr 9, 2026