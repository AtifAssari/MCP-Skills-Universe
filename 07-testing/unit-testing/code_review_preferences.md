---
title: code-review-preferences
url: https://skills.sh/chaiwithjai/claude-code-mastery/code-review-preferences
---

# code-review-preferences

skills/chaiwithjai/claude-code-mastery/code-review-preferences
code-review-preferences
Installation
$ npx skills add https://github.com/chaiwithjai/claude-code-mastery --skill code-review-preferences
SKILL.md

<essential_principles>

Code Review Philosophy

Reviews exist to:

Catch bugs before production
Share knowledge across the team
Maintain consistency in the codebase

Reviews do NOT exist to:

Show off knowledge
Enforce personal style preferences
Block progress unnecessarily
The 3-Pass Method
Pass 1: Understand (don't comment yet)
What is this change trying to do?
What files are affected?
What's the scope?
Pass 2: Correctness
Are there bugs?
Are edge cases handled?
Are there security issues?
Pass 3: Improvements (max 5 comments)
Is it readable?
Is it maintainable?
Are there better patterns?
Review Checklist
Must Check
 Tests pass
 No obvious bugs
 Edge cases handled
 No security vulnerabilities
 No secrets in code
Should Check
 Code is readable
 Functions < 50 lines
 Clear naming
 Helpful error messages
Nice to Check
 Performance considerations
 Documentation updated
 Consistent patterns
Feedback Style

DO:

Ask questions: "What happens if X is null?"
Be specific: "Line 42: Consider guard clause"
Acknowledge good work: "Nice refactor"
Limit comments: Max 5 per review

DON'T:

Dictate: "You must do X"
Be vague: "This could be better"
Nitpick style: "I prefer single quotes" </essential_principles>
Paste code/diff - I'll review inline
Reference file - Use @filename
Describe PR - I'll ask questions

Context:

Bug fix / New feature / Refactor / Performance

Specific concerns? (Security, breaking changes, etc.)

Weekly Installs
10
Repository
chaiwithjai/cla…-mastery
GitHub Stars
1
First Seen
Jan 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass