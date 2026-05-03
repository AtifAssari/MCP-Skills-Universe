---
rating: ⭐⭐
title: slide-generation
url: https://skills.sh/lingzhi227/agent-research-skills/slide-generation
---

# slide-generation

skills/lingzhi227/agent-research-skills/slide-generation
slide-generation
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill slide-generation
SKILL.md
Slide Generation

Convert a completed paper into presentation slides or poster.

Input
$0 — Paper LaTeX file (main.tex) or paper directory
References
Slide templates and layout patterns: ~/.claude/skills/slide-generation/references/slide-templates.md
Scripts
Extract paper elements for slides
python ~/.claude/skills/slide-generation/scripts/extract_paper_elements.py --tex main.tex --output slides_skeleton.tex
python ~/.claude/skills/slide-generation/scripts/extract_paper_elements.py --tex main.tex --format json --output elements.json
python ~/.claude/skills/slide-generation/scripts/extract_paper_elements.py --tex main.tex --output slides.tex --theme metropolis


Parses .tex, extracts title/authors/sections/equations/figures/tables, generates Beamer skeleton.

Workflow
Step 1: Extract Key Content

From the paper, extract:

Title, authors, affiliations
Core contribution (1-3 bullet points from abstract)
Key figures (all \includegraphics paths)
Key tables (simplified versions)
Key equations (numbered equations from Methods)
Main results (best numbers from Results section)
Step 2: Design Slide Structure

Standard oral presentation flow (~15-20 slides):

Slide #	Content	Source Section
1	Title slide	Title/Authors
2	Motivation / Problem	Introduction
3	Why existing solutions fail	Related Work
4-5	Our approach (high-level)	Methods
6-8	Technical details + equations	Methods
9	Experimental setup	Experiments
10-13	Results (figures + tables)	Results
14	Ablation study	Results
15	Limitations & Future work	Discussion
16	Conclusion	Conclusion
17	Thank you + Q&A	—
Step 3: Generate Beamer LaTeX
\documentclass[aspectratio=169]{beamer}
\usetheme{metropolis}
\title{Paper Title}
\author{Authors}
\date{Venue Year}

\begin{document}
\maketitle

\begin{frame}{Motivation}
\begin{itemize}
    \item Problem statement
    \item Why it matters
\end{itemize}
\end{frame}

% ... more frames
\end{document}

Step 4: Simplify for Presentation
Tables: reduce to essential rows/columns
Equations: show only the key insight, not full derivation
Figures: use largest versions, add annotations
Text: bullet points only, no paragraphs
Step 5: Generate Poster Layout (Optional)

For poster sessions, use a multi-column layout:

Column 1: Introduction + Motivation
Column 2: Methods + Key Equations
Column 3: Results + Figures
Column 4: Conclusions + References
Rules
Maximum 1 key message per slide
Figures should be large and readable
No more than 6 bullet points per slide
Equations should be simplified versions
Include slide numbers
Use consistent color scheme matching the paper's figures
Presentation should be self-contained (understandable without reading the paper)
Related Skills
Upstream: paper-compilation, figure-generation
See also: self-review, paper-assembly
Weekly Installs
122
Repository
lingzhi227/agen…h-skills
GitHub Stars
42
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass