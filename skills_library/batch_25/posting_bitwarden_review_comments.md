---
title: posting-bitwarden-review-comments
url: https://skills.sh/bitwarden/ai-plugins/posting-bitwarden-review-comments
---

# posting-bitwarden-review-comments

skills/bitwarden/ai-plugins/posting-bitwarden-review-comments
posting-bitwarden-review-comments
Installation
$ npx skills add https://github.com/bitwarden/ai-plugins --skill posting-bitwarden-review-comments
SKILL.md
Posting Bitwarden Review Comments
GitHub Comment Posting Protocol
MUST Analyze all changes before posting anything
MUST Use inline comments for code-specific findings
MUST Use the Bitwarden finding format
FORBIDDEN: Do NOT add "Strengths", "Highlights", or positive observations sections.
FORBIDDEN Do NOT post praise-only inline comments
FORBIDDEN: Do NOT post PR metadata issues (title, description, test plan) as inline comments. These go in the summary only.
Finding Format

CRITICAL: Never use # followed by numbers - GitHub will autolink it to unrelated issues/PRs.

Writing "#1" creates a clickable link to issue/PR #1 (not your finding)
"Issue" is also wrong terminology (use "Finding")
Use "Finding" + space + number (no # symbol); aim for under 30 words in sentence

CORRECT FORMAT:

Finding 1: Memory leak detected
Finding 2: Missing error handling

WRONG (DO NOT USE):

❌ Issue #1 (wrong term + autolink)
❌ #1 (autolink only)
❌ Issue 1 (wrong term only)
Inline Comments

Every inline comment MUST:

Reference specific line(s)
State the problem - what breaks or what's the risk?
Provide actionable fix (for ❌ and ⚠️)
Be brief yet clear
Use collapsed sections for comments over 5 lines
Include both opening <details> AND closing </details> tags

Visibility Rule: Only severity + one-line description visible; everything else inside <details> tags.

Template for long comments
[emoji] **[SEVERITY]**: [One-line issue description]

<details>
<summary>Details and fix</summary>

[Code example or specific fix]

[Rationale explaining why]

Reference: [docs link if applicable]
</details>

Summary Output

Invoke Skill(posting-review-summary) for all summary formatting and posting.

Weekly Installs
36
Repository
bitwarden/ai-plugins
GitHub Stars
90
First Seen
Feb 13, 2026
Security Audits
Gen Agent Trust HubPass
SocketPass
SnykPass