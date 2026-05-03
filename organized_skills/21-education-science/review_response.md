---
rating: ⭐⭐
title: review-response
url: https://skills.sh/galaxy-dawn/claude-scholar/review-response
---

# review-response

skills/galaxy-dawn/claude-scholar/review-response
review-response
Installation
$ npx skills add https://github.com/galaxy-dawn/claude-scholar --skill review-response
SKILL.md
Review Response

A systematic review response workflow that helps researchers efficiently and professionally reply to reviewer comments.

Core Features
Review Analysis - Parse and classify reviewer comments (Major/Minor/Typo/Misunderstanding)
Response Strategy - Develop response strategies for different comment types (Accept/Defend/Clarify/Experiment)
Rebuttal Writing - Write structured, professional rebuttal documents
Tone Management - Optimize tone to maintain professionalism, respect, and evidence-based arguments
Workflow
Receive reviewer comments -> Parse and classify -> Develop strategy -> Write responses -> Tone check -> Final rebuttal

When to Use

Use this skill when you need to:

"Help me write a rebuttal"
"How to respond to reviewer comments"
"Analyze these review comments"
"Develop a review response strategy"
Usage Steps
Provide reviewer comments - Share the reviewer comments text or file with Claude
Analysis and classification - Claude automatically parses and classifies the comments
Strategy recommendations - Receive response strategy suggestions for each comment
Write rebuttal - Generate a structured rebuttal document based on the strategy
Optimize tone - Review and optimize the professionalism and politeness of responses
Core Principles
Professionalism - Maintain an academically professional tone and expression
Respectfulness - Respect the reviewers' opinions and time
Evidence-based - Support every response with sufficient reasoning and evidence
Completeness - Ensure all reviewer comments receive a response
Success Factors (Based on ICLR Spotlight Paper Analysis)

Key lessons extracted from successful rebuttal cases:

1. Acknowledge Strengths, Respond Positively to Criticism
Reviewers will first acknowledge the paper's strengths (novelty, impact, practical applicability)
Even spotlight papers receive constructive criticism
Strategy: Thank reviewers for acknowledged strengths first, then address criticism specifically
2. Provide Clarity and Intuitive Understanding
Even high-quality papers may have clarity issues
Need to provide intuition and detailed explanations for readers with different backgrounds
Strategy: Expand key sections, move technical details to appendix, add step-by-step walkthroughs
3. Thorough Justification of Experimental Setup
Need to justify experimental setup choices
Consider and discuss alternative metrics
Provide comprehensive experiments to support claims
Strategy: Add ablation studies, explain why specific experimental setups were chosen
4. Emphasis on Ethical Considerations
For research involving privacy, security, and other sensitive topics, ethical considerations are crucial
Reviewers pay special attention to ethical implications
Strategy: Proactively discuss ethical considerations, even if reviewers don't explicitly request it
5. Highlight Practical Application Value
Reviewers value practical applicability and scalability of methods
"Easily applicable" and "scalable" are important strengths
Strategy: Emphasize practical benefits and scalability in the rebuttal
Integration with paper-miner global writing memory

When the rebuttal task involves:

tone calibration,
rebuttal phrasing,
clarification language,
structuring multi-point responses,
or learning from strong prior paper/review writing,

read this file before drafting:

~/.claude/skills/ml-paper-writing/references/knowledge/paper-miner-writing-memory.md
Default read order for rebuttal work
reviewer comments and paper context
paper-miner-writing-memory.md
references/response-strategies.md
references/rebuttal-templates.md
references/tone-guidelines.md

Read narrowly:

start with How this helps our writing,
then inspect Reusable phrasing,
then inspect Venue-specific signals if the rebuttal is venue-sensitive,
use Writing patterns mined only when the response needs stronger rhetorical structure.

Do not quote the memory mechanically. Use it to improve structure, clarity, restraint, and professionalism.

Reference Documents

For detailed guides, refer to:

references/review-classification.md - Review comment classification criteria
references/response-strategies.md - Response strategy library
references/rebuttal-templates.md - Rebuttal templates and examples
references/tone-guidelines.md - Tone and expression guidelines
Related Tools
Agent: rebuttal-writer - Dedicated agent for rebuttal writing and optimization
Command: /rebuttal <review_file> - Quick-start the rebuttal workflow
Weekly Installs
109
Repository
galaxy-dawn/cla…-scholar
GitHub Stars
3.5K
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubWarn
SocketPass
SnykPass