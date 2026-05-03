---
title: eval-systematic-optimization
url: https://skills.sh/cklxx/elephant.ai/eval-systematic-optimization
---

# eval-systematic-optimization

skills/cklxx/elephant.ai/eval-systematic-optimization
eval-systematic-optimization
Installation
$ npx skills add https://github.com/cklxx/elephant.ai --skill eval-systematic-optimization
SKILL.md
eval-systematic-optimization

Run baseline evaluation and failure clustering for foundation-suite.

Requirements
Go toolchain available (go in PATH).
Repo root as working directory (or pass cwd).
Constraints
Baseline command timeout: 600s.
Default baseline output path: /tmp/foundation-suite-<tag>-baseline.
analyze requires a valid JSON result file path.
Focus is conflict-family optimization, not single-case overfitting.
Usage
# Run baseline
python3 skills/eval-systematic-optimization/run.py '{"action":"baseline","tag":"r12"}'

# Analyze failures
python3 skills/eval-systematic-optimization/run.py '{"action":"analyze","result_file":"/tmp/foundation-suite-r12-baseline/foundation_suite_cases.json"}'

Weekly Installs
9
Repository
cklxx/elephant.ai
GitHub Stars
10
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass