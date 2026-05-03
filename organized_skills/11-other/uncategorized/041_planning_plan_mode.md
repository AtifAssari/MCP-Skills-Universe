---
rating: ⭐⭐
title: 041-planning-plan-mode
url: https://skills.sh/jabrena/cursor-rules-java/041-planning-plan-mode
---

# 041-planning-plan-mode

skills/jabrena/cursor-rules-java/041-planning-plan-mode
041-planning-plan-mode
Installation
$ npx skills add https://github.com/jabrena/cursor-rules-java --skill 041-planning-plan-mode
SKILL.md
Java Design Plan Creation for Cursor Plan Mode

Guide the process of creating a structured plan using Cursor Plan mode. This is an interactive SKILL. Plans follow a consistent section structure suitable for Java feature implementation, refactoring, or API design.

What is covered in this Skill?

Plan mode workflow: enter Plan mode, gather context, draft plan, iterate
YAML frontmatter: name, overview, todos, isProject
Required sections: Requirements Summary, Approach (with Mermaid), Task List, Execution Instructions, File Checklist, Notes
London Style (outside-in) TDD pattern
Plan execution discipline: update Status after each task before advancing
Plan storage: ask user for preferred folder and filename convention before creating artifact
Constraints

Gather context before drafting. Include Execution Instructions in every plan. Never advance to next task without updating the plan's Status column.

MANDATORY: Run date before starting to get date prefix for plan filename
MUST: Read the reference template fresh—do not use cached content
MUST: Ask one or two questions at a time; never all at once
MUST: Validate summary (Does this capture what you need?) before proposing plan creation
MUST: Wait for user to confirm proceed before generating the plan
MUST: Ask the user where they want to store the plan before generating the plan artifact
MUST: Include Execution Instructions section in every generated plan
When to use this skill
Create a plan with Cursor Plan mode
Write a plan with Claude Plan mode
Design an implementation plan
Structure a development plan
Create a structured design plan
Refactor the plan
Improve the plan
Update the plan
Workflow
Get current date

Run date before planning and use it to derive the plan filename prefix YYYY-MM-DD.

Read reference and gather context

Read references/041-planning-plan-mode.md and ask one or two questions at a time to clarify requirements, constraints, and target scope.

Validate summary and confirm proceed

Summarize understanding, ask Does this capture what you need?, and wait for explicit proceed before creating the plan artifact.

Confirm plan storage location

Ask where the user wants to store the plan (for example, .cursor/plans/ or another folder) and confirm the target filename pattern before writing.

Generate structured plan artifact

Create the plan at the confirmed location using required sections and YAML frontmatter, including Execution Instructions.

Apply execution discipline

When executing tasks from the plan, update the Status column after each task before moving to the next one.

Reference

For detailed guidance, examples, and constraints, see references/041-planning-plan-mode.md.

Weekly Installs
40
Repository
jabrena/cursor-…les-java
GitHub Stars
368
First Seen
2 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass