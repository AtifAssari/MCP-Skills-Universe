---
rating: ⭐⭐
title: workflow-template-extractor
url: https://skills.sh/heyvhuang/ship-faster/workflow-template-extractor
---

# workflow-template-extractor

skills/heyvhuang/ship-faster/workflow-template-extractor
workflow-template-extractor
Installation
$ npx skills add https://github.com/heyvhuang/ship-faster --skill workflow-template-extractor
SKILL.md
Workflow: Template Extractor (Real Project → Template)

Goal: Turn a real project into a shareable, runnable template in templates/ with minimal manual cleanup.

This is intended for “proven projects” you want to reuse as a baseline for future builds.

Input (pass paths only)
source_repo_root: Path to the real project
target_repo_root: Ship Faster repository root (where templates/ lives)
run_dir: runs/template-extractor/active/<run_id>/
extract_spec.md: What to keep/remove/generalize (brand, copy, assets, integrations, auth gates)
Output (persisted)
03-plans/extract-plan.md
05-final/extract-summary.md
templates/<NNN>-<slug>/ (runnable)
Workflow
0) Initialize
Create run_dir.
Decide <slug> and <NNN> (next available template number).
Copy source_repo_root → templates/<NNN>-<slug>/ (no build outputs, no caches).
1) De-secrets + de-brand

Must do:

Remove secret values from all files (.env*, config, hard-coded tokens).
Replace project IDs (Stripe price IDs, Supabase URLs/keys, webhook secrets) with env var keys.
Replace branding (names/domains/logos) with neutral placeholders unless the template is intentionally branded.
2) Normalize template entry docs

Required files:

README.md (5‑minute runnable)
.env.local.example (keys only)
metadata.json (name + description)

Recommended:

Ensure scripts exist for dev, build, start
If lint/typecheck/format are missing and the repo is TS-heavy, add minimal guardrails (avoid heavy governance)
3) Verification

Document in 05-final/extract-summary.md:

install works
dev starts
build succeeds (or clearly document why it can’t without credentials)
Constraints
Never commit secret values.
Extraction should be “copy + cleanup”, not a refactor project.
Weekly Installs
48
Repository
heyvhuang/ship-faster
GitHub Stars
338
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass