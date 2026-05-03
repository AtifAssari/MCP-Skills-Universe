---
title: transcript-fixer
url: https://skills.sh/daymade/claude-code-skills/transcript-fixer
---

# transcript-fixer

skills/daymade/claude-code-skills/transcript-fixer
transcript-fixer
Installation
$ npx skills add https://github.com/daymade/claude-code-skills --skill transcript-fixer
SKILL.md
Transcript Fixer

Two-phase correction pipeline: deterministic dictionary rules (instant, free) followed by AI-powered error detection. Corrections accumulate in ~/.transcript-fixer/corrections.db, improving accuracy over time.

Prerequisites

All scripts use PEP 723 inline metadata — uv run auto-installs dependencies. Requires uv (install guide).

Quick Start
# First time: Initialize database
uv run scripts/fix_transcription.py --init

# Single file
uv run scripts/fix_transcription.py --input meeting.md --stage 1

# Batch: multiple files in parallel (use shell loop)
for f in /path/to/*.txt; do
  uv run scripts/fix_transcription.py --input "$f" --stage 1
done


After Stage 1, Claude reads the output and fixes remaining ASR errors natively (no API key needed):

Read all Stage 1 outputs — read entire transcript before proposing corrections (later context disambiguates earlier errors)
Identify ASR errors — compile all corrections across files
Apply fixes with sed in batch, verify each with diff
Finalize: rename _stage1.md → .md, delete original .txt
Save stable patterns to dictionary for future reuse

See references/example_session.md for a concrete input/output walkthrough.

Alternative: API batch processing (for automation without Claude Code):

export GLM_API_KEY="<api-key>"  # From https://open.bigmodel.cn/
uv run scripts/fix_transcript_enhanced.py input.md --output ./corrected

Core Workflow

Two-phase pipeline with persistent learning:

Initialize (once): uv run scripts/fix_transcription.py --init
Add domain corrections: --add "错误词" "正确词" --domain <domain>
Phase 1 — Dictionary: --input file.md --stage 1 (instant, free)
Phase 2 — AI Correction: Claude reads output and fixes errors natively, or --stage 3 with GLM_API_KEY for API mode
Save stable patterns: --add "错误词" "正确词" after each session
Review learned patterns: --review-learned and --approve high-confidence suggestions

Domains: general, embodied_ai, finance, medical, or custom (e.g., 火星加速器) Learning: Patterns appearing ≥3 times at ≥80% confidence auto-promote from AI to dictionary

After fixing, always save reusable corrections to dictionary. This is the skill's core value — see references/iteration_workflow.md for the complete checklist.

Dictionary Addition After Fixing

After native AI correction, review all applied fixes and decide which to save. Use this decision matrix:

Pattern type	Example	Action
Non-word → correct term	克劳锐→Claude, cloucode→Claude Code	✅ Add (zero false positive risk)
Rare word → correct term	潜彩→前采, 维星→韦青	✅ Add (verify it's not a real word first)
Person/company name ASR error	宋天航→宋天生, 策马攀山→策马看山	✅ Add (stable, unique)
Common word → context word	争→蒸, 钱财→前采, 报纸→标品	❌ Skip (high false positive risk)
Real brand → different brand	Xcode→Claude Code, Clover→Claude	❌ Skip (real words in other contexts)

Batch add multiple corrections in one session:

uv run scripts/fix_transcription.py --add "错误1" "正确1" --domain tech
uv run scripts/fix_transcription.py --add "错误2" "正确2" --domain business
# Chain with && for efficiency

False Positive Prevention

Adding wrong dictionary rules silently corrupts future transcripts. Read references/false_positive_guide.md before adding any correction rule, especially for short words (≤2 chars) or common Chinese words that appear correctly in normal text.

Native AI Correction (Default Mode)

When running inside Claude Code, use Claude's own language understanding for Phase 2:

Run Stage 1 (dictionary) on all files (parallel if multiple)
Verify Stage 1 — diff original vs output. If dictionary introduced false positives, work from the original file
Read all Stage 1 outputs fully before proposing any corrections — later context often disambiguates earlier errors. For large files (>10k tokens), read in chunks but finish the entire file before identifying errors
Identify ASR errors per file — classify by confidence:
High confidence (apply directly): non-words, obvious garbling, product name variants
Medium confidence (present for review): context-dependent homophones, person names
Apply fixes efficiently:
Global replacements (unique non-words like "克劳锐"→"Claude"): use sed -i '' with -e flags, multiple patterns in one command
Context-dependent (common words like "争"→"蒸" only in distillation context): use sed with longer context phrases for uniqueness, or Edit tool
Verify with diff: diff original.txt corrected_stage1.md
Finalize files: rename *_stage1.md → *.md, delete original .txt
Save stable patterns to dictionary (see "Dictionary Addition" below)
Remove false positives if Stage 1 had any
Common ASR Error Patterns

AI product names are frequently garbled. These patterns recur across transcripts:

Correct term	Common ASR variants
Claude	cloud, Clou, calloc, 克劳锐, Clover, color
Claude Code	cloud code, Xcode, call code, cloucode, cloudcode, color code
Claude Agent SDK	cloud agent SDK
Opus	Opaas
Vibe Coding	web coding, Web coding
GitHub	get Hub, Git Hub
prototype	Pre top

Person names and company names also produce consistent ASR errors across sessions — always add confirmed name corrections to the dictionary.

Efficient Batch Fix Strategy

When fixing multiple files (e.g., 5 transcripts from one day):

Stage 1 in parallel: run all files through dictionary at once
Read all files first: build a mental model of speakers, topics, and recurring terms before fixing anything
Compile a global correction list: many errors repeat across files from the same session (same speakers, same topics)
Apply global corrections first (sed with multiple -e flags), then per-file context-dependent fixes
Verify all diffs, finalize all files, then do one dictionary addition pass
Enhanced Capabilities (Native Mode Only)
Intelligent paragraph breaks: Add \n\n at logical topic transitions
Filler word reduction: "这个这个这个" → "这个"
Interactive review: Corrections confirmed before applying
Context-aware judgment: Full document context resolves ambiguous errors
When to Use API Mode Instead

Use GLM_API_KEY + Stage 3 for batch processing, standalone usage without Claude Code, or reproducible automated processing.

Legacy Fallback

When the script outputs [CLAUDE_FALLBACK] (GLM API error), switch to native mode automatically.

Utility Scripts

Timestamp repair:

uv run scripts/fix_transcript_timestamps.py meeting.txt --in-place


Split transcript into sections (rebase each to 00:00:00):

uv run scripts/split_transcript_sections.py meeting.txt \
  --first-section-name "课前聊天" \
  --section "正式上课::好，无缝切换嘛。" \
  --rebase-to-zero


Word-level diff (recommended for reviewing corrections):

uv run scripts/generate_word_diff.py original.md corrected.md output.html

Output Files
*_stage1.md — Dictionary corrections applied
*_corrected.txt — Final version (native mode) or *_stage2.md (API mode)
*_对比.html — Visual diff (open in browser)
Database Operations

Read references/database_schema.md before any database operations.

sqlite3 ~/.transcript-fixer/corrections.db "SELECT * FROM active_corrections;"
sqlite3 ~/.transcript-fixer/corrections.db "SELECT value FROM system_config WHERE key='schema_version';"

Stages
Stage	Description	Speed	Cost
1	Dictionary only	Instant	Free
1 + Native	Dictionary + Claude AI (default)	~1min	Free
3	Dictionary + API AI + diff report	~10s	API calls
Bundled Resources

Scripts:

fix_transcription.py — Core CLI (dictionary, add, audit, learning)
fix_transcript_enhanced.py — Enhanced wrapper for interactive use
fix_transcript_timestamps.py — Timestamp normalization and repair
generate_word_diff.py — Word-level diff HTML generation
split_transcript_sections.py — Split transcript by marker phrases

References (load as needed):

Safety: false_positive_guide.md (read before adding rules), database_schema.md (read before DB ops)
Workflow: iteration_workflow.md, workflow_guide.md, example_session.md
CLI: quick_reference.md, script_parameters.md
Advanced: dictionary_guide.md, sql_queries.md, architecture.md, best_practices.md
Operations: troubleshooting.md, installation_setup.md, glm_api_setup.md, team_collaboration.md
Troubleshooting

uv run scripts/fix_transcription.py --validate checks setup health. See references/troubleshooting.md for detailed resolution.

Next Step: Structure into Meeting Minutes

After correcting a transcript, if the content is from a meeting, lecture, or interview, suggest structuring it:

Transcript corrected: [N] errors fixed, saved to [output_path].

Want to turn this into structured meeting minutes with decisions and action items?

Options:
A) Yes — run /meeting-minutes-taker (Recommended for meetings/lectures)
B) Export as PDF — run /pdf-creator on the corrected text
C) No thanks — the corrected transcript is all I need

Weekly Installs
266
Repository
daymade/claude-…e-skills
GitHub Stars
968
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykPass