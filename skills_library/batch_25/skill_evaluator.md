---
title: skill_evaluator
url: https://skills.sh/vuralserhat86/antigravity-agentic-skills/skill_evaluator
---

# skill_evaluator

skills/vuralserhat86/antigravity-agentic-skills/skill_evaluator
skill_evaluator
Installation
$ npx skills add https://github.com/vuralserhat86/antigravity-agentic-skills --skill skill_evaluator
SKILL.md
Skill Evaluator (WIP)

Evaluates skills against Anthropic's official best practices for agent skill authoring. Produces structured evaluation reports with scores and actionable recommendations.

Quick Start
Read the skill's SKILL.md and understand its purpose
Run automated validation: scripts/validate_skill.py <skill-path>
Perform manual evaluation against criteria below
Generate evaluation report with scores and recommendations
Evaluation Workflow
Step 1: Automated Validation

Run the validation script first:

scripts/validate_skill.py <path/to/skill>


This checks:

SKILL.md exists with valid YAML frontmatter
Name follows conventions (lowercase, hyphens, max 64 chars)
Description is present and under 1024 chars
Body is under 500 lines
File references are one-level deep
Step 2: Manual Evaluation

Evaluate each dimension and assign a score (1-5):

A. Naming (Weight: 10%)
Score	Criteria
5	Gerund form (-ing), clear purpose, memorable
4	Descriptive, follows conventions
3	Acceptable but could be clearer
2	Vague or misleading
1	Violates naming rules

Rules: Max 64 chars, lowercase + numbers + hyphens only, no reserved words (anthropic, claude), no XML tags.

Good: processing-pdfs, analyzing-spreadsheets, building-dashboards Bad: pdf, my-skill, ClaudeHelper, anthropic-tools

B. Description (Weight: 20%)
Score	Criteria
5	Clear functionality + specific activation triggers + third person
4	Good description with some triggers
3	Adequate but missing triggers or vague
2	Too brief or unclear purpose
1	Missing or unhelpful

Must include: What the skill does AND when to use it. Good: "Extracts text from PDFs. Use when working with PDF documents for text extraction, form parsing, or content analysis." Bad: "A skill for PDFs." or "Helps with documents."

C. Content Quality (Weight: 30%)
Score	Criteria
5	Concise, assumes Claude intelligence, actionable instructions
4	Generally good, minor verbosity
3	Some unnecessary explanations or redundancy
2	Overly verbose or confusing
1	Bloated, explains obvious concepts

Ask: "Does Claude really need this explanation?" Remove anything Claude already knows.

D. Structure & Organization (Weight: 25%)
Score	Criteria
5	Excellent progressive disclosure, clear navigation, optimal length
4	Good organization, appropriate file splits
3	Acceptable but could be better organized
2	Poor organization, missing references, or bloated SKILL.md
1	No structure, everything dumped in SKILL.md

Check:

SKILL.md under 500 lines
References are one-level deep (no nested chains)
Long reference files (>100 lines) have table of contents
Uses forward slashes in all paths
E. Degrees of Freedom (Weight: 10%)
Score	Criteria
5	Perfect match: high freedom for flexible tasks, low for fragile operations
4	Generally appropriate freedom levels
3	Acceptable but could be better calibrated
2	Mismatched: too rigid or too loose
1	Completely wrong freedom level for the task type

Guideline:

High freedom (text): Multiple valid approaches, context-dependent
Medium freedom (parameterized): Preferred pattern exists, some variation OK
Low freedom (specific scripts): Fragile operations, exact sequence required
F. Anti-Pattern Check (Weight: 5%)

Deduct points for each anti-pattern found:

 Too many options without clear recommendation (-1)
 Time-sensitive information with date conditionals (-1)
 Inconsistent terminology (-1)
 Windows-style paths (backslashes) (-1)
 Deeply nested references (more than one level) (-2)
 Scripts that punt error handling to Claude (-1)
 Magic numbers without justification (-1)
Step 3: Generate Report

Use this template:

# Skill Evaluation Report: [skill-name]

## Summary
- **Overall Score**: X.X/5.0
- **Recommendation**: [Ready for publication / Needs minor improvements / Needs major revision]

## Dimension Scores
| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Naming | X/5 | 10% | X.XX |
| Description | X/5 | 20% | X.XX |
| Content Quality | X/5 | 30% | X.XX |
| Structure | X/5 | 25% | X.XX |
| Degrees of Freedom | X/5 | 10% | X.XX |
| Anti-Patterns | X/5 | 5% | X.XX |
| **Total** | | 100% | **X.XX** |

## Strengths
- [List 2-3 things done well]

## Areas for Improvement
- [List specific issues with actionable fixes]

## Anti-Patterns Found
- [List any anti-patterns detected]

## Recommendations
1. [Priority 1 fix]
2. [Priority 2 fix]
3. [Priority 3 fix]

## Pre-Publication Checklist
- [ ] Description is specific with activation triggers
- [ ] SKILL.md under 500 lines
- [ ] One-level-deep file references
- [ ] Forward slashes in all paths
- [ ] No time-sensitive information
- [ ] Consistent terminology
- [ ] Concrete examples provided
- [ ] Scripts handle errors explicitly
- [ ] All configuration values justified
- [ ] Required packages listed
- [ ] Tested with Haiku, Sonnet, Opus

Score Interpretation
Score Range	Rating	Action
4.5 - 5.0	Excellent	Ready for publication
4.0 - 4.4	Good	Minor improvements recommended
3.0 - 3.9	Acceptable	Several improvements needed
2.0 - 2.9	Needs Work	Major revision required
1.0 - 1.9	Poor	Fundamental redesign needed
References
references/evaluation-criteria.md - Detailed evaluation criteria with examples
references/scoring-rubric.md - Complete scoring rubric and edge cases

Skill Evaluator v1.1 - Enhanced

🔄 Workflow

Kaynak: Google Engineering Practices - Code Review & Anthropic System Prompts

Aşama 1: Structural Analysis
 Compliance: Dosya yapısı (scripts/, references/) standarta uyuyor mu?
 Metadata: YAML frontmatter (name, description) eksiksiz ve valid mi?
 Modularity: Skill çok mu büyük? Bölünmesi gerekiyor mu? (Single Responsibility Principle).
Aşama 2: Content & Semantic Review
 Clarity: Talimatlar emir kipiyle (Imperative) ve net yazılmış mı? Belirsizlik var mı?
 Context Efficiency: "Gereksiz nezaket" veya "aşırı açıklama" var mı? Token israfı önlenmeli.
 Safety: Skill tehlikeli bir işlem (dosya silme, yetkisiz erişim) öneriyor mu?
Aşama 3: Functionality Verification
 Script Audit: scripts/ içindeki Python/Bash kodları güvenli ve çalışır durumda mı?
 Reference Check: references/ dosyaları gerçekten gerekli mi? Yoksa SKILL.md içine mi gömülmeli?
 Usability: Bir kullanıcı (veya ajan) bu skill'i okuyup hemen kullanabilir mi?
Kontrol Noktaları
Aşama	Doğrulama
1	Skill adı ve açıklaması birbiriyle tutarlı mı?
2	Anti-pattern (örn: Hardcoded path) tespit edildi mi?
3	Puanlama rubriğine göre objektif bir skor (1-5) verildi mi?
Weekly Installs
11
Repository
vuralserhat86/a…c-skills
GitHub Stars
42
First Seen
Jan 24, 2026