---
title: docs-quality
url: https://skills.sh/illusion47586/isol8/docs-quality
---

# docs-quality

skills/illusion47586/isol8/docs-quality
docs-quality
Installation
$ npx skills add https://github.com/illusion47586/isol8 --skill docs-quality
SKILL.md
Docs Quality

Use this skill to produce documentation that is accurate, scannable, and complete enough for first-time and advanced users.

Workflow
Read docs/docs.json first to understand IA, tabs, and existing groups.
Research source-of-truth implementation details before writing:
scan relevant files under src/
read /src/types.ts for public types/options/contracts
read /schema/isol8.config.schema.json for config keys/defaults/enums
Read the target page(s) and at least 2 neighboring pages to match tone and structure.
Load the mintlify skill and check whether a better component exists to represent the current content (instead of defaulting to plain Markdown).
Choose the page archetype (overview, how-to, reference, guide, faq, troubleshooting, api).
Apply the standards in references/docs-quality-manual.md.
If adding pages, update navigation in docs/docs.json.
Add cross-links to adjacent conceptual and reference pages.
Run checks from references/review-checklist.md.
Optionally run scripts/docs_qc.sh for quick structural linting.
Which reference file to load
Complete standards: references/docs-quality-manual.md
Page skeletons: references/page-templates.md
Final QA gate: references/review-checklist.md
Mintlify component decisions: references/component-playbook.md
Ollama structural references: references/ollama-reference-notes.md
Non-negotiables
Every page must have clear title and description frontmatter.
Use explicit parameter/flag coverage for reference pages.
Examples must be realistic and runnable-looking.
Include expected output/behavior only when the snippet has a meaningful observable result to validate.
When documenting explicit input/output pairs, group them in a single <CodeGroup> (for example: Command + Expected output) instead of separating them into distant blocks.
When CLI + Library + API examples appear together, present them in <Tabs> (one tab per interface).
For substantial “Related pages” sections, use a <CardGroup> with descriptive cards instead of plain bullet links.
Diagrams must be readable on standard viewport (prefer vertical/simple over wide dense graphs).
New/changed pages must be cross-linked from related pages.
Avoid parser pitfalls in Markdown tables (especially unescaped pipe characters in inline code cells).
End substantial pages with page-relevant FAQ and troubleshooting guidance (or links to dedicated FAQ/troubleshooting pages when full sections would be redundant).
Callouts must follow intent: <Warning> for risk/breakage, <Info> for operational context, <Tip> for best-practice recommendations, <Note> for important but non-risk caveats, <Check> for explicit success confirmation.
Weekly Installs
12
Repository
illusion47586/isol8
GitHub Stars
4
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass