---
title: analyze-results
url: https://skills.sh/wanshuiyin/auto-claude-code-research-in-sleep/analyze-results
---

# analyze-results

skills/wanshuiyin/auto-claude-code-research-in-sleep/analyze-results
analyze-results
Installation
$ npx skills add https://github.com/wanshuiyin/auto-claude-code-research-in-sleep --skill analyze-results
SKILL.md
Analyze Experiment Results

Analyze: $ARGUMENTS

Workflow
Step 1: Locate Results

Find all relevant JSON/CSV result files:

Check figures/, results/, or project-specific output directories
Parse JSON results into structured data
Step 2: Build Comparison Table

Organize results by:

Independent variables: model type, hyperparameters, data config
Dependent variables: primary metric (e.g., perplexity, accuracy, loss), secondary metrics
Delta vs baseline: always compute relative improvement
Step 3: Statistical Analysis
If multiple seeds: report mean +/- std, check reproducibility
If sweeping a parameter: identify trends (monotonic, U-shaped, plateau)
Flag outliers or suspicious results
Step 4: Generate Insights

For each finding, structure as:

Observation: what the data shows (with numbers)
Interpretation: why this might be happening
Implication: what this means for the research question
Next step: what experiment would test the interpretation
Step 5: Update Documentation

If findings are significant:

Propose updates to project notes or experiment reports
Draft a concise finding statement (1-2 sentences)
Output Format

Always include:

Raw data table
Key findings (numbered, concise)
Suggested next experiments (if any)
Weekly Installs
100
Repository
wanshuiyin/auto…in-sleep
GitHub Stars
7.9K
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass