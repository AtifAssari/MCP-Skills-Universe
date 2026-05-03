---
title: code-review-checklist
url: https://skills.sh/vudovn/antigravity-kit/code-review-checklist
---

# code-review-checklist

skills/vudovn/antigravity-kit/code-review-checklist
code-review-checklist
Installation
$ npx skills add https://github.com/vudovn/antigravity-kit --skill code-review-checklist
SKILL.md
Code Review Checklist
Quick Review Checklist
Correctness
 Code does what it's supposed to do
 Edge cases handled
 Error handling in place
 No obvious bugs
Security
 Input validated and sanitized
 No SQL/NoSQL injection vulnerabilities
 No XSS or CSRF vulnerabilities
 No hardcoded secrets or sensitive credentials
 AI-Specific: Protection against Prompt Injection (if applicable)
 AI-Specific: Outputs are sanitized before being used in critical sinks
Performance
 No N+1 queries
 No unnecessary loops
 Appropriate caching
 Bundle size impact considered
Code Quality
 Clear naming
 DRY - no duplicate code
 SOLID principles followed
 Appropriate abstraction level
Testing
 Unit tests for new code
 Edge cases tested
 Tests readable and maintainable
Documentation
 Complex logic commented
 Public APIs documented
 README updated if needed
AI & LLM Review Patterns (2025)
Logic & Hallucinations
 Chain of Thought: Does the logic follow a verifiable path?
 Edge Cases: Did the AI account for empty states, timeouts, and partial failures?
 External State: Is the code making safe assumptions about file systems or networks?
Prompt Engineering Review
// ❌ Vague prompt in code
const response = await ai.generate(userInput);

// ✅ Structured & Safe prompt
const response = await ai.generate({
  system: "You are a specialized parser...",
  input: sanitize(userInput),
  schema: ResponseSchema
});

Anti-Patterns to Flag
// ❌ Magic numbers
if (status === 3) { ... }

// ✅ Named constants
if (status === Status.ACTIVE) { ... }

// ❌ Deep nesting
if (a) { if (b) { if (c) { ... } } }

// ✅ Early returns
if (!a) return;
if (!b) return;
if (!c) return;
// do work

// ❌ Long functions (100+ lines)
// ✅ Small, focused functions

// ❌ any type
const data: any = ...

// ✅ Proper types
const data: UserData = ...

Review Comments Guide
// Blocking issues use 🔴
🔴 BLOCKING: SQL injection vulnerability here

// Important suggestions use 🟡
🟡 SUGGESTION: Consider using useMemo for performance

// Minor nits use 🟢
🟢 NIT: Prefer const over let for immutable variable

// Questions use ❓
❓ QUESTION: What happens if user is null here?

Weekly Installs
229
Repository
vudovn/antigravity-kit
GitHub Stars
7.3K
First Seen
Jan 21, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass