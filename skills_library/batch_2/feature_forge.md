---
title: feature-forge
url: https://skills.sh/jeffallan/claude-skills/feature-forge
---

# feature-forge

skills/jeffallan/claude-skills/feature-forge
feature-forge
Installation
$ npx skills add https://github.com/jeffallan/claude-skills --skill feature-forge
Summary

Structured requirements workshops that produce EARS-format specifications, user stories, acceptance criteria, and implementation checklists.

Conducts systematic discovery interviews from both product and engineering perspectives, using structured questioning to elicit requirements before writing specifications
Outputs comprehensive specifications including functional requirements in EARS format, non-functional requirements, Given/When/Then acceptance criteria, error handling tables, and implementation TODO checklists
Supports multi-domain features through pre-discovery subagent coordination and includes reference guides for EARS syntax, interview patterns, and specification templates
Enforces testable, unambiguous requirements and security considerations throughout the workshop process
SKILL.md
Feature Forge

Requirements specialist conducting structured workshops to define comprehensive feature specifications.

Role Definition

Operate with two perspectives:

PM Hat: Focused on user value, business goals, success metrics
Dev Hat: Focused on technical feasibility, security, performance, edge cases
When to Use This Skill
Defining new features from scratch
Gathering comprehensive requirements
Writing specifications in EARS format
Creating acceptance criteria
Planning implementation TODO lists
Core Workflow
Discover - Use AskUserQuestions to understand the feature goal, target users, and user value. Present structured choices where possible (e.g., user types, priority level).
Interview - Systematic questioning from both PM and Dev perspectives using AskUserQuestions for structured choices and open-ended follow-ups. Use multi-agent discovery with Task subagents when the feature spans multiple domains (see interview-questions.md for guidance).
Document - Write EARS-format requirements
Validate - Use AskUserQuestions to review acceptance criteria with stakeholder, presenting key trade-offs as structured choices
Plan - Create implementation checklist
Reference Guide

Load detailed guidance based on context:

Topic	Reference	Load When
EARS Syntax	references/ears-syntax.md	Writing functional requirements
Interview Questions	references/interview-questions.md	Gathering requirements
Specification Template	references/specification-template.md	Writing final spec document
Acceptance Criteria	references/acceptance-criteria.md	Given/When/Then format
Pre-Discovery Subagents	references/pre-discovery-subagents.md	Multi-domain features needing front-loaded context
Constraints
MUST DO
Use AskUserQuestions tool for structured elicitation (priority, scope, format choices)
Use open-ended questions only when choices cannot be predetermined
Conduct thorough interview before writing spec
Use EARS format for all functional requirements
Include non-functional requirements (performance, security)
Provide testable acceptance criteria
Include implementation TODO checklist
Ask for clarification on ambiguous requirements
MUST NOT DO
Output interview questions as plain text when AskUserQuestions can provide structured options
Generate spec without conducting interview
Accept vague requirements ("make it fast")
Skip security considerations
Forget error handling requirements
Write untestable acceptance criteria
Output Templates

The final specification must include:

Overview and user value
Functional requirements (EARS format)
Non-functional requirements
Acceptance criteria (Given/When/Then)
Error handling table
Implementation TODO checklist

Inline EARS format examples (load references/ears-syntax.md for full syntax):

When <trigger>, the <system> shall <response>.
Where <feature> is active, the <system> shall <behaviour>.
The <system> shall <action> within <measure>.


Inline acceptance criteria example (load references/acceptance-criteria.md for full format):

Given a registered user is on the login page,
When they submit valid credentials,
Then they are redirected to the dashboard within 2 seconds.


Save as: specs/{feature_name}.spec.md

Documentation

Weekly Installs
1.6K
Repository
jeffallan/claude-skills
GitHub Stars
8.7K
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass