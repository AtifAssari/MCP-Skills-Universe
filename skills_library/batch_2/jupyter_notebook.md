---
title: jupyter-notebook
url: https://skills.sh/openai/skills/jupyter-notebook
---

# jupyter-notebook

skills/openai/skills/jupyter-notebook
jupyter-notebook
Installation
$ npx skills add https://github.com/openai/skills --skill jupyter-notebook
Summary

Create and scaffold Jupyter notebooks for experiments and tutorials with bundled templates.

Two notebook kinds: experiment for exploratory analysis and hypothesis-driven work, tutorial for instructional step-by-step content
Helper script new_notebook.py generates clean notebooks from templates, avoiding manual JSON authoring
Workflow emphasizes small, focused code cells paired with markdown explanations, with reference guides for experiment patterns, tutorial structure, and safe editing of existing notebooks
Output conventions use output/jupyter-notebook/ for final artifacts and tmp/jupyter-notebook/ for intermediates
SKILL.md
Jupyter Notebook Skill

Create clean, reproducible Jupyter notebooks for two primary modes:

Experiments and exploratory analysis
Tutorials and teaching-oriented walkthroughs

Prefer the bundled templates and the helper script for consistent structure and fewer JSON mistakes.

When to use
Create a new .ipynb notebook from scratch.
Convert rough notes or scripts into a structured notebook.
Refactor an existing notebook to be more reproducible and skimmable.
Build experiments or tutorials that will be read or re-run by other people.
Decision tree
If the request is exploratory, analytical, or hypothesis-driven, choose experiment.
If the request is instructional, step-by-step, or audience-specific, choose tutorial.
If editing an existing notebook, treat it as a refactor: preserve intent and improve structure.
Skill path (set once)
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"


User-scoped skills install under $CODEX_HOME/skills (default: ~/.codex/skills).

Workflow

Lock the intent. Identify the notebook kind: experiment or tutorial. Capture the objective, audience, and what "done" looks like.

Scaffold from the template. Use the helper script to avoid hand-authoring raw notebook JSON.

uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb

uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb


Fill the notebook with small, runnable steps. Keep each code cell focused on one step. Add short markdown cells that explain the purpose and expected result. Avoid large, noisy outputs when a short summary works.

Apply the right pattern. For experiments, follow references/experiment-patterns.md. For tutorials, follow references/tutorial-patterns.md.

Edit safely when working with existing notebooks. Preserve the notebook structure; avoid reordering cells unless it improves the top-to-bottom story. Prefer targeted edits over full rewrites. If you must edit raw JSON, review references/notebook-structure.md first.

Validate the result. Run the notebook top-to-bottom when the environment allows. If execution is not possible, say so explicitly and call out how to validate locally. Use the final pass checklist in references/quality-checklist.md.

Templates and helper script
Templates live in assets/experiment-template.ipynb and assets/tutorial-template.ipynb.
The helper script loads a template, updates the title cell, and writes a notebook.

Script path:

$JUPYTER_NOTEBOOK_CLI (installed default: $CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py)
Temp and output conventions
Use tmp/jupyter-notebook/ for intermediate files; delete when done.
Write final artifacts under output/jupyter-notebook/ when working in this repo.
Use stable, descriptive filenames (for example, ablation-temperature.ipynb).
Dependencies (install only when needed)

Prefer uv for dependency management.

Optional Python packages for local notebook execution:

uv pip install jupyterlab ipykernel


The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

Environment

No required environment variables.

Reference map
references/experiment-patterns.md: experiment structure and heuristics.
references/tutorial-patterns.md: tutorial structure and teaching flow.
references/notebook-structure.md: notebook JSON shape and safe editing rules.
references/quality-checklist.md: final validation checklist.
Weekly Installs
1.6K
Repository
openai/skills
GitHub Stars
18.0K
First Seen
Feb 7, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass