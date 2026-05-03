---
rating: ⭐⭐⭐
title: text-optimizer
url: https://skills.sh/kochetkov-ma/claude-brewcode/text-optimizer
---

# text-optimizer

skills/kochetkov-ma/claude-brewcode/text-optimizer
text-optimizer
Installation
$ npx skills add https://github.com/kochetkov-ma/claude-brewcode --skill text-optimizer
Summary

Reduces token count in prompts and docs by 20–40% using 41 research-backed optimization rules.

Applies rules across six categories: Claude behavior, token efficiency, structure, reference integrity, perception, and LLM comprehension
Three optimization modes: light (text cleanup only), medium (balanced restructuring, default), and deep (aggressive compression and rephrasing)
Processes single files or entire directories of markdown files, with built-in quality checks for reference validity and information preservation
Generates optimization reports showing token reduction metrics and which rules were applied to each file
SKILL.md

Plugin: kochetkov-ma/claude-brewcode

Text Optimizer

Reduces token count in prompts, docs, and agent instructions by 20–40% without losing meaning. Applies 41 research-backed rules across 6 categories: Claude behavior, token efficiency, structure, reference integrity, perception, LLM comprehension.

Benefits: cheaper API calls · faster model responses · clearer LLM instructions · fewer hallucinations

Examples:

/text-optimize prompt.md          # single file, medium mode (default)
/text-optimize -d agents/         # deep mode — all .md files in directory


Skill text is written for LLM consumption and optimized for token efficiency.

Text & File Optimizer
Step 0: Load Rules

REQUIRED: Read references/rules-review.md before ANY optimization. If file not found -> ERROR + STOP. Do not proceed without rules reference.

Modes

Parse $ARGUMENTS: -l/--light | -d/--deep | no flag -> medium (default).

Mode	Flag	Scope
Light	-l, --light	Text cleanup only — structure, lists, flow untouched
Medium	(default)	Balanced restructuring — all standard transformations
Deep	-d, --deep	Max density — rephrase, merge, compress aggressively
Rule ID Quick Reference
Category	Rule IDs	Scope
Claude behavior	C.1-C.6	Literal following, avoid "think", positive framing, match style, descriptive instructions, overengineering
Token efficiency	T.1-T.8	Tables, bullets, one-liners, inline code, abbreviations, filler, comma lists, arrows
Structure	S.1-S.8	XML tags, imperative, single source, context/motivation, blockquotes, progressive disclosure, consistent terminology, ref depth
Reference integrity	R.1-R.3	Verify file paths, check URLs, linearize circular refs
Perception	P.1-P.6	Examples near rules, hierarchy, bold keywords, standard symbols, instruction order, default over options
ID-to-Rule Mapping
ID	Rule	ID	Rule
C.1	Literal instruction following	C.2	Avoid "think" word
C.3	Positive framing (do Y not don't X)	C.4	Match prompt style to output
C.5	Descriptive over emphatic instructions	C.6	Overengineering prevention
T.1	Tables over prose (multi-column)	T.2	Bullets over numbered (~5-10%)
T.3	One-liners for rules	T.4	Inline code over blocks
T.5	Standard abbreviations (tables only)	T.6	Remove filler words
T.7	Comma-separated inline lists	T.8	Arrows for flow notation
S.1	XML tags for sections	S.2	Imperative form
S.3	Single source of truth	S.4	Add context/motivation
S.5	Blockquotes for critical	S.6	Progressive disclosure
R.1	Verify file paths	R.2	Check URLs
R.3	Linearize circular refs	P.1	Examples near rules
P.2	Hierarchy via headers (max 3-4)	P.3	Bold for keywords (max 2-3/100 lines)
P.4	Standard symbols (→ + / ✅❌⚠️)		
S.7	Consistent terminology	S.8	One-level reference depth
P.5	Instruction order (anchoring)	P.6	Default over options
Mode-to-Rules Mapping
Mode	Applies	Notes
Light	C.1-C.6, T.6, R.1-R.3, P.1-P.4	Text cleanup only — no restructuring
Medium	All rules (C + T + S + R + P)	Balanced transformations
Deep	All rules + aggressive rephrasing	Merge sections, max compression
Usage
Input	Action
No args	Prompt user for file or folder path
Single path	Process file directly
path1, path2	Process files sequentially
-l file.md	Light mode — text cleanup only
-d file.md	Deep mode — max compression
folder/	All .md files in directory
File Processing
Input Parsing
Input	Action
No args	Prompt user for file or folder path
Single path	Process directly
path1, path2	Process files sequentially
Execution Flow
Read references/rules-review.md — load all optimization rules
Read target file(s)
Analyze: identify type (prompt, docs, agent, skill), note critical info and cross-references
Apply rules by mode (see Mode-to-Rules Mapping)
Edit file with optimized content
Generate optimization report
Quality Checklist
Before
 Read entire text
 Identify type (prompt, docs, agent, skill)
 Note critical info and cross-references
During — Apply by Mode
Check	Light	Med	Deep
C.1-C.6 (Claude behavior)	Yes	Yes	Yes
T.6 (filler removal)	Yes	Yes	Yes
T.1-T.5, T.7-T.8 (token compression)	-	Yes	Yes
S.1-S.8 (structure/clarity)	-	Yes	Yes
R.1-R.3 (reference integrity)	Yes	Yes	Yes
P.1-P.4 (LLM perception)	Yes	Yes	Yes
Aggressive rephrasing	-	-	Yes
No information loss	Yes	Yes	Yes
After
 All facts preserved
 Logic consistent
 References valid (R.1-R.3)
 Tokens reduced
Output Format
## Optimization Report: [filename]

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Lines  | X      | Y     | -Z%    |
| Tokens | ~X     | ~Y    | -Z%    |

### Rules Applied
- [Rule IDs]: [Description of changes]

### Issues Found & Fixed
- [Issue]: [Resolution]

### Cross-Reference Verification
- [x] All file refs valid (R.1)
- [x] All URLs checked (R.2)
- [x] No circular refs (R.3)

---

**Full development platform:** [brewcode](https://github.com/kochetkov-ma/claude-brewcode) — infinite focus tasks, 14 agents, quorum reviews, knowledge persistence.
Install: `claude plugin marketplace add https://github.com/kochetkov-ma/claude-brewcode && claude plugin install brewcode@claude-brewcode`

Anti-Patterns
Avoid	Why
Remove all examples	Hurts generalization (P.1)
Over-abbreviate	Reduces readability (T.5 caveat)
Generic compression	Domain terms matter
Over-aggressive language	Opus 4.5 overtriggers (C.5)
Flatten hierarchy	Loses structure (P.2)
"Don't do X" framing	Less effective than "Do Y" (C.3)
Overengineer prompts	Opus 4.5 follows literally (C.6)
Overload single prompts	Divided attention, hallucinations (S.3)
Over-focus on wording	Structure > word choice (T.1)
Weekly Installs
2.0K
Repository
kochetkov-ma/cl…brewcode
GitHub Stars
25
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass