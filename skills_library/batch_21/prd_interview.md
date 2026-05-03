---
title: prd-interview
url: https://skills.sh/mwguerra/claude-code-plugins/prd-interview
---

# prd-interview

skills/mwguerra/claude-code-plugins/prd-interview
prd-interview
Installation
$ npx skills add https://github.com/mwguerra/claude-code-plugins --skill prd-interview
SKILL.md
PRD Interview Skill

Guide comprehensive interviews to transform rough ideas into actionable Product Requirements Documents through structured discovery across 8 categories.

Core Interview Process
Interview Flow
Initial Prompt: Capture the base idea in user's own words
Category-Based Discovery: Work through relevant categories using AskUserQuestion
Adaptive Branching: Skip irrelevant questions based on context
Progressive Summarization: Summarize after each category before moving on
Document Generation: Create the final PRD with Mermaid diagrams
Task Integration: Offer to generate hierarchical tasks via taskmanager
Interview Categories

Conduct interviews across these 8 categories (adapt based on PRD type):

Category	Focus Areas	When to Use
Problem & Context	Pain points, current state, why now	Always
Users & Customers	Personas, segments, user journeys	Always
Solution & Features	Feature list, MVP scope, priorities	Always
Technical Implementation	Architecture, stack, integrations	Always
Business & Value	ROI, pricing, revenue model	Products, major features
UX & Design	Flows, wireframes, accessibility	UI-facing work
Risks & Concerns	Dependencies, assumptions, blockers	Always
Testing & Quality	Test strategies, acceptance criteria	Always
Question Guidelines

When using AskUserQuestion:

Ask 2-4 questions per round maximum
Provide concrete options when possible
Enable multiSelect for non-mutually-exclusive choices
Include "Other" automatically (tool handles this)
Use short headers (max 12 chars)
Adaptive Branching Rules

Skip categories based on context:

Internal tool: Skip pricing/revenue questions in Business & Value
Backend-only: Minimize UX & Design category
Bug fix: Focus on Problem & Context, Technical, Testing
Feature: Full interview but lighter on Business & Value
Session State Management
State File Location

Save interview progress to: .taskmanager/prd-state.json

State Structure
{
  "sessionId": "uuid",
  "prdType": "product|feature|bugfix",
  "slug": "feature-name",
  "startedAt": "ISO timestamp",
  "lastUpdatedAt": "ISO timestamp",
  "currentCategory": "category-name",
  "completedCategories": ["category1", "category2"],
  "answers": {
    "category-name": {
      "question-key": "answer-value"
    }
  },
  "initialPrompt": "User's original description"
}

Resuming Sessions

When /prd-builder:prd or similar is invoked:

Check for existing state in .taskmanager/prd-state.json
If found, ask user: "Resume previous session for '{slug}' or start fresh?"
If resuming, continue from currentCategory
If starting fresh, archive old state and begin new session
PRD Document Structure
Output Location

Save PRDs to: docs/prd/prd-{slug}.md

Document Template

Generate PRDs following the template in templates/prd-template.md. Key sections:

Header: Title, version, date, status, author
Executive Summary: One-paragraph overview
Problem Statement: What problem, who has it, current solutions
Users & Personas: Target users with characteristics
Solution Overview: High-level approach
Features & Requirements: Detailed feature breakdown with priorities
Technical Architecture: Stack, integrations, Mermaid diagrams
User Experience: Flows, wireframes references
Business Case: Value proposition, pricing (if applicable)
Risks & Mitigations: Known risks with mitigation strategies
Testing Strategy: Acceptance criteria, test approach
Timeline & Milestones: Phase breakdown (if applicable)
Open Questions: Unresolved items for follow-up
Mermaid Diagrams

Include these diagrams where appropriate:

Architecture Diagram:

graph TB
    subgraph Frontend
        UI[User Interface]
    end
    subgraph Backend
        API[API Layer]
        DB[(Database)]
    end
    UI --> API --> DB


User Flow Diagram:

flowchart LR
    A[Start] --> B{Decision}
    B -->|Yes| C[Action]
    B -->|No| D[Alternative]

TaskManager Integration
Task Generation Process

After PRD completion:

Parse all features from the PRD
Create hierarchical task structure:
Parent task per major feature
Child tasks for implementation steps
Use /taskmanager:plan with the PRD file path
Task Hierarchy Example
Feature: User Authentication
├── Setup authentication infrastructure
├── Implement login endpoint
├── Implement registration endpoint
├── Add password reset flow
├── Create authentication middleware
└── Write authentication tests

Automatic Execution

After generating tasks, ask: "Tasks created. Start autonomous execution?" If yes, invoke /taskmanager:run to begin implementation.

PRD Types
Full Product PRD (/prd-builder:prd)

Complete interview covering all 8 categories in depth:

10-15 question rounds
Comprehensive documentation
Full Mermaid diagrams
Complete task breakdown
Feature PRD (/prd-builder:feature)

Lighter interview focused on implementation:

5-8 question rounds
Skip or minimize Business & Value (unless monetized feature)
Focus on Technical, UX, Testing
Assume product context exists
Bug Fix PRD (/prd-builder:bugfix)

Problem-focused documentation:

3-5 question rounds
Heavy focus on Problem & Context
Technical root cause analysis
Regression testing strategy
Skip Business, minimize UX
Refine PRD (/prd-builder:refine)

Enhance existing PRDs:

Read and analyze existing PRD
Identify weak or missing sections
Ask targeted questions for gaps only
Merge new answers into existing document
Preserve original content where adequate
Additional Resources
Reference Files

Detailed question banks for each category:

references/question-bank.md - Complete question library organized by category
Template Files

PRD output template:

templates/prd-template.md - Full PRD document structure
Weekly Installs
22
Repository
mwguerra/claude…-plugins
GitHub Stars
29
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass