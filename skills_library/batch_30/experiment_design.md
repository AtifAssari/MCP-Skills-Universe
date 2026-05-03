---
title: experiment-design
url: https://skills.sh/lingzhi227/agent-research-skills/experiment-design
---

# experiment-design

skills/lingzhi227/agent-research-skills/experiment-design
experiment-design
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill experiment-design
SKILL.md
Experiment Design

Design structured, progressive experiment plans for research papers.

Input
$0 — Research idea, plan, or method description
References
4-stage progressive experiment prompts: ~/.claude/skills/experiment-design/references/stage-prompts.md
Scripts
Generate experiment design
python ~/.claude/skills/experiment-design/scripts/design_experiments.py --plan research_plan.json --output experiment_design.json
python ~/.claude/skills/experiment-design/scripts/design_experiments.py --method "contrastive learning" --task classification --format markdown


Generates baselines, ablation matrix, hyperparameter grid, metric selection. Stdlib-only.

4-Stage Progressive Framework (from AI-Scientist-v2)
Stage 1: Initial Implementation
Focus on getting a basic working implementation
Use a simple dataset
Aim for basic functional correctness
Completion: at least one working (non-buggy) implementation
Stage 2: Baseline Tuning
Tune hyperparameters (learning rate, epochs, batch size)
Do NOT change model architecture
Test on at least TWO datasets
Completion: stable training curves, improvement over Stage 1
Stage 3: Creative Research
Explore novel improvements and insights
Be creative and think outside the box
Test on at least THREE datasets
Completion: demonstrated novel improvement
Stage 4: Ablation Studies
Systematic component analysis
Each ablation tests a different aspect
Use same datasets as Stage 3
Completion: all planned ablations done
Output Format
{
  "stages": [
    {
      "name": "initial_implementation",
      "goals": ["Basic working baseline", "Simple dataset"],
      "max_iterations": 5,
      "completion_criteria": "Working implementation with non-zero accuracy"
    }
  ],
  "baselines": ["Method A", "Method B"],
  "datasets": ["Dataset1", "Dataset2", "Dataset3"],
  "metrics": ["accuracy", "F1", "inference_time"],
  "ablation_components": ["component_A", "component_B"],
  "hyperparameter_grid": {
    "lr": [1e-4, 1e-3, 1e-2],
    "batch_size": [32, 64, 128]
  },
  "num_seeds": 3
}

Rules
Always start simple (Stage 1) before complex experiments
Each stage builds on the best result from the previous stage
Multi-seed evaluation for statistical significance
Document every experiment run in notes.txt
Generate figures for training curves and comparisons
Related Skills
Upstream: research-planning, idea-generation
Downstream: experiment-code, data-analysis
See also: paper-assembly
Weekly Installs
149
Repository
lingzhi227/agen…h-skills
GitHub Stars
42
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass