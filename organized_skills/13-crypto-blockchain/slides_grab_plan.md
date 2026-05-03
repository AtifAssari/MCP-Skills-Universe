---
rating: ⭐⭐
title: slides-grab-plan
url: https://skills.sh/vkehfdl1/slides-grab/slides-grab-plan
---

# slides-grab-plan

skills/vkehfdl1/slides-grab/slides-grab-plan
slides-grab-plan
Installation
$ npx skills add https://github.com/vkehfdl1/slides-grab --skill slides-grab-plan
SKILL.md
slides-grab Plan Skill (Codex)

Use this when the user asks to start a new presentation from scratch.

Goal

Produce an approved slide-outline.md before any slide HTML generation.

Inputs
Topic and intent
Audience
Tone and constraints
Optional research findings
Output
slide-outline.md (must include style: <id> in meta section)
Workflow
Analyze user goal and audience.
Style selection (mandatory, before outline): Run slides-grab list-styles, shortlist 2–3 styles that match the topic/tone, present the shortlist with reasons, and get explicit user approval. Optionally offer slides-grab preview-styles for visual preview. If no bundled style fits, propose a custom direction and get approval.
Create or revise slide-outline.md with ordered slides and key messages. Record the approved style ID in the meta section (style: <id>).
Present a concise summary to user.
Repeat revisions until explicit approval.
Rules
Do not write the outline before the user approves a style. Style selection comes first.
Do not generate slide HTML (<slides-dir>/slide-*.html) in this stage.
Keep scope to structure, narrative, and style selection.
Ask for approval before moving to design.
Assume later stages run through the packaged slides-grab CLI.
Use the packaged CLI and bundled references only; do not depend on unpublished agent-specific files.
Reference

If needed, use the bundled outline reference:

references/outline-format.md
references/plan-workflow-reference.md — archived detailed planning workflow and organizer-agent guidance
Weekly Installs
11
Repository
vkehfdl1/slides-grab
GitHub Stars
641
First Seen
Mar 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass