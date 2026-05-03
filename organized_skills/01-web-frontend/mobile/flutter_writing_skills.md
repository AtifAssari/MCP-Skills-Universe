---
rating: ⭐⭐⭐
title: flutter-writing-skills
url: https://skills.sh/vp-k/flutter-craft/flutter-writing-skills
---

# flutter-writing-skills

skills/vp-k/flutter-craft/flutter-writing-skills
flutter-writing-skills
Installation
$ npx skills add https://github.com/vp-k/flutter-craft --skill flutter-writing-skills
SKILL.md
Writing Flutter-Craft Skills
Overview

Create new skills for flutter-craft that follow the established patterns and integrate with the skill system.

Announce at start: "I'm using the flutter-writing-skills skill to create a new skill."

Skill Structure

Every skill needs:

skills/
└── skill-name/
    └── SKILL.md

SKILL.md Format
---
name: skill-name
description: Use when [trigger condition] - [what it does]
---

# Skill Title

## Overview

[1-2 sentence description of what this skill does]

**Core principle:** [The key rule this skill enforces]

**Announce at start:** "I'm using the [skill-name] skill to [purpose]."

## When to Use

[Clear criteria for when to trigger this skill]

## The Process

[Step-by-step workflow]

## [Domain-Specific Sections]

[Add sections relevant to the skill's domain]

## Red Flags

**Never:**
- [Things to avoid]

**Always:**
- [Things to ensure]

## REQUIRED SUB-SKILL (if applicable)

After completing this skill, you MUST invoke:
→ **flutter-craft:[next-skill]**

## Integration

**Called by:** [Which skills trigger this one]
**Pairs with:** [Related skills]

Frontmatter Rules

The frontmatter is critical - it's how Claude Code discovers skills:

---
name: skill-name           # kebab-case, unique
description: Use when...   # Must start with "Use when"
---


Description format:

Start with "Use when [trigger]"
Add " - [what it does]" after trigger
Be specific about the trigger condition

Examples:

# Good
description: Use when implementing Flutter features - follows Clean Architecture layer order

# Bad (too vague)
description: Helps with Flutter development

Flutter-Craft Skill Conventions
Naming
Use flutter- prefix for Flutter-specific skills
Use kebab-case: flutter-feature-name
Be descriptive but concise
Core Principles

Include a Core principle that captures the essence:

"Evidence before claims, always"
"Fresh subagent per task + two-stage review"
"Domain → Data → Presentation layer order"
Announce Pattern

Skills should announce themselves:

"I'm using the [skill-name] skill to [action]."


This helps users understand which skill is active.

REQUIRED SUB-SKILL

If the skill MUST be followed by another skill:

## REQUIRED SUB-SKILL

After completing brainstorming, you MUST invoke:
→ **flutter-craft:flutter-planning**

This is NOT optional. The workflow is incomplete without planning.

Flutter-Specific Content

Include Flutter commands where relevant:

flutter analyze
flutter test
flutter build apk --debug
flutter pub get
flutter pub run build_runner build

Testing Your Skill
1. Syntax Check
# Read the skill file
cat skills/my-skill/SKILL.md

# Check frontmatter is valid
head -5 skills/my-skill/SKILL.md

2. Trigger Test

Verify the skill triggers correctly:

Start a new Claude Code session
Describe a scenario matching the trigger
Check if Claude invokes the skill
3. Workflow Test

Run through the complete workflow:

Follow every step in the process
Check REQUIRED SUB-SKILLs are invoked
Verify integration with other skills
Skill Categories
Workflow Skills (Core)
Process-oriented
Have clear steps
Often have REQUIRED SUB-SKILLs
Examples: brainstorming, planning, executing
Verification Skills
Focus on checking/validating
Include specific commands
Examples: verification, debugging
Utility Skills
Support other skills
May be invoked by multiple skills
Examples: worktrees, parallel-agents
Review Skills
Handle feedback loops
Two-way communication
Examples: review-request, review-receive
Common Mistakes

Vague trigger:

# Bad
description: Use for Flutter stuff

# Good
description: Use when starting a new Flutter feature - explores requirements and designs before implementation


Missing announce:

# Bad - no announcement
## Overview
This skill helps with...

# Good
**Announce at start:** "I'm using the flutter-brainstorming skill to design this feature."


No verification steps:

# Bad - no verification
After implementation, you're done.

# Good
After implementation, run:
$ flutter analyze
$ flutter test

Checklist for New Skills
 Frontmatter has valid name and description
 Description starts with "Use when"
 Has "Announce at start" instruction
 Has clear "When to Use" section
 Has step-by-step "Process" section
 Includes Flutter-specific commands where relevant
 Has "Red Flags" section
 REQUIRED SUB-SKILL documented if applicable
 Tested trigger in Claude Code session
 Tested full workflow
Weekly Installs
12
Repository
vp-k/flutter-craft
GitHub Stars
6
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass