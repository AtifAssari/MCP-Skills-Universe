---
title: think
url: https://skills.sh/johnlindquist/claude/think
---

# think

skills/johnlindquist/claude/think
think
Installation
$ npx skills add https://github.com/johnlindquist/claude --skill think
SKILL.md
Think - Structured Reasoning

Apply structured thinking frameworks to complex problems.

Prerequisites

Gemini CLI installed:

pip install google-generativeai
export GEMINI_API_KEY=your_api_key

CLI Reference

All commands use Gemini with structured prompts:

gemini -m pro -o text -e "" "Your prompt"

Thinking Operations
Deep Analysis

Multi-framework reasoning on complex problems:

gemini -m pro -o text -e "" "Analyze this problem using multiple thinking frameworks:

PROBLEM: [Your problem]

Apply these frameworks:
1. First Principles - Break down to fundamental truths
2. Systems Thinking - Map components and interactions
3. Inversion - What would make this fail?
4. Second-Order Effects - What happens after the obvious?

For each framework:
- Key insights
- Blind spots it reveals
- Actionable implications

Synthesize into a coherent recommendation."

Quick Think

Fast reasoning on simpler questions:

gemini -m pro -o text -e "" "Think through this question step by step:

[Your question]

Provide:
1. Initial reaction
2. Key considerations
3. Potential pitfalls
4. Recommended approach"

Challenge an Idea

Stress-test a proposal:

gemini -m pro -o text -e "" "Challenge this idea rigorously:

IDEA: [The idea to challenge]
CONTEXT: [Relevant context]

Apply these challenges:
1. Steel man the counterargument
2. Identify hidden assumptions
3. Find edge cases that break it
4. Consider who might disagree and why
5. What evidence would change your mind?

Conclude with: Should we proceed, modify, or abandon?"

Evaluate Options

Compare multiple choices:

gemini -m pro -o text -e "" "Evaluate these options for: [Decision question]

OPTIONS:
1. [Option A]
2. [Option B]
3. [Option C]

CRITERIA:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]

For each option:
- Score against each criterion (1-5)
- Key advantages
- Key risks
- Hidden costs

Provide a clear recommendation with reasoning."

Thinking Frameworks
First Principles
gemini -m pro -o text -e "" "Apply first principles thinking to: [problem]

1. What do we know for certain? (facts, not assumptions)
2. What are we assuming? (challenge each)
3. What's the simplest explanation?
4. Build up from fundamentals"

Pre-Mortem
gemini -m pro -o text -e "" "Conduct a pre-mortem for: [project/decision]

Imagine this has completely failed. Working backward:
1. What went wrong?
2. What warning signs did we ignore?
3. What assumptions proved false?
4. What can we do NOW to prevent this?"

Opportunity Cost
gemini -m pro -o text -e "" "Analyze opportunity costs for: [decision]

If we choose this:
1. What are we NOT doing?
2. What resources are locked up?
3. What options are foreclosed?
4. What's the cost of reversing?"

Second-Order Effects
gemini -m pro -o text -e "" "Explore second-order effects of: [action/decision]

First-order effect: [The obvious outcome]

Now trace the chain:
- What does that cause?
- Who responds and how?
- What unintended consequences emerge?
- What feedback loops are created?"

Use Cases
Architecture Decisions
gemini -m pro -o text -e "" "Evaluate architecture options:

CONTEXT: Building a real-time collaborative editor

OPTIONS:
1. Operational Transform (OT)
2. CRDTs
3. Custom sync engine

CRITERIA:
- Correctness guarantees
- Performance at scale
- Implementation complexity
- Offline support

Provide detailed analysis and recommendation."

Code Design
gemini -m pro -o text -e "" "Think through this design decision:

PROBLEM: Where to put validation logic - in the controller, service, or model?

Consider:
- Separation of concerns
- Testability
- Maintainability
- Real-world examples
- What experienced developers prefer and why"

Debugging Strategy
gemini -m pro -o text -e "" "Help me think through debugging this issue:

SYMPTOM: [What's happening]
CONTEXT: [System description]
TRIED: [What you've already attempted]

1. What does this symptom tell us?
2. What's the most likely root cause?
3. What's the most costly root cause?
4. What's the quickest diagnostic test?
5. In what order should I investigate?"

Best Practices
Be specific - Vague problems get vague analysis
Provide context - Include constraints and requirements
Request structure - Ask for frameworks, criteria, scores
Challenge the output - Use follow-up questions
Capture reasoning - Save good analyses for future reference
Weekly Installs
169
Repository
johnlindquist/claude
GitHub Stars
23
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass