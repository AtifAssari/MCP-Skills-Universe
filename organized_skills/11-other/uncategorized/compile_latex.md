---
rating: ⭐⭐⭐
title: compile-latex
url: https://skills.sh/pedrohcgs/claude-code-my-workflow/compile-latex
---

# compile-latex

skills/pedrohcgs/claude-code-my-workflow/compile-latex
compile-latex
Installation
$ npx skills add https://github.com/pedrohcgs/claude-code-my-workflow --skill compile-latex
SKILL.md
Compile Beamer LaTeX Slides

Compile a Beamer slide deck using XeLaTeX with full citation resolution.

Steps
Navigate to Slides/ directory and compile with 3-pass sequence:
cd Slides
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode $ARGUMENTS.tex
BIBINPUTS=..:$BIBINPUTS bibtex $ARGUMENTS
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode $ARGUMENTS.tex
TEXINPUTS=../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode $ARGUMENTS.tex


Alternative (latexmk):

cd Slides
TEXINPUTS=../Preambles:$TEXINPUTS BIBINPUTS=..:$BIBINPUTS latexmk -xelatex -interaction=nonstopmode $ARGUMENTS.tex


Check for warnings:

Grep output for Overfull \\hbox warnings
Grep for undefined citations or Label(s) may have changed
Report any issues found

Open the PDF for visual verification:

open Slides/$ARGUMENTS.pdf          # macOS
# xdg-open Slides/$ARGUMENTS.pdf    # Linux


Report results:

Compilation success/failure
Number of overfull hbox warnings
Any undefined citations
PDF page count
Why 3 passes?
First xelatex: Creates .aux file with citation keys
bibtex: Reads .aux, generates .bbl with formatted references
Second xelatex: Incorporates bibliography
Third xelatex: Resolves all cross-references with final page numbers
Important
Always use XeLaTeX, never pdflatex
TEXINPUTS is required: your Beamer theme lives in Preambles/
BIBINPUTS is required: your .bib file lives in the repo root
Weekly Installs
16
Repository
pedrohcgs/claud…workflow
GitHub Stars
1.0K
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass