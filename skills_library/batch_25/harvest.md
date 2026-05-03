---
title: harvest
url: https://skills.sh/shihyuho/skills/harvest
---

# harvest

skills/shihyuho/skills/harvest
harvest
Installation
$ npx skills add https://github.com/shihyuho/skills --skill harvest
SKILL.md
Planning Second Brain

Create and maintain a project second brain without replacing source-of-truth planning files.

Core Contract
Treat task_plan.md, findings.md, and progress.md as the only source of truth (SOT).
Write second-brain outputs into docs/notes using Obsidian-compatible Markdown.
Never let docs/notes overwrite or redefine source-of-truth files.
Route all entrypoints through one deterministic capture workflow.
Required Skill Composition
Invoke planning-with-files first for primary planning workflow.
Invoke obsidian-markdown when writing or updating second-brain Markdown.
Trigger Contract

Use this skill when users ask to:

keep project memory over time
summarize milestones into reusable notes
record stable decisions and knowledge
build an Obsidian-friendly project knowledge base
read intents: find prior decision, look up past context, trace project timeline, retrieve existing second-brain note

Do not use this skill for unrelated implementation work that does not involve capture, summarization, or project memory publishing.

Output Locations
docs/notes/index.md
docs/notes/projects.md
docs/notes/decisions.md
docs/notes/knowledge.md
docs/notes/harvest-quality.md
docs/notes/projects/<project>/timeline/YYYY-MM-DD.md
docs/notes/decisions/*.md
docs/notes/knowledge/*.md
docs/notes/harvest-quality/YYYY-MM-DD-<project-slug>-harvest-review.md
docs/notes/harvest-quality/rollups/YYYY-MM-<project-slug>-harvest-optimization.md

Create missing folders/files when absent.

Progressive Disclosure Read Workflow (Required)

Follow this read order before any retrieval or context lookup:

Read docs/notes/index.md to discover available hubs.
Read the intent hub: docs/notes/projects.md, docs/notes/decisions.md, or docs/notes/knowledge.md.
Read only targeted leaf notes that match the intent.

Stop condition:

Stop when the target note is found, or after two consecutive reads that add no novel information.

Hard constraints:

Never start from deep leaves unless the user provides an exact path.
Treat docs/notes as retrieval-only; never capture or summarize docs/notes back into docs/notes.
Preserve the anti-recursion guard and existing SOT-only contract (task_plan.md, findings.md, progress.md).
Do not expand read scope beyond the minimal files needed for the requested intent.

Reference example:

references/progressive-disclosure-read-example.md
Deterministic Workflow (Required)

Run this workflow in order for every entrypoint (manual trigger phrases, slash-command wrappers, and plugin-driven invocation):

Preflight
Confirm SOT inputs exist: task_plan.md, findings.md, progress.md.
Confirm output root: docs/notes.
Set mode: capture, status, audit, review, or optimize.
For optimize mode, collect optional user-provided report directories as additional input roots.
Bootstrap
Ensure required minimal docs/notes files and templates exist.
Apply contract in references/publishing-and-dedupe.md.
Extract Candidates
Apply contracts in references/extraction-and-classification.md.
Classify
Route each candidate using the classification decision table contract.
Publish
Append same-day timeline events and update decision/knowledge notes with dedupe.
Verify and Report
Run verification checklist.
For review and optimize, apply references/quality-reports.md.
Candidate Schema and Extraction Rules (Required)

Candidate fields MUST include:

source_ref, change, why, candidate_type, confidence
optional: sot_fingerprint, exclusion_reason, unresolved_source_ref

Apply full extraction/classification contract in references/extraction-and-classification.md.

Publish Confirmation Semantics (Required)
Extract candidate.
Validate schema fields and thresholds.
Publish into target note.
Mark committed after publish succeeds.

Apply full publishing contract in references/publishing-and-dedupe.md.

First-Run Bootstrap (Required)

If docs/notes is missing, or if any required minimal file is missing, bootstrap from references/bootstrap/.

Apply the required minimal files list and bootstrap rules in references/publishing-and-dedupe.md.

Publishing Strategy

Apply classification, timeline, and milestone publish contracts in references/extraction-and-classification.md.

Review Report Mode (Required)

Use review mode to evaluate harvest output quality and persist one reusable report for later optimization planning.

Apply full review contract in references/quality-reports.md.

Review Rollup Mode (Required)

Use optimize mode to aggregate multiple review reports into one optimization roadmap.

Apply full rollup contract in references/quality-reports.md.

Execution Contract (Required)
Treat trigger methods as entrypoints only (manual phrases, slash-command wrappers, plugin-driven calls).
MUST route all entrypoints through the same deterministic workflow.
Produce equivalent output for equivalent source input regardless of trigger method.
Do not implement separate dedupe behavior per trigger entrypoint.
Keep plugin-driven capture behavior contract-compatible with manual entrypoints.
Keep review and optimize modes repo-agnostic. Do not hardcode project-specific heuristics as universal rules.
Source Extraction Boundaries (Required)

Extract with allowlist rules from source-of-truth files. Do not summarize everything.

Apply full allowlist/denylist and thresholds in references/extraction-and-classification.md.

Harvest Exclusion Markers

Support explicit exclusion markers inside source-of-truth files:

<!-- harvest:exclude:start -->
<!-- harvest:exclude:end -->

Ignore content inside this block during harvest publishing.

Anti-Recursion Guard
Do not summarize notes under docs/notes back into new notes.
Use source-of-truth files as input only (task_plan.md, findings.md, progress.md).
Skip entries that only describe harvest's own publishing activity.
Dedupe and Fingerprint Contract (Required)
Timeline events MUST include sot_fingerprint.
Compute sot_fingerprint from normalized source_ref + change + why.
Same timeline day + same sot_fingerprint means no-op (do not append duplicate block).
Equivalent source input must produce equivalent no-op behavior across manual and plugin entrypoints.

Fingerprint normalization:

Trim leading/trailing whitespace on source_ref, change, and why.
Collapse internal whitespace to single spaces.
Lowercase each part.
Join as <source_ref>||<change>||<why>.
Compute SHA-256 hex lowercase.

Reference example:

references/publishing-and-dedupe.md
Note Rules
Keep notes concise and reusable.
Include traceability metadata in formal notes.
Summarize; do not paste large verbatim source-of-truth sections.
Verification Checklist

Before finalizing updates:

Every formal note has source_files, source_date, and source_ref.
Every timeline event has source_ref and sot_fingerprint.
docs/notes/index.md links to latest decisions and knowledge.
No reverse edits were made to task_plan.md, findings.md, progress.md by second-brain steps.
No large copied source-of-truth blocks appear in formal notes.
In review mode, report file includes scorecard, deductions, and path-based evidence.
In optimize mode, rollup file includes coverage counts, aggregated scores, roadmap priority, and source report paths.
In optimize mode, rollup file includes input root resolution results (included + skipped + reasons).
Failure Handling
If source_ref cannot be resolved, set note status: draft and record unresolved_source_ref.
Do not block the source-of-truth workflow because of second-brain publish errors.
Non-Goals
Do not modify global IDE/user rule files.
Do not add mandatory always-on conversation loops.
Do not turn this skill into a general cross-skill memory engine.
Do not collect or persist tool chatter as project knowledge.
Anti-Patterns
Treating second-brain notes as execution-state files.
Creating parallel truth that conflicts with source-of-truth planning files.
Defining trigger-specific behavior that diverges from the deterministic workflow.
Weekly Installs
29
Repository
shihyuho/skills
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass