---
rating: ⭐⭐
title: skill-improver
url: https://skills.sh/trailofbits/skills/skill-improver
---

# skill-improver

skills/trailofbits/skills/skill-improver
skill-improver
Installation
$ npx skills add https://github.com/trailofbits/skills --skill skill-improver
Summary

Iteratively refines Claude Code skills through automated review-fix cycles until quality standards are met.

Runs repeated skill-reviewer assessments and applies fixes in a continuous loop, stopping only when critical and major issues are resolved
Categorizes issues by severity: critical (missing frontmatter, broken paths), major (weak triggers, missing guidance sections), and minor (style preferences requiring individual evaluation)
Requires the plugin-dev plugin and works exclusively on SKILL.md files within skill directories
Best suited for multi-issue skills or new skills needing systematic refinement; use /skill-reviewer directly for one-time reviews
SKILL.md
Skill Improvement Methodology

Iteratively improve a Claude Code skill using the skill-reviewer agent until it meets quality standards.

Prerequisites

Requires the plugin-dev plugin which provides the skill-reviewer agent.

Verify it's enabled: run /plugins — plugin-dev should appear in the list. If missing, install from the Trail of Bits plugin repository.

Core Loop
Review - Call skill-reviewer on the target skill
Categorize - Parse issues by severity
Fix - Address critical and major issues
Evaluate - Check minor issues for validity before fixing
Repeat - Continue until quality bar is met
When to Use
Improving a skill with multiple quality issues
Iterating on a new skill until it meets standards
Automated fix-review cycles instead of manual editing
Consistent quality enforcement across skills
When NOT to Use
One-time review: Use /skill-reviewer directly instead
Quick single fixes: Edit the file directly
Non-skill files: Only works on SKILL.md files
Experimental skills: Manual iteration gives more control during exploration
Issue Categorization
Critical Issues (MUST fix immediately)

These block skill loading or cause runtime failures:

Missing required frontmatter fields (name, description) — Claude cannot index or trigger the skill
Invalid YAML frontmatter syntax — Parsing fails, skill won't load
Referenced files that don't exist — Runtime errors when Claude follows links
Broken file paths — Same as above, leads to tool failures
Major Issues (MUST fix)

These significantly degrade skill effectiveness:

Weak or vague trigger descriptions — Claude may not recognize when to use the skill
Wrong writing voice (second person "you" instead of imperative) — Inconsistent with Claude's execution model
SKILL.md exceeds 500 lines without using references/ — Overloads context, reduces comprehension
Missing "When to Use" or "When NOT to Use" sections — Required by project quality standards
Description doesn't specify when to trigger — Skill may never be selected
Minor Issues (Evaluate before fixing)

These are polish items that may or may not improve the skill:

Subjective style preferences — Reviewer may have different taste than author
Optional enhancements — May add complexity without proportional value
"Nice to have" improvements — Consider cost-benefit before implementing
Formatting suggestions — Often valid but low impact
Minor Issue Evaluation

Before implementing any minor issue fix, evaluate:

Is this a genuine improvement? - Does it add real value or just satisfy a preference?
Could this be a false positive? - Is the reviewer misunderstanding context?
Would this actually help Claude use the skill? - Focus on functional improvements

Only implement minor fixes that are clearly beneficial. Skill-reviewer may produce false positives.

Invoking skill-reviewer

Use the skill-reviewer agent from the plugin-dev plugin. Request a review by asking Claude to:

Review the skill at [SKILL_PATH] using the plugin-dev:skill-reviewer agent. Provide a detailed quality assessment with issues categorized by severity.

Replace [SKILL_PATH] with the absolute path to the skill directory (e.g., /path/to/plugins/my-plugin/skills/my-skill).

Example Fix Cycle

Iteration 1 — skill-reviewer output:

Critical: SKILL.md:1 - Missing required 'name' field in frontmatter
Major: SKILL.md:3 - Description uses second person ("you should use")
Major: Missing "When NOT to Use" section
Minor: Line 45 is verbose


Fixes applied:

Added name field to frontmatter
Rewrote description in third person
Added "When NOT to Use" section

Iteration 2 — run skill-reviewer again to verify fixes:

Minor: Line 45 is verbose


Minor issue evaluation: Line 45 communicates effectively as-is. The verbosity provides useful context. Skip.

All critical/major issues resolved. Output the completion marker:

<skill-improvement-complete>


Note: The marker MUST appear in the output. Statements like "quality bar met" or "looks good" will NOT stop the loop.

Completion Criteria

CRITICAL: The stop hook ONLY checks for the explicit marker below. No other signal will terminate the loop.

Output this marker when done:

<skill-improvement-complete>


When to output the marker:

skill-reviewer reports "Pass" or no issues found → output marker immediately
All critical and major issues are fixed AND you've verified the fixes → output marker
Remaining issues are only minor AND you've evaluated them as false positives or not worth fixing → output marker

When NOT to output the marker:

Any critical issue remains unfixed
Any major issue remains unfixed
You haven't run skill-reviewer to verify your fixes worked

The marker is the ONLY way to complete the loop. Natural language like "looks good" or "quality bar met" will NOT stop the loop.

Rationalizations to Reject
"I'll just mark it complete and come back later" - Fix issues now
"This minor issue seems wrong, I'll skip all of them" - Evaluate each one individually
"The reviewer is being too strict" - The quality bar exists for a reason
"It's good enough" - If there are major issues, it's not good enough
Weekly Installs
1.5K
Repository
trailofbits/skills
GitHub Stars
5.0K
First Seen
1 day ago
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass