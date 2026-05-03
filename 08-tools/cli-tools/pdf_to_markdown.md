---
title: pdf-to-markdown
url: https://skills.sh/pspdfkit-labs/nutrient-skills/pdf-to-markdown
---

# pdf-to-markdown

skills/pspdfkit-labs/nutrient-skills/pdf-to-markdown
pdf-to-markdown
Installation
$ npx skills add https://github.com/pspdfkit-labs/nutrient-skills --skill pdf-to-markdown
SKILL.md
PDF to Markdown

Convert PDFs into structured, semantic Markdown that preserves the document's logical structure — headings, tables, lists, and reading order — rather than producing flat text. This is significantly higher quality than reading a PDF directly with the read tool, which only extracts raw text without structure.

Usage

Before running any commands, set SKILL_DIR to the absolute path of the directory containing this SKILL.md file. Use $SKILL_DIR/bin/pdf-to-markdown in all commands below.

The $SKILL_DIR/bin/pdf-to-markdown wrapper automatically installs the platform-specific binary into ~/.local/share/nutrient/cli/ from the CDN. It caches the binary and only checks for updates every 6 hours, so subsequent runs are fast.

Single file
$SKILL_DIR/bin/pdf-to-markdown INPUT.pdf OUTPUT.md


If OUTPUT.md is omitted, the converter writes the Markdown to stdout instead.

Batch directory (2+ files)

For multiple files, pass directories instead of individual files. The converter processes all PDFs in the input directory in parallel, which is much faster than converting one at a time.

$SKILL_DIR/bin/pdf-to-markdown INPUT_DIR/ OUTPUT_DIR/

Image export

To extract images from the PDF and reference them in the output Markdown, add the --enable-image-export flag:

$SKILL_DIR/bin/pdf-to-markdown --enable-image-export INPUT.pdf OUTPUT.md


Images are saved to {output}_resources/ alongside the output file and referenced as standard Markdown image links. This is useful when feeding output to LLMs that support vision, or when image context improves downstream accuracy. Off by default because it increases processing time for image-heavy documents.

Workflow
Choose mode: Use batch directory mode for 2+ files, single file mode otherwise.
Run the converter: $SKILL_DIR/bin/pdf-to-markdown INPUT [OUTPUT]
Check the exit code: Exit 0 means success. On failure, read stderr for the error message.
Validate the output: If the output file is empty or near-empty, see Troubleshooting below.
Report the output path: Tell the user where the converted file(s) are. Do NOT read the markdown back into context by default — converted documents can be very large and will fill the context window. Only read the output if the user's task specifically requires analyzing or summarizing the content (e.g., "summarize this PDF", "what does this contract say about X").
Troubleshooting
Empty or minimal output: The PDF may be scanned/image-only and contains no extractable text.
Non-zero exit code: Read stderr for the specific error. Common causes: corrupted PDF, unsupported encryption, or network issues during first-run binary download.
First run is slow: The wrapper downloads the platform binary on first use (~a few seconds). Subsequent runs use the cached binary.
License

Free for processing up to 1,000 documents per calendar month.

Commercial license required for:

processing over 1,000 documents/month
redistributing the binary
OEM/white-label use

Contact sales@nutrient.io for commercial licensing.

Weekly Installs
76
Repository
pspdfkit-labs/n…t-skills
GitHub Stars
10
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn