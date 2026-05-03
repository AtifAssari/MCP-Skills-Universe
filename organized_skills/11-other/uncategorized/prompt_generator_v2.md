---
rating: ⭐⭐⭐
title: prompt-generator-v2
url: https://skills.sh/hoangvantuan/claude-plugin/prompt-generator-v2
---

# prompt-generator-v2

skills/hoangvantuan/claude-plugin/prompt-generator-v2
prompt-generator-v2
Installation
$ npx skills add https://github.com/hoangvantuan/claude-plugin --skill prompt-generator-v2
SKILL.md
Prompt Generator V2 — KERNEL Framework

Generate prompts that work on the first try. The KERNEL framework ensures every prompt has a clear goal, verifiable success criteria, and explicit constraints.

KERNEL at a Glance

Each letter is a checkpoint. Chi tiết + ví dụ before/after → kernel-framework.

Principle	Check	Action if failing
Keep simple	Describe in one sentence?	Split into prompt chain
Easy to verify	Stranger could verify?	Add measurable criteria
Reproducible	Works in 30 days?	Remove temporal refs, add versions
Narrow scope	One deliverable?	Extract goals into separate prompts
Explicit constraints	2-3 "do NOT" rules?	Add negative constraints
Logical structure	Context→Task→Constraints→Format?	Restructure
Workflow
Step 0: Determine Mode
User input	Mode	Action
Vague request ("help me write a prompt for X")	Create	Go to Step 1
Existing prompt provided	Improve	Run KERNEL checklist against the prompt, diagnose which principles fail, fix targeted. Skip to Step 2
Step 1: Understand Intent

Extract or ask (max 3 questions — skip if the request already answers them):

What's the single goal? — If multiple goals detected, suggest splitting into a prompt chain
What does success look like? — Specific, verifiable criteria (numbers, formats, concrete deliverables)
What should it NOT do? — Constraints and exclusions

If the user provides a vague request, propose a draft immediately and iterate — action beats interrogation.

Step 2: Apply KERNEL

Transform intent into a structured prompt. Run each principle as a mental checklist using the table above. For detailed explanations, consult kernel-framework.

Step 3: Generate the Prompt

Use this structure. Include only relevant sections — omit what doesn't apply:

## Context
[Background information the AI needs. Keep minimal — only what's necessary to understand the task. Include domain, audience, and relevant technical context.]

## Task
[One clear, specific goal. Start with an action verb. This is the single sentence that passes the K-test.]

## Constraints
- [What to do — specific, measurable behaviors]
- Do NOT [negative constraint 1]
- Do NOT [negative constraint 2]
- [Additional bounds: length, format, libraries, scope limits]

## Output Format
[Exact structure of the expected output. Include: format (markdown, JSON, code), length bounds, sections/headers if applicable, delimiters.]

## Verification
[How to check success — specific criteria that make the E-principle concrete. Think: "I'll know this worked when..."]


Optional sections (include when they add value):

Examples — When output quality depends on seeing patterns (2-3 examples: basic + edge case)
Input — When the prompt processes structured data (describe format, required fields)
Chain — When the task was split, show how prompts connect
Step 4: Verify with KERNEL Checklist

Before delivering, run this self-review:

 K: Can I describe this prompt's goal in one sentence?
 E: At least 2 measurable success criteria?
 R: No temporal references, no version-ambiguous terms?
 N: Exactly one deliverable per prompt?
 E: At least 2 explicit "do NOT" constraints?
 L: Follows Context → Task → Constraints → Format structure?
 No vague virtue words ("good", "helpful", "detailed") without concrete definition
 No contradictions (e.g., "be concise" + "cover everything")
 All implicit assumptions made explicit
Step 5: Deliver and Iterate

Present the prompt in a clean code block. If the original request was complex and got split:

Show each prompt in the chain, numbered
Explain how outputs feed into subsequent prompts
Suggest which prompts can run in parallel vs sequential

Always offer: "Want me to adjust the constraints, add examples, or split this differently?"

Prompt Chaining

When a task is too complex for one prompt (fails N-principle), decompose into a chain. Each link:

Has a single clear goal (passes all KERNEL checks independently)
Produces output that feeds cleanly into the next prompt
Can be verified independently before moving to the next step

Pattern: Task → subtask analysis → ordered chain with data flow

Example: "Build a REST API" →

Design data models (output: schema)
Generate endpoint specifications (input: schema → output: OpenAPI spec)
Implement endpoints (input: OpenAPI spec → output: code)
Write tests (input: code + spec → output: test suite)
Failure Modes

Các lỗi phổ biến cần nhận diện và tránh khi generate prompt:

Failure mode	Dấu hiệu	Sửa
Prompt quá chung	Không constraint, output có thể là bất kỳ thứ gì	Thêm scope, format, length bounds
Over-engineering	Prompt dài hơn output mong đợi, quá nhiều rules	Cắt constraints không ảnh hưởng output quality
Constraint mâu thuẫn	"Be concise" + "Cover everything thoroughly"	Chọn 1, bỏ kia, hoặc chia scope
Vague virtue stacking	"Good", "helpful", "engaging", "detailed" liên tiếp	Thay bằng criteria cụ thể, đo được
Temporal drift	"Current", "latest", "recent" không pin version	Pin version/date cụ thể
Missing audience	Prompt không nói cho ai → tone/depth không phù hợp	Thêm audience + expertise level
Format ambiguity	Không nói rõ output format → AI tự chọn	Thêm Output Format section tường minh
Weekly Installs
11
Repository
hoangvantuan/cl…e-plugin
First Seen
Mar 26, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass