---
rating: ⭐⭐
title: visual-audit
url: https://skills.sh/pedrohcgs/claude-code-my-workflow/visual-audit
---

# visual-audit

skills/pedrohcgs/claude-code-my-workflow/visual-audit
visual-audit
Installation
$ npx skills add https://github.com/pedrohcgs/claude-code-my-workflow --skill visual-audit
SKILL.md
Visual Audit of Slide Deck

Perform a thorough visual layout audit of a slide deck.

Steps

Read the slide file specified in $ARGUMENTS

For Quarto (.qmd) files:

Render with quarto render Quarto/$ARGUMENTS
Open in browser to inspect each slide

For Beamer (.tex) files:

Compile and check for overfull hbox warnings

Audit every slide for:

OVERFLOW: Content exceeding slide boundaries FONT CONSISTENCY: Inline font-size overrides, inconsistent sizes BOX FATIGUE: 2+ colored boxes on one slide, wrong box types SPACING: Missing negative margins, missing fig-align LAYOUT: Missing transitions, missing framing sentences, semantic colors

Produce a report organized by slide with severity and recommendations

Follow the spacing-first principle:

Reduce vertical spacing with negative margins
Consolidate lists
Move displayed equations inline
Reduce image/SVG size
Last resort: font size reduction (never below 0.85em)
Weekly Installs
17
Repository
pedrohcgs/claud…workflow
GitHub Stars
1.0K
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass