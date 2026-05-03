---
rating: ⭐⭐⭐
title: research-strategy
url: https://skills.sh/autumnsgrove/groveengine/research-strategy
---

# research-strategy

skills/autumnsgrove/groveengine/research-strategy
research-strategy
Installation
$ npx skills add https://github.com/autumnsgrove/groveengine --skill research-strategy
SKILL.md
Research Strategy Skill
When to Activate

Activate this skill when:

Researching technology options
Evaluating libraries or frameworks
Investigating best practices
Analyzing security concerns
Making architectural decisions
Performing codebase analysis
Core Principles
Research and report, don't implement
Multiple sources beat single sources
Document confidence levels for all findings
Acknowledge knowledge gaps openly
Present alternatives objectively
7-Step Research Methodology
Define Research Questions - What exactly needs answering?
Identify Information Sources - Where to look?
Gather Raw Information - Collect systematically
Cross-Reference Findings - Verify across sources
Validate Accuracy - Check dates, authority, consensus
Identify Gaps - What's still unknown?
Synthesize Insights - Connect into actionable knowledge
Source Prioritization

Primary Sources (Highest priority)

Official documentation
Technical specifications
API references

Authoritative Sources

Well-maintained libraries
Industry standards (OWASP, NIST)
Academic papers

Community Sources

Stack Overflow discussions
GitHub issues/PRs
Technical blogs

Experimental Sources (Use with caution)

Beta features
Draft proposals
Confidence Scoring

Assign to ALL findings:

Level	Range	Criteria
HIGH	90-100%	Multiple authoritative sources agree, widely adopted
MEDIUM	60-89%	Good documentation, some adoption, minor disagreements
LOW	30-59%	Limited sources, conflicting information
SPECULATIVE	<30%	Educated guess, no direct sources
Research Report Structure
# Research Report: [Topic]

## Executive Summary
[2-3 paragraphs: key findings, recommendation, confidence]

## Research Questions
1. [Question 1]
2. [Question 2]

## Key Findings

### Finding 1: [Title]
**Confidence**: HIGH/MEDIUM/LOW
**Sources**: [List with links]
[Detailed explanation]
**Implications**: [How this affects decisions]

## Comparative Analysis

| Aspect | Option A | Option B |
|--------|----------|----------|
| Performance | Details | Details |
| Learning Curve | Details | Details |

## Best Practices
1. **[Practice]**: Why, Source, Adoption level

## Risks and Concerns
- **Risk**: Severity, Likelihood, Mitigation

## Knowledge Gaps
- **Gap**: Impact, How to address

## Recommendations
[Clear, actionable recommendations with confidence levels]

Library/Framework Research Template
## Overview
- Purpose: [One sentence]
- Maturity: Stable/Beta/Experimental
- Last commit: [Date]
- License: [Type]

## Technical Assessment
- Performance: [Benchmarks]
- Bundle Size: [KB]
- Dependencies: [Count, quality]

## Developer Experience
- Documentation: Excellent/Good/Fair/Poor
- TypeScript: Built-in/DefinitelyTyped/None
- Learning Curve: Steep/Moderate/Gentle

## Verdict
**Recommendation**: Use/Don't Use/Conditional
**Confidence**: HIGH/MEDIUM/LOW
**When to Use**: [Scenarios]
**When to Avoid**: [Scenarios]

Analysis Framework

For each topic, answer:

Current State

What exists today?
What patterns are established?

Best Practices

What do experts recommend?
What anti-patterns to avoid?

Trade-offs

What are alternatives?
Pros/cons of each option?

Risks

What could go wrong?
Common pitfalls?
Anti-Patterns to Avoid

❌ Single Source Syndrome

"According to this one article..."
✅ "Multiple sources agree (A, B, C)..."

❌ Premature Implementation

"Here's the code..."
✅ "Implementation would follow this approach..."

❌ Missing Confidence Levels

"This is the way."
✅ "HIGH confidence: Recommended by [sources]..."

❌ Outdated Information

Using 2020 practices without checking updates
✅ Verify current practices, note recent changes
Research Quality Checklist
Completeness
 All questions answered
 Multiple sources consulted (minimum 2-3)
 Advantages AND disadvantages investigated
 Edge cases considered
Accuracy
 Sources are authoritative and current
 Publication dates checked
 Conflicting info acknowledged
 Assumptions stated
Actionability
 Findings translate to next steps
 Risks quantified
 Alternatives provided
 Decision criteria clear
Related Resources

See AgentUsage/research_workflow.md for complete documentation including:

Security research template
Detailed report examples
Research mission template
Quality checklists
Weekly Installs
74
Repository
autumnsgrove/groveengine
GitHub Stars
5
First Seen
Today
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykWarn