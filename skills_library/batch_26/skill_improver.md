---
title: skill-improver
url: https://skills.sh/heyvhuang/ship-faster/skill-improver
---

# skill-improver

skills/heyvhuang/ship-faster/skill-improver
skill-improver
Installation
$ npx skills add https://github.com/heyvhuang/ship-faster --skill skill-improver
SKILL.md
Skill Improver

Retrospect and improve Skills/Workflows based on real execution artifacts, making the skill chain more stable with use.

Input (pass path only)
run_dir: runs/<workflow>/active/<run_id>/ (or openspec/changes/<change-id>/)
Output
improvements.md: Improvement suggestions (can be directly converted to change tasks)
Optional: Minimal patch to relevant SKILL.md (only change what's necessary)
Process
Read logs/state.json and logs/events.jsonl, extract:
Failure points (error types, frequency, missing context)
Time bottlenecks (repetitive steps, ineffective searches, excessive context)
Manual confirmation points (whether too early/too late/missing)
Check artifact contracts:
Whether each step has persisted output
Whether only paths are passed instead of content
Whether there are inconsistent naming/paths
Output improvement suggestions (sorted by benefit):
Prompt/trigger word optimization
I/O contract completion (add required fields, fix artifact file names)
Error handling and rejection strategies
Suggest new deterministic scripts (only when necessary)
Output Template (recommended)
Overview: Core issues from this run
Top Issues (high → low): Each includes "symptom/root cause/fix suggestion/related skill/suggested change point"
Suggested Minimal Change List: Listed by file
Weekly Installs
49
Repository
heyvhuang/ship-faster
GitHub Stars
338
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass