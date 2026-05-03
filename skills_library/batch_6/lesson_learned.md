---
title: lesson-learned
url: https://skills.sh/softaworks/agent-toolkit/lesson-learned
---

# lesson-learned

skills/softaworks/agent-toolkit/lesson-learned
lesson-learned
Installation
$ npx skills add https://github.com/softaworks/agent-toolkit --skill lesson-learned
Summary

Extract software engineering lessons from recent git changes by analyzing actual code patterns.

Analyzes code diffs against a curated principles reference to identify dominant patterns, trade-offs, and structural decisions
Supports multiple scopes: feature branches vs. main, specific commits, commit ranges, or uncommitted working changes
Maps findings to concrete SE principles with specific file and line references, avoiding generic advice
Presents lessons in a reflective format that mirrors the user's own code back to them rather than prescribing rules
SKILL.md
Lesson Learned

Extract specific, grounded software engineering lessons from actual code changes. Not a lecture -- a mirror. Show the user what their code already demonstrates.

Before You Begin

Load the principles reference first.

Read references/se-principles.md to have the principle catalog available
Optionally read references/anti-patterns.md if you suspect the changes include areas for improvement
Determine the scope of analysis (see Phase 1)

Do not proceed until you've loaded at least se-principles.md.

Phase 1: Determine Scope

Ask the user or infer from context what to analyze.

Scope	Git Commands	When to Use
Feature branch	git log main..HEAD --oneline + git diff main...HEAD	User is on a non-main branch (default)
Last N commits	git log --oneline -N + git diff HEAD~N..HEAD	User specifies a range, or on main (default N=5)
Specific commit	git show <sha>	User references a specific commit
Working changes	git diff + git diff --cached	User says "what about these changes?" before committing

Default behavior:

If on a feature branch: analyze branch commits vs main
If on main: analyze the last 5 commits
If the user provides a different scope, use that
Phase 2: Gather Changes
Run git log with the determined scope to get the commit list and messages
Run git diff for the full diff of the scope
If the diff is large (>500 lines), use git diff --stat first, then selectively read the top 3-5 most-changed files
Read commit messages carefully -- they contain intent that raw diffs miss
Only read changed files. Do not read the entire repo.
Phase 3: Analyze

Identify the dominant pattern -- the single most instructive thing about these changes.

Look for:

Structural decisions -- How was the code organized? Why those boundaries?
Trade-offs made -- What was gained vs. sacrificed? (readability vs. performance, DRY vs. clarity, speed vs. correctness)
Problems solved -- What was the before/after? What made the "after" better?
Missed opportunities -- Where could the code improve? (present gently as "next time, consider...")

Map findings to specific principles from references/se-principles.md. Be specific -- quote actual code, reference actual file names and line changes.

Phase 4: Present the Lesson

Use this template:

## Lesson: [Principle Name]

**What happened in the code:**
[2-3 sentences describing the specific change, referencing files and commits]

**The principle at work:**
[1-2 sentences explaining the SE principle]

**Why it matters:**
[1-2 sentences on the practical consequence -- what would go wrong without this, or what goes right because of it]

**Takeaway for next time:**
[One concrete, actionable sentence the user can apply to future work]


If there is a second lesson worth noting (maximum 2 additional):

---

### Also worth noting: [Principle Name]

**In the code:** [1 sentence]
**The principle:** [1 sentence]
**Takeaway:** [1 sentence]

What NOT to Do
Avoid	Why	Instead
Listing every principle that vaguely applies	Overwhelming and generic	Pick the 1-2 most relevant
Analyzing files that were not changed	Scope creep	Stick to the diff
Ignoring commit messages	They contain intent that diffs miss	Read them as primary context
Abstract advice disconnected from the code	Not actionable	Always reference specific files/lines
Negative-only feedback	Demoralizing	Lead with what works, then suggest improvements
More than 3 lessons	Dilutes the insight	One well-grounded lesson beats seven vague ones
Conversation Style
Reflective, not prescriptive. Use the user's own code as primary evidence.
Never say "you should have..." -- instead use "the approach here shows..." or "next time you face this, consider..."
If the code is good, say so. Not every lesson is about what went wrong. Recognizing good patterns reinforces them.
If the changes are trivial (a single config tweak, a typo fix), say so honestly rather than forcing a lesson. "These changes are straightforward -- no deep lesson here, just good housekeeping."
Be specific. Generic advice is worthless. Every claim must point to a concrete code change.
Weekly Installs
2.6K
Repository
softaworks/agent-toolkit
GitHub Stars
1.7K
First Seen
Feb 24, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass