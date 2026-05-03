---
title: prompting
url: https://skills.sh/diskd-ai/prompting/prompting
---

# prompting

skills/diskd-ai/prompting/prompting
prompting
Installation
$ npx skills add https://github.com/diskd-ai/prompting --skill prompting
SKILL.md
Prompt Engineering

Guide for crafting effective prompts for large language models (Claude, GPT, Gemini, Llama, etc.).

Workflow
Clarify the goal: What task should the prompt accomplish?
Choose techniques: Select from references/techniques.md
Structure the prompt: Apply appropriate format
Add constraints: Specify requirements and boundaries
Test and refine: Iterate based on outputs
Writing a New Prompt

Start with this template:

[Context/Role - optional]
[Task - required]
[Constraints/Requirements - as needed]
[Output format - as needed]
[Examples - for complex tasks]


Minimal prompt (simple tasks):

Summarize this article in 3 bullet points.


Structured prompt (complex tasks):

You are a senior code reviewer.

Review this code for:
- Security vulnerabilities
- Performance issues
- Maintainability concerns

Format your response as:
## Summary
[1-2 sentences]

## Issues
- [severity]: [description]

## Recommendations
[prioritized list]

Improving an Existing Prompt

Diagnose issues:

Problem	Solution
Output too vague	Add specific constraints or examples
Wrong format	Specify output structure explicitly
Missing details	Use chain-of-thought or decomposition
Inconsistent results	Add few-shot examples
Off-topic responses	Strengthen role/context framing

Improvement checklist:

Is the task clear and unambiguous?
Are constraints specific (not "be concise" but "under 100 words")?
Does output format match intended use?
Would examples clarify expectations?
Quick Reference: Techniques
Technique	When to Use
Few-shot	Specific format/style needed
Chain-of-thought	Complex reasoning, math, analysis
Role prompting	Domain expertise, specific tone
Task decomposition	Multi-step workflows
Constraints	Precise requirements

See references/techniques.md for detailed patterns and examples.

Quick Reference: Output Formats
Format	When to Use
XML tags	Complex prompts, clear section boundaries
JSON	Programmatic parsing, structured data
Markdown	Human-readable reports, documentation

See references/structured.md for format patterns.

System Prompts

For designing AI assistant behavior, see references/system-prompts.md.

Key sections:

Identity and role definition
Behavioral guidelines
Constraints and boundaries
Output format defaults
Weekly Installs
66
Repository
diskd-ai/prompting
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass