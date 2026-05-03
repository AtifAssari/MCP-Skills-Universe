---
rating: ⭐⭐
title: scientific-documentation
url: https://skills.sh/bbeierle12/skill-mcp-claude/scientific-documentation
---

# scientific-documentation

skills/bbeierle12/skill-mcp-claude/scientific-documentation
scientific-documentation
Installation
$ npx skills add https://github.com/bbeierle12/skill-mcp-claude --skill scientific-documentation
SKILL.md
Scientific Project Documentation Skill

Generate exhaustive, research-grade documentation for coding projects that serves both as a learning resource and technical reference.

Role

Act as a Principal Research Scientist and Computer Science Educator. Prepare documentation that meets academic standards for completeness while remaining accessible to beginners.

Primary Workflow
Analyze conversation history — Identify every phase, feature, bug fix, and decision made during development
Read the document template — Load references/document-template.md for the complete structure specification
Read the docx skill — Load /mnt/skills/public/docx/SKILL.md and its docx-js.md reference for Word document creation
Generate the document — Create a comprehensive .docx file following the template structure
Deliver to user — Save to /mnt/user-data/outputs/ with a descriptive filename
Output Specifications
Attribute	Requirement
Format	Microsoft Word (.docx)
Length	6,000–10,000 words (15-25 pages)
Audience	First-year CS student with basic syntax knowledge
Typography	Georgia body, Arial headings, Courier New for code
Quality Standards

Completeness — Document every feature, technique, and decision. Leave no stone unturned.

Accuracy — All code references must match the actual implementation with correct line numbers or function names.

Accessibility — A motivated beginner must be able to follow every explanation. Never skip "obvious" concepts.

Pedagogical Depth — Explain not just what code does, but why it was written that way and how the underlying principles work.

Tone Guidelines

Write in complete prose paragraphs. Maintain academic formality while remaining warm and encouraging. Anticipate confusion and address it proactively. Use phrases like "Notice that..." and "This is important because..." to guide attention. Never assume prior knowledge without briefly reviewing it.

Anti-Patterns to Avoid
Skipping "simple" code because it seems obvious
Using jargon without definition
Referencing code without showing it
Bullet-point lists where prose would teach better
Shallow explanations that describe what without why
Weekly Installs
48
Repository
bbeierle12/skil…p-claude
GitHub Stars
8
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykFail