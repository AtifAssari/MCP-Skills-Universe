---
title: lovstudio-pdf2png
url: https://skills.sh/lovstudio/skills/lovstudio-pdf2png
---

# lovstudio-pdf2png

skills/lovstudio/skills/lovstudio-pdf2png
lovstudio-pdf2png
Installation
$ npx skills add https://github.com/lovstudio/skills --skill lovstudio-pdf2png
SKILL.md
pdf2png — PDF to Vertically Concatenated PNG

Convert multi-page PDF files into a single tall PNG image. All pages are rendered at 2x scale (Retina quality) and stitched vertically. Uses macOS CoreGraphics directly — no pdftoppm, no ImageMagick, no Ghostscript.

When to Use
User wants to convert a PDF to a single PNG image
User needs a long screenshot-style image of a PDF
User wants to share PDF content as an image (WeChat, social media, etc.)
Workflow
Step 1: Identify PDF files

Locate the PDF file(s) the user wants to convert. Confirm the path(s).

Step 2: Execute
bash lovstudio-pdf2png/scripts/pdf2png.sh /path/to/file.pdf


Output: /path/to/file.png (same directory, same name, .png extension).

For multiple files:

bash lovstudio-pdf2png/scripts/pdf2png.sh file1.pdf file2.pdf file3.pdf

Step 3: Verify

Check the output file exists and report its size.

CLI Reference
Argument	Description
file1.pdf [file2.pdf ...]	One or more PDF files to convert

Output is always <input>.png in the same directory as the input file.

Finder Quick Action

This skill can also be installed as a macOS Finder Quick Action for right-click conversion. See lovstudio/mac-pdf2png for the Automator workflow.

Dependencies
pip install pyobjc-framework-Quartz --break-system-packages

Weekly Installs
12
Repository
lovstudio/skills
GitHub Stars
45
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass