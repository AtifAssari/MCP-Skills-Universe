---
title: nature-figure
url: https://skills.sh/yuan1z0825/nature-skills/nature-figure
---

# nature-figure

skills/yuan1z0825/nature-skills/nature-figure
nature-figure
Installation
$ npx skills add https://github.com/yuan1z0825/nature-skills --skill nature-figure
SKILL.md
Nature Figure Making Skill

A complete guide for producing publication-quality matplotlib figures matching Nature journal standards. Derived from the figures4papers repository (papers published in Nature Machine Intelligence and top ML venues), then extended with direct visual observations from a 2026 Nature sample spanning materials science, genomics, neuroscience, plant biology and clinical studies.

Color policy: prefer unified method families across all panels over maximal hue separation. For dense Nature Machine Intelligence-style figure pages, use the low-saturation NMI pastel family described in references/api.md and reserve green/red mainly for gains, drops, and other directional cues.

Quick-start: Mandatory rcParams

Always apply these at the top of every script:

import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['svg.fonttype'] = 'none'          # editable text in SVG/PDF
plt.rcParams['font.size'] = 16                 # 24 for large bar panels
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.linewidth'] = 2.5           # 3 for big bars, 2 for compact
plt.rcParams['legend.frameon'] = False


Use text.usetex = True only when LaTeX is installed and math-rich labels are required.

Default operating stance
Start by classifying the requested figure into one of four archetypes: quantitative grid, schematic-led composite, image plate + quant, or asymmetric mixed-modality figure.
Prefer one hero panel plus subordinate evidence panels over filling the canvas with equal-sized subplots.
Keep the background white for plots and diagrams; switch to black only for microscopy / volume-rendering image plates.
Prefer direct labels over legends when categories are spatially fixed or the legend would force unnecessary eye travel.
Keep one restrained palette per figure: usually one neutral family, one signal family, and one accent family.
When the user asks for broad Nature style rather than ML/NMI-specific style, read references/nature-2026-observations.md before choosing layout.
When to load this skill
Matplotlib figures for papers, slides, or reports targeting Nature, NeurIPS, ICLR, or similar venues.
Requests involving grouped bars, trend lines, heatmaps, radar plots, multi-panel grids, or PDF/SVG/high-DPI output.
Any mention of "Nature style", "publication figure", "paper figure", or "high-quality scientific plot".
When NOT to load
Plotly, Altair, Bokeh, or other interactive/web-first plotting.
EDA-only plots without a publication target.
Primary workflow is 3D, GIS, or non-matplotlib tooling.
Illustrator / Figma–first layout.
Related files
File	Open when
references/design-theory.md	Typography, color theory, layout rationale, export policy
references/api.md	PALETTE, helper function signatures, validation rules
references/common-patterns.md	Ultra-wide panels, legend-only axes, print-safe bars
references/nature-2026-observations.md	Real Nature page archetypes: schematic-led composites, dark image plates, clinical triptychs, asymmetric hero layouts
references/tutorials.md	End-to-end walkthroughs: bars, trends, heatmaps
references/chart-types.md	Radar, 3D sphere, fill_between, scatter patterns
Weekly Installs
22
Repository
yuan1z0825/nature-skills
GitHub Stars
733
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass