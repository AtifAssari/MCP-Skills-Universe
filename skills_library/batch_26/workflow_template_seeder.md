---
title: workflow-template-seeder
url: https://skills.sh/heyvhuang/ship-faster/workflow-template-seeder
---

# workflow-template-seeder

skills/heyvhuang/ship-faster/workflow-template-seeder
workflow-template-seeder
Installation
$ npx skills add https://github.com/heyvhuang/ship-faster --skill workflow-template-seeder
SKILL.md
Workflow: Template Seeder (Skills → Templates)

Goal: Turn a short template spec into a runnable, documented template under templates/.

This workflow is skills-first:

Use skills as the primary execution engine
Treat templates as “frozen outputs” (examples + regression references), not the mainline product
Input (pass paths only)
repo_root: Ship Faster repository root (where templates/ lives)
run_dir: runs/template-seeder/active/<run_id>/
template_spec.md: One-page spec (what it is, target user, core pages, required integrations)
Output (persisted)
03-plans/template-plan.md
05-final/template-summary.md
A new template directory: templates/<NNN>-<slug>/ containing:
README.md (5‑minute runnable)
.env.local.example (keys only)
metadata.json
Workflow
0) Initialize
Create run_dir.
Determine:
<slug> from spec (kebab-case)
<NNN> as the next available number under templates/ (001, 002, …)
Write 01-input/context.json for this workflow:
entry_type: idea
repo_root: <path-to-new-template-dir>
need_deploy: false (templates should not auto-deploy)
Enable only the integrations required by the spec (DB/billing/SEO)
1) Generate the template baseline (prefer clean + minimal)

Preferred path:

Create a clean Next.js baseline in the new template directory, then run the same “Ship Faster chain” against it.

Execution order (recommended):

workflow-project-intake (optional if spec is already complete)
workflow-ship-faster with the template directory as repo_root
If any steps are skipped (e.g., no DB/billing), record why in 00-index.md / 05-final/template-summary.md
2) Template hardening (shareable output)

Must do:

Remove secrets; only keep env key names in .env.local.example
Ensure README.md includes:
Node version
install + dev
required env keys
optional integrations notes
Ensure metadata.json is accurate and generic (no private branding unless intended)
3) Verification

At minimum (document results in 05-final/template-summary.md):

install works
dev starts
build succeeds (if the template requires external credentials, document the minimal required keys)
Constraints
Do not create a “kitchen sink” template.
Avoid large refactors; prefer small, clean baselines that are easy to adapt.
Never commit secrets.
Weekly Installs
48
Repository
heyvhuang/ship-faster
GitHub Stars
338
First Seen
Feb 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass