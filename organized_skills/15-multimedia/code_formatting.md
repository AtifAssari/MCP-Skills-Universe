---
rating: ⭐⭐
title: code formatting
url: https://skills.sh/openshift/hypershift/code-formatting
---

# code formatting

skills/openshift/hypershift/Code Formatting
Code Formatting
Installation
$ npx skills add https://github.com/openshift/hypershift --skill 'Code Formatting'
SKILL.md
Code Quality, Formatting and Conventions
Code Formatting and Linting
Use make lint-fix after writing Go code to automatically fix most linting issues
Run make verify to verify both linting and tests pass before committing
For markdown files, use make verify-codespell to catch spelling errors
Test Conventions - MANDATORY

NON-NEGOTIABLE RULE: Every Go test name MUST follow this exact format:

name: "When <condition>, it should <expected behavior>"


Examples:

name: "When NodePool has valid image ID, it should create Azure machine template"
name: "When subnet ID is invalid, it should return error"
name: "When encryption is enabled, it should configure disk encryption set"


NEVER use generic names like:

❌ "nominal case without managed identity"
❌ "basic Azure machine template with ImageID"
❌ "error case - invalid subnet ID"

ALWAYS use "When...it should..." format:

✅ "When NodePool has no managed identity, it should create template without identity"

✅ "When NodePool has ImageID, it should create basic Azure machine template"

✅ "When subnet ID is invalid, it should return error with subnet parse message"

Always include unit tests when creating new functions or modifying existing ones

Quick Checklist

Before committing:

 Ran make lint-fix on Go code
 Ran make verify (passes)
 Tests use "When...it should..." naming format
 New functions have unit tests
 Markdown checked with make verify-codespell
Weekly Installs
–
Repository
openshift/hypershift
GitHub Stars
523
First Seen
–
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass