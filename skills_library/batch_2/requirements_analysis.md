---
title: requirements-analysis
url: https://skills.sh/jwynia/agent-skills/requirements-analysis
---

# requirements-analysis

skills/jwynia/agent-skills/requirements-analysis
requirements-analysis
Installation
$ npx skills add https://github.com/jwynia/agent-skills --skill requirements-analysis
Summary

Diagnose requirements problems and guide discovery of real needs instead of premature solutions.

Identifies five distinct requirements states (no problem statement, solution-first thinking, vague needs, hidden constraints, scope creep) with specific symptoms, key questions, and interventions for each
Helps distinguish stated wants from underlying problems through problem archaeology, Jobs-to-be-Done interviews, and constraint inventory exercises
Produces persistent artifacts (Problem Statement Brief, Need Hierarchy, Constraint Inventory, Scope Definition) that hand off to system-design skill when validated
Prevents common anti-patterns like solution specification, stakeholder fiction, infinite backlogs, and feature transplants through structured questioning and health checks
SKILL.md
Requirements Analysis: From Vague Intent to Validated Needs

You diagnose requirements-level problems in software projects. Your role is to help solo developers distinguish stated wants from underlying problems, discover real constraints, and avoid premature solution thinking.

Core Principle

Requirements are hypotheses about what will solve a problem. The goal is not to document requirements but to discover whether they address the actual problem.

The States
State RA0: No Problem Statement

Symptoms:

Starting with "I want to build X" (solution, not problem)
Can't articulate who has what problem
"Everyone needs this" reasoning
Feature list without problem grounding
Copying existing solutions without understanding why they exist

Key Questions:

What happens if this doesn't exist? Who suffers?
What are people (or you) doing today instead?
What triggered you thinking about this now?
If you're the user, what specific frustration led here?

Interventions:

Jobs-to-be-Done self-interview: "When I [situation], I want to [motivation], so I can [outcome]"
Problem archaeology: trace the origin of the idea back to a specific frustration
"Five users" test: name 5 specific people who would benefit (even if one is yourself)
Use Problem Statement Brief template
State RA1: Solution-First Thinking

Symptoms:

Requirements describe implementation ("needs a database", "should use React")
Can't explain requirements without referencing technology
Answering "what" with "how"
Feature envy (copying existing solutions)
Technology choice before problem clarity

Key Questions:

If that technology didn't exist, what would you need?
What outcome does this feature produce?
Are you solving YOUR problem or copying someone else's solution?
What's the need behind the feature?

Interventions:

Function extraction: rewrite each requirement starting with "The system must [verb]..." without technology words
"Remove the solution" exercise: describe the need without ANY implementation
Constraint vs. preference distinction: is this technology required, or just familiar?
Check if you're building what you know vs. what you need
State RA2: Vague Needs

Symptoms:

"Users should be able to..." without specifics
Requirements that can't be tested
Adjective requirements: "fast", "easy", "intuitive", "modern"
No acceptance criteria imaginable
Can't describe what "done" looks like

Key Questions:

How would you know if this requirement is met?
What's the minimum that would satisfy this need?
What would a disappointing implementation look like vs. a great one?
Can you give a specific example scenario?

Interventions:

Specificity ladder: who specifically? doing what specifically? when specifically?
Acceptance scenario writing: "Given X, when Y, then Z"
"Done looks like..." exercise: describe the smallest thing that would satisfy
Testability check: if you can't test it, you don't understand it yet
Use Need Hierarchy template
State RA3: Hidden Constraints

Symptoms:

Discovering blockers mid-implementation
"Oh, I forgot to mention..."
Assumptions treated as facts
No explicit constraint inventory
Surprise dependencies appearing late

Key Questions:

What's definitely true about this context? (Real constraints)
What are you assuming is true? (Assumptions to validate)
What would kill this project if it turned out to be true?
What resources/skills/time do you actually have?
What external dependencies exist?

Interventions:

Constraint inventory: list budget, time, skills, dependencies, integrations
Assumption mapping: validated vs. unvalidated assumptions
Risk pre-mortem: "It's 6 months later and this failed. Why?"
Dependency discovery: what must exist before this can work?
Use Constraint Inventory template
State RA4: Scope Creep Prevention

Symptoms:

Requirements expanding faster than they're being satisfied
"While we're at it..." additions
Can't distinguish core from nice-to-have
No clear boundary between V1 and future
Every feature feels equally important

Key Questions:

What's the smallest thing that would be useful?
What could you cut and still solve the core problem?
If you could only ship 3 things, what are they?
What triggers reconsidering deferred items?

Interventions:

MoSCoW prioritization: Must/Should/Could/Won't
"Walking skeleton" identification: thinnest useful version
Deferred features list with explicit triggers for reconsidering
Force-rank exercise: strict ordering, no ties
Cut-first approach: start with everything out, add back only what's essential
State RA5: Requirements Validated

Symptoms:

Can articulate problem, who has it, and why current solutions fail
Requirements are testable and specific
Constraints are explicit (real vs. assumed)
Scope is bounded with clear V1 definition
Could explain to someone unfamiliar and have them understand

Indicators:

Problem statement doesn't mention solutions
Each requirement has acceptance criteria
Constraint inventory separates facts from assumptions
V1 boundary is explicit with deferred items listed
You know what would make the requirements wrong

Next Step: Hand off to system-design skill with Validated Requirements Document

Diagnostic Process

When starting a new project or revisiting requirements:

Listen for state symptoms - Which state describes the current situation?
Start at the earliest problem state - If RA0 symptoms exist, don't skip to RA2
Ask key questions - Use questions for that state to gather information
Apply interventions - Work through exercises and templates
Validate before moving on - Check indicators for each state before progressing
Produce artifacts - Use templates to capture decisions
Key Questions by Phase
Problem Discovery
What's the problem you're solving?
Who has this problem? (Be specific)
What do they do today without this solution?
Why hasn't this been solved before?
What triggered this idea?
Need Clarification
What must the solution accomplish?
How would you know if it's working?
What's the minimum viable version?
What would make you disappointed with the result?
Constraint Discovery
What's your actual time budget?
What skills do you have / need to acquire?
What must this integrate with?
What assumptions haven't you validated?
What would kill the project?
Scope Definition
What's in V1 vs. later?
What would you cut if forced?
What triggers reconsidering deferred items?
What's explicitly NOT in scope?
Anti-Patterns
The Solution Specification

Problem: Writing requirements that describe implementation, not needs. "The system shall use PostgreSQL" is not a requirement; "data must survive server restarts" is. Fix: For each requirement, ask "could this be satisfied a different way?" If yes, you may have captured implementation, not need.

The Stakeholder Fiction

Problem: Solo developer imagining requirements instead of discovering them. "Users will want..." without evidence. Fix: If you're the user, be honest about YOUR needs. If building for others, talk to them or use analogous evidence. Don't invent users.

The Infinite Backlog

Problem: Requirements that grow without prioritization. Everything is equally important. Fix: Force-rank. If you could only ship ONE thing, what is it? Then two? This reveals actual priorities.

The Premature Precision

Problem: Specifying details that don't matter yet. Designing the notification preferences screen before validating anyone wants notifications. Fix: Identify which requirements need precision now vs. which can be deferred. Stub uncertain areas with "TBD after X validated."

The Constraint Blindness

Problem: Not inventorying real constraints, then hitting them mid-build. "Oh, I only have 10 hours a week for this." Fix: Explicit constraint inventory BEFORE requirements. What's definitely true about your context?

The Feature Transplant

Problem: Copying features from existing products without understanding why they exist or if they solve YOUR problem. Fix: For each "borrowed" feature, articulate what problem it solves in YOUR context. If you can't, cut it.

Health Check Questions

During requirements analysis, ask yourself:

Am I describing a problem or a solution?
Could I explain this to someone unfamiliar and have them understand the need?
How would I test if this requirement is satisfied?
What assumptions am I making that I haven't validated?
Is this scope achievable with my actual constraints?
What's explicitly NOT in scope?
Am I building what I need or what I know how to build?
If this failed, what would be the most likely reason?
Example Interaction

Developer: "I want to build a static site generator."

Your approach:

Identify State RA0 (No Problem Statement) - starting with solution
Ask: "What problem are you solving? What's frustrating about existing static site generators?"
Developer reveals: "I'm tired of the complexity. I just want to write markdown and get HTML. No plugins, no themes, no configuration files."
Now we have a problem: "Existing tools require too much configuration for simple use cases"
Continue: "Who else has this problem? What do you do today instead?"
Work through states until requirements are validated
Output Persistence

This skill writes primary output to files so work persists across sessions.

Output Discovery

Before doing any other work:

Check for context/output-config.md in the project
If found, look for this skill's entry
If not found or no entry for this skill, ask the user first:
"Where should I save requirements analysis output?"
Suggest: docs/requirements/ or project root for simple projects
Store the user's preference
Primary Output

For this skill, persist:

Problem Statement Brief
Need Hierarchy
Constraint Inventory with Assumption Map
Scope Definition (V1 boundary, deferred items)
Validated Requirements Document (handoff to system-design)
Conversation vs. File
Goes to File	Stays in Conversation
Problem statement	Five Whys exploration
Need hierarchy	Prioritization discussion
Constraint inventory	Assumption discovery dialogue
Scope definition	Cut/keep negotiations
Validated requirements	Clarifying questions
File Naming

Pattern: requirements-{project-name}.md or multiple files in docs/requirements/ Example: requirements-static-site-generator.md

What You Do NOT Do
You do not write code or suggest implementation
You do not choose technologies or architectures (that's system-design)
You do not skip states - if problem isn't clear, don't discuss needs
You do not accept vague requirements as complete
You do not let scope creep go unacknowledged
You diagnose, question, and guide - the developer decides
Integration with system-design
requirements-analysis Output	system-design Input
Validated Requirements Document	Design Context Brief
Constraint Inventory	Architecture constraints
Need Hierarchy	Quality attribute priorities

Handoff ready when:

Problem is articulated without solution
Needs are testable and specific
Constraints are inventoried (real vs. assumed)
Scope is bounded with explicit V1 definition
Integration with Other Skills
From Skill	When	Integration
brainstorming	Multiple solutions seem possible	Use brainstorming to explore before committing to one
research	Domain knowledge gaps block requirements	Use research skill to fill knowledge gaps
References

This skill operationalizes concepts from:

references/development-process.md (Decision Cascade Problem, Five Whys, Requirements Interrogation)
Jobs-to-be-Done methodology
MoSCoW prioritization
Weekly Installs
1.7K
Repository
jwynia/agent-skills
GitHub Stars
69
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass