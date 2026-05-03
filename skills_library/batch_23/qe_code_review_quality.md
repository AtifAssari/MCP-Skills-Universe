---
title: qe-code-review-quality
url: https://skills.sh/proffesor-for-testing/agentic-qe/qe-code-review-quality
---

# qe-code-review-quality

skills/proffesor-for-testing/agentic-qe/qe-code-review-quality
qe-code-review-quality
Installation
$ npx skills add https://github.com/proffesor-for-testing/agentic-qe --skill qe-code-review-quality
SKILL.md
Code Review Quality

<default_to_action> When reviewing code or establishing review practices:

PRIORITIZE feedback: 🔴 Blocker (must fix) → 🟡 Major → 🟢 Minor → 💡 Suggestion
FOCUS on: Bugs, security, testability, maintainability (not style preferences)
ASK questions over commands: "Have you considered...?" > "Change this to..."
PROVIDE context: Why this matters, not just what to change
LIMIT scope: Review < 400 lines at a time for effectiveness

Quick Review Checklist:

Logic: Does it work correctly? Edge cases handled?
Security: Input validation? Auth checks? Injection risks?
Testability: Can this be tested? Is it tested?
Maintainability: Clear naming? Single responsibility? DRY?
Performance: O(n²) loops? N+1 queries? Memory leaks?

Critical Success Factors:

Review the code, not the person
Catching bugs > nitpicking style
Fast feedback (< 24h) > thorough feedback </default_to_action>
Quick Reference Card
When to Use
PR code reviews
Pair programming feedback
Establishing team review standards
Mentoring developers
Feedback Priority Levels
Level	Icon	Meaning	Action
Blocker	🔴	Bug/security/crash	Must fix before merge
Major	🟡	Logic issue/test gap	Should fix before merge
Minor	🟢	Style/naming	Nice to fix
Suggestion	💡	Alternative approach	Consider for future
Review Scope Limits
Lines Changed	Recommendation
< 200	Single review session
200-400	Review in chunks
> 400	Request PR split
What to Focus On
✅ Review	❌ Skip
Logic correctness	Formatting (use linter)
Security risks	Naming preferences
Test coverage	Architecture debates
Performance issues	Style opinions
Error handling	Trivial changes
Feedback Templates
Blocker (Must Fix)
🔴 **BLOCKER: SQL Injection Risk**

This query is vulnerable to SQL injection:
```javascript
db.query(`SELECT * FROM users WHERE id = ${userId}`)


Fix: Use parameterized queries:

db.query('SELECT * FROM users WHERE id = ?', [userId])


Why: User input directly in SQL allows attackers to execute arbitrary queries.


### Major (Should Fix)
```markdown
🟡 **MAJOR: Missing Error Handling**

What happens if `fetchUser()` throws? The error bubbles up unhandled.

**Suggestion:** Add try/catch with appropriate error response:
```javascript
try {
  const user = await fetchUser(id);
  return user;
} catch (error) {
  logger.error('Failed to fetch user', { id, error });
  throw new NotFoundError('User not found');
}


### Minor (Nice to Fix)
```markdown
🟢 **minor:** Variable name could be clearer

`d` doesn't convey meaning. Consider `daysSinceLastLogin`.

Suggestion (Consider)
💡 **suggestion:** Consider extracting this to a helper

This validation logic appears in 3 places. A `validateEmail()` helper would reduce duplication. Not blocking, but might be worth a follow-up PR.

Review Questions to Ask
Logic
What happens when X is null/empty/negative?
Is there a race condition here?
What if the API call fails?
Security
Is user input validated/sanitized?
Are auth checks in place?
Any secrets or PII exposed?
Testability
How would you test this?
Are dependencies injectable?
Is there a test for the happy path? Edge cases?
Maintainability
Will the next developer understand this?
Is this doing too many things?
Is there duplication we could reduce?
Agent-Assisted Reviews
// Comprehensive code review
await Task("Code Review", {
  prNumber: 123,
  checks: ['security', 'performance', 'testability', 'maintainability'],
  feedbackLevels: ['blocker', 'major', 'minor'],
  autoApprove: { maxBlockers: 0, maxMajor: 2 }
}, "qe-quality-analyzer");

// Security-focused review
await Task("Security Review", {
  prFiles: changedFiles,
  scanTypes: ['injection', 'auth', 'secrets', 'dependencies']
}, "qe-security-scanner");

// Test coverage review
await Task("Coverage Review", {
  prNumber: 123,
  requireNewTests: true,
  minCoverageDelta: 0
}, "qe-coverage-analyzer");

Agent Coordination Hints
Memory Namespace
aqe/code-review/
├── review-history/*     - Past review decisions
├── patterns/*           - Common issues by team/repo
├── feedback-templates/* - Reusable feedback
└── metrics/*            - Review turnaround time

Fleet Coordination
const reviewFleet = await FleetManager.coordinate({
  strategy: 'code-review',
  agents: [
    'qe-quality-analyzer',    // Logic, maintainability
    'qe-security-scanner',    // Security risks
    'qe-performance-tester',  // Performance issues
    'qe-coverage-analyzer'    // Test coverage
  ],
  topology: 'parallel'
});

Review Etiquette
✅ Do	❌ Don't
"Have you considered...?"	"This is wrong"
Explain why it matters	Just say "fix this"
Acknowledge good code	Only point out negatives
Suggest, don't demand	Be condescending
Review < 400 lines	Review 2000 lines at once
Related Skills
agentic-quality-engineering - Agent coordination
security-testing - Security review depth
refactoring-patterns - Maintainability patterns
Remember

Prioritize feedback: 🔴 Blocker → 🟡 Major → 🟢 Minor → 💡 Suggestion. Focus on bugs and security, not style. Ask questions, don't command. Review < 400 lines at a time. Fast feedback (< 24h) beats thorough feedback.

With Agents: Agents automate security, performance, and coverage checks, freeing human reviewers to focus on logic and design. Use agents for consistent, fast initial review.

Weekly Installs
41
Repository
proffesor-for-t…entic-qe
GitHub Stars
334
First Seen
Feb 27, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass