---
rating: ⭐⭐
title: copy-review
url: https://skills.sh/sungkhum/agent-skills-pack/copy-review
---

# copy-review

skills/sungkhum/agent-skills-pack/copy-review
copy-review
Installation
$ npx skills add https://github.com/sungkhum/agent-skills-pack --skill copy-review
SKILL.md
Copy Review
Overview

Review text for communication issues that impede comprehension and output minimal, precise fixes. Preserve structure and author intent.

Inputs
content (required): Text to review (markdown, plain text, or text-heavy XML)
style_guide (optional): Project-specific guide that overrides defaults
reader_type (optional): humans (default) or llm
Workflow

Follow references/workflow.md exactly. Do not reorder steps. Honor all halt conditions.

Output
If issues found: return a three-column markdown table of fixes.
If none: output No editorial issues identified.
Reference
references/workflow.md for the canonical procedure and output format.
Weekly Installs
8
Repository
sungkhum/agent-…lls-pack
First Seen
Mar 12, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass