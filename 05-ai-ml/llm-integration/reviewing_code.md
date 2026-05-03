---
title: reviewing-code
url: https://skills.sh/tdhopper/dotfiles2.0/reviewing-code
---

# reviewing-code

skills/tdhopper/dotfiles2.0/reviewing-code
reviewing-code
Installation
$ npx skills add https://github.com/tdhopper/dotfiles2.0 --skill reviewing-code
SKILL.md
Code Review

Focus on substantive issues: bugs, missing tests, complexity, performance, duplication, incomplete implementations. Skip linting concerns (formatting, imports, naming style).

External Review (Optional)

Check for external reviewers and use if available. Priority: Codex > Gemini

command -v codex >/dev/null 2>&1 && echo "Codex available"
command -v gemini >/dev/null 2>&1 && echo "Gemini available"


If Codex available:

Local branch: codex --config model_reasoning_effort="high" review --base BASE_BRANCH
Remote PR: gh pr diff NUMBER | codex review --config model_reasoning_effort="high" -

If only Gemini: Pipe diff to gemini with review prompt.

Workflow

Get the diff

PR: gh pr view NUMBER --json title,body,files then gh pr diff NUMBER
Branch: git diff origin/master...HEAD
Uncommitted: git diff

Gather context - Read PR description, commit messages, project CLAUDE.md

Review each file for:

Completeness: All code paths handled? Stubs left behind?
Tests: Added? Meaningful? Edge cases covered?
Complexity: Justified abstractions? Simpler alternatives?
Performance: Hot path regressions? Unbatched I/O?
Duplication: Similar code already exists? (rg "pattern")

Synthesize external review (if used) with your findings. Consensus issues = high confidence.

Output Format
## Summary
[1-2 sentences]

## External Reviewer
[If used: Codex or Gemini]

## Key Findings

### Must Address
1. **[Issue]** (`file:line`) [Models]
   - Details
   - **Risk**: Why it matters

### Should Consider
2. **[Issue]** (`file:line`)
   - Details

### Minor Notes
- Observations

## Tests
[Coverage and quality assessment]

## Complexity
[Net impact on codebase complexity]


Numbering: Single sequence across all sections. Model attribution: [Codex + Claude], [Claude], etc.

Scope

In scope: Logic errors, missing error handling, test gaps, performance regressions, unnecessary complexity, duplication, incomplete implementations, project guideline violations.

Out of scope (linters handle): Formatting, import order, naming style, type annotations, docstring format.

Weekly Installs
8
Repository
tdhopper/dotfiles2.0
GitHub Stars
7
First Seen
Jan 27, 2026
Security Audits
Gen Agent Trust HubWarn
SocketFail
SnykWarn