---
rating: ⭐⭐⭐
title: write-a-skill
url: https://skills.sh/mattpocock/skills/write-a-skill
---

# write-a-skill

skills/mattpocock/skills/write-a-skill
write-a-skill
Installation
$ npx skills add https://github.com/mattpocock/skills --skill write-a-skill
Summary

Scaffold new agent skills with structured templates, progressive disclosure, and bundled utility scripts.

Guides skill creation through a four-step process: gather requirements, draft the skill structure, review with user, and finalize
Provides SKILL.md template with quick start, workflows, and advanced features sections; splits content into separate reference files when exceeding 100 lines
Includes utility script patterns for deterministic operations like validation and formatting to reduce token overhead
Emphasizes agent-readable descriptions with specific trigger keywords so the agent knows when to load the skill
SKILL.md
Writing Skills
Process

Gather requirements - ask user about:

What task/domain does the skill cover?
What specific use cases should it handle?
Does it need executable scripts or just instructions?
Any reference materials to include?

Draft the skill - create:

SKILL.md with concise instructions
Additional reference files if content exceeds 500 lines
Utility scripts if deterministic operations needed

Review with user - present draft and ask:

Does this cover your use cases?
Anything missing or unclear?
Should any section be more/less detailed?
Skill Structure
skill-name/
├── SKILL.md           # Main instructions (required)
├── REFERENCE.md       # Detailed docs (if needed)
├── EXAMPLES.md        # Usage examples (if needed)
└── scripts/           # Utility scripts (if needed)
    └── helper.js

SKILL.md Template
---
name: skill-name
description: Brief description of capability. Use when [specific triggers].
---

# Skill Name

## Quick start

[Minimal working example]

## Workflows

[Step-by-step processes with checklists for complex tasks]

## Advanced features

[Link to separate files: See [REFERENCE.md](REFERENCE.md)]

Description Requirements

The description is the only thing your agent sees when deciding which skill to load. It's surfaced in the system prompt alongside all other installed skills. Your agent reads these descriptions and picks the relevant skill based on the user's request.

Goal: Give your agent just enough info to know:

What capability this skill provides
When/why to trigger it (specific keywords, contexts, file types)

Format:

Max 1024 chars
Write in third person
First sentence: what it does
Second sentence: "Use when [specific triggers]"

Good example:

Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when user mentions PDFs, forms, or document extraction.


Bad example:

Helps with documents.


The bad example gives your agent no way to distinguish this from other document skills.

When to Add Scripts

Add utility scripts when:

Operation is deterministic (validation, formatting)
Same code would be generated repeatedly
Errors need explicit handling

Scripts save tokens and improve reliability vs generated code.

When to Split Files

Split into separate files when:

SKILL.md exceeds 100 lines
Content has distinct domains (finance vs sales schemas)
Advanced features are rarely needed
Review Checklist

After drafting, verify:

 Description includes triggers ("Use when...")
 SKILL.md under 100 lines
 No time-sensitive info
 Consistent terminology
 Concrete examples included
 References one level deep
Weekly Installs
27.2K
Repository
mattpocock/skills
GitHub Stars
53.2K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass