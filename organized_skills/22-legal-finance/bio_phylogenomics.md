---
rating: ⭐⭐
title: bio-phylogenomics
url: https://skills.sh/fmschulz/omics-skills/bio-phylogenomics
---

# bio-phylogenomics

skills/fmschulz/omics-skills/bio-phylogenomics
bio-phylogenomics
Installation
$ npx skills add https://github.com/fmschulz/omics-skills --skill bio-phylogenomics
SKILL.md
Bio Phylogenomics

Build marker gene alignments and phylogenetic trees.

Instructions
Extract marker genes or SSU rRNA sequences.
Align and trim sequences using project-standard workflows.
Build ML trees with bootstraps:
Standard accuracy: Use IQ-TREE (comprehensive model selection, publication-quality)
Fast mode: Use IQ-TREE -fast (exploratory analysis, large datasets >10K sequences)
Very large datasets: Use VeryFastTree (>100K sequences, ultra-fast)
Post-process trees with ETE Toolkit:
Calculate tree statistics (branch lengths, distances, topology metrics)
Root, prune, or collapse nodes as needed
Filter by bootstrap support values
Add taxonomic or trait annotations
Generate publication-quality visualizations
Quick Reference
Task	Action
Run workflow	Follow the steps in this skill and capture outputs.
Validate inputs	Confirm required inputs and reference data exist.
Review outputs	Inspect reports and QC gates before proceeding.
Tool docs	See docs/README.md.
References	- See ../bio-skills-references.md
Input Requirements

Prerequisites:

Tools available in the active environment (Pixi/conda/system). See docs/README.md for expected tools.
Marker gene set or alignments available. Inputs:
markers.faa (marker genes) or alignments.fasta
Output
results/bio-phylogenomics/alignments/
results/bio-phylogenomics/trees/
results/bio-phylogenomics/phylo_report.md
results/bio-phylogenomics/logs/
Quality Gates
 Alignment length and missingness meet project thresholds.
 Bootstrap support summary meets project thresholds.
 On failure: retry with alternative parameters; if still failing, record in report and exit non-zero.
 Verify markers.faa is non-empty and aligned sequences are consistent.
Examples
Example 1: Expected input layout
markers.faa (marker genes) or alignments.fasta

Troubleshooting

Issue: Missing inputs or reference databases Solution: Verify paths and permissions before running the workflow.

Issue: Low-quality results or failed QC gates Solution: Review reports, adjust parameters, and re-run the affected step.

Weekly Installs
19
Repository
fmschulz/omics-skills
GitHub Stars
1
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass