---
rating: ⭐⭐⭐
title: bulktrajblend-trajectory-interpolation
url: https://skills.sh/starlitnightly/omicverse/bulktrajblend-trajectory-interpolation
---

# bulktrajblend-trajectory-interpolation

skills/starlitnightly/omicverse/bulktrajblend-trajectory-interpolation
bulktrajblend-trajectory-interpolation
Installation
$ npx skills add https://github.com/starlitnightly/omicverse --skill bulktrajblend-trajectory-interpolation
SKILL.md
BulkTrajBlend trajectory interpolation
Overview

Invoke this skill when users need to bridge gaps in single-cell developmental trajectories using matched bulk RNA-seq. It follows t_bulktrajblend.ipynb, showcasing how BulkTrajBlend deconvolves PDAC bulk samples, identifies overlapping communities with a GNN, and interpolates "interrupted" cell states.

Instructions
Prepare libraries and inputs
Import omicverse as ov, scanpy as sc, scvelo as scv, and helper functions like from omicverse.utils import mde; run ov.plot_set().
Load the reference scRNA-seq AnnData (scv.datasets.dentategyrus()) and raw bulk counts with ov.utils.read(...) followed by ov.bulk.Matrix_ID_mapping(...) for gene ID harmonisation.
Configure BulkTrajBlend
Instantiate ov.bulk2single.BulkTrajBlend(bulk_seq=bulk_df, single_seq=adata, bulk_group=['dg_d_1','dg_d_2','dg_d_3'], celltype_key='clusters').
Explain that bulk_group names correspond to raw bulk columns and the method expects unscaled counts.
Set beta-VAE expectations
Call bulktb.vae_configure(cell_target_num=100) (or pass a dictionary) to define expected cell counts per cluster. Mention that omitting the argument triggers TAPE-based estimation.
Train or load the beta-VAE
Use bulktb.vae_train(batch_size=512, learning_rate=1e-4, hidden_size=256, epoch_num=3500, vae_save_dir='...', vae_save_name='dg_btb_vae', generate_save_dir='...', generate_save_name='dg_btb').
Highlight resuming with bulktb.vae_load('.../dg_btb_vae.pth') and the need to regenerate cells with consistent random seeds for reproducibility.
Generate synthetic cells
Produce filtered AnnData via bulktb.vae_generate(leiden_size=25) and inspect compositions with ov.bulk2single.bulk2single_plot_cellprop(...).
Save outputs to disk for reuse (adata.write_h5ad).
Configure and train the GNN
Call bulktb.gnn_configure(max_epochs=2000, use_rep='X', neighbor_rep='X_pca', gpu=0, ...) to set hyperparameters.
Train using bulktb.gnn_train(); reload checkpoints with bulktb.gnn_load('save_model/gnn.pth').
Generate overlapping community assignments through bulktb.gnn_generate().
Visualise community structure
Create MDE embeddings: bulktb.nocd_obj.adata.obsm['X_mde'] = mde(bulktb.nocd_obj.adata.obsm['X_pca']).
Plot clusters vs. discovered communities using sc.pl.embedding(..., color=['clusters','nocd_n'], palette=ov.utils.pyomic_palette()) and filtered subsets excluding synthetic labels with hyphens.
Interpolate missing states
Run bulktb.interpolation('OPC') (replace with target lineage) to synthesise continuity, then preprocess the interpolated AnnData (HVG selection, scaling, PCA).
Compute embeddings with mde, visualise with ov.pl.embedding, and compare to the original atlas.
Analyse trajectories
Initialise ov.single.pyVIA on both original and interpolated data to derive pseudotime, followed by get_pseudotime, ov.pp.neighbors, ov.utils.cal_paga, and ov.utils.plot_paga for topology validation.
Defensive validation
# Before BulkTrajBlend: verify bulk_group columns exist
for g in bulk_group:
    assert g in bulk_df.columns, f"Bulk group '{g}' not in bulk data columns"
# Verify celltype_key exists in reference
assert celltype_key in adata.obs.columns, f"Cell type column '{celltype_key}' not in reference AnnData"
# Verify gene name overlap
shared = set(bulk_df.index) & set(adata.var_names)
assert len(shared) > 100, f"Only {len(shared)} shared genes — harmonize gene IDs first"

Troubleshooting tips
If the VAE collapses (high reconstruction loss), lower learning_rate or reduce hidden_size.
Ensure the same generated dataset is used before calling gnn_train; regenerating cells changes the graph and can break checkpoint loading.
Sparse clusters may need adjusted cell_target_num thresholds or a smaller leiden_size filter to retain rare populations.
Examples
"Train BulkTrajBlend on PDAC cohorts, then interpolate missing OPC states in the trajectory."
"Load saved beta-VAE and GNN weights to regenerate overlapping communities and plot cluster vs. nocd labels."
"Run VIA on interpolated cells and compare PAGA graphs with the original scRNA-seq trajectory."
References
Tutorial notebook: t_bulktrajblend.ipynb
Example datasets and checkpoints: omicverse_guide/docs/Tutorials-bulk2single/data/
Quick copy/paste commands: reference.md
Weekly Installs
29
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