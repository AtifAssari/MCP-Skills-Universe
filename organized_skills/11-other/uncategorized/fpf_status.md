---
rating: ⭐⭐⭐
title: fpf:status
url: https://skills.sh/neolabhq/context-engineering-kit/fpf:status
---

# fpf:status

skills/neolabhq/context-engineering-kit/fpf:status
fpf:status
Installation
$ npx skills add https://github.com/neolabhq/context-engineering-kit --skill fpf:status
SKILL.md
Status Check

Display the current state of the FPF knowledge base.

Action (Run-Time)
Check Directory Structure: Verify .fpf/ exists and contains required subdirectories.
Count Hypotheses: List files in each knowledge layer:
.fpf/knowledge/L0/ (Proposed)
.fpf/knowledge/L1/ (Verified)
.fpf/knowledge/L2/ (Validated)
.fpf/knowledge/invalid/ (Rejected)
Check Evidence Freshness: Scan .fpf/evidence/ for expired evidence.
Count Decisions: List files in .fpf/decisions/.
Report to user.
Status Report Format
## FPF Status

### Directory Structure
- [x] .fpf/ exists
- [x] knowledge/L0/ exists
- [x] knowledge/L1/ exists
- [x] knowledge/L2/ exists
- [x] evidence/ exists
- [x] decisions/ exists

### Current Phase
Based on hypothesis distribution: ABDUCTION | DEDUCTION | INDUCTION | DECISION | IDLE

### Hypothesis Counts

| Layer | Count | Status |
|-------|-------|--------|
| L0 (Proposed) | 3 | Awaiting verification |
| L1 (Verified) | 2 | Awaiting validation |
| L2 (Validated) | 1 | Ready for decision |
| Invalid | 1 | Rejected |

### Evidence Status

| Total | Fresh | Stale | Expired |
|-------|-------|-------|---------|
| 5 | 3 | 1 | 1 |

### Warnings

- 1 evidence file is EXPIRED: ev-benchmark-old-2024-06-15
- Consider running `/fpf:decay` to review stale evidence

### Recent Decisions

| DRR | Date | Winner |
|-----|------|--------|
| DRR-2025-01-15-use-redis | 2025-01-15 | redis-caching |

Phase Detection Logic

Determine current phase by examining the knowledge base state:

Condition	Phase	Next Step
No .fpf/ directory	NOT INITIALIZED	Run /fpf:propose-hypotheses
L0 > 0, L1 = 0, L2 = 0	ABDUCTION	Continue with verification
L1 > 0, L2 = 0	DEDUCTION	Continue with validation
L2 > 0, no recent DRR	INDUCTION	Continue with audit and decision
Recent DRR exists	DECISION COMPLETE	Review decision
All empty	IDLE	Run /fpf:propose-hypotheses
Evidence Freshness Check

For each evidence file in .fpf/evidence/:

Read the valid_until field from frontmatter
Compare with current date
Classify:
Fresh: valid_until > today + 30 days
Stale: valid_until > today but < today + 30 days
Expired: valid_until < today

If any evidence is stale or expired, warn the user and suggest /fpf:decay.

Example Output
## FPF Status

### Current Phase: DEDUCTION

You have 3 hypotheses in L0 awaiting verification.
Next step: Continue the FPF workflow to process L0 hypotheses.

### Hypothesis Counts

| Layer | Count |
|-------|-------|
| L0 | 3 |
| L1 | 0 |
| L2 | 0 |
| Invalid | 0 |

### Evidence Status

No evidence files yet (hypotheses not validated).

### No Warnings

All systems nominal.

Weekly Installs
354
Repository
neolabhq/contex…ring-kit
GitHub Stars
942
First Seen
Feb 23, 2026