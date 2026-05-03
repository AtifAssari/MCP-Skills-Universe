---
title: skill-design
url: https://skills.sh/shihyuho/skills/skill-design
---

# skill-design

skills/shihyuho/skills/skill-design
skill-design
Installation
$ npx skills add https://github.com/shihyuho/skills --skill skill-design
SKILL.md
Skill Design

Design skills as reusable behavior systems that are easy to discover and execute.

Trigger Contract

Use this skill when users ask to:

create a new skill
refactor an existing skill
improve trigger quality or discoverability
align SKILL.md, README.md, and references/
remove ambiguity or conflicting guidance

Typical trigger phrases:

"create a skill for X"
"design a new skill"
"refactor this skill"
"make this skill reusable"
"align README and SKILL behavior"
Core Principles
Optimize for reliable agent behavior, not document aesthetics.
Make trigger conditions explicit and searchable.
Keep instructions executable and verifiable.
Avoid implicit project context unless explicitly required.
Default to secure-by-construction wording for any instructions that may trigger execution.
Writing Style Rules
Use imperative voice.
Keep sections short and high-signal.
Prefer concrete constraints over abstract advice.
Use MUST/NEVER for true invariants (safety, correctness, irreversible failure).
For normal guidance, use direct action verbs and clear defaults.
Avoid weak modal wording for hard rules (should, could, may, consider, usually).
Remove narrative text that does not change execution.
Metadata and Discovery
Write frontmatter description in third person.
Include both what the skill does and when to use it.
Keep trigger terms concrete (file type, task type, user phrasing).
Do not put workflow details in description; keep those in the body.
Workflow
Phase 1 - Define Contract
Define who uses the skill and when it triggers.
Define non-negotiable behavior and failure boundaries.
Define deterministic vs heuristic decisions.
Phase 2 - Structure Content
Write trigger and constraints first.
Keep SKILL.md as execution logic and decision constraints.
Move bulky detail to references/ and keep one source of truth per schema.
Add scripts/ only for repeatable deterministic operations.
When composing with other skills, invoke them by name and never copy their instruction bodies.
Phase 2.5 - Outer/Inner Boundary
Treat SKILL.md as outer governance: trigger contract, conservative boundaries, workflow, verification gates, and escalation path.
Treat references/ as inner detail: practical conventions, preferred patterns, examples, and extended rationale.
Do not place decision gates only in references/; keep governing decisions in SKILL.md.
If references/ and SKILL.md conflict, align references/ to SKILL.md.
Phase 3 - Author/Refactor SKILL
Tighten description and trigger wording.
Convert soft guidance into explicit, executable instructions.
Provide one default path first; add alternatives only when necessary.
Remove duplicate or contradictory instructions.
Phase 3.5 - Security Hardening Pass (When Skill Includes Commands/Automation)
Replace direct execution language with review-gated flow (fetch -> review/validate -> explicit approval).
Add trust-boundary disclosure when external services or remote content are involved.
Add forbidden command patterns and safer alternatives.
Add persistence checkpoints for changes that mutate shell/profile/system state.
Add provenance requirements for external artifacts (source rationale, version pin, integrity verification, rollback).
Document residual risk explicitly rather than implying risk elimination.
Phase 4 - Align README (Human-Facing)
Keep README value-first: problem -> value -> example -> activation.
Treat README.md as style charter for future AI output quality.
Keep implementation internals out of README.
Keep claims behavior-accurate.
Phase 5 - Validate
Run available validator for your environment.
If no validator exists, run manual consistency checks.
Confirm no repository-specific assumptions remain unless explicitly intended.
Progressive Disclosure Rules
Keep SKILL.md body compact (target under 500 lines).
Put advanced or domain-specific detail in references/.
Link reference files directly from SKILL.md (avoid deep nested references).
For long reference files (100+ lines), add a short table of contents.
README Rules
In this skill, README.md means the skill-level README (for example skills/<skill-name>/README.md), not the repository root README.
README.md is not required by Agent Skills Specification.
README.md is recommended for faster human understanding and adoption.
Keep README focused on outcomes, style expectations, and activation cues.
Anti-Patterns
Hardcoded local paths as universal defaults.
Tool lock-in with no fallback path.
Copying external skill instruction bodies instead of invoking the source skill.
Workflow summary inside frontmatter description.
Duplicated schema definitions across files.
Long narrative prose with no executable instruction.
Repeating MUST/NEVER for non-critical guidance.
Offering too many equivalent options without a default recommendation.
Fetch-and-follow phrasing that implies autonomous execution of remote content.
Unsafe install examples (curl|bash, wget|bash) without review and verification gates.
Persistent environment mutation guidance without explicit confirmation checkpoint.
Security logic split across multiple docs with no single source of truth.
Keeping conservative boundaries, workflow gates, or escalation rules only in references/.
Letting references/ override governing decisions defined in SKILL.md.
Security Patterns (Execution-Sensitive Skills)

Apply these when skills can produce or run commands:

Review Gate Pattern

Use: fetch -> review/validate -> explicit approval -> execute.
Never imply direct execution from raw URLs.

Trust Boundary Pattern

Explicitly state outbound data flow to external APIs/services.
Require redaction/sanitization guidance for sensitive content.

Command Safety Pattern

Define forbidden command patterns.
Provide safer alternatives (pinned versions, checksum/signature, least privilege).

Persistence Checkpoint Pattern

Prefer session-scoped behavior by default.
Require explicit confirmation before persistent shell/profile mutation.

Provenance Pattern

Require source rationale, version pin, integrity verification command, rollback/uninstall path.
Required Output Contract for Security Patterns

When applying security patterns, the resulting skill text MUST include explicit, auditable wording:

Review gate text

MUST include all four steps in order: fetch -> review/validate -> explicit approval -> execute.
MUST include a prohibition sentence equivalent to: "Do not execute remote content directly from URL."

Trust boundary text

MUST name the external destination (domain/service) when data leaves local context.
MUST include redaction/sanitization instruction before transmission.

Command safety text

MUST include a forbidden list with concrete examples.
MUST include at least one safer alternative for each high-risk pattern class.

Persistence checkpoint text

MUST include session-scoped default first.
MUST include explicit confirmation checkpoint before persistent shell/profile change.

Provenance text

MUST require source rationale, version pin, integrity verification command, and rollback/uninstall path.
Rewrite Templates (Use Verbatim Structure)

Replace risky phrase:

from: Fetch and follow instructions from [URL]
to: Fetch [URL], review and validate steps, ask for explicit approval, then execute.

Add prohibition:

Never execute remote raw content directly from URL.

Add persistence checkpoint:

Use session-scoped change by default; require explicit confirmation before persistent shell rc updates.
Security Verification Checklist (MANDATORY)

Before finalizing an execution-sensitive skill, verify all checks pass:

No fetch-and-follow wording remains.
Forbidden patterns and safer alternatives are both present.
Trust boundary disclosure includes explicit external destination.
Persistent mutation requires explicit confirmation language.
Provenance requirements include all four fields.
Residual risk statement exists and does not claim full elimination.
Consolidation Pattern (Multi-Plan Work)

When multiple plan docs overlap:

Create one consolidated execution plan as single source of truth.
Keep a "Sources Consolidated" section with explicit source paths.
Preserve all unique requirements via phased plan + detailed task matrix.
Prefer deleting superseded plan docs after consolidation to prevent drift.
Done Checklist
SKILL.md has explicit trigger contract and executable workflow.
SKILL.md defines outer governance boundaries (conservative rules, gates, escalation).
Frontmatter description clearly states what + when.
README.md defines style expectations for future contributions.
references/ contains heavy details only when needed.
references/ extends details without conflicting with SKILL.md governance.
No stale terms, duplicated schema ownership, or contradictory rules.
Validation evidence is recorded (tool-based or manual).
Example validation command: npx --yes skills-ref validate ./skills/<skill-name>.
See Also
Agent Skills Specification
Claude Skill Authoring Best Practices
Weekly Installs
27
Repository
shihyuho/skills
First Seen
Feb 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass