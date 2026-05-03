---
rating: ⭐⭐⭐⭐
title: reviewing-claude-config
url: https://skills.sh/bitwarden/ai-plugins/reviewing-claude-config
---

# reviewing-claude-config

skills/bitwarden/ai-plugins/reviewing-claude-config
reviewing-claude-config
Installation
$ npx skills add https://github.com/bitwarden/ai-plugins --skill reviewing-claude-config
SKILL.md
Reviewing Claude Configuration
Instructions

IMPORTANT: Use structured thinking throughout your review process. Plan your analysis before providing feedback. This improves accuracy and catches critical security issues.

Step 1: Detect File Type

Determine the primary file type(s) being reviewed:

Detection Rules:

Agents: Changes to .claude/agents/*.md or plugins/*/agents/*.md
Skills: Changes to skill.md files or skill support files (checklists, references, examples)
CLAUDE.md: Changes to CLAUDE.md files (any location: project root, .claude/, or subdirectories)
Prompts/Commands: Changes to .claude/prompts/*.md or .claude/commands/*.md
Settings: Changes to .claude/settings.json or .claude/settings.local.json

If multiple types modified, review each with appropriate checklist.

Step 2: Execute Security Scan (ALWAYS)

CRITICAL CHECKS (perform for ALL Claude config reviews):

Run these mental checks immediately:

 settings.local.json NOT in git (check changed files list)
 No hardcoded credentials in any modified files
 Permissions scoped appropriately (if settings.json modified)
 No API keys, tokens, or passwords in plaintext

If ANY security issue found: Flag as CRITICAL immediately, stop and report.

Consult reference/security-patterns.md for detailed security checks and detection commands.

Step 3: Load Appropriate Checklist

Based on detected file type, read and follow the relevant checklist:

Agents → checklists/agents.md (YAML, tool access security, model selection, system prompts)
Skills → checklists/skills.md (structure, YAML, progressive disclosure, quality)
CLAUDE.md → checklists/claude-md.md (clarity, references, no duplication)
Prompts/Commands → checklists/prompts.md (purpose, session context, skill references)
Settings → checklists/settings.md (security, permissions scoping)

The checklist provides:

Multi-pass review strategy
What to check and what to skip
Structured thinking guidance
Common issues and red flags
Step 4: Consult Reference Materials As Needed

Load reference files only when needed for specific questions:

Issue prioritization → reference/priority-framework.md (CRITICAL vs IMPORTANT vs SUGGESTED vs OPTIONAL)
Security patterns → reference/security-patterns.md (detection commands, fix examples)
Claude Code requirements → reference/claude-code-requirements.md (YAML frontmatter, model selection, tool names, progressive disclosure, settings conventions)
Step 5: Document Findings

This section defines the standard output format for ALL Claude config reviews. Checklists reference this section rather than duplicating content.

CRITICAL: Use inline comments on specific lines, NOT one large summary comment.

Inline Comment Rules:

Create separate comment for EACH specific issue on the exact line
Do NOT create one large summary comment with all issues
Do NOT update existing comments - always create new comments
Include specific fix with code example when applicable
Explain rationale (why this matters)

Comment Format:

**[file:line]** - [PRIORITY]: [Issue description]

[Specific fix with code example if applicable]

[Rationale explaining why this matters]

Reference: [documentation link if applicable]


Example inline comment:

**.claude/skills/my-skill/skill.md:1** - CRITICAL: Missing YAML frontmatter

Skills require YAML frontmatter to be discoverable by Claude Code:

\```yaml
---
name: my-skill
description: Clear description with activation triggers
---
\```

Without frontmatter, the skill won't be recognized by Claude Code.

Reference: Anthropic Skills Documentation


When to use inline vs summary:

Inline comment: Specific issue, recommendation, or question (use file:line format)
Summary comment: Overall assessment, recommendation (APPROVE or REQUEST CHANGES)

Load the specific example relevant to your file type (on-demand only, not upfront):

Agents → examples/example-agent-review.md
Skills → examples/example-skill-review.md
CLAUDE.md → examples/example-claude-md-review.md
Settings → examples/example-settings-review.md
Prompts → examples/example-prompts-review.md
Cross-Plugin Enrichment
Enhanced Secret Detection (bitwarden-security-engineer plugin)

When the bitwarden-security-engineer plugin is installed, supplement the manual security scan above with:

Comprehensive secret patterns → activate Skill(detecting-secrets) for context-aware detection that distinguishes test fixtures from production secrets, and covers patterns beyond the manual checks above (connection strings, private keys, cloud provider tokens)

This skill is optional. If unavailable, rely on the manual security checks above.

Core Principles
Security first: Always check for committed settings, secrets, overly broad permissions
Structure matters: YAML frontmatter, file references, progressive disclosure, line limits
Quality counts: Clear instructions, examples, proper emphasis, structured thinking
Token efficiency: Progressive disclosure, appropriate file sizes, on-demand loading
Actionable feedback: Say what to do and why, not just what's wrong
Constructive tone: Focus on code/config, not people; explain rationale
Weekly Installs
41
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