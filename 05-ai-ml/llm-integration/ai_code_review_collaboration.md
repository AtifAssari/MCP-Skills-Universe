---
title: ai-code-review-collaboration
url: https://skills.sh/mkalhitti-cloud/universal-or-strategy/ai-code-review-collaboration
---

# ai-code-review-collaboration

skills/mkalhitti-cloud/universal-or-strategy/ai-code-review-collaboration
ai-code-review-collaboration
Installation
$ npx skills add https://github.com/mkalhitti-cloud/universal-or-strategy --skill ai-code-review-collaboration
SKILL.md
Multi-AI Code Review Collaboration Framework

A systematic approach to getting diverse AI perspectives on code, then synthesizing insights into actionable improvements.

When to Use This
Complex codebases where blind spots are likely
Production/live trading code where reliability is critical
Architecture decisions with trade-offs
When you want to validate Claude's recommendations
Before major refactoring or deployment
The Process
Phase 1: Initial Review (Claude)
Claude reviews code and documents findings
Creates context prompt for external AI
Identifies platform-specific constraints external AI must understand
Phase 2: External AI Review
User pastes prompt to external AI (Gemini, DeepSeek, GPT, etc.)
External AI provides structured review
User brings response back to Claude
Phase 3: Synthesis & Debate
Claude evaluates external AI's points
Categorizes into: Valid, Partially Valid, Invalid
Explains reasoning for each categorization
Creates response prompt for user to continue dialogue
Phase 4: Consensus
Continue rounds until agreement reached
Document final action plan
Prioritize fixes by risk and effort
Prompt Templates
Template A: Initial External AI Request
**[AI NAME] CODE REVIEW REQUEST - [PROJECT TYPE]**

I need a comprehensive code review. This code [CRITICAL CONTEXT - e.g., "runs on live funded accounts"]. Please review thoroughly and respond in a format I can share with another AI for collaborative discussion.

---

## CRITICAL PLATFORM CONTEXT (Read First)

[List platform-specific constraints that might not be obvious]
[List what IS and ISN'T possible on this platform]
[Explain why certain "standard" patterns don't apply]

---

## REVIEW SCOPE

Please analyze:
1. **Logic & Correctness** - [specific concerns]
2. **Risk Management** - [specific concerns]  
3. **Performance** - [specific concerns]
4. **Reliability** - [specific concerns]
5. **Code Quality** - [specific concerns]
6. **Scalability** - [planned expansion, multi-instance needs, performance at scale]
7. **Future Updateability** - [extension points, configuration extensibility, technical debt, breaking change risks]

---

## FUTURE ROADMAP (if applicable)

[Describe planned features, scaling needs, and future requirements so the reviewer can assess how well the current architecture supports them]

---

## THE CODE

[Include full code or key sections]

---

## RESPONSE FORMAT

Structure your response as:

**[AI NAME] CODE REVIEW - ROUND 1**

## ðŸ”´ CRITICAL ISSUES (Must Fix)
## ðŸŸ¡ IMPORTANT CONCERNS (Should Fix)  
## ðŸŸ¢ MINOR SUGGESTIONS (Nice to Have)
## âœ… WELL IMPLEMENTED
## ðŸ”® SCALABILITY ASSESSMENT
## ðŸ”§ FUTURE UPDATEABILITY ASSESSMENT
## â“ QUESTIONS / CLARIFICATIONS NEEDED
## ðŸ“‹ PRIORITIZED ACTION PLAN

---

## EXISTING FINDINGS (if any)

[Include prior AI findings so new AI can confirm/challenge]

Template B: Response to External AI
**CLAUDE'S RESPONSE TO [AI NAME] - ROUND [N]**

## âœ… FULL AGREEMENT
[Points we agree on completely]

## ðŸ¤ CONCESSIONS & MODIFICATIONS  
[Points where Claude adjusts position with explanation]

## ðŸ›¡ï¸ POINTS I STILL MAINTAIN
[Disagreements with detailed reasoning]

## ðŸ” NEW OBSERVATIONS
[Anything new Claude notices based on discussion]

## ðŸ“‹ UPDATED ACTION PLAN
[Current consensus on what to fix]

## ðŸ¤ CLOSING QUESTION
[Ask if they agree or have remaining concerns]

Template C: Final Consensus Summary
## MULTI-AI REVIEW CONSENSUS

**Participants:** [List AIs involved]
**Code Reviewed:** [File/project name]
**Date:** [Date]

### AGREED FIXES (In Priority Order)
| # | Issue | Fix | Effort | Risk |
|---|-------|-----|--------|------|
| 1 | [Issue] | [Solution] | [Low/Med/High] | [Low/Med/High] |

### EXPLICITLY REJECTED SUGGESTIONS
| Suggestion | Rejected Because |
|------------|------------------|
| [Suggestion] | [Platform constraint / Not applicable / etc.] |

### VERIFIED AS CORRECT
- [Item 1 that was reviewed and confirmed good]
- [Item 2]

### OPEN QUESTIONS FOR FUTURE
- [Any unresolved items to revisit later]

Best Practices
Always provide platform context - External AIs apply generic patterns without knowing constraints
Be specific about what CAN'T be done - Prevents suggestions for impossible approaches
Request structured responses - Makes synthesis easier
Track rounds - Label each exchange for clarity
Document consensus - Final agreement should be explicit
Implement incrementally - Test each fix before moving to next
Reference Files
references/prompt-templates.md - Copy-paste ready templates
references/platform-contexts.md - Pre-written context blocks for common platforms
references/synthesis-checklist.md - How to evaluate external AI suggestions
Weekly Installs
10
Repository
mkalhitti-cloud…strategy
First Seen
Jan 23, 2026
Security Audits
Gen Agent Trust HubFail
SocketPass
SnykWarn