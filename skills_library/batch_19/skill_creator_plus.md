---
title: skill-creator-plus
url: https://skills.sh/aktsmm/agent-skills/skill-creator-plus
---

# skill-creator-plus

skills/aktsmm/agent-skills/skill-creator-plus
skill-creator-plus
Installation
$ npx skills add https://github.com/aktsmm/agent-skills --skill skill-creator-plus
SKILL.md
Skill Creator+

Design and review Agent Skills that trigger reliably and stay lean.

Decision Flow

Start by deciding whether the user really needs a skill.

Need	Use
Reusable multi-step workflow with bundled scripts, references, or templates	Skill
Single focused slash task with parameterized input	Prompt
Always-on or file-scoped guidance	Instruction
Persona, tool restrictions, delegation, or handoffs	Custom Agent
Deterministic enforcement or lifecycle automation	Hook

If the answer is not Skill, stop and create the right primitive instead.

→ references/customization-primitives.md for the full selection guide

When to Use
Create skill, /create-skill, new skill, review skill, fix skill trigger, SKILL.md, スキル作成
Creating a new skill from scratch
Updating or refactoring an existing skill
Reviewing existing SKILL.md files
Deciding whether a customization should be a skill before authoring it
Core Principles
Principle	Description
Concise is Key	Context window is shared. Only add what Claude doesn't already know.
Discovery First	The description is the routing surface. Triggers must be explicit.
Degrees of Freedom	Match specificity to task fragility (high/medium/low freedom)
Progressive Disclosure	Split into 3 levels: Metadata → Body → References
Integrate Before Add	Update, merge, or replace existing guidance before appending more.
Right Primitive	A good skill is not a fallback for prompt/agent/instruction design.
Scope Before File	Decide workspace vs profile before creating anything.

Default assumption: Claude is already very smart. Challenge each piece: "Does this justify its token cost?"

Before adding a new section, ask three questions:

Can this update an existing rule instead?
Can this move to references/ instead of staying in SKILL.md?
Is this actually reusable, or is it just a session-specific note?
Skill Structure

→ references/skill-structure.md for locations, frontmatter, and bundled resource rules

skill-name/
├── SKILL.md (required)        # Lean overview + decision points
├── scripts/                   # Deterministic helpers
├── references/                # Load on demand
└── assets/                    # Templates and reusable outputs


→ See skill-structure.md > What NOT to Include for excluded files.

Creation Process

→ references/creation-process.md for the end-to-end workflow

Step	Action
0	Choose primitive + scope (skill vs prompt/agent/etc.)
1	Understand with concrete examples and trigger phrases
2	Plan reusable contents (scripts/references/assets)
3	Initialize or refactor the skill folder
4	Write SKILL.md and implement resources
5	Validate frontmatter, structure, and trigger quality
6	Test on real prompt patterns and iterate
Refactor Order

When improving an existing skill, use this order:

Delete stale or low-value guidance
Merge duplicate rules
Move long detail to references/
Add genuinely missing guidance last
Frontmatter and Triggering

Use the smallest viable frontmatter.

---
name: skill-name
description: "What it does. Use when [trigger conditions]. Triggers on 'keyword', 'phrase'."
argument-hint: "Optional slash-command hint"
user-invocable: true
disable-model-invocation: false
---

name must match the folder name
description must say both what and when
For manually used skills, default to explicit argument-hint and user-invocable: true
Use argument-hint as short input guidance, not as a long explanation
Use user-invocable: false only for background knowledge skills you do not want in the / menu
Use disable-model-invocation: true only for manual-only skills
Optional fields should be intentional, not boilerplate
Resource links must stay relative and shallow

→ references/common-pitfalls.md for silent failures and trigger misses

SKILL.md Guidelines
Size Target

→ See skill-review-checklist.md > Line Count Target for size guidelines.

Quick rule: < 150 lines is good, > 300 lines must split to references.

✅ Good	❌ Bad
Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.	Helps with documents
Set up book writing workspace. Triggers on "book writing", "執筆ワークスペース", "technical writing project".	Creates workspaces
When to Use Section

Start with generic keywords users are likely to say:

## When to Use

- **PDF**, **extract text**, **form filling** ← Keywords first
- Processing documents with embedded images
- Filling PDF forms programmatically

Body
Use imperative/infinitive form
Link to references for details
Keep essential workflow only
Add decision points when misuse is common
Reuse a proven shape from references/skill-structure-gallery.md before inventing a custom layout
Push reference material out of SKILL.md aggressively
Prefer replacing or compressing existing text over appending a new subsection
Review Checklist

→ references/skill-review-checklist.md

For bloat review specifically, use references/skill-bloat-review.md.

- [ ] SKILL.md under 150 lines?
- [ ] Request truly needs a skill?
- [ ] Description has trigger conditions?
- [ ] `argument-hint` is present for manually used skills?
- [ ] `user-invocable` is set intentionally?
- [ ] Optional frontmatter fields are intentional?
- [ ] Details moved to references/?
- [ ] No README.md or auxiliary docs?

Key References
Topic	Reference
Primitive Choice	references/customization-primitives.md
Skill Structure	references/skill-structure.md
Structure Gallery	references/skill-structure-gallery.md
Creation Process	references/creation-process.md
Review Checklist	references/skill-review-checklist.md
Bloat Review	references/skill-bloat-review.md
Common Pitfalls	references/common-pitfalls.md
Workflows	references/workflows.md
Output Patterns	references/output-patterns.md
Done Criteria
 Request is confirmed to be a skill, not another primitive
 Scope is decided before file creation
 SKILL.md created and under 150 lines
 Frontmatter has name + description with trigger conditions
 Manually used skills have argument-hint
 user-invocable is set intentionally
 Optional fields are added only when they change behavior
 Details moved to references/ (Progressive Disclosure)
 Review checklist passed
Weekly Installs
37
Repository
aktsmm/agent-skills
GitHub Stars
11
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass