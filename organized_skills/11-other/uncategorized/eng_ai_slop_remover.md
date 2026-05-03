---
rating: ⭐⭐
title: eng-ai-slop-remover
url: https://skills.sh/hungv47/agent-skills/eng-ai-slop-remover
---

# eng-ai-slop-remover

skills/hungv47/agent-skills/eng-ai-slop-remover
eng-ai-slop-remover
Installation
$ npx skills add https://github.com/hungv47/agent-skills --skill eng-ai-slop-remover
SKILL.md
AI Slop Remover

Remove AI-generated code patterns that are inconsistent with human-written code in the codebase.

Workflow
Get the diff against main branch
For each changed file, analyze patterns to remove
Make edits to remove identified slop
Report a 1-3 sentence summary of changes
Step 1: Get the Diff
git diff main --name-only


Then view each changed file to understand existing code style.

Step 2: Identify AI Slop Patterns

Comments to remove:

Obvious or redundant comments explaining what code clearly does
Comments that don't match the commenting style elsewhere in the file
Section divider comments when not used elsewhere

Defensive code to remove:

Try/catch blocks around code that doesn't throw or is already in a trusted path
Null/undefined checks when callers guarantee valid input
Type guards that duplicate earlier validation
Redundant error handling when parent functions already handle it

Type issues to fix:

Casts to any that bypass TypeScript's type system
Type assertions that hide real type mismatches
Overly broad generic types when specific types exist

Style inconsistencies:

Naming conventions that differ from the file
Spacing/formatting patterns that differ from the file
Import organization that differs from the file
Step 3: Make Edits

Remove identified patterns while preserving code functionality. Match the existing file's style.

Step 4: Report

End with only a 1-3 sentence summary of what was changed. No lists, no detailed breakdowns.

Example: "Removed 12 redundant comments and 3 unnecessary try/catch blocks across 4 files. Fixed 2 casts to any by using proper interface types."

Weekly Installs
8
Repository
hungv47/agent-skills
GitHub Stars
2
First Seen
Feb 28, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass