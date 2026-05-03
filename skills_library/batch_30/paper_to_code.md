---
title: paper-to-code
url: https://skills.sh/lingzhi227/agent-research-skills/paper-to-code
---

# paper-to-code

skills/lingzhi227/agent-research-skills/paper-to-code
paper-to-code
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill paper-to-code
SKILL.md
Paper to Code

Convert a research paper into a complete, runnable code repository.

Input
$0 — Paper PDF path, paper text, or paper URL
References
Paper2Code prompts (planning, analysis, coding stages): ~/.claude/skills/paper-to-code/references/paper-to-code-prompts.md
Workflow (from Paper2Code)
Stage 1: Planning

Four-turn conversation to create a comprehensive plan:

Overall Plan: Extract methodology, experiments, datasets, hyperparameters, evaluation metrics
Architecture Design: Generate file list, Mermaid classDiagram, sequenceDiagram
Task Breakdown: Logic analysis per file, dependency-ordered task list, required packages
Configuration: Extract training details into config.yaml
Stage 2: Analysis

For each file in the task list (dependency order):

Conduct detailed logic analysis
Map paper methodology to code structure
Reference the config.yaml for all settings
Follow the UML class diagram interfaces strictly
Stage 3: Coding

For each file in dependency order:

Generate code with access to all previously generated files
Follow the design's data structures and interfaces exactly
Reference config.yaml — never fabricate configuration values
Write complete code — no TODOs or placeholders
Stage 4: Debugging (if needed)

If execution fails:

Collect error messages
Identify root cause using SEARCH/REPLACE diff format
Apply minimal fixes preserving original intent
Re-run until successful
Output Structure
reproduced_code/
├── config.yaml        # Training configuration
├── main.py            # Entry point
├── model.py           # Model architecture
├── dataset_loader.py  # Data loading
├── trainer.py         # Training loop
├── evaluation.py      # Metrics and evaluation
├── reproduce.sh       # Run script
└── requirements.txt   # Dependencies

Key Constraints
Dependency order: Each file is generated with access to all previously generated files
Interface contracts: Mermaid diagrams serve as rigid interface definitions across all stages
No fabrication: Only use configurations explicitly stated in the paper
Complete code: Every function must be fully implemented
Rules
Follow the paper's methodology exactly — do not invent improvements
Generate code in dependency order (data loading → model → training → evaluation → main)
Use config.yaml for all hyperparameters and settings
Every class/method in UML diagram must exist in code
Generate a reproduce.sh script for one-command execution
If paper details are ambiguous, note them explicitly
Related Skills
Upstream: literature-search
Downstream: experiment-code
See also: code-debugging, algorithm-design
Weekly Installs
126
Repository
lingzhi227/agen…h-skills
GitHub Stars
42
First Seen
1 day ago
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykWarn