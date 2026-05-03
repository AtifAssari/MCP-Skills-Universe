---
title: prompt engineer
url: https://skills.sh/jmsktm/claude-settings/prompt-engineer
---

# prompt engineer

skills/jmsktm/claude-settings/Prompt Engineer
Prompt Engineer
Installation
$ npx skills add https://github.com/jmsktm/claude-settings --skill 'Prompt Engineer'
SKILL.md
Prompt Engineer

The Prompt Engineer skill helps you craft, refine, and optimize prompts for Claude Code and other AI systems. It applies proven prompt engineering principles including clarity, specificity, context provision, and structural best practices to transform vague requests into effective AI instructions.

This skill analyzes existing prompts for weaknesses, suggests improvements based on prompt engineering research, and helps you build prompt libraries for recurring tasks. It's particularly valuable when you need consistent, high-quality AI outputs or want to maximize the effectiveness of complex multi-step AI workflows.

Whether you're creating one-off prompts or building reusable templates, this skill ensures your AI interactions are clear, actionable, and produce the results you need.

Core Workflows
Workflow 1: Analyze & Optimize Existing Prompt
Receive the current prompt from user
Analyze against prompt engineering principles:
Clarity: Is the request unambiguous?
Specificity: Are outputs well-defined?
Context: Is necessary background provided?
Structure: Is the prompt well-organized?
Constraints: Are limitations clearly stated?
Identify weaknesses and improvement opportunities
Provide optimized version with explanations
Test improved prompt if requested
Iterate based on results
Workflow 2: Design New Prompt from Scratch
Clarify the goal: What outcome is needed?
Gather requirements:
Target AI system capabilities
Output format requirements
Domain context needed
Edge cases to handle
Structure the prompt using proven patterns:
Role/persona if beneficial
Clear task description
Specific constraints and requirements
Output format specification
Examples if complex
Draft initial version
Refine for clarity and completeness
Document usage guidelines
Workflow 3: Build Prompt Template Library
Identify recurring prompt patterns in workflow
Extract reusable components
Parameterize variable elements
Document template with:
Purpose and use cases
Parameter descriptions
Example usage
Expected outputs
Test template with multiple scenarios
Store in organized library structure
Quick Reference
Action	Command/Trigger
Optimize existing prompt	"Optimize this prompt: [prompt]"
Design new prompt	"Design a prompt for [goal]"
Review prompt quality	"Review this prompt: [prompt]"
Create template	"Create a prompt template for [use case]"
Apply best practices	"Apply prompt engineering best practices to [prompt]"
Fix prompt issues	"This prompt isn't working well: [prompt]"
Best Practices

Be Specific: Replace vague terms with concrete requirements

Bad: "Make it better"
Good: "Increase response accuracy by providing 3 cited examples"

Provide Context: Give AI the background it needs

Include: Domain knowledge, target audience, constraints
Example: "For a technical audience familiar with React..."

Structure Clearly: Use formatting to organize complex prompts

Sections, bullets, numbered steps
Clear delineation between instructions and examples

Define Success: Specify what good output looks like

Format requirements (JSON, markdown, etc.)
Length constraints
Quality criteria

Use Examples: Show don't just tell for complex outputs

Provide 1-3 examples of desired output
Include edge cases if relevant

Iterate: Prompts improve through testing

Start simple, add complexity as needed
Test with edge cases
Refine based on actual outputs

Separate Concerns: Don't mix multiple requests

One clear goal per prompt
Chain prompts for multi-step workflows

Constrain Appropriately: Set boundaries without over-constraining

Specify limits (word count, format)
Allow flexibility where creativity helps
Advanced Techniques
Chain-of-Thought Prompting

Encourage step-by-step reasoning by asking AI to "think through" problems:

Before providing the final answer, work through:
1. What are the key factors?
2. What are the trade-offs?
3. What does the evidence suggest?
Then provide your conclusion.

Few-Shot Learning

Provide examples of input-output pairs:

Example 1: [input] → [output]
Example 2: [input] → [output]
Now apply the same pattern to: [new input]

Role-Based Prompting

Assign expertise or perspective:

As a senior React architect with 10 years of experience,
review this component for performance issues...

Constraint-Based Refinement

Use specific constraints to shape output:

Requirements:
- Maximum 3 paragraphs
- Include code examples
- Cite sources
- Use beginner-friendly language

Common Pitfalls to Avoid
Assuming context the AI doesn't have
Being too vague about desired output format
Mixing multiple unrelated requests
Over-complicating simple requests
Not specifying constraints until after receiving output
Forgetting to provide examples for complex patterns
Using ambiguous language or jargon without definition
Weekly Installs
–
Repository
jmsktm/claude-settings
GitHub Stars
3
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass