---
title: ralph-loop
url: https://skills.sh/andrelandgraf/fullstackrecipes/ralph-loop
---

# ralph-loop

skills/andrelandgraf/fullstackrecipes/ralph-loop
ralph-loop
Installation
$ npx skills add https://github.com/andrelandgraf/fullstackrecipes --skill ralph-loop
Summary

Automated agent-driven development loop that executes AI agents against user story acceptance criteria.

Structures features as JSON-formatted user stories with testable acceptance criteria that agents can verify and track
Runs AI agents in a continuous loop to implement features, check acceptance criteria, and log progress for subsequent agent iterations
Requires prerequisite setup of AI coding agent configuration and user stories framework before running the Ralph agent loop
Integrates with AI coding agents like Cursor, GitHub Copilot, or Claude Code for consistent, project-aware development
SKILL.md
Ralph Loop

Complete setup for automated agent-driven development. Define features as user stories with testable acceptance criteria, then run AI agents in a loop until all stories pass.

Prerequisites

Complete these recipes first (in order):

AI Coding Agent Configuration

Configure AI coding agents like Cursor, GitHub Copilot, or Claude Code with project-specific patterns, coding guidelines, and MCP servers for consistent AI-assisted development.

curl -H "Accept: text/markdown" https://fullstackrecipes.com/api/recipes/agent-setup

Cookbook - Complete These Recipes in Order
User Stories Setup

Create a structured format for documenting feature requirements as user stories. JSON files with testable acceptance criteria that AI agents can verify and track.

curl -H "Accept: text/markdown" https://fullstackrecipes.com/api/recipes/user-stories-setup

Working with User Stories

Document and track feature implementation with user stories. Workflow for authoring stories, building features, and marking acceptance criteria as passing.

curl -H "Accept: text/markdown" https://fullstackrecipes.com/api/recipes/using-user-stories

Ralph Agent Loop

Set up automated agent-driven development with Ralph. Run AI agents in a loop to implement features from user stories, verify acceptance criteria, and log progress for the next agent.

curl -H "Accept: text/markdown" https://fullstackrecipes.com/api/recipes/ralph-setup

Weekly Installs
2.0K
Repository
andrelandgraf/f…krecipes
GitHub Stars
14
First Seen
1 day ago
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn