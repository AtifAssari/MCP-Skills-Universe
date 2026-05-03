---
title: docs
url: https://skills.sh/buiducnhat/agent-skills/docs
---

# docs

skills/buiducnhat/agent-skills/docs
docs
Installation
$ npx skills add https://github.com/buiducnhat/agent-skills --skill docs
SKILL.md
Docs

Create and maintain project documentation in docs/ with a consistent, lightweight structure.

Outputs

Maintain these outputs:

docs/SUMMARY.md — documentation entry point (always regenerated)
docs/architecture/ — system design, infrastructure, component interactions, data flows, feature flows. Focus on how the system works, not file/code structure.
docs/codebase/ — file organization, directory structure, entry points, key modules and their responsibilities. Focus on where things live in the code.
docs/code-standard/ — coding conventions, naming rules, style guides, environment setup, custom rules and patterns the team follows. Focus on how to write code that fits in with the existing codebase, best practices, and team conventions, very important for maintaining consistency.
docs/project-pdr/ — product goals, use cases, business rules, constraints, and decision rationale. Nice to have many use case/requirements files

Also keep README.md aligned with current docs links and project summary.

Workflow
Step 1: Context Scan

Scan the project to understand what needs documenting:

Read existing docs if any (docs/SUMMARY.md and topic folders)
Read README.md and key config files (package.json, tsconfig.json, Cargo.toml, etc.)
Scan source directories to understand project structure, entry points, and major components
Check git log --oneline -20 for recent changes when updating existing docs

Focus on facts: features, architecture, stack, directory structure, and workflows. Do not invent requirements or assume business logic that is not evident from the code.

Step 2: Infer Behavior
Infer whether the repository needs an initial documentation pass or an incremental update based on the current docs/ state.
If docs/ does not exist or is clearly incomplete, perform initialization behavior.
If docs/ already exists with the standard structure, perform update behavior.
State the inferred behavior briefly when relevant.
Step 3: Produce Documentation
Initialize docs when missing or incomplete
Create docs/ and 4 topic folders: architecture/, codebase/, code-standard/, project-pdr/
For each topic folder: a. Scan codebase for relevant information b. Generate content based on codebase scan c. Create topic-specific files based on content found in the codebase. Name each file by its content (e.g., components.md, conventions.md). Do NOT use generic names (overview.md, index.md, main.md). Split into multiple files when content covers 2+ clearly distinct sub-topics. Minimum 1 file per folder.
Create docs/SUMMARY.md using the format specified in Content Requirements
Update README.md with link to docs/SUMMARY.md

Populate each file with concrete, project-specific content. Avoid placeholders and generic templates.

Update docs when they already exist
Detect what changed: compare current code against existing docs. Use git log --oneline and source file scanning to identify new/modified/removed components.
Preserve useful existing content and section structure.
Update stale or inaccurate sections in-place — do not rewrite from scratch.
Add newly discovered features, components, or conventions.
Remove clearly obsolete statements.
Add, modify, or remove detail files as needed based on content changes.
Regenerate docs/SUMMARY.md to match current files — only list files that actually exist on disk.
Update README.md if documentation links changed.

Important: The goal is an incremental, surgical update — not a full rewrite.

Step 4: Sync README

Ensure README.md includes:

Short project overview
Quick start (if present in project)
Documentation link pointing to docs/SUMMARY.md
Step 5: Validate Quality

Before finishing, verify:

docs/SUMMARY.md exists and lists every detail file that actually exists on disk (no phantom entries)
Each topic folder has at least 1 topic-specific file
No generic file names (overview.md, index.md, main.md) in topic folders
README.md links point to docs/SUMMARY.md
SUMMARY.md is concise and contains file tables for all sections
Terminology is consistent across files
No contradictions between docs and code
Paths and component names are accurate
Content is concise, specific, and actionable
Content Requirements
SUMMARY.md format

Contains project overview and file tables for each documentation section.

Strictly follow the template in references/summary-template.md.

Topic file rules
Each file focuses on 1 specific sub-topic within its folder
Named by content slug: components.md, conventions.md, product-goals.md
Do NOT use generic names: overview.md, index.md, main.md, general.md
Keep files focused and concise without enforcing line-count targets
Edge Cases
Minimal/empty project: If the codebase has very little code, keep topic files short and factual. Do not pad content to reach arbitrary size targets. Mark sections as "TBD — to be documented as the project grows" when there is genuinely nothing to document yet. Even with 1 file per folder, name it by its content.
Custom files in docs/: Preserve any user-created files outside the 4 standard topic folders (e.g., docs/API.md, docs/deployment.md). List them under "Other" in SUMMARY.md. Do not move or rename them.
Monorepo: If the project contains multiple packages/apps, document the overall structure in architecture/components.md and note each package's purpose. Each package does not need its own full docs set — keep it proportional.
Rules
Keep documentation factual; do not invent requirements.
Prefer concise updates over verbose prose.
Keep docs aligned with current implementation.
When uncertain, mark assumptions explicitly and request confirmation.
Ask targeted questions when information cannot be reliably inferred (business goals, ambiguous module ownership, conflicting conventions, unclear architecture decisions).
Weekly Installs
307
Repository
buiducnhat/agent-skills
GitHub Stars
45
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass