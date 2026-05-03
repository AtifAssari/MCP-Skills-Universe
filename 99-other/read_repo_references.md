---
title: read-repo-references
url: https://skills.sh/eyh0602/skillshub/read-repo-references
---

# read-repo-references

skills/eyh0602/skillshub/read-repo-references
read-repo-references
Installation
$ npx skills add https://github.com/eyh0602/skillshub --skill read-repo-references
SKILL.md
Read Repo References

Use this skill when you need inspiration or guidance from prior art and reference implementations.

When to Use
Designing new features that have established patterns elsewhere
Stuck on architecture decisions
Need to understand how similar tools solve a problem
Reference Structure

References live in .references/<name>/ with this format:

.references/
└── <reference-name>/
    ├── REF.md              # Required: metadata and description
    └── [local files]       # Optional: PDFs, markdown, code samples

REF.md Format
---
name: reference-name
type: link | local | hybrid
url: https://...               # Required if type includes link
description: Brief description
---

# Reference Name

Notes on key patterns, architecture, and relevance...

Reference Types
link: Points to external resource (GitHub repo, docs). Use WebFetch or browse the URL.
local: Contains files directly. Read the files in the reference directory.
hybrid: Both a link and local supplementary materials.
How to Use References

List available references:

ls .references/


Read a reference:

cat .references/<name>/REF.md


For link-type references: The REF.md contains the URL and notes about what to look for. Fetch specific files from the URL as needed.

For local-type references: Read the files directly from the reference directory.

Apply learnings: Extract relevant patterns and adapt them to the current project's conventions.

Best Practices
Read REF.md first to understand what the reference offers
Focus on patterns relevant to your current task
Adapt patterns to fit the project, don't copy blindly
Note any new insights in .agents/notes/ for future reference
Weekly Installs
8
Repository
eyh0602/skillshub
GitHub Stars
5
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn