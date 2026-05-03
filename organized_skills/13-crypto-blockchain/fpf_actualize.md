---
rating: ⭐⭐⭐
title: fpf:actualize
url: https://skills.sh/neolabhq/context-engineering-kit/fpf:actualize
---

# fpf:actualize

skills/neolabhq/context-engineering-kit/fpf:actualize
fpf:actualize
Installation
$ npx skills add https://github.com/neolabhq/context-engineering-kit --skill fpf:actualize
SKILL.md
Actualize Knowledge Base

This command is a core part of maintaining a living assurance case. It keeps your FPF knowledge base (.fpf/) in sync with the evolving reality of your project's codebase.

The command performs a three-part audit against recent git changes to surface potential context drift, stale evidence, and outdated decisions. This aligns with the Observe phase of the FPF Canonical Evolution Loop (B.4) and helps manage Epistemic Debt (B.3.4).

Action (Run-Time)
Step 1: Check Git Changes

Run git commands to identify changes since last actualization:

# Get current commit hash
git rev-parse HEAD

# Check for changes since last known baseline
# (Read .fpf/.baseline file if it exists, otherwise use initial commit)
git diff --name-only <baseline_commit> HEAD

# List all changed files
git diff --stat <baseline_commit> HEAD

Step 2: Analyze Report for Context Drift

Review changed files for core project configuration:

package.json, go.mod, Cargo.toml, requirements.txt
Dockerfile, docker-compose.yml
.env.example, config files

If configuration files changed:

Re-read project structure (README, config files)
Compare detected context with .fpf/context.md
Present diff to user

Ask user if they want to update context.md

Step 3: Analyze Report for Evidence Staleness (Epistemic Debt)
Read all evidence files in .fpf/evidence/
Check carrier_ref field in each evidence file
Cross-reference with changed files from git diff
If a referenced file changed:
Flag the evidence as STALE
Note which hypothesis is affected
Step 4: Analyze Report for Decision Relevance
Read all DRR files in .fpf/decisions/
Trace back to source evidence and hypothesis files
If foundational files changed:
Flag the DRR as POTENTIALLY OUTDATED
Step 5: Update Baseline

Create/update .fpf/.baseline file:

# FPF Actualization Baseline
# Last actualized: 2025-01-15T16:00:00Z
commit: abc123def456

Step 6: Present Findings

Output a structured report:

## Actualization Report

**Baseline**: abc123 (2025-01-10)
**Current**: def456 (2025-01-15)
**Files Changed**: 42

### Context Drift

The following configuration files have changed:
- package.json (+5 dependencies)
- Dockerfile (base image updated)

**Action Required**: Review and update `.fpf/context.md` if constraints have changed.

### Stale Evidence (3 items)

| Evidence | Hypothesis | Changed File |
|----------|------------|--------------|
| ev-benchmark-api | api-optimization | src/api/handler.ts |
| ev-test-auth | auth-module | src/auth/login.ts |
| ev-perf-db | db-indexing | migrations/002.sql |

**Action Required**: Re-validate to refresh evidence for affected hypotheses.

### Decisions to Review (1 item)

| DRR | Affected By |
|-----|-------------|
| DRR-2025-01-10-api-design | src/api/handler.ts changed |

**Action Required**: Consider re-evaluating decision via `/fpf:propose-hypotheses`.

### Summary

- Context drift detected: YES
- Stale evidence: 3 items
- Decisions to review: 1 item

Run `/fpf:decay` for detailed freshness management.

File: .fpf/.baseline

Track the last actualization point:

# FPF Actualization Baseline
last_actualized: 2025-01-15T16:00:00Z
commit: abc123def456789
branch: main

When to Run
Before starting new work: Ensure knowledge base is current
After major changes: Sync evidence with code changes
Weekly maintenance: Part of regular hygiene
Before decisions: Ensure evidence is still valid
Weekly Installs
353
Repository
neolabhq/contex…ring-kit
GitHub Stars
942
First Seen
Feb 23, 2026