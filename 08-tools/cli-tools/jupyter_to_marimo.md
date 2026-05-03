---
rating: ⭐⭐
title: jupyter-to-marimo
url: https://skills.sh/marimo-team/skills/jupyter-to-marimo
---

# jupyter-to-marimo

skills/marimo-team/skills/jupyter-to-marimo
jupyter-to-marimo
Installation
$ npx skills add https://github.com/marimo-team/skills --skill jupyter-to-marimo
Summary

Convert Jupyter notebooks to marimo Python scripts with CLI-driven transformation and cleanup guidance.

Use uvx marimo convert <notebook.ipynb> -o <notebook.py> to generate marimo-compatible .py files without local installation
Run marimo check before and after manual edits to catch syntax and compatibility issues
Common cleanup tasks include removing Jupyter artifacts (%magic commands, display() calls), verifying package metadata, and ensuring final cell expressions render correctly
Includes reference guides for porting ipywidgets to marimo equivalents, converting MathJax to KaTeX, and adding environment variable configuration via EnvConfig widget
SKILL.md
Converting Jupyter Notebooks to Marimo

IMPORTANT: When asked to translate a notebook, ALWAYS run uvx marimo convert <notebook.ipynb> -o <notebook.py> FIRST before reading any files. This saves precious tokens - reading large notebooks can consume 30k+ tokens, while the converted .py file is much smaller and easier to work with.

Steps
Convert using the CLI

Run the marimo convert command via uvx so no install is needed:

uvx marimo convert <notebook.ipynb> -o <notebook.py>


This generates a marimo-compatible .py file from the Jupyter notebook.

Run marimo check on the output
uvx marimo check <notebook.py>


Fix any issues that are reported before continuing.

Review and clean up the converted notebook

Read the generated .py file and apply the following improvements:

Ensure the script metadata block lists all required packages. The converter may miss some.
Drop leftover Jupyter artifacts like display() calls, or %magic commands that don't apply in marimo.
Make sure the final expression of each cell is the value to render. Indented or conditional expressions won't display.
If the original notebook requires environment variables via an input, consider adding the EnvConfig widget from wigglystuff. Details can be found here.
If the original notebook uses ipywidgets, see references/widgets.md for a full mapping of ipywidgets to marimo equivalents, including patterns for callbacks, linking, and anywidget integration.
If the notebook contains LaTeX, see references/latex.md for how to port MathJax syntax to KaTeX (which marimo uses).
Run marimo check again after your edits to confirm nothing was broken.
Weekly Installs
1.2K
Repository
marimo-team/skills
GitHub Stars
127
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass