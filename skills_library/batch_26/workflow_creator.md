---
title: workflow-creator
url: https://skills.sh/heyvhuang/ship-faster/workflow-creator
---

# workflow-creator

skills/heyvhuang/ship-faster/workflow-creator
workflow-creator
Installation
$ npx skills add https://github.com/heyvhuang/ship-faster --skill workflow-creator
SKILL.md
Workflow Creator

Create a new workflow-<slug>/ skill package that chains existing skills with Ship Faster-standard artifacts.

Hard rules (do not skip)
Compose skills, don't copy them: a workflow's job is orchestration. Do not paste long best-practice content from other skills into the workflow. Instead: map each step to a single existing skill and point to it.
One step = one skill: every step in workflow_spec.md must map to exactly one skill (or a tiny, verifiable manual action).
Missing required skill = stop: do not approximate a missing skill by rewriting its logic. When a required skill is missing locally, you must look up candidates on https://skills.sh/, suggest 2-3 options + install commands, and wait for the user.
Artifact-first, resumable: state lives in proposal.md, tasks.md, context.json under run_dir/.
Plan-then-confirm execution: generated workflows must write a plan first, then ask the user to confirm execution; the confirmation must be recorded under tasks.md -> ## Approvals.
Defaults (Ship Faster standard)
Artifact store: runs/ by default, OpenSpec when openspec/project.md exists (unless overridden in context.json).
Required run files: proposal.md, tasks.md, context.json.
Execution model: plan first, then ask the user to confirm execution; on confirmation, record approval in tasks.md.
Inputs (paths only)
Optional: repo_root (skills repository root)
Optional: workflow_spec_path (if the user already wrote a spec)
Outputs
New or updated workflow skill folder:
workflow-<slug>/SKILL.md
workflow-<slug>/references/workflow-spec.md (SSOT)
References
Prompt pack (verbatim prompts): references/prompt-pack.md
Workflow spec template (SSOT): references/workflow-spec-template.md
Example generated workflow skill: references/example-workflow-skill.md
Example workflow spec (valid): references/example-workflow-spec.md
Process
0) Resolve skills root (deterministic)

Resolve skills_root using this priority:

If user provides repo_root, use it.
Else search upward from the current working directory for:
<dir>/skills/manifest.json (monorepo layout) -> skills_root = <dir>/skills/
<dir>/manifest.json (skills-repo layout) -> skills_root = <dir>/
1) Create or load workflow_spec.md (SSOT)

If workflow_spec_path is not provided:

Call workflow-brainstorm first to converge on:

core goal (1 sentence)
acceptance criteria (3-7 bullets)
non-goals (1-5 bullets)
constraints (risk preference, timeline)
5-10 real trigger phrases the user would say

Skill Discovery (REQUIRED) - before finalizing required_skills:

a) Local skills scan: List all potentially relevant skills under skills_root:

ls -1 ~/.claude/skills/ | grep -E "(tool-|review-|workflow-)" 


Identify which local skills could serve steps in the workflow.

b) skills.sh lookup (MANDATORY): Fetch the leaderboard from https://skills.sh/ and identify relevant skills:

Search for keywords related to the workflow goal
Note top skills by install count in relevant categories
Identify 3-5 potentially useful external skills

c) Present findings to user:

## Skill Discovery Results

### Local Skills (available)
| Skill | Relevance | Notes |
|-------|-----------|-------|
| tool-xxx | HIGH | ... |
| review-yyy | MEDIUM | ... |

### External Skills (skills.sh)
| Skill | Installs | Source | Relevance |
|-------|----------|--------|-----------|
| skill-name | 10K | owner/repo | ... |

**Want to inspect any external skills before deciding?** (list numbers or "none")


d) If user wants to inspect: fetch skill details from skills.sh page, show SKILL.md content, then ask again.

e) User confirms final skill selection: only then proceed to write spec.

Write a workflow_spec.md using the template in references/workflow-spec-template.md.

2) Validate spec (deterministic)

Run:

python3 scripts/validate_workflow_spec.py /path/to/workflow_spec.md


Fix any validation errors before generating.

3) Resolve skill dependencies
Read required_skills / optional_skills from the spec.
Check which skills exist locally under skills_root.
If any required skill is missing:
Stop.
Use the prompt in references/prompt-pack.md to do a skills.sh lookup.
Suggest 2-3 candidates (links + why) and provide install command suggestions, but do not auto-install.
4) Generate/update workflow-<slug>/
Create workflow-<slug>/ under skills_root if missing.
Write SSOT:
workflow-<slug>/references/workflow-spec.md (copy from the validated spec).
Generate/update workflow-<slug>/SKILL.md:
Frontmatter name must match directory name (workflow-<slug>).
Frontmatter description must embed the spec triggers (routing fuel).
Include Ship Faster artifact backend selection rules (runs/ vs OpenSpec).
Include the plan-then-confirm execution policy:
Plan stage writes checklist to tasks.md.
Ask user to confirm start.
On confirmation, append an approval record under tasks.md -> ## Approvals (timestamp + scope) and start execution.
Map each chain step to one skill.
Keep the workflow concise: link to other skills for deep details.
5) Basic validation (required)

Run:

python3 scripts/validate_skill_md.py /path/to/workflow-<slug>


If it fails, fix frontmatter/name/line endings until it passes.

Note: The repo also includes skill-creator/scripts/quick_validate.py, but it may require extra Python deps. Use the validator in this skill as the default.

Weekly Installs
49
Repository
heyvhuang/ship-faster
GitHub Stars
338
First Seen
Feb 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn