---
title: huggingface-hub
url: https://skills.sh/gary149/huggingface-hub-skill/huggingface-hub
---

# huggingface-hub

skills/gary149/huggingface-hub-skill/huggingface-hub
huggingface-hub
Installation
$ npx skills add https://github.com/gary149/huggingface-hub-skill --skill huggingface-hub
SKILL.md
Hugging Face Hub Development Skill
When to Use This Skill

Trigger this skill when the user asks to:

Make HTTP/curl requests to Hugging Face APIs
Upload or download models/datasets using huggingface_hub Python library
Use Inference Providers API (chat completion, text generation, image generation)
Create or modify Gradio or Docker Spaces applications
Work with GGUF models, PEFT/LoRA adapters, or quantization
Load datasets with pandas, Polars, or DuckDB
Set up webhooks, Jobs, or CI/CD automation
Configure model cards, dataset cards, or Space YAML metadata
Use @huggingface/hub or Transformers.js JavaScript packages
Set up authentication, tokens, or security features
Embed Spaces in websites or enable OAuth sign-in
Quick Reference
Authentication
# Python - Interactive login
from huggingface_hub import login
login()  # Opens browser or prompts for token

# Python - Programmatic login
login(token="hf_xxx")

# Environment variable (recommended for CI/production)
# export HF_TOKEN="hf_xxx"

# CLI login
huggingface-cli login

# Set token directly
huggingface-cli login --token hf_xxx


Get tokens at: https://huggingface.co/settings/tokens

Download Files
from huggingface_hub import hf_hub_download, snapshot_download

# Single file
model_path = hf_hub_download(
    repo_id="user/model",
    filename="model.safetensors"
)

# Entire repository
local_dir = snapshot_download(repo_id="user/model")

# Specific revision
hf_hub_download(repo_id="user/model", filename="config.json", revision="v1.0")

# CLI download
huggingface-cli download HuggingFaceH4/zephyr-7b-beta
huggingface-cli download user/model model.safetensors

Upload Files
from huggingface_hub import upload_file, upload_folder, HfApi

# Single file
upload_file(
    path_or_fileobj="model.safetensors",
    path_in_repo="model.safetensors",
    repo_id="user/model"
)

# Entire folder
upload_folder(
    folder_path="./my_model",
    repo_id="user/model"
)

# Using HfApi
api = HfApi()
api.create_repo(repo_id="user/new-model", repo_type="model")
api.upload_file(path_or_fileobj="model.pt", path_in_repo="model.pt", repo_id="user/new-model")

Inference Providers
import os
from huggingface_hub import InferenceClient

client = InferenceClient(api_key=os.environ["HF_TOKEN"])

# Chat completion (OpenAI-compatible)
response = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[{"role": "user", "content": "Hello!"}]
)

# Text generation
response = client.text_generation(
    "The answer to the universe is",
    model="meta-llama/Llama-3.1-8B-Instruct"
)

# Image generation
image = client.text_to_image(
    "A serene mountain landscape at sunset",
    model="black-forest-labs/FLUX.1-schnell"
)


curl:

curl https://router.huggingface.co/v1/chat/completions \
  -H "Authorization: Bearer $HF_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta-llama/Llama-3.1-8B-Instruct",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'

Dataset Loading
import pandas as pd
import polars as pl

# Pandas with hf:// protocol
df = pd.read_parquet("hf://datasets/stanfordnlp/imdb/plain_text/train-00000-of-00001.parquet")

# Polars with hf:// protocol
df = pl.read_parquet("hf://datasets/stanfordnlp/imdb/plain_text/train-*.parquet")

# DuckDB
import duckdb
conn = duckdb.connect()
df = conn.execute("SELECT * FROM 'hf://datasets/stanfordnlp/imdb/plain_text/*.parquet' LIMIT 100").fetchdf()

Gradio Space (Minimal)

README.md:

---
title: My Space
emoji: 🚀
sdk: gradio
sdk_version: 5.0.0
app_file: app.py
---


app.py:

import gradio as gr
from transformers import pipeline

pipe = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify(text):
    result = pipe(text)[0]
    return {result["label"]: result["score"]}

demo = gr.Interface(fn=classify, inputs="text", outputs="label")
demo.launch()

Space Configuration
---
title: My Application
emoji: 🤗
colorFrom: blue
colorTo: purple
sdk: gradio              # gradio, docker, or static
sdk_version: 5.0.0
python_version: "3.10"
app_file: app.py
app_port: 7860           # Docker only
suggested_hardware: t4-small  # or cpu-basic, a10g-small, etc.
pinned: true
models:
  - openai-community/gpt2
datasets:
  - mozilla-foundation/common_voice_13_0
hf_oauth: true           # Enable HF OAuth
preload_from_hub:
  - user/model config.json,model.safetensors
---


Hardware options:

CPU: cpu-basic, cpu-upgrade
GPU: t4-small, t4-medium, l4x1, l4x4, a10g-small, a10g-large, a100-large
TPU: v5e-1x1, v5e-2x2, v5e-2x4
Model Card Metadata
---
language:
  - en
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
  - nlp
  - sentiment
datasets:
  - stanfordnlp/imdb
base_model: bert-base-uncased
metrics:
  - accuracy
---

Resources

Detailed documentation organized by topic:

references/
api-http.md - curl/HTTP API examples for all endpoints
python-sdk.md - huggingface_hub Python patterns (download, upload, HfApi)
javascript-sdk.md - @huggingface/hub and Transformers.js
inference-providers.md - InferenceClient and provider selection
models-advanced.md - GGUF, PEFT/LoRA, quantization formats
datasets-workflows.md - pandas, Polars, DuckDB data workflows
spaces-config.md - Complete YAML configuration reference
spaces-gradio.md - Building Gradio Spaces
spaces-docker.md - Docker Spaces with secrets and permissions
spaces-integration.md - Embedding, OAuth, MCP servers
automation.md - Webhooks, Jobs, GitHub Actions
security.md - Tokens, gating, scanning, SSO
models.md - Model repositories, cards, and uploading
datasets.md - Dataset repositories and configuration
enterprise.md - Enterprise Hub features
doc-syntax.md - Doc-builder markdown syntax
examples/
inference-curl.sh - Complete curl examples for all APIs
jupyter-pandas.py - Jupyter + pandas workflow
browser-transformersjs.html - Browser inference with Transformers.js
lora-peft-workflow.py - LoRA adapter find/load/merge workflow
webhooks-auto-retrain.py - Webhook automation for retraining
collections-api.py - Collections creation and management
offline-setup.py - Offline/air-gapped environment setup
space-embed-iframe.html - Embedding patterns for websites
gradio-image-classifier.py - Image classification with gr.Interface
gradio-chat-interface.py - Chat interface with HF model
upload-model.py - PyTorchModelHubMixin complete example
download-files.py - Various download patterns
model-card.md - Model card template with metadata
dataset-card.md - Dataset card template with metadata
patterns/
missing-features.md - iOS, Next.js, full offline workarounds
Best Practices
Always use environment variables for tokens - Never hardcode hf_xxx tokens
Use .safetensors format - Preferred over .bin for model weights
Add comprehensive model cards - Include intended use, limitations, training data
Pin SDK versions in Spaces - Ensure reproducibility
Use preload_from_hub - Speed up Space startup by preloading models
Set appropriate hardware - Match compute needs to avoid OOM errors
Use fine-grained tokens - Minimize scope for production apps
Use Parquet for datasets - Much faster than CSV for large data
Weekly Installs
31
Repository
gary149/hugging…ub-skill
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykWarn