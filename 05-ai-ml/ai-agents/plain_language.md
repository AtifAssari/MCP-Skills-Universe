---
title: plain-language
url: https://skills.sh/ggwicz/skills/plain-language
---

# plain-language

skills/ggwicz/skills/plain-language
plain-language
Installation
$ npx skills add https://github.com/ggwicz/skills --skill plain-language
SKILL.md
Plain Language Review

Review text files against the U.S. federal government Plain Language Guidelines (~30 rules across 6 categories) and produce a structured report of findings with concrete rewrites.

Important: This skill produces a report. Do not modify any reviewed files.

Review Workflow
Select files — Use the user's specified files. If none specified, run scripts/scan-plaintext-files.sh <project-directory> to discover all .md, .mdx, .markdown, .txt, .rtf, .rst, .adoc, .org, and .wiki files. The <project-directory> argument is required — it must be the root of the user's project (the repository being reviewed), NOT the skill's own directory.
Load rules — Read references/rules-quick-ref.md for the full rule checklist.
Review files in parallel — Spawn parallel sub-agents (via the Task tool, model sonnet, effort medium) to review files concurrently. Batch files into groups of 3–5 per sub-agent. Each sub-agent receives: the list of files to review, the rules from references/rules-quick-ref.md, and instructions to apply all rules, verify each rewrite resolves the flagged violation without introducing new ones, and produce findings in the Output Format below. Run up to 5 sub-agents concurrently. Once all complete, collect their findings. If a sub-agent fails, log the error and continue — do not block the rest of the review.
Collect and deduplicate findings — Gather findings from all sub-agents. Remove exact duplicates if file batches overlapped. For each finding, verify the rewrite resolves the flagged rule violation and does not introduce new violations.
Classify severity — Use references/severity-rubric.md to assign high/medium/low.
Assemble report — Write findings to .agents/plain-language/plain-language-findings-YYYYMMDD.md (create the directory if it doesn't exist; use today's date). Group findings by file, then by severity (high first). End with the summary block.
Model & Effort Guidance

This skill does not require frontier-class reasoning. Rule application is structured pattern matching; prose rewrites are sentence-level edits. Use a mid-tier model (e.g., Claude Sonnet) at high effort for orchestration, and the same model at medium effort for file-review sub-agents. A frontier model adds cost without meaningful quality gain here.

Output Format

Use this exact structure for each finding:

## [file path]

### Finding [N] — [Rule name] (severity: [high|medium|low])
- **Line [N]:** "[original text]"
- **Guideline:** [One-sentence explanation of the rule violated]
- **Suggested:** "[concrete rewrite]"


Example:

## docs/getting-started.md

### Finding 1 — Use simple words (severity: medium)
- **Line 14:** "In order to utilize the configuration module..."
- **Guideline:** Replace complex words with simple alternatives — "utilize" → "use", "in order to" → "to"
- **Suggested:** "To use the configuration module..."

### Finding 2 — Use active voice (severity: high)
- **Line 23:** "The database will be initialized by the setup script."
- **Guideline:** Make the actor the subject of the sentence
- **Suggested:** "The setup script initializes the database."


If a file has no findings, omit it from the report entirely — do not include a "no issues found" entry. The summary's "Files reviewed" count should still include it.

End the report with a summary:

## Summary
- **Files reviewed:** [N]
- **Total findings:** [N] ([N] high, [N] medium, [N] low)
- **Top issues:** [List the 2-3 most frequent rule violations]

When to Load Reference Files

Load references on demand to conserve context:

File	When to load
references/rules-quick-ref.md	Always — load at start of every review
references/word-substitutions.md	When reviewing word choice in any finding
references/active-voice-guide.md	When you detect passive voice patterns (forms of "to be" + past participle)
references/before-and-after-examples.md	When a rewrite requires restructuring (sentence split, list conversion, undoing a hidden verb, or reorder) rather than a simple word swap
references/severity-rubric.md	When classifying findings — consult definitions and examples
Scope Rules
Review: prose in .md, .mdx, .markdown, .txt, .rtf, .rst, .adoc, .org, .wiki files; comments in source code files; UI strings; error messages
Skip: code inside fences/backticks, variable names, import statements, configuration values, URLs, file paths
Preserve technical terms — flag jargon only when a simpler alternative exists without losing precision
Do not modify reviewed files — produce recommendations only
Weekly Installs
21
Repository
ggwicz/skills
GitHub Stars
1
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail