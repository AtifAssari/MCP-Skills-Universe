---
rating: ⭐⭐⭐
title: validate-skills
url: https://skills.sh/callstackincubator/agent-skills/validate-skills
---

# validate-skills

skills/callstackincubator/agent-skills/validate-skills
validate-skills
Installation
$ npx skills add https://github.com/callstackincubator/agent-skills --skill validate-skills
Summary

Validates skills against agentskills.io spec and Claude Code best practices.

Checks skill metadata compliance including name format, description length, and optional fields like license and compatibility
Enforces Claude Code best practices: third-person descriptions, body length limits, single-level references, and markdown link formatting
Provides structured validation reports flagging spec violations and authoring guideline deviations
Designed for use via /validate-skills command within a skills repository workflow
SKILL.md
Validate Skills

Validate all skills in skills/ against the agentskills.io spec and Claude Code best practices.

Validation Checklist

For each skill directory, verify:

Spec Compliance (agentskills.io)
Check	Rule
name format	1-64 chars, lowercase alphanumeric + hyphens, no leading/trailing/consecutive hyphens
name matches directory	Directory name must equal name field
description length	1-1024 characters, non-empty
Optional fields valid	license, metadata, compatibility if present
Best Practices (Claude Code)
Check	Rule
Description format	Third person, describes what + when to use
Body length	Under 500 lines
References one-level deep	No nested reference chains
Links are markdown	Use [text](path) not bare filenames
No redundancy	Don't repeat description in body
Concise	Only add context Claude doesn't already have
How to Run

Find all skill directories:

fd -t d -d 1 . skills/


For each skill, read SKILL.md and check against the rules above

Report issues in this format:

## Validation Results

### skills/example-skill
- [PASS] name format valid
- [FAIL] name "example" doesn't match directory "example-skill"
- [PASS] description length OK (156 chars)

References
agentskills.io spec
Claude Code best practices
Weekly Installs
1.7K
Repository
callstackincuba…t-skills
GitHub Stars
1.3K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass