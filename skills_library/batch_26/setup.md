---
title: setup
url: https://skills.sh/adaptyvbio/protein-design-skills/setup
---

# setup

skills/adaptyvbio/protein-design-skills/setup
setup
Installation
$ npx skills add https://github.com/adaptyvbio/protein-design-skills --skill setup
SKILL.md
Setup Guide

Help users get their environment ready to run protein design tools.

Quick checklist

Run through this checklist when a user encounters setup issues:

Step	Check	Fix
1. Modal CLI	modal --version	pip install modal
2. Modal auth	modal token show	modal setup
3. biomodals	ls biomodals/modal_*.py	git clone https://github.com/hgbrian/biomodals
4. Test	cd biomodals && modal run modal_boltzgen.py --help	See troubleshooting
Diagnosing issues
Error: "modal: command not found"

Cause: Modal CLI not installed.

Fix:

pip install modal


Then restart the terminal or run hash -r.

Error: "Permission denied" or "Unauthorized"

Cause: Modal not authenticated.

Fix:

modal setup


This opens a browser. Click "Authorize" to complete authentication.

Error: "No such file or directory: modal_boltzgen.py"

Cause: biomodals repository not cloned or not in correct directory.

Fix:

git clone https://github.com/hgbrian/biomodals
cd biomodals

Error: "uvx: command not found"

Cause: uvx is an optional wrapper from the uv package. It's not required.

Fix: Run modal directly (recommended):

modal run modal_boltzgen.py --help


Or install uv if you prefer using uvx:

pip install uv

Full setup steps
Step 1: Install Modal CLI
pip install modal


Verify: modal --version

Step 2: Authenticate Modal
modal setup


This opens a browser. Click "Authorize".

Verify: modal token show

Step 3: Clone biomodals
git clone https://github.com/hgbrian/biomodals
cd biomodals


Verify: ls modal_*.py should show files like modal_boltzgen.py

Step 4: Test the Setup
cd biomodals
modal run modal_boltzgen.py --help


Expected: Usage instructions appear showing --input-yaml, --protocol, --num-designs options.

Common workflows after setup

Once setup is complete, users can:

cd biomodals

# Design binders with BoltzGen (requires YAML config)
modal run modal_boltzgen.py --input-yaml binder.yaml --protocol protein-anything --num-designs 50

# Generate backbones with RFdiffusion
modal run modal_rfdiffusion.py --pdb target.pdb --contigs "A1-150/0 70-100" --num-designs 100

# Validate with Chai
modal run modal_chai1.py --input-faa designs.fasta

GPU selection

Set GPU with environment variable:

GPU=A10G modal run modal_rfdiffusion.py --pdb target.pdb --contigs "A1-100/0 50-80" --num-designs 10
GPU=L40S modal run modal_boltzgen.py --input-yaml config.yaml --num-designs 50
GPU=A100 modal run modal_chai1.py --input-faa complex.fasta

GPU	VRAM	Best For
T4	16GB	ProteinMPNN, ESM
A10G	24GB	RFdiffusion, Chai
L40S	48GB	BoltzGen, BindCraft
A100	40-80GB	Large complexes
Modal free tier

Modal offers $30/month in free credits - enough for:

~500 BoltzGen designs
~2000 RFdiffusion backbones
~1000 Chai predictions

Full documentation: See Installation Guide

Weekly Installs
17
Repository
adaptyvbio/prot…n-skills
GitHub Stars
125
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn