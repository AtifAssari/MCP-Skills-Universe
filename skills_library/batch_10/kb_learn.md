---
title: kb-learn
url: https://skills.sh/farzadshbfn/knowledge-skills/kb-learn
---

# kb-learn

skills/farzadshbfn/knowledge-skills/kb-learn
kb-learn
Installation
$ npx skills add https://github.com/farzadshbfn/knowledge-skills --skill kb-learn
SKILL.md
Contains Hooks

This skill uses Claude hooks which can execute code automatically in response to events. Review carefully before installing.

/kb-learn
Contents
1. Configuration
2. Routing
2a. Agents
3. KB Discovery
3a. Concept Evolution
4. Update KB
4a. Structure Health Check
5. User Approval
6. Naming and Folders
1. Configuration

On first invocation, check for config at .claude/knowledge-base/config.json.

No config: Tell user "Run /kb-bootstrap to set up your knowledge base." and stop.

Config exists: Read kb_roots. Single entry → use it. Multiple → defer to §4 step 0.

2. Routing

Parse $0 to determine workflow:

article → reference/article-workflow.md
topic → reference/topic-workflow.md
fix → reference/mistake-workflow.md
compact → Redirect: "Run /kb-compact [path] instead."
Otherwise → show usage with modes (article/topic/fix), tips, and examples
2a. Agents

Specialized agents isolate high-volume work and enable parallelism. SKILL.md is the orchestrator — spawns agents and chains results. Agents never spawn other agents.

Agent	Model	Purpose	Used by
scouter	haiku	KB discovery via /kb-find (supports --challenge)	all workflows
searcher	sonnet	Web research — search, fetch, structure findings	topic, article
challenger	sonnet	Adversarial web research — finds counter-evidence	topic
assessor	opus	Evaluate claims against KB + web evidence	article, topic
Orchestration Pipeline
1. Spawn scouter(s) + searcher IN PARALLEL
   ├── scouter (normal) → supporting evidence
   ├── scouter (challenge) → counter-evidence
   └── searcher → web findings
2. Spawn challenger (with claims from step 1) → counter-evidence from web
3. Spawn assessor (with all evidence incl. challenger) → verdicts + KB impact
4. Apply changes


Not all steps required every time:

Article: scouter(s) + searcher → assessor (no challenger)
Topic: full pipeline including challenger
Fix: single scouter, no web search

Use agents when output is high-volume, work is parallelizable, or task benefits from model specialization. Use inline when KB is small, single simple claim, or latency matters.

3. Shared Procedure: KB Discovery

All KB discovery goes through the scouter agent. Never use /kb-find directly.

How to spawn scouters
Read the kb-find SKILL.md at ${CLAUDE_SKILL_DIR}/../kb-find/SKILL.md
Build prompt: scouter body text (after frontmatter) + separator + full kb-find SKILL.md content
Spawn Agent with model: haiku, background: true

Why: Skill-internal agents don't get automatic skill injection — the orchestrator must explicitly inject kb-find content.

Spawning patterns
Bare lookup (topic, fix): single scouter, normal mode
Claim evaluation (article, deep assessment): two scouters in parallel (normal + challenge)
Per-workflow queries
article: search by claims and key terms
topic: search by topic name
fix: search by described error (with scrutiny)

Empty KB: Skip loading, note KB is empty.

3a. Shared Procedure: Concept Evolution and Legacy Patterns

After loading KB, check for concept evolution — outdated terminology, framing, or versioning. Follow reference/evolution-workflow.md for detection, callouts, old patterns, and legacy notes.

4. Shared Procedure: Update KB

KB routing: Multiple KBs → infer target from context; if ambiguous, ask user.

Read-only guard: If target KB has [read-only] badge (global KB), do NOT write to it. Instead, create a suggestion file in ~/.claude/knowledge-base/suggestions/ using suggestion.py (see ${CLAUDE_SKILL_DIR}/scripts/suggestion.py --help). Inform the user that a suggestion was created for the global KB. 0a. Skill folder check: If topic has skill/ subfolder, route by content type:
"What/where/when" → KB concept notes (lightweight: summary, sources)
"How/when to use/procedures" → skill's reference/ or SKILL.md
Move overlapping "how" sections from concept notes into skill (no duplication)
No skill/ → all content to concept notes

Templates from assets/: topic-note, index-note, legacy-note

Slim frontmatter:

Topic/index notes: only name + description in frontmatter. No title, summary, confidence, tags.
Inline <conf:high>, <conf:medium>, <conf:low> markers on claims are allowed and preserved during edits. Claims without a confidence tag should be treated as <conf:medium> (unverified but not flagged).
Body: # {Title} → content sections. No summary paragraph duplicating description.
TOC: Notes >100 lines need ## Contents in first 10 lines of body.
Legacy notes: name (append " (legacy)") + description (mention replacement).

Keep heading accurate after modifications.

Cross-references: markdown links with relative paths. Every concept note should link to at least one other note/index. Cross-KB: use @kb-name/path format. Global KBs: use soft references only — see: @namespace.kb/topic (no hard markdown links to read-only KBs).

Index updates: Link new notes from relevant index. Create index if 3+ notes and none exists. Use table when section has 3+ items (see reference/folder-structure.md).

5a. Sibling unification: Skip if §4a already ran. Otherwise, if creating a new folder, check siblings per §4a.

MANDATORY changelog: Every change to KB files → prepend entry to that KB's CHANGELOG.md. Follow reference/changelog-workflow.md. Do NOT skip.

Large notes: If note reaches ~500 lines, suggest /kb-compact <path>.

4a. Shared Procedure: Structure Health Check

Run after any KB update. Reuse KB root listing from step 5 if available; otherwise one ls.

Detection: Group KB root folders by first hyphen-delimited segment. 3+ folders sharing prefix (no existing parent) = candidate. No candidate = stop.

If found: Ask user — "Restructure now", "Skip", "Not applicable".

If approved: Follow reference/folder-structure.md. Run validate_kb.py --quiet to confirm zero errors.

5. Shared Procedure: User Approval

Before non-trivial KB changes, present summary: notes to create, modify, index updates, changelog entry. Group claims by confidence level. Show <conf:low> claims in a separate "⚠ Low confidence" section. Use the AskUserQuestion tool (not plain text) with options: "Apply high/medium confidence", "Apply all (including low confidence)", "Apply selectively", "Cancel".

Exception: Minor changes (adding source URL, fixing typo) may proceed without approval but must be mentioned.

6. Note Naming and Folder Conventions
Lowercase, hyphen-separated. Topic-prefixed when ambiguous (crdt-operation-based.md, not operations.md). 2-4 words.
Index: one index.md per folder. See reference/folder-structure.md.
Skill Folders (KB-backed skills)

Topics with "how" content have skill/ inside their concept folder. Symlink from .claude/skills/ makes it discoverable. All skills must be KB-backed. When skill/ exists, concept notes are lightweight (provenance, summary, pointers to skill).

Forward-Only

Conventions apply to new notes by default. Existing notes not moved unless requested. When editing, may normalize frontmatter and update indexes.

Moving files

When relocation requested: mv files → run validate_kb.py → fix reported broken links. Don't rewrite content just to relocate.

7. Validation

After completing KB changes, run the validator to catch broken links, frontmatter issues, and structural errors:

uv run ${CLAUDE_SKILL_DIR}/scripts/validate_kb.py --quiet --json


Fix any reported errors before finishing.

Weekly Installs
9
Repository
farzadshbfn/kno…e-skills
GitHub Stars
3
First Seen
Mar 18, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn