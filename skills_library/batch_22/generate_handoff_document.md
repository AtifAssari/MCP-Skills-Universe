---
title: generate-handoff-document
url: https://skills.sh/b-mendoza/agent-skills/generate-handoff-document
---

# generate-handoff-document

skills/b-mendoza/agent-skills/generate-handoff-document
generate-handoff-document
Installation
$ npx skills add https://github.com/b-mendoza/agent-skills --skill generate-handoff-document
SKILL.md
Generating Handoff Documents

Create a resumable handoff package for an in-progress analytical session. This orchestrator does three things: think (identify missing inputs and failed gates), decide (choose the next specialist or targeted rerun), and dispatch (send extraction, validation, and assembly work to co-located subagents). The working data lives on disk as structured artifacts; the orchestrator keeps only verdicts, paths, counts, and unresolved questions in context.

Inputs
Input	Required	Example
TARGET_FILE	Yes	docs/auth-review-handoff.md
SUBJECT	No	Authentication review
TRACKING_FILES	No	docs/auth-review-notes.md,docs/plan.md
CONTEXT_SOURCE	No	current conversation or docs/transcript.md

If the user omits optional values, infer them from the session when that is safe. Read ./references/data-contracts.md when deriving sibling artifact paths or checking the structured artifact schemas.

Workflow Overview
context-extractor writes the instruction/Q&A artifact.
insight-documenter writes the insights artifact.
claim-validator optionally writes the claims artifact when tracking files exist.
document-assembler reads those artifacts and writes the final handoff document.
The orchestrator validates the final document and reruns only the failing stage(s).
Subagent Registry

Read a subagent definition only when you are about to dispatch it.

Subagent	Path	Purpose
context-extractor	./subagents/context-extractor.md	Capture the original mandate, instruction amendments, and chronological Q&A history
insight-documenter	./subagents/insight-documenter.md	Extract evidence-backed findings, risks, and recommendations from the session
claim-validator	./subagents/claim-validator.md	Verify factual claims from external tracking files against primary sources when available
document-assembler	./subagents/document-assembler.md	Assemble the final handoff document from the structured artifacts
How This Skill Works
Read ./references/data-contracts.md when you need the sibling artifact naming rules, JSON schemas, or final-section requirements.
Pass only explicit handoffs between stages: source path, target artifact path, subject, and optional tracking files.
Keep only verdicts, file paths, counts, and actionable warnings from each subagent. The detailed payload stays in the artifact files.
Treat claims from tracking files as provisional even after validation. The final handoff must preserve that caution for the next agent.
Use targeted fix cycles. If source extraction is incomplete, rerun the relevant upstream subagent and the downstream stages that consume it. If the problem is only document coherence or formatting, rerun document-assembler only.
Stop and surface the blocker if dispatch is unavailable or if three fix cycles fail to produce a coherent handoff.
Output Contract

All files written by this skill are resumability artifacts. They preserve workflow state for later continuation; they are not product-code changes.

Artifact	Produced by	Purpose
TARGET_FILE	document-assembler	Final cold-start handoff document
<stem>.context.json	context-extractor	Original instructions, amendments, and Q&A log
<stem>.insights.json	insight-documenter	Findings with evidence, category, priority, and verification state
<stem>.claims.json	claim-validator	Optional claim-validation checklist and summary

On success, TARGET_FILE contains five sections:

Original Instructions & Scope
Q&A Log
Observations & Insights
Unverified Claims & Validation Checklist
Open Questions & Recommended Next Steps

If no tracking files were provided, Section 4 must explicitly say so and tell the next agent to verify any factual claims independently.

Phase Guide
Situation	Reference file	Purpose
Contract or artifact-path questions	./references/data-contracts.md	Derive sibling artifact names and confirm the schemas/required sections
Execution Steps
Confirm TARGET_FILE and derive the sibling artifact paths described in ./references/data-contracts.md.
Dispatch context-extractor with CONTEXT_SOURCE and CONTEXT_FILE.
Dispatch insight-documenter with CONTEXT_SOURCE and INSIGHTS_FILE.
If TRACKING_FILES exist, dispatch claim-validator with TRACKING_FILES, INSIGHTS_FILE, and CLAIMS_FILE. Otherwise record the claims step as skipped.
Dispatch document-assembler with TARGET_FILE, SUBJECT, CONTEXT_FILE, INSIGHTS_FILE, and optional CLAIMS_FILE.
Validate the written handoff against this checklist:
every required section exists
each insight has rationale plus evidence
the claims section includes either the validation directive or the explicit "no tracking files" note
open questions are listed or explicitly marked resolved
a fresh agent could continue without consulting prior chat history
If a check fails, rerun only the failing stage(s); cap the fix loop at three passes.
Return the final handoff path plus a concise summary of counts, warnings, and open questions.
Example

Derived working artifacts:

docs/auth-review-handoff.context.json
docs/auth-review-handoff.insights.json
docs/auth-review-handoff.claims.json
Dispatch context-extractor
Subagent returns: CONTEXT: PASS File: docs/auth-review-handoff.context.json Q&A exchanges: 4
Dispatch insight-documenter
Subagent returns: INSIGHTS: PASS File: docs/auth-review-handoff.insights.json Insights: 6
Dispatch claim-validator
Subagent returns: CLAIMS: WARN File: docs/auth-review-handoff.claims.json Claims checked: 9 Unverified: 2
Dispatch document-assembler
Subagent returns: HANDOFF: PASS File: docs/auth-review-handoff.md Open questions: 2
Report: "Handoff document written to docs/auth-review-handoff.md. The session is resumable from disk; two open questions remain."

The orchestrator keeps only those summaries and file paths.

Weekly Installs
23
Repository
b-mendoza/agent-skills
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass