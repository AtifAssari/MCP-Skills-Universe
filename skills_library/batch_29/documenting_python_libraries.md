---
title: documenting-python-libraries
url: https://skills.sh/wdm0006/python-skills/documenting-python-libraries
---

# documenting-python-libraries

skills/wdm0006/python-skills/documenting-python-libraries
documenting-python-libraries
Installation
$ npx skills add https://github.com/wdm0006/python-skills --skill documenting-python-libraries
SKILL.md
Python Library Documentation
Docstring Style (Google)
def encode(latitude: float, longitude: float, *, precision: int = 12) -> str:
    """Encode geographic coordinates to a quadtree string.

    Args:
        latitude: The latitude in degrees (-90 to 90).
        longitude: The longitude in degrees (-180 to 180).
        precision: Number of characters in output. Defaults to 12.

    Returns:
        A string representing the encoded location.

    Raises:
        ValidationError: If coordinates are out of valid range.

    Example:
        >>> encode(37.7749, -122.4194)
        '9q8yy9h7wr3z'
    """

Sphinx Quick Setup
# Install
pip install sphinx furo myst-parser sphinx-copybutton

# Initialize
sphinx-quickstart docs/


conf.py essentials:

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Google docstrings
    'myst_parser',          # Markdown support
]
html_theme = 'furo'

pyproject.toml Dependencies
[project.optional-dependencies]
docs = [
    "sphinx>=7.0",
    "furo>=2024.0",
    "myst-parser>=2.0",
]

README Template
# Package Name

[![PyPI](https://badge.fury.io/py/package.svg)](https://pypi.org/project/package/)

Short description of what it does.

## Installation

pip install package

## Quick Start

from package import function
result = function(args)

## Documentation

Full docs at [package.readthedocs.io](https://package.readthedocs.io/)

ReadTheDocs (.readthedocs.yaml)
version: 2
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
sphinx:
  configuration: docs/conf.py
python:
  install:
    - method: pip
      path: .
      extra_requirements: [docs]


For detailed setup, see:

SPHINX_CONFIG.md - Full Sphinx configuration
TUTORIALS.md - Tutorial writing guide
Checklist
README:
- [ ] Clear project description
- [ ] Installation instructions
- [ ] Quick start example
- [ ] Link to full documentation

API Docs:
- [ ] All public functions documented
- [ ] Args, Returns, Raises sections
- [ ] Examples in docstrings
- [ ] Type hints included

Learn More

This skill is based on the Documentation section of the Guide to Developing High-Quality Python Libraries by Will McGinnis. See these posts for deeper coverage:

Writing Effective Docstrings
Getting Started with Sphinx
Automating Docs Deployment
Documenting Your Library's API
Weekly Installs
22
Repository
wdm0006/python-skills
GitHub Stars
24
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass