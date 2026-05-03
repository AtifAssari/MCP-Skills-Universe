---
title: reviewing-code
url: https://skills.sh/jlowin/fastmcp/reviewing-code
---

# reviewing-code

skills/jlowin/fastmcp/reviewing-code
reviewing-code
Installation
$ npx skills add https://github.com/jlowin/fastmcp --skill reviewing-code
SKILL.md
Code Review
Philosophy

Code review maintains a healthy codebase while helping contributors succeed. The burden of proof is on the PR to demonstrate it adds value. Your job is to help it get there through actionable feedback.

Critical: A perfectly written PR that adds unwanted functionality must still be rejected. The code must advance the codebase in the intended direction. When rejecting, provide clear guidance on how to align with project goals.

Be friendly and welcoming while maintaining high standards. Call out what works well. When code needs improvement, be specific about why and how to fix it.

What to Focus On
Does this advance the codebase correctly?

Even perfect code for unwanted features should be rejected.

Dependency version compatibility

When a PR adapts code to a new version of a dependency (e.g., removing a parameter that was dropped upstream, using a new API):

The version pin in pyproject.toml must match. If the change breaks compatibility with the previously-pinned minimum version, the minimum version must be bumped. Otherwise users on the old version get a regression.
If backwards compatibility with the old version is desired, the code must handle both versions (e.g., try/except, version check). Simply deleting the old API usage without bumping the pin is always wrong — it silently breaks users on the old version.
Lock file (uv.lock) changes should be scoped to the PR's purpose. A PR fixing a ty compatibility issue should not also include unrelated dependency version bumps (anthropic, google-auth, etc.) from running uv sync --upgrade. These create noise and make the diff harder to review.
API design and naming

Identify confusing patterns or non-idiomatic code:

Parameter values that contradict defaults
Mutable default arguments
Unclear naming that will confuse future readers
Inconsistent patterns with the rest of the codebase
Specific improvements

Provide actionable feedback, not generic observations.

User ergonomics

Think about the API from a user's perspective. Is it intuitive? What's the learning curve?

For Agent Reviewers
Read the full context: Examine related files, tests, and documentation before reviewing
Check against established patterns: Look for consistency with codebase conventions
Verify functionality claims: Understand what the code actually does, not just what it claims
Consider edge cases: Think through error conditions and boundary scenarios
What to Avoid
Generic feedback without specifics
Hypothetical problems unlikely to occur
Nitpicking organizational choices without strong reason
Summarizing what the PR already describes
Star ratings or excessive emojis
Bikeshedding style preferences when functionality is correct
Requesting changes without suggesting solutions
Focusing on personal coding style over project conventions
Tone
Acknowledge good decisions: "This API design is clean"
Be direct but respectful
Explain impact: "This will confuse users because..."
Remember: Someone else maintains this code forever
Decision Framework

Before approving, ask:

Does this PR achieve its stated purpose?
Is that purpose aligned with where the codebase should go?
Would I be comfortable maintaining this code?
Have I actually understood what it does, not just what it claims?
Does this change introduce technical debt?

If something needs work, your review should help it get there through specific, actionable feedback. If it's solving the wrong problem, say so clearly.

Comment Examples

Good comments:

Instead of	Write
"Add more tests"	"The handle_timeout method needs tests for the edge case where timeout=0"
"This API is confusing"	"The parameter name data is ambiguous - consider message_content to match the MCP specification"
"This could be better"	"This approach works but creates a circular dependency. Consider moving the validation to utils/validators.py"
Checklist

Before approving, verify:

 All required development workflow steps completed (uv sync, prek, pytest)
 Changes align with repository patterns and conventions
 API changes are documented and backwards-compatible where possible
 Error handling follows project patterns (specific exception types)
 Tests cover new functionality and edge cases
 The change advances the codebase in the intended direction
Weekly Installs
77
Repository
jlowin/fastmcp
GitHub Stars
25.0K
First Seen
Jan 22, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass