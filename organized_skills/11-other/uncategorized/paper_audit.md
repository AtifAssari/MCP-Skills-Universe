---
rating: ⭐⭐⭐
title: paper-audit
url: https://skills.sh/bahayonghang/academic-writing-skills/paper-audit
---

# paper-audit

skills/bahayonghang/academic-writing-skills/paper-audit
paper-audit
Installation
$ npx skills add https://github.com/bahayonghang/academic-writing-skills --skill paper-audit
SKILL.md
Paper Audit Skill v4.5

paper-audit is now deep-review-first. Its core job is to behave like a serious reviewer: find technical, methodological, claim-level, and cross-section issues; keep script-backed findings separate from reviewer judgment; and return a structured issue bundle plus a revision roadmap.

Version 4.5 adds a script-backed PRESUBMISSION layer for final-week mechanical checks: em dashes, AI-tone term frequency, abstract completeness, LaTeX citation/label/equation hygiene, paragraph-shape weak signals, and concrete captions. This layer supports existing modes; it is not a separate public mode.

Use it for audit and review. Do not use it as the first tool for source editing, sentence rewriting, or build fixing.

What This Skill Produces
quick-audit: fast submission-readiness screen with script-backed findings, including PRESUBMISSION
deep-review: reviewer-style structured issue bundle with major/moderate/minor findings
gate: PASS/FAIL decision calibrated for submission blockers; PRESUBMISSION Major/Minor findings remain advisory
re-audit: compare current issue bundle against a previous audit, including mechanical regression findings
polish: precheck-only handoff into a polishing workflow

The primary product is no longer just a score. For deep-review, the main outputs are:

final_issues.json
overall_assessment.txt
review_report.md
peer_review_report.md
revision_roadmap.md
Do Not Use
direct source surgery on .tex / .typ
compilation debugging as the main task
free-form literature survey writing
paragraph-level related-work rewriting
cosmetic grammar cleanup without an audit goal
Critical Rules
Never rewrite the paper source unless the user explicitly switches to an editing skill.
Never fabricate references, baselines, or reviewer evidence.
Always distinguish [Script] from [LLM] findings.
Always anchor reviewer findings to a quote, section, or exact textual location.
Be conservative with OCR noise, formatting quirks, and obvious copy-editing trivia.
Review like a careful reader: understand the author's intended meaning before flagging an issue.
For literature findings, judge whether the gap is evidence-backed and fairly positioned; do not rewrite the prose inside paper-audit.
For PRESUBMISSION, map CRITICAL/MAJOR/MINOR to Critical/Major/Minor script severities; only Critical or failed checklist items can fail gate.
In PDF mode, do not guess source-only hygiene. Report text-proven items and note that LaTeX/Typst source checks were skipped.
Mode Selection
Requested intent	Mode
"check my paper", "quick audit", "submission readiness", "pre-submission review", "投稿前检查"	quick-audit
"review my paper", "simulate peer review", "harsh review", "deep review"	deep-review
"is this ready to submit", "gate this submission", "blockers only"	gate
"did I fix these issues", "re-audit", "compare against old review"	re-audit
"polish the writing, but only if safe"	polish

Legacy aliases still work for one compatibility cycle:

self-check -> quick-audit
review -> deep-review
Input Resolution
Resolve the paper path first and keep the user-provided relative path when it already works.
Infer the paper format from the extension (.tex, .typ, .pdf) before choosing checks or parser behavior.
Infer report-style from the request: use peer-review when the user asks for journal-review prose such as Summary / Major Issues / Minor Issues / Recommendation; otherwise default to deep-review.
Infer output language from the request first, then fall back to the paper language when the request is ambiguous.
For re-audit, require --previous-report PATH. If it is missing, stop immediately and ask only for that path instead of running a fresh audit.
State the locked mode, report style, focus, language, and venue (if known) before running commands when any of them were inferred rather than explicitly provided.
Presentation Surface
deep-review: make the issue bundle, revision roadmap, and artifact paths the primary summary surface. It is acceptable to mention schema-level fields such as review lanes or source provenance here.
peer-review: make reviewer prose the primary summary surface. Do not expose raw internal keys like review_lane, source_kind, or root_cause_key in the top-level prose summary; keep them inside the artifact bundle.
gate: show verdict first, then EIC screening, then blockers, then advisory recommendations.
re-audit: show status buckets (FULLY_ADDRESSED, PARTIALLY_ADDRESSED, NOT_ADDRESSED, NEW) before any new audit commentary.
Committee Focus Routing (deep-review)

For deep-review, use the Academic Pre-Review Committee by default. This is a 5-role review pass:

Editor (desk-reject screen)
Reviewer 1 (theory contribution)
Reviewer 3 (literature dialogue / gap)
Reviewer 2 (methodology transparency)
Reviewer 4 (logic chain)

If the user requests a single dimension, run only the matching committee role(s).

Literature focus means:

verify whether the literature is thematically synthesized or merely enumerated
verify whether contradictions are acknowledged rather than flattened
verify whether the claimed gap is genuine instead of manufactured by selective citation
do not rewrite the related-work prose; hand that off to the format-specific writing skill when needed

If --focus ... is provided, it overrides keyword inference:

--focus full (default)
--focus editor|theory|literature|methodology|logic

Keyword map (English + Chinese):

editor: "desk reject", "pre-screen", "editor", "EIC", "主编", "预筛", "初筛"
theory: "theory", "contribution", "novelty", "theoretical dialogue", "理论", "贡献", "创新性"
literature: "related work", "literature", "research gap", "citation", "文献", "综述", "Research Gap", "引用", "gap is fake", "选择性引用"
methodology: "methods", "sample", "coding", "data", "design", "SRQR", "方法", "样本", "编码", "数据", "研究设计", "透明度"
logic: "logic", "argument", "causal", "structure", "论证", "因果", "逻辑", "结构"

Output language: match the user's request language. If ambiguous, match the paper language.

Review Standard

Read these references before running reviewer-style work:

references/REVIEW_CRITERIA.md
references/DEEP_REVIEW_CRITERIA.md
references/CHECKLIST.md
references/CONSOLIDATION_RULES.md
references/ISSUE_SCHEMA.md
references/PRE_SUBMISSION_RULES.md

The deep-review workflow uses a 16-part issue taxonomy:

formula / derivation errors
notation inconsistency
prose vs formal object mismatch
numerical inconsistency
missing justification
overclaim or claim inaccuracy
ambiguity that can mislead a careful reader
underspecified methods / missing information
internal contradiction
self-consistency of standards
table structure violations
abstract structural incompleteness
theory contribution deficiency
qualitative methodology opacity
pseudo-innovation / straw man
paragraph-level argument incoherence
Workflow
Common Step 0

Parse $ARGUMENTS, lock the paper path, and infer the mode if the user did not provide one. State the inferred mode before running commands if you had to infer it.

quick-audit
Run:
uv run python -B "$SKILL_DIR/scripts/audit.py" <paper> --mode quick-audit ...

Present a concise report:
Submission Blockers first
then Quality Improvements
then checklist items
call out PRESUBMISSION mechanical findings separately when they matter
mark quick-audit findings with [Script] provenance
If the user clearly wants reviewer-depth critique after the quick screen, escalate to deep-review.
deep-review

Use this as the default reviewer-style path.

If the user explicitly wants a submission-style reviewer report (for example: “SCI reviewer”, “journal review report”, “Summary / Major Issues / Minor Issues / Recommendation”, or “审稿报告”), keep the same deep-review evidence pipeline but make peer_review_report.md the Primary View in the combined CLI summary while keeping review_report.md as the richer evidence bundle. In this path, keep raw schema fields inside artifacts rather than the reviewer-facing prose.

Phase 1: Prepare workspace

Run:

uv run python -B "$SKILL_DIR/scripts/prepare_review_workspace.py" <paper> --output-dir ./review_results


This creates:

full_text.md
metadata.json
section_index.json
claim_map.json
paper_summary.md
sections/*.md
comments/
references/ (minimal copies for reviewer agents)
committee/ (committee reviewer artifacts)
Phase 2: Phase 0 automated audit

Run:

uv run python -B "$SKILL_DIR/scripts/audit.py" <paper> --mode deep-review ...


Treat this as Phase 0 only. It supplies script-backed context and scores, not the final review. PRESUBMISSION findings stay here for focused theory/literature/methodology/logic reviews; only full/editor deep-review can promote high-signal mechanical findings into the pre_submission_readiness lane.

Phase 3: Committee + Review Lanes
Phase 3A: Academic Pre-Review Committee (default)

Decide committee focus:

If --focus ... is provided, use it.
Otherwise infer from the user request using the keyword map in "Committee Focus Routing".
If nothing matches, default to full (all five roles).

Dispatch the committee reviewers (in this exact order) and have them write artifacts into the workspace:

agents/committee_editor_agent.md
write: committee/editor.md
write: comments/committee_editor.json
agents/committee_theory_agent.md
write: committee/theory.md
write: comments/committee_theory.json
agents/committee_literature_agent.md
write: committee/literature.md
write: comments/committee_literature.json
agents/committee_methodology_agent.md
write: committee/methodology.md
write: comments/committee_methodology.json
agents/committee_logic_agent.md
write: committee/logic.md
write: comments/committee_logic.json

If subagents are unavailable, run the committee reviewers inline, but keep the same file outputs.

Then write: committee/consensus.md

include: overall score (1-10), ordered priorities, and the top 3 issues to fix first
scoring formula:
start at 9.0
subtract: 1.5 * (# major) + 0.7 * (# moderate) + 0.2 * (# minor)
floor at 1.0
if Editor verdict is Desk Reject, cap at 4.0

Note: render_deep_review_report.py automatically embeds committee/*.md into review_report.md when present.

Phase 3B: Section and cross-cutting review lanes (coverage)

Read:

references/SUBAGENT_TEMPLATES.md
references/REVIEW_LANE_GUIDE.md

Then dispatch reviewer tasks for:

section lanes
introduction / related work
methods
results
discussion / conclusion
appendix, if present
cross-cutting lanes
claims vs evidence
notation and numeric consistency
evaluation fairness and reproducibility
self-standard consistency
prior-art and novelty grounding
pre-submission readiness (full/editor focus only)

Each lane writes a JSON array into comments/.

If subagents are unavailable, use the built-in deterministic fallback lane pass in scripts/audit.py so the workflow still writes lane-compatible JSON into comments/ before consolidation.

Phase 4: Consolidation

Run:

uv run python -B "$SKILL_DIR/scripts/consolidate_review_findings.py" <review_dir>
uv run python -B "$SKILL_DIR/scripts/verify_quotes.py" <review_dir> --write-back
uv run python -B "$SKILL_DIR/scripts/render_deep_review_report.py" <review_dir>


Consolidation rules:

merge exact duplicates
keep distinct paper-level consequences separate even if they share a root cause
preserve singleton findings unless clearly false positive
assign comment_type, severity, confidence, and root_cause_key
Phase 5: Present result

Summarize:

1 short paragraph overall assessment
counts of major / moderate / minor issues
3 highest-priority revision items
identify the Primary View selected by --report-style
path to review_report.md, peer_review_report.md, and final_issues.json
gate
Run:
uv run python -B "$SKILL_DIR/scripts/audit.py" <paper> --mode gate ...

EIC Screening (Phase 0.5): Read agents/editor_in_chief_agent.md and perform the editor-in-chief desk-reject screening on the paper's title, abstract, and introduction. This evaluates pitch quality, venue fit, fatal flaws, and presentation baseline. A desk-reject verdict is a gate blocker.
Report PASS/FAIL.
Present EIC screening results first (verdict + score + justification).
List blockers next.
Keep advisory items separate from blockers.
Keep PRESUBMISSION Major/Minor items advisory; only Critical mechanical findings can block the gate.
For IEEE pseudocode checks, make it explicit which issues are mandatory and which are only IEEE-safe recommendations.
re-audit
Requires --previous-report PATH.
Run:
uv run python -B "$SKILL_DIR/scripts/audit.py" <paper> --mode re-audit --previous-report <path> ...

If both old and new final_issues.json bundles are available, also run:
uv run python -B "$SKILL_DIR/scripts/diff_review_issues.py" <old_final_issues.json> <new_final_issues.json>

Present:
root-cause-aware status labels: FULLY_ADDRESSED, PARTIALLY_ADDRESSED, NOT_ADDRESSED, NEW
use structured prior issue bundles when available, but still accept Markdown previous reports
polish
Run the audit precheck:
uv run python -B "$SKILL_DIR/scripts/audit.py" <paper> --mode polish ...

If blockers exist, stop and report them.
Only proceed into polishing if the precheck is safe.
Output Contract

For deep-review, the final issue schema is:

{
  "title": "short issue title",
  "quote": "exact quote from paper",
  "explanation": "why this matters and what remains problematic",
  "comment_type": "methodology|claim_accuracy|presentation|missing_information",
  "severity": "major|moderate|minor",
  "confidence": "high|medium|low",
  "source_kind": "script|llm",
  "source_section": "methods",
  "related_sections": ["results", "appendix"],
  "root_cause_key": "shared-normalized-key",
  "review_lane": "claims_vs_evidence",
  "gate_blocker": false,
  "quote_verified": true
}


Always prefer:

exact quotes over vague paraphrase
evidence-backed findings over style commentary
issue bundle + roadmap over raw script dumps
References
File	Purpose
references/REVIEW_CRITERIA.md	top-level audit scoring and mapping
references/DEEP_REVIEW_CRITERIA.md	deep-review-specific issue taxonomy (16 dimensions) and leniency rules
references/CONSOLIDATION_RULES.md	deduplication and root-cause merge policy
references/ISSUE_SCHEMA.md	canonical JSON schema
references/REVIEW_LANE_GUIDE.md	section lanes and cross-cutting lanes
references/PRE_SUBMISSION_RULES.md	final-week mechanical audit rules, severity mapping, and PDF/source limits
references/SUBAGENT_TEMPLATES.md	reviewer task templates
references/QUICK_REFERENCE.md	CLI and mode cheat sheet
Scripts
Script	Purpose
scripts/audit.py	Phase 0 audit and mode entrypoint
scripts/pre_submission_check.py	deterministic PRESUBMISSION mechanical audit layer
scripts/prepare_review_workspace.py	create deep-review workspace
scripts/build_claim_map.py	extract headline claims and closure targets
scripts/consolidate_review_findings.py	deduplicate comment JSONs
scripts/verify_quotes.py	verify exact quote presence
scripts/render_deep_review_report.py	render final Markdown report
scripts/diff_review_issues.py	compare old vs new issue bundles
Reviewer Lanes

Committee agents (deep-review default):

committee_editor_agent.md
committee_theory_agent.md
committee_literature_agent.md
committee_methodology_agent.md
committee_logic_agent.md

Default deep-review lanes live in agents/:

section_reviewer_agent.md
claims_evidence_reviewer_agent.md
notation_consistency_reviewer_agent.md
evaluation_fairness_reviewer_agent.md
self_consistency_reviewer_agent.md
prior_art_reviewer_agent.md
synthesis_agent.md
editor_in_chief_agent.md — EIC desk-reject screener (used in gate mode)

Specialized deep-review agents (read their files for activation criteria):

critical_reviewer_agent.md — devil's advocate with C3-C5 checks
domain_reviewer_agent.md — domain expertise with A1-A7 assessments
methodology_reviewer_agent.md — methodology rigor with B3-B10 checks
literature_reviewer_agent.md — evidence-based literature verification (optional, --literature-search)
Examples
“Review this manuscript like a serious conference reviewer and tell me the biggest validity risks.”
“Run a quick audit on paper.tex and tell me what blocks submission.”
“Gate this IEEE submission and separate blockers from recommendations.”
“Re-audit this revision against my previous report.”
“Audit only the literature positioning and tell me whether the claimed gap is real or fabricated by selective citation.”
Weekly Installs
501
Repository
bahayonghang/ac…g-skills
GitHub Stars
172
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn