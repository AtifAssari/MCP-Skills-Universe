---
title: playwright-excel
url: https://skills.sh/rukkha1024/elderly-balance-assessment/playwright-excel
---

# playwright-excel

skills/rukkha1024/elderly-balance-assessment/playwright-excel
playwright-excel
Installation
$ npx skills add https://github.com/rukkha1024/elderly-balance-assessment --skill playwright-excel
SKILL.md
Playwright Excel Integration
Overview

Convert Playwright codegen scripts into Excel-driven automations with centralized config and required MCP validation.

Environment
Use the playwright conda environment.
Before running any Python command, run: conda run -n playwright python -c "import sys; print(sys.executable)"
Do not create or activate any venv or .venv.
Inputs
Playwright codegen script path
Excel .xlsx path
Mapping lines: "hardcoded_value" -> Excel[Sheet][FilterCol==FilterVal][DataCol]
Optional override: PLAYWRIGHT_TARGET_SUBJECT
Workflow
Analyze the Playwright script and the Excel structure (sheets, columns, sample rows).
Detect hardcoded .fill() values and confirm that each has a mapping; request clarification for mismatches.
Ensure dependencies in the playwright conda env (prefer conda install -n playwright, fall back to conda run -n playwright pip install).
Create or update config.yaml using centralized control (paths, patterns, column definitions, constants, tunables, shared texts).
Modify the Playwright script:
Add a config loader and an Excel loader (polars; see references/excel-loading.md).
Replace hardcoded values with data[...].
Always run Playwright MCP validation; if MCP is not running, start it from this repo before continuing (see references/mcp-validation.md).
When refactoring existing pipelines/logic, generate outputs and compare MD5 checksums with reference files (see references/md5-validation.md).
Run the updated script with conda run -n playwright python.
References
references/excel-loading.md
references/mcp-validation.md
references/md5-validation.md
references/examples.md
Weekly Installs
9
Repository
rukkha1024/elde…sessment
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass