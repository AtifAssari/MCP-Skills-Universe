---
rating: ⭐⭐
title: translate-pdf
url: https://skills.sh/wshuyi/translate-pdf-skill/translate-pdf
---

# translate-pdf

skills/wshuyi/translate-pdf-skill/translate-pdf
translate-pdf
Installation
$ npx skills add https://github.com/wshuyi/translate-pdf-skill --skill translate-pdf
Summary

Translate PDF documents to any language while preserving layout, colors, and styling.

Three-step workflow: extract text strings, create a JSON translation mapping, then apply translations with language-specific font selection
Supports five font families covering Latin languages, Simplified Chinese, Traditional Chinese, Japanese, and Korean
CJK fonts automatically scale to 90% for optimal text fitting within original PDF boundaries
Preserves all original formatting including colors, backgrounds, and element positioning
SKILL.md
PDF Translation

Translate PDF text while preserving structure, colors, and background styling.

Workflow
Step 1: Extract texts
python {skill_path}/scripts/extract_texts.py <input.pdf>


Review output to see all unique text strings in the PDF.

Step 2: Create translation mapping

Translate each text to target language. Create JSON file:

{
  "Original Text 1": "Translated 1",
  "Original Text 2": "Translated 2"
}


Save as translations.json next to input PDF.

Step 3: Apply translations
python {skill_path}/scripts/translate_pdf.py <input.pdf> translations.json <output.pdf> --font <fontname>


Font options:

Font	Language
helv	Latin (English, Spanish, Portuguese, French, German, etc.)
china-ss	Simplified Chinese
china-ts	Traditional Chinese
japan	Japanese
korea	Korean
Output naming

Append language suffix: filename_EN.pdf, filename_ZH.pdf, filename_JA.pdf

Tips
Keep proper nouns, abbreviations, technical terms unchanged when appropriate
CJK fonts auto-scale to 90% for better fit
Use transparent fill to preserve original background colors
Weekly Installs
604
Repository
wshuyi/translat…df-skill
GitHub Stars
7
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass