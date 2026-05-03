---
title: quality-audit
url: https://skills.sh/nickcrew/claude-ctx-plugin/quality-audit
---

# quality-audit

skills/nickcrew/claude-ctx-plugin/quality-audit
quality-audit
Installation
$ npx skills add https://github.com/nickcrew/claude-ctx-plugin --skill quality-audit
SKILL.md
Quality Audit Skill

Systematic framework for evaluating skill quality across four dimensions: Clarity, Completeness, Accuracy, and Usefulness.

When to Use This Skill
Reviewing a new skill before adding to the registry
Auditing existing skills for quality improvements
Creating quality rubrics for skill validation
Standardizing skill quality across the library
Preparing skills for production use
Core Principles
The Four Quality Dimensions
Dimension	Weight	Focus
Clarity	25%	Structure, readability, progressive disclosure
Completeness	25%	Coverage, examples, edge cases, anti-patterns
Accuracy	30%	Correctness, best practices, security
Usefulness	20%	Real-world applicability, production-readiness
Scoring Scale (1-5)
Score	Label	Meaning
1	Unacceptable	Fundamentally broken, dangerous, or unusable
2	Needs Work	Major issues requiring significant revision
3	Acceptable	Meets minimum standards, functional
4	Good	High quality, minor improvements possible
5	Excellent	Exemplary, production-ready, best-in-class
Passing Criteria
Minimum: 3.0 weighted average (acceptable)
Target: 4.0 weighted average (good)
Exceptional: 4.5+ weighted average (excellent)
Blocking: Accuracy must be ≥3.0 (no dangerous advice)
Audit Workflow
Phase 1: Structure Check
checklist:
  structure:
    - [ ] Has valid YAML frontmatter
    - [ ] Contains required metadata (name, description)
    - [ ] Follows progressive disclosure (Tier 1 → 2 → 3)
    - [ ] Sections are logically ordered
    - [ ] Token estimate is reasonable (<5000 for core)

Phase 2: Content Evaluation
checklist:
  content:
    - [ ] "When to Use" section is clear
    - [ ] Core principles are well-defined
    - [ ] Code examples are complete and runnable
    - [ ] Anti-patterns are documented
    - [ ] Troubleshooting guidance exists

Phase 3: Dimension Scoring

For each dimension, evaluate against specific criteria:

Clarity Criteria:

Well-organized sections with logical flow
Concise explanations without jargon overload
Code examples are readable and well-commented
Progressive disclosure from simple to complex

Completeness Criteria:

Covers core concepts thoroughly
Includes edge cases and error handling
Provides both do's and don'ts
Has working examples for main use cases

Accuracy Criteria:

Code examples compile/run without errors
Follows current best practices (not deprecated)
Security considerations are correct
Performance claims are verifiable

Usefulness Criteria:

Examples solve real-world problems
Can be applied immediately
Scales to production use cases
Includes troubleshooting guidance
Phase 4: Report Generation
## Audit Report: {skill_name}

**Date**: {date}
**Auditor**: {auditor}
**Status**: {PASS|FAIL|NEEDS_REVIEW}

### Scores

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Clarity | {x}/5 | 25% | {x*0.25} |
| Completeness | {x}/5 | 25% | {x*0.25} |
| Accuracy | {x}/5 | 30% | {x*0.30} |
| Usefulness | {x}/5 | 20% | {x*0.20} |
| **Total** | | | **{sum}/5** |

### Issues Found

- [CRITICAL] {issue description}
- [MAJOR] {issue description}
- [MINOR] {issue description}

### Recommendations

1. {actionable recommendation}
2. {actionable recommendation}

Implementation Patterns
Pattern 1: Quick Audit (5-minute review)

Use for rapid assessment of skill quality:

# Run automated structure checks
cortex skills audit <skill-name> --quick

# Output: Pass/Fail with basic metrics


Quick Audit Checks:

YAML frontmatter valid?
Required sections present?
Code blocks have language tags?
No TODO/FIXME markers?
Token count reasonable?
Pattern 2: Full Audit (15-30 minute review)

Comprehensive evaluation with human review:

# Generate full audit report
cortex skills audit <skill-name> --full

# Interactive mode for scoring
cortex skills audit <skill-name> --interactive


Full Audit Process:

Run automated checks
Read through content manually
Test code examples
Score each dimension
Document issues and recommendations
Generate report
Pattern 3: Comparative Audit

Compare skill against reference implementation:

# Compare against template-skill-enhanced
cortex skills audit <skill-name> --compare template-skill-enhanced

Pattern 4: Batch Audit

Audit multiple skills for registry health:

# Audit all skills in a category
cortex skills audit --category security

# Audit skills below threshold
cortex skills audit --below-score 3.5

CLI Commands
# Basic audit
cortex skills audit <skill-name>

# Options
  --quick           Quick structural check only
  --full            Full audit with all dimensions
  --interactive     Interactive scoring mode
  --output FILE     Write report to file
  --format FORMAT   Output format (markdown|json|yaml)
  --compare SKILL   Compare against reference skill
  --fix             Auto-fix simple issues (formatting)

Creating Custom Rubrics

Skills can define custom rubrics in validation/rubric.yaml:

# validation/rubric.yaml
version: "1.0.0"
skill_name: my-skill

dimensions:
  clarity:
    weight: 25
    criteria:
      - "API examples use realistic data"
      - "Error handling is shown for each operation"
  completeness:
    weight: 25
    criteria:
      - "Covers all HTTP methods"
      - "Includes pagination patterns"
  accuracy:
    weight: 30
    criteria:
      - "Follows REST conventions"
      - "Security headers documented"
  usefulness:
    weight: 20
    criteria:
      - "Examples work with common frameworks"

passing_criteria:
  minimum_score: 3.5  # Higher bar for this skill
  required_dimensions:
    - accuracy
    - completeness

Best Practices
Do
Be specific - "Line 45: SQL query vulnerable to injection" not "has security issues"
Be actionable - Include how to fix each issue
Be fair - Use the same standards consistently
Document evidence - Quote specific content for each score
Prioritize - Critical issues first, suggestions last
Don't
Score based on personal style preferences
Mark deprecated patterns without suggesting alternatives
Fail skills for missing optional sections
Ignore security issues regardless of other scores
Rush through audits for complex skills
Anti-Patterns
The Rubber Stamp

Problem: Approving skills without thorough review Why it's bad: Low-quality skills erode trust in the library Fix: Use the full audit checklist, test code examples

The Perfectionist Block

Problem: Failing skills for minor issues Why it's bad: Prevents useful skills from being available Fix: Distinguish between blocking issues and suggestions

Score Inflation

Problem: Giving high scores without justification Why it's bad: Makes scores meaningless Fix: Document specific evidence for each score

Integration with CI/CD
# .github/workflows/skill-quality.yml
name: Skill Quality Gate

on:
  pull_request:
    paths:
      - 'skills/**'

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install cortex
        run: pip install cortex
      - name: Audit changed skills
        run: |
          for skill in $(git diff --name-only HEAD~1 | grep 'skills/' | cut -d'/' -f2 | uniq); do
            cortex skills audit "$skill" --quick --fail-under 3.0
          done

Troubleshooting
"Audit fails but skill looks fine"
Check YAML frontmatter syntax
Verify all required sections exist
Ensure code blocks have language tags
Check for hidden characters (copy/paste issues)
"Scores seem inconsistent"
Review the scoring guide for each dimension
Calibrate by auditing template-skill-enhanced first
Use --interactive mode for clearer criteria
External Resources
Skill Template Reference
Rubric Schema
Skill Creator Guide
Changelog
1.0.0 (2026-01-05)
Initial release
Four-dimension scoring framework
CLI integration
CI/CD workflow example
Weekly Installs
53
Repository
nickcrew/claude…x-plugin
GitHub Stars
15
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass