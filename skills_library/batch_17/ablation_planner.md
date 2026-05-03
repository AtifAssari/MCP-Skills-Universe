---
title: ablation-planner
url: https://skills.sh/wanshuiyin/auto-claude-code-research-in-sleep/ablation-planner
---

# ablation-planner

skills/wanshuiyin/auto-claude-code-research-in-sleep/ablation-planner
ablation-planner
Installation
$ npx skills add https://github.com/wanshuiyin/auto-claude-code-research-in-sleep --skill ablation-planner
SKILL.md
Ablation Planner

Systematically design ablation studies that answer the questions reviewers will ask. Codex leads the design (reviewer perspective), CC reviews feasibility and implements.

Context: $ARGUMENTS
When to Use
Main results pass /result-to-claim with claim_supported = yes or partial
User explicitly requests ablation planning
/auto-review-loop reviewer identifies missing ablations
Workflow
Step 1: Prepare Context

CC reads available project files to build the full picture:

Method description and components (from docs/research_contract.md or project CLAUDE.md)
Current experiment results (from EXPERIMENT_LOG.md, EXPERIMENT_TRACKER.md, or W&B)
Confirmed and intended claims (from result-to-claim output or project notes)
Available compute resources (from CLAUDE.md server config, if present)
Step 2: Codex Designs Ablations
mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    You are a rigorous ML reviewer planning ablation studies.
    Given this method and results, design ablations that:

    1. Isolate the contribution of each novel component
    2. Answer questions reviewers will definitely ask
    3. Test sensitivity to key hyperparameters
    4. Compare against natural alternative design choices

    Method: [description from project files]
    Components: [list of removable/replaceable components]
    Current results: [key metrics from experiments]
    Claims: [what we claim and current evidence]

    For each ablation, specify:
    - name: what to change (e.g., "remove module X", "replace Y with Z")
    - what_it_tests: the specific question this answers
    - expected_if_component_matters: what we predict if the component is important
    - priority: 1 (must-run) to 5 (nice-to-have)

    Also provide:
    - coverage_assessment: what reviewer questions these ablations answer
    - unnecessary_ablations: experiments that seem useful but won't add insight
    - suggested_order: run order optimized for maximum early information
    - estimated_compute: total GPU-hours estimate

Step 3: Parse Ablation Plan

Normalize Codex response into structured format:

## Ablation Plan

### Component Ablations (highest priority)
| # | Name | What It Tests | Expected If Matters | Priority |
|---|------|---------------|---------------------|----------|
| 1 | remove module X | contribution of X | performance drops on metric Y | 1 |
| 2 | replace X with simpler Z | value of learned vs fixed | drops, especially on dataset A | 2 |

### Hyperparameter Sensitivity
| # | Parameter | Values to Test | What It Tests | Priority |
|---|-----------|---------------|---------------|----------|
| 3 | lambda | [0.01, 0.1, 1.0] | sensitivity to regularization | 3 |

### Design Choice Comparisons
| # | Name | What It Tests | Priority |
|---|------|---------------|----------|
| 4 | joint vs separate matching | whether joint adds value | 4 |

### Coverage Assessment
[What reviewer questions these ablations answer]

### Unnecessary Ablations
[Experiments that seem useful but won't add insight — skip these]

### Run Order
[Optimized for maximum early information]

### Estimated Compute
[Total GPU-hours]

Step 4: CC Reviews Feasibility

Before running anything, CC checks:

Compute budget: can we afford all ablations with available GPUs?
Code changes: which ablations need code modifications vs config-only changes?
Dependencies: which ablations can run in parallel?
Cuts: if budget is tight, propose removing lower-priority ablations and ask Codex to confirm
Step 5: Implement and Run
Create configs/scripts for each ablation (config-only changes first)
Smoke test each ablation before full run
Run in suggested order, using descriptive names (e.g., ablation-no-module-X)
Track results in EXPERIMENT_LOG.md
After all ablations complete → update findings.md with insights
Rules
Codex leads the design. CC does not pre-filter or bias the ablation list before Codex sees it. Codex thinks like a reviewer; CC thinks like an engineer.
Every ablation must have a clear what_it_tests and expected_if_component_matters. No "just try it" experiments.
Config-only ablations take priority over those needing code changes (faster, less error-prone).
If total compute exceeds budget, CC proposes cuts and asks Codex to re-prioritize — don't silently drop ablations.
Component ablations (remove/replace) take priority over hyperparameter sweeps.
Do not generate ablations for components identical to the baseline (no-op ablations).
Record all ablation results in EXPERIMENT_LOG.md, including negative results (component removal had no effect = important finding).
Weekly Installs
74
Repository
wanshuiyin/auto…in-sleep
GitHub Stars
7.9K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass