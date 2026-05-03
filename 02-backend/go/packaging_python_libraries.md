---
rating: ⭐⭐⭐
title: packaging-python-libraries
url: https://skills.sh/wdm0006/python-skills/packaging-python-libraries
---

# packaging-python-libraries

skills/wdm0006/python-skills/packaging-python-libraries
packaging-python-libraries
Installation
$ npx skills add https://github.com/wdm0006/python-skills --skill packaging-python-libraries
SKILL.md
Python Library Packaging
pyproject.toml Essentials
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-package"
version = "1.0.0"
description = "Short description"
readme = "README.md"
requires-python = ">=3.10"
license = {text = "MIT"}
dependencies = []

[project.optional-dependencies]
dev = ["pytest>=7.0", "ruff>=0.1", "mypy>=1.0"]

[project.urls]
Homepage = "https://github.com/user/package"
Documentation = "https://package.readthedocs.io"

[project.scripts]
mycli = "my_package.cli:main"

[tool.setuptools.packages.find]
where = ["src"]

Building
pip install build
python -m build              # Creates dist/
twine check dist/*           # Validate

Publishing to PyPI

First time setup:

# Create API token at pypi.org/manage/account/token/
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-xxx...


Publish:

twine upload --repository testpypi dist/*  # Test first
twine upload dist/*                         # Production

GitHub Actions (Trusted Publishing)
# .github/workflows/publish.yml
on:
  release:
    types: [published]

jobs:
  publish:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install build && python -m build
      - uses: pypa/gh-action-pypi-publish@release/v1

Dependency Best Practices
# DO: Minimum versions
dependencies = ["requests>=2.28", "click>=8.0"]

# DON'T: Exact pins (locks users)
dependencies = ["requests==2.28.1"]

# DO: Optional for features
[project.optional-dependencies]
cli = ["click>=8.0"]

Including Package Data
[tool.setuptools.package-data]
my_package = ["py.typed", "data/*.json"]

from importlib.resources import files
data = files("my_package.data").joinpath("file.json").read_text()


For detailed templates, see:

PYPROJECT_FULL.md - Complete pyproject.toml
CONDA.md - Conda packaging guide
Checklist
Before Release:
- [ ] pyproject.toml valid
- [ ] README.md informative
- [ ] LICENSE file exists
- [ ] Version set correctly
- [ ] twine check passes

After Release:
- [ ] pip install works
- [ ] Import works
- [ ] GitHub release created

Learn More

This skill is based on the Distribution section of the Guide to Developing High-Quality Python Libraries by Will McGinnis. See these posts for deeper coverage:

pyproject.toml Explained
Publishing PyGeohash
Weekly Installs
17
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