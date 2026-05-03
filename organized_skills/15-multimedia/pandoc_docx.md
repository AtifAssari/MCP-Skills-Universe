---
rating: ⭐⭐⭐
title: pandoc-docx
url: https://skills.sh/mengbo/mengbo-skills/pandoc-docx
---

# pandoc-docx

skills/mengbo/mengbo-skills/pandoc-docx
pandoc-docx
Installation
$ npx skills add https://github.com/mengbo/mengbo-skills --skill pandoc-docx
SKILL.md
Pandoc Docx
Prerequisites

Ensure Pandoc is installed:

pandoc --version
# If not installed: brew install pandoc (macOS) or apt-get install pandoc (Linux)

Directory Setup

Create working directories in your project root:

mkdir -p import export

import/ - Source files to convert
export/ - Converted output files
Convert to DOCX

Basic conversion:

pandoc import/input.md -o export/output.docx


Common options:

--reference-doc=template.docx - Apply custom styling
--toc - Generate table of contents
--toc-depth=2 - Set TOC depth
--metadata="title=My Document" - Set document metadata

Use skill's Chinese template:

# Path depends on where skill is installed:
# - Project local: .agents/skills/pandoc-docx/ (or your skill installation path)
# - Global: ~/.config/skills/pandoc-docx/ (varies by OS and tool)

pandoc import/input.md -o export/output.docx \
  --reference-doc=<skill-path>/assets/templates.docx

Convert from DOCX
pandoc import/document.docx -o export/document.md --extract-media=export/images/

Custom Templates
Generate default template: pandoc --print-default-data-file reference.docx > reference.docx
Edit styles in Word
Apply: pandoc import/input.md -o export/output.docx --reference-doc=reference.docx
Batch Processing
SKILL_PATH="<skill-path>"  # Adjust to your skill installation path

for file in import/*.md; do
  pandoc "$file" -o "export/$(basename "${file%.md}").docx" \
    --reference-doc=$SKILL_PATH/assets/templates.docx
done

Resources
assets/templates.docx - Chinese DOCX template with title numbering and code highlighting
scripts/convert.sh - Helper script for conversions (see usage below)
references/pandoc-options.md - Complete option reference and advanced patterns
Using convert.sh
# Run from project root. Adjust <skill-path> to where skill is installed:
<skill-path>/scripts/convert.sh report.md report.docx

# With options
<skill-path>/scripts/convert.sh report.md report.docx --toc

# Absolute paths work as usual
<skill-path>/scripts/convert.sh /path/to/input.md /path/to/output.docx

Weekly Installs
59
Repository
mengbo/mengbo-skills
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass