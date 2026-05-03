---
rating: ⭐⭐⭐
title: pdf-toolkit
url: https://skills.sh/dkyazzentwatwa/chatgpt-skills/pdf-toolkit
---

# pdf-toolkit

skills/dkyazzentwatwa/chatgpt-skills/pdf-toolkit
pdf-toolkit
Installation
$ npx skills add https://github.com/dkyazzentwatwa/chatgpt-skills --skill pdf-toolkit
SKILL.md
PDF Toolkit

Comprehensive PDF manipulation toolkit for merging, splitting, rotating, and more.

Features
Merge: Combine multiple PDFs into one
Split: Extract pages or split into chunks
Rotate: Rotate pages by 90/180/270 degrees
Extract: Extract specific pages or page ranges
Watermark: Add text/image watermarks
Compress: Reduce file size
Encrypt: Add password protection
Metadata: Edit PDF metadata
Page Numbers: Add page numbers
Bookmarks: Add/remove bookmarks
Quick Start
from pdf_toolkit import PDFToolkit

toolkit = PDFToolkit()

# Merge PDFs
toolkit.merge(['doc1.pdf', 'doc2.pdf'], 'merged.pdf')

# Extract pages
toolkit.load('document.pdf').extract_pages([1, 3, 5], 'extracted.pdf')

# Add watermark
toolkit.load('document.pdf').watermark('CONFIDENTIAL', output='watermarked.pdf')

CLI Usage
# Merge
python pdf_toolkit.py merge file1.pdf file2.pdf --output merged.pdf

# Split
python pdf_toolkit.py split document.pdf --pages 10 --output chunks/

# Rotate
python pdf_toolkit.py rotate document.pdf --angle 90 --pages 1-5 --output rotated.pdf

# Watermark
python pdf_toolkit.py watermark document.pdf --text "DRAFT" --output watermarked.pdf

Dependencies
PyPDF2>=3.0.0
PyMuPDF>=1.23.0
pillow>=10.0.0
reportlab>=4.0.0
Weekly Installs
93
Repository
dkyazzentwatwa/…t-skills
GitHub Stars
53
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass