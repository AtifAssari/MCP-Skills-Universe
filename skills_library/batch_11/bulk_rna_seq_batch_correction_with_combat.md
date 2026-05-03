---
title: bulk-rna-seq-batch-correction-with-combat
url: https://skills.sh/starlitnightly/omicverse/bulk-rna-seq-batch-correction-with-combat
---

# bulk-rna-seq-batch-correction-with-combat

skills/starlitnightly/omicverse/bulk-rna-seq-batch-correction-with-combat
bulk-rna-seq-batch-correction-with-combat
Installation
$ npx skills add https://github.com/starlitnightly/omicverse --skill bulk-rna-seq-batch-correction-with-combat
SKILL.md
Bulk RNA-seq batch correction with ComBat
Overview

Apply this skill when a user has multiple bulk expression matrices measured across different batches and needs to harmonise them before downstream analysis. It follows t_bulk_combat.ipynb, w hich demonstrates the pyComBat workflow on ovarian cancer microarray cohorts.

Instructions
Import core libraries
Load omicverse as ov, anndata, pandas as pd, and matplotlib.pyplot as plt.
Call ov.ov_plot_set() (aliased ov.plot_set() in some releases) to align figures with omicverse styling.
Load each batch separately
Read the prepared pickled matrices (or user-provided expression tables) with pd.read_pickle(...)/pd.read_csv(...).
Transpose to gene × sample before wrapping them in anndata.AnnData objects so adata.obs stores sample metadata.
Assign a batch column for every cohort (adata.obs['batch'] = '1', '2', ...). Encourage descriptive labels when availa ble.
Concatenate on shared genes
Use anndata.concat([adata1, adata2, adata3], merge='same') to retain the intersection of genes across batches.
Confirm the combined adata reports balanced sample counts per batch; if not, prompt users to re-check inputs.
Run ComBat batch correction
Execute ov.bulk.batch_correction(adata, batch_key='batch').
Explain that corrected values are stored in adata.layers['batch_correction'] while the original counts remain in adata.X.
Export corrected and raw matrices
Obtain DataFrames via adata.to_df().T (raw) and adata.to_df(layer='batch_correction').T (corrected).
Encourage saving both tables (.to_csv(...)) plus the harmonised AnnData (adata.write_h5ad('adata_batch.h5ad', compressio n='gzip')).
Benchmark the correction
For per-sample variance checks, draw before/after boxplots and recolour boxes using ov.pl.red_color, blue_color, gree n_color palettes to match batches.
Copy raw counts to a named layer with adata.layers['raw'] = adata.X.copy() before PCA.
Run ov.pp.pca(adata, layer='raw', n_pcs=50) and ov.pp.pca(adata, layer='batch_correction', n_pcs=50).
Visualise embeddings with ov.pl.embedding(..., basis='raw|original|X_pca', color='batch', frameon='small') and repeat fo r the corrected layer to verify mixing.
Defensive validation
# Before ComBat: verify batch column exists and has >1 batch
assert 'batch' in adata.obs.columns, "adata.obs must contain a 'batch' column"
n_batches = adata.obs['batch'].nunique()
assert n_batches > 1, f"Only {n_batches} batch — need >1 for batch correction"
# Verify gene overlap after concatenation
if adata.n_vars < 100:
    print(f"WARNING: Only {adata.n_vars} shared genes after concat — check gene ID harmonization")

Troubleshooting tips
Mismatched gene identifiers cause dropped features—remind users to harmonise feature names (e.g., gene symbols) before conca tenation.
pyComBat expects log-scale intensities or similarly distributed counts; recommend log-transforming strongly skewed matrices.
If batch_correction layer is missing, ensure the batch_key matches the column name in adata.obs.
Examples
"Combine three GEO ovarian cohorts, run ComBat, and export both the raw and corrected CSV matrices."
"Plot PCA embeddings before and after batch correction to confirm that batches 1–3 overlap."
"Save the harmonised AnnData file so I can reload it later for downstream DEG analysis."
References
Tutorial notebook: t_bulk_combat.ipynb
Example inputs: omicverse_guide/docs/Tutorials-bulk/data/combat/
Quick copy/paste commands: reference.md
Weekly Installs
30
Repository
starlitnightly/omicverse
GitHub Stars
968
First Seen
Jan 26, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass