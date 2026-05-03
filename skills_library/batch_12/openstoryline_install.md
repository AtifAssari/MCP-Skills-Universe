---
title: openstoryline-install
url: https://skills.sh/fireredteam/firered-openstoryline/openstoryline-install
---

# openstoryline-install

skills/fireredteam/firered-openstoryline/openstoryline-install
openstoryline-install
Installation
$ npx skills add https://github.com/fireredteam/firered-openstoryline --skill openstoryline-install
SKILL.md
OpenStoryline Install

Use this skill when the task is to install or repair a local source checkout of FireRed-OpenStoryline.

Keep the workflow deterministic:

Confirm the repo path and read the current README.md and config.toml.
Detect local prerequisites before changing anything.
Prefer a local venv install unless the user explicitly asks for Docker or conda.
Download resources only after Python dependencies succeed.
Validate imports and config loading before claiming success.
This skill assumes macOS, Linux, or WSL with a POSIX shell.
What This Skill Covers
Clone the GitHub repo if needed
Create a Python environment
Install Python dependencies
Download .storyline models and resource/ assets
Fill config.toml model settings
Start MCP and web servers
Explain common installation/documentation gaps
Preconditions

Check these first:

git
Python >= 3.11
ffmpeg
wget
unzip

Optional:

docker
conda

If ffmpeg, wget, or unzip are missing, install them through the OS package manager before continuing.

Examples:

macOS with Homebrew:

brew install ffmpeg wget unzip


Debian/Ubuntu:

sudo apt-get update
sudo apt-get install -y ffmpeg wget unzip


If no supported package manager or permission is available, stop and report the missing system dependency clearly.

Interpreter selection

First prefer any interpreter that already exists and passes version checks:

A system Python >= 3.11
An already available conda Python >= 3.11
An already available pyenv Python >= 3.11, but only if basic stdlib modules work

Validate candidate interpreters before using them:

/path/to/python -c "import ssl, sqlite3, venv; print('stdlib_ok')"


If no supported interpreter already exists, peferr conda fallback:

conda create -y -n openstoryline-py311 python=3.11
conda run -n openstoryline-py311 python --version
conda run -n openstoryline-py311 python -m venv .venv


After a supported interpreter is found, always create a repo-local .venv and continue using .venv/bin/python for install, config validation, and service startup.

Do not duplicate the rest of the workflow for pyenv or conda unless the user explicitly asks to stay inside a conda environment.

Preferred Install Path

From the repo root:

/path/to/python -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
bash download.sh


Notes:

download.sh pulls both model weights and a large resource archive. It can take a long time and may resume after network drops.
The resource download is required for a full local run, not just the Python package install.
Configuration

Before starting the app, update config.toml.

You can use scripts/update_config.py.

At minimum, fill:

.venv/bin/python scripts/update_config.py --config ./config.toml --set llm.model=REPLACE_WITH_REAL_MODEL
.venv/bin/python scripts/update_config.py --config ./config.toml --set llm.base_url=REPLACE_WITH_REAL_URL
.venv/bin/python scripts/update_config.py --config ./config.toml --set llm.api_key=sk-REPLACE_WITH_REAL_KEY

.venv/bin/python scripts/update_config.py --config ./config.toml --set vlm.model=REPLACE_WITH_REAL_MODEL
.venv/bin/python scripts/update_config.py --config ./config.toml --set vlm.base_url=REPLACE_WITH_REAL_URL
.venv/bin/python scripts/update_config.py --config ./config.toml --set vlm.api_key=sk-REPLACE_WITH_REAL_KEY


Optional but common:

search_media.pexels_api_key for searching media
TTS provider keys under generate_voiceover.providers.* (choose one provider)
Verification

Run these checks before saying installation is complete:

.venv/bin/pip check
PYTHONPATH=src .venv/bin/python -c "from open_storyline.config import load_settings; load_settings('config.toml'); print('config_ok')"


Also confirm key resources exist:

test -f .storyline/models/transnetv2-pytorch-weights.pth
test -d resource/bgms

Start Services

There are two common paths. These are long-running processes. Do not wait for them to exit normally. Treat successful startup log lines or confirmed listening ports as success, and keep the services running in separate shells/sessions as needed.

Manual start:

PYTHONPATH=src .venv/bin/python -m open_storyline.mcp.server


In a second shell:

PYTHONPATH=src .venv/bin/python -m uvicorn agent_fastapi:app --host 127.0.0.1 --port 8005

Expected Outputs

After a successful install:

.venv/ exists
MCP listens on the configured local port (commonly 127.0.0.1:8001)
Web listens on the configured web port (commonly 127.0.0.1:8005, though run.sh defaults may differ)
Common Problems
download.sh is slow or interrupted

Symptom:

Large downloads stall or reconnect

Fix:

Let wget continue; it supports resume behavior here
Verify extracted outputs instead of trusting the progress meter
Web/MCP server fails to bind

Symptom:

operation not permitted while binding 127.0.0.1 or 0.0.0.0

Fix:

In agent sandboxes, request permission to open local listening ports
Prefer 127.0.0.1 over 0.0.0.0 unless external access is required
Response Pattern

When reporting status to the user, separate:

what is installed
what is still downloading
what config is still missing
what address the service is listening on

Do not say "installation complete" if only the Python packages are installed but the resource bundle is still missing.

Weekly Installs
81
Repository
fireredteam/fir…toryline
GitHub Stars
2.4K
First Seen
2 days ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykFail