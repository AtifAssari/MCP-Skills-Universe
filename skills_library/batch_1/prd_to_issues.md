---
title: prd-to-issues
url: https://skills.sh/mattpocock/skills/prd-to-issues
---

# prd-to-issues

skills/mattpocock/skills/prd-to-issues
prd-to-issues
Installation
$ npx skills add https://github.com/mattpocock/skills --skill prd-to-issues
Summary

Convert product requirements into independently-deliverable GitHub issues using vertical-slice architecture.

Fetches PRD content from GitHub, analyzes the codebase context, and breaks requirements into thin vertical slices that span all integration layers end-to-end
Distinguishes between HITL (human-in-the-loop, requiring decisions) and AFK (autonomous, mergeable without review) slices, preferring AFK where possible
Presents proposed breakdown for user feedback on granularity, dependencies, and slice categorization before creating issues
Generates GitHub issues in dependency order with acceptance criteria, blocker references, and traceability back to parent PRD user stories
SKILL.md
PRD to Issues

Break a PRD into independently-grabbable GitHub issues using vertical slices (tracer bullets).

Process
1. Locate the PRD

Ask the user for the PRD GitHub issue number (or URL).

If the PRD is not already in your context window, fetch it with gh issue view <number> (with comments).

2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code.

3. Draft vertical slices

Break the PRD into tracer bullet issues. Each issue is a thin vertical slice that cuts through ALL integration layers end-to-end, NOT a horizontal slice of one layer.

Slices may be 'HITL' or 'AFK'. HITL slices require human interaction, such as an architectural decision or a design review. AFK slices can be implemented and merged without human interaction. Prefer AFK over HITL where possible.

4. Quiz the user

Present the proposed breakdown as a numbered list. For each slice, show:

Title: short descriptive name
Type: HITL / AFK
Blocked by: which other slices (if any) must complete first
User stories covered: which user stories from the PRD this addresses

Ask the user:

Does the granularity feel right? (too coarse / too fine)
Are the dependency relationships correct?
Should any slices be merged or split further?
Are the correct slices marked as HITL and AFK?

Iterate until the user approves the breakdown.

5. Create the GitHub issues

For each approved slice, create a GitHub issue using gh issue create. Use the issue body template below.

Create issues in dependency order (blockers first) so you can reference real issue numbers in the "Blocked by" field.

#

What to build

A concise description of this vertical slice. Describe the end-to-end behavior, not layer-by-layer implementation. Reference specific sections of the parent PRD rather than duplicating content.

Acceptance criteria
 Criterion 1
 Criterion 2
 Criterion 3
Blocked by
Blocked by # (if any)

Or "None - can start immediately" if no blockers.

User stories addressed

Reference by number from the parent PRD:

User story 3
User story 7

Do NOT close or modify the parent PRD issue.

Weekly Installs
8.7K
Repository
mattpocock/skills
GitHub Stars
53.2K
First Seen
Mar 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn