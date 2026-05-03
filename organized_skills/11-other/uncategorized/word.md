---
rating: ⭐⭐
title: word
url: https://skills.sh/igorwarzocha/opencode-workflows/word
---

# word

skills/igorwarzocha/opencode-workflows/word
word
Installation
$ npx skills add https://github.com/igorwarzocha/opencode-workflows --skill word
SKILL.md

<quality_workflow> For all professional deliverables, you MUST follow the "Render & Review" loop:

Edit: Use python-docx for structure/styling or the Document library for XML edits.
Render: Convert to PDF/PNG using soffice and pdftoppm:
soffice --headless --convert-to pdf document.docx
pdftoppm -png -r 150 document.pdf page
Inspect: Read the generated PNG images. You MUST look for clipped text, overlapping shapes, or misaligned margins.
Fix: Address defects and repeat the loop until the document is visually flawless. </quality_workflow>

<technical_workflows>

1. Creating New Documents
Python: You SHOULD use python-docx. Establish hierarchy with HeadingLevel styles.
JavaScript: You SHOULD use docx-js. Reference: See references/docx-js.md for syntax.
CRITICAL: You MUST NOT use \n for line breaks (use Paragraphs). You MUST NOT use Unicode bullets (use numbering config). PageBreak MUST be inside a Paragraph.
2. Redlining & Tracked Changes

For legal or business review:

Initialize: Use scripts/document.py. Reference: Read references/ooxml.md for XML patterns.
Procedure: Unpack (unpack.py), edit XML using the Document Library, then Pack (pack.py).
Standard: You MUST only mark text that actually changes. Keep unchanged text outside <w:del>/<w:ins>.
3. Text Extraction
You SHOULD use Pandoc to convert to markdown while preserving structure:
pandoc --track-changes=all path-to-file.docx -o output.md </technical_workflows>

<quality_expectations>

Client-Ready: You MUST NOT use Unicode dashes (use ASCII hyphens). No internal AI tokens.
Element Ordering: In <w:pPr>, elements MUST follow schema order: Style -> Numbering -> Spacing -> Indent -> Alignment.
Visual Fidelity: Charts and tables MUST be sharp and legible in rendered previews. </quality_expectations>

</word_document_professional_suite>

Weekly Installs
124
Repository
igorwarzocha/op…orkflows
GitHub Stars
111
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass