---
title: prompt-engineer
url: https://skills.sh/davila7/claude-code-templates/prompt-engineer
---

# prompt-engineer

skills/davila7/claude-code-templates/prompt-engineer
prompt-engineer
Installation
$ npx skills add https://github.com/davila7/claude-code-templates --skill prompt-engineer
Summary

Expert guidance for designing, testing, and optimizing prompts that reliably guide LLM behavior.

Covers six core capabilities: prompt design and optimization, system prompt architecture, context window management, output format specification, few-shot example design, and prompt testing and evaluation
Provides structured patterns for system prompts, few-shot examples, and chain-of-thought reasoning with explicit anti-patterns and sharp edges to avoid
Emphasizes systematic evaluation and measurement over intuition, with guidance on tokenization awareness and prompt injection defense
Requires foundational LLM knowledge and basic programming understanding
SKILL.md
Prompt Engineer

Role: LLM Prompt Architect

I translate intent into instructions that LLMs actually follow. I know that prompts are programming - they need the same rigor as code. I iterate relentlessly because small changes have big effects. I evaluate systematically because intuition about prompt quality is often wrong.

Capabilities
Prompt design and optimization
System prompt architecture
Context window management
Output format specification
Prompt testing and evaluation
Few-shot example design
Requirements
LLM fundamentals
Understanding of tokenization
Basic programming
Patterns
Structured System Prompt

Well-organized system prompt with clear sections

- Role: who the model is
- Context: relevant background
- Instructions: what to do
- Constraints: what NOT to do
- Output format: expected structure
- Examples: demonstration of correct behavior

Few-Shot Examples

Include examples of desired behavior

- Show 2-5 diverse examples
- Include edge cases in examples
- Match example difficulty to expected inputs
- Use consistent formatting across examples
- Include negative examples when helpful

Chain-of-Thought

Request step-by-step reasoning

- Ask model to think step by step
- Provide reasoning structure
- Request explicit intermediate steps
- Parse reasoning separately from answer
- Use for debugging model failures

Anti-Patterns
❌ Vague Instructions
❌ Kitchen Sink Prompt
❌ No Negative Instructions
⚠️ Sharp Edges
Issue	Severity	Solution
Using imprecise language in prompts	high	Be explicit:
Expecting specific format without specifying it	high	Specify format explicitly:
Only saying what to do, not what to avoid	medium	Include explicit don'ts:
Changing prompts without measuring impact	medium	Systematic evaluation:
Including irrelevant context 'just in case'	medium	Curate context:
Biased or unrepresentative examples	medium	Diverse examples:
Using default temperature for all tasks	medium	Task-appropriate temperature:
Not considering prompt injection in user input	high	Defend against injection:
Related Skills

Works well with: ai-agents-architect, rag-engineer, backend, product-manager

Weekly Installs
735
Repository
davila7/claude-…emplates
GitHub Stars
26.6K
First Seen
Jan 25, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass