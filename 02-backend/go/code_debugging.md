---
rating: ⭐⭐
title: code-debugging
url: https://skills.sh/lingzhi227/agent-research-skills/code-debugging
---

# code-debugging

skills/lingzhi227/agent-research-skills/code-debugging
code-debugging
Installation
$ npx skills add https://github.com/lingzhi227/agent-research-skills --skill code-debugging
SKILL.md
Code Debugging

Systematically debug experiment code with structured error categorization and fix strategies.

Input
$0 — Error message, stderr output, or code file with issues
$1 — Optional: the code that produced the error
References
Debug patterns and state machine: ~/.claude/skills/code-debugging/references/debug-patterns.md
Workflow
Step 1: Categorize the Error
Category	Examples	Severity
SyntaxError	Invalid syntax, indentation	Low
ImportError	Missing module, wrong name	Low
RuntimeError	Division by zero, shape mismatch	Medium
TimeoutError	Infinite loop, too slow	Medium
OutputError	Missing files, wrong format	Medium
LogicError	Wrong results, 0% accuracy	High
Step 2: Analyze Root Cause
Read the error traceback (last 1500 chars if truncated)
Identify the exact line and variable causing the error
Check for common patterns:
Device mismatch (CPU vs GPU tensors)
Shape mismatch in matrix operations
Missing data normalization
Off-by-one errors in indexing
Incorrect loss function for task type
Step 3: Apply Fix Strategy

For syntax/import errors: Direct fix, single attempt For runtime errors: Fix and rerun, up to 4 retries For logic errors: Reflect on approach, consider alternative methods For timeout: Reduce dataset size, optimize bottleneck, add early stopping

Step 4: Reflect and Prevent

After fixing:

Explain why the error occurred
Identify which lines caused it
Describe the fix line-by-line
Note patterns to avoid in future code
Fix Strategy State Machine
Stage 0 (first attempt) → repost code as fresh
Stage 1 (second attempt) → repost or leave depending on severity
Stage 2 (third attempt) → regenerate from scratch if still failing

Rules
Prefer minimal targeted edits over full rewrites
Maximum 4-5 fix attempts before changing approach
Always truncate long error outputs to last 1500 characters
After fixing, verify the fix doesn't introduce new errors
Keep error history to avoid repeating the same mistakes
If 0% accuracy: check accuracy calculation first, then check data pipeline
Related Skills
Upstream: experiment-code
See also: paper-to-code, data-analysis
Weekly Installs
133
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