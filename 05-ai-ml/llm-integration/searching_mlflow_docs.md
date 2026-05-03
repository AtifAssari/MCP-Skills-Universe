---
title: searching-mlflow-docs
url: https://skills.sh/mlflow/skills/searching-mlflow-docs
---

# searching-mlflow-docs

skills/mlflow/skills/searching-mlflow-docs
searching-mlflow-docs
Installation
$ npx skills add https://github.com/mlflow/skills --skill searching-mlflow-docs
SKILL.md
MLflow Documentation Search
Workflow
Fetch https://mlflow.org/docs/latest/llms.txt to find relevant page paths
Fetch the .md file at the identified path
Present results with verbatim code examples
Step 1: Fetch llms.txt Index
WebFetch(
  url: "https://mlflow.org/docs/latest/llms.txt",
  prompt: "Find links or references to [TOPIC]. List all relevant URLs."
)

Step 2: Fetch Target Documentation

Use the path from Step 1, always with .md extension:

WebFetch(
  url: "https://mlflow.org/docs/latest/[path].md",
  prompt: "Return all code blocks verbatim. Do not summarize."
)

Anti-Patterns

Do not use .html files — Fetch .md source files only.

Do not use WebSearch — Always start from llms.txt; web search returns outdated or third-party content.

Do not use vague prompts — "Extract complete documentation" allows summarization. Use "Return all code blocks verbatim. Do not summarize."

Do not use versioned paths — Always use /docs/latest/, never /docs/3.8/ or other versions unless the user explicitly requests a specific version.

Do not guess URLs — Always verify paths exist in llms.txt before fetching. Never construct documentation paths from assumptions.

Do not follow external links — Stay within mlflow.org/docs. Do not follow links to GitHub, PyPI, or third-party sites.

Do not mix sources — Use only MLflow docs. Do not combine with LangChain docs, OpenAI docs, or other external documentation.

Do not use llms.txt for non-GenAI topics — The llms.txt index covers LLM/GenAI documentation only. For classic ML tracking features, paths may differ.

Weekly Installs
237
Repository
mlflow/skills
GitHub Stars
36
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn