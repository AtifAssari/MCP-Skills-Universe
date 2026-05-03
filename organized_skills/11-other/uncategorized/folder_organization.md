---
rating: ⭐⭐⭐
title: folder-organization
url: https://skills.sh/delphine-l/claude_global/folder-organization
---

# folder-organization

skills/delphine-l/claude_global/folder-organization
folder-organization
Installation
$ npx skills add https://github.com/delphine-l/claude_global --skill folder-organization
SKILL.md
Folder Organization Best Practices

Expert guidance for organizing project directories, establishing file naming conventions, and maintaining clean, navigable project structures for research and development work.

When to Use This Skill
Setting up new projects
Reorganizing existing projects
Establishing team conventions
Creating reproducible research structures
Managing data-intensive projects
Core Principles
Predictability - Standard locations for common file types
Scalability - Structure grows gracefully with project
Separation of Concerns - Code, data, documentation, outputs separated
Discoverability - Easy for others (and future you) to navigate
Version Control Friendly - Large/generated files excluded appropriately
Quick Reference: Standard Project Structure

Use the structure matching your project type. Full templates in project-structures.md.

Research/Analysis: data/{raw,processed,external}, notebooks/, src/, scripts/, tests/, docs/, results/, config/

Development: src/package_name/, tests/, docs/, examples/, .github/workflows/

Bioinformatics: data/{raw,reference,processed}, workflows/, config/, scripts/, results/, logs/

Data Analysis with Notebooks: notebooks/, figures/, data/, tests/, scripts/, docs/, archives/

Add MANIFEST.md files for token-efficient navigation (see manifest-system.md).

File Naming Rules

Detailed conventions in naming-conventions.md. Key rules:

Use lowercase with hyphens or underscores (not spaces or CamelCase)
Be descriptive but concise - process-telomere-data.py not script.py
Use consistent separators - hyphens for files, underscores for Python modules
Include version/date for important outputs - report-2026-01-23.pdf
Zero-pad sequences - 01-exploration.ipynb, 02-analysis.ipynb
Standardize session notes in session-saves/ directory
Version Control

DO commit: Source code, documentation, config files, small test data (<1MB), requirements files, READMEs

DON'T commit: Large data files, generated outputs, environment dirs, logs, temp files, API keys/secrets

.gitignore Template
# Claude Code
.claude/

# Python
__pycache__/
*.py[cod]
.venv/
venv/

# Jupyter
.ipynb_checkpoints/

# Data
data/raw/
data/processed/
*.fastq.gz
*.bam

# Outputs
results/
outputs/
*.png
*.pdf

# Logs & Environment
logs/
*.log
.env
.DS_Store

Data Organization
Never modify raw data - keep originals in data/raw/ (read-only if possible)
Document data provenance (source, download date)
Use hierarchy: raw/ -> interim/ -> processed/ -> external/
Common Anti-Patterns

Avoid these patterns:

Flat structure: Everything in root directory with no organization
Ambiguous naming: notebook1.ipynb, test.ipynb, analysis_new.ipynb
Mixed concerns: Data files and output images inside src/ directory
Deprecation Strategy

Deprecate rather than delete to maintain history and recovery options. Full guide in deprecation-guide.md.

Key pattern:

Create deprecated/ subdirectory with descriptive name
Move old files there
Write README.md explaining what, when, why, and how to recover
For scattered deprecated dirs, consolidate to single root deprecated/
Project Reorganization

Full systematic guide in reorganization-guide.md. Critical steps:

Update all file paths in scripts and notebooks after moving files
Search for references: grep -r "\.json\|\.csv\|\.png" --include="*.ipynb" --include="*.py"
Verify file counts match expectations (no files lost)
Remove temp files (.bak, .ipynb_checkpoints)
Test that notebooks/scripts still run correctly
Documentation Standards

Full guide in documentation-organization.md. Key points:

Every project needs a README with: description, installation, usage, structure, data, results
After major changes, create dated summary documents
Consolidate scattered docs into documentation/ directory
Keep only README.md, LICENSE, .gitignore in project root
MANIFEST System

Token-efficient project navigation system. Full documentation in manifest-system.md.

Provides 85-90% token reduction for session startup
Root MANIFEST.md gives complete project overview in ~1,500 tokens
Subdirectory MANIFESTs for data/, figures/, scripts/, documentation/
Update at end of every session with /update-manifest
Project Cleanup: Identifying Essential Files

Detailed process in deprecation-guide.md (section "Project Cleanup"). Summary:

Analyze notebooks to find referenced figures
Map figures to generating scripts
Move unused files to deprecated/ with descriptive subdirectory names
Document what was kept in MINIMAL_ESSENTIAL_FILES.md
Verify notebooks still work with cleaned structure
Integration with Other Skills
python-environment - Environment setup and management
claude-collaboration - Team workflow best practices
jupyter-notebook-analysis - Notebook organization standards
data-backup - Backup system should include MANIFESTs
project-sharing - Include MANIFESTs in shared packages
Quick Setup
# Create standard research project structure
mkdir -p data/{raw,processed,external} notebooks scripts src tests docs results config
touch README.md .gitignore environment.yml

Supporting Files
File	Contents
project-structures.md	Detailed directory templates for all project types
naming-conventions.md	File naming rules, patterns, and session notes storage
reorganization-guide.md	Step-by-step reorganization, path updates, verification
deprecation-guide.md	Deprecation strategy, consolidation, essential file identification
documentation-organization.md	Documentation standards, change summaries, doc directory structure
manifest-system.md	Complete MANIFEST system: templates, commands, workflows, best practices
References and Resources
Cookiecutter Data Science
A Quick Guide to Organizing Computational Biology Projects
Good Enough Practices in Scientific Computing
Weekly Installs
114
Repository
delphine-l/claude_global
GitHub Stars
12
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass