---
rating: ⭐⭐
title: figure-generation
url: https://skills.sh/lingzhi227/agent-research-skills/figure-generation
---

# figure-generation

skills/lingzhi227/agent-research-skills/figure-generation
figure-generation
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill figure-generation
SKILL.md
Scientific Figure Generation

Generate publication-quality figures for research papers.

Input
$0 — Description of the desired figure
$1 — (Optional) Path to data file (CSV, JSON, NPY, PKL) or results directory
Scripts
Generate figure template
python ~/.claude/skills/figure-generation/scripts/figure_template.py --type bar --output figure_script.py --name comparison
python ~/.claude/skills/figure-generation/scripts/figure_template.py --list-types


Available types: bar, training-curve, heatmap, ablation, line, scatter, radar, violin, tsne, attention

Three-Phase Pipeline (from MatPlotAgent)
Phase 1: Query Expansion

Expand the user's figure description into step-by-step coding specifications using the prompts in references/figure-prompts.md. Determine: figure type, data mapping (x/y/color/hue), style requirements, paper conventions.

Phase 2: Code Generation with Execution Loop (up to 4 retries)
Generate a self-contained Python script using the template from scripts/figure_template.py as a starting point
Write script to a temp file and execute: python figure_script.py
If error: capture traceback, feed back, regenerate (see ERROR_PROMPT in references)
If no .png produced: add explicit save instruction, retry
On success: report the generated figure path
Phase 3: Visual Refinement

Read the generated PNG file and visually inspect using the VLM feedback prompts from references/figure-prompts.md:

Does the figure type match the request?
Are labels, titles, and legends correct?
Is the color scheme appropriate and consistent?
Are axis scales sensible? Is text readable at publication size?

If improvements needed: generate corrective instructions and re-execute.

References
All MatPlotAgent prompts: ~/.claude/skills/figure-generation/references/figure-prompts.md
Figure templates: ~/.claude/skills/figure-generation/scripts/figure_template.py
Output

Both PNG (preview, 300 DPI) and PDF (vector, for paper) formats. Plus the LaTeX include code:

\begin{figure}[t]
    \centering
    \includegraphics[width=\linewidth]{figures/figure_name.pdf}
    \caption{Description. Best viewed in color.}
    \label{fig:figure_name}
\end{figure}

Quality Requirements
DPI ≥ 300, or vector PDF
Colorblind-friendly palette (no red-green only)
All text ≥ 8pt at print size
Consistent styling across all paper figures
No matplotlib default title — use LaTeX caption
Related Skills
Upstream: data-analysis, experiment-code
Downstream: paper-writing-section, paper-compilation, slide-generation
See also: table-generation
Weekly Installs
142
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