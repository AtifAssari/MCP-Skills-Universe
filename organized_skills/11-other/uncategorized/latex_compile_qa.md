---
rating: ⭐⭐
title: latex-compile-qa
url: https://skills.sh/willoscar/research-units-pipeline-skills/latex-compile-qa
---

# latex-compile-qa

skills/willoscar/research-units-pipeline-skills/latex-compile-qa
latex-compile-qa
Installation
$ npx skills add https://github.com/willoscar/research-units-pipeline-skills --skill latex-compile-qa
SKILL.md
LaTeX Compile + QA

Compile the LaTeX project and produce a PDF (when the toolchain is available), plus a short build report.

This step is deterministic; if compilation fails, record actionable diagnostics rather than guessing.

Inputs
latex/main.tex
citations/ref.bib
Outputs
latex/main.pdf (if compilation succeeds)
output/LATEX_BUILD_REPORT.md (recommended)
Workflow
Run a LaTeX build (e.g., latexmk) if available.
Fix missing packages, missing bib entries, and unresolved references.
Record remaining issues in a build report.
Quality checklist
 Either latex/main.pdf exists, or output/LATEX_BUILD_REPORT.md explains why compilation failed.
 For arxiv-survey-latex deliverables: latex/main.pdf is >= 8 pages and has no undefined citations/references (strict gate).
Script
Quick Start
python .codex/skills/latex-compile-qa/scripts/run.py --help
python .codex/skills/latex-compile-qa/scripts/run.py --workspace <workspace_dir>
All Options
See --help (inputs/outputs are taken from the unit runner when used via pipeline)
Examples
Compile + produce report:
python .codex/skills/latex-compile-qa/scripts/run.py --workspace <ws>
Notes
Uses latexmk -xelatex -bibtex when available.
Always writes output/LATEX_BUILD_REPORT.md (success or failure).
Report includes page count + warning summary when available.
Troubleshooting
Common Issues
Issue: latexmk not found

Symptom:

Build report says “latexmk not found in PATH”.

Causes:

LaTeX toolchain is not installed.

Solutions:

Install a TeX distribution that includes latexmk.
If you can’t install tools, still use latex-scaffold to generate latex/main.tex and compile elsewhere.
Issue: Build fails with bib/ref errors

Symptom:

Report shows missing citations/refs or BibTeX errors.

Causes:

citations/ref.bib missing/miswired, or draft contains invalid cite keys.

Solutions:

Ensure latex/main.tex points to ../citations/ref.bib (or the correct relative path).
Ensure all citation keys exist in citations/ref.bib.
Recovery Checklist
 Read output/LATEX_BUILD_REPORT.md tail for the first actionable error.
 Confirm latex/main.tex exists and bibliography path is correct.
Weekly Installs
91
Repository
willoscar/resea…e-skills
GitHub Stars
424
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass