---
rating: ⭐⭐⭐
title: jupyter
url: https://skills.sh/openhands/skills/jupyter
---

# jupyter

skills/openhands/skills/jupyter
jupyter
Installation
$ npx skills add https://github.com/openhands/skills --skill jupyter
SKILL.md
Jupyter Notebook Guide

Notebooks are JSON files. Cells are in nb['cells'], each has source (list of strings) and cell_type ('code', 'markdown', or 'raw').

Modifying Notebooks
import json
with open('notebook.ipynb') as f:
    nb = json.load(f)
# Modify nb['cells'][i]['source'], then:
with open('notebook.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)

Executing & Converting
jupyter nbconvert --to notebook --execute --inplace notebook.ipynb  # Execute in place
jupyter nbconvert --to html notebook.ipynb      # Convert to HTML
jupyter nbconvert --to script notebook.ipynb    # Convert to Python
jupyter nbconvert --to markdown notebook.ipynb  # Convert to Markdown

Finding Code
grep -n "search_term" notebook.ipynb

Cell Structure
# Code cell
{"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["code\n"]}
# Markdown cell
{"cell_type": "markdown", "metadata": {}, "source": ["# Title\n"]}

Clear Outputs
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        cell['outputs'] = []
        cell['execution_count'] = None

Weekly Installs
88
Repository
openhands/skills
GitHub Stars
93
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass