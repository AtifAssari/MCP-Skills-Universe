---
rating: ⭐⭐
title: eta
url: https://skills.sh/elliotjlt/claude-skill-potions/eta
---

# eta

skills/elliotjlt/claude-skill-potions/eta
eta
Installation
$ npx skills add https://github.com/elliotjlt/claude-skill-potions --skill eta
SKILL.md
ETA
Instructions
Step 1: Gather Task Context

When triggered, collect:

Task description from the user
Path to relevant codebase (default: current directory)
Number of files likely in scope (if known)
Step 2: Run Estimation
python scripts/estimate_task.py --task "<task_description>" --path "<codebase_path>"


Optional flags:

--files <n>: Override estimated files in scope
--json: Output structured JSON for programmatic use
Step 3: Present Estimate

Return the formatted estimate showing:

Task category (trivial/simple/medium/complex/major)
Scope analysis (files, lines, test coverage)
Time range (low-high estimate)
Breakdown by phase (analysis, implementation, testing, verification)
Risk factors with explanations
Checkpoint recommendations for long tasks
Step 4: Adjust Based on Feedback

If user provides more context:

Re-run with --files override if scope is clearer
Adjust category interpretation based on domain knowledge
NEVER
Start a complex task without providing an estimate first
Give single-point estimates (always provide ranges)
Ignore risk factors when they're detected
Skip the estimate for tasks over 15 minutes
Promise exact completion times
ALWAYS
Run the estimate script before non-trivial tasks
Show the breakdown so users understand where time goes
Flag risk factors visibly with explanations
Recommend checkpoints for tasks over 30 minutes
Update estimates if scope changes mid-task
Examples
Example 1: User asks about task duration

Input: "How long will it take to add user authentication?"

Workflow:

Run scripts/estimate_task.py --task "Add user authentication" --path .
Output shows:
Category: Complex
Estimated time: 24-53 minutes
Risk factors: High-risk changes, External dependencies
Recommendation: Break into phases with commits between each
Example 2: Before starting a feature

Input: "Add a dark mode toggle to settings"

Workflow:

Detect this is a non-trivial task (feature keyword)
Run scripts/estimate_task.py --task "Add dark mode toggle to settings" --path ./src
Present estimate: 10-22 minutes (Medium complexity)
Begin implementation with checkpoint plan
Example 3: Quick fix request

Input: "Fix the typo in the README"

Workflow:

Detect trivial task (typo keyword)
Run quick estimate: 3-6 minutes
Proceed immediately (no detailed breakdown needed for trivial tasks)
Weekly Installs
11
Repository
elliotjlt/claud…-potions
GitHub Stars
55
First Seen
Feb 3, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass