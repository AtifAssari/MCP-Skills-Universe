---
rating: ⭐⭐
title: cv-matcher-ai-data
url: https://skills.sh/neurongraph/skills_repo/cv-matcher-ai-data
---

# cv-matcher-ai-data

skills/neurongraph/skills_repo/cv-matcher-ai-data
cv-matcher-ai-data
Installation
$ npx skills add https://github.com/neurongraph/skills_repo --skill cv-matcher-ai-data
SKILL.md
CV Matcher for AI and Data Roles
Instructions
Read CVs from the specified directory, defaulting to current directory if unspecified. Look for .pdf or .docx files only
Extract experience, projects, and technologies from each CV
Map candidates to roles based on criteria below
Generate Output1 (role-based analysis with rankings)
Request open demands from user (Account, Role, Number of resources)
Generate Output2 (candidate-to-demand matching)
Role Classification Criteria

ML Engineer: Machine Learning experience, data analysis, ML-related Python packages

GenAI Engineer: Python, LLMs, prompt engineering, GenAI packages. Agents/agentic frameworks preferred

AI Architect: ML/Data Platform/Application Architecture background with Architect or Solution Designer role. Python, LLMs, prompt engineering, GenAI packages, agents/agentic frameworks preferred

Data Engineer: ETL experience using Python or SQL frameworks (PySpark, PySQL, dbt, Databricks, AWS Glue)

Output Specifications
Output1: Role Analysis

Markdown tables by role, ranking candidates by skill match with short justifications. Include summary table showing each candidate's best-matched roles.

Output2: Demand Matching

Match candidates to open demands by role. If demand > supply, fill minimum one role per account. If supply > demand, assign more candidates than requested based on role match. Output markdown table with assignments and justifications.

Weekly Installs
9
Repository
neurongraph/skills_repo
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass