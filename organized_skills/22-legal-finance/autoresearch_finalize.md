---
rating: ⭐⭐⭐
title: autoresearch-finalize
url: https://skills.sh/davebcn87/pi-autoresearch/autoresearch-finalize
---

# autoresearch-finalize

skills/davebcn87/pi-autoresearch/autoresearch-finalize
autoresearch-finalize
Installation
$ npx skills add https://github.com/davebcn87/pi-autoresearch --skill autoresearch-finalize
SKILL.md
Finalize Autoresearch

Turn a noisy autoresearch branch into clean, independent branches — one per logical change, each starting from the merge-base.

Step 1 — Analyze and Propose Groups
Read autoresearch.jsonl. Filter to kept experiments only.
Read autoresearch.md for context.
Expand all short commit hashes to full hashes: git rev-parse <short_hash>
Get the merge-base: git merge-base HEAD main
For each kept commit, get the diff stat (use $BASE..<commit> for the first, <prev_kept>..<commit> for subsequent).
Group kept commits into logical changesets:
Preserve application order. Group N comes before Group N+1.
No two groups may touch the same file. Each branch is applied to merge-base independently — overlapping files would conflict. If two groups touch the same file, merge them into one group.
Watch for cross-file dependencies. Each branch is independent, so if group 1 adds an API in api.js and group 2 calls it in parser.js, group 2's branch won't work in isolation. When proposing groups, flag dependencies: "group 2 depends on group 1 — review together." If the dependency is tight, merge the groups.
Keep each group small and focused. One idea, one theme per group.
Don't hardcode a count. Could be 2, could be 15.

Present the proposed grouping to the user:

Proposed branches (each from merge-base, independent):

1. **Switch test runner to forks pool** (commits abc1234, def5678)
   Files: vitest.config.ts, package.json
   Metric: 42.3s → 38.1s (-9.9%)

2. **Tune worker count and timeouts** (commits ghi9012, jkl3456)
   Files: test/setup.ts
   Metric: 38.1s → 31.7s (-16.8%)


Wait for approval before proceeding.

Step 2 — Write groups.json and Run

Write groups.json:

{
  "base": "<full merge-base hash>",
  "trunk": "main",
  "final_tree": "<full hash of current HEAD>",
  "goal": "short-slug",
  "groups": [
    {
      "title": "Switch to forks pool",
      "body": "Why + what changed.\n\nExperiments: #3, #5\nMetric: total_time 42.3s → 38.1s (-9.9%)",
      "last_commit": "<full hash of last kept commit in this group>",
      "slug": "forks-pool"
    }
  ]
}


Key rules:

last_commit must be a full hash. Expand from jsonl short hashes with git rev-parse.
No two groups may share a file. The script validates this and fails if violated.

Then run:

bash <SKILL_DIR>/finalize.sh /tmp/groups.json


The script creates one branch per group from the merge-base, verifies the union matches the original branch, and prints a summary with all branches, cleanup commands, and any ideas from autoresearch.ideas.md.

On creation failure: rolls back (deletes branches, restores original branch, pops stash). On verification failure: exits non-zero but leaves branches intact for inspection.

Step 3 — Report

After the script finishes, report to the user:

Branches created and what each contains
Overall metric improvement (baseline → best)
Show the cleanup commands from the script's summary output
Edge Cases
Only 1 kept experiment: One branch is fine — don't force splits.
Overlapping files between groups: The script fails with an error naming the file. Merge the overlapping groups and retry.
Non-experiment commits on the branch: Skip them — only process kept experiments from the jsonl.
Weekly Installs
9
Repository
davebcn87/pi-au…research
GitHub Stars
6.2K
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass