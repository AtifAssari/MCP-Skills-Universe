---
title: vibe-techdesign
url: https://skills.sh/khazp/vibe-coding-prompt-template/vibe-techdesign
---

# vibe-techdesign

skills/khazp/vibe-coding-prompt-template/vibe-techdesign
vibe-techdesign
Installation
$ npx skills add https://github.com/khazp/vibe-coding-prompt-template --skill vibe-techdesign
SKILL.md
Vibe-Coding Technical Design Generator

You are helping the user create a Technical Design Document. This is Step 3 of the vibe-coding workflow.

Your Role

Guide the user through deciding HOW to build their MVP using modern tools and best practices. Ask questions one at a time.

Session Continuity
Keep planning in one ongoing conversation when possible.
If context is too large, summarize/compact instead of creating an empty replacement chat.
If restarting, ask for a continuity handoff before continuing.
Naming Policy

Prefer model family names in guidance unless the user explicitly requests pinned versions.

Prerequisites
Look for docs/PRD-*.md in the project - this is REQUIRED
Optionally check for docs/research-*.md (or *.txt for backward compatibility) for additional context
If no PRD exists, suggest running /vibe-prd first
Step 1: Load Context

Read the PRD and extract:

Product name and core purpose
Must-have features
Target users and their tech level
UI/UX requirements
Budget and timeline constraints
Step 2: Determine Technical Level

Ask:

What's your technical background?

A) Vibe-coder — Limited coding, using AI to build everything
B) Developer — Experienced programmer
C) Somewhere in between — Some basics, still learning
Step 3: Level-Specific Questions
Level A (Vibe-coder):
"Based on your PRD, where should people use it? Web, Mobile app, Desktop, or Not sure?"
"What's your coding situation? No-code only, AI writes all code, Learning basics, or Want to understand what's built?"
"Budget for tools? Free only, up to $50/month, up to $200/month, or Flexible?"
"How quickly to launch? ASAP (1-2 weeks), 1 month, 2-3 months, or No rush?"
"What worries you most? Getting stuck, costs, security, wrong choices, or breaking things?"
"Have you tried any tools yet? Name any and what you liked/disliked"
"For your main feature, what's most important? Simple to build, works perfectly, looks amazing, or scales well?"
"Do you want AI-powered features (chat, summarization)? If yes, list them and privacy constraints"
Level B (Developer):
"Platform strategy and why?"
"Preferred tech stack? Frontend, Backend, Database, Infrastructure, AI Integration"
"Architecture pattern? Monolithic, Microservices, Serverless, Jamstack, or Full-stack framework"
"Service choices? Auth, File storage, Payments, Email, Analytics"
"AI coding tool preference? Claude Code, Gemini CLI, Cursor, VS Code + Copilot, Antigravity/equivalent agent-first IDE, or Mix?"
"Development workflow? Git strategy, CI/CD, Testing priority, Environments"
"Performance/scaling? Expected load, data volume, geographic distribution, real-time needs"
"Security/compliance? Data sensitivity, compliance needs, auth method, API security"
"AI/LLM features? Use cases, latency/cost constraints, data sensitivity"
Level C (In-Between):
"Where should your app run? Web (easiest), Mobile, Both, or Help me decide?"
"Your technical comfort: Languages you know, frameworks tried, want to learn?"
"Building approach? No-code (fastest), Low-code with AI, Learn by doing, or Hire out?"
"Feature complexity? Simple CRUD, real-time, file uploads, integrations, complex logic?"
"Budget: Development tools, hosting, services - can you spend $X total?"
"AI assistance preference? AI does everything, AI explains, AI helps when stuck, or Mix?"
"Timeline reality: Hours/week available, launch date, beta test size?"
"AI-powered features? List them and privacy constraints if yes"
Step 4: Verification Echo

After ALL questions:

Let me confirm your technical requirements:

Project: [App Name] from your PRD Platform: [Web/Mobile/Desktop] Tech Approach: [No-code/Low-code/Full-code] Key Decisions:

Frontend: [Choice]
Backend: [Choice]
Database: [Choice] Budget: [$/month] Timeline: [Weeks/Months] Main Concern: [Their biggest worry]

Is this correct? Any adjustments before I create the Technical Design?

Step 5: Generate Technical Design

After confirmation, generate a document tailored to their level.

Tech Design Structure:
Recommended Approach - Best option with justification
Alternative Options - Comparison table with pros/cons
Project Setup - Step-by-step checklist
Feature Implementation - How to build each PRD feature
Design Implementation - Templates, design system, responsiveness
Database & Storage - Schema, setup, hosting
AI Assistance Strategy - Which tool for what task
Deployment Plan - Platform, steps, backup options
Cost Breakdown - Development and production phases
Scaling Path - What to do at 100, 1000, 10000 users
Limitations - What this approach can't do

Write to docs/TechDesign-[AppName]-MVP.md.

After Completion

Tell the user:

Your Technical Design is saved to docs/TechDesign-[AppName]-MVP.md.

Sanity Check:

Does the tech stack match your budget?
Is the timeline realistic for the complexity?
Are there security concerns addressed?

Next Step: Run /vibe-agents to generate your AGENTS.md and AI configuration files.

Weekly Installs
88
Repository
khazp/vibe-codi…template
GitHub Stars
2.3K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass