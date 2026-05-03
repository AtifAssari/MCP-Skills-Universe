---
title: antivibe
url: https://skills.sh/mohi-devhub/antivibe/antivibe
---

# antivibe

skills/mohi-devhub/antivibe/antivibe
antivibe
Installation
$ npx skills add https://github.com/mohi-devhub/antivibe --skill antivibe
SKILL.md
AntiVibe - AI Code Learning Framework
Purpose

AntiVibe generates learning-focused explanations of AI-written code. Not generic summaries - actual educational content that helps developers understand:

What the code does (functionality)
Why it was written this way (design decisions)
When to use these patterns (context)
What alternatives exist (broader knowledge)
When to Use

Use AntiVibe when:

Manual invocation: User types /antivibe or "deep dive"
Post-task learning: After a feature/phase completes, user wants to learn from it
Proactive: User says "explain what AI wrote", "learn from this code", or "understand what AI wrote"
What AntiVibe Produces

Output saved to deep-dive/ folder as markdown:

deep-dive/
├── auth-system-2026-01-15.md
├── api-layer-2026-01-15.md
└── database-models-2026-01-15.md


Each file contains:

Overview: What this code does and why it exists
Code Walkthrough: File-by-file explanation with line-by-line notes
Concepts Explained: Design patterns, algorithms, CS concepts used
Learning Resources: Curated docs, tutorials, videos
Related Code: Links to other files in the codebase
Workflow
Step 1: Identify Code to Analyze
Check for explicit file list in user request
Or use git diff to find recently modified/created files
Or ask user which files/components they want to understand
Step 2: Analyze Code Structure

For each file:

Identify main purpose and responsibilities
Note key functions, classes, modules
Identify design patterns used (factory, singleton, observer, etc.)
Find any complex logic or algorithms
Step 3: Explain Concepts

For each concept/pattern found:

What: Plain-language explanation
Why: Why this approach was chosen over alternatives
When: When to use this pattern (with context)
Alternatives: Other approaches and trade-offs
Step 4: Find External Resources

Search for and include:

Official documentation for libraries/frameworks used
Quality tutorials or blog posts
Video resources (if available)
Related concepts for further learning
Step 5: Generate Output

Create markdown file in deep-dive/ folder:

Name format: [component]-[timestamp].md
Follow the template in templates/deep-dive.md
Include code snippets where helpful
Make it educational, not just descriptive
Configuration

AntiVibe can be configured to auto-trigger via hooks:

SubagentStop: After a Task completes a feature
Stop: At session end

To enable auto-trigger, configure hooks in your project (see hooks/hooks.json).

Principles
Why over what - Always explain design decisions
Context matters - Explain when/why to use patterns
Curated resources - Quality links, not random Google results
Phase-aware - Group by implementation phase
Learning path - Suggest next steps for deeper study
Concept mapping - Connect code to underlying CS concepts
Dependencies

Optional scripts in scripts/ folder:

capture-phase.sh - Detect implementation phase boundaries
analyze-code.sh - Parse code structure
find-resources.sh - Search for external resources
generate-deep-dive.sh - Create markdown output

These are helpers - you can also do everything via direct code analysis.

Examples

Input: "Explain the auth system Claude wrote" Output: deep-dive/auth-system-2026-01-15.md containing:

JWT structure explanation
Password hashing rationale
Session management concepts
Learning resources for auth patterns

Input: "I want to understand this API layer" Output: deep-dive/api-layer-2026-01-15.md containing:

REST design decisions
Middleware explanation
Error handling patterns
Further reading on API design
Weekly Installs
9
Repository
mohi-devhub/antivibe
GitHub Stars
633
First Seen
3 days ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass