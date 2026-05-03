---
rating: ⭐⭐
title: beo-writing-skills
url: https://skills.sh/minhtri2710/skills/beo-writing-skills
---

# beo-writing-skills

skills/minhtri2710/skills/beo-writing-skills
beo-writing-skills
Installation
$ npx skills add https://github.com/minhtri2710/skills --skill beo-writing-skills
SKILL.md
Beo Writing Skills
Overview

See ../reference/references/shared-hard-gates.md § Shared References Convention.

This skill teaches a strict test-first loop for beo skills.

Core principle: do not revise or ship a skill until it has first failed under a realistic pressure scenario.

Hard Gates

If the condition is subjective guidance (e.g., "write clearly", "prefer small skills"), express it as a GUIDELINE, not a HARD-GATE.

The Core Cycle: RED -> GREEN -> REFACTOR
RED -> create realistic pressure scenarios and confirm failure without the skill
GREEN -> write the minimal skill and rerun the same scenarios with the skill present
REFACTOR -> close loopholes, generalize the principle, and remove overfit or low-value wording

Use references/writing-skills-operations.md for the exact RED/GREEN/REFACTOR execution flow and documentation steps.

Handoff

After the skill survives RED/GREEN/REFACTOR:

run the validation flow from references/writing-skills-operations.md
document the work using references/creation-log-template.md
keep pressure-test artifacts clear enough to explain why the skill changed
Success Criteria

A beo skill is in good shape when:

it survives realistic pressure
it cites or reflects the rule clearly enough to follow it
it avoids obvious loopholes
it generalizes beyond the exact original examples
Context Budget

Follow ../reference/references/shared-hard-gates.md § Context Budget Protocol. Skill-specific checkpoint: see references/writing-skills-operations.md for the full procedure.

Red Flags & Anti-Patterns
Skill has no Hard Gates section (every skill must gate entry)
Skill duplicates protocol content instead of referencing beo-reference
Pressure tests don't cover the skill's specific failure modes
Skill reads STATE.json but doesn't validate schema_version
Eval fixtures use non-canonical status values
References

Load when needed:

references/writing-skills-operations.md — exact RED/GREEN/REFACTOR and validation flow
references/creation-log-template.md — CREATION-LOG.md template
references/pressure-test-template.md — pressure scenario templates
Weekly Installs
15
Repository
minhtri2710/skills
GitHub Stars
1
First Seen
Mar 30, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass