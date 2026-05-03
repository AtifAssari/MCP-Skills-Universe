---
title: code-quality
url: https://skills.sh/tai-ch0802/skills-bundle/code-quality
---

# code-quality

skills/tai-ch0802/skills-bundle/code-quality
code-quality
Installation
$ npx skills add https://github.com/tai-ch0802/skills-bundle --skill code-quality
SKILL.md
Code Quality — Standards & Review

CRITICAL SKILL — Be concise, direct, and solution-focused.

Core Principles
Principle	Rule
SRP	Single Responsibility — each function/class does ONE thing
DRY	Don't Repeat Yourself — extract duplicates, reuse
KISS	Keep It Simple — simplest solution that works
YAGNI	You Aren't Gonna Need It — don't build unused features
Boy Scout	Leave code cleaner than you found it
Naming Rules
Element	Convention
Variables	Reveal intent: userCount not n
Functions	Verb + noun: getUserById() not user()
Booleans	Question form: isActive, hasPermission, canEdit
Constants	SCREAMING_SNAKE: MAX_RETRY_COUNT

Rule: If you need a comment to explain a name, rename it.

Function Rules
Rule	Description
Small	Max 20 lines, ideally 5-10
One Thing	Does one thing, does it well
One Level	One level of abstraction per function
Few Args	Max 3 arguments, prefer 0-2
No Side Effects	Don't mutate inputs unexpectedly
Code Structure
Pattern	Apply
Guard Clauses	Early returns for edge cases
Flat > Nested	Avoid deep nesting (max 2 levels)
Composition	Small functions composed together
Colocation	Keep related code close
Code Review Checklist
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

Anti-Patterns
❌ Pattern	✅ Fix
Comment every line	Delete obvious comments
Helper for one-liner	Inline the code
Factory for 2 objects	Direct instantiation
utils.ts with 1 function	Put code where used
"First we import..."	Just write code
Deep nesting	Guard clauses
Magic numbers	Named constants
God functions	Split by responsibility
any type	Proper types
Long functions (100+ lines)	Small, focused functions
Review Comments Guide
// Blocking issues use 🔴
🔴 BLOCKING: SQL injection vulnerability here

// Important suggestions use 🟡
🟡 SUGGESTION: Consider using useMemo for performance

// Minor nits use 🟢
🟢 NIT: Prefer const over let for immutable variable

// Questions use ❓
❓ QUESTION: What happens if user is null here?

AI Coding Style
Situation	Action
User asks for feature	Write it directly
User reports bug	Fix it, don't explain
No clear requirement	Ask, don't assume
🔴 Before Editing ANY File (THINK FIRST!)
Question	Why
What imports this file?	They might break
What does this file import?	Interface changes
What tests cover this?	Tests might fail
Is this a shared component?	Multiple places affected

🔴 Rule: Edit the file + all dependent files in the SAME task. 🔴 Never leave broken imports or missing updates.

🔴 Self-Check Before Completing (MANDATORY)
Check	Question
✅ Goal met?	Did I do exactly what user asked?
✅ Files edited?	Did I modify all necessary files?
✅ Code works?	Did I test/verify the change?
✅ No errors?	Lint and TypeScript pass?
✅ Nothing forgotten?	Any edge cases missed?

🔴 Rule: If ANY check fails, fix it before completing.

Summary
Do	Don't
Write code directly	Write tutorials
Let code self-document	Add obvious comments
Fix bugs immediately	Explain the fix first
Inline small things	Create unnecessary files
Name things clearly	Use abbreviations
Keep functions small	Write 100+ line functions

Remember: The user wants working code, not a programming lesson.

Weekly Installs
12
Repository
tai-ch0802/skills-bundle
GitHub Stars
1
First Seen
Mar 1, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass