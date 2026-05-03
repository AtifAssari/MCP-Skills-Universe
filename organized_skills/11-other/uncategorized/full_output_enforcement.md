---
rating: ⭐⭐
title: full-output-enforcement
url: https://skills.sh/leonxlnx/taste-skill/full-output-enforcement
---

# full-output-enforcement

skills/leonxlnx/taste-skill/full-output-enforcement
full-output-enforcement
Installation
$ npx skills add https://github.com/leonxlnx/taste-skill --skill full-output-enforcement
Summary

Enforces complete, unabridged output by banning truncation patterns and placeholder code.

Eliminates common shortcuts like // ..., // TODO, // rest of code, and prose phrases that defer work ("let me know if you want more")
Treats every task as production-critical: full files, all components, no skeletons or partial implementations
Handles token-limit splits cleanly by pausing at logical breakpoints (end of function, end of file) with a resumption marker, then continuing without recap on "continue" command
Includes a pre-output verification checklist to confirm no banned patterns remain, all requested deliverables are present, and code is runnable rather than descriptive
SKILL.md
Full-Output Enforcement
Baseline

Treat every task as production-critical. A partial output is a broken output. Do not optimize for brevity — optimize for completeness. If the user asks for a full file, deliver the full file. If the user asks for 5 components, deliver 5 components. No exceptions.

Banned Output Patterns

The following patterns are hard failures. Never produce them:

In code blocks: // ..., // rest of code, // implement here, // TODO, /* ... */, // similar to above, // continue pattern, // add more as needed, bare ... standing in for omitted code

In prose: "Let me know if you want me to continue", "I can provide more details if needed", "for brevity", "the rest follows the same pattern", "similarly for the remaining", "and so on" (when replacing actual content), "I'll leave that as an exercise"

Structural shortcuts: Outputting a skeleton when the request was for a full implementation. Showing the first and last section while skipping the middle. Replacing repeated logic with one example and a description. Describing what code should do instead of writing it.

Execution Process
Scope — Read the full request. Count how many distinct deliverables are expected (files, functions, sections, answers). Lock that number.
Build — Generate every deliverable completely. No partial drafts, no "you can extend this later."
Cross-check — Before output, re-read the original request. Compare your deliverable count against the scope count. If anything is missing, add it before responding.
Handling Long Outputs

When a response approaches the token limit:

Do not compress remaining sections to squeeze them in.
Do not skip ahead to a conclusion.
Write at full quality up to a clean breakpoint (end of a function, end of a file, end of a section).
End with:
[PAUSED — X of Y complete. Send "continue" to resume from: next section name]


On "continue", pick up exactly where you stopped. No recap, no repetition.

Quick Check

Before finalizing any response, verify:

No banned patterns from the list above appear anywhere in the output
Every item the user requested is present and finished
Code blocks contain actual runnable code, not descriptions of what code would do
Nothing was shortened to save space
Weekly Installs
31.3K
Repository
leonxlnx/taste-skill
GitHub Stars
14.5K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass