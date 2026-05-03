---
rating: ⭐⭐⭐
title: bulk-wgcna-analysis-with-omicverse
url: https://skills.sh/starlitnightly/omicverse/bulk-wgcna-analysis-with-omicverse
---

# bulk-wgcna-analysis-with-omicverse

skills/starlitnightly/omicverse/bulk-wgcna-analysis-with-omicverse
bulk-wgcna-analysis-with-omicverse
Installation
$ npx skills add https://github.com/starlitnightly/omicverse --skill bulk-wgcna-analysis-with-omicverse
SKILL.md
Bulk WGCNA analysis with omicverse
Overview

Activate this skill for users who want to reproduce the WGCNA workflow from t_wgcna.ipynb. It guides you through loading expression data, configuring PyWGCNA, constructing weighted gene co-expression networks, and inspecting modules of interest.

Instructions
Prepare the environment
Import omicverse as ov, scanpy as sc, matplotlib.pyplot as plt, and pandas as pd.
Set plotting defaults via ov.plot_set().
Load and filter expression data
Read expression matrices (e.g., from expressionList.csv).
Calculate median absolute deviation with from statsmodels import robust and gene_mad = data.apply(robust.mad).
Keep the top variable genes (e.g., data = data.T.loc[gene_mad.sort_values(ascending=False).index[:2000]]).
Initialise PyWGCNA
Create pyWGCNA_5xFAD = ov.bulk.pyWGCNA(name=..., species='mus musculus', geneExp=data.T, outputPath='', save=True).
Confirm pyWGCNA_5xFAD.geneExpr looks correct before proceeding.
Preprocess the dataset
Run pyWGCNA_5xFAD.preprocess() to drop low-expression genes and problematic samples.
Construct the co-expression network
Evaluate soft-threshold power: pyWGCNA_5xFAD.calculate_soft_threshold().
Build adjacency and TOM matrices via calculating_adjacency_matrix() and calculating_TOM_similarity_matrix().
Detect gene modules
Generate dendrograms and modules: calculate_geneTree(), calculate_dynamicMods(kwargs_function={'cutreeHybrid': {...}}).
Derive module eigengenes with calculate_gene_module(kwargs_function={'moduleEigengenes': {'softPower': 8}}).
Visualise adjacency/TOM heatmaps using plot_matrix(save=False) if needed.
Inspect specific modules
Extract genes from modules with get_sub_module([...], mod_type='module_color').
Build sub-networks using get_sub_network(mod_list=[...], mod_type='module_color', correlation_threshold=0.2) and plot them via plot_sub_network(...).
Update sample metadata for downstream analyses
Load sample annotations updateSampleInfo(path='.../sampleInfo.csv', sep=',').
Assign colour maps for metadata categories with setMetadataColor(...).
Analyse module–trait relationships
Run analyseWGCNA() to compute module–trait statistics.
Plot module eigengene heatmaps and bar charts with plotModuleEigenGene(module, metadata, show=True) and barplotModuleEigenGene(...).
Find hub genes
Identify top hubs per module using top_n_hub_genes(moduleName='lightgreen', n=10).
Defensive validation
# Before WGCNA: verify enough genes remain after MAD filtering
assert data.shape[0] >= 1000, f"Only {data.shape[0]} genes after filtering — WGCNA needs >1000 for meaningful modules"
# Verify expression values are numeric and non-negative
assert data.dtypes.apply(lambda d: d.kind in 'iuf').all(), "Expression matrix contains non-numeric columns"
# Verify enough samples for network construction
assert data.shape[1] >= 6, f"Only {data.shape[1]} samples — WGCNA needs >=6 samples for reliable co-expression"

Troubleshooting tips
Large datasets may require increasing save=False to avoid writing many intermediate files.
If module detection fails, confirm enough genes remain after MAD filtering and adjust deepSplit or softPower.
Ensure metadata categories have assigned colours before plotting eigengene heatmaps.
Examples
"Build a WGCNA network on the 5xFAD dataset, visualise modules, and extract hub genes from the lightgreen module."
"Load sample metadata, update colours for sex and genotype, and plot module eigengene heatmaps."
"Create a sub-network plot for the gold module using a correlation threshold of 0.2."
References
Tutorial notebook: t_wgcna.ipynb
Tutorial dataset: data/5xFAD_paper/
Quick copy/paste commands: reference.md
Weekly Installs
31
Repository
starlitnightly/omicverse
GitHub Stars
968
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass