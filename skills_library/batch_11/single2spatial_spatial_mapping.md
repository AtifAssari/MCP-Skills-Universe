---
title: single2spatial-spatial-mapping
url: https://skills.sh/starlitnightly/omicverse/single2spatial-spatial-mapping
---

# single2spatial-spatial-mapping

skills/starlitnightly/omicverse/single2spatial-spatial-mapping
single2spatial-spatial-mapping
Installation
$ npx skills add https://github.com/starlitnightly/omicverse --skill single2spatial-spatial-mapping
SKILL.md
Single2Spatial spatial mapping
Overview

Apply this skill when converting single-cell references into spatially resolved profiles. It follows t_single2spatial.ipynb, demonstrating how Single2Spatial trains on PDAC scRNA-seq and Visium data, reconstructs spot-level proportions, and visualises marker expression.

Instructions
Import dependencies and style
Load omicverse as ov, scanpy as sc, anndata, pandas as pd, numpy as np, and matplotlib.pyplot as plt.
Call ov.utils.ov_plot_set() (or ov.plot_set() in older versions) to align plots with omicverse styling.
Load single-cell and spatial datasets
Read processed matrices with pd.read_csv(...) then create AnnData objects (anndata.AnnData(raw_df.T)).
Attach metadata: single_data.obs = pd.read_csv(...)[['Cell_type']] and spatial_data.obs = pd.read_csv(... ) containing coordinates and slide metadata.
Initialise Single2Spatial
Instantiate ov.bulk2single.Single2Spatial(single_data=single_data, spatial_data=spatial_data, celltype_key='Cell_type', spot_key=['xcoord','ycoord'], gpu=0).
Note that inputs should be normalised/log-scaled scRNA-seq matrices; ensure spot_key matches spatial coordinate columns.
Train the deep-forest model
Execute st_model.train(spot_num=500, cell_num=10, df_save_dir='...', df_save_name='pdac_df', k=10, num_epochs=1000, batch_size=1000, predicted_size=32) to fit the mapper and generate reconstructed spatial AnnData (sp_adata).
Explain that spot_num defines sampled pseudo-spots per iteration and cell_num controls per-spot cell draws.
Load pretrained weights
Use st_model.load(modelsize=14478, df_load_dir='.../pdac_df.pth', k=10, predicted_size=32) when checkpoints already exist to skip training.
Assess spot-level outputs
Call st_model.spot_assess() to compute aggregated spot AnnData (sp_adata_spot) for QC.
Plot marker genes with sc.pl.embedding(sp_adata, basis='X_spatial', color=['REG1A', 'CLDN1', ...], frameon=False, ncols=4).
Visualise proportions and cell-type maps
Use sc.pl.embedding(sp_adata_spot, basis='X_spatial', color=['Acinar cells', ...], frameon=False) to highlight per-spot cell fractions.
Plot sp_adata coloured by Cell_type with palette=ov.utils.ov_palette()[11:] to show reconstructed assignments.
Export results
Encourage saving generated AnnData objects (sp_adata.write_h5ad(...), sp_adata_spot.write_h5ad(...)) and derived CSV summaries for downstream reporting.
Defensive validation
# Before Single2Spatial: verify spatial coordinates exist
for col in spot_key:
    assert col in spatial_data.obs.columns, f"Spatial coordinate column '{col}' not found in spatial_data.obs"
# Verify scRNA-seq is log-normalized (max should be <~15, not hundreds/thousands)
if single_data.X.max() > 50:
    print("WARNING: scRNA-seq data may not be log-normalized. Raw counts cause scale mismatches.")
# Verify cell type column exists
assert celltype_key in single_data.obs.columns, f"Cell type column '{celltype_key}' not found"

Troubleshooting tips
If training diverges, reduce learning_rate via keyword arguments or decrease predicted_size to stabilise the forest.
Ensure scRNA-seq inputs are log-normalised; raw counts can lead to scale mismatches and poor spatial predictions.
Verify GPU availability when gpu is non-zero; fallback to CPU by omitting the argument or setting gpu=-1.
Examples
"Train Single2Spatial on PDAC scRNA-seq and Visium slides, then visualise REG1A and CLDN1 spatial expression."
"Load a saved Single2Spatial checkpoint to regenerate spot-level cell-type proportions for reporting."
"Plot reconstructed cell-type maps with omicverse palettes to compare against histology."
References
Tutorial notebook: t_single2spatial.ipynb
Example datasets and models: omicverse_guide/docs/Tutorials-bulk2single/data/pdac/
Quick copy/paste commands: reference.md
Weekly Installs
32
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