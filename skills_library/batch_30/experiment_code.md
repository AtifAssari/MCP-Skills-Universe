---
title: experiment-code
url: https://skills.sh/lingzhi227/agent-research-skills/experiment-code
---

# experiment-code

skills/lingzhi227/agent-research-skills/experiment-code
experiment-code
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill experiment-code
SKILL.md
Experiment Code

Generate and iteratively improve ML experiment code for research papers.

Input
$0 — Task: generate, improve, debug, plot
$1 — Research plan, idea description, or error message
References
Experiment prompts and patterns: ~/.claude/skills/experiment-code/references/experiment-prompts.md
Code patterns (error handling, repair, hill-climbing): ~/.claude/skills/experiment-code/references/code-patterns.md
Action: generate

Generate initial experiment code following this structure:

Plan experiments first — List all runs needed (hyperparameter sweeps, ablations, baselines)
Write self-contained code — All code in project directory, no external imports from reference repos
Include proper logging — Save results to JSON, print intermediate metrics
Generate figures — At minimum Figure_1.png and Figure_2.png
Mandatory Structure
project/
├── experiment.py      # Main experiment script
├── plot.py            # Visualization script
├── notes.txt          # Experiment descriptions and results
├── run_1/             # Results from run 1
│   └── final_info.json
├── run_2/
└── ...

Constraints
No placeholder code (pass, ..., raise NotImplementedError)
Must use actual datasets (not toy data unless explicitly requested)
PyTorch or scikit-learn preferred (no TensorFlow/Keras)
Each run uses: python experiment.py --out_dir=run_i
Action: improve

Improve existing experiment code:

Read current code and results
Reflect on what worked and what didn't
Apply targeted edits (prefer small edits over full rewrites)
Re-run and compare scores
Keep the best-performing code variant
Action: debug

Fix experiment code errors:

Read the error message (truncate to last 1500 chars if very long)
Identify the root cause
Apply minimal fix
Up to 4 retry attempts before changing approach
Action: plot

Generate publication-quality plots from experiment results:

Read all run_*/final_info.json files
Generate comparison plots with proper labels
Use the figure-generation skill for styling
Rules
Always plan experiments before writing code
After each run, document results in notes.txt
Include print statements explaining what results show
Method MUST not get 0% accuracy — verify accuracy calculations
Use seeds for reproducibility
Before each experiment include a print statement explaining exactly what the results are meant to show
Related Skills
Upstream: experiment-design, algorithm-design
Downstream: data-analysis, backward-traceability
See also: code-debugging, paper-to-code
Weekly Installs
128
Repository
lingzhi227/agen…h-skills
GitHub Stars
42
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass