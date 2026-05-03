---
rating: ⭐⭐⭐
title: typst-creator
url: https://skills.sh/buyoung/skills/typst-creator
---

# typst-creator

skills/buyoung/skills/typst-creator
typst-creator
Installation
$ npx skills add https://github.com/buyoung/skills --skill typst-creator
SKILL.md
Typst Document Creation Capability

This skill enables the agent to create Typst documents with correct syntax, styling, and mathematical formulas.

Version: Based on Typst v0.14.2

Core Capability
Function: Generate Typst source code for documents, reports, papers, and presentations
Output Format: .typ files with proper Typst syntax
Modes: Markup, Math, and Code modes
Typst Syntax Overview
Mode	Entry Syntax	Purpose
Markup	Default	Text, headings, lists, emphasis
Math	$...$	Mathematical formulas
Code	# prefix	Variables, functions, logic
Domain Knowledge
Topic	Reference
Syntax	Markup, math, and code mode syntax. See ./references/syntax.md
Styling	Set rules and show rules for styling. See ./references/styling.md
Scripting	Variables, functions, control flow. See ./references/scripting.md
Math	Mathematical notation and symbols. See ./references/math.md
Layout	Page setup, grids, alignment. See ./references/layout.md
Key Differences from LaTeX
Feature	LaTeX	Typst
Bold	\textbf{text}	*text*
Italic	\textit{text}	_text_
Heading	\section{Title}	= Title
Fraction	\frac{a}{b}	a/b or frac(a, b)
Function call	\func{arg}	#func(arg)
Set property	preamble commands	#set func(prop: value)
Constraints
File Extension: Output files use .typ extension
Unicode Support: Typst natively supports Unicode symbols
No Packages Required: Most features are built-in (unlike LaTeX)
Weekly Installs
19
Repository
buyoung/skills
GitHub Stars
12
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass