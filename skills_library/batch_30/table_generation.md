---
title: table-generation
url: https://skills.sh/lingzhi227/agent-research-skills/table-generation
---

# table-generation

skills/lingzhi227/agent-research-skills/table-generation
table-generation
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill table-generation
SKILL.md
Table Generation

Convert experimental results into publication-ready LaTeX tables.

Input
$0 — Table type: comparison, ablation, descriptive, custom
$1 — Data source: JSON file, CSV file, or inline data
Scripts
Generate LaTeX table from JSON/CSV
python ~/.claude/skills/table-generation/scripts/results_to_table.py \
  --input results.json --type comparison \
  --bold-best max --caption "Performance comparison" \
  --label tab:main_results


Supports: comparison, ablation, descriptive, multi-dataset table types. Additional flags: --type multi-dataset for methods x datasets x metrics layout, --significance for p-value stars, --underline-second for second-best results.

References
LaTeX table templates and examples: ~/.claude/skills/table-generation/references/table-templates.md
Table Types
comparison — Main results table
Rows = methods (baselines + ours), Columns = metrics/datasets
Bold the best result in each column
Include mean +/- std when available
Use \multirow for method categories (Supervised, Self-supervised, etc.)
ablation — Ablation study table
Rows = variants (full model, minus component A, minus component B, ...)
Columns = metrics
Bold the full model result
Use checkmarks for component presence
descriptive — Dataset/statistics table
Dataset characteristics, hyperparameters, or summary statistics
Clean formatting with proper units
custom — Free-form table
User specifies layout and content
Required Packages
\usepackage{booktabs}    % \toprule, \midrule, \bottomrule
\usepackage{multirow}    % \multirow
\usepackage{multicol}    % multi-column layouts
\usepackage{threeparttable}  % table notes

Output Format

Always generate tables with:

booktabs rules (\toprule, \midrule, \bottomrule)
\caption{} and \label{tab:...}
Bold best results using \textbf{}
Table notes via threeparttable when needed
Proper alignment (l for text, c or r for numbers)
Rules
Only include numbers from actual experimental logs — never hallucinate results
All numbers must match the data source exactly
Use $\pm$ for standard deviations
Use \underline{} for second-best results when appropriate
Keep tables compact — avoid unnecessary columns
Use table* for wide tables spanning two columns
Add glossary/notes for abbreviated column headers
Related Skills
Upstream: data-analysis, experiment-code
Downstream: paper-writing-section, paper-compilation
See also: figure-generation
Weekly Installs
135
Repository
lingzhi227/agen…h-skills
GitHub Stars
42
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass