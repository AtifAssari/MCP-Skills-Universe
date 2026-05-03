---
title: decision-log
url: https://skills.sh/bjg4/decision-log-skill/decision-log
---

# decision-log

skills/bjg4/decision-log-skill/decision-log
decision-log
Installation
$ npx skills add https://github.com/bjg4/decision-log-skill --skill decision-log
SKILL.md
Decision Log Skill

Maintain a decisions/ directory where each decision is a standalone markdown file with YAML frontmatter. An _index.md manifest is regenerated on every invocation for fast scanning.

Critical Behavior Rule

This skill is fully autonomous. When invoked:

Do NOT ask the user which decisions to log. Log all unlogged decisions found.
Do NOT present candidates for confirmation. Just write them.
Do NOT narrate your phases or telegraph your process. Execute silently, then show results.
The only output the user should see is the final result: the logged entries themselves.
Directory Structure
decisions/
  _index.md        # Auto-generated manifest — never hand-edit
  DEC-0001.md      # One file per decision
  DEC-0002.md

Instructions
Step 1 — Assess State
Check if decisions/ directory exists. If not, create it.
List existing DEC-*.md files to determine the next ID (highest number + 1, zero-padded to 4 digits).
Read _index.md if it exists to know which decisions are already logged.
Scan the current conversation for any decisions not already captured.
Step 2 — Extract and Classify

For each unlogged decision, determine:

Field	Values
domain	A short descriptive label for the area this decision belongs to. Infer from context. Examples: Architecture, Product, Design, Operations, Strategy, Data Engineering, Security, Research, Finance, Health, Creative, Legal, Education, Workflow, Relationships, Career, Music, Science, Writing — any domain is valid. Use whatever fits the decision. Prefer reusing domains already present in existing decisions for consistency, but create new ones freely when the context demands it.
status	Active, Proposed, Superseded, Revisited, Deprecated
method	analysis, discussion, constraint, default, research, prototype, stakeholder-input

Method definitions:

analysis — decided by weighing data, benchmarks, or structured comparison
discussion — emerged from back-and-forth conversation
constraint — forced by a technical, budget, or time limitation
default — accepted a sensible default without active deliberation
research — decided after investigating documentation, articles, or prior art
prototype — decided after building and evaluating a proof of concept
stakeholder-input — directed by a stakeholder, client, or external party

When the method is ambiguous, pick the one that best describes the primary driver. Default to discussion if genuinely unclear.

Also capture: decision statement, options considered (with pros/cons), rationale, expected outcome, related DEC-XXXX IDs, 2-5 lowercase tags, and context (summary, conversation highlights, actions performed, artifacts).

Step 3 — Write Decision Files

Create a file per decision using the schema in references/templates.md. File naming: decisions/DEC-XXXX.md (zero-padded to 4 digits). Write all files in a single pass.

Step 4 — Regenerate Index

Read all DEC-*.md files in decisions/, extract frontmatter, regenerate decisions/_index.md using the index template in references/templates.md. The index is always rebuilt from disk — it self-heals.

Step 5 — Show Results

Present a clean summary table:

Logged 3 decisions:

ID	Domain	Decision	Status
DEC-0001	Architecture	Per-file decision tracking with YAML frontmatter	Active
DEC-0002	Research	Use longitudinal study design over cross-sectional	Active
DEC-0003	Creative	Analog synth palette for album intro tracks	Active

Updated: ./decisions/

Edge Cases

Explicit single decision ("log this decision: X"): Extract only that decision. Do not scan for others.

Supersession ("we changed our mind on DEC-0003"): Create new file with supersedes: DEC-XXXX. Edit prior file's frontmatter to status: Superseded. Regenerate index. Output:

Logged 1 decision:

ID	Domain	Decision	Status
DEC-0004	Creative	Switch to FM synthesis for album intro tracks	Active

Superseded: DEC-0003 → Superseded

Updated: ./decisions/

Review request ("what decisions have we made"): Read _index.md, present it.

Context lookup ("tell me more about DEC-0003"): Read decisions/DEC-0003.md, present it.

Status update ("mark DEC-0003 as Deprecated"): Edit frontmatter, regenerate index.

Security

Decision files capture conversation context. When extracting decisions, omit credentials, API keys, tokens, passwords, and other secrets that may have appeared in the conversation. If a decision references a secret (e.g., "we chose AWS as our provider"), log the decision but redact the actual credential values. Frontmatter tags should never contain sensitive identifiers.

Error Handling

No decisions found in conversation: Tell the user: "No unlogged decisions found in this conversation." Do not create empty files or fabricate decisions.

Malformed existing DEC file: If a DEC-*.md file has broken frontmatter, skip it during index regeneration and warn: "Skipped DEC-XXXX.md — invalid frontmatter." Do not delete or overwrite it.

Ambiguous decision boundary: When it's unclear whether something is one decision or two, prefer fewer, broader decisions. One well-scoped decision is better than two overlapping ones.

Referenced DEC file missing: If a supersession or related reference points to a non-existent file, write the reference anyway but add an open question: "Referenced DEC-XXXX not found — may have been removed or renamed."

Weekly Installs
41
Repository
bjg4/decision-log-skill
First Seen
Feb 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketWarn
SnykPass