---
rating: ⭐⭐
title: writer
url: https://skills.sh/tao3k/omni-dev-fusion/writer
---

# writer

skills/tao3k/omni-dev-fusion/writer
writer
Installation
$ npx skills add https://github.com/tao3k/omni-dev-fusion --skill writer
SKILL.md
Writer Skill System Prompts
CRITICAL INSTRUCTION

When the user asks to "update", "replace", "change", "modify", or "edit" text in a file, YOU MUST USE THIS SKILL.

Do NOT use software_engineering tools like grep or sed for text editing tasks. They are:

Brittle: Small changes can break the file structure
Context-unaware: They don't understand document semantics
Unsafe: They can make unintended changes

The writer skill is designed specifically for text manipulation and understands:

File structure and syntax
Markdown formatting
Code block preservation
Document semantics
Quick Reference

The writing style guide has been auto-loaded above. Key rules:

Concise over verbose - Remove unnecessary words
Active voice - Use "we" and "do", not "it is done"
One H1 only - Document title at top
Max 3-4 sentences per paragraph
Remove clutter words (utilize→use, facilitate→help, in order to→to)
Workflow
Editing Files (Primary Use Case)

When editing files (MOST COMMON):

ONE-TIME READ: Read the file ONCE using filesystem.read_files. DO NOT call cat, head, or read_file again. The content stays in your context.
ANALYSIS: Plan your edits based on the content in context.
EXECUTION: Use writer.replace or writer.rewrite with the exact strings from step 1.
VERIFY: Done. No need to re-read.

FORBIDDEN: Repeated reads of the same file waste tokens and slow down the agent.

Writing Documentation

When writing documentation:

Trust the Context: The writing style guide has been auto-loaded above. Rely on it.
Draft Content: Write following the style rules in your context.
Polish: Use writer.polish_text() before saving if needed.
Save: Use filesystem.write_file() or writer.rewrite().

DO NOT run external validation tools like vale unless explicitly requested. The style guide in context is sufficient.

Weekly Installs
13
Repository
tao3k/omni-dev-fusion
GitHub Stars
9
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail