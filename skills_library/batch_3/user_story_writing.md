---
title: user-story-writing
url: https://skills.sh/aj-geddes/useful-ai-prompts/user-story-writing
---

# user-story-writing

skills/aj-geddes/useful-ai-prompts/user-story-writing
user-story-writing
Installation
$ npx skills add https://github.com/aj-geddes/useful-ai-prompts --skill user-story-writing
Summary

Write user stories with clear acceptance criteria to guide development from the user's perspective.

Provides a structured template covering user role, desired action, business value, and detailed acceptance criteria using Given-When-Then format
Includes reference guides for story refinement, splitting, estimation, and acceptance criteria examples
Emphasizes user-focused writing, testability, and small story sizing appropriate for single-sprint completion
Covers best practices for avoiding common pitfalls like technical task focus, ambiguous criteria, and oversized stories
SKILL.md
User Story Writing
Table of Contents
Overview
When to Use
Quick Start
Reference Guides
Best Practices
Overview

Well-written user stories communicate requirements in a user-focused way, facilitate discussion, and provide clear acceptance criteria for developers and testers.

When to Use
Breaking down requirements into development tasks
Product backlog creation and refinement
Agile sprint planning
Communicating features to development team
Defining acceptance criteria
Creating test cases
Quick Start

Minimal working example:

# User Story Template

**Title:** [Feature name]

**As a** [user role/persona]
**I want to** [action/capability]
**So that** [business value/benefit]

---

## User Context

- User Role: [Who is performing this action?]
- User Goals: [What are they trying to accomplish?]
- Use Case: [When do they perform this action?]

---

## Acceptance Criteria

Given [precondition]
When [action]
Then [expected result]

Example:
// ... (see reference guides for full implementation)

Reference Guides

Detailed implementations in the references/ directory:

Guide	Contents
Story Refinement Process	Story Refinement Process
Acceptance Criteria Examples	Acceptance Criteria Examples
Story Splitting	Story Splitting
Story Estimation	Story Estimation
Best Practices
✅ DO
Write from the user's perspective
Focus on value, not implementation
Create stories small enough for one sprint
Define clear acceptance criteria
Use consistent format and terminology
Have product owner approve stories
Include edge cases and error scenarios
Link to requirements/business goals
Update stories based on learning
Create testable stories
❌ DON'T
Write technical task-focused stories
Create overly detailed specifications
Write stories that require multiple sprints
Forget about non-functional requirements
Skip acceptance criteria
Create dependent stories unnecessarily
Write ambiguous acceptance criteria
Ignore edge cases
Create too large stories
Change stories mid-sprint without discussion
Weekly Installs
525
Repository
aj-geddes/usefu…-prompts
GitHub Stars
193
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass