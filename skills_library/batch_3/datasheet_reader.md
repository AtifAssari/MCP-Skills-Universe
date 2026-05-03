---
title: datasheet-reader
url: https://skills.sh/diodeinc/pcb/datasheet-reader
---

# datasheet-reader

skills/diodeinc/pcb/datasheet-reader
datasheet-reader
Installation
$ npx skills add https://github.com/diodeinc/pcb --skill datasheet-reader
SKILL.md
Datasheet Reader

Use this skill when a task depends on a datasheet or technical PDF.

Input: local .pdf path or http(s) URL
Command: pcb scan <input>
Output: stdout is the resolved markdown path
Next step: read the markdown file, not the raw PDF
Images are linked from the markdown
Workflow
Run pcb scan /path/to/file.pdf or pcb scan https://....
Capture the printed markdown path.
Read the markdown file and work from that artifact.
Follow image links only if the task depends on figures, diagrams, or tables.
Examples
pcb scan ./TPS54331.pdf
pcb scan https://www.ti.com/lit/gpn/tca9554

Notes
Prefer the minimal invocation above. Do not depend on optional flags unless a task explicitly requires them.
If pcb scan fails, report the failure briefly and then choose the best fallback.
Weekly Installs
727
Repository
diodeinc/pcb
GitHub Stars
228
First Seen
Mar 17, 2026
Security Audits
Gen Agent Trust HubWarn
SocketWarn
SnykWarn