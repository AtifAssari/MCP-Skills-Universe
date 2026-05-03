---
title: eval
url: https://skills.sh/alirezarezvani/claude-skills/eval
---

# eval

skills/alirezarezvani/claude-skills/eval
eval
Installation
$ npx skills add https://github.com/alirezarezvani/claude-skills --skill eval
SKILL.md
/hub:eval — Evaluate Agent Results

Rank all agent results for a session. Supports metric-based evaluation (run a command), LLM judge (compare diffs), or hybrid.

Usage
/hub:eval                           # Eval latest session using configured criteria
/hub:eval 20260317-143022           # Eval specific session
/hub:eval --judge                   # Force LLM judge mode (ignore metric config)

What It Does
Metric Mode (eval command configured)

Run the evaluation command in each agent's worktree:

python {skill_path}/scripts/result_ranker.py \
  --session {session-id} \
  --eval-cmd "{eval_cmd}" \
  --metric {metric} --direction {direction}


Output:

RANK  AGENT       METRIC      DELTA      FILES
1     agent-2     142ms       -38ms      2
2     agent-1     165ms       -15ms      3
3     agent-3     190ms       +10ms      1

Winner: agent-2 (142ms)

LLM Judge Mode (no eval command, or --judge flag)

For each agent:

Get the diff: git diff {base_branch}...{agent_branch}
Read the agent's result post from .agenthub/board/results/agent-{i}-result.md
Compare all diffs and rank by:
Correctness — Does it solve the task?
Simplicity — Fewer lines changed is better (when equal correctness)
Quality — Clean execution, good structure, no regressions

Present rankings with justification.

Example LLM judge output for a content task:

RANK  AGENT    VERDICT                               WORD COUNT
1     agent-1  Strong narrative, clear CTA            1480
2     agent-3  Good data points, weak intro           1520
3     agent-2  Generic tone, no differentiation       1350

Winner: agent-1 (strongest narrative arc and call-to-action)

Hybrid Mode
Run metric evaluation first
If top agents are within 10% of each other, use LLM judge to break ties
Present both metric and qualitative rankings
After Eval
Update session state:
python {skill_path}/scripts/session_manager.py --update {session-id} --state evaluating

Tell the user:
Ranked results with winner highlighted
Next step: /hub:merge to merge the winner
Or /hub:merge {session-id} --agent {winner} to be explicit
Weekly Installs
818
Repository
alirezarezvani/…e-skills
GitHub Stars
13.4K
First Seen
Today
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass