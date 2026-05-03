---
title: create-skill
url: https://skills.sh/videojs/v10/create-skill
---

# create-skill

skills/videojs/v10/create-skill
create-skill
Installation
$ npx skills add https://github.com/videojs/v10 --skill create-skill
SKILL.md
Create Skill

Create a new skill with proper structure and conventions.

Usage
/create-skill [name]

name (optional): Skill identifier. If omitted, will prompt interactively.
Arguments

$ARGUMENTS

When to Create a Skill

Create a skill when:

Domain-specific knowledge that Claude doesn't inherently have
Multi-step workflows that benefit from procedural guidance
Automated commands that should run in isolated context
Patterns used repeatedly across conversations

Don't create a skill when:

Cross-cutting convention (naming, utilities) → add to CLAUDE.md Code Rules
One-off task → just do it
Information Claude already knows well → unnecessary context bloat

Decision tree:

Is this domain-specific knowledge?
├─ No → Does it affect multiple domains?
│       ├─ Yes → CLAUDE.md Code Rules
│       └─ No → Probably don't need anything
└─ Yes → Create a skill
         ├─ Reference material for a domain? → Knowledge skill
         ├─ Conventions and processes? → Workflow skill
         └─ Automated multi-step task? → Command skill

Skill Types
Type	Characteristics	Examples
Knowledge	Domain expertise, reference-heavy, may have review workflow	api, component, aria, docs
Workflow	Conventions, processes, templates	git, rfc
Command	Procedural steps, forked context, restricted tools	commit-pr, gh-issue, review-branch
Quick Reference

Frontmatter (required):

name: skill-name
description: >-
  What it does. Use when X. Triggers: "phrase1", "phrase2".


Frontmatter (optional):

context: fork                       # Isolated sub-agent context
allowed-tools: Tool1, Tool2         # Restrict available tools
agent: plan                         # Plan mode (no edits)
disable-model-invocation: true      # Prevent model calls


Structure options:

skill-name/
├── SKILL.md              # Always required
├── references/           # Detailed content (load on demand)
├── templates/            # Output templates
└── review/               # Review workflow (if applicable)

Reference Material
Topic	Load
Core principles (conciseness, progressive disclosure)	references/principles.md
Full structure and frontmatter schema	references/structure.md
Complete examples of each skill type	references/patterns.md
Your Tasks
Step 1: Validate Need

Before creating, verify this should be a skill:

Check if similar skill exists: ls .claude/skills/
Check if pattern belongs in CLAUDE.md instead
If skill name provided, check for conflicts with existing skills

If the pattern is cross-cutting (affects all domains), suggest adding to CLAUDE.md Code Rules instead.

Step 2: Gather Requirements

Ask the user (use question tool):

Skill type: Knowledge, Workflow, or Command?
Purpose: What problem does this skill solve?
Triggers: What phrases should activate this skill?
Scope: What topics/tasks does it cover?
Review capability: Does it need a review workflow?
Templates: Does it need output templates?
Step 3: Plan Structure

Based on requirements, determine:

Skill name (kebab-case)
Which directories needed (references/, templates/, review/)
Reference file names and purposes
Step 4: Create Skill

Create skill directory:

mkdir -p .claude/skills/<skill-name>


Create SKILL.md with:

Proper frontmatter (name, description, optional fields based on type)
Section headers with guidance comments
Reference table (if using references/)
Related Skills section

Create subdirectories if needed:

mkdir -p .claude/skills/<skill-name>/references
mkdir -p .claude/skills/<skill-name>/templates
mkdir -p .claude/skills/<skill-name>/review


Create placeholder reference files with:

Clear purpose header
Section structure
TODO markers for content
Step 5: Update README

Add the new skill to .claude/skills/README.md:

Add to "Quick Reference" table (if it's a workflow)
Add to "Skills" table with purpose and review status
Step 6: Report

Output:

Created file structure
Next steps (fill in content, test triggers)
Reminder to load principles.md when writing content
What NOT to Include

Skills should only contain what Claude needs to do the job:

No README.md, INSTALLATION_GUIDE.md, CHANGELOG.md
No setup and testing procedures
No user-facing documentation about the skill
No duplicate information (lives in SKILL.md OR references, not both)
After Creating

Checklist:

 Fill in SKILL.md content
 Write reference files (if any)
 Test trigger phrases work
 Verify skill loads correctly
 Update README.md tables
Weekly Installs
13
Repository
videojs/v10
GitHub Stars
705
First Seen
Mar 9, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass