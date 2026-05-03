---
title: creating-effective-skills
url: https://skills.sh/taisukeoe/agentic-ai-skills-creator/creating-effective-skills
---

# creating-effective-skills

skills/taisukeoe/agentic-ai-skills-creator/creating-effective-skills
creating-effective-skills
Installation
$ npx skills add https://github.com/taisukeoe/agentic-ai-skills-creator --skill creating-effective-skills
SKILL.md
Creating Effective Skills

Guide for creating agent skills that follow Claude's official best practices.

Core Principles

Concise is Key: The context window is shared. Only add what Claude doesn't already know. Default assumption: Claude is already very smart.

Progressive Disclosure: Skills load in three levels:

Metadata (~100 tokens) - always loaded
SKILL.md body (<5k tokens) - when triggered
Bundled resources - as needed

Keep SKILL.md small: Target ~200 lines, maximum 500 lines. Move detailed content to reference files aggressively.

Single Responsibility: Each skill does one thing well.

Workflow
Step 1: Understand the Skill Need

Ask the user to clarify (adapt questions to context):

For clear requests (e.g., "format markdown tables"):

"What input formats should be supported?"
"What output preferences do you have?"
"What edge cases should be handled?"

For ambiguous requests (e.g., "handle data", "help with files"):

"What KIND of data/files?" (format, source, structure)
"What OPERATIONS?" (transform, validate, migrate, analyze)
"What's the specific problem to solve?"
Ask at least 3 specific questions before proceeding

Red flags requiring extra clarification:

Vague verbs: "handle", "process", "manage", "help with"
Broad nouns: "data", "files", "documents" without specifics

Get clear sense of: purpose, usage examples, triggers, AND scope boundaries.

Step 2: Validate Scope

Before proceeding, verify the skill follows Single Responsibility:

Check naming:

❌ handling-data - too broad, what data? what handling?
❌ data-helper - generic, unclear purpose
✅ transforming-csv-data - specific operation + data type
✅ validating-json-schemas - clear single purpose

Check boundaries:

Can you clearly state what's IN scope vs OUT of scope?
If boundaries are unclear, scope is too broad → ask user to narrow

If scope is too broad:

Propose a focused alternative (e.g., "handling data" → "transforming-csv-data")
Explain what's excluded and why
Suggest splitting into multiple skills if needed

Do NOT proceed to file creation until scope is validated.

Step 3: Determine Freedom Level

Freedom level controls how much latitude Claude has when following the skill:

High: Multiple valid approaches, context-dependent decisions
Medium: Preferred pattern exists, some variation acceptable
Low: Fragile operations, consistency critical

Unless clearly LOW freedom: Read references/degrees-of-freedom.md and apply the decision framework. Cite the factors (fragility, context-dependency, consistency, error impact) in your justification.

If uncertain after reading the reference, ask the user.

Step 4: Plan Reusable Contents

Identify what to include:

Scripts (scripts/): Executable code for deterministic operations References (references/): Documentation loaded as needed Assets (assets/): Files used in output (templates, images, fonts)

Step 5: Create Structure
skill-name/
├── SKILL.md (required - AI agent instructions)
├── README.md (optional - human-facing installation and usage guide)
├── references/ (optional)
├── tests/
│   └── scenarios.md (optional - self-evaluation scenarios)
├── scripts/ (optional)
└── assets/ (optional)


README.md vs SKILL.md:

SKILL.md: Instructions for Claude (workflows, patterns, technical details)
README.md: Instructions for humans (installation, permissions, overview)

README.md, if present, should include:

Overview of what the skill does
File structure explanation (especially tests/scenarios.md purpose)
Installation instructions and required permissions

Avoid creating: INSTALLATION_GUIDE.md, CHANGELOG.md, or other redundant docs. Use README.md for human-facing documentation.

Step 6: Write SKILL.md
Frontmatter
---
name: skill-name
description: What the skill does and when to use it
---


Naming (use gerund form):

Good: processing-pdfs, analyzing-spreadsheets, managing-databases
Avoid: helper, utils, tools, anthropic-*, claude-*

Description (third person, include WHAT and WHEN):

Good: "Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction."
Avoid: "Helps with documents", "Processes data"

Be specific and include key terms. Description is the primary triggering mechanism.

Body

Use imperative form. Keep small (target ~200 lines, max 500). Include only:

Quick start / basic usage
Core workflows
References to additional files

For complex multi-step processes, see references/workflows-and-validation.md.

Example pattern:

## Quick start
[Basic usage]

## Advanced features
**Feature A**: See [references/feature-a.md](references/feature-a.md)
**Feature B**: See [references/feature-b.md](references/feature-b.md)


Keep references one level deep. See references/progressive-disclosure.md for patterns.

Step 7: Create Reference Files

For files >100 lines, include table of contents at top.

Organize by domain when appropriate:

skill/
├── SKILL.md
└── references/
    ├── domain_a.md
    └── domain_b.md


Avoid: deeply nested references, duplicate information, generic file names.

Step 8: Create Test Scenarios (Optional)

Ask the user: "Would you like to create test scenarios for this skill? Test scenarios enable automated evaluation with /evaluating-skills-with-models to measure skill quality across different models (sonnet, opus, haiku)."

If the user agrees, create tests/scenarios.md for self-evaluation:

## Scenario: [Name]

**Difficulty:** Easy | Medium | Hard | Edge-case

**Query:** User request that triggers this skill

**Expected behaviors:**

1. [Action description]
   - **Minimum:** What counts as "did it"
   - **Quality criteria:** What "did it well" looks like
   - **Haiku pitfall:** Common failure mode for smaller models
   - **Weight:** 1-5 (importance)

**Output validation:** (optional)
- Pattern: `regex`
- Line count: `< N`


Why this format: Binary pass/fail doesn't differentiate models. Quality-based scoring reveals capability differences.

Step 9: Define allowed-tools

After completing SKILL.md and references, identify which tools the skill uses:

Review SKILL.md and reference files for tool usage
List tools that need pre-approval (e.g., Bash(git status:*), WebSearch, Skill(other-skill))
Add allowed-tools field to frontmatter if needed
---
name: skill-name
description: ...
allowed-tools: "Bash(git status:*) Bash(git diff:*) WebSearch"
---


This field is experimental but helps agents pre-approve tool access.

Important considerations:

Read, Glob are already allowed by default - do not include
Edit, Write are destructive - do not pre-approve
Be as specific as possible with Bash subcommands
Good: Bash(git status:*) Bash(git diff:*) Bash(git log:*)
Avoid: Bash(git:*) (too broad, includes destructive operations like git push --force)
Anti-Patterns

❌ Windows-style paths (scripts\file.py) ❌ Too many options without a default ❌ Time-sensitive information ❌ Inconsistent terminology ❌ Deeply nested references ❌ Vague instructions

References

Progressive Disclosure: references/progressive-disclosure.md - Detailed patterns and examples

Degrees of Freedom: references/degrees-of-freedom.md - Guidance on appropriate freedom levels

Workflows and Validation: references/workflows-and-validation.md - Creating workflows with validation and feedback loops

Weekly Installs
62
Repository
taisukeoe/agent…-creator
GitHub Stars
2
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass