---
rating: ⭐⭐
title: classifying-review-findings
url: https://skills.sh/bitwarden/ai-plugins/classifying-review-findings
---

# classifying-review-findings

skills/bitwarden/ai-plugins/classifying-review-findings
classifying-review-findings
Installation
$ npx skills add https://github.com/bitwarden/ai-plugins --skill classifying-review-findings
SKILL.md
Classifying Review Findings
Severity Categories
Emoji	Category	Criteria
❌	CRITICAL	Will break, crash, expose data, or violate requirements
⚠️	IMPORTANT	Missing error handling, unhandled edge cases, could cause bugs
♻️	DEBT	Duplicates patterns, violates conventions, needs rework within 6 months
🎨	SUGGESTED	Measurably improves security, reduces complexity by 3+, eliminates bug classes
❓	QUESTION	Requires human knowledge - unclear requirements, intent, or system conflicts

ALWAYS use hybrid emoji + text format for each finding (if multiple severities apply, use the most severe: ❌ > ⚠️ > ♻️ > 🎨 > ❓):

Before Classifying

Verify ALL three:

Can you trace the execution path showing incorrect behavior?
Is this handled elsewhere (error boundaries, middleware, validators)?
Are you certain about framework behavior and language semantics?

If any answer is "no" or "unsure" → DO NOT classify as a finding.

Not Valid Findings (Reject)
Praise ("great implementation")
Vague suggestions ("could be simpler")
Style preferences without enforced standard
Naming nitpicks unless actively misleading
PR metadata issues (title, description, test plan) - handled by summary skill, not classified here
Renovate/Dependabot minor/patch updates to existing dependencies with passing CI — these are routine Stage 5 monitoring, not reviewable findings
Suggested Improvements (🎨) Criteria

Only suggest improvements that provide measurable value:

Security gain - Eliminates entire vulnerability class (SQL injection, XSS, etc.)
Complexity reduction - Reduces cyclomatic complexity by 3+, eliminates nesting level
Bug prevention - Makes entire category of bugs impossible (type safety, null safety)
Performance gain - Reduces O(n²) to O(n), eliminates N+1 queries (provide evidence)

Provide concrete metrics:

❌ "This could be simpler"
✅ "This has cyclomatic complexity of 12; extracting validation logic would reduce to 6"

If you can't measure the improvement, don't suggest it.

Weekly Installs
42
Repository
bitwarden/ai-plugins
GitHub Stars
90
First Seen
Feb 16, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass