---
title: arxiv-paper-translator
url: https://skills.sh/yrom/arxiv-paper-translator/arxiv-paper-translator
---

# arxiv-paper-translator

skills/yrom/arxiv-paper-translator/arxiv-paper-translator
arxiv-paper-translator
Installation
$ npx skills add https://github.com/yrom/arxiv-paper-translator --skill arxiv-paper-translator
SKILL.md
arXiv Paper Translator

Translate academic papers from arXiv by downloading LaTeX source, translating content while preserving structure, and generating translated PDFs with technical reports.

Workflow Overview
Download & Extract - Get LaTeX source from arXiv
Translate - Translate English narrative content to Chinese following LaTeX-specific rules
REVIEW PHASE - MUST COMPLETE before compiling
CJK Support & Localize Labels - Add xeCJK, localize labels
Compile .tex Files - Generate translated PDF using XeLaTeX
Report - Create technical summary document
Prerequisites

Check local xelatex installation:

xelatex --version


If not installed, make sure Docker is installed and available.

docker --version


This skill requires XeLaTeX to compile translated PDFs. If not installed locally, Docker will be used instead.

Recommend using xu-cheng/latex-docker Docker images.

e.g. Tex Live full distribution (only linux/amd64):

# NOTICE: ghcr.1ms.run is a mirror of ghcr.io.
docker pull ghcr.1ms.run/xu-cheng/texlive-debian:20260101 --platform linux/amd64
# => docker pull ghcr.io/xu-cheng/latex-debian:20260101 --platform linux/amd64


If both local XeLaTeX and Docker are not installed, then STOP trying to run this skill. And Ask user question: "XeLaTeX or Docker is required to compile translated PDFs. Which one do you want to use? I'll help you to setup."

Step 1: Download LaTeX Source

Extract ARXIV_ID from user input.

Download and extract source code from arXiv:

# Download LaTeX source (replace ARXIV_ID with user-specified paper ID)
ARXIV_ID="2206.04655"
mkdir -p arXiv_${ARXIV_ID}
wget -q https://arxiv.org/e-print/${ARXIV_ID} -O arXiv_${ARXIV_ID}/paper_source.tar.gz
mkdir -p arXiv_${ARXIV_ID}/paper_source
tar -xzf arXiv_${ARXIV_ID}/paper_source.tar.gz -C arXiv_${ARXIV_ID}/paper_source


Verify extraction:

# List files to understand structure
tree arXiv_${ARXIV_ID}/paper_source

Step 2: Translate LaTeX Files

IMPORTANT: Before translating, read references/translation_guidelines.md for detailed rules.

Translation Workflow

Step 2.1. Copy all files from paper_source/ to paper_cn/:

Option 1 - Using cp (standard):

cd arXiv_${ARXIV_ID}
mkdir -p paper_cn
cp -r paper_source/* paper_cn/


Option 2 - Using rsync (better for incremental sync):

cd arXiv_${ARXIV_ID}
mkdir -p paper_cn
rsync -av paper_source/ paper_cn/


All .tex files in paper_cn/ will be translated in-place later.

Step 2.2. Gather Context (MANDATORY):

Before ANY translation, you MUST extract:

Paper Title: From \title{...} in main file
Abstract: From \begin{abstract}...\end{abstract} or \abstract{...} in main file
Paper Structure: List all sections and which .tex file contains each
Key Terminologies: Build terminology table from paper content

For some glossaries or terminologies you don't know how to translate, you can ASK user question for definition.

This information is REQUIRED for translation tasks.

Read references/translation_prompt.md for the prompt template.

Step 2.3. Dispatch Translation Tasks

Identify files to translate:

Find main file (contains \documentclass{...}, usually main.tex, paper.tex, template.tex, etc.)
Filter .tex files that need translation (skip macro-only files if any, or user specified files)
Create list of files to translate

Translation Strategy:

Translate main file first (sequential)

Builds shared terminology context
Ensures consistency for other files

Translate other files:

If 3+ files: Dispatch in parallel
If 1-2 files: Sequential translation

Each translation Task:

Task type: general-purpose subagent
Input: File path in paper_cn/ directory
Action: Read file → Translate → Edit file (Update file content with translated text)
Must follow references/translation_prompt.md
Must use gathered context (title, abstract, structure, terminologies)

Example command to find main .tex file:

find paper_cn/ -name "*.tex" -exec grep -l '\\documentclass' {} \; | head -1

Step 3: Review Translation

After all translation Tasks are completed, you MUST review the translated content following references/review_checklist.md to verify:

File Completeness Check
LaTeX Command Spelling
CJK Catcode Issues
Translation Quality Check
Content Spot-Check

Perform fixes as needed based on review findings.

CRITICAL: Before proceeding to Step 4, you must confirm:

 All review checks completed
 Any issues identified and fixed
 Translation quality verified
Step 4: Add Chinese Support

IMPORTANT: Follow references/chinese_support.md to configure CJK fonts and localize labels.

Modify main .tex file to include xeCJK package and set CJK fonts.

e.g. for Fandol font (which is included in TexLive Docker image):

\usepackage{xeCJK}
\setCJKmainfont{FandolSong}[ItalicFont=FandolKai]  % 宋体 - 正文，\emph 用楷体
\setCJKsansfont{FandolHei}    % 黑体 - 标题、\textsf
\setCJKmonofont{FandolFang}   % 仿宋 - 代码、\texttt


If running locally, Ask user for font preference before configuring. Check available fonts with fc-list :lang=zh family.

Step 5: Compile Translated PDF
Option 1: Local XeLaTeX
# Basic compilation
xelatex main.tex

# If paper has bibliography (recommended approach)
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex


Or use latexmk for automated compilation:

latexmk -xelatex main.tex

Option 2: Docker with TeX Live
# change working directory to arXiv_${ARXIV_ID}
cd /path/to/arXiv_${ARXIV_ID}
docker run --rm \
  -v "$(pwd)/paper_cn":/workspace \
  -w /workspace \
  ghcr.1ms.run/xu-cheng/texlive-debian:20260101 \
  latexmk -xelatex main.tex

Step 6: Generate Technical Report

If user requests a technical summary, spawn a subagent following references/summary_prompt.md to create a technical summary using assets/report_template.md.

Save report: arXiv_${ARXIV_ID}/technical_report.md

Final Deliverables
Translated PDF: paper_cn/<main-file>.pdf
Technical report: arXiv_${ARXIV_ID}/technical_report.md
TeX Source: paper_cn/ directory with all translated LaTeX files
Common Issues & Solutions
Issue	Solution
Downloaded file is single .tex, not .tar.gz	mv paper_source.tar.gz paper_source.tex and create directory
Main file not named main.tex	find . -name "*.tex" -exec grep -l "\\documentclass" {} \;
Compilation fails with encoding error	file *.tex to check, iconv -f ISO-8859-1 -t UTF-8 to convert
Command misspelling (e.g. \footnotext)	See review checklist step 2 — diff command sets to find typos
Undefined control sequence - \xmax概率	xeCJK catcode issue — insert {} to separate custom macro from CJK text → \xmax{}概率
Undefined control sequence - \chinese{弋}	Original uses CJK package's \chinese macro; add \newcommand{\chinese}[1]{#1} after xeCJK config to prevent catcode issue
Custom .sty/.cls files	Copy to paper_cn/, check for hard-coded English text
Missing $ inserted in translated tables	Mixed CJK/Latin characters may cause xeCJK font switching errors (e.g. (xyz) be treated as math mode), restore original content in table cells
Undefined references (e.g., \ref{fig:joint-train})	Ensure ALL referenced files are present in paper_cn/, even if NOT translated files.
References
Translation rules: references/translation_guidelines.md
Translation prompt: references/translation_prompt.md
Review checklist: references/review_checklist.md
Chinese support: references/chinese_support.md
Report template: assets/report_template.md
Makefile template (optional): assets/Makefile.template
Weekly Installs
189
Repository
yrom/arxiv-pape…anslator
GitHub Stars
17
First Seen
Feb 12, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn