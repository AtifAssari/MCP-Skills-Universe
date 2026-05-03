---
title: ask-plan-questions
url: https://skills.sh/sebkay/skills/ask-plan-questions
---

# ask-plan-questions

skills/sebkay/skills/ask-plan-questions
ask-plan-questions
Installation
$ npx skills add https://github.com/sebkay/skills --skill ask-plan-questions
SKILL.md
Ask Plan Questions

Identify uncertainty in the plan and ask only the questions that materially reduce implementation risk.

Use the AskQuestion tool for every question.

Do not force a fixed number of questions. Ask only relevant questions, and stop once risk is acceptably low.

Workflow
Review current context and plan.
Identify gaps that could cause defects, rework, or delivery delays.
Prioritize questions by impact and urgency.
Ask concise, concrete questions with the AskQuestion tool.
Ask in small batches (1-3 at a time) when many gaps exist.
Incorporate user answers before asking the next batch.
Continue until the remaining ambiguity is low-risk.
Question Selection Rules
Ask only questions that change implementation decisions.
Skip questions already answered in the thread or files.
Prefer specific questions over broad prompts.
Tie each question to one risk area.
De-prioritize style preferences unless they affect architecture or acceptance.
Question Bank (pick only relevant items)

Use these as templates. Reword for project context.

What is the single success criterion for this task?
What is explicitly out of scope for this implementation?
Which environments must this work in (local, staging, production)?
Are there hard deadlines or sequencing constraints?
Which existing behavior must remain unchanged?
What are the non-negotiable technical constraints (language, framework, versions)?
What data contracts or schemas are fixed versus negotiable?
What are the expected edge cases and failure modes?
What performance/reliability targets must be met?
What security/privacy/compliance requirements apply?
What is the source of truth when docs and code disagree?
What acceptance tests define "done"?
What level of backward compatibility is required?
What rollout strategy is expected (flag, staged, immediate)?
Who is the final approver for tradeoff decisions?
Completion Criteria

Finish questioning when all of the following are true:

Scope boundaries are clear.
Constraints and dependencies are explicit.
Acceptance criteria are testable.
Known high-risk assumptions are resolved or documented.
Weekly Installs
15
Repository
sebkay/skills
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass