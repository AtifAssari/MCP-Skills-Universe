---
title: reflection
url: https://skills.sh/davidkiss/smart-ai-skills/reflection
---

# reflection

skills/davidkiss/smart-ai-skills/reflection
reflection
Installation
$ npx skills add https://github.com/davidkiss/smart-ai-skills --skill reflection
Summary

Analyzes conversation patterns and tool usage to propose targeted skill improvements or user preferences.

Reviews conversation history and tool failures to identify gaps in skill definitions or recurring user preferences
Proposes one change at a time (either a skill update shown as a diff or a preference addition to CLAUDE.md) for focused review
Requires explicit user confirmation before applying any changes to skills or preference files
Prioritizes failure analysis and user corrections as primary signals for improvement opportunities
SKILL.md
Reflection Skill
Overview

This skill is used to learn from interaction with the user and failures in tool calls. It analyzes what worked, what didn't (tool failures), and identifies recurring patterns or explicit user preferences that should be formalized.

Objectives
Improve Skills: Identify gaps or inefficiencies in existing skill definitions and propose concise updates.
Store Preferences: Capture user preferences, project-specific rules, or recurring instructions in a AGENT.md or CLAUDE.md (when used in Claude Code) file.
Process
Analyze: Review the conversation history, tool calls, and any failures or corrections from the user.
Identify: Determine if a specific behavior should be codified in a skill or if a user preference has emerged.
Propose: Formulate a single, concise change.
If updating a skill, show a diff of the proposed change.
If adding a preference, show the proposed addition to CLAUDE.md.
Confirm: Present the proposal to the user and ask for explicit confirmation without making any changes first.
Apply Changes: Once user confirmed the changes, only then apply them
Guidelines
One at a time: Only propose one change per invocation to maintain focus and allow for careful review.
Conciseness: Keep changes as brief as possible. Often a few words are enough to clarify a requirement or fix a common mistake.
Accuracy: Ensure the proposal directly addresses a real issue or preference observed in the session.
Specificity: Think how you could make the learnings more generic to apply to other use cases, but don't make the changes too generic so that it would not address the original learnings
Failure Analysis: Pay special attention to tool failures or when the user has to correct your approach. These are primary candidates for reflection.
Conflict Resolution: If a proposed change conflicts with details of an existing skill or user preference, propose a resolution that best serves the user's current intent.
Weekly Installs
569
Repository
davidkiss/smart…i-skills
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass