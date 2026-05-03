---
rating: ⭐⭐⭐
title: hf-init
url: https://skills.sh/richfrem/agent-plugins-skills/hf-init
---

# hf-init

skills/richfrem/agent-plugins-skills/hf-init
hf-init
Installation
$ npx skills add https://github.com/richfrem/agent-plugins-skills --skill hf-init
SKILL.md
Dependencies

This skill requires Python 3.8+ and standard library only. No external packages needed.

To install this skill's dependencies:

pip-compile ./requirements.in
pip install -r ./requirements.txt


See ./requirements.txt for the dependency lockfile (currently empty — standard library only).

HuggingFace Init (Onboarding)

Status: Active Author: Richard Fremmerlid Domain: HuggingFace Integration

Purpose

Sets up everything needed for HuggingFace persistence. Run this once when onboarding a new project, or whenever credentials change.

What It Does
Validates required .env variables are set
Tests API connectivity with the configured token
Ensures the dataset repository exists on HF Hub
Creates the standard folder structure (lineage/, data/, metadata/)
Uploads the dataset card (README.md) with configurable discovery tags
Required Environment Variables
Variable	Required	Description
HUGGING_FACE_USERNAME	✅ Yes	Your HF username
HUGGING_FACE_TOKEN	✅ Yes	API token (set in ~/.zshrc, NOT .env)
HUGGING_FACE_REPO	✅ Yes	Model repo name
HUGGING_FACE_DATASET_PATH	✅ Yes	Dataset repo name
HUGGING_FACE_TAGS	❌ No	Comma-separated discovery tags for dataset card
HUGGING_FACE_PROJECT_NAME	❌ No	Pretty name for dataset card heading
SOUL_VALENCE_THRESHOLD	❌ No	Moral/emotional charge filter (default: -0.7)
Usage
Validate Config
python ./hf_config.py

Full Init (Validate + Create Structure + Dataset Card)
python ./hf_init.py

Validate Only (No Changes)
python ./hf_init.py --validate-only

Quick Setup
# Token goes in shell profile (never committed):
export HUGGING_FACE_TOKEN=hf_xxxxxxxxxxxxx

# Project vars go in .env:
HUGGING_FACE_USERNAME=<your-username>
HUGGING_FACE_REPO=<your-model-repo>
HUGGING_FACE_DATASET_PATH=<your-dataset-repo>

# Optional customization:
HUGGING_FACE_TAGS=reasoning-traces,cognitive-continuity,your-project-tag
HUGGING_FACE_PROJECT_NAME=My Project Soul

# Run init
python ./hf_init.py

Weekly Installs
20
Repository
richfrem/agent-…s-skills
GitHub Stars
2
First Seen
Mar 6, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass