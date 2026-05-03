---
title: paper-compilation
url: https://skills.sh/lingzhi227/agent-research-skills/paper-compilation
---

# paper-compilation

skills/lingzhi227/agent-research-skills/paper-compilation
paper-compilation
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill paper-compilation
SKILL.md
Paper Compilation

Compile a LaTeX paper to PDF with error detection and correction.

Input
$ARGUMENTS — Path to the main .tex file
Scripts
Compile paper
python ~/.claude/skills/paper-compilation/scripts/compile_paper.py paper/main.tex
python ~/.claude/skills/paper-compilation/scripts/compile_paper.py paper/main.tex --check-style
python ~/.claude/skills/paper-compilation/scripts/compile_paper.py paper/main.tex --output paper/output.pdf


Reports: compilation status, page count, warnings, citation/reference stats, style issues.

Validate citations before compiling
python ~/.claude/skills/citation-management/scripts/validate_citations.py \
  --tex paper/main.tex --bib paper/references.bib --check-figures --figures-dir paper/figures/

Auto-fix LaTeX errors
python ~/.claude/skills/paper-compilation/scripts/fix_latex_errors.py \
  --tex paper/main.tex --log compile.log --output paper/main_fixed.tex


Fixes: HTML tags in LaTeX, mismatched environments, missing figures. Key flags: --dry-run, --auto-detect

Compile with auto-fix retry
python ~/.claude/skills/paper-compilation/scripts/compile_paper.py paper/main.tex --auto-fix


Runs fix_latex_errors.py + recompile up to 3 rounds until compilation succeeds.

Workflow
Step 1: Pre-Compilation Validation

Run validate_citations.py to catch issues before compiling:

Every \cite{key} has a matching .bib entry
Every \includegraphics{file} exists
No duplicate labels or sections
Step 2: Compile

Run compile_paper.py which executes: pdflatex → bibtex → pdflatex → pdflatex

Step 3: Error Correction Loop (up to 5 rounds)

If compilation fails, read the error output and fix:

! Undefined control sequence → Add missing package or fix typo
! Missing $ inserted → Wrap math in $...$
! Missing } inserted → Fix unmatched brace
Citation 'key' undefined → Add to .bib or fix \cite
</end{figure}> → Replace with \end{figure} (HTML syntax in LaTeX)

Apply minimal fixes. Do not remove packages unnecessarily. Recompile after each fix.

Step 4: Post-Compilation Report

Check: page count vs venue limit, remaining warnings, chktex style issues.

Troubleshooting
pdflatex not found
# macOS
brew install --cask mactex-no-gui
# Ubuntu
sudo apt install texlive-full

Alternative: latexmk (auto-handles multiple passes)
latexmk -pdf -interaction=nonstopmode main.tex

Related Skills
Upstream: latex-formatting, citation-management, figure-generation, table-generation
Downstream: self-review
See also: paper-assembly
Weekly Installs
129
Repository
lingzhi227/agen…h-skills
GitHub Stars
42
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass