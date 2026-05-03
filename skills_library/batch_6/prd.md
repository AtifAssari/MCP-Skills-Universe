---
title: prd
url: https://skills.sh/github/awesome-copilot/prd
---

# prd

skills/github/awesome-copilot/prd
prd
Installation
$ npx skills add https://github.com/github/awesome-copilot --skill prd
Summary

Generate comprehensive Product Requirements Documents that translate business vision into technical specifications.

Follows a strict three-phase workflow: discovery interview to fill knowledge gaps, analysis and scoping to identify dependencies, and technical drafting using a standardized PRD schema
Requires concrete, measurable success criteria and acceptance criteria; explicitly avoids vague language like "fast" or "intuitive" in favor of quantifiable benchmarks
Covers executive summary, user personas and stories, technical architecture, AI system requirements with evaluation strategies, and phased rollout planning with risk analysis
Includes discovery questions on core problems, success metrics, and constraints before generating any document; presents drafts for iterative feedback on specific sections
SKILL.md
Product Requirements Document (PRD)
Overview

Design comprehensive, production-grade Product Requirements Documents (PRDs) that bridge the gap between business vision and technical execution. This skill works for modern software systems, ensuring that requirements are clearly defined.

When to Use

Use this skill when:

Starting a new product or feature development cycle
Translating a vague idea into a concrete technical specification
Defining requirements for AI-powered features
Stakeholders need a unified "source of truth" for project scope
User asks to "write a PRD", "document requirements", or "plan a feature"
Operational Workflow
Phase 1: Discovery (The Interview)

Before writing a single line of the PRD, you MUST interrogate the user to fill knowledge gaps. Do not assume context.

Ask about:

The Core Problem: Why are we building this now?
Success Metrics: How do we know it worked?
Constraints: Budget, tech stack, or deadline?
Phase 2: Analysis & Scoping

Synthesize the user's input. Identify dependencies and hidden complexities.

Map out the User Flow.
Define Non-Goals to protect the timeline.
Phase 3: Technical Drafting

Generate the document using the Strict PRD Schema below.

PRD Quality Standards
Requirements Quality

Use concrete, measurable criteria. Avoid "fast", "easy", or "intuitive".

# Vague (BAD)
- The search should be fast and return relevant results.
- The UI must look modern and be easy to use.

# Concrete (GOOD)
+ The search must return results within 200ms for a 10k record dataset.
+ The search algorithm must achieve >= 85% Precision@10 in benchmark evals.
+ The UI must follow the 'Vercel/Next.js' design system and achieve 100% Lighthouse Accessibility score.

Strict PRD Schema

You MUST follow this exact structure for the output:

1. Executive Summary
Problem Statement: 1-2 sentences on the pain point.
Proposed Solution: 1-2 sentences on the fix.
Success Criteria: 3-5 measurable KPIs.
2. User Experience & Functionality
User Personas: Who is this for?
User Stories: As a [user], I want to [action] so that [benefit].
Acceptance Criteria: Bulleted list of "Done" definitions for each story.
Non-Goals: What are we NOT building?
3. AI System Requirements (If Applicable)
Tool Requirements: What tools and APIs are needed?
Evaluation Strategy: How to measure output quality and accuracy.
4. Technical Specifications
Architecture Overview: Data flow and component interaction.
Integration Points: APIs, DBs, and Auth.
Security & Privacy: Data handling and compliance.
5. Risks & Roadmap
Phased Rollout: MVP -> v1.1 -> v2.0.
Technical Risks: Latency, cost, or dependency failures.
Implementation Guidelines
DO (Always)
Define Testing: For AI systems, specify how to test and validate output quality.
Iterate: Present a draft and ask for feedback on specific sections.
DON'T (Avoid)
Skip Discovery: Never write a PRD without asking at least 2 clarifying questions first.
Hallucinate Constraints: If the user didn't specify a tech stack, ask or label it as TBD.
Example: Intelligent Search System
1. Executive Summary

Problem: Users struggle to find specific documentation snippets in massive repositories. Solution: An intelligent search system that provides direct answers with source citations. Success:

Reduce search time by 50%.
Citation accuracy >= 95%.
2. User Stories
Story: As a developer, I want to ask natural language questions so I don't have to guess keywords.
AC:
Supports multi-turn clarification.
Returns code blocks with "Copy" button.
3. AI System Architecture
Tools Required: codesearch, grep, webfetch.
4. Evaluation
Benchmark: Test with 50 common developer questions.
Pass Rate: 90% must match expected citations.
Weekly Installs
16.5K
Repository
github/awesome-copilot
GitHub Stars
32.0K
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass