---
title: context manager
url: https://skills.sh/eddiebe147/claude-settings/context-manager
---

# context manager

skills/eddiebe147/claude-settings/Context Manager
Context Manager
Installation
$ npx skills add https://github.com/eddiebe147/claude-settings --skill 'Context Manager'
SKILL.md
Context Manager

The Context Manager skill helps you optimize conversation context to maintain Claude's effectiveness throughout long sessions. It tracks context window usage, identifies when to summarize or prune context, and helps you structure conversations to keep relevant information accessible while staying within token limits.

This skill is essential for complex, multi-day projects where conversation history grows large. It helps you decide what to preserve, what to summarize, and what to discard, ensuring Claude maintains awareness of important decisions and project state without hitting context limits.

Use this skill proactively during long development sessions, before starting new major features, or when you notice performance degradation due to context bloat.

Core Workflows
Workflow 1: Monitor Context Health
Check current context usage:
Token count
Percentage of limit
Recent growth rate
Analyze context composition:
How much is code?
How much is conversation?
How much is documentation?
Identify problematic areas:
Redundant information
Outdated references
Irrelevant tangents
Assess risk level:
Green: <50% usage, healthy
Yellow: 50-75% usage, monitor
Red: >75% usage, take action
Recommend actions if needed
Report status to user
Workflow 2: Summarize Long Conversation
Review conversation history
Extract key information:
Decisions made
Problems solved
Current project state
Open questions
Next steps
Organize by topic/timeline
Create concise summary
Validate with user
Suggest starting new thread with summary
Workflow 3: Prune Irrelevant Context
Identify candidates for removal:
Resolved issues
Abandoned approaches
Temporary debugging
Superseded information
Categorize by importance:
Safe to remove
Could summarize
Must preserve
Propose pruning plan to user
Execute approved removals
Preserve critical context
Verify coherence after pruning
Workflow 4: Optimize Context Structure
Analyze current context organization
Identify inefficiencies:
Information scattered across conversation
Redundant explanations
Lack of structure
Restructure for efficiency:
Group related information
Create reference sections
Use concise formats
Suggest external documentation for:
Architecture decisions
API specifications
Configuration details
Link to external docs instead of inlining
Validate improved efficiency
Quick Reference
Action	Command/Trigger
Check context status	"Check context window" or "How's our context?"
Summarize conversation	"Summarize this conversation"
Start fresh with summary	"Start new thread with summary"
Prune old context	"Clear old context" or "Prune conversation"
Optimize context structure	"Optimize our context"
Preserve key decisions	"Document key decisions"
Estimate context usage	"How much context are we using?"
Best Practices

Monitor Proactively: Don't wait for performance issues

Check context before starting major features
Monitor after long debugging sessions
Review weekly on long-running projects

Summarize Regularly: Compress history at natural breakpoints

End of feature development
After resolving major issues
Before switching contexts (dev → deployment)

Externalize Static Info: Move unchanging content to files

Architecture docs
API specifications
Code style guides
Reference materials

Use Structured Formats: Make information dense and scannable

Tables instead of prose
Bullet points instead of paragraphs
Code blocks instead of descriptions

Preserve Decisions: Always keep the "why"

Why this approach was chosen
Why alternatives were rejected
What constraints influenced decisions

Discard Aggressively: Be ruthless with temporary content

Debugging exploration
Failed experiments
Resolved issues
Superseded plans

Start Fresh Strategically: Know when to begin new conversation

After major milestones
When switching to unrelated work
When context is >75% full
When performance degrades

Document Externally: Use files for persistent knowledge

PIPELINE_STATUS.md for project state
DECISIONS.md for architecture choices
TODO.md for task lists
README.md for onboarding
Context Optimization Strategies
Strategy 1: Hierarchical Summarization
Long conversation →
  Detailed summary (50% reduction) →
    Executive summary (80% reduction) →
      Key decisions (95% reduction)

Strategy 2: Time-Based Windowing
Keep in context:
- Last 1 hour: Full detail
- Last 4 hours: Summarized
- Last day: Key decisions only
- Older: Link to external docs

Strategy 3: Topic-Based Partitioning
Separate threads for:
- Feature development
- Bug investigation
- Deployment/ops
- Architecture discussion

Link between threads as needed

Strategy 4: Progressive Disclosure
Start with:
- Current task context only

Add on demand:
- Related decisions
- Relevant code
- Background information

Remove when done

Context Health Checklist

Before starting a major task, verify:

 Context usage < 75%
 Recent decisions documented
 Obsolete information removed
 Current project state clear
 Next steps identified
 Relevant files/docs linked
 Debugging traces cleaned up
Warning Signs of Context Issues

Watch for these indicators:

Responses get slower: Processing large context
Information ignored: AI misses recent context
Repetition: AI re-explains known information
Loss of coherence: AI forgets earlier decisions
Token limit warnings: Approaching hard limits
Degraded accuracy: Mistakes in previously solid areas
External Memory Strategies

Move these to files, not context:

Information Type	Best Storage
Project overview	README.md
Architecture decisions	ARCHITECTURE.md or ADRs
API contracts	OpenAPI spec or schema files
Current project state	PIPELINE_STATUS.md or TODO.md
Configuration	.env, config files
Code style rules	.eslintrc, prettier.config.js
Deployment process	DEPLOYMENT.md or CI/CD config
Team decisions	DECISIONS.md or meeting notes
Context Templates
Project State Summary Template
## Project: [Name]
- **Status**: [Current pipeline stage]
- **Current focus**: [What we're working on]
- **Last completed**: [Recent achievement]
- **Next steps**: [Immediate tasks]
- **Blockers**: [What's preventing progress]
- **Key decisions**: [Recent important choices]

Decision Log Template
## Decision: [Topic]
- **Date**: [When]
- **Context**: [Why we needed to decide]
- **Options considered**: [Alternatives]
- **Choice**: [What we decided]
- **Rationale**: [Why this choice]
- **Consequences**: [Trade-offs accepted]

Session Summary Template
## Session Summary: [Date]
- **Duration**: [How long]
- **Accomplished**: [What we built/fixed]
- **Decisions**: [Choices made]
- **Issues found**: [Problems discovered]
- **Next session**: [Where to continue]

Advanced: Context Compression Techniques

For power users:

Use references: Link to code instead of pasting

"See function processData in /src/utils/data.ts"
Instead of: [pasting entire function]

Leverage AI memory: Store in knowledge graph

Key relationships between entities
Project-specific terminology
Team member roles and expertise

Create abbreviations: Define once, use everywhere

"FE" = Frontend, "BE" = Backend
"MR" = Merge Request, "PR" = Pull Request
Project-specific acronyms

Use diff format: Show changes, not entire files

Especially for code reviews
Before/after comparisons

Batch similar information: Group related items

All env vars in one block
All API endpoints in table
All dependencies in list
Weekly Installs
–
Repository
eddiebe147/clau…settings
First Seen
–
Security Audits
Gen Agent Trust HubPass