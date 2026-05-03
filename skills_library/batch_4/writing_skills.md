---
title: writing-skills
url: https://skills.sh/sickn33/antigravity-awesome-skills/writing-skills
---

# writing-skills

skills/sickn33/antigravity-awesome-skills/writing-skills
writing-skills
Installation
$ npx skills add https://github.com/sickn33/antigravity-awesome-skills --skill writing-skills
Summary

Decision tree and templates for building agent skills that agents actually follow.

Provides three architecture tiers based on skill complexity: Tier 1 for simple single-file skills, Tier 2 for multi-concept skills, and Tier 3 for large platforms
Includes specialized guides for improving existing skills: modularization, anti-rationalization (preventing agent rule-ignoring), and CSO (search optimization for LLM discovery)
Offers four skill templates covering technique, reference, discipline, and pattern-based skills with standardized YAML frontmatter and naming conventions
Pre-deploy checklist ensures metadata compliance, trigger keywords, and file structure before publishing
SKILL.md
Writing Skills (Excellence)

Dispatcher for skill creation excellence. Use the decision tree below to find the right template and standards.

⚡ Quick Decision Tree
What do you need to do?

Create a NEW skill:

Is it simple (single file, <200 lines)? → Tier 1 Architecture
Is it complex (multi-concept, 200-1000 lines)? → Tier 2 Architecture
Is it a massive platform (10+ products, AWS, Convex)? → Tier 3 Architecture

Improve an EXISTING skill:

Fix "it's too long" -> Modularize (Tier 3)
Fix "AI ignores rules" -> Anti-Rationalization
Fix "users can't find it" -> CSO (Search Optimization)

Verify Compliance:

Check metadata/naming -> Standards
Add tests -> Testing Guide
📚 Component Index
Component	Purpose
CSO	"SEO for LLMs". How to write descriptions that trigger.
Standards	File naming, YAML frontmatter, directory structure.
Anti-Rationalization	How to write rules that agents won't ignore.
Testing	How to ensure your skill actually works.
🛠️ Templates
Technique Skill (How-to)
Reference Skill (Docs)
Discipline Skill (Rules)
Pattern Skill (Design Patterns)
When to Use
Creating a NEW skill from scratch
Improving an EXISTING skill that agents ignore
Debugging why a skill isn't being triggered
Standardizing skills across a team
How It Works
Identify goal → Use decision tree above
Select template → From references/templates/
Apply CSO → Optimize description for discovery
Add anti-rationalization → For discipline skills
Test → RED-GREEN-REFACTOR cycle
Quick Example
---
name: my-technique
description: Use when [specific symptom occurs].
metadata:
  category: technique
  triggers: error-text, symptom, tool-name
---

# My Technique

## When to Use
- [Symptom A]
- [Error message]

Common Mistakes
Mistake	Fix
Description summarizes workflow	Use "Use when..." triggers only
No metadata.triggers	Add 3+ keywords
Generic name ("helper")	Use gerund (creating-skills)
Long monolithic SKILL.md	Split into references/

See gotchas.md for more.

✅ Pre-Deploy Checklist

Before deploying any skill:

 name field matches directory name exactly
 SKILL.md filename is ALL CAPS
 Description starts with "Use when..."
 metadata.triggers has 3+ keywords
 Total lines < 500 (use references/ for more)
 No @ force-loading in cross-references
 Tested with real scenarios
🔗 Related Skills
opencode-expert: For OpenCode environment configuration
Use /write-skill command for guided skill creation
Examples

Create a Tier 1 skill:

mkdir -p ~/.config/opencode/skills/my-technique
touch ~/.config/opencode/skills/my-technique/SKILL.md


Create a Tier 2 skill:

mkdir -p ~/.config/opencode/skills/my-skill/references/core
touch ~/.config/opencode/skills/my-skill/{SKILL.md,gotchas.md}
touch ~/.config/opencode/skills/my-skill/references/core/README.md

Limitations
Use this skill only when the task clearly matches the scope described above.
Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
Weekly Installs
484
Repository
sickn33/antigra…e-skills
GitHub Stars
36.1K
First Seen
Jan 19, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass