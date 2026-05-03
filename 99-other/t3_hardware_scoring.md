---
title: t3-hardware-scoring
url: https://skills.sh/toyworks/agent-skills/t3-hardware-scoring
---

# t3-hardware-scoring

skills/toyworks/agent-skills/t3-hardware-scoring
t3-hardware-scoring
Installation
$ npx skills add https://github.com/toyworks/agent-skills --skill t3-hardware-scoring
SKILL.md
MantaBase T3 Hardware Audit System — v2.1
Objectives
Crawl product information → Brand Blind → Triple-Auditor independent scoring → Eagle Eye Validation → Final Judge synthesis
Output: objective Tool / Toy / Trash classification with Eagle Eye safety veto
Core principles: evidence-first, parallel audits, zero hallucination, transparent math
Architecture Overview (v2.1)
Main Agent                             Subagents
───────────────────────────────────    ──────────────────────────────
Step 1: Data Collection                
Step 2: Organize + Brand Blind         
  ↓ write 02-brand-blinded.md          
                                       Step 3: ×3 parallel (Tool/Toy/Trash)
                                         · read file paths, print JSON to stdout
                                         · main agent writes 03-*.json files
  ↓ receive JSON, write files           
  ↓ auto-build auditor_reports.json    
                                       Step 4: ×1 Eagle Eye Validator (conditional)
                                         · AI subagent, not Python script
                                         · outputs adjustments[] diff
  ↓ apply diffs, rebuild JSON           
Step 5: synthesize_results.py           
Step 6: 99-audit-report.md             


Key v2.1 changes:

Step 4 replaces 3-way Peer Review with single AI-driven Eagle Eye Validator
Subagents print JSON to stdout; main agent writes all files
New Eagle Eye pattern: Architectural Implausibility
Mandatory auto-rebuild of auditor_reports.json from 03-*.json files
Token guardrails on verbatim_evidence and prompt size
Data Collection Strategy (Step 1-2)
Primary: crawl_product_info.py
python3 scripts/crawl_product_info.py --url https://example.com/product --pretty


Uses Jina AI Reader first, then direct HTTP fallback. Exit code 2 = content insufficient → trigger Exa fallback.

Fallback: Exa MCP (use when crawl fails or is insufficient)
mcporter call 'exa.web_search_exa(query: "{product name} specs review", numResults: 5)'
mcporter call 'exa.company_research_exa(companyName: "{brand}", numResults: 3)'


Exa is the preferred fallback — always available, no API key required. Collect at least 3 independent sources before proceeding.

Additional sources (check in order)
Official product page (specs, pricing, marketing claims)
Third-party reviews (TechAdvisor, The Verge, Tom's Guide, TrustedReviews)
Community discussion (Reddit, forums) for real-user pain points
Investigation/news coverage (privacy issues, lawsuits, controversies)
Minimum data threshold

Proceed only when you have:

 At least one official source with tech specs + price
 At least one third-party review with hands-on findings
 Marketing claims verbatim (needed for Eagle Eye Honest check)
Pre-launch data flag

If the product meets ALL of the following, append (Pre-launch) to the case_id and skip Step 4:

Zero independent hands-on reviews
≥3 critical specs undisclosed (battery, weight, connectivity, regulatory)
Pre-order only / not shipping
Procedure
Step 1: Collect Raw Data
Run crawl_product_info.py on official product URL
If exit code 2, run Exa MCP queries
Save raw extracts to 01-level0-extracts.md with source tags [S1], [S2], etc.
Step 2: Organize + Brand Blind (combined step)
Read references/organize-guide.md
Read references/defluff-guide.md
Merge all sources into one structured document
Apply Brand Blinding inline (replace brand names with [BRAND], [PRODUCT], [FEATURE])
Preserve ALL adjectives and marketing claims verbatim — needed by downstream auditors
Brand-blinded text should be ≤ 1200 words — deduplicate aggressively but keep all unique claims
Save to 02-brand-blinded.md
Step 3: Triple Auditor Scoring (independent, parallel)

Each Auditor sees only the Brand-Blinded text from Step 2.

Subagent execution rules (mandatory):

Pass file path to 02-brand-blinded.md — do NOT embed full text in prompt
Each subagent reads the file, reads their rubric file, and prints JSON to stdout
Main agent writes files — subagents never call write (prevents timeout file loss)
verbatim_evidence limits:
score 0–1: max 1 quote (or [] for score 0)
score 2–3: max 2 quotes
Recommended timeouts: Tool=150s, Toy=150s, Trash=180s
🟢 Tool Auditor
Reads references/tool-auditor.md
Template: references/tool-auditor-template.md
Score 11 items (0-3 scale), max 33 points
Output litmus_gate: "Yes"/"No" at top level
🟡 Toy Auditor
Reads references/toy-auditor.md
Template: references/toy-auditor-template.md
Score 11 items (0-3 scale), max 33 points
Output litmus_gate: "Yes"/"No" at top level
🔴 Trash Auditor
Reads references/trash-auditor.md
Reads references/trash-red-flags.md (required for Eagle Eye)
Score 14 items (0-3 scale), max 42 points
Eagle Eye triggers → auto-set score to 3 for flagged items
Output litmus_gate: "Yes"/"No" and critical_issues: [...] at top level

Key principles:

Each auditor works from Brand-Blinded text only
No cross-talk between auditors during scoring
Evidence FIRST, then score — no score without a verbatim quote
If a feature isn't in the text, it scores 0
Step 3.5: Auto-rebuild auditor_reports.json (mandatory)

After all three auditors return, the main agent MUST:

Read each 03-tool-auditor.json, 03-toy-auditor.json, 03-trash-auditor.json
Rebuild auditor_reports.json programmatically:
merged = {
  "tool":  { "total_score": tool["total_score"], "litmus_gate": tool["litmus_gate"], "extract_for_report": tool["extract_for_report"] },
  "toy":   { "total_score": toy["total_score"],  "litmus_gate": toy["litmus_gate"],  "extract_for_report": toy["extract_for_report"] },
  "trash": { "total_score": trash["total_score"], "litmus_gate": trash["litmus_gate"], "critical_issues": trash["critical_issues"], "extract_for_report": trash["extract_for_report"] }
}

Sanity check before proceeding:
merged.trash.total_score == sum of all 14 items in 03-trash-auditor.json
len(merged.trash.critical_issues) == count of Eagle Eye triggers in 03-trash-auditor.json
If mismatch: re-read the source file (never hand-edit scores)

🚨 Never manually write auditor_reports.json from memory or summaries — always rebuild from 03-*.json files.

Step 4: Eagle Eye Validator (conditional, AI-driven)

Read references/eagle-eye-validator.md

Trigger conditions — run Step 4 if ANY is true:

Trash report critical_issues is non-empty
Any auditor has any item scored 3
Composite score is in Gray Zone (-10 to +10)

Otherwise: skip directly to Step 5.

Execution:

Spawn 1 subagent (timeout: 120s)
Subagent reads 02-brand-blinded.md + only the flagged items from 03-*.json
Performs three checks:
Eagle Eye trigger validity — do both conflicting quotes exist verbatim?
Architectural Plausibility — are on-device/local claims technically feasible for the form factor? (NEW in v2.1)
Score=3 evidence check — does evidence actually support the 3-level rubric?
Outputs adjustments[] diff (not a full re-score)
Main agent applies diffs to auditor_reports.json and re-saves
Step 5: Final Judge Synthesis
python3 scripts/synthesize_results.py --input auditor_reports.json --text


Or manually per references/t3-classification.md:

Normalize scores: Tool=(raw/33)×100, Toy=(raw/33)×100, Trash=(raw/42)×100
Composite = max(NormTool, NormToy) - NormTrash
Check primary conditions (need 2+ of 4 conditions per category)
Check secondary conditions
Apply Eagle Eye Veto (if Trash critical_issues non-empty → force Trash into label)
Step 6: Generate Audit Report

Output file: 99-audit-report.md Directory: tmp/reports/t3-{YYYY-MM-DD}-{slug}/

Follow YAML schema in references/report-schema.md.

Output Format for Messaging Surfaces (WhatsApp / Telegram)

When delivering results in a chat interface, do not paste the full file. Use this condensed format instead:

🏷️ T3 Audit — {Product Name}
Price: ${price} | Date: {YYYY-MM-DD}

📊 Scores
🟢 Tool:  {raw}/{33} → {norm}/100
🟡 Toy:   {raw}/{33} → {norm}/100
🔴 Trash: {raw}/{42} → {norm}/100
Composite: {composite:+.1f}

🏆 Classification: {final_label}
Confidence: {confidence}

{If Eagle Eye:}
🚨 Eagle Eye: {trigger name}
"{verbatim quote A}"
vs.
"{verbatim quote B}"

🟢 Tool highlights (3 bullets)
🟡 Toy highlights (3 bullets)
🔴 Trash issues (3 bullets)

💬 One-line verdict


Rules for messaging output:

No markdown tables (WhatsApp doesn't render them)
Use bold for emphasis, bullet lists for details
Keep total message under 600 words
If Eagle Eye triggered, always show the conflicting quotes
Important Constraints
🚨 Information Isolation (critical)
Brand-Blinded text is the ONLY input for auditors
Auditors must never see original brand names, marketing copy, or each other's reports during scoring
Final Judge reads only the three auditor JSON outputs, not original product text
📊 Objective data completeness
Collect specs, performance, reliability, market, and cost data
Brand Blinding must retain all specs and numbers
Every score must link to extracted verbatim evidence
Eagle Eye enforcement
Trash Auditor MUST check every item against references/trash-red-flags.md
Eagle Eye trigger → automatic score 3 → populate critical_issues[]
Eagle Eye Validator (Step 4) re-checks triggers including Architectural Plausibility
Final Judge must respect Eagle Eye Veto regardless of composite math
synthesize_results.py input format

The script expects a JSON file like:

{
  "tool":  { "total_score": <int 0-33>, "litmus_gate": "Yes|No", ... },
  "toy":   { "total_score": <int 0-33>, "litmus_gate": "Yes|No", ... },
  "trash": { "total_score": <int 0-42>, "litmus_gate": "Yes|No",
             "critical_issues": ["<eagle eye trigger text>", ...], ... }
}

Resource Index
Scripts
scripts/crawl_product_info.py — Multi-strategy product crawler (Jina → direct HTTP fallback)
scripts/synthesize_results.py — Final Judge math (normalization + Eagle Eye + Litmus Gate)
References (v2.1)
File	Used In	Notes
organize-guide.md	Step 2	
defluff-guide.md	Step 2	
tool-auditor.md	Step 3	
tool-auditor-template.md	Step 3	
toy-auditor.md	Step 3	
toy-auditor-template.md	Step 3	
trash-auditor.md	Step 3	
trash-red-flags.md	Step 3 (Eagle Eye)	v2.1: added Architectural Implausibility
eagle-eye-validator.md	Step 4	v2.1: AI-driven, replaces peer review
t3-classification.md	Step 5	
report-schema.md	Step 6	
peer-review-guide.md	Step 4	Deprecated in v2.1 — kept for reference only
Weekly Installs
16
Repository
toyworks/agent-skills
GitHub Stars
2
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn