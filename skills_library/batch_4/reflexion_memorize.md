---
title: reflexion:memorize
url: https://skills.sh/neolabhq/context-engineering-kit/reflexion:memorize
---

# reflexion:memorize

skills/neolabhq/context-engineering-kit/reflexion:memorize
reflexion:memorize
Installation
$ npx skills add https://github.com/neolabhq/context-engineering-kit --skill reflexion:memorize
SKILL.md
Memory Consolidation: Curate and Update CLAUDE.md

Output must add precise, actionable bullets that future tasks can immediately apply.

Memory Consolidation Workflow
Phase 1: Context Harvesting

First, gather insights from recent reflection and work:

Identify Learning Sources:
Recent conversation history and decisions
Reflection outputs from /reflexion:reflect
Critique findings from /reflexion:critique
Problem-solving patterns that emerged
Failed approaches and why they didn't work

If scope is unclear, ask: “What output(s) should I memorize? (last message, selection, specific files, critique report, etc.)”

Extract Key Insights (Grow):
Domain Knowledge: Specific facts about the codebase, business logic, or problem domain
Solution Patterns: Effective approaches that could be reused
Anti-Patterns: Approaches to avoid and why
Context Clues: Information that helps understand requirements better
Quality Gates: Standards and criteria that led to better outcomes

Extract only high‑value, generalizable insights:

Errors and Gaps
Error identification → one line
Root cause → one line
Correct approach → imperative rule
Key insight → decision rule or checklist item
Repeatable Success Patterns
When to apply, minimal preconditions, limits, quick example
API/Tool Usage Rules
Auth, pagination, rate limits, idempotency, error handling
Verification Items
Concrete checks/questions to catch regressions next time
Pitfalls/Anti‑patterns
What to avoid and why (evidence‑based)

Prefer specifics over generalities. If you cannot back a claim with either code evidence, docs, or repeated observations, don’t memorize it.

Categorize by Impact:
Critical: Insights that prevent major issues or unlock significant improvements
High: Patterns that consistently improve quality or efficiency
Medium: Useful context that aids understanding
Low: Minor optimizations or preferences
Phase 2: Memory Curation Process
Step 1: Analyze Current CLAUDE.md Context
# Read current context file
@CLAUDE.md


Assess what's already documented:

What domain knowledge exists?
Which patterns are already captured?
Are there conflicting or outdated entries?
What gaps exist that new insights could fill?
Step 2: Curation Rules (Refine)

For each insight identified in Phase 1 apply ACE’s “grow‑and‑refine” principle:

Relevance: Only include items helpful for recurring tasks in this repo/org
Non‑redundancy: Do not duplicate existing bullets; merge or skip if similar
Atomicity: One idea per bullet; short, imperative, self‑contained
Verifiability: Avoid speculative claims; link docs when stating external facts
Safety: No secrets, tokens, internal URLs, or private PII
Stability: Prefer strategies that remain valid over time; call out version‑specifics
Step 3: Apply Curation Transformation

Generation → Curation Mapping:

Raw insight: [What was learned]
Context category: [Where it fits in CLAUDE.md structure]
Actionable format: [How to phrase it for future use]
Validation criteria: [How to know if it's being applied correctly]

Example Transformation:

Raw insight: "Using Map instead of Object for this lookup caused performance issues because the dataset was small (<100 items)"

Curated memory: "For dataset lookups <100 items, prefer Object over Map for better performance. Map is optimal for 10K+ items. Use performance testing to validate choice."

Step 4: Prevent Context Collapse

Ensure new memories don't dilute existing quality context:

Consolidation Check:

Can this insight be merged with existing knowledge?
Does it contradict something already documented?
Is it specific enough to be actionable?

Specificity Preservation:

Keep concrete examples and code snippets
Maintain specific metrics and thresholds where available
Include failure conditions alongside success patterns

Organization Integrity:

Place insights in appropriate sections
Maintain consistent formatting
Update related cross-references

If a potential bullet conflicts with an existing one, prefer the more specific, evidence‑backed rule and mark the older one for future consolidation (but do not auto‑delete).

Phase 3: CLAUDE.md Updates

Update the context file with curated insights:

Where to Write in CLAUDE.md

Create the file if missing with these sections (top‑level headings):

Project Context

Domain Knowledge: Business domain insights
Technical constraints discovered
User behavior patterns

Code Quality Standards

Performance criteria that matter
Security considerations
Maintainability patterns

Architecture Decisions

Patterns that worked well
Integration approaches
Scalability considerations

Testing Strategies

Effective test patterns
Edge cases to always consider
Quality gates that catch issues

Development Guidelines

APIs to Use for Specific Information
Formulas and Calculations
Checklists for Common Tasks
Review criteria that help
Documentation standards
Debugging techniques

Strategies and Hard Rules

Verification Checklist
Patterns and Playbooks
Anti‑patterns and Pitfalls

Place each new bullet under the best‑fit section. Keep bullets concise and actionable.

Memory Update Template

For each significant insight, add structured entries:

## [Domain/Pattern Category]

### [Specific Context or Pattern Name]

**Context**: [When this applies]

**Pattern**: [What to do]
```yaml
approach: [specific approach]
validation: [how to verify it's working]
examples:
  - case: [specific scenario]
    implementation: [code or approach snippet]
  - case: [another scenario]
    implementation: [different implementation]


Avoid: [Anti-patterns or common mistakes]

[mistake 1]: [why it's problematic]
[mistake 2]: [specific issues caused]

Confidence: [High/Medium/Low based on evidence quality]

Source: [reflection/critique/experience date]

Phase 4: Memory Validation
Quality Gates (Must Pass)

After updating CLAUDE.md:

Coherence Check:

Do new entries fit with existing context?
Are there any contradictions introduced?
Is the structure still logical and navigable?

Actionability Test: A developer should be able to use the bullet immediately

Could a future agent use this guidance effectively?
Are examples concrete enough?
Are success/failure criteria clear?

Consolidation Review: No near‑duplicates; consolidate wording if similar exists

Can similar insights be grouped together?
Are there duplicate concepts that should be merged?
Is anything too verbose or too vague?

Scoped: Names technologies, files, or flows when relevant

Evidence‑backed: Derived from reflection/critique/tests or official docs

Memory Quality Indicators

Track the effectiveness of memory updates:

Successful Memory Patterns
Specific Thresholds: "Use pagination for lists >50 items"
Contextual Patterns: "When user mentions performance, always measure first"
Failure Prevention: "Always validate input before database operations"
Domain Language: "In this system, 'customer' means active subscribers only"
Memory Anti-Patterns to Avoid
Vague Guidelines: "Write good code" (not actionable)
Personal Preferences: "I like functional style" (not universal)
Outdated Context: "Use jQuery for DOM manipulation" (may be obsolete)
Over-Generalization: "Always use microservices" (ignores context)
Implementation Notes
Incremental Updates: Add insights gradually rather than massive rewrites
Evidence-Based: Only memorize patterns with clear supporting evidence
Context-Aware: Consider project phase, team size, constraints when curating
Version Awareness: Note when insights become obsolete due to tech changes
Cross-Reference: Link related concepts within CLAUDE.md for better navigation
Expected Outcomes

After effective memory consolidation:

Faster Problem Recognition: Agent quickly identifies similar patterns
Better Solution Quality: Leverages proven approaches from past success
Fewer Repeated Mistakes: Avoids anti-patterns that caused issues before
Domain Fluency: Uses correct terminology and understands business context
Quality Consistency: Applies learned quality standards automatically
Usage
# Memorize from most recent reflections and outputs
/reflexion:memorize

# Dry‑run: show proposed bullets without writing to CLAUDE.md
/reflexion:memorize --dry-run

# Limit number of bullets
/reflexion:memorize --max=5

# Target a specific section
/reflexion:memorize --section="Verification Checklist"

# Choose source
/reflexion:memorize --source=last|selection|chat:<id>

Output
Short summary of additions (counts by section)
Confirmation that CLAUDE.md was created/updated
Notes
This command is the counterpart to /reflexion:reflect: reflect → curate → memorize.
The design follows ACE to avoid brevity bias and context collapse by accumulating granular, organized knowledge over time (https://arxiv.org/pdf/2510.04618).
Do not overwrite or compress existing context; only add high‑signal bullets.

Remember: The goal is not to memorize everything, but to curate high-impact insights that consistently improve future agent performance. Quality over quantity - each memory should make future work measurably better.

Weekly Installs
470
Repository
neolabhq/contex…ring-kit
GitHub Stars
942
First Seen
Feb 23, 2026