---
title: tribev2-brain-encoding
url: https://skills.sh/aradotso/trending-skills/tribev2-brain-encoding
---

# tribev2-brain-encoding

skills/aradotso/trending-skills/tribev2-brain-encoding
tribev2-brain-encoding
Installation
$ npx skills add https://github.com/aradotso/trending-skills --skill tribev2-brain-encoding
SKILL.md
TRIBE v2 Brain Encoding Model

Skill by ara.so — Daily 2026 Skills collection

TRIBE v2 is Meta's multimodal foundation model that predicts fMRI brain responses to naturalistic stimuli (video, audio, text). It combines LLaMA 3.2 (text), V-JEPA2 (video), and Wav2Vec-BERT (audio) encoders into a unified Transformer architecture that maps multimodal representations onto the cortical surface (fsaverage5, ~20k vertices).

Installation
# Inference only
pip install -e .

# With brain visualization (PyVista & Nilearn)
pip install -e ".[plotting]"

# Full training dependencies (PyTorch Lightning, W&B, etc.)
pip install -e ".[training]"

Quick Start — Inference
Load pretrained model and predict from video
from tribev2 import TribeModel

# Load from HuggingFace (downloads weights to cache)
model = TribeModel.from_pretrained("facebook/tribev2", cache_folder="./cache")

# Build events dataframe from a video file
df = model.get_events_dataframe(video_path="path/to/video.mp4")

# Predict brain responses
preds, segments = model.predict(events=df)
print(preds.shape)  # (n_timesteps, n_vertices) on fsaverage5

Multimodal input — video + audio + text
from tribev2 import TribeModel

model = TribeModel.from_pretrained("facebook/tribev2", cache_folder="./cache")

# All modalities together (text is auto-converted to speech and transcribed)
df = model.get_events_dataframe(
    video_path="path/to/video.mp4",
    audio_path="path/to/audio.wav",   # optional, overrides video audio
    text_path="path/to/script.txt",   # optional, auto-timed
)

preds, segments = model.predict(events=df)
print(preds.shape)  # (n_timesteps, n_vertices)

Text-only prediction
from tribev2 import TribeModel

model = TribeModel.from_pretrained("facebook/tribev2", cache_folder="./cache")

df = model.get_events_dataframe(text_path="path/to/narration.txt")
preds, segments = model.predict(events=df)

Brain Visualization
from tribev2 import TribeModel
from tribev2.plotting import plot_brain_surface

model = TribeModel.from_pretrained("facebook/tribev2", cache_folder="./cache")
df = model.get_events_dataframe(video_path="path/to/video.mp4")
preds, segments = model.predict(events=df)

# Plot a single timepoint on the cortical surface
plot_brain_surface(preds[0], backend="nilearn")   # or backend="pyvista"

Training a Model from Scratch
1. Set environment variables
export DATAPATH="/path/to/studies"
export SAVEPATH="/path/to/output"
export SLURM_PARTITION="your_slurm_partition"

2. Authenticate with HuggingFace (required for LLaMA 3.2)
huggingface-cli login
# Paste a HuggingFace read token when prompted
# Request access at: https://huggingface.co/meta-llama/Llama-3.2-3B

3. Local test run
python -m tribev2.grids.test_run

4. Full grid search on Slurm
# Cortical surface model
python -m tribev2.grids.run_cortical

# Subcortical regions
python -m tribev2.grids.run_subcortical

Key API — TribeModel
from tribev2 import TribeModel

# Load pretrained weights
model = TribeModel.from_pretrained(
    "facebook/tribev2",
    cache_folder="./cache"  # local cache for HuggingFace weights
)

# Build events dataframe (word-level timings, chunking, etc.)
df = model.get_events_dataframe(
    video_path=None,   # str path to .mp4
    audio_path=None,   # str path to .wav
    text_path=None,    # str path to .txt
)

# Run prediction
preds, segments = model.predict(events=df)
# preds: np.ndarray of shape (n_timesteps, n_vertices)
# segments: list of segment metadata dicts

Project Structure
tribev2/
├── main.py              # Experiment pipeline: Data, TribeExperiment
├── model.py             # FmriEncoder: Transformer multimodal→fMRI model
├── pl_module.py         # PyTorch Lightning training module
├── demo_utils.py        # TribeModel and inference helpers
├── eventstransforms.py  # Event transforms (word extraction, chunking)
├── utils.py             # Multi-study loading, splitting, subject weighting
├── utils_fmri.py        # Surface projection (MNI / fsaverage) and ROI analysis
├── grids/
│   ├── defaults.py      # Full default experiment configuration
│   └── test_run.py      # Quick local test entry point
├── plotting/            # Brain visualization backends
└── studies/             # Dataset definitions (Algonauts2025, Lahner2024, …)

Configuration — Defaults

Edit tribev2/grids/defaults.py or set environment variables:

# tribev2/grids/defaults.py (key fields)
{
    "datapath": "/path/to/studies",       # override with DATAPATH env var
    "savepath": "/path/to/output",        # override with SAVEPATH env var
    "slurm_partition": "learnfair",       # override with SLURM_PARTITION env var
    "model": "FmriEncoder",
    "modalities": ["video", "audio", "text"],
    "surface": "fsaverage5",              # ~20k vertices
}

Custom Experiment with PyTorch Lightning
from tribev2.main import Data, TribeExperiment
from tribev2.pl_module import TribePLModule
import pytorch_lightning as pl

# Configure experiment
experiment = TribeExperiment(
    datapath="/path/to/studies",
    savepath="/path/to/output",
    modalities=["video", "audio", "text"],
)

data = Data(experiment)
module = TribePLModule(experiment)

trainer = pl.Trainer(
    max_epochs=50,
    accelerator="gpu",
    devices=4,
)
trainer.fit(module, data)

Working with fMRI Surfaces
from tribev2.utils_fmri import project_to_fsaverage, get_roi_mask

# Project MNI coordinates to fsaverage5 surface
surface_data = project_to_fsaverage(mni_data, target="fsaverage5")

# Get a specific ROI mask (e.g., early visual cortex)
roi_mask = get_roi_mask(roi_name="V1", surface="fsaverage5")
v1_responses = preds[:, roi_mask]
print(v1_responses.shape)  # (n_timesteps, n_v1_vertices)

Common Patterns
Batch prediction over multiple videos
from tribev2 import TribeModel
import numpy as np

model = TribeModel.from_pretrained("facebook/tribev2", cache_folder="./cache")

video_paths = ["video1.mp4", "video2.mp4", "video3.mp4"]
all_predictions = []

for vp in video_paths:
    df = model.get_events_dataframe(video_path=vp)
    preds, segments = model.predict(events=df)
    all_predictions.append(preds)

# all_predictions: list of (n_timesteps_i, n_vertices) arrays

Extract predictions for specific brain region
from tribev2 import TribeModel
from tribev2.utils_fmri import get_roi_mask

model = TribeModel.from_pretrained("facebook/tribev2", cache_folder="./cache")
df = model.get_events_dataframe(video_path="video.mp4")
preds, segments = model.predict(events=df)

# Focus on auditory cortex
ac_mask = get_roi_mask("auditory_cortex", surface="fsaverage5")
auditory_responses = preds[:, ac_mask]  # (n_timesteps, n_ac_vertices)

Access segment timing metadata
preds, segments = model.predict(events=df)

for i, seg in enumerate(segments):
    print(f"Segment {i}: onset={seg['onset']:.2f}s, duration={seg['duration']:.2f}s")
    print(f"  Brain response shape: {preds[i].shape}")

Troubleshooting

LLaMA 3.2 access denied

# Must request access at https://huggingface.co/meta-llama/Llama-3.2-3B
# Then authenticate:
huggingface-cli login
# Use a HuggingFace token with read permissions


CUDA out of memory during inference

# Use CPU for inference on smaller machines
import torch
model = TribeModel.from_pretrained("facebook/tribev2", cache_folder="./cache")
model.to("cpu")


Missing visualization dependencies

pip install -e ".[plotting]"
# Installs pyvista and nilearn backends


Slurm training not submitting

# Check env vars are set
echo $DATAPATH $SAVEPATH $SLURM_PARTITION
# Or edit tribev2/grids/defaults.py directly


Video without audio track causes error

# Provide audio separately or use text-only mode
df = model.get_events_dataframe(
    video_path="silent_video.mp4",
    audio_path="separate_audio.wav",
)

Citation
@article{dAscoli2026TribeV2,
  title={A foundation model of vision, audition, and language for in-silico neuroscience},
  author={d'Ascoli, St{\'e}phane and Rapin, J{\'e}r{\'e}my and Benchetrit, Yohann and Brookes, Teon
          and Begany, Katelyn and Raugel, Jos{\'e}phine and Banville, Hubert and King, Jean-R{\'e}mi},
  year={2026}
}

Resources
Paper
Interactive Demo
HuggingFace Weights
Colab Notebook
Weekly Installs
579
Repository
aradotso/trending-skills
GitHub Stars
42
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass