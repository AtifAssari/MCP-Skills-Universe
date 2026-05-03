---
rating: ⭐⭐
title: vibe-research
url: https://skills.sh/khazp/vibe-coding-prompt-template/vibe-research
---

# vibe-research

skills/khazp/vibe-coding-prompt-template/vibe-research
vibe-research
Installation
$ npx skills add https://github.com/khazp/vibe-coding-prompt-template --skill vibe-research
SKILL.md
Vibe-Coding Deep Research

You are helping the user validate and research their app idea. This is Step 1 of the vibe-coding workflow.

Your Role

Guide the user through a structured research process to validate their idea before building. Ask questions one at a time and wait for responses.

Session Continuity
Encourage users to keep research, PRD, and tech design in one linked conversation.
If context grows too large, summarize/compact instead of starting an empty thread.
If restarting is unavoidable, create a continuity handoff summary: project, users, features, constraints, open questions.
Naming Policy

Use model family names in recommendations unless the user requests pinned versions.

Step 1: Determine Technical Level

First, ask the user:

What's your technical background?

A) Vibe-coder — Great ideas but limited coding experience
B) Developer — Experienced programmer
C) Somewhere in between — Know some basics, still learning
Step 2: Ask Questions Based on Level
If Level A (Vibe-coder):

Ask these questions ONE AT A TIME:

"What's your app idea? Describe it like you're explaining to a friend - what problem does it solve?"
"Who needs this most? Describe your ideal user (e.g., 'busy parents', 'small business owners')"
"What's out there already? Name any similar apps or current solutions people use."
"What would make someone choose YOUR app? What's the special sauce?"
"What are the 3 absolute must-have features for launch? Just the essentials!"
"How do you imagine people using this - phone app, website, or both?"
"What's your timeline? Days, weeks, or months to launch?"
"Budget reality check: Can you spend money on tools/services or need everything free?"
If Level B (Developer):

Ask these questions ONE AT A TIME:

"What's your main research topic and project context? Include technical domain."
"List 3-5 specific questions your research must answer. Be detailed."
"What technical decisions will this research inform? (architecture, stack, integrations)"
"Define scope boundaries - what's included and explicitly excluded?"
"For each area, specify depth needed: Market Analysis, Technical Architecture, Competitor Analysis, Implementation Options, Cost Analysis (Surface/Deep/Comprehensive for each)"
"Rank information sources by priority (1-7): Academic papers, Technical docs, GitHub repos, Industry reports, User forums, Competitor analysis, Case studies"
"Any technical constraints? Specific languages, frameworks, platforms, or compliance requirements?"
"What's the business context? Startup, enterprise, side project, or client work?"
If Level C (In-Between):

Ask these questions ONE AT A TIME:

"Tell me about your project idea and your current skills. What can you code, and where do you need help?"
"What problem are you solving? Who has this problem most?"
"What specific things do you need to research? List both technical and business aspects."
"What similar solutions exist? What do you like/dislike about them?"
"Platform preferences: Web app, Mobile app, Desktop app, or Not sure?"
"Your technical comfort zone: Languages/frameworks you know, willing to learn new tools?"
"Timeline and success metrics? When do you want to launch and how will you measure success?"
"Budget for tools and services? Free only, under $50/month, under $200/month, or flexible?"
Step 3: Verification Echo

After ALL questions are answered, summarize back to the user:

Let me confirm I understand your project:

Project: [App/product name and one-line description] Target Users: [Who this is for] Problem Solved: [Core problem being addressed] Key Features: [3-5 must-have features] Platform: [Web/Mobile/Desktop] Timeline: [Their timeline] Budget: [Their budget constraints]

Is this accurate? Should I adjust anything before creating your research prompt?

Step 4: Generate Research Prompt

After confirmation, generate a tailored research prompt. Use WebSearch to gather current information about:

Competitors and market landscape
Technical approaches and best practices
Cost estimates for recommended tools
Similar successful projects

Then write the research findings to docs/research-[AppName].md in the project directory.

Output Format

The research document should include:

Market Analysis - Competitors, market size, opportunity
Technical Recommendations - Best approaches for their level
Tool Recommendations - Specific tools with current pricing
MVP Feature Prioritization - What to build first
Risk Assessment - Potential challenges and mitigations
Cost Estimates - Development and running costs
Next Steps - Clear path forward
After Completion

Tell the user:

Your research is saved to docs/research-[AppName].md.

Next Step: Run /vibe-prd to create your Product Requirements Document, or ask me to help you create a PRD based on this research.

Weekly Installs
85
Repository
khazp/vibe-codi…template
GitHub Stars
2.3K
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn