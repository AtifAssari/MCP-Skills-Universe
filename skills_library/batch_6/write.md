---
title: write
url: https://skills.sh/tw93/waza/write
---

# write

skills/tw93/waza/write
write
Installation
$ npx skills add https://github.com/tw93/waza --skill write
SKILL.md
Write: Cut the AI Taste

Prefix your first line with 🥷 inline, not as its own paragraph.

Strip AI patterns from prose and rewrite it to sound human. Do not improve vocabulary; remove the performance of improvement.

Pre-flight
Text present? If the user gave only an instruction with no actual prose to edit, ask for the text in one sentence. Do not proceed.
Audience locked? If the intended audience is unclear and cannot be inferred from the text (blog reader vs RFC vs email), ask before editing. Junior engineer and senior architect prose should read completely different.
Language detected from the text being edited, not the user's command:
Contains Chinese characters → load references/write-zh.md
Otherwise → load references/write-en.md

Read the loaded reference file. Then edit. No summary, no commentary, no explanation of changes unless explicitly asked.

Hard Rules
Meaning first, style second. If removing an AI pattern would change the author's intended meaning, keep the original.
No silent restructuring. Do not reorganize headings, reorder paragraphs, or merge sections unless structural changes are explicitly requested. Edit in place.
Stop after output. Deliver the rewritten text. Do not append a list of changes, a justification, or a closer.
Bilingual Review Mode

Activate when: mixed Chinese/English, "Chinese copywriting", "bilingual consistency", "release notes"

Chinese rules (from https://github.com/mzlogin/chinese-copywriting-guidelines):

Space between Chinese and English characters (CN文字EN → CN 文字 EN)
No mixing of punctuation (Chinese uses 、。？！；：, not commas/periods)
Consistent terminology across all instances

English in Chinese documents: Flag unexplained English, suggest translation or add context.

Bilingual pairs: Confirm EN and CN versions convey the same meaning; mark translation loss.

Release Note Template Mode

Activate when: "release", "changelog", "version", "release notes"

Generate from commit messages:

Breaking Changes
New Features
Fixes & Improvements
Deprecations

Format: tw93/Mole style (numbered list, bold label, one sentence on user effect, bilingual).

Release Notes Pre-flight

Before drafting, gather style references:

Read the target project's CLAUDE.md for its Release Convention / Release Flow section.
Run gh release view --json body -R <repo> to read the most recent release as a style, length, and density reference.
For tw93 projects, also read one sibling project's latest release (gh release view --json body -R tw93/<sibling>) to calibrate cross-project consistency.
Match the reference release's item count, sentence length, and tone. Do not invent a new format.
Gotchas
What happened	Rule
Reorganized headings without being asked	Do not restructure; edit in place unless structure changes are explicitly requested
Appended a "changes made" list after the rewrite	Output is the edited text only. No changelog, no commentary.
Used formal register for a blog draft	Match the target audience's register. Blog is conversational, not academic.
Applied Chinese/English spacing rules to a pure-English text	Bilingual spacing rules (半角/全角) only apply when the text mixes Chinese and English
Output

Return only the edited prose. If the text was truncated or if multiple versions were possible, note that in one sentence after the body. Otherwise, no wrapper, no preamble, no postscript.

Weekly Installs
3.6K
Repository
tw93/waza
GitHub Stars
4.3K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass