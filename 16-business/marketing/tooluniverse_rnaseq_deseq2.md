---
title: tooluniverse-rnaseq-deseq2
url: https://skills.sh/mims-harvard/tooluniverse/tooluniverse-rnaseq-deseq2
---

# tooluniverse-rnaseq-deseq2

skills/mims-harvard/tooluniverse/tooluniverse-rnaseq-deseq2
tooluniverse-rnaseq-deseq2
Installation
$ npx skills add https://github.com/mims-harvard/tooluniverse --skill tooluniverse-rnaseq-deseq2
SKILL.md
RNA-seq Differential Expression Analysis (DESeq2)

Differential expression analysis of RNA-seq count data using PyDESeq2, with enrichment analysis (gseapy) and gene annotation via ToolUniverse.

BixBench Coverage: Validated on 53 BixBench questions across 15 computational biology projects.

Domain Reasoning

DESeq2 assumes that most genes are NOT differentially expressed — this is its normalization assumption. If this assumption is violated (e.g., global transcriptional shutdown, where the majority of genes genuinely decrease), size factor normalization will inflate expression in the treatment group and produce artifactually upregulated genes. Always check the MA plot: the fold-change cloud should be centered on zero across all expression levels. A systematic upward or downward shift indicates a normalization problem, not biology.

LOOK UP DON'T GUESS
Gene identifiers and annotations: use ToolUniverse annotation tools (MyGene_query_genes, UniProt); do not recall gene function or pathway from memory.
Enriched pathways: run gseapy or equivalent on the actual DEG list; do not list expected pathways.
Design formula factors: inspect metadata.columns and metadata[factor].unique() from the actual data; do not assume metadata structure.
DEG thresholds: apply the values specified by the user (padj, log2FC, baseMean); do not substitute defaults without checking the question.
Core Principles
Data-first - Load and validate count data and metadata BEFORE any analysis
Statistical rigor - Proper normalization, dispersion estimation, multiple testing correction
Flexible design - Single-factor, multi-factor, and interaction designs
Threshold awareness - Apply user-specified thresholds exactly (padj, log2FC, baseMean)
Reproducible - Set random seeds, document all parameters
Question-driven - Parse what the user is actually asking; extract the specific answer
Enrichment integration - Chain DESeq2 results into pathway/GO enrichment when requested
When to Use
RNA-seq count matrices needing differential expression analysis
DESeq2, DEGs, padj, log2FC questions
Dispersion estimates or diagnostics
GO, KEGG, Reactome enrichment on DEGs
Specific gene expression changes between conditions
Batch effect correction in RNA-seq
Required Packages
import pandas as pd, numpy as np
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import gseapy as gp          # enrichment (optional)
from tooluniverse import ToolUniverse  # annotation (optional)

Analysis Workflow
Step 1: Parse the Question

Extract: data files, thresholds (padj/log2FC/baseMean), design factors, contrast, direction, enrichment type, specific genes. See question_parsing.md.

Step 2: Load & Validate Data

Load counts + metadata, ensure samples-as-rows/genes-as-columns, verify integer counts, align sample names, remove zero-count genes. See data_loading.md.

Step 2.5: Inspect Metadata (REQUIRED)

List ALL metadata columns and levels. Categorize as biological interest vs batch/block. Build design formula with covariates first, factor of interest last. See design_formula_guide.md.

Step 3: Run PyDESeq2

Set reference level via pd.Categorical, create DeseqDataSet, call dds.deseq2(), extract DeseqStats with contrast, run Wald test, optionally apply LFC shrinkage. See pydeseq2_workflow.md.

Tool boundaries:

Python (PyDESeq2): ALL DESeq2 analysis
ToolUniverse: ONLY gene annotation (ID conversion, pathway context)
gseapy: Enrichment analysis (GO/KEGG/Reactome)
Step 4: Filter Results

Apply padj, log2FC, baseMean thresholds. Split by direction if needed. See result_filtering.md.

Step 5: Dispersion Analysis (if asked)

Key columns: genewise_dispersions, fitted_dispersions, MAP_dispersions, dispersions. See dispersion_analysis.md.

Step 6: Enrichment (optional)

Use gseapy enrich() with appropriate gene set library. See enrichment_analysis.md.

Step 7: Gene Annotation (optional)

Use ToolUniverse for ID conversion and gene context only. See output_formatting.md.

Common Patterns
Pattern	Type	Key Operation
1	DEG count	len(results[(padj<0.05) & (abs(lfc)>0.5)])
2	Gene value	results.loc['GENE', 'log2FoldChange']
3	Direction	Filter log2FoldChange > 0 or < 0
4	Set ops	degs_A - degs_B for unique DEGs
5	Dispersion	(dds.var['genewise_dispersions'] < thr).sum()

See bixbench_examples.md for all 10 patterns with examples.

Error Quick Reference
Error	Fix
No matching samples	Transpose counts; strip whitespace
Dispersion trend no converge	fit_type='mean'
Contrast not found	Check metadata['factor'].unique()
Non-integer counts	Round to int OR use t-test
NaN in padj	Independent filtering removed genes

See troubleshooting.md for full debugging guide.

Interpretation Framework
DESeq2 Result Interpretation
Metric	Threshold	Interpretation
padj	< 0.05	Statistically significant after multiple testing correction
log2FoldChange	> 1 or < -1	Biologically meaningful fold change (2x up or down)
baseMean	> 10	Gene is expressed at detectable levels
lfcSE	< 1.0	Fold change estimate is precise
Evidence Grading for DEGs
Grade	Criteria	Action
Strong DEG	padj < 0.01,	LFC
Moderate DEG	padj < 0.05,	LFC
Weak DEG	padj < 0.1 or	LFC
Not significant	padj >= 0.1	Do not report as differentially expressed
Synthesis Questions
How many DEGs and in which direction? (up vs down ratio indicates biological response type)
What pathways are enriched? (GO/KEGG enrichment of DEGs reveals mechanism)
Are the top DEGs biologically plausible? (known markers for the condition?)
Is the fold change magnitude realistic? (LFC > 5 is unusual; check for outlier-driven effects)
Are there batch effects? (PCA should separate by condition, not by batch)
Known Limitations
PyDESeq2 vs R DESeq2: Numerical differences exist for very low dispersion genes (<1e-05). For exact R reproducibility, use rpy2.
gseapy vs R clusterProfiler: Results may differ. See r_clusterprofiler_guide.md.
Reference Files
question_parsing.md - Extract parameters from questions
data_loading.md - Data loading and validation
design_formula_guide.md - Multi-factor design decision tree
pydeseq2_workflow.md - Complete PyDESeq2 code examples
result_filtering.md - Advanced filtering and extraction
dispersion_analysis.md - Dispersion diagnostics
enrichment_analysis.md - GO/KEGG/Reactome workflows
output_formatting.md - Format answers correctly
bixbench_examples.md - All 10 question patterns
troubleshooting.md - Common issues and debugging
r_clusterprofiler_guide.md - R clusterProfiler via rpy2
Utility Scripts
format_deseq2_output.py - Output formatters
load_count_matrix.py - Data loading utilities
Weekly Installs
185
Repository
mims-harvard/to…universe
GitHub Stars
1.3K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass