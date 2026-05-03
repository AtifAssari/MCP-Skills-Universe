---
title: summarization
url: https://skills.sh/jwynia/agent-skills/summarization
---

# summarization

skills/jwynia/agent-skills/summarization
summarization
Installation
$ npx skills add https://github.com/jwynia/agent-skills --skill summarization
SKILL.md
Summarization
Purpose

Create effective summaries by matching summarization type to purpose, audience, and context. "Summarize" can mean many different things—this skill helps identify and execute the right approach.

Core Principle

Summarization is translation, not just reduction. Different purposes require different summary types. Clarify the need before condensing.

Clarifying Questions

Before summarizing, consider:

Purpose: What will this summary be used for?

Decision-making
Background information
Further research
Quick understanding
Reference/recall

Audience: Who will read it?

Technical experts
General audience
Decision makers
Familiar/unfamiliar with topic

Scope: How comprehensive?

Ultra-brief (single sentence)
Brief (paragraph)
Moderate (page)
Extended (multiple pages)

Emphasis: What aspects are most important?

Methodology
Findings/results
Arguments/claims
Context/background
Implications/applications

Format: What structure?

Narrative text
Bullet points
Hierarchical outline
Visual representation
Summary Type Taxonomy
Information Reduction Approaches
Type	What It Is	When to Use
Key Point Extraction	Isolating the most important claims	Original has discrete important points
Abstraction	Higher-level statements covering multiple details	Patterns matter more than specifics
Gisting	Capturing essential meaning, discarding details	Only core message matters
Compression	Shortening while preserving information	Comprehensive coverage needed in less space
Structural Approaches
Type	What It Is	When to Use
Executive Summary	Business-focused: decisions, recommendations, outcomes	Documents requiring action
Abstract/Précis	Academic: methodology and findings	Research papers, technical documents
TLDR	Ultra-brief main takeaway	Casual communication, extreme brevity
Outline	Hierarchical structure of main/supporting points	Logical structure matters
Purpose-Oriented Approaches
Type	What It Is	When to Use
Synthesis	Combining multiple sources coherently	Summarizing across documents
Critical Summary	Evaluating claims while condensing	Assessment of quality needed
Contextual Summary	Framing within broader knowledge	Understanding bigger picture matters
Actionable Summary	Focusing on implications and next steps	Summary will drive action
Execution by Type
Key Point Extraction
Scan for topic sentences and conclusions
Identify explicitly stated main ideas
List each distinct point
Preserve original phrasing where powerful

Example: "The author makes three main arguments: (1)..., (2)..., (3)..."

Abstraction
Group related details
Find common themes or patterns
Create higher-level statements
Reduce specifics to principles

Example: "Multiple studies consistently show..." instead of listing 12 studies

Gisting
Ask: "What is the one thing to remember?"
Distill to core insight
Remove all supporting detail
Verify essence is preserved

Example: "Remote work increases productivity for most knowledge workers."

Executive Summary
State the problem/opportunity
Present the solution/recommendation
Highlight key benefits
Note costs/risks
Specify required actions
Synthesis
Read all sources
Identify common themes
Note contradictions
Find complementary information
Create unified narrative

Example: "Across the five reports, three key trends emerge..."

Critical Summary
Summarize the claims
Evaluate the evidence
Assess methodology
Note limitations
Conclude with assessment

Example: "While the author claims X, the evidence is limited by..."

Format Variations
Quotation-Based
Use key phrases verbatim
When precise wording is important
Select and organize most important quotes
Bullet Points
Break continuous text into discrete units
When quick scanning is valued
Make each point standalone
Progressive Summary
Start ultra-brief
Add layers of detail
Let reader choose depth
Comparative Summary
Side-by-side analysis
Highlight similarities and differences
When contrasting sources
Quality Checklist
 Purpose is clear
 Audience is considered
 Scope is appropriate
 Emphasis matches needs
 Format serves purpose
 Core message is preserved
 Reduction is proportional
 No invented information
 Attribution where needed
Anti-Patterns
The Information Dump

Problem: Reduces length but not complexity Fix: Focus on what matters, not just what's short

The Distortion

Problem: Changes meaning through compression Fix: Verify summary against original claims

The One-Size-Fits-All

Problem: Same approach for all requests Fix: Match type to purpose and audience

The Over-Abstraction

Problem: Loses all useful specifics Fix: Preserve concrete details that support understanding

Integration Points

Inbound:

When asked to summarize any content
When processing long documents
When creating documentation

Outbound:

To decision-making processes
To knowledge management systems
To communication outputs

Complementary:

speech-adaptation: For spoken summaries
voice-analysis: For maintaining voice in summaries
Weekly Installs
528
Repository
jwynia/agent-skills
GitHub Stars
69
First Seen
Jan 20, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass