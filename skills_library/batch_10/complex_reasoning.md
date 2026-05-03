---
title: complex-reasoning
url: https://skills.sh/lobbi-docs/claude/complex-reasoning
---

# complex-reasoning

skills/lobbi-docs/claude/complex-reasoning
complex-reasoning
Installation
$ npx skills add https://github.com/lobbi-docs/claude --skill complex-reasoning
SKILL.md
Complex Reasoning Skill

Structured reasoning frameworks for systematic problem solving, leveraging extended thinking capabilities for deep analysis.

When to Use
Debugging complex issues with multiple potential causes
Architecture decisions requiring trade-off analysis
Root cause analysis for production incidents
Performance optimization with multiple variables
Security vulnerability assessment
Code refactoring with many dependencies
Reasoning Frameworks
Chain-of-Thought (CoT)

Linear step-by-step reasoning for sequential problems.

## Chain-of-Thought Analysis

**Problem**: [State the problem clearly]

**Step 1: Understand the Context**
- What do we know?
- What are the constraints?
- What is the expected outcome?

**Step 2: Identify Key Components**
- Component A: [description]
- Component B: [description]
- Interactions: [how they relate]

**Step 3: Analyze Each Component**
- Component A analysis...
- Component B analysis...

**Step 4: Synthesize Findings**
- Key insight 1
- Key insight 2

**Step 5: Formulate Solution**
- Recommended approach
- Rationale
- Trade-offs

**Conclusion**: [Final recommendation with confidence level]

Tree-of-Thought (ToT)

Branching exploration for problems with multiple solution paths.

## Tree-of-Thought Exploration

**Root Problem**: [Problem statement]

### Branch 1: Approach A
├── Pros: [List advantages]
├── Cons: [List disadvantages]
├── Feasibility: [High/Medium/Low]
├── Sub-branch 1.1: [Variation]
│   └── Outcome: [Expected result]
└── Sub-branch 1.2: [Variation]
    └── Outcome: [Expected result]

### Branch 2: Approach B
├── Pros: [List advantages]
├── Cons: [List disadvantages]
├── Feasibility: [High/Medium/Low]
└── Sub-branches: [...]

### Branch 3: Approach C
├── Pros: [...]
├── Cons: [...]
└── Feasibility: [...]

### Evaluation Matrix
| Approach | Feasibility | Impact | Risk | Score |
|----------|-------------|--------|------|-------|
| A        | High        | Medium | Low  | 8/10  |
| B        | Medium      | High   | Med  | 7/10  |
| C        | Low         | High   | High | 5/10  |

**Selected Path**: Branch [X] because [reasoning]

MECE Framework

Mutually Exclusive, Collectively Exhaustive analysis.

## MECE Analysis

**Problem Space**: [Define the complete problem]

### Category 1: [Mutually exclusive category]
- Sub-element 1.1
- Sub-element 1.2
- Sub-element 1.3

### Category 2: [Mutually exclusive category]
- Sub-element 2.1
- Sub-element 2.2

### Category 3: [Mutually exclusive category]
- Sub-element 3.1
- Sub-element 3.2
- Sub-element 3.3

**Completeness Check**:
- [ ] Categories are mutually exclusive (no overlap)
- [ ] Categories are collectively exhaustive (cover all cases)
- [ ] Each sub-element belongs to exactly one category

**Priority Matrix**:
| Category | Urgency | Impact | Action |
|----------|---------|--------|--------|
| 1        | High    | High   | Now    |
| 2        | Medium  | High   | Next   |
| 3        | Low     | Medium | Later  |

Hypothesis-Driven Debugging

Systematic approach to debugging complex issues.

## Hypothesis-Driven Debug Session

**Symptom**: [Observed behavior]
**Expected**: [What should happen]
**Environment**: [Relevant context]

### Hypothesis 1: [Most likely cause]
**Evidence For**:
- [Supporting observation 1]
- [Supporting observation 2]

**Evidence Against**:
- [Contradicting observation]

**Test**: [How to validate]
**Result**: [Confirmed/Refuted]

### Hypothesis 2: [Second most likely]
**Evidence For**:
- [...]

**Evidence Against**:
- [...]

**Test**: [...]
**Result**: [...]

### Root Cause Identified
**Cause**: [Confirmed root cause]
**Evidence Chain**: [How we proved it]
**Fix**: [Remediation steps]
**Prevention**: [How to prevent recurrence]

Code Analysis Patterns
Dependency Analysis
## Dependency Analysis: [Component Name]

### Direct Dependencies
| Dependency | Version | Purpose | Risk Level |
|------------|---------|---------|------------|
| dep-a      | 2.3.1   | Auth    | Low        |
| dep-b      | 1.0.0   | Data    | Medium     |

### Transitive Dependencies
- Total: [N] packages
- Security vulnerabilities: [N]
- Outdated: [N]

### Dependency Graph


[component] ├── dep-a │ ├── sub-dep-1 │ └── sub-dep-2 └── dep-b └── sub-dep-3


### Risk Assessment
1. **High Risk**: [Dependencies with known issues]
2. **Medium Risk**: [Outdated or unmaintained]
3. **Low Risk**: [Stable, well-maintained]

### Recommendations
1. [Action item 1]
2. [Action item 2]

Impact Analysis
## Impact Analysis: [Proposed Change]

### Affected Components
| Component | Impact Type | Severity | Test Required |
|-----------|-------------|----------|---------------|
| Service A | Direct      | High     | Yes           |
| Service B | Indirect    | Medium   | Yes           |
| Client C  | Downstream  | Low      | Optional      |

### Risk Assessment
- **Breaking Changes**: [List any]
- **Performance Impact**: [Expected effect]
- **Data Migration**: [Required/Not required]

### Rollback Plan
1. [Step 1]
2. [Step 2]
3. [Verification]

### Recommendation
[Go/No-Go with reasoning]

Integration with Extended Thinking

When using these frameworks with extended thinking:

# Enable extended thinking for complex reasoning
response = client.messages.create(
    model="claude-opus-4-5-20250514",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 15000  # Higher budget for complex reasoning
    },
    system="""You are a systematic problem solver. Use structured
    reasoning frameworks like Chain-of-Thought, Tree-of-Thought,
    or MECE analysis as appropriate for the problem.""",
    messages=[{
        "role": "user",
        "content": "Analyze this architecture decision using ToT..."
    }]
)

Best Practices
Choose the right framework: CoT for linear problems, ToT for branching decisions
Document your reasoning: Makes it reviewable and repeatable
Validate assumptions: Each step should build on verified facts
Consider alternatives: Always explore at least 2-3 approaches
Quantify when possible: Use metrics to compare options
Time-box exploration: Set limits on analysis depth
See Also
[[extended-thinking]] - Enable deep reasoning capabilities
[[deep-analysis]] - Analytical templates
[[debugging]] - General debugging patterns
[[testing]] - Validation strategies
Weekly Installs
95
Repository
lobbi-docs/claude
GitHub Stars
11
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass