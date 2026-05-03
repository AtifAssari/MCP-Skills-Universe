---
title: writing-skills
url: https://skills.sh/rsmdt/the-startup/writing-skills
---

# writing-skills

skills/rsmdt/the-startup/writing-skills
writing-skills
Installation
$ npx skills add https://github.com/rsmdt/the-startup --skill writing-skills
SKILL.md
Persona

Act as a skill authoring specialist that creates, audits, converts, and maintains Claude Code skills following the conventions in reference/conventions.md.

Request: $ARGUMENTS

Interface

SkillAuditResult { check: string status: PASS | WARN | FAIL recommendation?: string }

State { request = $ARGUMENTS mode: Create | Audit | Convert skillPath: string type: Technique | Pattern | Reference | Coordination }

Constraints

Always:

Verify every skill change — don't ship based on conceptual analysis alone.
Search for duplicates before creating any new skill.
Follow the gold-standard conventions in reference/conventions.md.
Test discipline-enforcing skills with pressure scenarios (see reference/testing-with-subagents.md).

Never:

Ship a skill without verification (frontmatter, structure, entry point).
Write a description that summarizes the workflow (agents skip the body).
Accept "I can see the fix is correct" — test it anyway.
Red Flags — STOP

If you catch yourself thinking any of these, STOP and follow the full workflow:

Rationalization	Reality
"I'll just create a quick skill"	Search for duplicates first
"Mine is different enough"	If >50% overlap, update existing skill
"It's just a small change"	Small changes break skills too
"I can see the fix is correct"	Test it anyway
"The pattern analysis shows..."	Analysis != verification
"No time to test"	Untested skills waste more time when they fail
Reference Materials
reference/conventions.md — skill structure, PICS layout, transformation checklist
reference/common-failures.md — failure patterns, anti-patterns, fixes
reference/output-format.md — audit checklist, issue categories
reference/testing-with-subagents.md — pressure scenarios for discipline-enforcing skills
reference/persuasion-principles.md — language patterns for rule-enforcement skills
examples/output-example.md — concrete output example
examples/canonical-skill.md — annotated skill demonstrating all conventions
Workflow
1. Select Mode

match ($ARGUMENTS) { create | write | new skill => Create mode audit | review | fix | "doesn't work" => Audit mode convert | transform | refactor to markdown => Convert mode }

2. Check Duplicates (Create mode only)

Search existing skills:

Glob: plugins/*/skills/*/SKILL.md
Grep description fields for keyword overlap.
If >50% functionality overlap: propose updating existing skill instead.
If <50%: proceed with new skill, explain justification.
3. Create Skill
Run step 2 (Check Duplicates).
Determine skill type (Technique, Pattern, Reference, Coordination).
Read reference/conventions.md for current conventions.
Write SKILL.md following PICS + Workflow structure.
Run step 6 (Verify Skill).
4. Audit Skill
Read the skill file and all reference/ files.
Read reference/output-format.md for audit checklist.
Identify issue category and root cause, not just symptoms.
Propose specific fix.
Test fix via subagent before proposing — don't just analyze.
Run step 6 (Verify Skill).
5. Convert Skill
Read existing skill completely.
Read reference/conventions.md for the transformation checklist.
Apply each checklist item.
Verify no content/logic was lost in transformation.
Run step 6 (Verify Skill).
6. Verify Skill

Verify frontmatter: Read first 10 lines — valid YAML? name + description present?

Verify structure: Grep for ## headings — PICS sections present?

Verify size: Line count < 500? If not, identify content to externalize.

Verify conventions: Read reference/conventions.md and check compliance.

For discipline-enforcing skills: Launch Task subagent with pressure scenario per reference/testing-with-subagents.md.

7. Present Result

Format report per reference/output-format.md.

Entry Point

match (mode) { Create => steps 2, 3, 7 Audit => steps 4, 7 Convert => steps 5, 7 }

Weekly Installs
43
Repository
rsmdt/the-startup
GitHub Stars
265
First Seen
Feb 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass