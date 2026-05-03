---
title: latex-tables
url: https://skills.sh/terrylica/cc-skills/latex-tables
---

# latex-tables

skills/terrylica/cc-skills/latex-tables
latex-tables
Installation
$ npx skills add https://github.com/terrylica/cc-skills --skill latex-tables
SKILL.md
LaTeX Tables with tabularray

Self-Evolving Skill: This skill improves through use. If instructions are wrong, parameters drifted, or a workaround was needed — fix this file immediately, don't defer. Only update for real, reproducible issues.

When to Use This Skill

Use this skill when:

Creating tables with fixed-width columns
Formatting complex table layouts
Need precise column alignment
Migrating from tabular/tabularx/longtable/booktabs
Troubleshooting table overflow issues
Quick Reference
Why tabularray?

Modern LaTeX3 package (replaces old solutions):

Fixed-width columns with proper alignment
Clean, consistent syntax
Replaces: tabular, tabularx, longtable, booktabs
Better performance than legacy packages
Part of TeX Live 2025
Installation
# Check if installed
kpsewhich tabularray.sty

# If not found, install:
sudo tlmgr install tabularray

Basic Usage
\documentclass{article}
\usepackage{tabularray}  % Modern table package

\begin{document}
% Simple table
\begin{tblr}{colspec={ccc}, hlines, vlines}
  Header 1 & Header 2 & Header 3 \\
  Data 1   & Data 2   & Data 3   \\
\end{tblr}
\end{document}

Quick Reference Card
% Minimal table
\begin{tblr}{colspec={ccc}}
  A & B & C \\
\end{tblr}

% With all lines
\begin{tblr}{colspec={ccc}, hlines, vlines}
  A & B & C \\
\end{tblr}

% Fixed widths
\begin{tblr}{colspec={Q[2cm] Q[3cm] Q[2cm]}, hlines}
  A & B & C \\
\end{tblr}

% Bold header
\begin{tblr}{
  colspec={ccc},
  row{1}={font=\bfseries}
}
  Header & Header & Header \\
  Data   & Data   & Data   \\
\end{tblr}

Best Practices
Use Q[width] for fixed columns instead of p{width}
Specify widths explicitly when text might overflow
Use X for flexible columns that should expand
Style headers with row{1} instead of manual formatting
Use colspec for column properties, not inline commands
Check package version: kpsewhich tabularray.sty (should be recent)
Reference Documentation

For detailed information, see:

Table Patterns - 5 common table patterns with examples
Column Specification - Alignment options and width control
Lines and Borders - All lines, selective lines, thick lines
Troubleshooting - Table too wide, text not wrapping, alignment issues
Migration - Migrating from tabular and tabularx

Official Docs: Run texdoc tabularray for complete package documentation

See Also:

Use latex/setup skill for installing tabularray package
Use latex/build skill for compilation workflows
Troubleshooting
Issue	Cause	Solution
Package not found	tabularray not installed	sudo tlmgr install tabularray
Table too wide	Fixed widths exceed page	Use smaller Q[width] values or X for flexible
Text not wrapping	Column spec missing width	Use Q[width] instead of c/l/r for wrapping
Alignment issues	Mixed column types	Ensure all columns have consistent spec
Compile error on colspec	Invalid syntax	Check for missing commas or typos in column spec
hlines not appearing	Missing from spec	Add hlines to the spec: {colspec={...}, hlines}
Row style not applied	Wrong row index	Remember row{1} is first row (1-indexed)
Package version too old	TeX Live outdated	sudo tlmgr update --self --all
Post-Execution Reflection

After this skill completes, check before closing:

Did the command succeed? — If not, fix the instruction or error table that caused the failure.
Did parameters or output change? — If the underlying tool's interface drifted, update Usage examples and Parameters table to match.
Was a workaround needed? — If you had to improvise (different flags, extra steps), update this SKILL.md so the next invocation doesn't need the same workaround.

Only update if the issue is real and reproducible — not speculative.

Weekly Installs
156
Repository
terrylica/cc-skills
GitHub Stars
39
First Seen
5 days ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn