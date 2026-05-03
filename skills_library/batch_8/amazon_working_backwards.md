---
title: amazon-working-backwards
url: https://skills.sh/robdefeo/agent-skills/amazon-working-backwards
---

# amazon-working-backwards

skills/robdefeo/agent-skills/amazon-working-backwards
amazon-working-backwards
Installation
$ npx skills add https://github.com/robdefeo/agent-skills --skill amazon-working-backwards
Summary

Guide ideas through Amazon's Working Backwards process, from 5 Questions to PR-FAQ.

Supports six entry points: drafting 5Q answers from a rough idea, refining existing answers, verifying answers with probing questions, generating a PR-FAQ document, reviewing an existing PR-FAQ, or clarifying any process element
The 5 Questions phase forces clarity on customer, problem, benefit, validation, and experience before any document writing
The PR-FAQ phase transforms solid 5Q answers into a press release and dual FAQ (external customer questions, internal stakeholder questions)
All substantive content writes directly to timestamped markdown files; feedback and iteration happen in chat
SKILL.md
Amazon Working Backwards

The Working Backwards process moves from idea to PR-FAQ in two phases: first answer the 5 Questions to force clarity of thinking, then write a PR-FAQ document that brings the idea to life for readers.

Workflow

Determine the entry point based on what the user provides:

Starting from a rough idea or proposal? → Follow the "5 Questions Phase" below Have 5Q answers to refine/verify? → Read references/five-questions-guide.md and apply the verification checklist Ready to write a PR-FAQ? → Follow the "PR-FAQ Phase" below Have a PR-FAQ to review? → Read references/prfaq-template.md and evaluate against the writing standards and common rejection reasons Want to clarify a specific element? → Read the relevant reference file for that phase

Output Convention

Always write to a file from the start. Do not draft in chat.

5Q answers: Write to YYYY-MM-DD - [Product Name] 5Q.md
PR-FAQ: Write to YYYY-MM-DD - [Product Name] PR-FAQ.md
Iterations: Edit the file in place; summarize changes in chat
Word format: If the user requests .docx, use the docx skill to produce a formatted document

When asking clarifying questions or presenting feedback, respond in chat. All substantive content (5Q answers, PR-FAQ drafts) goes to file.

5 Questions Phase

The 5 Questions force clarity before any document writing begins:

Who is the customer?
What is the customer problem or opportunity?
What is the most important customer benefit?
How do we know what the customer needs or wants?
What does the customer experience look like?
Drafting 5Q Answers
Read references/five-questions-guide.md for the quality bar and pitfalls for each question
Read references/examples.md to see a worked example from idea through 5Q to PR-FAQ
Ask clarifying questions if the user's idea is too vague to answer any question well — ask one question at a time
Draft all 5 answers, following the "What a strong answer looks like" guidance for each
Write answers to the 5Q file; summarize in chat and ask for feedback; iterate by editing the file
Verifying 5Q Answers

When reviewing or verifying answers (user's own or previously drafted):

Read references/five-questions-guide.md
Apply the verification checklist (coherence, specificity, customer obsession, intellectual honesty)
Use the probing questions from the guide to challenge weak areas
Present specific, actionable feedback — not generic praise
PR-FAQ Phase

Once 5Q answers are solid, generate the PR-FAQ document.

Read references/prfaq-template.md for the exact structure and quality bar
Read references/examples.md if not already loaded
Write the Press Release section, mapping: Q2 → problem paragraph, Q3 → solution paragraph, Q5 → experience paragraph, Q1 → customer quote persona
Write External FAQ (5-10 customer questions)
Write Internal FAQ (5-10 stakeholder questions)
Write to the PR-FAQ file; summarize in chat and ask for feedback; iterate by editing the file
Reviewing an Existing PR-FAQ
Read references/prfaq-template.md, paying attention to the "Common Rejection Reasons" section
Evaluate each section of the PR-FAQ against the writing standards
Check that the PR-FAQ is internally consistent (problem → benefit → experience alignment)
Provide specific, section-by-section feedback with concrete suggestions for improvement
Weekly Installs
469
Repository
robdefeo/agent-skills
GitHub Stars
3
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass